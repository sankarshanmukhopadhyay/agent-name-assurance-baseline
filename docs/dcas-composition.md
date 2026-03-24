# ANAB composition with DCAS

ANAB is a domain baseline. It does not try to be the evaluator. Its job is to define what a named agent implementation claims, what evidence should exist, and how that evidence is packaged.

DCAS is the verifier workflow that can consume those claims and determine whether reliance is justified for a given use case.

## Composition pattern

1. The implementer publishes an ANAB conformance declaration.
2. The implementer or assessor publishes an ANAB evidence bundle.
3. A DCAS evaluator maps the declared ANAB controls to its own control objectives and produces an evaluation result.
4. Relying parties consume the evaluation result while preserving the original ANAB identifiers for traceability.

## What changed in this increment

This release adds a DCAS-ready sample declaration so downstream evaluators have a concrete starting point. The intent is to reduce one of the most common integration failures: translating away the original ANAB control identifiers too early.

## Practical guidance

- keep the ANAB declaration authoritative for domain-specific control status
- use DCAS for evaluation posture, not for renaming the baseline
- preserve assurance level and evidence bundle references as stable pointers
