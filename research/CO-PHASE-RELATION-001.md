# CO-PHASE-RELATION-001

**Date:** 2026-08-31  
**Status:** RESEARCH / RELATION-SEMANTICS PRESSURE · NO RUNTIME CHANGE · NO AUTHORITY PROMOTION

## Seed

A working grammar separated four verbs:

```text
predict -> compose -> construct -> create
```

Each verb may occur in one of two relational phases:

```text
not-co
co
```

The epistemic question for ALEX is not whether the grammar is useful. It is what, if anything, entering `co` phase is allowed to imply.

## Hard boundary

Let an operation occurrence be represented minimally as

```math
e=(v,c,A,t)
```

where

- `v` is the declared verb;
- `c in {0,1}` is the declared co-phase;
- `A` is the attributed participant set;
- `t` is the occurrence anchor.

The `co` bit records relational posture only.

It does **not** entail any of the following:

```text
co-phase
!= agreement
!= shared belief
!= evidence
!= evidentiary support
!= causal support
!= authority
!= consent outside the declared operation
!= canonical admission
```

> **CO DECLARES HOW AN OPERATION IS RELATED. IT DOES NOT SILENTLY MINT WHAT THE RELATION MEANS.**

## `CO-DECLARATION-001`

A lawful co-phase claim requires attributable declaration or an owning-system rule that is itself attributable.

ALEX may preserve:

```text
who participated
which operation was declared
whether co-phase was declared
when the declaration was available
which receipt supports that declaration
```

ALEX must not infer `co=true` merely because two agents produced compatible outputs.

```text
COMPATIBLE OUTPUTS != DECLARED CO-OPERATION.
```

## `CO-CONSUMPTION-001`

A co-phase declaration is inert with respect to downstream semantics until a declared consumer uses it.

If a later operation `g` changes behavior depending on the earlier co-phase, preserve that use as an explicit causal relation:

```math
CO\_PHASE(e) \xrightarrow{\text{consumed by}} g.
```

The consumer may alter routing, composition, or construction behavior according to its own contract.

The co-phase itself does not become support.

```text
RELATIONAL PHASE -> DECLARED CONSUMER
!=
RELATIONAL PHASE -> SUPPORT BY DEFAULT.
```

## `CO-HISTORY-NE-ENDPOINT-001`

Two formation histories may end in the same visible operation state while differing in when co-phase entered the walk.

For example:

```text
predict -> compose -> co-construct
```

and

```text
predict -> co-compose -> co-construct
```

may share a final `co-construct` surface.

ALEX must preserve the distinction when formation history is in scope:

```text
same endpoint label
!=
same formation relation set
```

Do not retroject later co-phase into earlier occurrences.

```text
LATER CO != EARLIER CO.
```

## `CO-PHASE-PROMOTION-GATE-001`

No rule of the form

```text
co -> support
co -> evidence
co -> authority
co -> canon
```

is admitted without an explicit owner-approved relation rule and supporting receipt.

This mirrors the existing ALEX floor:

```text
NO RELATION SILENTLY MINTS ANOTHER RELATION.
```

## Hostile specimens

### H1 — compatible but independent

Two agents independently construct the same result.

Expected:

```text
compatibility = preserved
co-phase = false/unknown unless declared
```

### H2 — declared co-operation, disagreement survives

Two agents explicitly co-compose a packet but retain incompatible interpretations.

Expected:

```text
co-phase = true for the composition occurrence
agreement = not inferred
shared belief = not inferred
```

### H3 — later co-phase

An initially solo construction is later brought into co-review.

Expected:

```text
construction occurrence remains not-co
review occurrence may be co
history is append-only
```

### H4 — same endpoint, different walk

Two histories reach the same final operation label with different co/not-co transitions.

Expected:

```text
endpoint projection may match
formation traces remain distinct
```

## Seal

> **CO IS A RELATION PHASE, NOT AN EPISTEMIC PROMOTION.**
>
> **THE DECLARATION MAY ENTER CAUSAL ANCESTRY WHEN A DECLARED CONSUMER USES IT.**
>
> **THE RECEIPT MUST PRESERVE WHEN CO ENTERED THE WALK.**
