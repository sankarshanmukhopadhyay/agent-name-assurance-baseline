# Assurance Levels (AL1–AL4)

This repo already defines **name-binding tiers** (**AN-0 … AN-3**) and **operational profiles** (**Core / Deploy / Transact / Enterprise**).
This document adds a complementary axis: **Assurance Levels (AL1–AL4)** — the maturity and auditability of the *overall agent deployment*.

Think of it like this:

- **Tier (AN-x)** answers: *How strong is the name ↔ identifier binding?*
- **Profile** answers: *What operational scope is in play?*
- **Assurance Level (ALx)** answers: *How governed, testable, and audit-ready is the whole system — especially under delegation?*

ALs are intentionally defined in **normative, testable** language to minimize “interpretation tax”.

---

## Definitions and boundary cases

### Human-in-the-loop (HITL)
A system is considered HITL only if a **human approval step is both**:
1) **Required** for execution of the high-risk action, and  
2) **Effective**, meaning it cannot be bypassed by automation, policy misconfiguration, or race conditions.

“Human review exists in a UI” is not HITL. HITL must be enforceable in the execution path.

### Delegated agents
A delegated agent is any agent or workflow that can act **on behalf of** a person or organization with:
- authority to transact, commit, publish, modify access, or otherwise create durable consequences.

Delegation can be explicit (a signed delegation token) or implicit (long-lived keys, shared accounts, background automations).

### Organization-issued agents
An organization-issued agent is any agent where:
- the organization provisions the identity, keys, access, or runtime, **and**
- the organization can revoke, rotate, or constrain the agent’s authority.

---

## AL1 — Stated + bounded

**Intent:** you can explain what it does; you can’t yet prove much.

### What must be true (normative)
An AL1 system:

- **MUST** declare its **target tier (AN-x)** and **profile** and publish a conformance declaration.
- **MUST** identify whether it is **HITL**, **delegated**, and/or **org-issued** (it can be more than one).
- **MUST** have a documented **authority boundary**: what the agent is allowed to do, and what it MUST NOT do.
- **MUST** provide a basic **revocation / key-rotation** procedure for name bindings and agent credentials.
- **MUST** provide minimal logging sufficient to answer: *who acted, when, under what identity, and with what result*.

### Typical boundary cases
- **HITL UI-only review** without enforced blocking is **NOT** AL1-compliant for “HITL” claims.
- **Delegation** with no revocation story is **NOT** AL1-compliant.

---

## AL2 — Managed + evidenced

**Intent:** you can provide evidence that controls exist and are used.

### What must be true (normative)
An AL2 system:

- **MUST** satisfy all AL1 requirements.
- **MUST** maintain an **evidence bundle** aligned to the target tier/profile (see `evidence-bundles/`).
- **MUST** implement **change control** for policy/config that affects name binding, delegation, or risk gating.
- **MUST** provide an **audit trail** linking key events to evidence (logs, configs, test outputs, runbooks).
- If delegated:
  - **MUST** implement a **delegation artifact** (token/credential/policy) that is **scoped** (least privilege) and **revocable**.
- If org-issued:
  - **MUST** provide **joiner/mover/leaver** controls for agent identity and access.

---

## AL3 — Auditable + independently reviewable

**Intent:** an external reviewer can reproduce checks and reach the same conclusion.

### What must be true (normative)
An AL3 system:

- **MUST** satisfy all AL2 requirements.
- **MUST** provide **repeatable tests** (or test vectors) for critical controls (resolution, binding integrity, revocation checks).
- **MUST** include a **decision log** for key design choices (threat assumptions, identity root, revocation model, transparency).
- **MUST** define a **review cadence** for risk/threat updates and operational incident learning.
- If delegated:
  - **MUST** provide **step-up** / friction mechanisms for high-risk actions, aligned to the threat model.
- If org-issued:
  - **MUST** provide **segregation of duties** (SoD) for agent provisioning vs authorization for high-risk actions.

---

## AL4 — Continuous + monitored (runtime assurance)

**Intent:** assurance is not a PDF; it’s an operating mode.

### What must be true (normative)
An AL4 system:

- **MUST** satisfy all AL3 requirements.
- **MUST** provide **continuous control monitoring** for critical conditions (revocation freshness, policy drift, anomalous delegation use).
- **MUST** implement **automated evidence capture** (or strong automation support) to keep the evidence bundle current.
- **MUST** have defined **SLOs** (service level objectives) for assurance-critical services (resolution, revocation checking, transparency).
- **MUST** provide a **post-incident assurance loop**: incidents lead to updated controls, tests, and evidence.

---

## Upgrade paths (evidence deltas)

### AL1 → AL2 (minimum deltas)
- Add an evidence bundle with **artifact index** and **evidence pointers**.
- Add change control for configuration/policy impacting binding and delegation.
- Add delegation artifacts if delegation exists (scoped + revocable).

### AL2 → AL3 (minimum deltas)
- Add reproducible tests/test vectors for critical controls.
- Add decision logs and reviewer instructions so a third party can validate claims.
- Add review cadence and explicit step-up policy mapping (where delegation/high-risk actions exist).

### AL3 → AL4 (minimum deltas)
- Add continuous monitoring + alerting for assurance-critical conditions.
- Automate evidence collection and ensure freshness is measurable.
- Add SLOs and post-incident governance loop.

---

## How AL interacts with tier/profile

ALs do **not** replace tiers/profiles. They constrain *how well you can claim* that your tier/profile implementation is real.

- It is valid to be **AN-2 / Deploy / AL2** (managed deployment with evidence).
- It is suspicious to claim **AN-3 / Enterprise / AL1** (high assurance surface with low assurance operations).
Reviewers SHOULD treat mismatched claims as a trigger for deeper scrutiny.

