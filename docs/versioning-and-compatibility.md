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


## Unreleased tooling and fixture compatibility

The synthetic manifest advances from 1.0 to 1.1 with concrete case paths and expected per-control findings. Consumers of the former manifest must use the new schema. The A2A experimental admission gate now rejects schema-invalid parameters and verified claims without a freshness bound; migrate vectors to schema-valid parameters. ANAB v0.10.0 normative controls and public declaration schemas are unchanged. DCAS 0.2 requires reviewed explicit bindings; historical results are not migrated automatically.
