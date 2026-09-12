# CROSS-APERTURE-INTERSECTION-001 — Finite Fiber Tomography

**Date:** 2026-09-01  
**Status:** ARCHITECTURAL DESIGN · EXPERIMENTAL EXECUTABLE NOT YET ADMITTED  
**Repository:** `the-static-collective/ALEX.2`

## 0. Purpose

ALEX needs one bounded executable crucible for a distinction already earned by `FIBER-BEFORE-NEEDLE-001`, `FOG-TOMOGRAPHY-001`, 3rdi observer-local projection work, and ALEX projection invariance/break machinery:

> Several lawful observer cuts may reduce a compatible world family without any observer voting on reality and without forcing a representative before the surviving set earns uniqueness.

The executable is **`CROSS-APERTURE-INTERSECTION-001`**.

It is a finite research experiment, not a general sensor-fusion engine and not a truth/authority primitive.

```text
A SECOND APERTURE DOES NOT VOTE ON REALITY.
IT CUTS THE COMPATIBLE WORLD SET AGAIN.
```

Required non-collapses:

```text
DIFFERENT APERTURE != DIFFERENT WORLD
AGREEMENT != INDEPENDENCE
FIBER INTERSECTION != MAJORITY VOTE
SMALLER FIBER != TRUER OBSERVER
SINGLETON IN MODEL != UNIVERSAL IDENTITY
EMPTY INTERSECTION != IMPOSSIBLE REALITY
REPRESENTATIVE != FIBER
OBSERVABILITY != AUTHORITY
```

---

## 1. Architectural ancestry

For a declared map `f : X -> Y`, the fiber over `y` is:

```text
f^-1(y) = {x in X | f(x)=y}.
```

For a frozen world domain `W`, declared observation maps `P_A`, `P_B`, and observations `y_A`, `y_B`:

```text
F_A = P_A^-1(y_A)
F_B = P_B^-1(y_B)
F_joint = F_A ∩ F_B
```

The joint compatible set is a constraint intersection, not a vote.

Existing `projection_invariance.py` asks whether materially distinct worlds remain equivalent under one observer cut without hidden leakage. Existing `projection_break.py` asks whether one common attributable intervention later exposes a difference. This executable asks a different question:

```text
COMPARE TWO WORLDS UNDER ONE CUT
!=
INTERSECT MANY COMPATIBLE-STATE FIBERS ACROSS CUTS
```

3rdi owns how an observer/focus cut becomes a lawful projection. ALEX v0 consumes only already-declared finite observation maps and observed outputs. It does not infer visibility, manufacture observer cuts, reconstruct hidden paths, or import 3rdi runtime code.

---

## 2. Scope

### In scope

The first executable must:

1. accept a finite declared world domain;
2. accept one or more explicit observation maps over that domain;
3. accept the observed output for each map;
4. compute each observation fiber;
5. intersect fibers in supplied order;
6. preserve the compatible set after every cut;
7. classify each cut as `REFINE`, `REDUNDANT`, or `BREAK`;
8. distinguish non-singleton fog, model-local singleton identification, and empty-intersection model break;
9. retain optional correlation/independence declarations as metadata only;
10. refuse representative selection from a non-singleton compatible set unless a future, separately designed rule explicitly owns that policy;
11. emit `authority: none` in every result.

### Out of scope

V0 must not:

- call sensors, models, networks, databases, LOADOUT, 3rdi, or Dogram;
- infer observation maps from data;
- assign confidence weights, probabilities, truth scores, or witness ranks;
- treat agreement as independence;
- diagnose the cause of an empty intersection;
- select a world when more than one remains compatible;
- claim a singleton is universally true outside the frozen domain/maps;
- mutate existing ALEX predicates or projection evaluators;
- add a public ALEX operator, schema version, portable skill trigger, canon claim, support relation, or authority surface.

---

## 3. V0 input contract

Pure entry point:

```python
evaluate_cross_aperture_case(case: dict) -> dict
```

Canonical shape:

```text
{
  "case_id": "cross-aperture-001",
  "world_domain_id": "world-eight-v0",
  "world_states": ["a", "b", "c", "d", "e", "f", "g", "h"],
  "cuts": [
    {
      "cut_id": "A",
      "map_id": "P_A",
      "map": {
        "a": "0", "b": "0", "c": "0", "d": "0",
        "e": "1", "f": "1", "g": "1", "h": "1"
      },
      "observed": "0",
      "relation_declaration": "unknown"
    }
  ]
}
```

### World-domain requirements

- `case_id` and `world_domain_id`: non-empty strings.
- `world_states`: non-empty list of unique non-empty strings.
- Supplied `world_states` order is the canonical display order for every emitted state list.

### Cut requirements

- `cuts`: non-empty list.
- every `cut_id` and `map_id`: non-empty string;
- `cut_id` values unique within the case;
- `map_id` values unique within the case;
- each `map` key set exactly equals the frozen `world_states` set;
- every map output is a non-empty string;
- `observed` is a non-empty string;
- `relation_declaration`, when omitted, normalizes to `"unknown"`; when supplied it must be exactly one of:

```text
independent
correlated
unknown
```

`relation_declaration` never changes the set intersection in v0.

A partial observation map is malformed input. ALEX must not interpret an omitted world state as impossible, hidden, or default-valued.

An observed output that is well-formed but absent from a map's image is valid: it produces an empty fiber and therefore may produce `MODEL_BREAK`.

---

## 4. Evaluation semantics

Initialize:

```text
F_0 = W
```

For each supplied cut `i` in order:

```text
fiber_i = { w in W | P_i(w) = observed_i }
F_i = F_(i-1) ∩ fiber_i
```

Classify the cut:

```text
if F_i = ∅:
    effect = "BREAK"
elif F_i = F_(i-1):
    effect = "REDUNDANT"
else:
    effect = "REFINE"
```

`REDUNDANT` is local to the current compatible family; it does not globally rank the observer or map.

Terminal disposition:

```text
|F_n| > 1
    -> "FOG" / "NON_SINGLETON_COMPATIBLE_SET"

|F_n| = 1
    -> "IDENTIFIED_WITHIN_DECLARED_MODEL" / null

|F_n| = 0
    -> "MODEL_BREAK" / "INCONSISTENT_OBSERVATIONS"
```

Empty intersection does not choose among sensor error, domain incompleteness, observer-time mismatch, map misdeclaration, or world change. V0 leaves cause unresolved.

Every lineage step preserves the compatible family at that historical step. Later refinement never rewrites an earlier receipt.

---

## 5. V0 result contract

A valid result contains:

```text
{
  "case_id": "cross-aperture-001",
  "world_domain_id": "world-eight-v0",
  "disposition": "IDENTIFIED_WITHIN_DECLARED_MODEL",
  "reason_code": null,
  "initial_compatible_states": ["a","b","c","d","e","f","g","h"],
  "lineage": [
    {
      "cut_id": "A",
      "map_id": "P_A",
      "observed": "0",
      "relation_declaration": "unknown",
      "fiber_states": ["a","b","c","d"],
      "compatible_before": ["a","b","c","d","e","f","g","h"],
      "compatible_after": ["a","b","c","d"],
      "effect": "REFINE"
    }
  ],
  "final_compatible_states": ["a"],
  "unique_representative": "a",
  "selection_basis": "singleton_in_declared_model",
  "authority": "none"
}
```

### Non-singleton terminal result

```text
"unique_representative": null
"selection_basis": null
```

No first-item rule, sorting rule, confidence heuristic, or tie-break may populate a representative.

### Singleton terminal result

A singleton is not a tie-break. If exactly one compatible state remains, the result may expose it as:

```text
"unique_representative": <the only surviving state>
"selection_basis": "singleton_in_declared_model"
```

This states uniqueness only inside the supplied finite model.

### Model break

```text
"unique_representative": null
"selection_basis": null
"authority": "none"
```

The lineage records the exact cut where the compatible family first became empty.

### Malformed case extraction

For malformed input:

- `case_id` is the supplied non-empty string if one exists; otherwise `"unknown-case"`.
- `world_domain_id` is the supplied non-empty string if one exists; otherwise `null`.
- no partially validated lineage is emitted.

Result:

```text
{
  "case_id": "unknown-case",
  "world_domain_id": null,
  "disposition": "INSUFFICIENT_TO_TEST",
  "reason_code": <one stable code below>,
  "initial_compatible_states": [],
  "lineage": [],
  "final_compatible_states": [],
  "unique_representative": null,
  "selection_basis": null,
  "authority": "none"
}
```

Stable v0 refusal codes:

```text
MALFORMED_CASE
INVALID_WORLD_DOMAIN
INVALID_CUTS
DUPLICATE_CUT_ID
DUPLICATE_MAP_ID
INCOMPLETE_OBSERVATION_MAP
INVALID_MAP_OUTPUT
INVALID_OBSERVED_OUTPUT
INVALID_RELATION_DECLARATION
```

---

## 6. Hostile specimen matrix

### `CROSS-APERTURE-INTERSECTION-001`

Freeze `W = {a,b,c,d,e,f,g,h}` with:

```text
A(0) -> {a,b,c,d}
B(0) -> {a,b,e,f}
C(0) -> {a,c,e,g}
```

Expected:

```text
8 -> 4 -> 2 -> 1
IDENTIFIED_WITHIN_DECLARED_MODEL
unique_representative = "a"
```

### `NON-SINGLETON-FOG-001`

Apply only A and B:

```text
8 -> 4 -> 2
FOG
final = {a,b}
unique_representative = null
```

### `REDUNDANT-APERTURE-001`

A second distinct map id induces the same observed fiber as the first:

```text
8 -> 4 -> 4
second effect = REDUNDANT
```

### `CORRELATED-AGREEMENT-001`

Agreeing cuts declare `relation_declaration = "correlated"`.

Expected: mechanical intersection only; correlation metadata preserved; no independence bonus, confidence score, or support increase.

### `EMPTY-INTERSECTION-001`

A later observed fiber is disjoint from the surviving family.

Expected:

```text
MODEL_BREAK
INCONSISTENT_OBSERVATIONS
unique_representative = null
```

### `PARTIAL-MAP-REFUSAL-001`

Omit one world key from a map.

Expected:

```text
INSUFFICIENT_TO_TEST
INCOMPLETE_OBSERVATION_MAP
```

### `REPRESENTATIVE-LAUNDERING-001`

End with `{a,b}`.

Expected:

```text
unique_representative = null
selection_basis = null
```

---

## 7. Implementation boundary

Expected implementation slice:

```text
alex_runtime/cross_aperture.py
tests/test_cross_aperture.py
tests/fixtures/cross_aperture_001.json
```

Optional research receipt only if implementation produces a materially useful formation record.

V0 uses the Python standard library only. The evaluator performs no network, filesystem, model, or host access.

No package-level export is required unless current repository convention demonstrably requires it for tests.

---

## 8. Success criteria

Implementation succeeds only if:

1. canonical `8 -> 4 -> 2 -> 1` passes;
2. non-singleton fog preserves all surviving states and selects nobody;
3. redundant cuts are reported without fabricated information gain;
4. correlation metadata changes no mathematical intersection result;
5. empty intersection produces model break rather than a guessed state;
6. malformed/partial maps are refused with stable reason codes;
7. supplied world order is preserved in every emitted state list;
8. later refinement never rewrites earlier lineage entries;
9. every result emits `authority: none`;
10. the full existing ALEX test suite passes.

---

## 9. Promotion membrane

Passing this executable proves only that ALEX can receipt finite intersections of explicitly declared compatible-state fibers.

It does not prove:

```text
fiber is a universal ALEX primitive
all observer fusion should use this representation
real sensors are independent
smaller compatible set means more truthful witness
singleton means universal truth
empty intersection means reality is contradictory
Dogram path homology belongs in ALEX
3rdi should expose hidden world domains
LOADOUT should automatically execute a next probe
```

Any future promotion requires a separate design and hostile pressure pass.

---

## 10. Seal

> **DO NOT FORCE THE WORLD TO A POINT. FIRST COMPUTE THE SHAPE OF WHAT STILL COULD BE TRUE.**
>
> **WHEN ANOTHER APERTURE ARRIVES, INTERSECT THE CONSTRAINT — DO NOT COUNT A VOTE.**
>
> **A SINGLETON IS AN IDENTIFICATION INSIDE THE DECLARED MODEL. A NON-SINGLETON IS STILL DATA. AN EMPTY SET IS A MODEL BREAK, NOT PERMISSION TO INVENT A WORLD.**

**Authority:** none.