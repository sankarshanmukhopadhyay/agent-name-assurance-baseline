#!/usr/bin/env python3
"""
Repo validation for ANAGB.

Runs fast, deterministic checks:
- JSON Schema validation for the sample conformance declaration
- Control ID consistency across spec, checklist, and sample
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]


def read_text(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def load_json(rel: str) -> dict:
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def extract_control_ids_from_spec(spec_text: str) -> set[str]:
    # Control IDs are rendered in backticks inside the control table.
    return set(re.findall(r"`(ANAGB-[A-Z]+-\d{2})`", spec_text))


def extract_control_ids_from_checklist(checklist_text: str) -> set[str]:
    return set(re.findall(r"\b(ANAGB-[A-Z]+-\d{2})\b", checklist_text))


def main() -> int:
    spec = read_text("spec/agent-name-assurance-baseline.md")
    checklist = read_text("conformance/checklist.md")
    schema = load_json("conformance/conformance-declaration.schema.json")
    sample = load_json("conformance/sample-conformance-declaration.json")

    spec_controls = extract_control_ids_from_spec(spec)
    checklist_controls = extract_control_ids_from_checklist(checklist)
    sample_controls = set(sample.get("controls", {}).keys())

    # 1) JSON schema validation
    jsonschema.validate(instance=sample, schema=schema)

    # 2) Checklist should mention every spec control (even if "recommended")
    missing_in_checklist = sorted(spec_controls - checklist_controls)
    if missing_in_checklist:
        print("ERROR: Checklist missing control IDs:", ", ".join(missing_in_checklist), file=sys.stderr)
        return 2

    # 3) Sample should not claim controls that don't exist in the spec
    unknown_in_sample = sorted(sample_controls - spec_controls)
    if unknown_in_sample:
        print("ERROR: Sample declares unknown control IDs:", ", ".join(unknown_in_sample), file=sys.stderr)
        return 3

    print("OK: schema valid; controls consistent.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
