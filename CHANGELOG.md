# Changelog

All notable changes to this project will be documented in this file.

This repo follows semantic versioning as described in `docs/versioning-and-compatibility.md`.

## [Unreleased]

## [0.8.0] - 2026-04-20

### Added
- Added `docs/runtime-identity-lifecycle.md` as experimental guidance for runtime identity activation, delegation, revocation, rotation, and decommissioning.
- Added `docs/experimental/agent-governance-toolkit-alignment.md` to record the upstream conceptual boundary.

### Changed
- Refreshed README, docs index, assurance-level guidance, implementer guidance, and applicability notes to make higher-assurance runtime identity expectations legible without changing the normative ANAB controls.

## [0.7.0] - 2026-03-31

### Added
- Optional ODRL policy-reference guidance for usage, disclosure, attribution, and notice conditions.
- Example ODRL policy artifact and a lightweight ANAB ↔ ODRL crosswalk.

### Changed
- Clarified in the normative spec that ODRL publication does not replace ANAB controls, declarations, or evidence bundles.


### Added
- Added `docs/anab-over-a2a-binding.md` as a detailed binding specification for carrying ANAB trust metadata in A2A Agent Cards through the A2A extension model.
- Added `conformance/anab-over-a2a-description-extension.schema.json` and `conformance/samples/a2a-agent-card-with-anab-extension.json` for machine-readable binding validation and implementation guidance.
- Added four new A2A-facing controls: `ANAGB-A2A-07` through `ANAGB-A2A-10`.

### Changed
- Refreshed upstream references to point at `https://github.com/trustoverip/dtgwg-agent-names-tf` instead of treating the local extract as the upstream source of truth.
- Expanded A2A alignment, applicability, checklist, and threat model content to cover verified-identity extensions, freshness, and downgrade-safe trust handling.

## [0.6.0] - 2026-03-24

### Added
- Added `docs/dcas-composition.md` to explain how ANAB declarations and evidence bundles compose with DCAS evaluation workflows.
- Added `conformance/samples/dcas-ready-enterprise-agent.json` as a verifier-facing sample declaration with evidence bundle and standards alignment pointers.

### Changed
- Refreshed README navigation so cross-repo verifier composition is visible from the front door.
- Updated roadmap tracking to record delivery of DCAS-ready composition examples.

## [0.5.1] - 2026-03-14

### Changed
- Updated ecosystem references from `schemas` to `trust-infrastructure-schemas`.
- Clarified that ANAB consumes canonical Assurance Level semantics from the OTAM-aligned trust artifact repository.
- Refreshed architecture, interoperability, and transport docs to describe ANAB as a domain baseline layered on canonical trust artifact schemas.

### Compatibility
- No ANAB control semantics, JSON schema bodies, or conformance requirements changed.

## [0.5.0] - 2026-03-14

### Added
- Explicit A2A alignment guidance in `docs/a2a-alignment.md`.
- New Annex K for A2A concept-to-control mapping.
- Six A2A-facing controls covering signed metadata, page/card consistency, metadata gating, task scoping, callback trust boundaries, and media-type safety.

### Changed
- Normative baseline updated to treat Agent Pages and Agent Cards as a coherent trust surface when used in A2A ecosystems.
- Applicability matrix and checklist updated to show when A2A-facing controls apply.
- Threat model expanded for Agent Card drift, cross-tenant task leakage, callback trust, and artifact trust inflation.

### Quality
- README and docs landing page updated so A2A composition is discoverable without tribal knowledge.

## [0.4.0] - 2026-03-05

### Added
- Ecosystem interoperability documentation and upstream references (dtg-credentials, verifiable-trust-infrastructure, openVTC).
- Non-normative architecture diagram for cross-repo composition.

## [0.2.2] - 2026-03-05

### Added
- Pinned upstream working extract for *Agent Names and Agent Pages* under `upstream/agent-names-and-agent-pages/` to support control traceability.
- Docs landing page for GitHub Pages (`docs/index.md`) and Pages guidance (`docs/github-pages.md`).
- CI dependency pinning via `requirements-ci.txt`.
- `VERSION` file for explicit release pinning.

### Fixed
- CI now installs all required Python dependencies (including YAML support) so validation runs cleanly on a fresh runner.

## [0.2.1] - 2026-02-27

### Added
- Expanded standards annex coverage (OWASP, ISO 27001/27002, SOC 2, supply chain, privacy, AI governance, identity/crypto) with an annex index (`annex/README.md`).
- Machine-readable crosswalk registry for standards alignment (`crosswalk/*.yml`).
- Optional `standards_alignment` metadata in evidence bundle and conformance declaration schemas for traceable mappings.

## [0.2.0] - 2026-02-27

### Added
- Assurance Levels (AL1–AL4) with normative “what must be true” statements and upgrade paths (`docs/assurance-levels.md`).
- Standardized evidence bundle model + JSON schema + synthetic examples (`evidence-bundles/`).
- Implementer guidance with worked flow, stack guidance, patterns and anti-patterns (`docs/implementer-guidance.md`).
- Additional sample conformance declarations for common archetypes (`conformance/samples/`).

## [0.1.0] - Initial draft
- Initial normative baseline, control catalog, conformance tooling, annexes, and threat model.
