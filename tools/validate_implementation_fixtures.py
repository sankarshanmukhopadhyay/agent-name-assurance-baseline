#!/usr/bin/env python3
"""Validate synthetic ANAB assessment inputs and compare independent DCAS CLI findings."""
import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "conformance/fixtures"
REQUIRED = {f"ANAB-FX-{n:03}" for n in range(1, 7)}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def unique(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load(raw):
    def invalid(value):
        raise ValueError(f"invalid JSON constant: {value}")
    return json.loads(raw, object_pairs_hook=unique, parse_constant=invalid)


def check(value, schema_name):
    checker = FormatChecker()
    require({"date-time", "uri"} <= checker.checkers.keys(), "install requirements-ci.txt")
    schema = load((PACK / schema_name).read_bytes())
    Draft202012Validator(schema, format_checker=checker).validate(value)


def normalize(raw):
    """Only observed fixture inputs flow into DCAS; no expected outcome is available here."""
    case = load(raw)
    check(case, "implementation-validation-case.schema.json")
    refs = {o["id"]: o for o in case["observations"]}
    require(len(refs) == len(case["observations"]), "duplicate observation")
    bound = {v for values in case["requirement_evidence"].values() for v in values}
    require(bound == set(refs), "missing or unused observation record")
    require(len({o["observation_ref"] for o in refs.values()}) == len(refs), "duplicate observation reference")
    digest = "sha256:" + hashlib.sha256(raw).hexdigest()
    return {"contract_version": "0.2", "evaluation_id": case["fixture_id"],
            "target": case["target"], "evaluation_time": case["evaluation_time"], "policy": case["policy"],
            "claim": {"fixture_id": case["fixture_id"], "requirements": list(case["requirement_evidence"]),
                      "requirement_evidence": case["requirement_evidence"],
                      "source_context": {"synthetic": True, "case_digest": digest,
                                         "observations": case["observations"]}},
            "evidence": [{"id": o["id"], "uri": o["observation_ref"], "status": o["status"],
                          "digest": digest} for o in case["observations"]]}


def aggregate(findings):
    return "FAIL" if "FAIL" in findings else "INDETERMINATE" if "INDETERMINATE" in findings else "PASS"


def validate_pack(pack=PACK):
    manifest = load((pack / "implementation-validation-manifest.json").read_bytes())
    check(manifest, "implementation-validation-manifest.schema.json")
    entries = manifest["fixtures"]
    ids = {f["id"] for f in entries}
    require(len(ids) == len(entries) and REQUIRED <= ids, "duplicate or missing required fixture")
    require({f["expected_outcome"] for f in entries} == {"PASS", "FAIL", "INDETERMINATE"}, "all outcomes required")
    require({f["input"] for f in entries} == {str(p.relative_to(pack)) for p in (pack / "cases").glob("*.json")}, "untracked/missing case")
    controls = set(re.findall(r"`(ANAGB-[A-Z0-9]+-\d{2})`", (ROOT / "spec/agent-name-assurance-baseline.md").read_text()))
    cases = []
    for fixture in entries:
        fid = fixture["id"]
        require(fixture["input"] == f"cases/{fid}.json", "case identity mismatch")
        document = normalize((pack / fixture["input"]).read_bytes())
        require(document["evaluation_id"] == fid, "case ID mismatch")
        reqs = set(fixture["requirements"])
        require(reqs <= controls and reqs == set(document["claim"]["requirements"]) == set(fixture["expected_findings"]), "requirement mismatch")
        require(aggregate(fixture["expected_findings"].values()) == fixture["expected_outcome"], "inconsistent expected aggregate")
        cases.append((fixture, document))
    return manifest, cases


def run(dcas, output):
    manifest, cases = validate_pack()
    revision = subprocess.check_output(["git", "-C", str(dcas), "rev-parse", "HEAD"], text=True).strip()
    require(revision == manifest["dcas"]["revision"], "DCAS revision mismatch")
    require(not subprocess.check_output(["git", "-C", str(dcas), "status", "--porcelain", "--untracked-files=all"], text=True).strip(), "DCAS checkout dirty")
    output.mkdir(parents=True, exist_ok=True)
    report = []
    for fixture, document in cases:
        fid = fixture["id"]
        source, result_path = output / f"{fid}.input.json", output / f"{fid}.result.json"
        source.write_text(json.dumps(document, indent=2) + "\n", encoding="utf-8")
        subprocess.run([sys.executable, str(dcas / "tools/dcas_evaluate.py"), str(source),
                        "--output", str(result_path), "--expect", fixture["expected_outcome"]], check=True)
        result = load(result_path.read_bytes())
        findings = {f["requirement"]: f["result"] for f in result["findings"]}
        require(len(findings) == len(result["findings"]) and findings == fixture["expected_findings"], f"{fid}: requirement outcome mismatch")
        require(result["evaluation_id"] == fid and result["contract_version"] == "0.2" and result["evaluator"]["version"] == "0.2.0", f"{fid}: result identity mismatch")
        for finding in result["findings"]:
            require(set(finding["evidence_ids"]) == set(document["claim"]["requirement_evidence"][finding["requirement"]]), f"{fid}: binding mismatch")
        report.append({"fixture": fid, "expected": fixture["expected_outcome"], "observed": result["decision"],
                       "findings": findings, "input_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                       "result_sha256": hashlib.sha256(result_path.read_bytes()).hexdigest()})
        print(f"[OK] {fid}: {result['decision']}")
    (output / "report.json").write_text(json.dumps({"synthetic": True, "dcas_revision": revision, "results": report}, indent=2) + "\n")
    return len(report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dcas", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if args.dcas is None:
        require(args.output is None, "--output requires --dcas")
        _, cases = validate_pack()
        print(f"Validated {len(cases)} synthetic fixture inputs; DCAS execution not performed")
    else:
        require(args.output is not None, "--dcas requires --output")
        run(args.dcas.resolve(), args.output.resolve())


if __name__ == "__main__":
    main()
