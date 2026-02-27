# ANAGB Conformance Checklist

## Declare scope
- [ ] Declared verification tier (AN-0..AN-3)
- [ ] Declared conformance profile (Core/Deploy/Transact/Enterprise)

## UI signaling
- [ ] ANAGB-UI-01 implemented
- [ ] ANAGB-UI-02 implemented
- [ ] ANAGB-UI-03 implemented (as applicable)

## Resolution & binding
- [ ] ANAGB-RES-01 implemented
- [ ] ANAGB-RES-02 implemented
- [ ] ANAGB-RES-03 implemented
- [ ] ANAGB-RES-04 implemented (recommended)
- [ ] ANAGB-RES-05 implemented
- [ ] ANAGB-RES-06 implemented (recommended for AN-2/AN-3)

## Privacy
- [ ] ANAGB-PRIV-01 implemented
- [ ] ANAGB-PRIV-02 implemented
- [ ] ANAGB-PRIV-03 implemented
- [ ] ANAGB-PRIV-04 implemented
- [ ] ANAGB-PRIV-05 implemented (recommended)
- [ ] ANAGB-PRIV-06 implemented (recommended)

## Interaction, logging, abuse
- [ ] ANAGB-AGT-01 implemented
- [ ] ANAGB-AGT-02 implemented (recommended)
- [ ] ANAGB-LOG-01 implemented
- [ ] ANAGB-LOG-02 implemented
- [ ] ANAGB-LOG-03 implemented
- [ ] ANAGB-ABUSE-01 implemented
- [ ] ANAGB-ABUSE-02 implemented

## AI (if used)
- [ ] ANAGB-AI-01 implemented
- [ ] ANAGB-AI-02 implemented
- [ ] ANAGB-AI-03 implemented
- [ ] ANAGB-AI-04 implemented
- [ ] ANAGB-AI-05 implemented
- [ ] ANAGB-AI-06 implemented

## Incident & recovery
- [ ] ANAGB-IR-01 implemented
- [ ] ANAGB-IR-02 implemented
- [ ] ANAGB-IR-03 implemented
- [ ] ANAGB-IR-04 implemented

## Evidence bundle and audit readiness (AL)

### AL1 (minimum)
- [ ] Assurance level declared (AL1–AL4)
- [ ] Boundary case classification declared (HITL / delegated / org-issued)
- [ ] Authority boundary documented (allowed vs disallowed actions)
- [ ] Key rotation / revocation procedure documented
- [ ] Minimal audit log fields present (actor, time, identity, result)

### AL2 (managed)
- [ ] Evidence bundle published and referenced in conformance declaration
- [ ] Change control for policy/config affecting binding and delegation
- [ ] Delegation artifact scoped + revocable (if delegation exists)
- [ ] JML controls for org-issued agents (if org-issued)

### AL3 (auditable)
- [ ] Reproducible tests / test vectors for critical controls
- [ ] Decision log present with assumptions and threat model mapping
- [ ] Review cadence defined for threat/risk updates
- [ ] Step-up gating for high-risk actions (if delegated)

### AL4 (continuous)
- [ ] Continuous monitoring for assurance-critical conditions
- [ ] Automated evidence capture / freshness measurement
- [ ] SLOs defined for resolution/revocation/transparency services
- [ ] Post-incident assurance loop defined and exercised

