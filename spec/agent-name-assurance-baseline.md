# Agent Name Assurance & Governance Baseline (ANAGB) v0.1

## Normative Language

The key words MUST, MUST NOT, REQUIRED, SHALL, SHALL NOT, SHOULD, SHOULD NOT, RECOMMENDED, and MAY are to be interpreted as described in RFC 2119.

## Verification Tiers

AN-0: Self-Asserted  
AN-1: Domain-Control Verified  
AN-2: Trust Framework Verified  
AN-3: High Assurance Verified  

## Security Baseline

- Name-to-DID binding MUST be cryptographically provable.
- TLS MUST be enforced.
- Revocation MUST be machine-verifiable.
- Audit logs MUST be tamper-evident.

## AI Guardrails

- AI usage MUST be disclosed.
- Human override MUST exist.
- Delegation MUST be scoped, revocable, and time-bound.
