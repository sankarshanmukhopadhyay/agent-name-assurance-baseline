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

### Status
✅ **Completed (v0.2.0)**

Delivered:
- Normative AL1–AL4 definitions with boundary cases + upgrade paths: `docs/assurance-levels.md`
- Checklist expansion for audit readiness: `conformance/checklist.md`
- Conformance schema support for `assurance_level` + evidence bundle pointers

## 2. Evidence bundles and audit artifacts

- Publish a standardized **evidence bundle** model per assurance level (required vs optional artifacts).
- Provide example bundles (redacted / synthetic) showing “good enough” vs “best practice”.
- Expand checklist coverage so audits can be executed consistently across implementations.

**Outcome:** predictable audits and repeatable compliance.

### Status
✅ **Completed (v0.2.0)**

Delivered:
- Standardized evidence bundle model + JSON schema: `evidence-bundles/evidence-bundle.schema.json`
- Synthetic example bundles (“good enough” vs “best practice”): `evidence-bundles/examples/`
- Checklist expansion for repeatable audit execution: `conformance/checklist.md`

## 3. Conformance model hardening

- Evolve the conformance schema(s) to fully express AL requirements, profiles, and exceptions.
- Add additional sample conformance declarations for common archetypes (startup agent, enterprise agent, public-sector agent).
- Improve validation rules and error messages to be machine-consumable.

**Outcome:** machine-operable conformance, not prose-only compliance.

### Status
✅ **Completed (v0.2.0)**

Delivered:
- Conformance schemas updated to express AL claims + evidence bundle pointers + exceptions
- Additional sample declarations (startup, enterprise, public sector): `conformance/samples/`
- Improved validation tooling output for machine parsing: `tools/validate_repo.py`

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

### Status
✅ **Completed (v0.2.0)**

Delivered:
- Worked end-to-end adoption flow + decision log expectations: `docs/implementer-guidance.md`
- Stack guidance (Web PKI, DID-based, registry-backed, enterprise IAM-backed)
- Design patterns and anti-patterns for implementers

## 7. Repository UX and release discipline

- Improve navigation: link spec → conformance → annexes → threat model with a clear “start here” flow.
- Add a CHANGELOG and explicit versioning/compatibility policy (what breaks, what doesn’t).
- Expand CI checks (schema validation, markdown linting, link checking) for sustained quality.

**Outcome:** a repo that behaves like product-grade infrastructure.

### Status
✅ **Completed (v0.2.0)**

Delivered:
- Clear “start here” navigation flow: `README.md`
- CHANGELOG + explicit versioning/compatibility policy: `CHANGELOG.md`, `docs/versioning-and-compatibility.md`
- Expanded CI checks: schema validation, markdown linting, link checking (`.github/workflows/ci.yml`)

## Tracking philosophy

This roadmap is a living artifact. Items may evolve, merge, or reprioritize based on ecosystem feedback and downstream dependencies.
**No schedule is implied.**


## 8. Standards coverage and machine-readable crosswalk registry

- Expand annex coverage to include major adjacent standards used in real audits and procurement:
  - OWASP (ASVS, API Security Top 10)
  - ISO 27001/27002
  - SOC 2 (Trust Services Criteria)
  - Software supply chain standards (SLSA, NIST SSDF, SBOM formats)
  - Privacy standards (ISO 27701 + GDPR concepts)
  - AI governance standards (ISO 42001, ISO 23894, OECD, EU AI Act pointers)
  - Identity and crypto standards (W3C DID/VC, IETF JOSE/COSE, FIDO2/WebAuthn)
- Provide **machine-readable** mappings (YAML/JSON) so the crosswalk is usable by tooling (not just prose).
- Wire crosswalk references into evidence bundles and conformance declarations as optional, non-normative metadata.

**Outcome:** faster adoption and higher audit interoperability without weakening the normative core.

### Status
✅ **Completed (v0.2.2)**

Delivered:
- Annex index and expanded annex set: `annex/README.md`
- Machine-readable crosswalk registry: `crosswalk/README.md`
- Crosswalk YAMLs for OWASP, ISO, SOC2, supply chain, privacy, AI governance, and identity/crypto: `crosswalk/*.yml`
- Optional `standards_alignment` field in schemas for traceable mapping:
  - Evidence bundles: `evidence-bundles/evidence-bundle.schema.json`
  - Conformance declarations: `conformance/conformance-declaration.schema.json`


## 9. A2A alignment and task trust surfaces

- Add explicit controls for signed Agent Cards, task/context scoping, authenticated callbacks, and media-type safety.
- Publish ANAB guidance for composition with A2A and DCAS.
- Expand the threat model to include cross-tenant task leakage and callback trust failure.

**Outcome:** named agents can participate in A2A ecosystems without pretending that name assurance alone proves operational safety.

### Status
✅ **Completed (v0.5.0)**

Delivered:
- A2A-facing controls in the normative baseline
- A2A alignment guidance: `docs/a2a-alignment.md`
- A2A annex: `annex/K-a2a-alignment.md`
- Threat model expansion for A2A task trust surfaces


## 10. DCAS-ready composition examples

- Provide a verifier-facing composition note showing how ANAB declarations and evidence bundles should be consumed by DCAS.
- Publish a sample declaration that keeps ANAB control identifiers intact while remaining easy for evaluators to consume.

**Outcome:** downstream evaluation can be automated without flattening the ANAB namespace into ad hoc local labels.

### Status
✅ **Completed (v0.6.0)**

Delivered:
- Composition note: `docs/dcas-composition.md`
- DCAS-ready sample declaration: `conformance/samples/dcas-ready-enterprise-agent.json`

## 11. ANAB-over-A2A description binding and verified-identity controls

- Replace stale upstream-document references with the current ToIP Agent Names TF repository reference.
- Define a detailed ANAB-over-A2A description extension using the A2A `AgentExtension` mechanism.
- Add controls for operator/card identity-proof coherence, issuer trust anchoring, freshness and revocation semantics, and downgrade-safe client behavior.
- Publish a machine-readable schema and example Agent Card using the binding.

**Outcome:** A2A deployments can publish verifier-consumable trust metadata without mistaking a signed Agent Card for a complete assurance model.

### Status
✅ **Completed (post-v0.6.0 working increment)**

Delivered:
- Detailed binding spec: `docs/anab-over-a2a-binding.md`
- Machine-readable extension schema: `conformance/anab-over-a2a-description-extension.schema.json`
- Sample Agent Card using the extension: `conformance/samples/a2a-agent-card-with-anab-extension.json`
- Expanded A2A control set: `ANAGB-A2A-07` through `ANAGB-A2A-10`
- Freshness review of upstream references across README, spec, and docs
