# ALEXDEEPDIVE — ENDPOINT-BREAKPOINT-SPLIT-001

**Date:** 2026-09-01  
**Status:** RESEARCH · AUDIT → DOSSIER · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Ground

- **Question:** After the `POST-BREAK-001` repair on draft PR #87, what distinction remains materially unresolved in `CROSS-APERTURE-INTERSECTION-001`?
- **Desired consequence:** determine whether the repaired `BREAK` label is now safe as a traversal receipt, and freeze the smallest next discriminator before any stronger inconsistency-attribution semantics are introduced.
- **Stop condition:** establish whether final intersection, first breakpoint, and conflict attribution are the same or different objects; do not add an unsat-core runtime.
- **Corpus/date:** ALEX.2 state visible on 2026-09-01 23:24 America/Chicago, especially `main@dac0f99b1f90ee2861c1cffbae82f24b6a0b5ac9` and draft PR #87 head `a1d8adae313c5a63551afdd51a23da9607ae9013`.
- **Authority/effect boundary:** research packet only. No merge, runtime/schema promotion, blame assignment, support/evidence/canon authority, or cross-project ontology.
- **Task shape:** AUDIT → DOSSIER.
- **Formation trace active:** no. The previous packet is discovery context; support is rebuilt from current source state and exact computation.

## World cut

### Included

- Static Collective GitBook Front Room, freshly read this pass for orientation only.
- ALEX.2 `main@dac0f99b1f90ee2861c1cffbae82f24b6a0b5ac9`.
- Previous packet `research/ALEX-DEEPDIVE-2026-09-01-1723-BREAKPOINT-NOT-CULPRIT.md`.
- Draft PR #87 current head `a1d8adae313c5a63551afdd51a23da9607ae9013`.
- PR #87 delta from prior audited head `9a395dfdc3a386f94e14a05ff22a77cb0f83c95c` to current head.
- Current `alex_runtime/cross_aperture_intersection.py` and `tests/test_cross_aperture_intersection.py` at PR #87 head.
- ALEX constitutional files on `main`: `AGENTS.md`, `skills/alex/SKILL.md`, `skills/alex/references/research-receipt.md`.
- Exact Wolfram Language finite-set enumeration across all six permutations of the hostile three-cut specimen.
- Microsoft Z3 Guide on unsatisfiable cores.
- Current SMT-LIB language surface, Version 2.7.
- Liffiton & Sakallah, *Algorithms for Computing Minimal Unsatisfiable Subsets of Constraints*, Journal of Automated Reasoning 40(1), 1–33 (2008), DOI `10.1007/s10817-007-9084-z`.
- Helly's theorem only as structural counterpressure: local-to-global intersection guarantees require additional geometric structure not declared by this finite arbitrary-map evaluator.

### Deliberately omitted

- No 3rdi, LOADOUT, Dogram, or other project bodies. The live issue remains internal to the meaning of ALEX's ordered finite intersections.
- No probabilistic sensor-fusion literature; the evaluator consumes deterministic declared maps.
- No implementation proposal for MUS/unsat-core extraction.

### Missing / inaccessible

None required for this bounded audit. GitBook Front Room access succeeded this pass.

**Sufficiency:** sufficient.

## What newly surfaced

The prior packet proposed two discriminators:

1. `POST-BREAK-001` — distinguish the first nonempty→empty transition from later empty→empty persistence.
2. `PAIRWISE-SAT-TRIPLE-BREAK-001` — show that first breakpoint can move under reordering even when final inconsistency does not.

Since that packet, PR #87 added exactly the first repair:

- commit `5bf9cfdbc554ab323d8fa7786e5574a88206d8d7` — `test: distinguish first breakpoint from post-break persistence`;
- commit `a1d8adae313c5a63551afdd51a23da9607ae9013` — `fix: reserve BREAK for first empty transition`.

The current evaluator now checks equality before emptiness:

```python
if compatible == compatible_before:
    effect = "REDUNDANT"
elif not compatible:
    effect = "BREAK"
else:
    effect = "REFINE"
```

Therefore an already-empty compatible set followed by another cut is now `REDUNDANT`, not another `BREAK`.

The current test floor freezes this as:

```text
REFINE -> BREAK -> REDUNDANT
```

for `POST-BREAK-001`.

This is a real correction, not merely documentation: the previous ambiguity is closed on the PR branch.

## Why the remaining discriminator matters more now

Once `BREAK` is reserved for the first empty transition, its semantics become more precise—but also more obviously **path-relative**.

Set intersection itself is commutative, associative, and idempotent. For a fixed family of cuts:

```text
final intersection
```

does not depend on the order in which the cuts are applied.

But the prefix lineage does depend on order. Therefore:

```text
FINAL DISPOSITION
!=
FORMATION TRACE
```

and, more specifically:

```text
MODEL_BREAK endpoint
!=
which cut first receives BREAK
```

This is now the strongest live seam because PR #87 has correctly sharpened `BREAK` into a transition label. The next risk is allowing that transition label to be read as an order-invariant explanation.

## Exact hostile specimen

Declare:

```text
W = {1,2,3}
A = {1,2}
B = {2,3}
C = {1,3}
```

Exact pairwise intersections:

```text
A ∩ B = {2}
A ∩ C = {1}
B ∩ C = {3}
```

Exact joint intersection:

```text
A ∩ B ∩ C = {}
```

Thus every pair is compatible while the three-cut family is jointly inconsistent.

### Wolfram replay across all six orders

Exact Wolfram Language enumeration returned:

| Order | Prefix intersections | Cardinalities | First empty cut | Final |
| --- | --- | --- | --- | --- |
| A,B,C | `{1,2}` → `{2}` → `{}` | 2 → 1 → 0 | C | `{}` |
| A,C,B | `{1,2}` → `{1}` → `{}` | 2 → 1 → 0 | B | `{}` |
| B,A,C | `{2,3}` → `{2}` → `{}` | 2 → 1 → 0 | C | `{}` |
| B,C,A | `{2,3}` → `{3}` → `{}` | 2 → 1 → 0 | A | `{}` |
| C,A,B | `{1,3}` → `{1}` → `{}` | 2 → 1 → 0 | B | `{}` |
| C,B,A | `{1,3}` → `{3}` → `{}` | 2 → 1 → 0 | A | `{}` |

Two facts separate cleanly:

```text
final compatible set = {}              invariant across all permutations
first BREAK-labelled cut = A/B/C       varies with traversal order
```

No one cut is individually inconsistent with the declared world domain, and every pair remains satisfiable.

## Strongest survivor

> **ENDPOINT INVARIANCE != BREAKPOINT INVARIANCE.**
>
> **THE FINAL EMPTY FAMILY IS A PROPERTY OF THE CUT SET. THE FIRST BREAK IS A PROPERTY OF THE ORDERED WALK THROUGH THAT SET.**

The current ALEX runtime can lawfully preserve both without adding new ontology:

- terminal `MODEL_BREAK` records the order-invariant endpoint for a fixed family;
- ordered lineage records which prefix first became empty in the supplied walk;
- neither one, alone, identifies a unique culprit or minimal conflict family.

## External pressure

### Z3

The Microsoft Z3 Guide describes an unsatisfiable core as a subset of tracked assertions that cannot be satisfied together. This locates inconsistency in a set of constraints rather than equating it with whichever assertion was evaluated last.

Source: https://microsoft.github.io/z3guide/docs/logic/propositional-logic/#unsatisfiable-cores

### SMT-LIB 2.7

The current SMT-LIB site identifies Version 2.7 as the current standard, with a new reference release dated 2026-03-27. Its unsat-core interface likewise treats conflict explanation as a subset-level object rather than an execution-position label.

Sources:
- https://smt-lib.org/language.shtml
- https://smt-lib.org/news.shtml

### Peer-reviewed MUS literature

Liffiton & Sakallah treat a minimal unsatisfiable subset (MUS) as an unsatisfiable subset of constraints whose proper subsets are satisfiable, and develop methods for producing MUSes from infeasible constraint systems.

Citation:

Mark H. Liffiton & Karem A. Sakallah, “Algorithms for Computing Minimal Unsatisfiable Subsets of Constraints,” *Journal of Automated Reasoning* 40(1):1–33 (2008). DOI: https://doi.org/10.1007/s10817-007-9084-z

This is structurally close to the three-cut hostile specimen: the whole `{A,B,C}` family is inconsistent while every proper two-element subset remains consistent.

### Helly counterpressure

Helly's theorem shows that strong local-to-global intersection guarantees can exist when the family has additional structure, specifically convexity in finite-dimensional affine space. The current ALEX evaluator declares arbitrary finite world states and arbitrary observation maps; it does **not** declare convexity or another Helly-type structure.

Therefore the safe v0 inference is:

```text
pairwise compatibility
!=
global compatibility
```

unless a future owning model explicitly contributes enough structure to justify a stronger local-to-global rule.

Source: https://encyclopediaofmath.org/wiki/Helly_theorem

This is a formal analogy / counterpressure, not evidence that ALEX fibers are geometric convex sets.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #87 now labels later empty→empty steps `REDUNDANT`, reserving `BREAK` for the first nonempty→empty transition. | observed | current PR #87 code + test at `a1d8ada...` | PR remains draft and is not on `main`. | supported |
| C2 | For a fixed family of finite sets, final intersection is invariant under permutation. | mathematical | exact set algebra / Wolfram replay | Does not imply lineage invariance. | supported |
| C3 | In the hostile three-cut specimen, the first BREAK-labelled cut changes with permutation although final `MODEL_BREAK` does not. | mathematical | six exact Wolfram permutations | Depends on supplied ordering, by construction. | supported |
| C4 | First breakpoint is not a unique cause of inconsistency in that specimen. | inference from exact counterexample | every proper pair intersects; all three do not | Some other cases may have a single individually impossible cut. | supported for specimen; not universal |
| C5 | Constraint-solving practice distinguishes unsatisfiability from subset-level explanation. | source testimony / scholarly precedent | Z3, SMT-LIB, Liffiton–Sakallah | ALEX need not adopt solver machinery or terminology. | supported |
| C6 | Pairwise-compatible apertures guarantee a globally compatible world. | proposed overclaim | none | Directly disproved by `{A,B,C}` hostile specimen. | disproved |
| C7 | ALEX should implement minimal unsat-core extraction now. | proposal | none | Current v0 only needs semantic separation and one hostile fixture. | refused |

## Counterevidence and nearest boring explanation

The repaired runtime is already safer than the previous packet observed. It does not name a culprit, infer sensor fault, or claim causal diagnosis. `BREAK` can remain a perfectly lawful **ordered transition receipt** if consumers understand that scope.

The nearest boring explanation is therefore not “the runtime is broken.” It is:

> the runtime is an ordered fold over a commutative set operation, so the endpoint and the fold history naturally have different invariance properties.

That is ordinary mathematics. The architectural value lies in refusing to let one projection impersonate the other.

## Relation to ALEX constitutional law

This distinction composes directly with existing ALEX discipline without adding a primitive:

```text
same endpoint != same formation history
```

and:

```text
receipt of where a contradiction became visible
!=
proof of what caused the contradiction
```

That is analogous to ALEX's existing separation of discovery path from evidence path and replay match from historical identity: a lawful trace may be true about the walk without being a universal explanation of the destination.

## Smallest next discriminators / repo-worthy moves

1. **Freeze `PAIRWISE-SAT-TRIPLE-BREAK-001` on PR #87.** Run the exact `{A,B,C}` specimen in at least two different cut orders. Require identical terminal `MODEL_BREAK` / empty final compatible set while requiring different first `BREAK` cut IDs. This proves the endpoint/lineage split in executable form.
2. **Document one sentence of scope next to `effect = "BREAK"`:** `BREAK records the first empty transition in the supplied order; it does not identify a unique inconsistent aperture or minimal conflict set.` No new schema is required.
3. **Keep conflict localization on HOLD.** Only design a separate `conflict_set` / `inconsistency_core` surface if a concrete consumer later needs order-independent subset diagnosis. If that need appears, pressure whether all minimal conflict families or only one sufficient core is required before choosing machinery.

## Residual fog

- PR #87 is still draft and stacked on design PR #86; current branch semantics are not canonical `main` semantics.
- No current ALEX consumer has been shown to require order-independent conflict localization.
- The finite arbitrary-map model has no declared convexity, matroid, Horn, or other structure that would justify stronger local-to-global consistency inference.
- A future model may legitimately attach causal metadata to cuts, but such metadata would need its own evidence path; it cannot be inferred from breakpoint position alone.

## Bridge ledger

| Move | Type | Evidence bearing | Promotion limit |
| --- | --- | --- | --- |
| finite fiber intersection → set algebra | documented mechanism | exact for current evaluator | bears endpoint/lineage mathematics only |
| ALEX break lineage → unsat core/MUS | formal analogy + scholarly precedent | supports keeping transition separate from conflict set | does not authorize MUS runtime |
| arbitrary fibers → Helly theorem | formal counterpressure | shows local-to-global guarantees require extra structure | no claim that ALEX fibers are convex/geometric |

## Receipt

- **Created:** 2026-09-01 23:24 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE research pass
- **Tool/model boundary:** GitBook connector for Front Room orientation; GitHub connector for exact repository/PR witnesses; Wolfram Language for exact finite-set enumeration; web retrieval for current Z3/SMT-LIB/Helly references; Consensus search/fetch plus DOI verification for peer-reviewed MUS literature; model interpretation kept separate from computation/source testimony.
- **External byte egress:** public repository content and public documentation only; no private/local corpus bytes supplied externally.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-01-2324-ENDPOINT-BREAKPOINT-SPLIT.md`
- **Promotion:** none

## Seal

> **THE ENDPOINT BELONGS TO THE SET.**
>
> **THE BREAKPOINT BELONGS TO THE WALK.**
>
> **AN EXPLANATION OF THE CONFLICT IS A THIRD OBJECT AND MUST EARN ITS OWN RECEIPT.**
