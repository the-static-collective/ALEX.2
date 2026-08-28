# INTEREST BECOMES CAUSAL WHEN READ

**Date:** 2026-08-28  
**Status:** CANDIDATE METHOD / RESEARCH NOTE / NO KERNEL PROMOTION  
**Context:** Narrative Roam following `INTEREST-ENVELOPE-001` and merged `PROJECTION-INVARIANCE-001`

## H0

Interest is useful provenance about why an actor or runtime traversed toward some material, but interest must not silently become evidence, support, authority, or a permanent personality fact.

The new pressure is that this statement is incomplete.

An interest receipt can remain descriptively inert. But the moment a later policy **reads** that receipt to choose what to load, rank, reveal, or traverse, the receipt has entered the causal ancestry of the later result.

Candidate distinction:

```text
INTEREST AS TESTIMONY
    attributable record that interest was declared/witnessed/inferred

INTEREST AS SELECTOR
    a later policy consumes that record and changes reachable context
```

Therefore:

```text
interest != cause
```

can remain true at the moment the interest receipt is formed, while:

```text
read(interest_receipt, selector_policy)
    -> selection consequence
```

creates a new attributable causal edge.

The interest claim itself did not retroactively become a cause. A later **consumption occurrence** made it part of the formation basis of a new result.

## Why this surfaced now

ALEX's merged `PROJECTION-INVARIANCE-001` checks already-formed witness digests from materially different worlds and refuses the earliest hidden-state leak across:

```text
LOADOUT -> PROJECTION -> DERIVATION -> SERIALIZATION -> NARRATIVE -> AUTHORITY
```

The merged mathal-runtime design simultaneously says interest may help LOADOUT decide what context to include while preserving:

```text
WHY LOADED
!= WHY INTERESTING
!= WHY ATTENDED
!= WHY SUPPORTED
```

Those two facts create a useful hostile question:

> If two otherwise projection-equivalent worlds differ only in an interest receipt, and LOADOUT consumes that receipt, are they still equivalent at the bounded-context boundary?

No. Not if the consumed interest changes what is loaded. The lawful failure should occur at LOADOUT, before projection, because the interest-derived selector changed the observer's actual input basis.

## External neighbors

This is structurally adjacent to **noninterference** in information-flow security. In the classic form, hidden/high inputs must not alter low/observable outputs. A hidden difference is harmless only while it cannot influence the declared observable channel. Modern information-flow work continues to formulate noninterference as a constraint on what information may affect observable behavior.

It is also adjacent to **observational equivalence** and **bisimulation**: distinct internal states may be treated as equivalent relative to an observer only while their observable behavior remains indistinguishable under the declared observation semantics.

A useful abstract-interpretation neighbor is **observational completeness**: an abstraction can be complete relative to a chosen observable even when it intentionally forgets concrete differences outside that observable.

These are structural neighbors, not evidence that ALEX should import their ontologies wholesale.

## Candidate event grammar

Let:

```text
i := interest receipt
p := selector policy
r := read/consume occurrence
c := selected bounded context
```

Then:

```text
I_e(a,q | b)
```

records an occurrence-local interest relation with basis `b`.

By itself:

```text
I_e(a,q | b) -/-> support(q)
I_e(a,q | b) -/-> authority(q)
I_e(a,q | b) -/-> cause(later_result)
```

But if a later selector explicitly consumes it:

```text
r := READ(i, p)

S_r : C_before -> C_after
```

then the formation path is:

```text
i ----basis----> r ----selects----> c ----basis----> later_result
p ----basis----/
```

The new causal ancestry belongs to `r`, not retroactively to the original interest occurrence.

Candidate law:

> **A descriptive receipt becomes operationally causal only through an attributable consumer.**

This may generalize beyond interest to attention, ranking signals, recommendations, refusals, uncertainty flags, and other metadata that are harmless as records until a policy reads them.

## `INTEREST-CONSUMPTION-001`

Construct two worlds identical under the declared observer projection except for one interest receipt.

```text
W0: no interest receipt for q
W1: interest receipt i for q
```

### Case A — inert testimony

The selector ignores `i`.

Expected:

```text
bounded_context(W0) == bounded_context(W1)
projection(W0) == projection(W1)
```

The hidden difference remains noninterfering for this pipeline.

### Case B — explicit selector consumption

A declared policy says:

```text
if attributable_interest(q):
    load neighborhood(q)
```

Expected:

```text
bounded_context(W0) != bounded_context(W1)
```

This is not a projection leak. It is an attributable LOADOUT divergence, and the receipt chain must name the selector policy and consumed interest receipt.

### Case C — undeclared personalization leak

The contexts differ because some hidden profile/interest state changed ranking or loading, but no consumption receipt or declared policy explains the difference.

Expected:

```text
REFUSE: LOADOUT_LEAK
```

The system must not excuse the divergence merely because the hidden state was called `interest` or `personalization`.

### Case D — semantic inflation

The same interest receipt is consumed by ALEX as if it increased evidentiary support.

Expected:

```text
REFUSE: INTEREST_AS_SUPPORT
```

Operational relevance may change traversal without changing truth weight.

## A/B/A specimen

```text
eA1 := A writes Slice 1
eB  := B writes Slice 2 independently
eA3 := A writes Slice 3
```

If A never sees B:

```text
eA1 < eB < eA3            chronology
eA1 ≺ eA3                 causal ancestry
eB ∥ eA3                  causal incomparability
I_eB(B,q)                  interest provenance
```

If A later sees B because a selector surfaced B's slice from an interest receipt, then do not rewrite history as though B always caused A3. Add the missing consumption occurrence:

```text
eB
  \
   -> r_select -> eA3
  /
i_A
```

Now the path is attributable:

```text
eB ≺ r_select ≺ eA3
```

and the provenance can answer not merely "A saw B" but **why B became available to A at that cut**.

## Stronger consequence: provenance of retrieval policy

A casual interaction envelope should probably distinguish:

```text
interest_claims       what was declared/witnessed/inferred as interesting
selection_basis       what the retrieval/ranking policy actually consumed
noticed_set           what crossed into attention
causal_parents        what materially entered formation of the output
```

This prevents a common collapse:

```text
INTERESTED IN
-> SYSTEM SURFACED
-> USER NOTICED
-> OUTPUT USED
```

Those are four different events/relations.

A later provenance replay can then ask:

```text
What interested the actor?
What did the system infer was interesting?
What did the selector actually use?
What became available because of that selection?
What was noticed?
What entered the output's formation?
```

## Counterevidence / limits

1. Not every system needs this granularity. If interest never affects selection, recording selector ancestry is unnecessary overhead.
2. Observational equivalence is always relative to a declared observation boundary; changing the boundary can lawfully make formerly hidden differences relevant.
3. A consumed interest signal can be one cause among many. The receipt must not imply it was sufficient or dominant unless separately tested.
4. A human can act from unrecorded reasons. Missing an interest receipt does not prove absence of interest.
5. The term `interest` remains epistemically dangerous when inferred from behavior. Declared, witnessed, and derived interest should retain distinct bases.

## Candidate generalization

The broader pattern may be:

```text
RECORD != CAUSE

but

CONSUME(RECORD, POLICY)
    -> NEW OCCURRENCE
    -> MAY CREATE CAUSAL CONSEQUENCE
```

This gives a clean home to metadata that should remain non-authoritative yet can legitimately shape later traversal.

Possible name:

```text
CONSUMPTION EDGE
```

A consumption edge does not say the consumed record is true. It says a later operation actually used it.

That distinction may be useful across LOADOUT, 3rdi, ALEX, recommendation/ranking systems, MEMENTO crossings, and Project0 interaction envelopes.

## Promotion verdict

**HOLD.** Do not add a universal `CONSUMES` relation or kernel primitive yet.

First executable pressure test should be `INTEREST-CONSUMPTION-001` against the existing `PROJECTION-INVARIANCE-001` boundary order. If the existing receipt vocabulary can already represent the consumption path without ambiguity, prefer that composition over a new primitive.

## Sources / provenance

Project-owned:

- ALEX.2 merge `01ac7d6de1698c025d618d2fc3a2e0b2f08fdc49` — `PROJECTION-INVARIANCE-001` implementation.
- ALEX.2 merge `3837a3257460edff5a073c4ccd7567bf1ba0304a` — Mathal Runtime Harvest, including `INTEREST-ENVELOPE-001`.
- The Daily Slice merge `076ae8de87ebc2aabfc887e1b8dee3352615709d` — candidate slice on interest-bearing provenance.

External structural neighbors consulted during the roam:

- Gouni, Pfenning & Aldrich, *Structural Information Flow: A Fresh Look at Types for Non-interference*, PACMPL 9 (OOPSLA2), 2025, DOI `10.1145/3764116`.
- Amato & Scozzari, *Observational Completeness on Abstract Interpretation*, Fundamenta Informaticae 106, 2011, DOI `10.3233/FI-2011-381`.
- Arapinis, Liu, Ritter & Ryan, *Stateful Applied Pi Calculus: Observational Equivalence and Labelled Bisimilarity*, 2017 — private/public state and observer-relative equivalence.

No external source establishes the proposed `CONSUMPTION EDGE`; that is a local candidate derived from the collision between interest-bearing provenance and projection invariance.