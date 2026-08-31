# NAME-NULLS-001 — Design

**Date:** 2026-08-29

**Status:** approved hostile-pressure proving slice.

## Design sentence

ALEX must refuse to treat a NAME hypothesis as pressure-tested unless it carries a complete, attributable control battery capable of attacking the favored explanation through materially different dimensions.

## Core law

> **A favored hypothesis earns promotion by surviving loss, not by accumulating resemblance.**

And:

> **A hostile control may declare what changes and what would discriminate. It may not declare what answer should result.**

`NAME-NULLS-001` does not execute every control. It validates and receipts the hostile battery that downstream systems must execute.

## Required control family

A complete v0 battery contains exactly one of each:

- `COMMON_NAME`
- `REFERENT_SHUFFLE`
- `DECODER_SWAP`
- `WORLD_CUTOFF`
- `LABEL_BLIND`
- `EDGE_ABLATION`

Historical specimens such as Joshua, Jesus Barabbas, Sceva, or other controls are fixture/data choices beneath these control types; they are not hard-coded into runtime semantics.

## Input

`alex.name-null-battery/v0` requires:

- `battery_id`
- `hypothesis_ref` — SHA-256 reference to the exact hypothesis occurrence
- `target_ref` — SHA-256 reference to the exact research target occurrence
- `target_world` — A|B|C|D
- `controls` — list of control records
- `producer`

Each control requires:

- `control_id`
- `control_type`
- `changed_dimension`
- `preserved_invariants` — unique non-empty strings
- `next_discriminator`
- `executor_owner` — one of `ALEX|3rdi|Dogram|Wolfram|external`

The `changed_dimension` may not also appear in `preserved_invariants`; a control that claims both to change and preserve the same dimension is malformed.

### Favored-answer prohibition

Neither the battery nor any control may predeclare survival, expected outcome, favored result, or expected answer. v0 refuses these explicit result-bearing keys wherever they occur at those two record levels:

- `expected_answer`
- `expected_outcome`
- `favored_result`
- `survival_expected`

The battery may state a `next_discriminator`; that field describes what comparison would discriminate after execution, not which result is desired.

## Output

Accepted batteries return an `alex.name-null-battery-receipt/v0` with exact battery digest, hypothesis/target refs, target world, ordered control summaries, and `authority: none`.

Acceptance means only that the battery is structurally complete and attributable. It does not mean the hypothesis survived any control.

## Refusal surface

At minimum:

- `not_an_object`
- `wrong_schema`
- `missing_required_field`
- `invalid_ref`
- `invalid_world`
- `invalid_controls`
- `incomplete_control_family`
- `duplicate_control_type`
- `control_dimension_conflict`
- `invalid_executor_owner`
- `favored_answer_not_allowed`

## Owner-review correction

The first GREEN structural validator tolerated opaque extra keys. Owner review showed that this allowed a supposedly hostile battery to include `expected_answer`, `expected_outcome`, or `survival_expected` and still receive `ACCEPT`.

RED review tests proved all three forms were accepted. The corrected evaluator refuses explicit result-bearing fields before structural acceptance.

## Hostile tests

1. Complete six-control battery accepts.
2. Missing one family refuses.
3. Duplicate type refuses even when six records exist.
4. Changed dimension duplicated in preserved invariants refuses.
5. Invalid hypothesis/target ref refuses.
6. Invalid executor owner refuses.
7. Key reorder does not change battery identity.
8. Changing one discriminator changes battery identity.
9. Input authority cannot widen output authority.
10. Battery-level expected answer refuses.
11. Control-level expected outcome refuses.
12. Survival-predeclared control refuses.

## Seal

> **THE NULL MUST BE ABLE TO KILL THE CLAIM. OTHERWISE IT IS DECORATION.**

> **A TEST THAT ALREADY KNOWS ITS ANSWER IS NOT A HOSTILE TEST.**
