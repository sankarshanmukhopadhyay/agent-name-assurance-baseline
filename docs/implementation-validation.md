# ANAB implementation validation

The version 1.1 synthetic fixture pack makes selected ANAB v0.10.0 propositions independently evaluable. It is not a complete Enterprise assessment, a live platform test, or certification.

## Start with the local checks

From the ANAB repository root, with Python 3.11 or later:

```bash
python -m pip install -r requirements-ci.txt
python tools/validate_repo.py
python -m unittest discover -s tests -p 'test_*.py'
```

The local validator checks the case and manifest schemas, control IDs, complete bindings, fixture coverage, and A2A gate behavior. It does not execute DCAS.

## Run the independent evaluator

```bash
git clone https://github.com/sankarshanmukhopadhyay/dtg-conformance-assurance.git ../dcas-evaluator
git -C ../dcas-evaluator checkout --detach f1c81870d5a3e130841ff550d17e5a6f2fc3683c
python tools/validate_implementation_fixtures.py --dcas ../dcas-evaluator --output /tmp/anab-assessment
```

Use a clean pinned DCAS checkout. The script refuses an unexpected revision or dirty checkout. CI runs the same CLI and retains normalized inputs, observed results and report.json as a workflow artifact. A mismatch in overall outcome, individual control finding or binding fails the check.

## What the cases establish

| Fixture | Bounded proposition | Expected |
| --- | --- | --- |
| ANAB-FX-001 | Selected current name and operator binding propositions | PASS |
| ANAB-FX-002 | Stale binding under explicit rejection policy | FAIL |
| ANAB-FX-003 | Revoked status, despite working revocation mechanism and suspension | FAIL |
| ANAB-FX-004 | Missing freshness evidence, despite safe handling | INDETERMINATE |
| ANAB-FX-005 | Incorrect tier display, with separate missing transparency evidence | FAIL |
| ANAB-FX-006 | Valid separation of identity and authority, but no scoped authority evidence | INDETERMINATE |

The manifest at `conformance/fixtures/implementation-validation-manifest.json` owns expected overall and per-control outcomes. Inputs at `conformance/fixtures/cases/` contain synthetic assessor observations and explicit evidence bindings, not expected outcomes. The adapter records the exact input bytes' SHA-256 and preserves original control IDs and observation references. DCAS independently evaluates those assessed statuses. The fixture manifest is used only for validation and comparison, never to generate observed decisions.

An available observation represents a synthetic assessor finding; it is not an authenticated live evidence artifact. Production assessment requires actual source evidence, independently established relevance, authenticity, applicability, freshness and complete control coverage. An absent evidence record is invalid fixture construction; represent an absent source observation with the explicit missing status. No authority can be derived from identity or a declared delegation requirement alone.

## Authority and interpretation

ANAB owns its domain requirements, evidence expectations and expected outcomes. DCAS owns the independent evaluator algorithm and result contract. TIS owns canonical trust artifact and assurance-level semantics. The relying party owns reliance policy and residual risk acceptance. The Trust Protocol Interop Lab owns its own comparison and promotion decisions.

A stale condition is FAIL under the explicit fixture policy; if the available evidence cannot establish whether a binding is current, the outcome is INDETERMINATE. A working fail-safe client or revocation mechanism can pass its own control assessment even when current reliance fails. No normative controls or assurance levels are added. See [DCAS composition](dcas-composition.md).
