# Annex A — Risk Surface & Harm Matrix (Non-Normative)

This annex documents primary threat surfaces, harm pathways, and mitigation expectations for Agent Name ecosystems.
It informs Sections 2–7 of the ANAGB specification.

| Theme / Surface | What the proposal enables | Risk / harm pathway | Who gets harmed | Severity | Likelihood | Harms-prevention / controls to bake in | Open questions |
|---|---|---|---|---:|---:|---|---|
| Human-friendly names over DIDs | Domain + /@name resolves to a DID and then to endpoints/keys | Phishing + lookalike domains (homograph attacks, deceptive rendering) | All users, high-risk users | High | High | Require explicit tier display; anti-phishing UX; safe preview; mixed-script warnings | What is the baseline UX guidance across apps/browsers? |
| Redirect-based resolution | Web redirect from agent name to DID (+ possibly hosting DID doc) | DNS poisoning / server compromise redirects to attacker DID | Agents/users relying on resolution | High | Medium | Cryptographic binding; TLS+HSTS; monitoring; transparency logging | Do we standardize a transparency log for bindings? |
| AKA verification (alsoKnownAs) | Resolver checks DID doc includes the agent name | Weak proof; compromised DID doc; first-fetch trust failures | Users trusting first resolution | Medium | Medium | Treat AKA as weak signal only; tiered claims; avoid “verified” based on AKA alone | Need a crisp “verification levels” model for UX |
| Agent pages (browser view) | Human-readable page with signed/verifiable content | Over-disclosure, doxxing, correlation and indexing | Individuals, vulnerable groups | High | High | Data minimization; compartmentalization; privacy profiles; rate limiting | Recommended privacy posture for personal vs org pages? |
| Agent pages (agent view) | Machine-readable discovery of endpoints/capabilities | Silent probing/enumeration of capabilities | VTAs, communities | Medium | High | Authenticated discovery; coarse anonymous responses; rate limiting | Does discovery leak org structure? |
| Contact mediation | Policy-based contact handling | Coercive / discriminatory filtering; trust gating | Outsiders, marginalized, new entrants | Medium | Medium | Transparency and redress; avoid mandatory social proof; reason codes | What fairness expectations should be normative? |
| Buttons / QR invocations | One-click invocation of trust tasks | Drive-by consent; QR phishing; link hijacks | Users | High | High | Explicit consent screens; origin + DID display; no auto-execution | Baseline secure deeplink scheme? |
| Delegated AI agents | AI agent acts on behalf of entity | Authority creep; misalignment; delegated harms | End users, orgs, bystanders | High | Medium | Bounded delegation (scope/expiry/caps); revocation; audit logs; human override | Redress and rollback expectations? |
| Endpoint security | DID doc lists endpoints for VTA | DDoS, enumeration, replay, credential stuffing | Operators | Medium | High | Rate limiting; request signing; nonce replay protection; monitoring | Are endpoints public by default? |
| Credential ecosystem reliance | Uses issuers/trust frameworks | Weak issuers; fake creds; fragmentation | Everyone | High | Medium | Issuer governance baselines; revocation; tiered assurance claims | Conformance tiers for issuer governance? |
| Dispute / recovery / takedown | Domain-centric naming | Domain loss; coercive takedown; continuity failure | Individuals/orgs | High | Medium | Recovery playbooks; key rotation; safe suspension signaling | Who arbitrates conflicts on domain seizure? |
