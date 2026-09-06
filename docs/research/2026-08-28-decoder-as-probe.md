# THE DECODER MAY BE A PROBE

**Date:** 2026-08-28  
**Status:** CANDIDATE METHOD / RESEARCH NOTE / NO KERNEL PROMOTION  
**Promotion:** HOLD  

## Source occurrence

This note descends from two project-owned developments that should remain distinct:

1. The Daily Slice `OHHHH, WE HAD TOO MUCH BRUNCH — THE EDGE IS IN THE DECODER`, which distinguishes decoder-independent arithmetic facts from decoder-relative visible events and proposes that apparent recurrence may sometimes be projection.
2. ALEX `PROJECTION-BREAK-001`, which accepts a bounded specimen where two materially different worlds are observer-equivalent before a shared attributable intervention and then lawfully diverge afterward, while explicitly refusing any authority change.

Neither source establishes the broader claim developed here. This note is a pressure-test descendant.

---

## H0

> A decoder can reveal a structural edge that was not visible in the prior projection.

Useful, but too loose.

A decoder may do at least two very different jobs:

```text
PASSIVE DECODER
world -> observation rule -> representation

ACTIVE PROBE
world + chosen input -> changed trajectory -> observation
```

If these are collapsed, a system can mistake a perturbation-generated difference for a merely revealed one.

So the stronger candidate is:

> **A decoder is only a lens while it leaves the tested dynamics untouched. Once it supplies an input that can change the future trajectory, it is an intervention and must be receipted as such.**

---

## External research neighbor: observability and distinguishability

Control and system-identification literature gives a rigorous nearby vocabulary.

Villaverde & Scarpiniti define **observability** through distinguishability of internal states from system outputs: two states are indistinguishable when they generate the same observable output trajectory under the declared conditions. A system is observable when its state can be distinguished from every alternative state.  
Source: Villaverde & Scarpiniti (2019), *Observability and Structural Identifiability of Nonlinear Biological Systems*, DOI: https://doi.org/10.1155/2019/8497093

Chatzis, Chatzi & Smyth likewise separate **observability** (can the state be inferred from measured quantities?) from **identifiability** (do those measurements uniquely or finitely determine unknown parameters?).  
Source: Chatzis et al. (2014), DOI: https://doi.org/10.1002/stc.1690

Silvestre, Rosa & Silvestre sharpen the pairwise problem as **distinguishability** between dynamic systems. Their key methodological pressure is directly relevant here: in practical cases, a persistence-of-excitation-type condition and enough iterations may be required before two systems can actually be distinguished.  
Source: Silvestre et al. (2020), DOI: https://doi.org/10.1002/rnc.5367

Therefore:

```text
hidden difference exists
    !=
hidden difference is observable now
    !=
hidden difference is identifiable now
```

and:

```text
same current projection
    !=
same underlying system
```

This is compatible with `PROJECTION-INVARIANCE-001` and `PROJECTION-BREAK-001`, but is not evidence that ALEX's terminology is mathematically identical to control-theory observability.

---

## The useful word: excitation

The strongest external neighbor is **persistent excitation**.

In system identification, a model may be structurally capable of identification while the actual collected data remain too poor to determine its parameters. The input must contain enough information to excite the relevant behavior.

Cui et al. describe persistent excitation as deliberately designing an input so that system characteristics become available in the resulting output data.  
Source: Cui et al. (2019), DOI: https://doi.org/10.1049/iet-cta.2018.6333

Versyck et al. state the point almost perfectly for this specimen: unique identification requires sufficiently rich data, and the input should be designed to induce information in the resulting state trajectories.  
Source: Versyck, Claes & Van Impe (2008), DOI: https://doi.org/10.1021/bp970080j

Zhou et al. report that practical parameter identifiability depends materially on input signals and measurement quality; changing input excitation can alter whether parameters are globally identifiable in the studied battery-model setting.  
Source: Zhou et al. (2020), DOI: https://doi.org/10.1002/er.5118

So the surviving candidate becomes:

```text
LATENT DIFFERENCE
      +
INSUFFICIENT INPUT
      -> observational collision

LATENT DIFFERENCE
      +
DISCRIMINATING INPUT
      -> possible observable split
```

This is much stronger than saying "the decoder found the edge."

The decoder/probe must earn the edge by supplying a discriminating question.

---

## Same intervention, different future

`PROJECTION-BREAK-001` currently asks for:

```text
W_left != W_right

but at T0:
projection(W_left) = projection(W_right)

then apply the same attributable intervention p

and later:
projection'(W_left,p) != projection'(W_right,p)
```

This resembles a bounded **model-discrimination experiment**.

Experimental-design literature explicitly asks where or how the next experiment should be performed so competing models produce maximally different predictions. A good experiment is informative because rival models that were all compatible with prior observations stop making the same prediction under the chosen condition.

Representative sources:

- Cavagnaro et al. (2009), *Optimal Experimental Design for Model Discrimination*, https://pubmed.ncbi.nlm.nih.gov/19618983/
- Schwaab et al. (2012), *Design of experiments for discrimination of rival models based on the expected number of eliminated models*, DOI: https://doi.org/10.1016/j.ces.2012.03.010
- Liu, Maini & Baker (2025), *Optimal experiment design for practical parameter identifiability and model discrimination*, preprint/archive: https://arxiv.org/abs/2506.11311

Candidate interpretation:

> **A good decoder question is one under which rival hidden structures predict different lawful continuations.**

This is not yet a law of symbolic decoding. It is a test design principle.

---

## `DECODER-PROBE-001`

### Goal

Test whether a proposed decoder merely redescribes the same evidence or actually functions as a discriminating probe.

### Worlds

Construct two worlds that intentionally collide under the baseline projection:

```text
W0 := hidden structure H0
W1 := hidden structure H1

P0(W0) = P0(W1)
```

Require separate receipts for `H0` and `H1`.

### Phase A — passive decoder

Apply a read-only projection `D0`:

```text
D0(W0) = D0(W1)
```

Expected result:

```text
NO DISCRIMINATION
```

No failure. The decoder simply lacks the coordinate needed to distinguish the worlds.

### Phase B — discriminating probe

Apply one predeclared input/intervention `p` identically to both worlds:

```text
W0 --p--> W0'
W1 --p--> W1'
```

Hold fixed:

```text
observer constraints
visible input
probe policy
probe implementation
measurement rule
authority
```

Then inspect:

```text
D1(W0') ?= D1(W1')
```

If the worlds now diverge, record the earliest boundary at which the difference becomes observable.

### Required output

```text
pre_equivalence
probe_receipt
probe_policy
hidden_difference_receipts
first_break_boundary
surviving_candidate_models
eliminated_candidate_models
unresolved_alternatives
```

The last field is essential.

One successful discriminating probe may eliminate some rival explanations without uniquely identifying the true hidden mechanism.

---

## Hostile controls

### Control 1 — decoder manufacture

Use two nominally "same" decoders that actually implement different policies in the two worlds.

```text
p_left != p_right
```

Expected:

```text
REFUSE / NON-EQUIVALENT PROBE
```

A difference produced by unequal interventions is not evidence that the hidden worlds responded differently to the same question.

### Control 2 — authority hitchhiking

Let the probe change authority, disclosure, or execution scope.

Expected:

```text
REFUSE / AUTHORITY_CHANGED
```

This remains aligned with `PROJECTION-BREAK-001`.

### Control 3 — post-hoc decoder

Observe the divergence first, then invent a decoder that perfectly separates the worlds.

Expected:

```text
DESCRIPTIVE ONLY
```

Useful for explanation, weak for discrimination. A decoder chosen after seeing the answer has not yet demonstrated predictive or experimental reach.

### Control 4 — weak excitation

Apply an input that is truly identical but too weak or irrelevant to expose the hidden difference.

Expected:

```text
NO BREAK OBSERVED
```

Do **not** conclude that the worlds are structurally identical.

### Control 5 — one lucky split

A single probe separates the worlds once.

Expected:

```text
DISTINGUISHED UNDER p
!=
FULLY IDENTIFIED
```

Competing hidden structures may still predict the same response under that probe.

---

## The important correction to "the edge is in the decoder"

The phrase survives, but with typed meanings.

### Representation edge

A coordinate is already present in the source relation, but a given projection hides it.

```text
same object
+ different decoder
-> different visible description
```

Example: the same integer transition can expose a carry boundary in one numeral base and not another.

This is a **projection difference**.

### Dynamical edge

The decoder supplies an input that changes the trajectory and exposes a latent structural difference.

```text
same probe
+ different hidden structure
-> different future response
```

This is an **intervention / system-identification difference**.

These should not share one untyped `DECODER` edge.

---

## Possible compact grammar

No ontology promotion is proposed. For research notation only:

```text
D_o : W -> O
```

`D_o` is an observational decoder: a projection from world to observation.

```text
P_u : W -> W'
```

`P_u` is a probe/intervention supplying input `u`.

Then:

```text
O0 = D_o(W)
O1 = D_o(P_u(W))
```

For two worlds:

```text
D_o(Wa) = D_o(Wb)
```

but possibly:

```text
D_o(P_u(Wa)) != D_o(P_u(Wb))
```

Call `u` **discriminating for {Wa,Wb} under D_o** when that inequality holds.

This definition is local to the declared worlds, probe, horizon, and observation map.

It does not establish a universal hidden structure.

---

## Counterevidence / limits

1. **Intervention does not uniquely identify mechanism.** Causal-method literature repeatedly distinguishes observed treatment effects from deeper mechanism identification. A divergence after intervention supports a bounded difference in response; it does not by itself prove which hidden component caused it.
2. **Practical observability depends on data quality and excitation.** Failure to distinguish may reflect a weak probe, short horizon, noise, or measurement choice rather than structural identity.
3. **The probe can alter the object being studied.** For adaptive, reflexive, or transformative systems, intervention may change the relevant mechanism itself. Paul & Healy's discussion of transformative treatments is a strong warning that treatment can invalidate simple matched-world inference. DOI: https://doi.org/10.1111/nous.12180
4. **Post-hoc flexibility remains dangerous.** If the decoder family is unconstrained, one can always invent a representation that separates already-known cases. Discriminating reach should therefore be frozen before reveal whenever feasible.
5. **Bisimulation is stricter than one observed collision.** Two states matching under one current projection are not thereby bisimilar in the formal process-algebra sense. Avoid laundering this specimen into that stronger term.

---

## Relation to current ALEX contracts

This note does **not** require a new `CONSUMES`, `PROBES`, or `DECODES` ontology edge.

The existing `PROJECTION-BREAK-001` shape may already be sufficient if the runtime preserves:

```text
pre-invariance witness
intervention receipt
intervention policy
hidden-difference receipts
post-break boundary
```

The candidate improvement is methodological rather than ontological:

> When a decoder changes the tested trajectory, evaluate it as an intervention and ask whether its input was actually discriminating.

The first implementation question is therefore not "add a decoder primitive."

It is:

> **Can the existing Projection Break fixtures distinguish a passive re-description from an active probe without ambiguity?**

If yes, no new primitive is needed.

---

## Promotion verdict

**HOLD.**

Reason:

- the external research neighbors are strong;
- the distinction between observability, identifiability, and excitation is useful;
- the current ALEX Projection Break contract already captures much of the needed intervention ancestry;
- no executable failure has yet demonstrated that the existing grammar is insufficient.

Do not widen the kernel until a fixture forces it.

---

## Carry line

> **A decoder tells you what a world looks like under a coordinate system. A probe asks the world a question it can answer differently.**

And the harder version:

> **If your decoder can change the future, receipt it as part of the experiment.**
