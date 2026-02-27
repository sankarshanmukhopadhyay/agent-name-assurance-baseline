# Annex D — ISO 27001/27002 alignment

## Purpose

This annex positions ANAGB artifacts as inputs into an ISO/IEC 27001-aligned ISMS, improving procurement and audit interoperability for enterprises and governments.

- Treat evidence bundle artifacts as **ISMS evidence** (policies, risk treatment plans, monitoring, incident response).
- Use AL3/AL4 evidence expectations to decide when **formal attestation** and stronger operational controls are warranted.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/iso-27001-27002.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| Evidence bundle governance/risk artifacts | ISO 27001 ISMS documentation | Policy + risk treatment artifacts map cleanly. |
| Operational runbooks + monitoring | ISO 27002 operational controls | Runbooks and monitoring evidence support ongoing control operation. |
| Attestations (AL3/AL4) | ISMS internal/external audit evidence | Attach audit outputs and findings closure records. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
