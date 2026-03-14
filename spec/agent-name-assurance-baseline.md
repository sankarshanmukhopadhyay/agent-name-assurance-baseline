# Agent Name Assurance & Governance Baseline (ANAGB) v0.5.0

## Status
Draft — Working Group Review

This release introduces **Assurance Levels (AL1–AL4)** and standardized **evidence bundles** for repeatable audits.

## Normative Language
The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, and **MAY** are to be interpreted as described in RFC 2119.

---

## Upstream concept mapping (non-normative)

This baseline is informed by the upstream *Agent Names and Agent Pages* draft (working extract under `upstream/agent-names-and-agent-pages/`).

The table below shows how key upstream concepts are operationalized as controls.

| Upstream concept | What we operationalize | Primary controls |
|---|---|---|
| Human-friendly agent naming layered over DIDs | Treat the name as a **routing hint**; trust is derived from binding + verification evidence | ANAGB-RES-01, ANAGB-UI-01, ANAGB-UI-02 |
| Resolution chain (name → DID → DID document → endpoints) | Require secure transport, binding integrity, and monitoring for drift/takeover | ANAGB-RES-01, ANAGB-RES-03, ANAGB-RES-05 |
| Spoofing/impersonation risk | No generic “verified” indicator; step-up for risky actions; stronger tiers require stronger evidence | ANAGB-UI-02, ANAGB-UI-03, Tier AN-1…AN-3 requirements |
| Agent Page as a discovery surface | Minimize disclosure, avoid auto-exchange, require explicit consent, and support anti-scraping | ANAGB-PRIV-01…04, ANAGB-PRIV-05…06 |
| High assurance verification and transparency expectations | Encourage (or require, where applicable) revocation checking and transparency logging | ANAGB-RES-06, ANAGB-LOG-01…03 |

---

## 1. Scope and Objectives

This specification defines assurance, security, privacy, and AI governance requirements for systems implementing:

- Agent Names
- Agent Pages
- Agent-to-Agent interaction
- AI-mediated decisioning within decentralized agent ecosystems

The objective is to prevent phishing amplification, trust inflation, privacy harm, authority confusion, and unsafe AI delegation while enabling human-readable identifiers layered over decentralized identifiers (DIDs).

---


## 1.1 Assurance levels (AL1–AL4)

In addition to verification tiers (AN-0…AN-3), implementers MUST declare an **Assurance Level** claim (AL1–AL4) describing the maturity and auditability of the overall deployment.

- AL definitions and boundary cases are specified in `docs/assurance-levels.md`.
- AL2 and above MUST be backed by a published evidence bundle (see `evidence-bundles/`).

Conformance artifacts MUST include:
- `assurance_level` (AL1–AL4)
- `evidence_bundle` pointer for AL2+


## 2. Verification Tiers

Implementations MUST classify agent name bindings according to one of the following tiers.

| Tier | Label | Binding Strength | Required Evidence | Revocation Requirement |
|------|-------|-----------------|------------------|-----------------------|
| AN-0 | Self-Asserted | Weak | DID includes agent name | None |
| AN-1 | Domain-Control Verified | Medium | Cryptographic proof of domain control bound to DID | Periodic revalidation (≤90 days) |
| AN-2 | Trust Framework Verified | Strong | Verifiable Credential (VC) from recognized issuer | Continuous revocation checking |
| AN-3 | High Assurance Verified | Very Strong | Legal entity validation + operational security controls | Real-time revocation + transparency logging |

### 2.1 UI Signaling Requirements
- **ANAGB-UI-01**: Tier display.
- **ANAGB-UI-02**: No generic verified indicator.
- **ANAGB-UI-03**: Step-up verification for high-risk actions.

---

## 3. Name Resolution & Cryptographic Binding

### 3.1 Binding Integrity
- **ANAGB-RES-01**: Cryptographic binding.
- **ANAGB-RES-02**: Replay resistance.
- **ANAGB-RES-06**: Transparency logging for AN-2/AN-3 (recommended).

### 3.2 Transport Security
- **ANAGB-RES-03**: TLS required.
- **ANAGB-RES-04**: HSTS recommended.

### 3.3 Monitoring & Drift Detection
- **ANAGB-RES-05**: Monitor for DNS drift/domain takeover and alert on unexpected binding changes.

---

## 4. Agent Page Security & Privacy Baseline

### 4.1 Data Minimization
- **ANAGB-PRIV-01**: Minimal public disclosure by default.
- **ANAGB-PRIV-02**: Explicit reveal for sensitive attributes.

### 4.2 Indexing & Scraping Controls
- **ANAGB-PRIV-05**: noindex support (recommended).
- **ANAGB-PRIV-06**: rate limiting / bulk enumeration restriction (recommended).

### 4.3 Consent & Interaction Controls
- **ANAGB-PRIV-03**: MUST NOT auto-initiate credential exchange.
- **ANAGB-PRIV-04**: explicit consent required for credential exchange.

---

## 5. Agent-to-Agent Interaction Controls

Agent names increasingly resolve into agents that participate in **A2A-style discovery and delegated task execution**. When that happens, the name and page are no longer mere brochureware. They become the first trust anchor for protocol negotiation, endpoint selection, and operational reliance.

### 5.1 Capability Discovery

The Agent Page or linked Agent Card MUST disclose enough metadata for a verifier to distinguish low-risk discovery from operational delegation. Anonymous discovery MAY be coarse-grained. High-value capability disclosure SHOULD be authenticated and policy-gated.

### 5.2 Logging & Auditability

Named agents that participate in A2A flows MUST emit logs that let reviewers reconstruct the relationship between the public name, the resolved endpoint, the authenticated principal, the task identifier, and the resulting action.

### 5.3 Abuse Protection

Interaction endpoints MUST resist replay, enumeration, and rate-based abuse. Where the public Agent Page points to machine-operable interfaces, the implementation MUST minimize the chance that a pretty name launders an unsafe endpoint.

### 5.4 A2A-Specific Binding Expectations

When an implementation publishes an A2A Agent Card or equivalent metadata, the following additional requirements apply:

- the Agent Card SHOULD be signed or otherwise integrity protected
- the name, operator, endpoint, supported interfaces, and auth requirements SHOULD remain consistent across the Agent Page, the Agent Card, and the conformance declaration
- task, context, tenant, and subscription identifiers MUST be authorization-scoped
- access to extended metadata SHOULD be policy-gated where disclosure increases attack surface

## 6. AI Decisioning Guardrails

This section applies where AI systems influence contact mediation, trust scoring, credential evaluation, or delegated authority execution.

### 6.1 Disclosure & Transparency
- **ANAGB-AI-01**: disclose AI usage.
- **ANAGB-AI-02**: document decision categories.
- **ANAGB-AI-03**: provide redress mechanism.

### 6.2 Delegated Authority Constraints
- **ANAGB-AI-05**: scoped delegation, expiration, caps, revocation.
- **ANAGB-AI-06**: AI identity MUST NOT imply authority.

### 6.3 Human Override
- **ANAGB-AI-04**: human override for blocks/revocations/delegated actions.

---

## 7. Incident Handling & Recovery
- **ANAGB-IR-01**: incident response plan.
- **ANAGB-IR-02**: key rotation.
- **ANAGB-IR-03**: machine-verifiable revocation.
- **ANAGB-IR-04**: safe suspension (no impersonation).

---

## 8. Conformance Profiles

| Profile | Requirements |
|----------|-------------|
| Core | AN-1 + Sections 3–4 + applicable UI controls |
| Deploy | AN-2 + Sections 3–5 + logging + IR controls |
| Transact | Deploy + Section 6 (AI controls if AI is used) |
| Enterprise | AN-3 + transparency logging + formal governance attestation |

Conformance claims MUST specify the adopted profile and the implemented control IDs.
A tier/profile applicability matrix is provided in `conformance/applicability-matrix.md` to make control scoping auditable and repeatable.

---

## 9. Control Catalog (Normative)

| Control ID | Requirement |
|---|---|
| `ANAGB-UI-01` | Implementations MUST display the achieved tier accurately and MUST NOT collapse all tiers into a generic “verified” label. |
| `ANAGB-UI-02` | Implementations MUST distinguish identity/binding assurance from behavioral or authority assurance. |
| `ANAGB-UI-03` | High-risk actions MUST trigger step-up verification and fresh revocation checking before reliance. |
| `ANAGB-RES-01` | The Agent Name MUST bind to the claimed cryptographic identifier using verifiable proof. |
| `ANAGB-RES-02` | Name resolution and binding artifacts MUST resist replay and stale-state confusion. |
| `ANAGB-RES-03` | Production resolution endpoints MUST use TLS. |
| `ANAGB-RES-04` | HSTS SHOULD be enabled for web-hosted agent pages and resolution endpoints. |
| `ANAGB-RES-05` | Implementations MUST monitor for binding drift and unauthorized endpoint changes. |
| `ANAGB-RES-06` | Transparency logging SHOULD be used for material binding changes and MUST be used for Enterprise profile claims. |
| `ANAGB-PRIV-01` | Agent Pages MUST minimize personal and organizational data exposed by default. |
| `ANAGB-PRIV-02` | Sensitive details MUST require an explicit reveal or equivalent user action. |
| `ANAGB-PRIV-03` | Implementations MUST NOT auto-share high-risk data to unknown requesters. |
| `ANAGB-PRIV-04` | Consent or another documented lawful basis MUST govern non-public data disclosure. |
| `ANAGB-PRIV-05` | No-index hints SHOULD be supported where public discoverability is not intended. |
| `ANAGB-PRIV-06` | Implementations SHOULD apply scrape-friction and anti-enumeration controls proportionate to risk. |
| `ANAGB-AGT-01` | Capability discovery for operational or sensitive features MUST be authenticated. |
| `ANAGB-AGT-02` | Coarse anonymous discovery SHOULD remain available for low-risk ecosystem interoperability. |
| `ANAGB-LOG-01` | Exchanges involving named agents MUST be logged with sufficient identifiers for audit. |
| `ANAGB-LOG-02` | Logs MUST be tamper-evident. |
| `ANAGB-LOG-03` | Logs MUST be exportable for independent review. |
| `ANAGB-ABUSE-01` | Interaction endpoints MUST enforce rate limits or equivalent abuse throttles. |
| `ANAGB-ABUSE-02` | Interaction flows MUST mitigate replay and duplicate submission. |
| `ANAGB-A2A-01` | Published Agent Cards or equivalent metadata SHOULD be signed or otherwise integrity protected. |
| `ANAGB-A2A-02` | The Agent Page, Agent Card, and conformance declaration MUST remain consistent for name, operator, endpoint, and auth requirements. |
| `ANAGB-A2A-03` | Access to extended Agent Card metadata SHOULD be policy-gated where disclosure increases attack surface. |
| `ANAGB-A2A-04` | Task, context, tenant, and subscription identifiers MUST be authorization-scoped and resistant to cross-tenant leakage. |
| `ANAGB-A2A-05` | Push notifications and streaming updates MUST be authenticated or otherwise integrity protected, with replay mitigation. |
| `ANAGB-A2A-06` | Implementations MUST declare supported media types and handle unsupported content safely to avoid trust inflation through ambiguous artifacts. |
| `ANAGB-AI-01` | If AI-mediated decisioning or delegation is used, the implementation MUST disclose that fact. |
| `ANAGB-AI-02` | The implementation MUST distinguish advisory, assistive, and autonomous decision categories. |
| `ANAGB-AI-03` | A redress mechanism MUST exist for consequential errors or misclassification. |
| `ANAGB-AI-04` | Human override MUST exist for consequential actions where feasible. |
| `ANAGB-AI-05` | Delegation MUST be bounded by scope, purpose, and revocability. |
| `ANAGB-AI-06` | Names and tiers MUST NOT imply authority that has not actually been granted. |
| `ANAGB-IR-01` | An incident response procedure MUST exist for compromise or misleading resolution events. |
| `ANAGB-IR-02` | Key rotation procedures MUST be documented and exercised. |
| `ANAGB-IR-03` | Revocation status MUST be machine-verifiable where the deployment claims operational assurance. |
| `ANAGB-IR-04` | Safe suspension behavior MUST exist for compromised or disputed names and pages. |

## Annex References
Normative requirements in this specification are informed by:
- Annex A — Risk Surface & Harm Matrix
- Annex B — NIST & SDO Crosswalk