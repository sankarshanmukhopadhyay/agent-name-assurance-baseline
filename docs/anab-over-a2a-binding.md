# ANAB-over-A2A Description Extension

## Status
Draft binding specification for review.

## Purpose

This document defines a **reasonably detailed ANAB-over-A2A binding** that lets an A2A Agent Card carry machine-readable references to ANAB declarations, evidence bundles, and operator-bound identity material **without collapsing A2A into a trust framework**.

The design principle is simple:

- **A2A** remains the interaction protocol.
- **ANAB** remains the naming, operator-binding, and public trust-surface baseline.
- **DCAS or another verifier** remains the evaluation layer.

This binding therefore exposes enough metadata for a client or verifier to decide whether to trust a named agent before relying on its A2A capabilities.

## Why an extension instead of a core A2A field

A2A already provides an extension mechanism through `AgentExtension` (`uri`, `description`, `required`, `params`). That is the cleanest place to carry ANAB semantics because:

1. the information is domain-specific rather than universally required for every A2A deployment
2. the assurance material may vary by ecosystem and verifier policy
3. ANAB needs to express more than identity verification alone, including operator binding, authority boundaries, declaration freshness, and evidence references

The extension defined here can coexist with proposals focused on cryptographic identity verification of Agent Cards. In fact, it gives those proposals a larger governance frame: **who signed the card is not enough; the relying party also needs to know what the name means, who operates it, what evidence exists, and whether the resulting trust claim should be treated as identity, authority, or both.**

## Extension identifier

Agents implementing this binding SHOULD publish the following extension URI in `AgentCard.capabilities.extensions`:

- `https://trustoverip.github.io/dtgwg-agent-names-tf/extensions/anab-description/v1`

The extension SHOULD normally be marked `required: false` so that generic A2A clients can still interact. Deployments MAY mark it `required: true` where policy requires ANAB processing before any interaction is allowed.

## Extension shape

The extension is carried as an A2A `AgentExtension` object.

```json
{
  "uri": "https://trustoverip.github.io/dtgwg-agent-names-tf/extensions/anab-description/v1",
  "description": "Publishes ANAB declaration, operator binding, and verifier-consumable trust metadata for this agent.",
  "required": false,
  "params": {
    "anabVersion": "0.6.0",
    "verificationTier": "AN-2",
    "assuranceLevel": "AL2",
    "bindingStrength": "operator-bound",
    "declaration": {
      "format": "anab-conformance-declaration",
      "mediaType": "application/json",
      "uri": "https://example.org/.well-known/anab/conformance.json",
      "sha256": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    "evidenceBundle": {
      "uri": "https://example.org/.well-known/anab/evidence/bundle.json",
      "sha256": "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    },
    "agentName": {
      "displayName": "Example Research Agent",
      "pageUri": "https://example.org/agents/research",
      "resolverUri": "https://example.org/.well-known/agent-name.json"
    },
    "operator": {
      "legalName": "Example Corp",
      "operatorId": "did:web:example.org",
      "contactUri": "https://example.org/legal/agent-operator"
    },
    "cardBinding": {
      "bindingMethod": "jws-detached",
      "issuer": "did:web:example.org",
      "kid": "did:web:example.org#anab-card-signing-1",
      "verificationMaterialUri": "https://example.org/.well-known/jwks.json"
    },
    "identityVerification": {
      "status": "verified",
      "issuer": "Example Trust Registry",
      "verificationUri": "https://registry.example.org/agents/example-research-agent",
      "revocationCheck": "required"
    },
    "authorityBoundary": {
      "statement": "Identity and operator binding verified. No implied authority to spend funds or sign regulated filings.",
      "delegationRequired": true,
      "delegationPolicyUri": "https://example.org/policy/delegation"
    },
    "freshness": {
      "issuedAt": "2026-03-24T08:00:00Z",
      "expiresAt": "2026-06-22T08:00:00Z",
      "maxCacheAgeSeconds": 86400
    }
  }
}
```

## Parameter model

### 1. Core identification

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `anabVersion` | string | MUST | ANAB spec version used for the declaration |
| `verificationTier` | string | MUST | ANAB tier claim (`AN-0`..`AN-3`) |
| `assuranceLevel` | string | SHOULD | AL claim (`AL1`..`AL4`) where published |
| `bindingStrength` | string | SHOULD | Short classifier such as `self-asserted`, `domain-bound`, `framework-verified`, `operator-bound` |

### 2. Declaration and evidence references

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `declaration.format` | string | MUST | SHOULD be `anab-conformance-declaration` |
| `declaration.mediaType` | string | MUST | Serialization type |
| `declaration.uri` | URI | MUST | Stable retrievable ANAB declaration |
| `declaration.sha256` | hex string | SHOULD | Integrity pin for the declaration |
| `evidenceBundle.uri` | URI | SHOULD | Evidence bundle index for AL2+ |
| `evidenceBundle.sha256` | hex string | SHOULD | Integrity pin for the bundle index |

### 3. Public trust surface

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `agentName.displayName` | string | MUST | Public-facing agent name |
| `agentName.pageUri` | URI | SHOULD | Human-facing Agent Page |
| `agentName.resolverUri` | URI | SHOULD | Machine-facing resolver or name record |

### 4. Operator and card binding

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `operator.legalName` | string | SHOULD | Accountable legal or organizational operator |
| `operator.operatorId` | string | SHOULD | DID, URI, or other stable operator identifier |
| `operator.contactUri` | URI | MAY | Human-verifiable operator contact or policy page |
| `cardBinding.bindingMethod` | string | MUST | How the card is bound to the operator identity |
| `cardBinding.issuer` | string | MUST | Issuer or subject identifier responsible for the card-binding proof |
| `cardBinding.kid` | string | SHOULD | Key identifier used for card signatures where applicable |
| `cardBinding.verificationMaterialUri` | URI | SHOULD | JWKS, DID document, trust registry entry, or equivalent |

### 5. Identity verification and verifier hooks

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `identityVerification.status` | string | SHOULD | `self_asserted`, `verified`, `revoked`, `suspended`, or `unknown` |
| `identityVerification.issuer` | string | SHOULD | Entity asserting or publishing verified identity state |
| `identityVerification.verificationUri` | URI | SHOULD | URI a verifier can dereference for status or proof |
| `identityVerification.revocationCheck` | string | SHOULD | `none`, `recommended`, or `required` |

### 6. Authority boundary

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `authorityBoundary.statement` | string | MUST | Plain statement clarifying what is and is not implied by the published assurance |
| `authorityBoundary.delegationRequired` | boolean | SHOULD | Whether a separate delegation artifact is needed for consequential actions |
| `authorityBoundary.delegationPolicyUri` | URI | MAY | Policy or contract describing how delegation is granted and checked |

### 7. Freshness

| Field | Type | Requirement | Meaning |
|---|---|---|---|
| `freshness.issuedAt` | date-time | MUST | Timestamp of extension issuance |
| `freshness.expiresAt` | date-time | SHOULD | Timestamp after which the extension should not be relied on |
| `freshness.maxCacheAgeSeconds` | integer | SHOULD | Maximum cache lifetime for clients |

## Processing rules

### Publication rules

1. An agent publishing this extension **MUST** ensure that `agentName.displayName`, the ANAB declaration, and the public A2A Agent Card are materially consistent.
2. If `declaration.sha256` or `evidenceBundle.sha256` is present, the publisher **MUST** ensure the referenced artifact matches the digest.
3. If `identityVerification.status` is `verified`, the publisher **MUST NOT** use that to imply authority beyond the `authorityBoundary` statement.
4. If the extension is marked `required: true`, the publisher **MUST** expect clients that do not understand the extension to decline interaction.

### Client and verifier rules

1. Clients **SHOULD** treat this extension as a trust input, not as an automatic authorization grant.
2. Clients **SHOULD** retrieve the ANAB declaration before relying on the extension for high-risk actions.
3. Verifiers **SHOULD** perform freshness and revocation checks before treating the extension as valid for consequential reliance.
4. Clients **MUST NOT** infer spending authority, legal signing authority, regulated action authority, or organizational mandate solely from a successful card signature or a `verified` identity status.
5. If the extension is absent, clients MAY continue with normal A2A interaction under local policy, but they SHOULD treat the agent as lacking ANAB-described assurance.

## Relationship to A2A issue #1672

The identity-verification proposal in A2A issue `#1672` is directionally useful because it recognizes that transport security is not enough for agent trust. But ANAB needs to represent a wider surface than a single `verifiedIdentity` object.

The key distinction is:

- **card authenticity** proves who signed or issued the Agent Card
- **ANAB description** explains what the public agent name means, who operates it, what evidence exists, what tier is claimed, and what authority is explicitly *not* implied

A deployment can therefore support both:

- a cryptographic identity-verification mechanism for Agent Card authenticity
- this ANAB description extension for naming, operator binding, and verifier-consumable trust semantics

## Additional A2A controls motivated by this binding

This binding makes four additional control concerns explicit:

- identity-proof binding between the Agent Card and the accountable operator
- issuer and verifier policy anchoring for externally verified identity claims
- freshness and revocation handling for the published trust description
- downgrade-safe behavior when clients cannot process or choose not to rely on ANAB extension content

Those concerns are reflected in new controls `ANAGB-A2A-07` through `ANAGB-A2A-10` in the normative baseline.
