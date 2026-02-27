# Annex I — Identity & cryptography alignment (DID/VC, JOSE/COSE, FIDO2/WebAuthn)

## Purpose

This annex provides practical identity-binding and cryptographic alignment options for agent name/page assertions across multiple deployment stacks.

- Use DID/VC patterns when you need decentralized, interoperable claim verification.
- Use JOSE/COSE to document your signing/encryption profile and key management choices.
- For AL3/AL4, prefer phishing-resistant authentication for privileged operations when feasible.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/identity-and-crypto.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| Identity binding evidence | W3C DID/VC | Interoperable assertion formats and verification. |
| Signature/encryption profile evidence | IETF JOSE/COSE | Document profile and key mgmt decisions. |
| Privileged ops authentication (AL3/AL4) | FIDO2/WebAuthn | Phishing-resistant operator authentication. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
