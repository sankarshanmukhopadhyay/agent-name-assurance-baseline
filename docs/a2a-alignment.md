# ANAB and A2A alignment

ANAB is not an A2A protocol profile. It is the **naming and operator-binding baseline** that makes A2A interactions less feral.

## What ANAB contributes to A2A

A relying party encountering an A2A endpoint needs answers to four boring-but-fatal questions:

1. Is this the agent I think it is?
2. Is the published operator actually bound to that agent?
3. Are the named page, the machine-readable card, and the live endpoint consistent?
4. Does the trust signal stop at naming, or does it incorrectly imply authority and safety?

ANAB addresses those questions through verification tiers, evidence bundles, and explicit controls that separate **name assurance** from **authority assurance**.

## New A2A-facing controls

This working increment introduces a more complete A2A description binding and expands the control set.

The first six A2A-facing controls remain the baseline trust-surface controls:

- **ANAGB-A2A-01** signed Agent Card / metadata integrity
- **ANAGB-A2A-02** page-card-declaration consistency
- **ANAGB-A2A-03** extended metadata gating
- **ANAGB-A2A-04** task, context, tenant, and subscription scoping
- **ANAGB-A2A-05** authenticated streaming / push trust boundaries
- **ANAGB-A2A-06** safe media-type declaration and handling
- **ANAGB-A2A-07** Agent Card identity-proof and operator-binding coherence
- **ANAGB-A2A-08** issuer trust anchor and verifier-policy disclosure for verified identity claims
- **ANAGB-A2A-09** freshness, expiry, and revocation handling for published trust descriptions
- **ANAGB-A2A-10** downgrade-safe behavior when ANAB extension content is absent, unsupported, or cannot be trusted

## How to compose ANAB with DCAS

A practical deployment stack looks like this:

- **ANAB** for the name, page, and operator binding
- **DCAS CP-7** for the operational assurance of the A2A endpoint
- optional sector overlays for payments, healthcare, public sector, or other higher-risk environments

That separation keeps the architecture honest. A name can be well assured while the endpoint remains operationally weak. Conversely, a secure endpoint does not rescue a misleading name.

The detailed binding is specified in `docs/anab-over-a2a-binding.md`.
