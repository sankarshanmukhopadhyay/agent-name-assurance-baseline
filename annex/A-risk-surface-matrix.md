
# Annex A — Risk Surface & Harm Matrix (Non-Normative)

This annex documents primary threat surfaces, harm pathways,
and mitigation expectations for Agent Name ecosystems.

It informs Sections 3–7 of the ANAGB specification.

| Surface | What It Enables | Risk Pathway | Harm Category | Severity | Likelihood | Required Controls |
|----------|----------------|--------------|---------------|----------|------------|------------------|
| Human-readable names | Memorability | Phishing & lookalike domains | Credential theft | High | High | Explicit verification tiers; anti-phishing UX |
| Redirect resolution | Web-based binding | DNS compromise | Identity hijack | High | Medium | Cryptographic binding; TLS; monitoring |
| AKA verification | Lightweight linking | Weak verification signal | Trust inflation | Medium | Medium | Tier signaling; revocation checks |
| Agent pages | Public metadata display | Over-disclosure | Doxxing & surveillance | High | High | Data minimization; noindex; rate limits |
| Capability discovery | Machine discovery | Enumeration | Attack surface mapping | Medium | High | Authenticated discovery; coarse responses |
| Contact mediation | Filtering | Discriminatory exclusion | Access inequality | Medium | Medium | Transparency; redress mechanisms |
| AI prioritization | Automated decisions | Bias amplification | Exclusion & unfair treatment | High | Medium | AI disclosure; human override |
| Delegated AI agents | Autonomous execution | Authority creep | Unintended action | High | Medium | Scoped delegation; expiration; revocation |
| Public APIs | Endpoint exposure | DDoS & abuse | Service disruption | Medium | High | Rate limiting; logging; incident plan |
| Credential ecosystem | Trust layering | Weak issuers | Systemic trust collapse | High | Medium | Issuer governance; revocation checking |
