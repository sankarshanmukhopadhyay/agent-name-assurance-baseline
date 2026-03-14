# Transport alignment: ToIP Trust Spanning Protocol (TSP)

ANAB defines assurance controls for **agent identifiers** (agent names, agent pages) and the associated verification tasks. These tasks typically require secure exchanges between endpoints.

The ToIP **Trust Spanning Protocol (TSP)** is a candidate transport substrate for those exchanges.

Spec reference: https://trustoverip.github.io/tswg-tsp-specification/

## Where transport shows up in ANAB trust tasks

ANAB trust tasks that benefit from an explicit transport substrate include:

- **Name verification exchanges**: challenge/response flows used to prove control of an identifier and its endpoints.
- **Agent page retrieval and verification**: secure retrieval of machine-readable agent pages and integrity validation.
- **Capability negotiation**: exchanging supported verification methods and policy requirements.
- **Evidence exchange**: sharing signed declarations, receipts, and audit records in a privacy-preserving manner.

## Binding model

ANAB remains identifier- and transport-agnostic. When TSP is used:

- Agent identifiers are bound to endpoints via the resolution and verification model described in the ANAB documentation.
- TSP provides authenticated, integrity-protected exchange between endpoints.
- Evidence artifacts exchanged over TSP SHOULD be signed and versioned, and SHOULD reference canonical trust artifact schemas from `trust-infrastructure-schemas`.

## Implementation notes

- TSP does not replace identifier resolution; it provides a safer channel for exchanges that occur after endpoints are discovered.
- Transport selection does not change the ANAB control intent; it changes the operational evidence that can be collected.

## Non-goals

ANAB does not define:
- a mandatory transport protocol
- operational key management practices
- network policy constraints
