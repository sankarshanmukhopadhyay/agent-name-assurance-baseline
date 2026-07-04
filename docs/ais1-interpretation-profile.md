# AIS-1 v0.2 Interpretation Profile (Experimental)

This page mirrors the relying-party interpretation guidance published at `profiles/ais1/anab-profile.md` so the GitHub Pages documentation surface has a stable AIS-1 landing page.

This guidance is **experimental**. It should be used as careful interpretation support, not as proof that AIS-1 is already part of ANAB's settled normative core.

## Summary

AIS-1 v0.2 is useful inside ANAB as an **identity-and-accountability signal**. It can strengthen confidence that a named agent resolves to a durable, sponsor-backed identity surface with a visible lifecycle state.

It does **not** replace:

- delegation proofs
- runtime authorization checks
- risk-sensitive verifier policy
- protocol-level provenance controls

## Use it for

- discovery and low-risk trust signaling
- sponsor visibility
- tier and status interpretation
- revocation-aware downgrade or denial decisions
- ALA/SOA classification
- SOA parent accountability checks
- timestamp service and Assurance Container evidence as audit support

## Do not use it alone for

- spend authority
- regulated filing authority
- privileged tool invocation
- other consequential delegated actions
- independent SOA legal standing

## v0.2 relying-party checks

When AIS-1 v0.2 appears in an ANAB trust surface, relying parties should check:

1. the `did:ais1` identifier resolves through the documented method;
2. registry status is current;
3. the displayed tier is not collapsed into a generic verified badge;
4. `agentClass` is disclosed as `ala` or `soa`;
5. SOA records include a `parentDid`;
6. the parent ALA is active before relying on the SOA;
7. parent ALA revocation causes SOA downgrade or denial;
8. any high-risk action still has separate delegation or authorization evidence.

## Canonical profile

The full relying-party interpretation guidance remains at `profiles/ais1/anab-profile.md` in the repository. Optional machine-readable examples are available under `profiles/ais1/examples/`.
