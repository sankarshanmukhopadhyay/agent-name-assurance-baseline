# Portfolio Drift Review: AIS-1 v0.2 to ANAB v0.10.0

| Field | Value |
|---|---|
| Source standard | AIS-1 Agent Identity Standard |
| Source version | v0.2 draft for comment |
| Reviewed repo | agent-name-assurance-baseline |
| Target release | v0.10.0 |
| Review date | 2026-07-03 |
| Drift classification | Standards drift, artifact drift, assurance drift |

## Changed Surfaces

- `agentClass` introduces ALA and SOA distinction.
- `parentDid` introduces machine-readable SOA accountability chains.
- DID resolution and registry publication become explicit verifier inputs.
- `timestampServiceRef` replaces the earlier service-specific timestamp field.
- SOA revocation cascades from parent ALA revocation.
- Assurance Container introduces append-only attestations alongside the immutable bond.

## Relationship Review

| Source | Target | Relationship | Impact | Evidence |
|---|---|---|---|---|
| trust-systems-meta-model | ANAB | informs | Preserve AIS-1 as identity and accountability, not delegation | `profiles/ais1/anab-profile.md` |
| trust-infrastructure-schemas | ANAB | drift_sensitive_to | Align ANAB with TIS v0.10 runtime assurance artifacts | `model/tis-compatibility-review.json` |
| AIS-1 v0.2 | ANAB | binds_to | Add relying-party interpretation for ALA/SOA, parent state, registry status, and timestamp evidence | `conformance/ais1-v0.2-profile-extension.schema.json` |
| ANAB | DCAS | produces_evidence_for | Provide declarations and extension evidence that DCAS can evaluate | `conformance/samples/tis-v0.10-backed-enterprise-agent.json` |

## Decision

ANAB v0.10.0 should adopt AIS-1 v0.2 as an experimental interpretation profile only. The release must not promote AIS-1 bond existence, tier, DID resolution, or registry status into proof of delegated authority, runtime authorization, or message provenance.

## Required Evidence

- Updated TIS v0.10 compatibility review.
- Updated AIS-1 interpretation profile.
- Optional AIS-1 v0.2 extension schema.
- ALA and SOA extension examples.
- TIS v0.10-backed ANAB sample declaration.
- Validation tool coverage for new schema and examples.
