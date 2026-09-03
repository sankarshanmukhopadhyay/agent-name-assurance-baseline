# ANAB implementation validation

ANAB v0.10 is treated here as an assurance target rather than a source of new controls. The implementation-validation pack exists to make existing ANAB propositions falsifiable by independent evaluators.

## Validation pack

The canonical manifest is `conformance/fixtures/implementation-validation-manifest.json`.

It defines representative PASS, FAIL and INDETERMINATE expectations. These are expected domain outcomes, not DCAS implementation instructions.

## Authority boundary

ANAB owns:

- named-agent assurance requirements;
- domain-specific evidence expectations;
- the meaning of ANAB tiers and profiles;
- the expected domain result represented by each fixture.

ANAB does not own:

- the DCAS evaluator algorithm;
- relying-party policy outside ANAB;
- Interop Lab admission or promotion judgments;
- action-specific authority merely because identity/name assurance succeeds.

A valid named-agent identity binding therefore MUST NOT be interpreted as proof that the agent has authority to perform a consequential action.

## Epistemic outcomes

- **PASS** means the evaluated ANAB proposition is demonstrated by sufficient current evidence.
- **FAIL** means the evaluated proposition is contradicted or a required condition is demonstrably unmet.
- **INDETERMINATE** means available evidence is insufficient to decide, including missing, stale or unverifiable evidence.

Missing evidence MUST NOT be converted to PASS.

## Change discipline

Do not add a normative ANAB concept merely to make a fixture convenient. If a representative fixture cannot be expressed with the current control and evidence model, record that as a falsification finding and route it through a separate governance change.

## Cross-repository use

DCAS may consume this pack to test evaluator semantics. The Trust Protocol Interop Lab may use the same fixtures to compare expected and observed results. Neither consumer acquires authority to redefine ANAB requirements by doing so.
