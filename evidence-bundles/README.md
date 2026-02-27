# Evidence bundles

An **evidence bundle** is a portable, review-friendly package that makes conformance claims **auditable**.

The goal is not “paperwork”. The goal is **repeatable review**:
a reviewer should be able to follow links, verify artifacts exist, and reproduce key checks.

---

## Bundle structure (recommended)

```
evidence-bundles/
  examples/
  schemas/
  templates/
```

For implementers publishing evidence, the recommended layout is:

```
evidence/
  bundle.json
  artifacts/
    decision-log.md
    risk-assessment.md
    controls-mapping.md
    test-results/
    configs/
    runbooks/
```

- `bundle.json` is **machine-readable** and points to artifact locations, hashes, and freshness expectations.
- Artifact files can be local (in-repo) or remote (URLs), but SHOULD be stable and immutable (or versioned).

---

## Required vs optional artifacts

Each assurance level has:

- **Required artifacts:** minimum bar for auditability.
- **Optional artifacts:** best-practice items that reduce reviewer friction and increase confidence.

This repo provides synthetic examples for:
- **AL2** and **AL3** (“good enough” vs “best practice”)

---

## Schemas and examples

- Evidence bundle JSON schema: `evidence-bundles/evidence-bundle.schema.json`
- Examples:
  - `evidence-bundles/examples/al2-good-enough/`
  - `evidence-bundles/examples/al2-best-practice/`
  - `evidence-bundles/examples/al3-good-enough/`
  - `evidence-bundles/examples/al3-best-practice/`

