# AIS-1 Interpretation Profile for ANAB (Experimental)

## Status

This profile is **experimental**. It is included so relying parties can interpret AIS-1 consistently while the pattern is still being pressure-tested across the broader portfolio.

## Purpose

This profile explains how relying parties should interpret AIS-1 signals when an agent name, Agent Page, or Agent Card is backed by an AIS-1 bonded identity surface.

The aim is practical consistency. AIS-1 can strengthen the public trust surface around a named agent. It does **not** remove the need for delegation checks, policy evaluation, or risk-sensitive verifier behavior.

## What AIS-1 can usefully prove

| AIS-1 signal | Practical ANAB interpretation |
|---|---|
| `did:ais1` identifier | Durable identifier for the named agent |
| sponsor-backed bond | There is an accountable party standing behind the named agent |
| tier: Basic | Minimal published identity surface with limited verifier confidence |
| tier: Verified | Stronger confidence that the named agent has been verified under the AIS-1 process |
| tier: Sovereign | Highest available AIS-1 identity-and-accountability tier, still subject to verifier policy |
| active status | The bonded identity surface is currently valid to the extent checked by the verifier |
| suspended / revoked status | Relying party should downgrade or deny trust under normal policy |

## What AIS-1 does not prove

AIS-1 alone does **not** prove:

- that the named agent has spend authority
- that the named agent may sign regulated filings
- that the named agent is allowed to operate outside a stated mandate
- that outputs, messages, or tool calls are authentic by default
- that the deployment has met ANAB controls unrelated to identity and accountability

## Minimum verifier expectations

When AIS-1 is presented as part of an ANAB trust surface, relying parties should check at least the following:

1. **Bond existence and validity** — the named agent still resolves to an active bonded identity.
2. **Sponsor presence** — the sponsor or accountable operator is visible and materially consistent across the name, page, and supporting artifacts.
3. **Tier clarity** — the AIS-1 tier is displayed accurately and not collapsed into a generic “verified” badge.
4. **Revocation or suspension state** — stale or revoked state should not be silently ignored.
5. **Authority boundary** — any high-risk action still requires separate delegation or authorization proof.

## Usage guidance by risk

| Context | Can AIS-1 be useful? | Additional expectation |
|---|---|---|
| Discovery / low-risk lookup | Yes | Bond and status checks may be sufficient |
| Routine interaction with no consequential authority | Yes | Treat AIS-1 as identity-and-accountability input |
| High-risk delegated action | Partly | Require separate delegation artifact and policy check |
| Regulated or high-assurance workflow | Partly | Require stronger evidence, issuer trust anchor, and explicit verifier policy |

## Example evaluation scenarios

### Scenario 1: Public discovery
A verifier discovers a named agent on a public page and sees an AIS-1 `Verified` tier with an active bond. For low-risk discovery, that is a useful trust input. It supports the claim that the name is tied to a durable, sponsor-backed agent identity.

### Scenario 2: Tool invocation with spend risk
The same agent attempts to trigger a purchase. AIS-1 should still be treated as incomplete. The relying party should require a delegation artifact or another policy-bound authorization proof before allowing the action.

### Scenario 3: Suspended bond state
The agent name still resolves, but the AIS-1 status is suspended. The relying party should treat that as a downgrade or denial event even if old cached metadata looks healthy.

## Control interpretation note

For ANAB purposes, AIS-1 mainly strengthens interpretation around:

- identity-root clarity
- accountable operator or sponsor visibility
- status freshness and revocation awareness
- safer differentiation between identity assurance and authority assurance

That makes AIS-1 useful inside ANAB, but only as one trust input among several.
