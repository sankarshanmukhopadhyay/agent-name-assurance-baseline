# Crosswalk registry (machine-readable)

This directory contains **machine-readable** standards alignment mappings used by:
- reviewers (traceability),
- implementers (adoption shortcuts),
- tooling/CI (consistency checks).

These files are **additive**: they do not change the normative requirements in the spec.
They help interpret and operationalize the baseline in environments that already use existing assurance and security standards.

## Format

All crosswalks are YAML files with a common top-level shape:

- `standard_id`: short stable id (e.g., `OWASP-ASVS`, `ISO-27001`)
- `standard_name`
- `standard_version`
- `scope`: what the crosswalk is intended to cover
- `mappings`: list of mapping entries

Mapping entries reference ANAGB in a tool-friendly way:

- `anagb.assurance_levels`: list like `["AL2", "AL3"]`
- `anagb.evidence_categories`: one or more of `governance|risk|security|privacy|ai|testing|operations|attestation|other`
- `anagb.artifact_ids`: optional list of evidence artifact ids used in example bundles
- `anagb.refs`: optional list of in-repo references (`path#anchor`)

External references use:
- `external.id`: clause/control identifier (e.g., `ASVS 2.1.1`)
- `external.name`: short label
- `external.url`: optional

## Registry index

- OWASP ASVS: `crosswalk/owasp-asvs.yml`
- OWASP API Top 10: `crosswalk/owasp-api-top10.yml`
- ISO 27001/27002: `crosswalk/iso-27001-27002.yml`
- SOC 2 TSC: `crosswalk/soc2-tsc.yml`
- Supply chain (SLSA/SSDF/SBOM): `crosswalk/supply-chain.yml`
- Privacy (ISO 27701/GDPR concepts): `crosswalk/privacy.yml`
- AI governance (ISO 42001/23894/OECD/EU AI Act pointers): `crosswalk/ai-governance.yml`
- Identity & crypto (DID/VC/JOSE/COSE/FIDO2): `crosswalk/identity-and-crypto.yml`
