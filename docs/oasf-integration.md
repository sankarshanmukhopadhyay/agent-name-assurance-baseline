# ANAB OASF integration

## Why add OASF here

ANAB already defines the controls, declaration schema, and evidence bundle expectations for named agents. What it did not yet define was a clean publication surface for those materials in agent ecosystems that already use **OASF** to describe agents and their interaction metadata.

This increment adds that missing piece.

The intent is not to turn OASF into the source of truth for ANAB. The ANAB declaration remains authoritative for control status. The evidence bundle remains authoritative for substantiation. OASF simply becomes the machine-readable place where a relying party can discover that those materials exist and understand how they attach to the published agent.

## What is added

- Machine-readable crosswalk: `../crosswalk/oasf.yml`
- OASF-facing publication profile schema: `../conformance/oasf-anab-publication-profile.schema.json`
- Sample publication profile: `../conformance/samples/oasf-anab-publication-profile.json`

## Practical model

An OASF-described agent can publish an `anab_publication` extension or equivalent module that points to:

1. the authoritative ANAB conformance declaration
2. the evidence bundle for the claimed assurance level
3. the specific ANAB controls that are expected to matter for the advertised interaction surface
4. revocation, freshness, and downgrade-handling metadata where relevant

## Why this matters

This closes a common operational gap. A relying party may discover an agent through an OASF-compatible directory or record exchange, but still need to know whether the agent name, operator binding, and assurance posture are trustworthy enough for consequential use.

With this profile:

- discovery stays in the agent schema layer
- ANAB remains the domain baseline
- DCAS can evaluate what is published without renaming ANAB controls into a different namespace too early
