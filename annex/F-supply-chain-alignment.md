# Annex F — Software supply chain & SBOM alignment

## Purpose

This annex operationalizes high-assurance expectations for build integrity, provenance, and dependency transparency for agent implementations.

- For AL3/AL4, treat build provenance as a **first-class audit artifact** (not a nice-to-have).
- For AL2+, include SBOMs (SPDX or CycloneDX) to enable verifier cost containment and incident response.

## Crosswalk artifacts

- Machine-readable crosswalk: `crosswalk/supply-chain.yml`

## High-level mapping (illustrative)

| ANAGB hook | External standard hook | Notes |
|---|---|---|
| AL3/AL4 attestation + security evidence | SLSA provenance | Pipeline hardening and provenance reduce compromise risk. |
| Secure SDLC governance evidence | NIST SSDF (SP 800-218) | Maps to development practices and reviews. |
| SBOM artifact (AL2+) | SPDX / CycloneDX | Dependency transparency for audits and response. |


## How to use this annex

1. Start from your target **Assurance Level** (AL2–AL4) in `docs/assurance-levels.md`.
2. Build (or adapt) your **evidence bundle** using `evidence-bundles/evidence-bundle.schema.json`.
3. Use the crosswalk mapping to identify *which existing controls / audit artifacts* in your org already satisfy ANAGB expectations.
4. Record the mapping in your evidence bundle via `standards_alignment` (optional field; see schema).
