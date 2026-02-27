# agent-name-assurance-baseline

![Version](https://img.shields.io/badge/version-0.2.1-blue)
![Status](https://img.shields.io/badge/status-draft-orange)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Conformance](https://img.shields.io/badge/conformance-machine--readable-success)
![Alignment](https://img.shields.io/badge/aligned-multi-blueviolet)

## About
A normative assurance and governance baseline for **Agent Names** and **Agent Pages**. Defines verification tiers, control IDs, security/privacy safeguards, AI guardrails, and **machine-checkable conformance declarations** aligned with NIST frameworks to reduce phishing amplification, trust inflation, privacy harm, and authority drift.

## Start here (fast path)

1. Read the **normative spec**: `spec/agent-name-assurance-baseline.md`  
2. Choose your **Tier** (AN-0…AN-3) + **Profile** (Core/Deploy/Transact/Enterprise): `conformance/applicability-matrix.md`  
3. Decide your **Assurance Level** (AL1–AL4): `docs/assurance-levels.md`  
4. Publish a **conformance declaration** + **evidence bundle**:
   - Declaration schema: `conformance/conformance-declaration.schema.json`
   - Evidence bundle schema: `evidence-bundles/evidence-bundle.schema.json`
5. Use implementation guidance + patterns: `docs/implementer-guidance.md`

## Contents
- **Normative spec:** `spec/agent-name-assurance-baseline.md`
- **Control catalog:** embedded in the spec (Control IDs like `ANAGB-RES-01`, `ANAGB-AI-03`)
- **Applicability matrix (tier/profile):** `conformance/applicability-matrix.md`
- **Evidence bundles:** `evidence-bundles/README.md`
- **Conformance**
  - Conformance checklist: `conformance/checklist.md`
  - Conformance declaration template (Markdown): `conformance/conformance-declaration-template.md`
  - Conformance declaration schema (JSON Schema): `conformance/conformance-declaration.schema.json`
  - Sample conformance declaration: `conformance/sample-conformance-declaration.json`
  - Conformance claim schema (implemented controls list): `conformance/anagb-conformance-schema.json`
- **Annexes**
  - Annex index: `annex/README.md`
  - Risk surface matrix: `annex/A-risk-surface-matrix.md`
  - NIST crosswalk: `annex/B-nist-crosswalk-matrix.md`
  - OWASP alignment (ASVS + API Top 10): `annex/C-owasp-alignment.md`
  - ISO 27001/27002 alignment: `annex/D-iso27001-alignment.md`
  - SOC 2 alignment: `annex/E-soc2-alignment.md`
  - Supply chain & SBOM alignment: `annex/F-supply-chain-alignment.md`
  - Privacy alignment: `annex/G-privacy-alignment.md`
  - AI governance alignment: `annex/H-ai-governance-alignment.md`
  - Identity & crypto alignment: `annex/I-identity-and-crypto-alignment.md`
  - Machine-readable crosswalk registry: `crosswalk/README.md`
- **Threat model:** `threat-model/threat-matrix.md`
- **Repo validation tool:** `tools/validate_repo.py` (used by CI)


## Integration with DPI AI Governance Frameworks

This repository provides an **identity assurance substrate** for named agents. The DPI AI Governance repositories consume this work via a lightweight interface contract (risk-tier ↔ minimum assurance expectation) and MUST NOT duplicate ANAB annexes.

- DPI AI crosswalk annex: `annex/J-dpi-ai-crosswalk.md`

## Conformance model
Implementers SHOULD publish a **signed** conformance declaration using `conformance/conformance-declaration.schema.json` and include evidence pointers for each implemented control ID.

## Conformance quickstart (practical workflow)
1. **Pick your target tier and profile**
   - Tiers: **AN-0 … AN-3** (binding strength)
   - Profiles: **Core / Deploy / Transact / Enterprise** (operational scope)
   - Use `conformance/applicability-matrix.md` to see which controls are required.

2. **Start from the template**
   - Human-readable: `conformance/conformance-declaration-template.md`
   - Machine-readable example: `conformance/sample-conformance-declaration.json`

3. **Fill evidence links per control**
   - Config, logs, test outputs, runbooks, transparency log references, third-party attestations, etc.

4. **Validate locally (same checks as CI)**
   ```bash
   python -m pip install jsonschema
   python tools/validate_repo.py
   ```

5. **Publish and reference**
   - Host the signed declaration at a stable URL under your Agent Page / docs site.
   - Link to it from the Agent Page so verifiers and relying parties can fetch it deterministically.

## Release discipline
- Changelog: `CHANGELOG.md`
- Versioning & compatibility: `docs/versioning-and-compatibility.md`

## License
Apache 2.0
