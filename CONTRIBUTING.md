# Contributing

Substantive changes should preserve a visible Issue → PR → tests/evidence → merge judgment trail.

1. State the proposition, affected authority surface, compatibility/assurance impact, and acceptance criteria in an issue.
2. Implement the smallest coherent change on a branch.
3. Add or update deterministic tests, fixtures, negative cases, and evidence where the claim is consequential.
4. In the pull request, record implementation choice, validation, residual uncertainty, and any evidence invalidation or migration consequence.
5. Merge only after the applicable repository validation gate passes.

ANAB owns named-agent assurance requirements and expected evidence semantics. Contributions must not silently broaden those semantics into action-specific authority or transfer evaluation authority to downstream consumers.

Missing evidence is not a pass. Record unavailable evidence as indeterminate/evidence-required and track the gap explicitly.

Security reports must follow [`SECURITY.md`](SECURITY.md).
