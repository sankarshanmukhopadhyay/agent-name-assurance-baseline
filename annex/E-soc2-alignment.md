# Annex E — SOC 2 alignment (Trust Services Criteria)

## Purpose

This annex helps startups and service providers map ANAGB evidence and operational controls into SOC 2-style expectations used by customers and auditors.

- Use AL2 as a practical baseline for SOC 2 **Security** readiness.
- Use AL3/AL4 to justify broader SOC 2 scope (Availability/Confidentiality/Privacy) when the deployment requires it.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/soc2-tsc.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| AL2 operational + security evidence | SOC 2 Security (Common Criteria) | Baseline bar for service trust. |
| AL3 ops + risk + attestation | SOC 2 expanded criteria | Broader operational and evidence maturity. |
| AL4 multi-domain assurance | SOC 2 full TSC (context) | High assurance deployments map to broader TSC domains. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
