#!/usr/bin/env python3
"""
Repo validation for ANAGB.

Runs fast, deterministic checks:
- JSON Schema validation for conformance declarations (all samples)
- JSON Schema validation for evidence bundles (all examples)
- Control ID consistency across spec, checklist, and all sample declarations
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def iter_json_files(dir_rel: str) -> Iterable[Path]:
    base = ROOT / dir_rel
    if not base.exists():
        return []
    return sorted([p for p in base.rglob("*.json") if p.is_file()])


def extract_control_ids_from_spec(spec_text: str) -> set[str]:
    # Control IDs are rendered in backticks inside the control tables.
    return set(re.findall(r"`(ANAGB-[A-Z]+-\d{2})`", spec_text))


def extract_control_ids_from_checklist(checklist_text: str) -> set[str]:
    return set(re.findall(r"\b(ANAGB-[A-Z]+-\d{2})\b", checklist_text))


def validate_json(schema: dict, instance: dict, label: str) -> None:
    try:
        jsonschema.validate(instance=instance, schema=schema)
    except jsonschema.ValidationError as e:
        # Machine-consumable-ish output: path + message
        path = "/".join([str(p) for p in e.path]) or "(root)"
        raise RuntimeError(f"{label}: schema validation error at {path}: {e.message}") from e




def validate_crosswalk_registry() -> list[str]:
    errors: list[str] = []
    cw_dir = ROOT / "crosswalk"
    if not cw_dir.exists():
        return errors

    required_top = {"standard_id", "standard_name", "standard_version", "scope", "mappings"}

    for p in sorted(cw_dir.glob("*.yml")):
        try:
            doc = yaml.safe_load(p.read_text(encoding="utf-8"))
        except Exception as e:
            errors.append(f"[crosswalk] {p.name}: YAML parse error: {e}")
            continue

        if not isinstance(doc, dict):
            errors.append(f"[crosswalk] {p.name}: expected a mapping/object at top level")
            continue

        missing = required_top - set(doc.keys())
        if missing:
            errors.append(f"[crosswalk] {p.name}: missing keys: {sorted(missing)}")
            continue

        if not isinstance(doc.get("mappings"), list) or len(doc["mappings"]) < 1:
            errors.append(f"[crosswalk] {p.name}: 'mappings' must be a non-empty list")
            continue

        # lightweight checks for mapping entries
        for j, entry in enumerate(doc["mappings"]):
            if not isinstance(entry, dict):
                errors.append(f"[crosswalk] {p.name}: mapping[{j}] must be an object")
                continue
            if "anagb" not in entry or "external" not in entry:
                errors.append(f"[crosswalk] {p.name}: mapping[{j}] must include 'anagb' and 'external'")
                continue

    return errors

def main() -> int:
    spec = read_text("spec/agent-name-assurance-baseline.md")
    checklist = read_text("conformance/checklist.md")

    conformance_schema = load_json("conformance/conformance-declaration.schema.json")
    evidence_schema = load_json("evidence-bundles/evidence-bundle.schema.json")

    spec_controls = extract_control_ids_from_spec(spec)
    checklist_controls = extract_control_ids_from_checklist(checklist)

    # 1) Checklist should mention every spec control (even if "recommended")
    missing_in_checklist = sorted(spec_controls - checklist_controls)
    if missing_in_checklist:
        print("ERROR: Checklist missing control IDs:", ", ".join(missing_in_checklist), file=sys.stderr)
        return 2

    # 2) Validate conformance declarations (canonical + samples)
    conformance_files = [ROOT / "conformance" / "sample-conformance-declaration.json"]
    conformance_files += list(iter_json_files("conformance/samples"))
    all_sample_controls: set[str] = set()

    for f in conformance_files:
        inst = json.loads(f.read_text(encoding="utf-8"))
        validate_json(conformance_schema, inst, f"Conformance declaration {f.relative_to(ROOT)}")
        declared_controls = set(inst.get("controls", {}).keys())
        all_sample_controls |= declared_controls
        unknown = sorted(declared_controls - spec_controls)
        if unknown:
            print(f"ERROR: {f.relative_to(ROOT)} declares unknown control IDs: {', '.join(unknown)}", file=sys.stderr)
            return 3

    # 3) Validate evidence bundles (examples)
    bundle_files = list(iter_json_files("evidence-bundles/examples"))
    if not bundle_files:
        print("ERROR: No evidence bundle examples found.", file=sys.stderr)
        return 4

    for f in bundle_files:
        inst = json.loads(f.read_text(encoding="utf-8"))
        validate_json(evidence_schema, inst, f"Evidence bundle {f.relative_to(ROOT)}")

    print("OK: schemas valid; controls consistent; bundles valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
