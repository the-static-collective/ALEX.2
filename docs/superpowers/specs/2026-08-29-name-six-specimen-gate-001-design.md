# NAME Six-Specimen Gate 001 — Design

**Date:** 2026-08-29

**Status:** approved proving-slice design; this gate certifies packet completeness only, never historical/theological truth.

## Design sentence

ALEX must be able to say whether a bounded NAME research specimen carries the attributable road required for the deep dive, and must preserve a real `BLOCKED` state when a required witness layer is absent rather than manufacturing completion.

## Governing law

```text
PACKET COMPLETE != HYPOTHESIS TRUE
BLOCKED != DISPROVED
MISSING MATERIAL WITNESS != PERMISSION TO INVENT ONE
SIX GREEN PACKETS != CANON / AUTHORITY
```

## Six pilot specimens

The v0 pilot family is fixed for this proving slice:

1. `LXX_JOSHUA`
2. `MATTHEW_1_21`
3. `JESUS_BARABBAS`
4. `SCEVA`
5. `PHILIPPIANS_2`
6. `NOMEN_SACRUM`

The first five can be text-first packets. `NOMEN_SACRUM` additionally requires a material-witness reference because its research value depends on visible graphical treatment.

## Input

`alex.name-specimen-packet/v0` requires:

- `packet_id`
- `specimen_type` — one of the six fixed v0 types
- `attestation_ref` — exact ALEX attestation occurrence digest
- `transform_refs` — zero or more exact transform occurrence digests
- `hypothesis_ref` — exact hypothesis occurrence digest
- `null_battery_ref` — exact NAME-NULLS battery occurrence digest
- `receipt_refs` — one or more attributable downstream receipt digests
- `producer`
- optional `material_witness_ref`

All refs are lowercase `sha256:<64 hex>` occurrence references.

## Evaluation

The evaluator is structural and intentionally ignorant of research conclusions.

It returns:

- `READY` — required refs for this specimen type are present and well formed;
- `BLOCKED` — packet is structurally coherent but a required witness class is absent;
- `REFUSE` — malformed packet, unsupported specimen type, duplicate refs, or forbidden answer-bearing fields.

`NOMEN_SACRUM` without `material_witness_ref` returns `BLOCKED` with reason `material_witness_required`.

The evaluator must not accept explicit result-bearing fields such as `expected_answer`, `expected_outcome`, `favored_result`, `survival_expected`, `verdict`, or `conclusion`. The packet carries references to research outputs; it does not predeclare their meaning.

Every result freezes `authority: none`.

## Pilot-family gate

`alex.name-six-specimen-gate/v0` consumes exactly six packet-evaluation receipts, one per required specimen type.

It returns:

- `DIVE_READY` only if all six are `READY`;
- `DIVE_BLOCKED` if at least one is `BLOCKED` and none are malformed/refused;
- `REFUSE` if the family is incomplete, duplicated, contains unsupported specimen types, or includes any packet with evaluator disposition `REFUSE`.

The gate reports which specimen types block the dive. It never converts readiness into historical or theological promotion.

## Hostile tests

Tests must prove:

1. five text-first packets can be `READY` without pretending to be material witnesses;
2. nomen-sacrum without a material witness returns `BLOCKED`, not `READY` or `REFUSE`;
3. nomen-sacrum with a material witness can be `READY`;
4. duplicate transform/receipt refs refuse;
5. malformed SHA refs refuse;
6. answer-bearing fields refuse;
7. supplied authority cannot widen output authority;
8. six-packet family with one blocked specimen returns `DIVE_BLOCKED` and names the blocker;
9. six ready packets return `DIVE_READY`;
10. duplicate or missing specimen types refuse.

## Seal

> **THE GATE MAY SAY WE ARE READY TO DIVE. IT MAY NOT SAY WHAT WE WILL FIND.**

> **A REAL HOLE IN THE EVIDENCE IS A STATE, NOT AN INVITATION TO FILL IT WITH IMAGINATION.**
