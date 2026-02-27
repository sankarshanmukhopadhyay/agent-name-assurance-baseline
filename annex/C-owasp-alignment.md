# Annex C — OWASP alignment (ASVS + API Top 10)

## Purpose

This annex helps reviewers and implementers align ANAGB assurance expectations with widely used OWASP verification baselines for applications and APIs.

- Use **ASVS** to select a verification depth that matches AL2/AL3/AL4 expectations.
- Use **OWASP API Security Top 10** to drive API-focused threat modeling and test coverage for agent endpoints.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/owasp-asvs.yml`
- Machine-readable crosswalk: `crosswalk/owasp-api-top10.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| AL2 security + testing evidence | ASVS Level 1 | Baseline verification and test evidence expected. |
| AL3 security + attestation evidence | ASVS Level 2 | Stronger verification depth and more robust evidence. |
| AL4 security + risk evidence | ASVS Level 3 | Highest assurance environments; targeted attack resistance. |
| Threat model + API tests | OWASP API Top 10 | Ensure agent-facing APIs cover common API failures. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
