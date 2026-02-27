# Implementation guidance

This is the pragmatic layer: how to adopt ANAGB without rebuilding your universe.

It is written for implementers shipping real systems with real constraints.

---

## Start with a worked flow

### Worked example: publishing an Agent Page + conformance + evidence bundle
**Assumptions**
- You operate an agent with a stable public URL (an Agent Page).
- You use a DID as the cryptographic root for the agent identity.
- You publish JSON artifacts in a predictable location.

**End-to-end steps**
1. Implement the normative spec (`spec/agent-name-assurance-baseline.md`) for your chosen **tier** and **profile**.
2. Publish a **conformance declaration**:
   - Fill `conformance/conformance-declaration-template.md`
   - Export JSON conforming to `conformance/conformance-declaration.schema.json`
3. Publish an **evidence bundle**:
   - Create a `bundle.json` conforming to `evidence-bundles/evidence-bundle.schema.json`
   - Host it alongside the artifacts it references
4. Link it all from your Agent Page:
   - Spec version
   - Tier/profile/assurance level
   - Conformance declaration URL
   - Evidence bundle URL
5. Run validation locally (same as CI):
   ```bash
   python -m pip install jsonschema
   python tools/validate_repo.py
   ```

**Decision log**
Maintain `decision-log.md` that records:
- identity root choice (Web PKI vs DID vs IAM)
- revocation approach and freshness targets
- delegation model (scoped tokens, expiry, audience)
- threat assumptions and mitigations

---

## Common stacks

### A) Web PKI-backed (TLS + domain control)
Use when: you already have strong domain governance and want fast adoption.

- Map **domain control proofs** to AN-1.
- Use transparency logging / auditable issuance to step toward AN-2/AN-3 requirements.
- Anti-pattern: treating “TLS present” as equivalent to “identity verified”.

### B) DID-based (DID + VC issuance)
Use when: you need ecosystem interoperability and cryptographic portability.

- AN-2 is the natural sweet spot: VC from a recognized issuer + revocation checking.
- Anti-pattern: VCs without revocation strategy; that’s just collectible JSON.

### C) Registry-backed (trust registry + trust lists)
Use when: your ecosystem needs an authoritative source of issuers, policies, and endpoints.

- Use registries to operationalize “recognized issuer” for AN-2/AN-3.
- Anti-pattern: registry without governance; it becomes an unsigned spreadsheet of vibes.

### D) Enterprise IAM-backed (OIDC/SAML + managed identities)
Use when: internal agents act inside enterprise boundaries, but still need clear naming and authority rules.

- Treat IAM as the identity root, but still publish conformance and evidence for external review if the agent crosses boundaries.
- Anti-pattern: “internal only” as an excuse to skip logging, revocation, and SoD.

---

## Design patterns

- **Pattern: Step-up for authority**  
  High-risk actions MUST trigger stronger checks (human approval, stronger auth, smaller scopes).

- **Pattern: Delegation as a first-class object**  
  Represent delegation as a signed artifact with scope, expiry, audience, and revocation.

- **Pattern: Evidence freshness budgets**  
  Set explicit max-age for critical evidence (revocation checks, transparency inclusion proof).

---

## Anti-patterns (foot-guns)

- “Verified” badge with no tier specificity (violates UI signaling intent).
- Delegation via long-lived shared credentials (hard to revoke, impossible to audit).
- “Human-in-the-loop” that is advisory rather than enforced in the execution path.
- Claiming AN-3 without transparency, independent review readiness, and operational evidence.

---

## Where to go deeper
- Assurance levels: `docs/assurance-levels.md`
- Threat model: `threat-model/threat-matrix.md`
- Annexes: `annex/`
