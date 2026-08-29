# WORLD-BRIDGE-001 — Design

**Date:** 2026-08-29

**Status:** approved proving-slice design; no cross-world conclusion is constituted by this record.

## Design sentence

ALEX must make every A/B/C/D source-world crossing explicit, typed, attributable, and promotion-limited so that later reception or interpretation may relate to earlier evidence without silently becoming earlier evidence.

## Governing law

```text
CROSS-WORLD RELEVANCE != CROSS-WORLD SUPPORT
BRIDGE RECEIPT != HISTORICAL PROOF
LATER RECEPTION != EARLIER VISIBILITY
```

## Input

`alex.world-bridge/v0` requires:

- `bridge_id`
- `source_ref` — SHA-256 occurrence reference
- `source_world` — A|B|C|D
- `target_ref` — SHA-256 occurrence reference
- `target_world` — A|B|C|D
- `bridge_type`
- `formulation`
- `evidence_refs` — list of SHA-256 references
- `promotion_limit`
- `producer`

Allowed bridge types follow the existing ALEX Bridge Ledger:

- `documented_mechanism`
- `documented_association`
- `scholarly_interpretation`
- `inference`
- `formal_analogy`
- `metaphor`
- `theological_interpretation`
- `unresolved_bridge`

Documented bridge types (`documented_mechanism`, `documented_association`, `scholarly_interpretation`) require at least one evidence reference. Interpretive or formal bridge types may carry an empty evidence list but never acquire evidentiary promotion from that fact.

Same-world relations are outside this profile and refuse with `same_world_not_bridge`.

## Output

Accepted records return `alex.world-bridge-receipt/v0` containing the exact source/target refs and worlds, bridge type, formulation, evidence refs, promotion limit, bridge digest, and `authority: none`.

The receipt says only that the crossing has been made explicit under a declared type. It does not certify that the bridge is historically correct, causal, genealogical, canonical, or theologically authoritative.

## Hostile specimens

Tests must prove:

1. A B→D theological interpretation can be receipted without being promoted to historical support.
2. A D→B crossing cannot erase its directional ancestry.
3. A same-world relation refuses.
4. An invalid world refuses.
5. A documented bridge with no evidence refs refuses.
6. A malformed evidence ref refuses.
7. Reordered record keys do not alter bridge identity.
8. Changing source or target world changes bridge identity.
9. Supplied authority cannot widen output authority.

## Seal

> **THE BRIDGE MAY CONNECT WORLDS. IT MAY NOT MERGE THEM.**
