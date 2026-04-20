# Runtime identity lifecycle *(experimental guidance)*

ANAB is primarily a baseline for **Agent Names** and **Agent Pages**, but higher-assurance deployments increasingly need to prove how the named identity behaves **after publication**.

This document introduces an experimental runtime identity lifecycle lens, informed by the Microsoft Agent Governance Toolkit as an upstream reference for zero-trust identity, policy checks, and runtime auditability.

## Why this matters

A strong name-to-identifier binding can still be operationally weak if the deployment cannot show:

- when the runtime identity was activated
- what delegation scope it currently holds
- how revocation or suspension is checked at action time
- how credentials rotate
- how orphaned or stale identities are detected

## Lifecycle stages

1. **Issuance** — the named agent is bound to its identifier root and published trust surface
2. **Activation** — runtime credentials or execution identities are activated for a deployment context
3. **Delegation** — scoped runtime permissions are granted for bounded tasks or tool access
4. **Operation** — logs, receipts, or equivalent evidence show how the identity was used
5. **Rotation** — keys, certificates, or execution credentials are replaced without ambiguity about continuity
6. **Revocation / suspension** — relying systems can detect invalid or suspended status
7. **Decommissioning** — orphaned identities, stale pages, and residual endpoints are removed or marked unsafe

## Recommended evidence by higher assurance level

| Assurance Level | Recommended runtime identity evidence |
|---|---|
| AL1 | Static publication and internally consistent declaration |
| AL2 | Verifiable revocation/status checks and basic runtime logs |
| AL3 | Independent review of runtime identity and delegation handling for higher-risk actions |
| AL4 | Continuous monitoring, tamper-evident logs or receipts, rotation records, and orphan detection controls |

## Boundary

This guidance is experimental and does not change the normative ANAB control catalog. It provides a sharper interpretation path for assessors and implementers working with DCAS and TSMM in runtime-governed agent ecosystems.
