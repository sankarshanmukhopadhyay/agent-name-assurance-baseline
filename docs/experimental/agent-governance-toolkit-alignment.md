# ANAB ↔ Agent Governance Toolkit alignment *(experimental)*

This note explains which ideas from the Microsoft Agent Governance Toolkit are useful for ANAB and which are not.

## Useful upstream concepts

- **runtime identity visibility** for higher-assurance deployments
- **decision-time revocation and freshness checks** rather than publication-time assumptions alone
- **tamper-evident operational traces** for delegated or side-effecting actions
- **fail-safe handling** when runtime identity status cannot be established

## Not adopted into ANAB core

- Numeric trust scores are not adopted as ANAB semantics.
- Execution rings or privilege tiers are treated as implementation details, not baseline naming requirements.
- The toolkit is not imported as a normative dependency.

## Adoption pattern

ANAB uses the toolkit only as an upstream conceptual reference for **experimental runtime-assurance guidance**. The stable core remains the published name, page, identifier, control, declaration, and evidence model already defined in this repository.
