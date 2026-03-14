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

This release introduces six A2A-facing controls:

- **ANAGB-A2A-01** signed Agent Card / metadata integrity
- **ANAGB-A2A-02** page-card-declaration consistency
- **ANAGB-A2A-03** extended metadata gating
- **ANAGB-A2A-04** task, context, tenant, and subscription scoping
- **ANAGB-A2A-05** authenticated streaming / push trust boundaries
- **ANAGB-A2A-06** safe media-type declaration and handling

## How to compose ANAB with DCAS

A practical deployment stack looks like this:

- **ANAB** for the name, page, and operator binding
- **DCAS CP-7** for the operational assurance of the A2A endpoint
- optional sector overlays for payments, healthcare, public sector, or other higher-risk environments

That separation keeps the architecture honest. A name can be well assured while the endpoint remains operationally weak. Conversely, a secure endpoint does not rescue a misleading name.
