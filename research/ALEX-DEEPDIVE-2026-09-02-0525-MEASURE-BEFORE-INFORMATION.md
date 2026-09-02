# ALEXDEEPDIVE — MEASURE-BEFORE-INFORMATION-001

**Date:** 2026-09-02  
**Status:** RESEARCH · AUDIT → PRESSURE · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION  
**Promotion:** none

## Ground

- **Question:** After separating final intersection, ordered breakpoint, and conflict explanation, what is the next attribution trap in `CROSS-APERTURE-INTERSECTION-001`?
- **Desired consequence:** determine whether per-cut `REFINE` / `REDUNDANT` effects can lawfully be read as order-independent information or contribution, and freeze the smallest boundary before numeric information semantics are introduced.
- **Stop condition:** establish the exact order dependence of marginal pruning; test one order-independent attribution candidate; attack its hidden assumptions; do not add an information metric, Shapley runtime, probability model, or cross-project ontology.
- **Corpus/date:** ALEX.2 state visible 2026-09-02 05:25 America/Chicago; `main@7ddbc604b697995b59511b9c7a633d2a5bb21695`; draft PR #87 head `a1d8adae313c5a63551afdd51a23da9607ae9013`.
- **Authority/effect boundary:** research packet only. No merge, runtime/schema/skill promotion, evidence-weight semantics, sensor ranking, truth/canon authority, or automatic state quotienting.
- **Task shape:** AUDIT → PRESSURE.
- **Formation trace active:** no. The previous packet supplies discovery context only; claims below are rebuilt from current repository witnesses, exact computation, and external sources.

## World cut

### Included

- Static Collective GitBook Front Room, freshly searched this pass for orientation only. Its current orientation law remains: stable landmark, bounded traversal, current project evidence outranks the room, and unresolved fog stays visible.
- ALEX.2 constitutional files on `main`: `AGENTS.md`, `skills/alex/SKILL.md`, `skills/alex/references/research-receipt.md`.
- Previous packet `research/ALEX-DEEPDIVE-2026-09-01-2324-ENDPOINT-BREAKPOINT-SPLIT.md`.
- Draft PR #87 current head `a1d8adae313c5a63551afdd51a23da9607ae9013`, especially `alex_runtime/cross_aperture_intersection.py` and `tests/test_cross_aperture_intersection.py`.
- Exact Wolfram Language permutation enumeration and cooperative-game calculation for a three-cut finite specimen.
- Lloyd S. Shapley, “A Value for n-Person Games” (1953), inspected through the Cambridge reprint metadata/page; and Rothblum’s combinatorial description of the Shapley value as expected marginal contribution over all player orders.
- R. V. L. Hartley, “Transmission of Information,” *Bell System Technical Journal* 7(3), 535–563 (1928), DOI `10.1002/j.1538-7305.1928.tb01236.x`.
- Claude E. Shannon, “A Mathematical Theory of Communication,” *Bell System Technical Journal* 27, 379–423 and 623–656 (1948), inspected in the Harvard-hosted corrected reprint / IEEE primary-source surface.
- Modern submodular-cover scholarship only as confirmation that ordinary coverage functions are a standard submodular family; the key property is also derived directly below.

### Deliberately omitted

- No 3rdi, LOADOUT, Dogram, Bayesian sensor fusion, or machine-learning attribution body. The live distinction is already visible inside ALEX's finite set-intersection semantics.
- No claim that Shapley values are the correct ALEX attribution mechanism.
- No claim that state cardinality is epistemic probability, evidence weight, or semantic importance.
- No automatic quotient of observationally indistinguishable world states.

### Missing / inaccessible

None required for this bounded pass.

**Sufficiency:** sufficient.

## Current repository witness

PR #87 evaluates declared finite fibers in supplied order:

```text
F_i = F_(i-1) ∩ P_i^-1(y_i)
```

Its current effect labels are deliberately qualitative:

```python
if compatible == compatible_before:
    effect = "REDUNDANT"
elif not compatible:
    effect = "BREAK"
else:
    effect = "REFINE"
```

The current test floor freezes `POST-BREAK-001` as:

```text
REFINE -> BREAK -> REDUNDANT
```

and the module docstring explicitly says it does not rank witnesses or diagnose model breaks.

This is important: the implementation presently records what a cut did **at that prefix of that supplied walk**. It does not emit a scalar information quantity or global contribution score.

No newer commit has landed on `main` since the previous ALEXDEEPDIVE packet. PR #87 remains draft at the same exact head inspected by the previous packet. The present pass therefore does not manufacture novelty from repository churn; it pressures a still-unfrozen semantic consequence of the same branch.

## H0 — the tempting overread

> A cut that `REFINE`s contributes information, while a cut that is `REDUNDANT` contributes none.

Literalized:

```text
walk-local effect label
->
order-independent aperture contribution
->
epistemic information value
```

This chain does not survive pressure.

## Exact hostile specimen — effect changes under reordering

Declare the same world and the same three compatible fibers:

```text
W = {1,2,3,4}
A = {1,2}
B = {1,2,3}
C = {1,2,4}
```

The full intersection is always:

```text
A ∩ B ∩ C = {1,2}
```

but exact Wolfram enumeration of all six orders gives:

| Order | Marginal removals | Effects | Final |
| --- | --- | --- | --- |
| A,B,C | 2,0,0 | REFINE, REDUNDANT, REDUNDANT | `{1,2}` |
| A,C,B | 2,0,0 | REFINE, REDUNDANT, REDUNDANT | `{1,2}` |
| B,A,C | 1,1,0 | REFINE, REFINE, REDUNDANT | `{1,2}` |
| B,C,A | 1,1,0 | REFINE, REFINE, REDUNDANT | `{1,2}` |
| C,A,B | 1,1,0 | REFINE, REFINE, REDUNDANT | `{1,2}` |
| C,B,A | 1,1,0 | REFINE, REFINE, REDUNDANT | `{1,2}` |

Thus aperture `A` can be either:

```text
REFINE by 2
REFINE by 1
REDUNDANT by 0
```

across different valid arrival contexts, even though the cut itself and the final family are unchanged.

More generally:

> **MARGINAL PRUNING BELONGS TO A CUT-IN-CONTEXT, NOT TO THE CUT ALONE.**

## Why this is ordinary submodular coverage

For a selected cut family `S`, define only a **declared counting utility**:

```text
v(S) = |W| - | intersection of fibers in S |
```

Let each cut's excluded states be:

```text
E_i = W \ F_i
```

Then by De Morgan:

```text
v(S) = | union of E_i for i in S |
```

So the state-elimination count is exactly a finite coverage function. Coverage functions are monotone and submodular: as more exclusions have already been accumulated, a new cut can eliminate only states not already eliminated. Its marginal count can therefore decrease with context.

This is a mathematical explanation of the observed `REFINE` → `REDUNDANT` order sensitivity. It does **not** turn pruning count into epistemic information.

A modern submodular-cover reference explicitly treats ordinary set coverage as a canonical submodular function:

- Chekuri, Inamdar, Quanrud, Varadarajan, Zhang et al., “Algorithms for covering multiple submodular constraints and applications,” *Journal of Combinatorial Optimization* 44, 979–1010 (2022): https://link.springer.com/article/10.1007/s10878-022-00874-x

## PRESSURE: can an order-independent contribution be constructed?

Yes — but only after declaring an objective.

If, **for this specimen only**, the objective is uniform count of excluded represented states,

```text
v(S) = number of represented world states eliminated by cuts S,
```

then the Shapley value provides one principled order-average: each player's value is its expected marginal contribution over all player orders.

Shapley's original value was introduced for cooperative games in 1953. A later Cambridge treatment summarizes the familiar combinatorial representation as each player's expected marginal contribution to the players preceding it, averaged uniformly over all orders:

- Shapley, “A Value for n-Person Games”: https://www.cambridge.org/core/books/abs/shapley-value/value-for-nperson-games/1AA9D343DE7A87A97F69E999D329B57A
- Rothblum, “Combinatorial representations of the Shapley value based on average relative payoffs”: https://www.cambridge.org/core/books/abs/shapley-value/combinatorial-representations-of-the-shapley-value-based-on-average-relative-payoffs/2A1DFB90CA4D3D9334ED12A11B774470

For the exact specimen above, Wolfram gives:

```text
v({})       = 0
v({A})      = 2
v({B})      = 1
v({C})      = 1
v({A,B})    = 2
v({A,C})    = 2
v({B,C})    = 2
v({A,B,C})  = 2

Shapley(A) = 1
Shapley(B) = 1/2
Shapley(C) = 1/2
```

That is a valid order-independent allocation of **this declared counting utility**.

It is not yet an ALEX information metric.

## Direct counterexample — representation cloning changes the score

Now change no aperture logic and no observable distinction. Merely replace represented state `3` by two clones `3a` and `3b` that have exactly the same membership pattern across all three fibers:

```text
W' = {1,2,3a,3b,4}
A' = {1,2}
B' = {1,2,3a,3b}
C' = {1,2,4}
```

The represented observational structure is a refinement of the same coarse possibility: `3a` and `3b` are indistinguishable to every declared cut in this specimen.

Exact Wolfram recomputation changes the uniform-count game from:

```text
original:  A=1,   B=1/2, C=1/2    total reduction=2
```

to:

```text
clone-3:   A=3/2, B=1/2, C=1      total reduction=3
```

No new aperture discriminating power was introduced. The score changed because the representation supplied one previously single possibility twice.

Therefore:

> **ORDER-INDEPENDENT != REPRESENTATION-INDEPENDENT.**
>
> **A FAIR ALLOCATION RULE CANNOT REPAIR AN UNDECLARED UTILITY OR MEASURE.**

The issue is not specific to Shapley. Any metric based directly on raw represented cardinality inherits a state-granularity choice unless an owning model declares why those represented states carry the chosen weights.

## Hartley / Shannon pressure — count is a special information model, not neutral semantics

Hartley’s 1928 paper develops a quantitative communication measure based on the logarithm of the number of possible symbol sequences:

- R. V. L. Hartley, “Transmission of Information,” *Bell System Technical Journal* 7(3):535–563 (1928): https://onlinelibrary.wiley.com/doi/10.1002/j.1538-7305.1928.tb01236.x

The original text states the practical measure as the logarithm of the number of possible symbol sequences. That is a disciplined counting model, not a warrant to treat every arbitrary research-state discretization as intrinsically equipotent.

Shannon’s 1948 paper explicitly extends the theory to statistical structure and probability:

- C. E. Shannon, “A Mathematical Theory of Communication,” corrected reprint: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
- IEEE primary-source surface: https://reach.ieee.org/primary-sources/a-mathematical-theory-of-communication/

Shannon’s introduction says the extension includes savings possible from the statistical structure of the source. His entropy measure depends on a probability distribution, not cardinality alone.

The useful ALEX boundary is therefore narrower than “use Shannon entropy instead”:

```text
raw set shrink
!=
information gain by default
```

A numerical information claim first needs an attributable model for what the alternatives are and how they are measured or weighted.

## Strongest survivor

> **THE SET SHRINK CAN BE RECEIPTED WITHOUT NAMING ITS VALUE.**
>
> **MARGINAL PRUNING IS WALK-LOCAL.**
>
> **ORDER-INDEPENDENT CONTRIBUTION REQUIRES A DECLARED UTILITY.**
>
> **EPISTEMIC INFORMATION REQUIRES AN ATTRIBUTABLE MEASURE / PROBABILITY MODEL, NOT RAW CARDINALITY BY STEALTH.**

This is exactly why PR #87's current qualitative vocabulary is safer than a premature numeric `information_gain` field.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #87 currently emits walk-local `REFINE` / `REDUNDANT` / `BREAK` labels and no numeric information score. | observed | PR #87 head `a1d8ada...`, runtime + tests | PR remains draft; no canonical runtime promotion. | supported |
| C2 | The same fixed cut can be `REFINE` or `REDUNDANT` depending on supplied order. | mathematical | exact six-permutation Wolfram specimen | Some cut families may give order-stable marginal effects. | supported |
| C3 | Final intersection remains order-invariant while marginal removals are order-dependent. | mathematical | set algebra + exact Wolfram replay | Applies to fixed cut family; not to changing maps/observations. | supported |
| C4 | Uniform eliminated-state count is a monotone submodular coverage function. | mathematical | De Morgan reduction to union-of-exclusions + submodular coverage precedent | This says nothing about epistemic weighting of states. | supported |
| C5 | A Shapley value can make this declared counting utility order-independent by averaging marginal contributions over orders. | mathematical / scholarly | exact Wolfram calculation + Shapley/Rothblum | Choice of characteristic function remains external to Shapley. | supported |
| C6 | The cardinality-based Shapley allocation is representation-sensitive under observationally indistinguishable state cloning. | mathematical counterexample | exact clone-3 Wolfram recomputation | A separately declared weighting/quotient could restore invariance, but that is new model structure. | supported |
| C7 | Raw cardinality reduction is automatically epistemic information gain. | proposed overclaim | none | Hartley/Shannon pressure + clone counterexample + undeclared state weights. | refused |
| C8 | ALEX should implement Shapley attribution now. | proposal | none | No current consumer has established a need or declared utility/measure. | refused |

## Contradictions and alternatives

### Alternative A — keep only walk-local qualitative effects

This is the current PR #87 behavior. It is sufficient for tracing how a supplied ordered walk narrowed the compatible family. No extra measure is needed.

**Current verdict:** preferred v0 posture.

### Alternative B — add raw cardinality deltas

This can be useful as a descriptive statistic:

```text
|F_before| - |F_after|
```

but must remain explicitly `represented_state_count_delta`, not silently `information_gain` or `evidence_weight`.

**Current verdict:** possible future projection, not needed now.

### Alternative C — add order-independent contribution attribution

Requires an explicitly declared utility/measure first. Shapley is one candidate once that game is actually declared; other allocation rules are possible.

**Current verdict:** HOLD until a real consumer exists.

### Alternative D — quotient observationally indistinguishable states first

This could make some count metrics invariant to exact duplicates, but quotienting can also erase hidden distinctions that an owning model intentionally preserved. ALEX cannot silently decide those states are semantically identical merely because the current aperture family fails to distinguish them.

**Current verdict:** REFUSE as automatic preprocessing.

## Nearest boring explanation

Nothing exotic is required. Sequential finite-set intersection is an ordered fold over a commutative operation. Marginal changes naturally depend on what has already been intersected. Counting eliminated elements is a coverage function with diminishing returns.

The architectural hazard appears only when a truthful local receipt is rhetorically upgraded:

```text
this cut removed no new represented states at this prefix
```

into:

```text
this aperture has no information
```

Those are different claims.

## Bridge ledger

| Move | Type | Evidence bearing | Promotion limit |
| --- | --- | --- | --- |
| finite intersection → union of excluded states | documented mathematical identity | exact for current finite model | bears coverage/count semantics only |
| coverage count → submodularity | documented mechanism / exact derivation | explains diminishing marginal pruning | does not create epistemic value |
| order-dependent pruning → Shapley averaging | formal mathematical construction | proves one possible order-independent allocation after utility declaration | no claim Shapley is canonical for ALEX |
| raw possibility count → Hartley | historical mathematical precedent | shows counting/log-count can be a disciplined information model | does not justify arbitrary state granularity |
| probability-weighted uncertainty → Shannon | historical mathematical precedent | shows statistical structure is additional model content | does not prescribe a probability model for ALEX |

## Pressure

- **Direct counterexample:** observationally indistinguishable state cloning changes cardinality-based contribution scores.
- **Nearest boring explanation:** ordinary diminishing returns in a coverage function.
- **Independent-domain recurrence:** cooperative-game attribution and classical information theory both require a declared value/probability structure before numerical attribution means what its label suggests.
- **Serendipity trap:** Shapley is not promoted merely because it elegantly removes order dependence.
- **Forced-equilibrium check:** no competing metric is kept alive merely for symmetry; current qualitative trace is sufficient unless a consumer asks a new question.
- **Ghost-promotion check:** previous breakpoint/culprit work remains valid, but does not itself support information-value claims.

## PRESSURE verdict

- **Seed:** `REFINE means this aperture contributed information; REDUNDANT means it did not.`
- **Literal verdict:** disproved as an order-independent or epistemic statement.
- **What broke:** cut-local attribution, order invariance, and raw-cardinality neutrality.
- **What survived:** effect labels are truthful receipts about a cut at a particular prefix; cardinality deltas can be lawful descriptive statistics if named narrowly.
- **Why it survived:** exact permutation algebra and the current runtime contract support walk-local interpretation.
- **New prediction:** any future global contribution score will need an explicit utility/measure and should be tested against representation refinement/cloning before semantic promotion.
- **Residual weirdness:** a Shapley allocation of raw excluded-state count is mathematically elegant and exact, yet can change when the model duplicates an observationally indistinguishable state. The elegance therefore exposes rather than removes the hidden modeling choice.
- **Next discriminator:** freeze one reorder specimen where a named cut changes `REFINE` ↔ `REDUNDANT` while the final compatible set remains identical.

## Smallest next discriminators / repo-worthy moves

1. **Freeze `ORDER-RELATIVE-REDUNDANCY-001` on PR #87.** Use the exact `{A,B,C}` specimen above in two orders, for example `A,B,C` and `B,C,A`. Require identical final `{1,2}` while requiring cut `A` to be `REFINE` in the first walk and `REDUNDANT` in the second. This proves that `effect` is a cut-in-prefix receipt, not an intrinsic aperture score.
2. **Document one sentence beside effect semantics:** `REFINE / REDUNDANT / BREAK describe the effect of this cut on the current compatible set in supplied order; they do not measure global aperture information, evidentiary weight, or order-independent contribution.` No new schema is needed.
3. **If a future consumer asks for numeric contribution, require a measure declaration before choosing a formula.** Pressure at least: state cloning/refinement invariance, probability/weight provenance, whether the score concerns represented-state elimination vs uncertainty vs decision utility, and whether order-averaging is actually desired. Only then compare Shapley or other allocation rules.

The previous packet's `PAIRWISE-SAT-TRIPLE-BREAK-001` discriminator also remains unimplemented on current PR #87 and still has independent value. This pass does not supersede it.

## Residual fog

- PR #87 remains draft and stacked on draft design PR #86.
- No current ALEX consumer has demonstrated a need for an order-independent aperture contribution score.
- The repository does not currently declare a probability distribution or canonical measure over finite world states for this evaluator.
- “Observationally indistinguishable under the current cuts” does not prove two world states are semantically identical in the owning model; automatic quotienting would be an authority expansion.
- If future world states carry nonuniform weights, continuous measure, or structural multiplicity, raw cardinality may be actively misleading rather than merely incomplete.

## Receipt

- **Created:** 2026-09-02 05:25 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE research pass
- **Tool/model boundary:** GitBook connector for Front Room orientation; GitHub connector for exact repository and draft-PR witnesses; Wolfram Language for exact permutation/Shapley/state-clone computation; web retrieval for Shapley, Hartley, Shannon, and submodular-cover source surfaces; interpretation kept separate from computation and source testimony.
- **External byte egress:** public repository content and public scholarship/documentation only; no private/local corpus bytes supplied externally.
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-02-0525-MEASURE-BEFORE-INFORMATION.md`
- **Promotion:** none

## Seal

> **THE SET SHRINK CAN BE RECEIPTED WITHOUT NAMING ITS VALUE.**
>
> **THE MARGINAL BELONGS TO THE WALK.**
>
> **THE SCORE BELONGS TO A DECLARED MEASURE.**
>
> **NO MEASURE SILENTLY BECOMES EVIDENCE.**
