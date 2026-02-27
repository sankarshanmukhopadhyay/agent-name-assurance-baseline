# Changelog

All notable changes to this project will be documented in this file.

This repo follows semantic versioning as described in `docs/versioning-and-compatibility.md`.

## [0.2.0] - 2026-02-27

### Added
- Assurance Levels (AL1–AL4) with normative “what must be true” statements and upgrade paths (`docs/assurance-levels.md`).
- Standardized evidence bundle model + JSON schema + synthetic examples (`evidence-bundles/`).
- Implementer guidance with worked flow, stack guidance, patterns and anti-patterns (`docs/implementer-guidance.md`).
- Additional sample conformance declarations for common archetypes (`conformance/samples/`).

### Changed
- Conformance schemas updated to express assurance level and evidence bundle pointers.
- Checklist expanded for audit readiness and AL requirements.

### Quality
- CI validation expanded (schema checks, link checks, markdown lint).
- Repo navigation improved with a “start here” flow in README.

## [0.1.0] - Initial draft
- Initial normative baseline, control catalog, conformance tooling, annexes, and threat model.
