# ANAB composition with DCAS

ANAB defines named-agent domain requirements and evidence expectations. DCAS independently evaluates assessed evidence; neither a declaration nor an evaluator decision alone establishes relying-party acceptance.

## Adoption path

1. Choose ANAB tier, profile and applicable controls using the normative baseline and applicability matrix.
2. Publish a signed declaration and evidence bundle, preserving control IDs and artifact references.
3. An assessor establishes the relevance, authenticity, freshness and sufficiency of evidence for each requirement. Record missing, unverifiable, stale, revoked and contradicted evidence explicitly.
4. Submit explicit requirement-to-evidence bindings and a deterministic evaluation context to DCAS contract 0.2.
5. Retain per-requirement findings, source evidence and evaluator identity for audit. The relying party decides whether the bounded result supports reliance.

## Executable integration (unreleased)

The [implementation validation pack](implementation-validation.md) runs the DCAS reference CLI at [the pinned evaluator revision](https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance/tree/f1c81870d5a3e130841ff550d17e5a6f2fc3683c). This is evaluator contract 0.2, not the published DCAS v0.10.0 release. The ANAB normative target remains v0.10.0.

The older `conformance/samples/dcas-ready-enterprise-agent.json` is an illustrative declaration, not an assessed input or a real evidence bundle. Its placeholder references and digest are not proof. Historical DCAS 0.1 results remain historical; reassess explicit bindings before producing a current 0.2 result. Do not map every available observation to every control.

The synthetic case adapter is not a production evidence authenticator. It does not consume live Trust Tasks records; such intake belongs to DCAS. A future real assessment must preserve the original source evidence, scope and assessor authority independently. Identity/name assurance cannot imply permission to execute a consequential action.
