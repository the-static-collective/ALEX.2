# WHEN IS A PARTIAL ORDER

**Date:** 2026-08-27  
**Status:** CANDIDATE METHOD / RESEARCH NOTE / NO KERNEL PROMOTION  
**Projects touched:** ALEX.2, The Daily Slice, eCODE, 3rdi, Project0, DerekDerrikDark

## Trigger

The Daily Slice now distinguishes:

```text
=     equality at a declared cut
:=    state-transition assignment
S_e   attributable causal successor
```

and proposes the local shape:

```text
W[n] --S_e--> W[n+1]
```

This is useful, but it contains a hidden risk: `n+1` can be read as one global total order.

The Front Room's Hero Spiral independently provides a neighboring specimen:

```text
ROOM A_0 -> ROOM B -> ROOM A_1
```

where the rendered room may recur while worldline and reachable future differ.

## External pressure

Lamport's 1978 happened-before relation is a partial order over events, not a universal wall-clock ordering. If two events cannot causally affect one another, neither need precede the other. A total order may be imposed for a particular algorithm, but that extra order is not identical to causal order.

The distributed-systems literature therefore supports a harder distinction:

```text
physical timestamp
!=
logical clock
!=
causal precedence
!=
chosen totalization
```

Related formal work also distinguishes timing, causality, and value relations rather than collapsing them into one temporal coordinate.

### Evidence path

- Leslie Lamport, "Time, Clocks, and the Ordering of Events in a Distributed System," *Communications of the ACM* 21(7), 1978. DOI: 10.1145/359545.359563.
- Teshima, Hiraishi & Yajima, "Algebraic Specification of Parallel Systems Based on Binary Relations between Events," *Systems and Computers in Japan* 19(10), 1988. DOI: 10.1002/scj.4690191002.
- Chetlur & Wilsey, "Causality information and proactive cancellation mechanisms," *Concurrency and Computation: Practice and Experience* 21(11), 2009. DOI: 10.1002/cpe.1399.
- Wang et al., "Multiclock Constraint System Modelling and Verification for Ensuring Cooperative Autonomous Driving Safety," *Journal of Advanced Transportation*, 2020. DOI: 10.1155/2020/8830752.

## Candidate correction

`S_e` should be treated as a **local attributable successor relation**, not automatically as a global successor clock.

For one local lineage:

```text
W_i[k] --S_e--> W_i[k+1]
```

can remain lawful.

Across a wider field, use an event relation:

```text
e_a ≺ e_b
```

only when an attributable causal path makes `e_a` available to or constitutive of `e_b`.

If neither relation is derivable:

```text
e_a || e_b
```

means **causally incomparable / concurrent for this model**, not "same time" and not "unknown which happened first on a wall clock."

This gives a stronger answer to the recent question "what does WHEN mean?":

> `WHEN` is first a position in an attributable causal partial order. Wall-clock time is an optional additional coordinate.

## Why this matters

A global `n -> n+1` can smuggle several false implications:

```text
all events share one master clock
all pairs of events are orderable
later timestamp implies causal descent
concurrent branches must be serialized before they can be represented
same rendered object implies same historical state
```

The partial-order model refuses those implications.

It also makes room for:

```text
          e_a
         /   \
root e_0       e_merge
         \   /
          e_b
```

where `e_a` and `e_b` are both descendants of `e_0`, neither caused the other, and a later merge event can lawfully depend on both.

## Candidate operator discipline

```text
=       equality within a declared state/cut
:=      state update performed by an event
S_e     local attributable successor induced by event e
≺       happened-before / attributable causal precedence
||      causal incomparability / concurrency
~       declared equivalence under a named projection
@t      optional physical or provider timestamp
```

None silently substitutes for another.

## `WHEN-PARTIAL-001`

Construct four events:

```text
e0 := initialize x = 1

eA := branch A assigns x_A := x + 1

eB := branch B records/refuses without seeing eA

eM := merge/read event that sees both eA and eB
```

Required relations:

```text
e0 ≺ eA
e0 ≺ eB
eA || eB
eA ≺ eM
eB ≺ eM
```

Hostile controls:

1. Give `eB` a later wall-clock timestamp than `eA`; this must not manufacture `eA ≺ eB`.
2. Give both events the same rendered state value; this must not collapse their histories.
3. Totalize events for display order; the chosen serialization must remain explicitly distinct from causal order.
4. Replay from the same root with the same local traces; each branch should remain reproducible without pretending the sibling branch was already visible.
5. Introduce a message from A to B; only then may a derived causal path from `eA` to a subsequent `eB2` become admissible.

## Relationship to current ALEX work

`RELATION-DERIVATION-001` already asks whether a semantic relation has an attributable support path rather than being manufactured by attention. `WHEN-PARTIAL-001` proposes applying the same discipline to temporal relations:

```text
observed order
!=
causal order

clock order
!=
causal order

serialization
!=
causal order
```

A temporal edge should therefore be derivable, receipted, and falsifiable in the same spirit as a support edge.

## Candidate principle

> **Do not ask only "what came next?" Ask "next along which attributable worldline?"**

The field-level structure may be a DAG before it is a timeline.

## Counterpressure

A total order is sometimes useful and necessary. Lamport explicitly showed how to extend a causal partial order to a total order for distributed algorithms. Therefore this note does **not** claim total orders are wrong.

It claims only:

```text
total order chosen for coordination
!=
causal order discovered from formation history
```

ALEX should preserve which one it is carrying.

## Unresolved fog

The hard next problem is **cut semantics**.

If the world is partially ordered, what exactly is `W[n]`?

Possible answers include:

- a state on one local worldline;
- a consistent cut across a distributed execution;
- a projection assembled from all events causally available to an observer;
- a deliberately serialized presentation layer.

These are not automatically equivalent.

The strongest next research question is therefore:

> **Can a "world state" be defined as an observer-relative consistent cut over attributable events, rather than as one universal frame?**

No promotion is claimed.