# Architecture snapshot

This diagram is a **non-normative** view of how this repository composes with DTG Labs upstream work and the ToIP Trust Spanning Protocol (TSP).

```mermaid
flowchart TB
  subgraph A[Assurance and Conformance Layer]
    S[Trust Infrastructure Schemas
(OTAM)]
    D[DCAS]
    N[ANAB]
    S --> D --> N
  end

  subgraph T[Transport]
    TSP[ToIP Trust Spanning Protocol]
  end

  subgraph C[Credential Semantics]
    DC[dtg-credentials]
  end

  subgraph I[Ecosystem Architecture]
    VTI[verifiable-trust-infrastructure]
  end

  subgraph R[Reference Implementations]
    O[openVTC]
  end

  %% Typical dependency direction
  DC --> VTI --> O

  %% Transport adjacency (non-normative)
  N -. "trust tasks over transport" .- TSP
  DC -. "artifact exchange over transport" .- TSP

  %% Interop touchpoints (non-normative)
  S -. "trust artifact schemas" .- DC
  D -. "assurance profiles" .- VTI
  N -. "identifier trust tasks" .- O
```

## Notes

- Solid arrows represent a typical dependency direction.
- Dotted edges represent interoperability touchpoints (mapping, evaluation, integration), not hard dependencies.
- The transport layer is shown as an adjacency to highlight where secure message exchange is expected to occur.

## TIS v0.9 synchronization note

ANAB v0.9.0 aligns with TIS v0.9.0 by allowing DTG/OpenVTC/VTI runtime trust artifacts to support named-agent evidence. These references do not replace ANAB controls, declarations, evidence bundles, or relying-party interpretation. They provide a canonical evidence substrate for credential, relationship, authorization, decision, and provision artifacts.

For the governing composition model, see `tis-v0.9-agent-name-composition.md`.
