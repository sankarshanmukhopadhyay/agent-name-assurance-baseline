# agent-name-assurance-baseline

![Version](https://img.shields.io/badge/version-0.1-blue)
![Status](https://img.shields.io/badge/status-draft-orange)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Conformance](https://img.shields.io/badge/conformance-machine--readable-success)
![Alignment](https://img.shields.io/badge/aligned-NIST-blueviolet)

## About
A normative assurance and governance baseline for **Agent Names** and **Agent Pages**. Defines verification tiers, control IDs, security/privacy safeguards, AI guardrails, and **machine-checkable conformance declarations** aligned with NIST frameworks to reduce phishing amplification, trust inflation, privacy harm, and authority drift.

## Contents
- **Normative spec:** `spec/agent-name-assurance-baseline.md`
- **Control catalog:** embedded in the spec (Control IDs like `ANAGB-RES-01`, `ANAGB-AI-03`)
- **Applicability matrix (tier/profile):** `conformance/applicability-matrix.md`
- **Conformance**
  - Conformance checklist: `conformance/checklist.md`
  - Conformance declaration template (Markdown): `conformance/conformance-declaration-template.md`
  - Conformance declaration schema (JSON Schema): `conformance/conformance-declaration.schema.json`
  - Sample conformance declaration: `conformance/sample-conformance-declaration.json`
  - Conformance claim schema (implemented controls list): `conformance/anagb-conformance-schema.json`
- **Annexes**
  - Risk surface matrix: `annex/A-risk-surface-matrix.md`
  - NIST crosswalk: `annex/B-nist-crosswalk-matrix.md`
- **Threat model:** `threat-model/threat-matrix.md`
- **Repo validation tool:** `tools/validate_repo.py` (used by CI)

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

## License
Apache 2.0
