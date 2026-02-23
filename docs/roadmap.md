# Roadmap (Schedule-Free)

This roadmap captures the intended evolution of the **Agent Name Assurance Baseline (ANAGB)** repository.
It is a **directional record** of what we want to build next, and deliberately **does not** include delivery dates.

## Product direction

The north star is simple: make **agent naming** an auditable, interoperable, and automation-friendly assurance surface that can be
adopted by ecosystems (wallets, agents, registries, verifiers) without bespoke interpretation.

## 1. Assurance level maturity

- Tighten and clarify AL1–AL4 definitions, especially boundary cases (human-in-the-loop, delegated agents, org-issued agents).
- Add explicit “what must be true” statements per level (normative, testable language).
- Introduce “upgrade paths” (how AL2 can become AL3, AL3 to AL4) with required evidence deltas.

**Outcome:** assurance levels that can be implemented and audited without interpretive dance.

## 2. Evidence bundles and audit artifacts

- Publish a standardized **evidence bundle** model per assurance level (required vs optional artifacts).
- Provide example bundles (redacted / synthetic) showing “good enough” vs “best practice”.
- Expand checklist coverage so audits can be executed consistently across implementations.

**Outcome:** predictable audits and repeatable compliance.

## 3. Conformance model hardening

- Evolve the conformance schema(s) to fully express AL requirements, profiles, and exceptions.
- Add additional sample conformance declarations for common archetypes (startup agent, enterprise agent, public-sector agent).
- Improve validation rules and error messages to be machine-consumable.

**Outcome:** machine-operable conformance, not prose-only compliance.

## 4. Threat model and misuse-case coverage

- Expand the threat model with structured misuse cases (impersonation, squatting, homograph attacks, reputation laundering).
- Add mitigations mapped to controls and assurance levels.
- Maintain a concise “known gaps / assumptions” register that stays honest over time.

**Outcome:** security posture that is explicit, reviewable, and improvable.

## 5. Interop and ecosystem integration

- Provide guidance for integration with trust registries / discovery layers (where agent names are published and resolved).
- Add compatibility notes for VC/DID ecosystems and existing naming/identifier schemes.
- Define minimal interoperability hooks (what a verifier needs to rely on an agent name claim).

**Outcome:** adoption path across ecosystems instead of a standalone document.

## 6. Reference material and implementation guidance

- Add worked examples (end-to-end) with assumptions and decision logs.
- Publish implementer guidance for common stacks (web PKI, DID-based, registry-backed, enterprise IAM-backed).
- Provide “design patterns” and “anti-patterns” for implementers.

**Outcome:** faster adoption, fewer foot-guns.

## 7. Repository UX and release discipline

- Improve navigation: link spec → conformance → annexes → threat model with a clear “start here” flow.
- Add a CHANGELOG and explicit versioning/compatibility policy (what breaks, what doesn’t).
- Expand CI checks (schema validation, markdown linting, link checking) for sustained quality.

**Outcome:** a repo that behaves like product-grade infrastructure.

## Tracking philosophy

This roadmap is a living artifact. Items may evolve, merge, or reprioritize based on ecosystem feedback and downstream dependencies.
**No schedule is implied.**
