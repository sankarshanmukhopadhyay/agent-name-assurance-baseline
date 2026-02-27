# Annexes

This folder contains supporting (non-normative) reference material that makes the baseline easier to adopt, audit, and align to existing standards.

The annex set is intentionally split into:

- **Human-readable annex documents** (`annex/*.md`) for implementers and reviewers
- **Machine-readable crosswalk registries** (`crosswalk/*.yml`) for tooling and automation

## Annex index

- **Annex A — Risk surface matrix:** `annex/A-risk-surface-matrix.md`
- **Annex B — NIST crosswalk matrix:** `annex/B-nist-crosswalk-matrix.md`
- **Annex C — OWASP alignment (ASVS + API Top 10):** `annex/C-owasp-alignment.md`
- **Annex D — ISO 27001/27002 alignment:** `annex/D-iso27001-alignment.md`
- **Annex E — SOC 2 (Trust Services Criteria) alignment:** `annex/E-soc2-alignment.md`
- **Annex F — Software supply chain & SBOM alignment (SLSA, SSDF, SPDX/CycloneDX):** `annex/F-supply-chain-alignment.md`
- **Annex G — Privacy alignment (ISO 27701 + GDPR concepts):** `annex/G-privacy-alignment.md`
- **Annex H — AI governance alignment (ISO 42001, ISO 23894, OECD, EU AI Act pointers):** `annex/H-ai-governance-alignment.md`
- **Annex I — Identity & crypto alignment (W3C DID/VC, IETF JOSE/COSE, FIDO2/WebAuthn):** `annex/I-identity-and-crypto-alignment.md`

## Machine-readable crosswalk registry

Each annex that references external standards has a corresponding entry in `crosswalk/`.

Design goals:
- Small, stable identifiers for standards
- Mappings that reference **ANAGB artifacts** (controls, evidence categories, required artifacts, and/or assurance levels)
- Consumable by CI and external validation tools without scraping prose

See: `crosswalk/README.md`
