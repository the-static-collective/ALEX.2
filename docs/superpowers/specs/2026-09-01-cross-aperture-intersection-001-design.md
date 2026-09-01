# CROSS-APERTURE-INTERSECTION-001 — Finite Fiber Tomography

**Date:** 2026-09-01  
**Status:** ARCHITECTURAL DESIGN · EXPERIMENTAL EXECUTABLE NOT YET ADMITTED  
**Repository:** `the-static-collective/ALEX.2`

## 0. Purpose

ALEX needs one bounded executable crucible for a research distinction already earned by `FIBER-BEFORE-NEEDLE-001`, `FOG-TOMOGRAPHY-001`, 3rdi observer-local projection work, and ALEX projection invariance/break machinery:

> Several lawful observer cuts may reduce a compatible world family without any observer voting on reality and without forcing a representative before the surviving set earns uniqueness.

The executable is named **`CROSS-APERTURE-INTERSECTION-001`**.

It is a finite research experiment, not a general sensor-fusion engine and not a truth/authority primitive.

Core law:

```text
A SECOND APERTURE DOES NOT VOTE ON REALITY.
IT CUTS THE COMPATIBLE WORLD SET AGAIN.
```

Hard non-collapses:

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

This design extends existing ALEX laws rather than replacing them.

### 1.1 `FIBER-BEFORE-NEEDLE-001`

For a declared map

```text
f : X -> Y
```

the fiber over `y` is

```text
f^-1(y) = {x in X | f(x)=y}.
```

The fiber preserves which distinct sources a coarse image stopped distinguishing.

### 1.2 `FOG-TOMOGRAPHY-001`

For a frozen world domain `W` and declared observation maps

```text
P_A : W -> Y_A
P_B : W -> Y_B
```

with observations `y_A`, `y_B`, define

```text
F_A = P_A^-1(y_A)
F_B = P_B^-1(y_B)
F_joint = F_A ∩ F_B.
```

The joint compatible set is a constraint intersection, not a vote.

### 1.3 Existing executable ALEX projection work

`projection_invariance.py` already checks whether materially distinct worlds remain observer-equivalent without hidden differences leaking through later boundaries.

`projection_break.py` already checks whether a common attributable intervention later exposes a difference while preserving earlier invariance and frozen authority.

`CROSS-APERTURE-INTERSECTION-001` adds a different operation:

```text
COMPARE TWO WORLDS UNDER ONE CUT
!=
INTERSECT MANY COMPATIBLE-STATE FIBERS ACROSS CUTS
```

It does not replace either existing evaluator and does not call them internally in v0.

### 1.4 3rdi boundary

3rdi owns how an observer/focus cut becomes a lawful projection.

ALEX v0 consumes only **already declared finite observation maps and observed outputs**. It does not infer visibility, manufacture observer cuts, reconstruct hidden paths, or import 3rdi runtime code.

---

## 2. Scope

### 2.1 In scope

The first executable must:

1. accept a finite declared world domain;
2. accept one or more explicitly declared observation maps over that domain;
3. accept the observed output for each supplied map;
4. compute the fiber induced by each observation;
5. intersect those fibers in supplied order;
6. preserve the compatible set after every cut;
7. report whether each cut reduced, preserved, or broke the current compatible family;
8. distinguish non-singleton fog, model-local singleton identification, and empty-intersection model break;
9. retain optional correlation/independence declarations as receipt metadata only;
10. refuse any representative selection not supplied by an additional declared rule;
11. emit `authority: none` in every successful or model-break receipt.

### 2.2 Out of scope

V0 must not:

- call external sensors, models, networks, databases, LOADOUT, 3rdi, or Dogram;
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

The executable entry point should be a pure function:

```python
evaluate_cross_aperture_case(case: dict) -> dict
```

The case shape is:

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

### 3.1 World-domain requirements

- `case_id` and `world_domain_id` are non-empty strings.
- `world_states` is a non-empty list of unique non-empty strings.
- V0 preserves supplied `world_states` order as canonical display order.

### 3.2 Cut requirements

- `cuts` is a non-empty list.
- every `cut_id` and `map_id` is a non-empty string;
- `cut_id` values are unique within the case;
- `map_id` values are unique within the case;
- each `map` is a dictionary whose key set is **exactly** the frozen `world_states` set;
- every map output is a non-empty string;
- `observed` is a non-empty string;
- `relation_declaration` is optional; if present it is one of:

```text
independent
correlated
unknown
```

This field does not alter set intersection in v0. It exists so an apparently repeated or agreeing cut cannot silently acquire an independence claim.

### 3.3 No inferred missing states

A partial observation map is malformed input.

ALEX must not silently interpret an omitted state as impossible, hidden, or mapped to a default value.

---

## 4. Evaluation semantics

Initialize:

```text
F_0 = W
```

For each supplied cut `i` in order, compute:

```text
fiber_i = { w in W | P_i(w) = observed_i }
F_i = F_(i-1) ∩ fiber_i
```

Every step receives a lineage receipt.

### 4.1 Step classification

For each cut:

```text
if F_i = ∅:
    effect = "BREAK"
elif F_i = F_(i-1):
    effect = "REDUNDANT"
else:
    effect = "REFINE"
```

`REDUNDANT` is descriptive only. It does not mean the observer, sensor, or witness is useless in every context.

### 4.2 Terminal dispositions

After all supplied cuts:

```text
|F_n| > 1
    -> disposition = "FOG"
       reason_code = "NON_SINGLETON_COMPATIBLE_SET"

|F_n| = 1
    -> disposition = "IDENTIFIED_WITHIN_DECLARED_MODEL"
       reason_code = null

|F_n| = 0
    -> disposition = "MODEL_BREAK"
       reason_code = "INCONSISTENT_OBSERVATIONS"
```

An empty intersection does **not** choose among possible causes such as sensor error, domain incompleteness, time mismatch, map misdeclaration, or world change. Those remain unresolved possibilities outside v0.

### 4.3 Historical non-rewrite

Each lineage step is immutable evidence about what the supplied cut did to the then-current compatible family.

A later singleton does not rewrite an earlier step from four compatible states to one.

The receipt must therefore preserve the full ordered sequence:

```text
W
-> F_1
-> F_2
-> ...
-> F_n
```

---

## 5. V0 result contract

A valid case returns:

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

### 5.1 Non-singleton terminal result

When more than one state survives:

```text
"unique_representative": null
"selection_basis": null
```

No deterministic sorting rule, first-item rule, confidence heuristic, or arbitrary tie-break may populate a representative.

### 5.2 Singleton terminal result

When exactly one state survives, `unique_representative` may expose that state only with:

```text
selection_basis = "singleton_in_declared_model"
```

This is a statement about the supplied finite model, not universal truth.

### 5.3 Model break

When no state survives:

```text
"unique_representative": null
"selection_basis": null
"authority": "none"
```

The lineage still records the exact cut at which the compatible family first became empty.

### 5.4 Malformed cases

Malformed input returns:

```text
{
  "case_id": <best available id>,
  "world_domain_id": <best available id or null>,
  "disposition": "INSUFFICIENT_TO_TEST",
  "reason_code": <stable refusal code>,
  "initial_compatible_states": [],
  "lineage": [],
  "final_compatible_states": [],
  "unique_representative": null,
  "selection_basis": null,
  "authority": "none"
}
```

Stable v0 reason codes:

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

### 6.1 `CROSS-APERTURE-INTERSECTION-001`

Freeze:

```text
W = {a,b,c,d,e,f,g,h}
```

with cuts:

```text
A(0) -> {a,b,c,d}
B(0) -> {a,b,e,f}
C(0) -> {a,c,e,g}
```

Expected lineage sizes:

```text
8 -> 4 -> 2 -> 1
```

Expected terminal state:

```text
IDENTIFIED_WITHIN_DECLARED_MODEL
unique_representative = "a"
```

### 6.2 `NON-SINGLETON-FOG-001`

Apply only A and B.

Expected:

```text
8 -> 4 -> 2
FOG
final = {a,b}
unique_representative = null
```

### 6.3 `REDUNDANT-APERTURE-001`

Supply B with the same partition and observed fiber as A under a distinct declared map id.

Expected:

```text
8 -> 4 -> 4
second effect = REDUNDANT
```

The second cut exists but adds no discriminator to this frozen compatible set.

### 6.4 `CORRELATED-AGREEMENT-001`

Two agreeing cuts carry:

```text
relation_declaration = "correlated"
```

Expected:

- intersection behaves mechanically;
- correlation metadata is preserved;
- no independence bonus, confidence score, or support increase exists anywhere in the result.

### 6.5 `EMPTY-INTERSECTION-001`

Supply a later cut whose observed fiber is disjoint from the surviving compatible set.

Expected:

```text
MODEL_BREAK
INCONSISTENT_OBSERVATIONS
```

No world is invented.

### 6.6 `PARTIAL-MAP-REFUSAL-001`

Omit one world key from a declared observation map.

Expected:

```text
INSUFFICIENT_TO_TEST
INCOMPLETE_OBSERVATION_MAP
```

### 6.7 `REPRESENTATIVE-LAUNDERING-001`

End with `{a,b}`.

Expected:

```text
unique_representative = null
selection_basis = null
```

The implementation must not choose `a` merely because it appears first.

---

## 7. Implementation boundary

The expected implementation slice is deliberately small:

```text
alex_runtime/cross_aperture.py
tests/test_cross_aperture.py
tests/fixtures/cross_aperture_001.json
```

Optional documentation may add one research receipt, but v0 should not modify existing runtime modules unless a concrete import/export requirement is discovered during implementation.

The module should use Python standard library only.

No network or filesystem access is required by the evaluator itself.

No package-level export is required for the first experimental proof unless repository convention demonstrably requires it for tests.

---

## 8. Success criteria

The implementation is successful only if all of the following are true:

1. the canonical `8 -> 4 -> 2 -> 1` specimen passes;
2. non-singleton fog preserves the whole compatible set and selects nobody;
3. a redundant cut is reported without fabricated information gain;
4. correlation metadata changes no mathematical intersection result;
5. an empty intersection produces model break rather than a guessed state;
6. malformed/partial maps are refused with stable reason codes;
7. supplied world order is preserved deterministically in every state list;
8. later refinement never rewrites earlier lineage entries;
9. every result emits `authority: none`;
10. the full existing ALEX test suite still passes.

---

## 9. Promotion membrane

Passing this executable proves only that ALEX can correctly receipt finite intersections of explicitly declared compatible-state fibers.

It does **not** prove:

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