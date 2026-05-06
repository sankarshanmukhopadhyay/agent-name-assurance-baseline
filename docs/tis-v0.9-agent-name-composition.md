# TIS v0.9 agent-name composition profile

**Status:** Active guidance for ANAB v0.9.0
**Aligned TIS release:** v0.9.0
**Last reviewed:** 2026-05-06

## Purpose

This profile explains how ANAB declarations and evidence bundles can reference `trust-infrastructure-schemas` v0.9.0 runtime trust artifacts from DTG, OpenVTC, and VTI systems.

ANAB owns the domain baseline for agent names and agent pages. TIS owns canonical trust artifact schemas. DCAS owns the evaluation method. This profile keeps those boundaries explicit.

## Core rule

TIS artifacts can support ANAB evidence, but they do not automatically prove agent name assurance.

A named agent remains ANAB-conformant only when the relevant ANAB controls, public trust surface, operator binding, resolution integrity, lifecycle state, and evidence expectations are satisfied.

## Named-agent interpretation

| Question | ANAB interpretation | TIS contribution |
| --- | --- | --- |
| Who is the agent? | Agent Name, Agent Page, and associated public identifiers | Artifact references can support credential and relationship evidence |
| Who operates the agent? | Accountable operator binding and public disclosure | VTI or DTG artifacts may support operator or authority claims |
| What authority is claimed at runtime? | ANAB treats this as contextual evidence, not name proof | VTA context, ACL, authorization credential, and decision receipt |
| Is the evidence current? | ANAB requires freshness and lifecycle interpretation | OpenVTC relationship state, receipt timestamps, expiry, and revocation indicators |
| Can a relying party audit reliance? | ANAB requires stable references and explainable interpretation | Evidence bundle manifest and decision receipt artifacts |

## Composition with ANAB controls

TIS artifacts are most relevant to:

- `ANAGB-RES-*` controls for resolution and identifier coherence;
- `ANAGB-AGT-*` controls for agent identity and operator binding;
- `ANAGB-A2A-*` controls where Agent Card metadata references runtime trust artifacts;
- `ANAGB-LOG-*` controls for audit evidence;
- `ANAGB-IR-*` controls where revocation or incident state affects relying-party interpretation.

## A2A publication guidance

ANAB-over-A2A metadata MAY include stable references to TIS artifacts. Clients MUST NOT treat the mere presence of those references as proof of authority. A client should apply local policy and, for higher assurance cases, consume DCAS evaluation results.

Recommended fields for implementers include:

- TIS release or compatibility profile version;
- evidence bundle manifest reference;
- decision receipt reference;
- authorization credential reference;
- relationship state reference;
- declaration freshness and revocation policy;
- DCAS evaluation result reference, if available.

## Relying-party interpretation

A relying party SHOULD ask:

1. Does the Agent Name resolve to the same operator and public trust surface represented in the TIS artifacts?
2. Are the artifact references stable, retrievable, and hash-bound?
3. Do the artifacts carry current lifecycle and revocation evidence?
4. Is runtime authority scoped to the action being requested?
5. Has a DCAS evaluator issued a result for this evidence bundle or relying-party context?

## Non-overlap rule

ANAB MUST NOT copy TIS schemas into local schema definitions. ANAB MAY reference TIS artifacts as evidence pointers inside declarations, bundles, A2A metadata, and documentation.

## Example

See `../conformance/samples/tis-v0.9-backed-enterprise-agent.json` for a TIS-backed ANAB enterprise declaration.
