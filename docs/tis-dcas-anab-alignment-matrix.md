# TIS, DCAS, and ANAB alignment matrix

**Status:** Informative cross-repo alignment matrix
**Last reviewed:** 2026-05-06

| Concern | TIS | DCAS | ANAB |
| --- | --- | --- | --- |
| Schema contract | Owns canonical trust artifact schemas | Consumes as evidence inputs | References for agent-name evidence |
| Assurance levels | Owns canonical AL1-AL4 semantics | Evaluates sufficiency against AL targets | Applies AL expectations to agent-name declarations |
| Runtime authority | Represents authority artifacts and decision receipts | Evaluates authority, scope, and enforcement evidence | Interprets authority evidence for named agents |
| Agent name assurance | Supports through artifact references | Evaluates declarations and evidence | Owns domain-specific controls and tiers |
| Revocation | Defines artifact surfaces that may carry lifecycle state | Assesses freshness, revocation, and operational effect | Requires agent-name lifecycle interpretation |
| Drift tracking | Source matrix and release notes | Downstream evaluator drift review | Downstream domain-baseline drift review |
| Evidence bundle | Defines canonical evidence structures | Evaluates completeness and auditability | Produces or references bundles for named agents |

## Non-overlap principle

The three repositories MUST NOT collapse into one another. TIS should not become an evaluator. DCAS should not redefine TIS schemas. ANAB should not become a generic conformance method. Interoperability comes from explicit boundaries, stable references, and repeatable validation.
