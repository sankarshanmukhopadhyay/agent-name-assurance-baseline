---
name: TIS drift review
description: Review whether a TIS change affects ANAB composition guidance, samples, or validation.
title: "TIS drift review: <source release or change>"
labels: ["drift-review", "tis-alignment"]
---

## Source change

- TIS release or commit:
- Upstream implementation source, if applicable:
- Artifact family affected:

## Drift trigger

- [ ] New or renamed TIS schema `$id`
- [ ] New DTG/OpenVTC/VTI artifact family
- [ ] Authority, delegation, revocation, expiry, or scope semantics changed
- [ ] Decision receipt or evidence bundle structure changed
- [ ] Assurance-level guidance changed
- [ ] Example or validation fixture changed

## ANAB impact

- Affected controls:
- Affected docs:
- Affected samples:
- Relying-party interpretation impact: none / additive / breaking

## Required action

- [ ] No local change required
- [ ] Update docs
- [ ] Update samples
- [ ] Update validation tooling
- [ ] Prepare release note

## Evidence

Attach schema references, release notes, validation output, or review notes.
