# Annex G — Privacy alignment (ISO 27701 + GDPR concepts)

## Purpose

This annex helps implementers and reviewers map ANAGB privacy expectations into common privacy management and accountability frameworks.

- Use ISO 27701 (PIMS) concepts for privacy governance artifacts in evidence bundles.
- Use GDPR concepts as a practical checklist for transparency, minimization, and rights handling where applicable.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/privacy.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| Privacy governance + risk artifacts | ISO 27701 PIMS | Maps to policies, roles, DPIA-like artifacts, and reviews. |
| Delegated and public-facing agents (AL3/AL4) | GDPR-style accountability | Transparency, lawful basis, rights handling, and security of processing. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
