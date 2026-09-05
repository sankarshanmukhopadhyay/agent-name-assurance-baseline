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
| Default-branch delete/force-push protection | PASS | active `Main Branch Protect` ruleset observed 2026-09-05 | None identified for these two controls. |
| PR-based change control / required completion gate | EVIDENCE REQUIRED | current ruleset contains deletion + non-fast-forward protection only | Tracked separately as a GitHub repository-setting governance issue. |
| Release/version evidence | PASS | `VERSION`, `CHANGELOG.md`, `PROJECT-STATUS.yaml` | Release publication remains a maintainer decision. |
| Authority boundary | PASS | repository documentation and assurance model | Identity/name assurance MUST NOT imply action-specific authority. |

## Completion boundary

Repository-file baseline gaps are closed by the associated remediation PR. The missing PR/required-check ruleset semantics are intentionally tracked as a separate platform-setting control rather than being represented as PASS.
