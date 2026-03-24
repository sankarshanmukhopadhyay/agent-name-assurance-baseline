# Threat Matrix

This matrix maps adversary goals → common attack paths → the ANAGB controls that mitigate them.

**How to read this**
- The goal is the attacker’s outcome.
- Attack paths are typical ways they get there.
- Controls are the baseline safeguards ANAGB expects implementers to have in place.

> Note: This is a threat modeling aid. It is **not** a complete security review of any implementation.

## 1) Impersonation and brand hijack

| Adversary goal | Attack paths | Primary ANAGB controls |
|---|---|---|
| Make a fake “official” agent look legitimate | Lookalike names (homoglyphs), copycat profile pages, deceptive “Verified” UI | `ANAGB-UI-01`, `ANAGB-UI-02`, `ANAGB-ABUSE-01`, `ANAGB-ABUSE-02` |
| Bind a name to an attacker-controlled DID | Weak binding proofs, replayed binding assertions, missing key hygiene | `ANAGB-RES-01`, `ANAGB-RES-02`, `ANAGB-RES-03`, `ANAGB-IR-02` |
| Keep impersonation alive after discovery | No revocation channel, stale caches, unverifiable revocation state | `ANAGB-IR-03`, `ANAGB-UI-03`, `ANAGB-IR-01` |

## 2) Phishing amplification and trust inflation

| Adversary goal | Attack paths | Primary ANAGB controls |
|---|---|---|
| Trick users into disclosing credentials or signing transactions | Misleading tier display, forced-click CTAs from an agent page, step-up missing for high-risk actions | `ANAGB-UI-01`, `ANAGB-UI-02`, `ANAGB-UI-03`, `ANAGB-LOG-01` |
| Inflate “trust” by abusing social proof | Bulk creation of “verified-looking” agents, review/rating manipulation, badge farming | `ANAGB-ABUSE-01`, `ANAGB-ABUSE-02`, `ANAGB-LOG-02`, `ANAGB-LOG-03` |

## 3) Privacy harm and surveillance-by-enumeration

| Adversary goal | Attack paths | Primary ANAGB controls |
|---|---|---|
| Harvest agent pages at scale | Crawling, scraping, bulk enumeration over public endpoints | `ANAGB-PRIV-06`, `ANAGB-RES-05`, `ANAGB-RES-04`, `ANAGB-LOG-02` |
| Expose sensitive linkage and contact surfaces | Overly rich discovery responses, unredacted metadata, correlation vectors | `ANAGB-PRIV-01`, `ANAGB-PRIV-02`, `ANAGB-PRIV-03`, `ANAGB-AGT-02` |
| Force indexing of sensitive content | Search engine indexing of agent pages and logs | `ANAGB-PRIV-05`, `ANAGB-PRIV-04` |

## 4) Authority confusion and unsafe delegation

| Adversary goal | Attack paths | Primary ANAGB controls |
|---|---|---|
| Make an AI agent appear empowered to act | “AI identity implies authority”, ambiguous delegation statements, missing bounds | `ANAGB-AI-06`, `ANAGB-AI-01`, `ANAGB-AI-02` |
| Induce an agent to perform unsafe actions | Prompt injection via agent pages, tool abuse, jailbreak-through-context | `ANAGB-AI-03`, `ANAGB-AI-04`, `ANAGB-AI-05`, `ANAGB-LOG-03` |
| Abuse machine-to-machine interaction surfaces | Over-permissive capabilities, missing consent/audit trails | `ANAGB-AGT-01`, `ANAGB-LOG-01`, `ANAGB-LOG-02` |

## 5) Operational disruption and recovery failures

| Adversary goal | Attack paths | Primary ANAGB controls |
|---|---|---|
| Knock out resolution/discovery | Rate spikes, endpoint abuse, TLS downgrade, cache poisoning | `ANAGB-RES-05`, `ANAGB-RES-04`, `ANAGB-LOG-02` |
| Prevent clean recovery after compromise | No IR plan, no key rotation, revocation breaks identity continuity | `ANAGB-IR-01`, `ANAGB-IR-02`, `ANAGB-IR-03`, `ANAGB-IR-04` |


## A2A-specific additions

| Threat | Description | Typical control response |
|---|---|---|
| Agent Card drift | The public Agent Page and the machine-readable Agent Card diverge, creating trust confusion. | `ANAGB-A2A-02`, `ANAGB-RES-05` |
| Cross-tenant task leakage | Task or context identifiers can be replayed or guessed across tenants or principals. | `ANAGB-A2A-04`, `ANAGB-ABUSE-02` |
| Unsafely trusted callback | Push notifications or webhook updates are accepted without sufficient authenticity checks. | `ANAGB-A2A-05` |
| Artifact trust inflation | A named agent returns unsupported or ambiguous output that is over-trusted by relying parties. | `ANAGB-A2A-06`, `ANAGB-AI-06` |
| Mis-bound verified identity | The Agent Card carries a verification claim that is not coherently tied to the accountable operator or signing key. | `ANAGB-A2A-07`, `ANAGB-A2A-08` |
| Stale trust description | Clients rely on expired, revoked, or cached ANAB-over-A2A metadata. | `ANAGB-A2A-09`, `ANAGB-IR-03` |
| Silent trust downgrade or upgrade | A client ignores missing or unverifiable extension data and proceeds as if the higher-assurance trust claim still holds. | `ANAGB-A2A-10`, `ANAGB-UI-02` |
