#!/usr/bin/env python3
"""Validate the experimental ANAB assurance gate for A2A v1.0 Agent Cards."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance" / "a2a-v1.0" / "vectors"
EXTENSION_URI = "https://trustoverip.github.io/dtgwg-agent-names-tf/extensions/anab-description/v1"


def evaluate(vector: dict) -> str:
    extension = vector.get("extension")
    if extension is None:
        return "continue-without-anab" if not vector.get("anab_required") else "deny-missing-required-extension"
    if extension.get("uri") != EXTENSION_URI:
        return "deny-extension-identifier"
    if extension.get("required") and not vector.get("client_understands_extension", True):
        return "deny-unsupported-required-extension"

    params = extension.get("params", {})
    if params.get("anabVersion") != "0.10.0":
        return "deny-version"
    if params.get("agentName", {}).get("displayName") != vector.get("card_name"):
        return "deny-name-mismatch"

    freshness = params.get("freshness", {})
    evaluated_at = datetime.fromisoformat(vector["evaluated_at"].replace("Z", "+00:00"))
    expires_at = freshness.get("expiresAt")
    if expires_at and datetime.fromisoformat(expires_at.replace("Z", "+00:00")) <= evaluated_at:
        return "deny-stale"

    identity = params.get("identityVerification", {})
    if identity.get("status") in {"revoked", "suspended"}:
        return "deny-identity-status"
    if identity.get("status") == "verified":
        required = (
            params.get("operator", {}).get("operatorId"),
            identity.get("verificationUri"),
            identity.get("revocationCheck") == "required",
            params.get("declaration", {}).get("sha256"),
            params.get("cardBinding", {}).get("kid"),
            params.get("cardBinding", {}).get("verificationMaterialUri"),
        )
        if not all(required):
            return "deny-incomplete-verified-claim"

    if vector.get("consequential") and not params.get("authorityBoundary", {}).get("delegationRequired"):
        return "deny-authority-boundary"
    return "allow-assurance-evaluation"


def run() -> tuple[int, int]:
    manifest = json.loads((VECTORS / "manifest.json").read_text(encoding="utf-8"))
    passed = 0
    for entry in manifest["vectors"]:
        vector = json.loads((VECTORS / entry["file"]).read_text(encoding="utf-8"))
        observed = evaluate(vector)
        ok = observed == entry["expected"]
        print(f"[{'OK' if ok else 'FAIL'}] {entry['id']}: {observed}")
        passed += int(ok)
    return passed, len(manifest["vectors"])


if __name__ == "__main__":
    passed, total = run()
    print(f"ANAB A2A assurance vectors: {passed}/{total} OK")
    raise SystemExit(0 if passed == total else 1)
