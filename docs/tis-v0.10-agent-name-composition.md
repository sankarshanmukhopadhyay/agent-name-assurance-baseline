# TIS v0.10 Agent-Name Composition Profile

**Status:** Active guidance for ANAB v0.10.0
**Aligned TIS release:** v0.10.0
**Last reviewed:** 2026-07-03

## Purpose

This profile explains how ANAB declarations and evidence bundles can reference `trust-infrastructure-schemas` v0.10.0 runtime assurance artifacts while preserving ANAB as the domain baseline for agent names and agent pages.

The rule is deliberately strict:

- TSMM owns the semantic governance model.
- TIS owns canonical trust artifact schemas.
- DCAS owns the evaluator method.
- ANAB owns named-agent interpretation, control IDs, and relying-party guidance.

## Core Rule

TIS v0.10 artifacts can support ANAB evidence, but they do not automatically prove agent-name assurance.

A named agent remains ANAB-conformant only when the relevant ANAB controls, public trust surface, operator binding, resolution integrity, lifecycle state, and evidence expectations are satisfied. Runtime artifacts improve auditability; they do not replace domain interpretation.

## Runtime Assurance Interpretation

| Question | ANAB interpretation | TIS v0.10 contribution |
|---|---|---|
| Who is the agent? | Agent Name, Agent Page, Agent Card, and public identifiers | Runtime governance projection and registry entry references |
| Who is accountable? | Accountable operator, sponsor, or issuer is disclosed and consistent | Authority boundary, issuer, sponsor, and registry publication evidence |
| What authority is claimed? | Authority is contextual and must not be inferred from name or bond alone | VTI authorization, ACL, Trust Task execution receipt, and decision receipt |
| Is the evidence current? | Freshness and revocation state are interpreted against relying-party risk | Status-list reference, lifecycle event, registry publication profile |
| Can reliance be audited? | ANAB needs stable references and explainable interpretation | Integrity-bound evidence bundle and decision receipt |

## AIS-1 v0.2 Composition

AIS-1 v0.2 can be referenced as a named-agent identity and accountability input when it exposes:

- `agentClass` as `ala` or `soa`;
- `parentDid` for subordinate operating agents;
- DID resolution and registry evidence;
- current bond status;
- timestamp service reference where available;
- assurance container reference where available.

ANAB relying parties MUST preserve these guardrails:

1. Bond is not delegation.
2. Tier is not full assurance.
3. Verification is not provenance.
4. SOA status is unsafe to rely on unless the parent ALA is active.
5. Parent ALA revocation must cause SOA downgrade or denial.

## Recommended Evidence Pointers

ANAB declarations, evidence bundles, or A2A metadata MAY include:

- TIS release or compatibility profile version;
- TSMM runtime governance projection reference;
- authority boundary reference;
- integrity-bound evidence bundle manifest reference;
- decision receipt reference;
- Trust Task execution receipt reference;
- status-list or revocation reference;
- registry publication profile reference;
- AIS-1 v0.2 profile extension reference;
- DCAS evaluation result reference, if available.

## Relying-Party Checklist

A relying party SHOULD ask:

1. Does the Agent Name resolve to the same operator and public trust surface represented in the runtime artifacts?
2. Are artifact references stable, retrievable, hash-bound, and current?
3. Does the authority boundary preserve source, scope, lifecycle state, and revocation obligations?
4. Is an AIS-1 SOA backed by an active parent ALA?
5. Has a DCAS evaluator issued a result for this evidence bundle or relying-party context?
6. Does the implementation fail safely when status or parent state is unavailable?

## Non-Overlap Rule

ANAB MUST NOT copy TIS schemas into local schema definitions. ANAB MAY reference TIS artifacts as evidence pointers inside declarations, bundles, A2A metadata, and documentation.

See `../conformance/samples/tis-v0.10-backed-enterprise-agent.json` for a TIS v0.10-backed ANAB enterprise declaration.
