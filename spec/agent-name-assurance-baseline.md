# Agent Name Assurance & Governance Baseline (ANAGB) v0.2.0

## Status
Draft — Working Group Review

This release introduces **Assurance Levels (AL1–AL4)** and standardized **evidence bundles** for repeatable audits.

## Normative Language
The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, and **MAY** are to be interpreted as described in RFC 2119.

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

### 5.1 Capability Discovery
- **ANAGB-AGT-01**: authenticated capability discovery.
- **ANAGB-AGT-02**: coarse-grained anonymous discovery (recommended).

### 5.2 Logging & Auditability
- **ANAGB-LOG-01**: log credential exchanges.
- **ANAGB-LOG-02**: tamper-evident logs.
- **ANAGB-LOG-03**: exportable, machine-readable logs.

### 5.3 Abuse Protection
- **ANAGB-ABUSE-01**: rate limiting.
- **ANAGB-ABUSE-02**: replay mitigation.

---

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

The following control IDs are normative requirements unless marked RECOMMENDED.

| Control ID | Title | Requirement |
|---|---|---|
| `ANAGB-UI-01` | Tier display | Implementations MUST display the verification tier explicitly wherever an agent name is rendered. |
| `ANAGB-UI-02` | No generic verified | Implementations MUST NOT present a generic “Verified” indicator without the tier context. |
| `ANAGB-UI-03` | High-risk step-up | High-risk transactions MUST verify revocation status for AN-2 and AN-3 prior to execution. |
| `ANAGB-RES-01` | Cryptographic binding | Name-to-DID binding MUST be cryptographically provable. |
| `ANAGB-RES-02` | Replay resistance | Bindings MUST be replay-resistant using nonce and/or timestamp mechanisms. |
| `ANAGB-RES-03` | TLS required | All resolution endpoints MUST use TLS. |
| `ANAGB-RES-04` | HSTS recommended | HSTS SHOULD be enabled on resolution endpoints. |
| `ANAGB-RES-05` | Drift monitoring | Implementations MUST monitor for DNS drift and/or domain takeover indicators and alert on unexpected binding changes. |
| `ANAGB-RES-06` | Transparency log | For AN-2 and AN-3, implementations SHOULD publish binding events to an append-only transparency log. |
| `ANAGB-PRIV-01` | Data minimization default | Public agent pages MUST default to minimal disclosure. |
| `ANAGB-PRIV-02` | Explicit reveal | Sensitive attributes MUST require explicit user action to reveal. |
| `ANAGB-PRIV-03` | No auto-share | Agent pages MUST NOT auto-initiate credential exchange flows. |
| `ANAGB-PRIV-04` | Consent required | Credential exchange MUST require explicit consent. |
| `ANAGB-PRIV-05` | Noindex support | Implementations SHOULD support noindex directives for pages and sensitive contexts. |
| `ANAGB-PRIV-06` | Scrape controls | Automated scraping SHOULD be rate-limited and bulk enumeration SHOULD be restricted. |
| `ANAGB-AGT-01` | Authenticated capability discovery | Detailed capability discovery MUST require authentication. |
| `ANAGB-AGT-02` | Coarse anonymous discovery | Anonymous capability discovery SHOULD return coarse-grained responses only. |
| `ANAGB-LOG-01` | Exchange logging | All credential exchanges MUST be logged. |
| `ANAGB-LOG-02` | Tamper-evident logs | Logs MUST be tamper-evident. |
| `ANAGB-LOG-03` | Exportable logs | Audit logs MUST be exportable in a machine-readable format. |
| `ANAGB-ABUSE-01` | Rate limiting | Endpoints MUST implement rate limiting. |
| `ANAGB-ABUSE-02` | Replay mitigation | Replay attacks MUST be mitigated via nonces and validation. |
| `ANAGB-AI-01` | AI usage disclosure | Where AI influences decisions, AI usage MUST be disclosed. |
| `ANAGB-AI-02` | Decision categories | Decision categories influenced by AI MUST be documented. |
| `ANAGB-AI-03` | Redress mechanism | A redress mechanism MUST exist for AI-influenced decisions. |
| `ANAGB-AI-04` | Human override | Blocking contact, revoking credentials, or executing delegated actions MUST allow human override. |
| `ANAGB-AI-05` | Delegation bounded | Autonomous agents MUST implement scoped delegation, expiration timestamps, transaction caps, and revocation endpoints. |
| `ANAGB-AI-06` | Authority non-implication | AI identity MUST NOT imply authority. Authority MUST be explicitly delegated and bounded. |
| `ANAGB-IR-01` | Incident response plan | Implementations MUST maintain a documented incident response plan. |
| `ANAGB-IR-02` | Key rotation | Key rotation MUST be supported. |
| `ANAGB-IR-03` | Machine-verifiable revocation | Revocation status MUST be machine-verifiable. |
| `ANAGB-IR-04` | Safe suspension | Name suspension MUST NOT enable impersonation. |

---

## Annex References
Normative requirements in this specification are informed by:
- Annex A — Risk Surface & Harm Matrix
- Annex B — NIST & SDO Crosswalk