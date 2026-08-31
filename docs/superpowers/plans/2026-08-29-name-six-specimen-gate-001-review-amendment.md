# NAME Six-Specimen Gate 001 — Owner Review Amendment

**Date:** 2026-08-29

**Status:** material correctness correction discovered by owner-style review.

## Finding

The first GREEN family gate validated packet-result shape, specimen coverage, and packet digests, but trusted two upstream invariants without rechecking them:

1. a caller could forge a `READY` `NOMEN_SACRUM` packet receipt whose `material_witness_ref` was absent;
2. a caller could supply a packet result / receipt carrying widened authority such as `canon` and the family gate would still return `DIVE_READY`.

Both violate the meaning of the packet evaluator even though the JSON shape remains plausible.

## RED evidence

Two hostile tests were added before correction:

- `test_ready_nomen_sacrum_without_material_witness_ref_refuses`
- `test_upstream_authority_bearing_packet_refuses`

GitHub Actions run `33262898001` failed **exactly those two tests**. Both failures showed the pre-correction family gate returning `DIVE_READY` where `REFUSE` was required.

## Correction

The family gate now requires:

```text
packet_result.authority == none
READY receipt.authority == none
READY NOMEN_SACRUM -> valid material_witness_ref
BLOCKED -> NOMEN_SACRUM + material_witness_required only (v0)
```

A packet-shaped object that violates those upstream invariants returns:

```text
REFUSE / invalid_packet_result
```

## Governing refinement

```text
RECEIPT SHAPE != RECEIPT ADMISSIBILITY
DOWNSTREAM GATE != BLIND TRUST OF UPSTREAM CLAIMED STATE
READY LABEL != PROOF THAT READY PRECONDITIONS SURVIVE
AUTHORITY NONE MUST SURVIVE EVERY MEMBRANE
```

The family evaluator still does not recompute the underlying historical research. It validates only the invariants necessary for the packet result to mean what its declared disposition says.

## Seal

> **A RECEIPT MAY BE OPAQUE ABOUT ITS EVIDENCE, BUT NOT ABOUT THE INVARIANTS REQUIRED TO ADMIT IT.**
