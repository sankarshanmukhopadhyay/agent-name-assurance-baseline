# Tier & Profile Applicability Matrix (ANAGB v0.1)

This document operationalizes **what you must implement** by combining:

- **Verification tiers** (AN-0 … AN-3): strength of the *name ↔ DID binding*  
- **Conformance profiles** (Core / Deploy / Transact / Enterprise): scope of operational controls

It is intended to remove “interpretation tax” for implementers and give reviewers a crisp checklist for audits.

---

## 1) Profiles at a glance

| Profile | Minimum Tier | Target Use Case | Baseline Requirement Set |
|---|---|---|---|
| **Core** | **AN-1** | Discovery + basic interaction, low-risk | Sections **3–4** + UI signaling |
| **Deploy** | **AN-2** | Public deployment, ecosystem interoperability | **Core** + Sections **5** and **7** + logging/abuse controls |
| **Transact** | **AN-2** | High-risk actions (delegation, payments, authority) | **Deploy** + Section **6** (AI controls **if AI used**) + enforced step-up |
| **Enterprise** | **AN-3** | High assurance, regulated / critical environments | **Transact** + transparency logging + stronger governance evidence |


Notes:
- A profile is a **minimum bar**, not a ceiling. Implementers MAY implement stricter tiers/controls and claim them.
- Where a control is **Conditional**, the conformance declaration SHOULD explicitly mark it `notApplicable` and explain why.

---

## 2) Control applicability by profile

**Legend**  
- **M** = MUST / MUST NOT (normative requirement)  
- **S** = SHOULD (recommended)  
- **C** = Conditional (apply only when the condition is true; otherwise mark `notApplicable` with rationale in declaration)  
- **—** = Not required for this profile


| Control ID | Title | Requirement Level | Core | Deploy | Transact | Enterprise | Notes |
|---|---|---:|:---:|:---:|:---:|:---:|---|
| `ANAGB-UI-01` | Tier display | M | M | M | M | M |  |
| `ANAGB-UI-02` | No generic verified | M | M | M | M | M |  |
| `ANAGB-UI-03` | High-risk step-up | M | C | C | M | M | Applies for **high-risk actions** (step-up & revocation checks). |
| `ANAGB-RES-01` | Cryptographic binding | M | M | M | M | M |  |
| `ANAGB-RES-02` | Replay resistance | M | M | M | M | M |  |
| `ANAGB-RES-03` | TLS required | M | M | M | M | M |  |
| `ANAGB-RES-04` | HSTS recommended | S | S | S | S | S |  |
| `ANAGB-RES-05` | Drift monitoring | M | M | M | M | M |  |
| `ANAGB-RES-06` | Transparency log | S | S | S | S | M | Elevated to **M** for Enterprise by profile requirement (transparency logging). |
| `ANAGB-PRIV-01` | Data minimization default | M | M | M | M | M |  |
| `ANAGB-PRIV-02` | Explicit reveal | M | M | M | M | M |  |
| `ANAGB-PRIV-03` | No auto-share | M | M | M | M | M |  |
| `ANAGB-PRIV-04` | Consent required | M | M | M | M | M |  |
| `ANAGB-PRIV-05` | Noindex support | S | S | S | S | S |  |
| `ANAGB-PRIV-06` | Scrape controls | S | S | S | S | S |  |
| `ANAGB-AGT-01` | Authenticated capability discovery | M | — | M | M | M |  |
| `ANAGB-AGT-02` | Coarse anonymous discovery | S | — | S | S | S |  |
| `ANAGB-LOG-01` | Exchange logging | M | — | M | M | M |  |
| `ANAGB-LOG-02` | Tamper-evident logs | M | — | M | M | M |  |
| `ANAGB-LOG-03` | Exportable logs | M | — | M | M | M |  |
| `ANAGB-ABUSE-01` | Rate limiting | M | — | M | M | M |  |
| `ANAGB-ABUSE-02` | Replay mitigation | M | — | M | M | M |  |
| `ANAGB-AI-01` | AI usage disclosure | M | — | — | C | C | Applies only when **AI-mediated decisioning/delegation** is in scope. |
| `ANAGB-AI-02` | Decision categories | M | — | — | C | C | Applies only when **AI-mediated decisioning/delegation** is in scope. |
| `ANAGB-AI-03` | Redress mechanism | M | — | — | C | C | Applies only when **AI-mediated decisioning/delegation** is in scope. |
| `ANAGB-AI-04` | Human override | M | — | — | C | C | Applies only when **AI-mediated decisioning/delegation** is in scope. |
| `ANAGB-AI-05` | Delegation bounded | M | — | — | C | C | Applies only when **AI-mediated decisioning/delegation** is in scope. |
| `ANAGB-AI-06` | Authority non-implication | M | — | — | C | C | Applies only when **AI-mediated decisioning/delegation** is in scope. |
| `ANAGB-IR-01` | Incident response plan | M | — | M | M | M |  |
| `ANAGB-IR-02` | Key rotation | M | — | M | M | M |  |
| `ANAGB-IR-03` | Machine-verifiable revocation | M | — | M | M | M |  |
| `ANAGB-IR-04` | Safe suspension | M | — | M | M | M |  |

---

## 3) How to use this matrix in your conformance declaration

In `conformance/conformance-declaration.schema.json`, implementers SHOULD:

1. Set `tier` to your binding tier (AN-0 … AN-3)
2. Set `profile` to your operational profile (Core / Deploy / Transact / Enterprise)
3. For each control you claim, include:
   - `implemented: true`
   - `evidence`: links, docs, test results, config, logs, or third-party attestations

For controls marked **C** (Conditional), either:
- Implement them and declare them normally, or
- Mark them `notApplicable` with a short rationale (e.g., “No AI mediation in this deployment”).

---

## 4) Recommended evidence bundles (practical defaults)

- **AN-1**: domain control proof + renewal job/cron evidence
- **AN-2**: issuer trust framework reference + revocation checking evidence
- **AN-3**: legal entity validation evidence + change control + incident response attestations
- **Deploy/Transact/Enterprise**: abuse monitoring metrics, logging retention configs, incident runbooks
