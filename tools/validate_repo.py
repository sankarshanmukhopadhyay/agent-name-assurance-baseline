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

import yaml

try:
    import jsonschema  # type: ignore
except ModuleNotFoundError:  # pragma: no cover - exercised in constrained local runtimes.
    jsonschema = None


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
    return set(re.findall(r"`(ANAGB-[A-Z0-9]+-\d{2})`", spec_text))


def extract_control_ids_from_checklist(checklist_text: str) -> set[str]:
    return set(re.findall(r"\b(ANAGB-[A-Z0-9]+-\d{2})\b", checklist_text))


def validate_json(schema: dict, instance: dict, label: str) -> None:
    if jsonschema is not None:
        try:
            jsonschema.validate(instance=instance, schema=schema)
        except jsonschema.ValidationError as e:
            path = "/".join([str(p) for p in e.path]) or "(root)"
            raise RuntimeError(f"{label}: schema validation error at {path}: {e.message}") from e
        return

    _minimal_json_schema_validate(instance, schema, label)


def _matches_type(instance: object, expected: object) -> bool:
    if isinstance(expected, list):
        return any(_matches_type(instance, item) for item in expected)
    if expected == "object":
        return isinstance(instance, dict)
    if expected == "array":
        return isinstance(instance, list)
    if expected == "string":
        return isinstance(instance, str)
    if expected == "integer":
        return isinstance(instance, int) and not isinstance(instance, bool)
    if expected == "number":
        return isinstance(instance, (int, float)) and not isinstance(instance, bool)
    if expected == "boolean":
        return isinstance(instance, bool)
    if expected == "null":
        return instance is None
    return True


def _schema_condition_matches(instance: object, schema: dict) -> bool:
    props = schema.get("properties") or {}
    if not isinstance(instance, dict):
        return False
    for key, subschema in props.items():
        if key not in instance:
            return False
        if "const" in subschema and instance[key] != subschema["const"]:
            return False
        if "enum" in subschema and instance[key] not in subschema["enum"]:
            return False
    return True


def _minimal_json_schema_validate(instance: object, schema: dict, label: str, path: str = "(root)") -> None:
    expected_type = schema.get("type")
    if expected_type is not None and not _matches_type(instance, expected_type):
        raise RuntimeError(f"{label}: fallback schema validation error at {path}: expected {expected_type}")

    if "const" in schema and instance != schema["const"]:
        raise RuntimeError(f"{label}: fallback schema validation error at {path}: expected {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        raise RuntimeError(f"{label}: fallback schema validation error at {path}: value {instance!r} not in enum {schema['enum']}")
    if "pattern" in schema and isinstance(instance, str) and not re.match(schema["pattern"], instance):
        raise RuntimeError(f"{label}: fallback schema validation error at {path}: value {instance!r} does not match pattern {schema['pattern']}")

    if "allOf" in schema:
        for idx, subschema in enumerate(schema["allOf"]):
            if "if" in subschema and "then" in subschema:
                if _schema_condition_matches(instance, subschema["if"]):
                    _minimal_json_schema_validate(instance, subschema["then"], label, f"{path}.allOf[{idx}].then")
            else:
                _minimal_json_schema_validate(instance, subschema, label, f"{path}.allOf[{idx}]")

    if isinstance(instance, dict):
        required = schema.get("required") or []
        missing = [key for key in required if key not in instance]
        if missing:
            raise RuntimeError(f"{label}: fallback schema validation error at {path}: missing required keys {missing}")

        props = schema.get("properties") or {}
        pattern_props = schema.get("patternProperties") or {}
        if schema.get("additionalProperties") is False:
            unknown = []
            for key in instance:
                if key in props:
                    continue
                if any(re.match(pattern, key) for pattern in pattern_props):
                    continue
                unknown.append(key)
            if unknown:
                raise RuntimeError(f"{label}: fallback schema validation error at {path}: unknown keys {unknown}")

        for key, value in instance.items():
            if key in props:
                _minimal_json_schema_validate(value, props[key], label, f"{path}/{key}")
                continue
            for pattern, subschema in pattern_props.items():
                if re.match(pattern, key):
                    _minimal_json_schema_validate(value, subschema, label, f"{path}/{key}")
                    break

    if isinstance(instance, list):
        item_schema = schema.get("items")
        if item_schema:
            for idx, item in enumerate(instance):
                _minimal_json_schema_validate(item, item_schema, label, f"{path}/{idx}")




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


def validate_tis_alignment_artifacts(spec_controls: set[str]) -> None:
    manifest_path = ROOT / "model" / "tis-compatibility-review.json"
    if not manifest_path.exists():
        raise RuntimeError("Missing model/tis-compatibility-review.json for TIS drift tracking.")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    required = {"aligned_to_tis_release", "reviewed_at", "review_status", "tracked_artifact_families", "drift_triggers"}
    missing = required - set(manifest.keys())
    if missing:
        raise RuntimeError(f"TIS compatibility review manifest missing keys: {sorted(missing)}")
    if manifest.get("aligned_to_tis_release") != "v0.10.0":
        raise RuntimeError("TIS compatibility review manifest must declare alignment to v0.10.0 for this release.")
    if not manifest.get("tracked_artifact_families"):
        raise RuntimeError("TIS compatibility review manifest must track at least one artifact family.")

    sample_path = ROOT / "conformance" / "samples" / "tis-v0.10-backed-enterprise-agent.json"
    if not sample_path.exists():
        raise RuntimeError("Missing TIS v0.10-backed enterprise agent sample.")
    sample = json.loads(sample_path.read_text(encoding="utf-8"))
    unknown = sorted(set(sample.get("controls", {}).keys()) - spec_controls)
    if unknown:
        raise RuntimeError(f"TIS-backed enterprise sample declares unknown control IDs: {', '.join(unknown)}")
    alignments = sample.get("standards_alignment", [])
    if not any(a.get("standard_id") == "TIS100" for a in alignments):
        raise RuntimeError("TIS v0.10-backed enterprise sample must include a TIS100 standards_alignment entry.")
    if not any(a.get("standard_id") == "DCAS100" for a in alignments):
        raise RuntimeError("TIS v0.10-backed enterprise sample must include a DCAS100 standards_alignment entry.")


def validate_ais1_v02_extension() -> None:
    schema = load_json("conformance/ais1-v0.2-profile-extension.schema.json")
    examples = [
        ROOT / "profiles" / "ais1" / "examples" / "ais1-v0.2-ala-extension.example.json",
        ROOT / "profiles" / "ais1" / "examples" / "ais1-v0.2-soa-extension.example.json",
    ]
    for path in examples:
        if not path.exists():
            raise RuntimeError(f"Missing AIS-1 v0.2 extension example: {path.relative_to(ROOT)}")
        validate_json(schema, json.loads(path.read_text(encoding="utf-8")), f"AIS-1 v0.2 extension {path.relative_to(ROOT)}")

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
    conformance_files += [
        f for f in iter_json_files("conformance/samples")
        if f.name not in {"a2a-agent-card-with-anab-extension.json", "oasf-anab-publication-profile.json"}
    ]
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

    # 4) Validate ANAB-over-A2A extension sample
    extension_schema = load_json("conformance/anab-over-a2a-description-extension.schema.json")
    a2a_sample = load_json("conformance/samples/a2a-agent-card-with-anab-extension.json")
    try:
        params = a2a_sample["capabilities"]["extensions"][0]["params"]
    except Exception as e:
        raise RuntimeError(f"A2A extension sample malformed: {e}") from e
    validate_json(extension_schema, params, "ANAB-over-A2A extension sample params")

    # 4a) Exercise cross-field, freshness, downgrade and non-implication rules
    # that JSON Schema alone cannot express.
    from validate_a2a_assurance import run as run_a2a_assurance
    a2a_passed, a2a_total = run_a2a_assurance()
    if a2a_passed != a2a_total:
        raise RuntimeError(f"ANAB A2A assurance vectors failed: {a2a_passed}/{a2a_total}")

    # 5) Validate TIS alignment manifest and sample
    validate_tis_alignment_artifacts(spec_controls)

    # 6) Validate AIS-1 v0.2 optional extension examples
    validate_ais1_v02_extension()

    # 7) Validate OASF publication profile sample
    oasf_profile_schema = load_json("conformance/oasf-anab-publication-profile.schema.json")
    oasf_profile_sample = load_json("conformance/samples/oasf-anab-publication-profile.json")
    validate_json(oasf_profile_schema, oasf_profile_sample, "OASF publication profile sample")

    print("OK: schemas valid; controls consistent; bundles valid; A2A binding and assurance vectors valid; TIS alignment valid; AIS-1 v0.2 extension valid; OASF publication profile valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
