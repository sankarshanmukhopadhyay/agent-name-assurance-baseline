# Annex J — DPI AI Risk Tier ↔ Agent Name Assurance Crosswalk

This annex provides **non-normative** guidance for integrating the Agent Name Assurance Baseline (ANAB) with the DPI AI Governance repositories (Lab + Artifacts).

## Purpose

- Keep **identity assurance** (ANAB) and **AI governance** (DPI AI) as **separate, composable layers**
- Provide a practical **mapping** so adopters can select the minimum agent identity assurance level based on DPI AI risk tiering
- Avoid duplicating ANAB threat annexes or conformance ladder semantics in DPI AI repos

## Crosswalk (working default)

The table below expresses a **minimum** ANAB assurance level expectation for an acting agent used in a DPI AI context.

| DPI AI risk tier | Typical context characteristics | Minimum agent identity assurance | ANAB level | Why this exists |
|---|---|---:|---:|---|
| Tier 0 — Informational | Advisory, non-decisional, no binding authority | Basic namespace binding | AL1 | Prevent trivial impersonation and name collision |
| Tier 1 — Operational support | Assists workflows; limited blast radius | Registry-backed identity + basic audit trail | AL2 | Reduce spoofing/misbinding; enable accountability |
| Tier 2 — Decision-influencing | Impacts outcomes; public/financial consequences | Strong cryptographic binding + reviewable provenance | AL3 | Require traceability and stronger operator controls |
| Tier 3 — Public authority / high impact | Delegated authority; high harm potential | High-assurance identity + revocation guarantees + supervisory binding | AL4 | Identity failure becomes systemic harm |

## Implementation guidance

- DPI AI repositories SHOULD reference ANAB (or an equivalent baseline) rather than copying its annex set.
- DPI AI controls SHOULD express identity requirements using a tier-to-assurance mapping (machine-readable where possible).
- Where a deployment uses multiple agents, the **highest applicable tier** SHOULD drive the minimum required identity assurance level.

## Notes

- This mapping is intentionally conservative and is meant as a **portable default**.
- If your DPI AI tiering model differs, maintain the tier labels but update the “context characteristics” and “minimum level” accordingly.
