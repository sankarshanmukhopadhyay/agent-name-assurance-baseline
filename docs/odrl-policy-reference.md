# ANAB ODRL policy references

## Why this exists

ANAB is a **baseline and assurance repo**, not a general policy-language repo. Its normative core remains the control catalog, conformance declaration, evidence bundles, and verifier-facing interpretation.

That said, some deployments need a machine-readable way to publish **usage conditions, disclosure restrictions, notice duties, attribution duties, or operator-imposed prohibitions** around named agents and agent pages. ODRL is a reasonable carrier for that class of policy.

## Boundary

ODRL is **optional** in ANAB.

Publishing an ODRL policy MAY help a relying party understand conditions around:

- disclosure of extended agent metadata
- attribution or notice duties
- restrictions on downstream reuse of agent metadata
- policy-gated access to operational or high-risk surfaces

Publishing an ODRL policy does **not** satisfy ANAB controls by itself, and it does **not** replace the ANAB conformance declaration or evidence bundle.

## Recommended publication pattern

When used, an ANAB deployment SHOULD:

1. publish the authoritative ANAB declaration
2. publish the evidence bundle or stable evidence references
3. publish an ODRL policy or policy reference only for the bounded conditions that benefit from machine-readable expression
4. clearly separate **policy publication** from **policy enforcement evidence**

## What to point at

- Crosswalk: `crosswalk/odrl.yml`
- Example ODRL policy: `profiles/odrl/agent-name-policy.jsonld`

## Suggested policy topics

- metadata disclosure gating
- attribution requirements
- usage prohibitions for copied trust marks or agent metadata
- notice duties for downstream republishing
- constraints on automated harvesting of Agent Page data
