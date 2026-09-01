# ALEXDEEPDIVE — BREAKPOINT-NOT-CULPRIT-001

**Date:** 2026-09-01  
**Status:** RESEARCH · AUDIT → DOSSIER · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Ground

- **Question:** What is the strongest newly revealed ALEX frontier since `TRUST-BOUNDARY-CARRY-001`, and does the new `CROSS-APERTURE-INTERSECTION-001` executable preserve the distinction between detecting an inconsistent prefix and attributing inconsistency to a particular aperture?
- **Desired consequence:** pressure the new finite-fiber evaluator before merge or semantic promotion; leave one small discriminator that can fail.
- **Stop condition:** establish whether current `BREAK` semantics are sufficient, overstrong, or malformed; do not redesign the whole evaluator.
- **Corpus/date:** ALEX.2 state visible on 2026-09-01, especially draft PRs #85, #86, #87; exact external set/constraint references only where they bear the distinction.
- **Authority/effect boundary:** research packet only. No merge, no runtime/schema promotion, no support/evidence/canon authority.
- **Task shape:** AUDIT → DOSSIER.
- **Formation trace:** no. Discovery motive and evidence path remain separated below.

## World cut

### Included

- ALEX.2 `main@d4a4d2e6cfdeed8e27cfa6645050b1cdc468e1b0` — prior ALEXDEEPDIVE packet / current visible main head at start of this pass.
- Draft PR #85 `d56c57b5fa224c6403ae2cd34baaac1068b81356` — NAME result transport probe.
- Draft design PR #86 `abd01155d3cb43a091a338c95402ee87f6553a38` — `CROSS-APERTURE-INTERSECTION-001` design.
- Draft implementation PR #87 `9a395dfdc3a386f94e14a05ff22a77cb0f83c95c` — finite fiber tomography implementation and tests.
- ALEX constitutional files at main: `AGENTS.md`, `skills/alex/SKILL.md`, `skills/alex/references/research-receipt.md`.
- Microsoft Z3 Guide, “Unsatisfiable cores.”
- SMT-LIB Standard v2.7, §4.2.7 `get-unsat-core`.
- Exact finite-set calculations executed in Wolfram Language during this pass.

### Deliberately omitted

- No 3rdi, LOADOUT, Dogram, or other repo bodies were traversed. PR #86 explicitly consumes already-declared maps and does not import those runtimes; the discovered issue is internal to ALEX's cut/effect semantics.
- No broad sensor-fusion literature survey. The live discriminator does not require probabilistic estimation or real-sensor modeling.

### Missing / inaccessible

Fresh GitBook Front Room retrieval was attempted first and blocked by the connector safety layer. This is **access fog**, not evidence that the Front Room changed or disappeared. Its content was therefore not used as current evidence in this packet.

**Sufficiency:** sufficient for the bounded semantic audit.

## What newly surfaced

No new commit landed on `main` after the prior ALEXDEEPDIVE packet. Three new draft PRs did surface:

1. **#85 — NAME transport probe** demonstrates that lawful packet results survive a JSON round trip and remain observationally indistinguishable to the family gate while object identity is lost. This advances the already-live trust-boundary question but deliberately selects no transport contract.
2. **#86 — CROSS-APERTURE design** introduces finite compatible-world intersection with ordered lineage and `REFINE / REDUNDANT / BREAK` cut effects.
3. **#87 — CROSS-APERTURE implementation** realizes that design in a pure Python evaluator with tests and a frozen fixture.

### Why #86/#87 outrank #85 for this pass

#85 answers the next discriminator proposed by the previous packet: serialization is currently invisible to the NAME family gate. That is useful but stays inside the already-mapped result-admissibility frontier.

#86/#87 open a **new reusable semantic membrane**: ALEX now proposes to receipt sequential constraint intersection across multiple apertures. A small error in the meaning of `BREAK` could later contaminate contradiction attribution, observer comparison, or causal narration across domains. This therefore has larger architectural leverage while remaining cheaply testable.

## Evidence path

### A1 — Design semantics

PR #86 freezes:

```text
F_0 = W
F_i = F_(i-1) ∩ P_i^-1(y_i)
```

and classifies:

```text
if F_i = ∅:
    BREAK
elif F_i = F_(i-1):
    REDUNDANT
else:
    REFINE
```

It also says the lineage should record **the exact cut where the compatible family first became empty**, and explicitly refuses to diagnose whether the cause is sensor error, domain incompleteness, observer-time mismatch, map misdeclaration, or world change.

Source: `docs/superpowers/specs/2026-09-01-cross-aperture-intersection-001-design.md` at `abd01155d3cb43a091a338c95402ee87f6553a38`.

### A2 — Implementation semantics

PR #87 follows the design literally. For every supplied cut it computes a new intersection and then executes:

```python
if not compatible:
    effect = "BREAK"
elif compatible == compatible_before:
    effect = "REDUNDANT"
else:
    effect = "REFINE"
```

The loop continues after emptiness. Therefore, once one cut produces `[]`, every later cut also receives `effect = "BREAK"`, because the compatible set remains empty.

Source: `alex_runtime/cross_aperture_intersection.py` at `9a395dfdc3a386f94e14a05ff22a77cb0f83c95c`.

### A3 — Current tests do not discriminate first break from post-break persistence

`test_empty_intersection_is_model_break_not_reality_verdict()` checks only that the **last** lineage step is `BREAK` for the fixture. There is no specimen with a breaking cut followed by additional cuts.

Source: `tests/test_cross_aperture_intersection.py` at `9a395dfdc3a386f94e14a05ff22a77cb0f83c95c`.

### A4 — Exact set algebra

Wolfram exact calculation for a sequence with a breaking cut followed by another cut:

```text
W = {1,2,3,4,5,6,7,8}
A = {1,2,3,4}
B = {1,2,5,6}
BAD = {7,8}
C = {1,3,5,7}

W ∩ A           = {1,2,3,4}
... ∩ B         = {1,2}
... ∩ BAD       = {}
... ∩ C         = {}
cardinalities   = 4 -> 2 -> 0 -> 0
```

The final post-break cut does **not** create a new empty-set transition. It preserves already-established inconsistency.

This computation bears only the set-theoretic claim. It does not decide ALEX vocabulary.

### A5 — Breakpoint is traversal-relative, not necessarily culprit

A stronger hostile specimen uses:

```text
W = {1,2,3}
A = {1,2}
B = {2,3}
C = {1,3}
```

Exact results:

```text
A ∩ B = {2}
A ∩ C = {1}
B ∩ C = {3}
A ∩ B ∩ C = {}
```

Every pair is compatible; the triple is inconsistent. Across all six permutations, the compatible-set cardinalities are always:

```text
2 -> 1 -> 0
```

but **whichever aperture is processed third becomes the first `BREAK` step**.

Therefore:

```text
FIRST EMPTY PREFIX = attributable traversal event
!=
UNIQUE CAUSE OF INCONSISTENCY
```

No single aperture is intrinsically “the breaker” in this specimen. The contradiction belongs to the constraint set jointly.

### A6 — External constraint practice preserves the same distinction

The Microsoft Z3 Guide defines an unsatisfiable core as a **subset of named assertions that cannot be satisfied**, rather than identifying the last assertion in execution order as the cause of unsatisfiability.

Source: https://microsoft.github.io/z3guide/docs/logic/propositional-logic/#unsatisfiable-cores

SMT-LIB 2.7 likewise specifies `get-unsat-core` as returning labels for a subset of assertions whose conjunction (with relevant unlabeled assertions/assumptions) is itself unsatisfiable. It does not require the core to be minimal.

Source: https://smt-lib.org/papers/smt-lib-reference-v2.7-r2025-02-05.pdf, §4.2.7, p.73.

This is an **independent-domain structural precedent**, not authority over ALEX's vocabulary. It supports keeping inconsistency detection separate from blame/causal attribution.

## Claims

| ID | Claim | Class | Support | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #87 labels every cut after the first empty compatible set as `BREAK`. | observed | A2 | Could be intentional if `BREAK` means only “result is empty after this cut.” | supported |
| C2 | A post-empty cut cannot create a second transition from nonempty to empty. | mathematical | A4 | None within ordinary set intersection. | supported |
| C3 | The cut at which an ordered walk first becomes empty need not be the unique cause of inconsistency. | mathematical/inference | A5 | In some cases a single independently impossible cut really is sufficient; this claim is not universal denial of single-cut causes. | supported |
| C4 | `BREAK` currently conflates at least two possible readings: `first inconsistent prefix reached here` and `this cut caused the inconsistency`. | inference | A1+A2+A5 | The design partially guards this by refusing diagnosis and preserving full lineage. | supported, semantic pressure |
| C5 | Mature constraint tooling uses unsat subsets/cores rather than execution position alone for inconsistency localization. | source testimony | A6 | Unsat-core machinery is heavier than this v0 finite evaluator and should not be imported automatically. | supported |
| C6 | ALEX needs an unsat-core solver now. | proposal | none | Overkill for v0; a single hostile specimen can settle the immediate contract. | refused |

## Counterevidence and nearest boring explanation

The current result is **not catastrophic**. The lineage already preserves `compatible_before` and `compatible_after`, so a downstream reader can recover the first transition into emptiness. The design also explicitly says empty intersection does not diagnose cause. If `BREAK` is intended strictly as a surface classification meaning “the resulting compatible set is empty,” then the implementation is internally consistent.

The problem is narrower: `BREAK` is a semantically loaded word, and the design additionally speaks of “the exact cut where the compatible family first became empty.” Once multiple later cuts are also labeled `BREAK`, or when the first empty prefix depends on ordering among jointly inconsistent constraints, the label can silently overstate attribution.

## Strongest survivor

> **BREAKPOINT != CULPRIT.**
>
> **THE FIRST EMPTY PREFIX IS A FACT ABOUT AN ORDERED WALK. THE INCONSISTENCY MAY BELONG TO A SET OF CUTS JOINTLY.**

ALEX already has the right ingredients to preserve this law: ordered lineage, explicit fog, refusal to diagnose cause, and authority `none`. It only needs one discriminator before the vocabulary hardens.

## Smallest next discriminators / repo-worthy moves

1. **Freeze `POST-BREAK-001` before merging #87.** Construct a case where cut B makes the compatible set empty and cut C follows. Require the receipt to distinguish the first nonempty→empty transition from the later empty→empty step. The test should fail under current semantics if the desired law is “only the transition cut is BREAK.”
2. **Freeze `PAIRWISE-SAT-TRIPLE-BREAK-001`.** Use `{1,2}`, `{2,3}`, `{1,3}` over `W={1,2,3}` and verify that changing cut order changes the first breakpoint while leaving the final empty set invariant. Receipt law: `ordered breakpoint != unique causal attribution`.
3. **Do not add unsat-core machinery yet.** If future ALEX consumers need “which subset of apertures is jointly inconsistent?”, design that as a separate diagnostic surface (`conflict_set`, `inconsistency_core`, or equivalent) rather than laundering it through `effect = BREAK`.

## Residual fog

- The intended human meaning of `BREAK` in PR #86 is not fully explicit: state predicate, transition predicate, or causal label.
- It is unknown whether #87 is expected to stop evaluating after first break in a later revision.
- It is unknown whether ALEX will ever need minimal conflict localization; current evidence supports only keeping the possibility distinct.
- Fresh GitBook Front Room content was inaccessible this pass.

## Receipt

- **Created:** 2026-09-01 17:23 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitHub connector for repository witnesses; web retrieval for Z3/SMT-LIB primary documentation; Wolfram Language for exact finite-set calculations; model interpretation kept separate.
- **External byte egress:** public repository/docs only; no local/private corpus bytes supplied to external models.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-01-1723-BREAKPOINT-NOT-CULPRIT.md`
- **Promotion:** none

## Seal

> **EMPTY IS A PROPERTY OF THE SURVIVING FAMILY.**
>
> **THE STEP WHERE EMPTY FIRST APPEARS IS A TRAVERSAL RECEIPT.**
>
> **NEITHER FACT, BY ITSELF, NAMES A CULPRIT.**
