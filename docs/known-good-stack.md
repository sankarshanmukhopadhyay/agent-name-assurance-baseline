# Known-good stack

**Last reviewed:** 2026-05-06

| Component | Version | Role |
| --- | --- | --- |
| trust-infrastructure-schemas | v0.9.0 | Canonical DTG/OpenVTC/VTI runtime trust artifact schemas and compatibility matrix |
| dtg-conformance-assurance | v0.8.0 | Evaluation method for TIS-backed runtime evidence |
| agent-name-assurance-baseline | v0.9.0 | Domain baseline for named agents and public trust surfaces |

## Compatibility statement

This is an additive, non-breaking alignment set. ANAB v0.9.0 references TIS v0.9.0 artifacts as supporting evidence for named-agent assurance. DCAS v0.8.0 can evaluate those references as assurance evidence. TIS remains the canonical schema owner.

## Operational note

If TIS changes any DTG, OpenVTC, VTI, decision receipt, or evidence bundle schema, maintainers SHOULD open a drift review before issuing a new ANAB minor release.
