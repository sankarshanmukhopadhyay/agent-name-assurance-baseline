# Versioning and compatibility policy

This repo is treated as **product-grade infrastructure**: small wording changes can create real interoperability drift.
So we make compatibility explicit.

## SemVer
We use **Semantic Versioning**: `MAJOR.MINOR.PATCH`.

- **MAJOR**: breaking changes to schemas, control semantics, or required artifacts that invalidate prior conformance claims.
- **MINOR**: additive changes (new optional fields, new docs, new examples) that keep old artifacts valid.
- **PATCH**: clarifications and fixes that do not change normative meaning or schema compatibility.

## Compatibility promises

### JSON Schemas
- MINOR/PATCH releases MUST be backward compatible: existing valid declarations and bundles remain valid.
- MAJOR releases MAY break compatibility, but MUST provide:
  - migration notes
  - versioned schema IDs
  - updated samples and tooling

### Controls
- Control IDs are stable within a MAJOR version.
- Controls MAY be clarified, but the *testable meaning* must not change in a PATCH release.

### Conformance claims
A conformance claim MUST declare:
- `spec_version`
- `verification_tier` + `conformance_profile`
- `assurance_level`
- evidence bundle pointer (for AL2+)

Reviewers SHOULD validate claims using the corresponding tagged release version.

