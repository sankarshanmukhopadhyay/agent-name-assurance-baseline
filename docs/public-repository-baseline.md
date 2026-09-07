# Public repository baseline

This record captures the repository-owned controls reviewed under issue #12. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose, maturity, authority and adoption surface | PASS | `README.md`, `PROJECT-STATUS.yaml` | None identified. |
| Licensing | PASS | `LICENSE` | None identified. |
| Security reporting and supported versions | PASS | `SECURITY.md` | GitHub private-vulnerability-reporting enablement remains a hosted setting. |
| Contribution/support/community guidance | PASS | `CONTRIBUTING.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`, issue templates and PR template | None identified. |
| Dependency update management | PASS | `.github/dependabot.yml` | Hosted Dependabot enablement remains platform evidence. |
| CI least privilege and validation | PASS | `.github/workflows/ci.yml` declares `contents: read` and executes repository, Markdown, link and Mermaid validation | Third-party dependency/runtime availability remains an operational dependency. |
| Default-branch delete/force-push protection | PASS | active `Main Branch Protect` ruleset observed 2026-09-07; deletion and non-fast-forward updates are blocked | GitHub-hosted enforcement remains a platform dependency and must be re-observed after material settings changes. |
| PR-based change control / required completion gate | PASS | active `Main Branch Protect` ruleset observed 2026-09-07 requires pull requests, review-conversation resolution, linear history and strict required status check `validate` (integration ID `15368`); bypass actors are empty | Check-name, workflow, target or bypass changes invalidate this evidence and require reassessment. |
| Release/version evidence | PASS | `VERSION`, `CHANGELOG.md`, `PROJECT-STATUS.yaml` | Release publication remains a maintainer decision. |
| Authority boundary | PASS | repository documentation and assurance model | Identity/name assurance MUST NOT imply action-specific authority. |

## Completion boundary

Repository-file baseline gaps are closed by the associated remediation PR. The GitHub-hosted PR/required-check control has now been independently re-observed through the rulesets API and is recorded as PASS on that evidence rather than inferred from documentation.

Missing or stale hosted-control evidence MUST NOT be interpreted as PASS.
