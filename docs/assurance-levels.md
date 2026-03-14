# Assurance Levels (AL1–AL4)

This repository defines two primary axes for Agent Name Assurance:

- **Name-binding tiers:** **AN-0 … AN-3** (how strong the name ↔ identifier binding is)
- **Operational profiles:** **Core / Deploy / Transact / Enterprise** (what the deployment is allowed to do)

Assurance Levels add a third, complementary axis:

- **Assurance Levels (AL1–AL4):** the maturity and auditability of the overall deployment and its conformance claim.

## Normative source

The **canonical definition** of AL1–AL4 lives in the `trust-infrastructure-schemas` repository as part of the Open Trust Artifact Model (OTAM) at `assurance/assurance-levels.md`.

This document focuses on **how ANAB uses AL** (operational expectations and mapping), and intentionally avoids re-defining AL semantics.

## How to think about the three axes

- **AN-x** answers: *How strong is the name ↔ identifier binding and anti-impersonation posture?*
- **Profile** answers: *What operational capabilities are enabled and what safeguards are required?*
- **AL** answers: *How reviewable and audit-ready is the conformance claim and evidence package?*

In practice, AN-x and Profile determine **what controls apply**. AL determines **how strongly you must substantiate** that those controls are met.

## Practical expectations by AL (ANAB guidance)

| Assurance Level | What “good” looks like for ANAB deployments |
| --- | --- |
| AL1 | Evidence bundle is complete and internally consistent. Policies and attestations exist, but verification is limited. |
| AL2 | Evidence is verifiable where it matters: cryptographic integrity, provenance, identifier binding, audit logs retained. |
| AL3 | Independent review is present for high-risk controls. Remediation closure is documented and traceable. |
| AL4 | Continuous assurance: monitoring, audit-grade logs, recurring assessment, and strong governance controls. |

## Recommended mapping (rule of thumb)

This is not a hard constraint, but it is a useful procurement and governance heuristic:

- **AN-0 / Core:** typically achievable at **AL1–AL2**
- **AN-1 / Deploy:** typically **AL2** (and AL3 for higher exposure)
- **AN-2 / Transact:** typically **AL3** minimum
- **AN-3 / Enterprise:** typically **AL3–AL4**

If an issuer claims a high tier/profile at a low AL, verifiers SHOULD treat that as a risk signal and require additional evidence or remediation commitments.

## Where AL appears in ANAB conformance

- Machine-checkable conformance declarations SHOULD include an explicit `assurance_level`.
- Evidence bundles SHOULD justify the declared AL with references to artifacts and verification outputs.
- Verifiers SHOULD report both the **declared AL** and the **achieved AL** after review.

