# Annex K — A2A Alignment

This annex maps ANAB controls to the A2A concepts most likely to matter in production deployments. It is **non-normative** but intended to reduce interpretation drift.

| A2A concept | Why it matters for ANAB | Primary ANAB controls |
|---|---|---|
| Agent Card | The machine-readable public identity surface can be spoofed, drift, or over-disclose | `ANAGB-A2A-01`, `ANAGB-A2A-02`, `ANAGB-A2A-03` |
| Supported interfaces and auth schemes | Relying parties need consistency between published name, endpoint, and authentication expectations | `ANAGB-A2A-02`, `ANAGB-AGT-01` |
| Task and context identifiers | Cross-tenant or cross-principal leakage can turn a named endpoint into a confused deputy | `ANAGB-A2A-04`, `ANAGB-LOG-01` |
| Push notifications / webhooks | Unsafely trusted callbacks can counterfeit agent state | `ANAGB-A2A-05`, `ANAGB-ABUSE-02` |
| Artifact outputs and media types | Ambiguous or unsupported outputs can create false trust in downstream actions | `ANAGB-A2A-06`, `ANAGB-AI-06` |
| Signed metadata and change events | Helps verifiers distinguish real changes from malicious drift | `ANAGB-A2A-01`, `ANAGB-RES-05`, `ANAGB-RES-06` |

## Practical interpretation

ANAB SHOULD be used to answer **who this named agent is and whether its public trust surface is coherent**. DCAS and other operational overlays SHOULD be used to answer **whether the endpoint behaves safely enough to rely on**.
