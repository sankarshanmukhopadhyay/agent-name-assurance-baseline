# agent-name-assurance-baseline

![Version](https://img.shields.io/badge/version-0.1-blue)
![Status](https://img.shields.io/badge/status-draft-orange)
![License](https://img.shields.io/badge/license-Apache%202.0-green)
![Conformance](https://img.shields.io/badge/conformance-machine--readable-success)
![Alignment](https://img.shields.io/badge/aligned-NIST-blueviolet)

## About
A normative assurance and governance baseline for Agent Names and Agent Pages. Defines verification tiers, control IDs, security/privacy safeguards, AI guardrails, and machine-checkable conformance declarations aligned with NIST frameworks to prevent phishing, trust inflation, and authority drift.

## Contents

- **Normative spec:** `spec/agent-name-assurance-baseline.md`
- **Control catalog:** embedded in the spec (Control IDs like `ANAGB-RES-01`, `ANAGB-AI-03`)
- **Conformance**
  - Conformance checklist: `conformance/checklist.md`
  - Conformance declaration template (Markdown): `conformance/conformance-declaration-template.md`
  - Conformance declaration schema (JSON Schema): `conformance/conformance-declaration.schema.json`
  - Sample conformance declaration: `conformance/sample-conformance-declaration.json`
  - Conformance claim schema (implemented controls list): `conformance/anagb-conformance-schema.json`
- **Annexes**
  - Risk surface matrix: `annex/A-risk-surface-matrix.md`
  - NIST crosswalk: `annex/B-nist-crosswalk-matrix.md`
- **Threat model scaffold:** `threat-model/threat-matrix.md`

## Conformance model

Implementers SHOULD publish a signed conformance declaration using the JSON schema in `conformance/conformance-declaration.schema.json` and include evidence pointers for each implemented control ID.

## License

Apache 2.0
