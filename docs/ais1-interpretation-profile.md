# AIS-1 Interpretation Profile (Experimental)

This page mirrors the relying-party interpretation guidance published at `profiles/ais1/anab-profile.md` so the GitHub Pages documentation surface has a stable AIS-1 landing page.

This guidance is **experimental**. It should be used as careful interpretation support, not as proof that AIS-1 is already part of ANAB's settled normative core.

## Summary

AIS-1 is useful inside ANAB as an **identity-and-accountability signal**. It can strengthen confidence that a named agent resolves to a durable, sponsor-backed identity surface with a visible lifecycle state.

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

## Do not use it alone for

- spend authority
- regulated filing authority
- privileged tool invocation
- other consequential delegated actions

## Canonical profile

The full relying-party interpretation guidance remains at `profiles/ais1/anab-profile.md` in the repository. Keep that file and this docs page aligned.
