#!/usr/bin/env python3
"""Experimental admission to assurance evaluation; never action authorization."""
import json
from datetime import datetime
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance/a2a-v1.0/vectors"
EXTENSION_URI = "https://trustoverip.github.io/dtgwg-agent-names-tf/extensions/anab-description/v1"


def timestamp(value):
    if not isinstance(value, str) or not FormatChecker().conforms(value, "date-time"):
        raise ValueError("invalid timestamp")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("timezone required")
    return result


def evaluate(vector):
    checker = FormatChecker()
    if not {"date-time", "uri"} <= checker.checkers.keys():
        raise RuntimeError("install requirements-ci.txt for format validation")
    if not isinstance(vector, dict) or any(key in vector and type(vector[key]) is not bool
            for key in ("anab_required", "client_understands_extension", "consequential")):
        return "deny-invalid-input"
    extension = vector.get("extension")
    if extension is None:
        return "continue-without-anab" if not vector.get("anab_required") else "deny-missing-required-extension"
    if not isinstance(extension, dict) or type(extension.get("required")) is not bool:
        return "deny-invalid-extension"
    if extension.get("uri") != EXTENSION_URI:
        return "deny-extension-identifier"
    if extension["required"] and not vector.get("client_understands_extension", True):
        return "deny-unsupported-required-extension"
    params = extension.get("params")
    schema = json.loads((ROOT / "conformance/anab-over-a2a-description-extension.schema.json").read_text())
    if not Draft202012Validator(schema, format_checker=checker).is_valid(params):
        return "deny-invalid-extension"
    if params["anabVersion"] != "0.10.0":
        return "deny-version"
    if not isinstance(vector.get("card_name"), str) or not vector["card_name"].strip():
        return "deny-invalid-input"
    if params["agentName"]["displayName"] != vector["card_name"]:
        return "deny-name-mismatch"
    try:
        evaluated_at = timestamp(vector.get("evaluated_at"))
        freshness = params["freshness"]
        issued = timestamp(freshness["issuedAt"])
        expires = timestamp(freshness["expiresAt"]) if "expiresAt" in freshness else None
    except (ValueError, TypeError):
        return "deny-invalid-input"
    if expires is not None and expires <= issued:
        return "deny-invalid-freshness"
    if issued > evaluated_at:
        return "deny-future-issuance"
    if expires is not None and expires <= evaluated_at:
        return "deny-stale"
    max_age = freshness.get("maxCacheAgeSeconds")
    if max_age is not None and (evaluated_at - issued).total_seconds() > max_age:
        return "deny-stale"
    identity = params.get("identityVerification", {})
    if identity.get("status") in {"revoked", "suspended"}:
        return "deny-identity-status"
    if identity.get("status") == "verified":
        required = (params.get("operator", {}).get("operatorId"), identity.get("verificationUri"),
                    identity.get("revocationCheck") == "required", params["declaration"].get("sha256"),
                    params["cardBinding"].get("kid"), params["cardBinding"].get("verificationMaterialUri"))
        if not all(required):
            return "deny-incomplete-verified-claim"
        # Bounded local admission policy: a verified claim needs an explicit freshness bound.
        if expires is None and max_age is None:
            return "deny-freshness-unestablished"
    if vector.get("consequential") and params["authorityBoundary"].get("delegationRequired") is not True:
        return "deny-authority-boundary"
    return "allow-assurance-evaluation"


def run():
    manifest = json.loads((VECTORS / "manifest.json").read_text())
    entries = manifest["vectors"]
    if not entries or len({e["id"] for e in entries}) != len(entries) or len({e["file"] for e in entries}) != len(entries):
        raise ValueError("empty or duplicate vector manifest")
    if {e["file"] for e in entries} != {p.name for p in VECTORS.glob("*.json") if p.name != "manifest.json"}:
        raise ValueError("untracked or missing vector")
    if not any(e["expected"] == "allow-assurance-evaluation" for e in entries) or not any(e["expected"].startswith("deny-") for e in entries):
        raise ValueError("positive and negative coverage required")
    passed = 0
    for entry in entries:
        vector = json.loads((VECTORS / entry["file"]).read_text())
        observed = evaluate(vector)
        ok = observed == entry["expected"]
        print(f"[{'OK' if ok else 'FAIL'}] {entry['id']}: {observed}")
        passed += int(ok)
    return passed, len(entries)


if __name__ == "__main__":
    passed, total = run()
    print(f"ANAB A2A assurance vectors: {passed}/{total} OK")
    raise SystemExit(0 if passed == total else 1)
