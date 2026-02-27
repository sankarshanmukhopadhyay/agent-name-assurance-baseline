# Annex H — AI governance alignment (ISO 42001, ISO 23894, OECD, EU AI Act pointers)

## Purpose

This annex connects ANAGB AI safeguards, risk management, and evidence expectations to major AI governance standards and policy frameworks.

- Use ISO 42001 to organize governance, roles, monitoring, and continual improvement evidence.
- Use ISO 23894 concepts to structure AI risk identification, assessment, and treatment.
- Use OECD and EU AI Act pointers as a lens for AL3/AL4 transparency and robustness expectations.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/ai-governance.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| AI governance + monitoring evidence | ISO 42001 AIMS | Management system framing for AI controls. |
| AI risk artifacts | ISO 23894 | Risk lifecycle structure and documentation. |
| AL3/AL4 AI testing + attestation | OECD / EU AI Act pointers | Higher assurance transparency and robustness posture. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
