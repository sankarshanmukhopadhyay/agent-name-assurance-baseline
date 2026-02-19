
# Agent Name Assurance & Governance Baseline (ANAGB) v0.1

## Status
Draft – Working Group Review

---

# 1. Introduction

This specification defines assurance, security, privacy, and AI governance requirements for systems implementing:

- Agent Names
- Agent Pages
- Agent-to-Agent interaction
- AI-mediated decisioning within decentralized agent ecosystems

The objective is to prevent phishing amplification, trust inflation, privacy harm, authority confusion, and unsafe AI delegation while enabling human-readable identifiers layered over decentralized identifiers (DIDs).

---

# 2. Normative Language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, and MAY are to be interpreted as described in RFC 2119.

---

# 3. Agent Name Verification Tiers

Implementations MUST classify agent name bindings according to one of the following tiers.

## 3.1 Tier Definitions

| Tier | Label | Binding Strength | Required Evidence | Revocation Requirement |
|------|-------|-----------------|------------------|-----------------------|
| AN-0 | Self-Asserted | Weak | DID includes agent name | None |
| AN-1 | Domain-Control Verified | Medium | Cryptographic proof of domain control bound to DID | Periodic revalidation (≤90 days) |
| AN-2 | Trust Framework Verified | Strong | Verifiable Credential (VC) from recognized issuer | Continuous revocation checking |
| AN-3 | High Assurance Verified | Very Strong | Legal entity validation + operational security controls | Real-time revocation + transparency logging |

## 3.2 UI Signaling Requirements

1. Verification tier MUST be displayed explicitly.
2. Implementations MUST NOT use generic “Verified” indicators without tier context.
3. High-risk transactions MUST require revocation verification for AN-2 and AN-3.

---

# 4. Name Resolution & Cryptographic Binding

## 4.1 Binding Integrity

- Name-to-DID binding MUST be cryptographically provable.
- Bindings MUST be replay-resistant using nonce or timestamp mechanisms.
- Bindings SHOULD be published to an append-only transparency log for AN-2 and AN-3.

## 4.2 Transport Security

- Resolution endpoints MUST use TLS.
- HSTS SHOULD be enabled.
- Certificate mis-issuance monitoring SHOULD be implemented.

## 4.3 Monitoring & Drift Detection

- Implementations MUST monitor for DNS drift or domain takeover.
- Unexpected binding changes MUST trigger alerts.

---

# 5. Agent Page Security & Privacy Baseline

## 5.1 Data Minimization

- Public agent pages MUST default to minimal disclosure.
- Sensitive attributes MUST require explicit user action.
- Implementations SHOULD support privacy profiles (individual vs organizational).

## 5.2 Indexing & Scraping Controls

- Pages SHOULD support noindex directives.
- Automated scraping SHOULD be rate-limited.
- Bulk capability enumeration MUST be restricted.

## 5.3 Consent & Interaction Controls

- Credential exchange MUST require explicit consent.
- Pages MUST NOT auto-initiate credential flows.
- All outbound trust actions MUST present clear origin information.

---

# 6. Agent-to-Agent Interaction Controls

## 6.1 Capability Discovery

- Detailed capability discovery MUST require authentication.
- Anonymous discovery SHOULD return coarse-grained responses only.

## 6.2 Logging & Auditability

- All credential exchanges MUST be logged.
- Logs MUST be tamper-evident.
- Logs MUST be exportable in machine-readable format.

## 6.3 Abuse Protection

- Endpoints MUST implement rate limiting.
- Replay attacks MUST be mitigated.
- An incident response plan MUST be documented.

---

# 7. AI Decisioning Guardrails

This section applies where AI systems influence contact mediation, trust scoring, credential evaluation, or delegated authority execution.

## 7.1 Disclosure & Transparency

- AI usage MUST be disclosed.
- Decision categories MUST be documented.
- A redress mechanism MUST exist.

## 7.2 Delegated Authority Constraints

Autonomous AI agents MUST implement:

- Scoped delegation
- Expiration timestamps
- Transaction caps
- Revocation endpoints

AI identity MUST NOT imply authority. Authority MUST be explicitly delegated and bounded.

## 7.3 Human Override

Blocking contact, revoking credentials, or executing delegated actions MUST allow human override.

---

# 8. Conformance Profiles

| Profile | Requirements |
|----------|-------------|
| Core | AN-1 + Sections 4–5 |
| Deploy | AN-2 + Sections 4–6 |
| Transact | Deploy + Section 7 |
| Enterprise | AN-3 + Transparency Log + Formal Governance Attestation |

Conformance claims MUST specify the adopted profile.

---

# 9. Incident Handling & Recovery

- Key rotation MUST be supported.
- Revocation MUST be machine-verifiable.
- Identity continuity mechanisms SHOULD exist.
- Name suspension MUST NOT enable impersonation.

---

# 10. Security & Privacy Considerations

This specification addresses phishing, trust inflation, enumeration abuse, AI bias, privacy overexposure, authority creep, and resolution compromise.

Residual risk MUST be documented by implementers as part of deployment-specific risk assessments.

---

# 11. Future Work

- Transparency log standardization
- Formal threat model mapping
- Automated conformance test suite
- Interoperable UI signaling guidelines


---

# Annex References

Normative requirements in this specification are informed by:
- Annex A — Risk Surface & Harm Matrix
- Annex B — NIST & SDO Crosswalk

