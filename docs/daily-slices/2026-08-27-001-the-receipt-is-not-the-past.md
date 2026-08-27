# THE RECEIPT IS NOT THE PAST

**Date:** 2026-08-27  
**Status:** CANDIDATE METHOD / RESEARCH NOTE  
**Authority:** ALEX research branch only; not canonical project law.

## Trigger

The Daily Slice candidate **CAUSALITY WRITES RECEIPTS** proposed:

> receipt = present difference attributable to past interaction

and:

> a receipt is a tiny crossing

That survives pressure, but it needs one hard boundary:

> **A receipt may preserve real information about a vanished interaction without uniquely preserving the interaction that produced it.**

The dangerous inference is:

```text
present trace
  therefore
this exact past happened
```

That implication often fails.

## The missing distinction

A present state may have three very different evidentiary strengths:

```text
INFLUENCE
The past affected this state.

DISCRIMINATION
This state favors some candidate histories over others.

IDENTIFICATION
This state uniquely determines one admissible history under the model and evidence.
```

These must not be silently collapsed.

A muddy footprint may strongly discriminate `someone crossed wet ground` from `nothing crossed here`, while doing little to identify the exact walker, route, motive, or sequence of prior steps.

A hysteretic material may preserve that loading history mattered while many loading trajectories remain compatible with the same present response.

A software artifact may contain a compatibility scar proving prior constraint without uniquely reconstructing the exact discussion, abandoned branches, or decision path that produced it.

## Formal neighbor: identifiability

Recent causal-discovery literature defines **identifiability** as the ability to uniquely determine a causal effect or model from observed data plus stated assumptions. It also preserves **Markov equivalence classes**: distinct causal graphs may be statistically indistinguishable from observational conditional-independence structure alone.

This supplies an important ALEX brake:

```text
receipt detected
    ≠
causal history identified
```

Reference: Suzuki et al. (2026), *Advances in causal discovery methods for ecological time series*, Biological Reviews. DOI: https://doi.org/10.1002/brv.70180

Cox (2020) likewise distinguishes identifiability of causal effects from identifiability of the causal model itself and notes that data can support equivalence classes rather than one unique causal structure. DOI: https://doi.org/10.1111/risa.13553

## Formal neighbor: recoverability

Recoverability asks a different question from physical reversal:

> How much information about the prior state remains accessible after coarse-graining, noise, projection, or an irreversible update?

Lohmann (2026) frames backward inference in exactly these terms and emphasizes that an optimal recovery map is not a physical inverse of the original process. DOI: https://doi.org/10.1002/andp.202500556

Project translation:

```text
ORIGINAL HISTORY
      ↓ process / crossing / compression
PRESENT RECEIPT
      ↓ decoder + assumptions
RECOVERABLE FEATURES
      +
IRRECOVERABLE RESIDUAL
```

The correct output of a receipt decoder may therefore be a **set of compatible histories** or a posterior over histories, not one reconstructed story.

## Formal neighbor: many-to-one causation

A particularly useful 2026 philosophical result considers robust causal regularities where multiple histories can merge into the same effect state. The key pressure is simple: distinct histories may converge before the effect occurs, so counting or observing effects cannot automatically recover their unique antecedents.

Reference: Gyenis (2026), *The Causal Second Law*, Noûs. DOI: https://doi.org/10.1111/nous.70042

A related computational observation is older and blunt: models can often reach the same state through many different sequences of earlier states, making retrodiction underdetermined even when forward evolution is well specified. See Symons & Boschetti as summarized in Gershenson (2013), DOI: https://doi.org/10.1002/cplx.21435

## Hysteresis survives — but carefully

Hysteresis remains a strong literal neighbor for **formation receipt** because current or future behavior can depend on prior trajectory. But hysteresis demonstrates history-dependence, not necessarily full history recovery.

Paxton (2023) reviews hysteresis as system memory: later state transitions differ depending on prior trajectory. DOI: https://doi.org/10.1111/tops.12712

Favela (2020) likewise describes hysteresis as a case where system history constrains current state. DOI: https://doi.org/10.1111/phc3.12695

So:

```text
history matters
    ≠
whole history is stored
```

## A better receipt object

Instead of treating a receipt as a miniature transcript of the past, model it as a constrained channel from histories to present observations:

```text
HISTORY h
   ↓
formation / dynamics F
   ↓
RECEIPT r
```

The inverse image

```text
F⁻¹(r)
```

may contain:

- one admissible history;
- several admissible histories;
- a very large equivalence class;
- no history under the current model, indicating model error, contamination, or bad assumptions.

This gives a useful candidate measure:

```text
receipt specificity
    ∝
1 / size-or-entropy-of-compatible-history-class
```

This is a conceptual handle, not yet a committed scalar metric.

## The forensic connection gets stronger, not weaker

Larsson, Wagner & Brigandt (2012) formulate a **forensic evidence principle** for evolutionary-developmental inference: alternative historical developmental explanations should leave discriminating signatures, and rigorous testing depends on finding evidence that separates the competing hypotheses. DOI: https://doi.org/10.1002/jez.b.22458

That is almost exactly the right correction to the project-local word `receipt`:

> A trace becomes a strong receipt not merely by being caused by the past, but by discriminating among plausible pasts.

White et al. (2022) make a similar distinction in historical climatology between traces of the past and the higher-level inferences built from them, urging explicit separation of assumptions, likelihoods, and causal claims. DOI: https://doi.org/10.1002/wcc.808

## Candidate receipt stack v2

```text
EVENT / HISTORY
      ↓
TRACE
observable modification
      ↓
RECORD
persisted trace
      ↓
RECEIPT
trace posed against explicit candidate histories
      ↓
DISCRIMINATION
which histories become more or less plausible?
      ↓
IDENTIFIABILITY CHECK
is one history uniquely supported under stated assumptions?
      ↓
PROVENANCE CLAIM
bounded ancestry claim with remaining equivalence class exposed
      ↓
WITNESS
independent corroborating structure
```

This preserves the excellent original stack while preventing `receipt` from silently becoming `proof` or `complete replay`.

## Consequence for THE DIAMOND

The next crossing experiment should not ask only:

```text
Did recognizable organization appear after crossing?
```

It should ask three separate questions:

```text
1. RETENTION
Does the receiving state contain information about the source?

2. DISCRIMINATION
Does that information distinguish the true source/formation path from hostile alternatives?

3. IDENTIFICATION
Is the observed output sufficient to identify the actual ancestry uniquely, or do multiple source histories remain compatible?
```

A successful continuity experiment does not need perfect identification.

But it must not mistake:

```text
recognizable recurrence
```

for:

```text
uniquely attributable continuity
```

unless hostile alternatives have actually been ruled out.

## Proposed specimen: RECEIPT-COLLISION-001

Construct several distinct formation histories that deliberately converge on similar or identical surfaces.

```text
H1 ─┐
H2 ─┼──→ R
H3 ─┘

H4 ─────→ R'
```

Then give the decoder only `R` or `R'` and ask it to produce:

- candidate source histories;
- confidence over histories;
- discriminating features used;
- features irreversibly lost;
- explicit abstention where ancestry is not identifiable.

Controls:

- identical surface / different history;
- different surface / same relevant ancestry;
- contamination added after formation;
- deliberately misleading but noncausal resemblance;
- full formation receipt with replayable ancestry.

Score separately:

```text
source-retention
history-discrimination
history-identification
false-certainty
abstention-quality
```

The killer metric may be **false certainty**. A decoder that says `one history` when the receipt only supports an equivalence class is worse than one that returns bounded fog.

## Candidate law

> **The receipt is not the past.**
>
> A receipt is a present constraint on what the past could have been.
>
> Strong receipts narrow the admissible history class. Perfect receipts collapse it to one. Most do neither completely.

Or smaller:

```text
causal influence ≠ recoverable history ≠ identifiable history
```

## What remains unresolved

- When should two histories count as meaningfully different rather than irrelevant microscopic variants?
- What equivalence relation should a specific experiment impose before asking whether ancestry is identifiable?
- Can `formation receipt` be defined as retention of task-relevant path information rather than literal path replay?
- Does a stigmergic receipt need a second axis for **future causal leverage**, independent of backward recoverability?
- Can DIAMOND deliberately compare a carrier that preserves strong predictive structure but weak historical identifiability against one that preserves exact ancestry but little generative power?

That last contrast may be especially important. A thing can be excellent at carrying **what to do next** while being poor at telling us **exactly how it got here**.

## Provenance

Project source:

- The Daily Slice, 2026-08-27, **RE-SEATED: BRUNCH AGAIN, STILL EARLY — CAUSALITY WRITES RECEIPTS**, commit `d11bbcd0ff64ed9d350eb6a855d06615b1550d1e`.

External evidence path:

- Suzuki et al. 2026 — causal identifiability / Markov equivalence — https://doi.org/10.1002/brv.70180
- Lohmann 2026 — recoverability under coarse-graining and irreversible information loss — https://doi.org/10.1002/andp.202500556
- Gyenis 2026 — causal histories may merge into shared effects — https://doi.org/10.1111/nous.70042
- Cox 2020 — causal-model and causal-effect identifiability — https://doi.org/10.1111/risa.13553
- Jiang & Kumar 2019 — information from immediate and distant causal history may persist in present dynamics — https://doi.org/10.1029/2019WR025820
- Larsson, Wagner & Brigandt 2012 — forensic evidence principle / discriminating historical explanations — https://doi.org/10.1002/jez.b.22458
- White et al. 2022 — distinguish traces/data from inferences about past conditions — https://doi.org/10.1002/wcc.808
- Paxton 2023 — hysteresis as history-dependent system memory — https://doi.org/10.1111/tops.12712

## Epistemic split

**Documented fact:** Present observations can retain information about past dynamics; causal inference often leaves equivalence classes rather than uniquely identifiable models; coarse-graining and observation can make prior information irrecoverable; hysteretic systems can retain path dependence.

**Inference:** The project-local `receipt` concept is safer and more useful if it explicitly returns a compatible-history class rather than pretending every persistent trace uniquely reconstructs its cause.

**Speculation / candidate method:** `RECEIPT-COLLISION-001`, receipt specificity, and the five proposed scores are ALEX-local research instruments, not established scientific standards.

## Working seal

> **Causality writes receipts, but causality also writes collisions.**
>
> **Different pasts can arrive at the same present.**
>
> **A trustworthy decoder preserves that fog instead of forging a history to fill it.**
