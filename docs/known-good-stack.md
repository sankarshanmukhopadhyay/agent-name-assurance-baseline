# Known-good stack

**Last reviewed:** 2026-07-03

| Component | Version | Role |
| --- | --- | --- |
| trust-systems-meta-model | v0.21.0 | Semantic governance model for authority, delegation, evidence, lifecycle state, and runtime decisions |
| trust-infrastructure-schemas | v0.10.0 | Canonical runtime assurance artifact schemas and compatibility matrix |
| dtg-conformance-assurance | v0.10.0 | Evaluation method for TIS-backed and AIS-1 v0.2-backed runtime evidence |
| agent-name-assurance-baseline | v0.10.0 | Domain baseline for named agents and public trust surfaces |
| AIS-1 | v0.2 draft | Experimental bonded identity and accountability signal for ALA/SOA agents |

## Compatibility statement

This is an additive, non-breaking alignment set. ANAB v0.10.0 references TIS v0.10.0 artifacts as supporting evidence for named-agent assurance. DCAS v0.10.0 can evaluate those references as assurance evidence. TIS remains the canonical schema owner.

AIS-1 v0.2 is experimental in this stack. It contributes bonded identity, sponsor accountability, ALA/SOA classification, parent-chain visibility, registry status, timestamp evidence, and assurance-container references. It does not replace delegation, runtime authorization, or provenance controls.

## Operational note

If TIS changes any runtime governance, authority boundary, status, decision receipt, registry publication, or evidence bundle schema, maintainers SHOULD open a drift review before issuing a new ANAB minor release.

If AIS-1 changes `agentClass`, `parentDid`, DID resolution, registry status, timestamp semantics, SOA cascade revocation, or Assurance Container semantics, maintainers SHOULD open a standards drift review before issuing a new ANAB minor release.
