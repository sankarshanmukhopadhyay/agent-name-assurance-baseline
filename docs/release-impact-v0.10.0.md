# Portfolio Release Impact: ANAB v0.10.0

## Release Summary

| Field | Value |
|---|---|
| Repository | agent-name-assurance-baseline |
| Release version | v0.10.0 |
| Release date | 2026-07-03 |
| Primary change type | TIS v0.10 synchronization and AIS-1 v0.2 interpretation |
| Portfolio impact classification | Artifact / Assurance / Standards |

## Changed Surfaces

- [x] Terminology or conceptual model
- [x] Schema or runtime artifact
- [x] Evidence bundle or decision receipt
- [ ] Conformance verdict or test fixture
- [x] Assurance level or control mapping
- [x] Registry publication or status/revocation semantics
- [x] Standards binding or crosswalk
- [x] README, onboarding, or adoption workflow

## Relationship Review

| Source repo | Target repo | Relationship | Impact | Evidence |
|---|---|---|---|---|
| trust-infrastructure-schemas | agent-name-assurance-baseline | drift_sensitive_to | ANAB now tracks TIS v0.10 runtime assurance artifacts | `model/tis-compatibility-review.json` |
| trust-systems-meta-model | agent-name-assurance-baseline | informs | AIS-1 kept inside bounded identity/accountability semantics | `profiles/ais1/anab-profile.md` |
| agent-name-assurance-baseline | dtg-conformance-assurance | produces_evidence_for | New AIS-1 v0.2 examples can feed DCAS evaluation | `conformance/samples/tis-v0.10-backed-enterprise-agent.json` |

## Validation Evidence

```text
python -m pip install -r requirements-ci.txt
python tools/validate_repo.py
python tools/lint_markdown.py
python tools/check_links.py
```

## Release Note Language

ANAB v0.10.0 aligns the named-agent baseline with TIS v0.10 runtime assurance artifacts and adds an experimental AIS-1 v0.2 interpretation profile. The release supports ALA/SOA classification, parent accountability checks, DID resolution, registry status, timestamp references, assurance containers, and cascade revocation interpretation while preserving the key relying-party boundary: AIS-1 bonded identity is not delegated authority.

## Decision

- [ ] Release has no cross-repo impact.
- [ ] Release has documentation impact only.
- [x] Release requires downstream artifact/profile/test updates.
- [ ] Release should be held until downstream compatibility is updated.
