# REBIND-WITHOUT-RETROJECTION-001

**Status:** hostile research specimen / HOLD pending execution
**Owner:** ALEX research-pressure semantics
**Cross-project relation:** National Treasure owns the cross-case bridge; LOADOUT owns live-resolution behavior; 3rdi owns observer/projection rendering.

> **CONTINUITY MAY BE REBOUND. ATTRIBUTION MAY NOT BE RETROJECTED.**

## Research question

Can one logical organ remain continuously addressable across multiple exact software bodies without allowing the currently resolved body to impersonate the body that produced a historical consequence?

## Hypothesis

ALEX should preserve at least four distinct roles whenever a live logical reference participates in historical research formation:

```text
logical_ref
occurrence-local resolution receipt
exact body identity
optional target-relative macrostate
```

These roles may project together for a declared coarse target, but they must not be stored as one identity relation.

## Formal candidate

Let

```math
\pi:B\to L
```

map exact bodies to continuing logical identities. An occurrence-local resolution is a partial section:

```math
s_o:L\rightharpoonup B.
```

If `s_o(L)=b`, a consequence emitted under that occurrence may record:

```text
logical_owner_ref = L
resolved_body = b
occurrence = o
```

Historical producer identity is then body-local:

```math
producer(R_o)=b,
```

not dynamically recomputed as `current(L)`.

## Target-relative quotient

For a declared target `T`:

```math
b_1 \sim_T b_2 \iff T(b_1)=T(b_2).
```

Examples:

```text
T_owner:
  body A ~ body B
  owner=ALEX is sufficient

T_replay:
  body A !~ body B
  exact historical body required

T_derivation:
  body A !~ body B
  exact historical body required

T_historical_attribution:
  body A !~ body B
  exact historical body required
```

The quotient is therefore target-relative rather than a permanent collapse of the source state.

## Hostile crucible

### Fixture

```yaml
logical_ref: ALEX
occurrences:
  O1:
    resolution: RESOLVED
    body: sha:A
    receipt: R1
  O2:
    resolution: RESOLVED
    body: sha:B
    receipt: R2
  O3:
    resolution: UNRESOLVED
```

Required invariants:

```text
logical_ref(O1) == logical_ref(O2) == logical_ref(O3)
body(O1) != body(O2)
producer(R1) == sha:A
producer(R2) == sha:B
O3 does not silently fall back to an embedded or previous body and call it current
```

### Hostile replay

At `O4`, the live reference resolves to `sha:B`.

Input:

```text
replay historical receipt R1
```

Required behavior:

```text
historical_producer(R1) = sha:A
current_resolution(ALEX) = sha:B

CURRENT RESOLUTION != HISTORICAL PRODUCER
```

A replay request that requires historical execution must select `sha:A` through historical body resolution rather than substituting `sha:B`.

### Coarse projection control

For target `T_owner`, both historical bodies may lawfully project to:

```json
{"owner":"ALEX"}
```

This projection is valid only because body identity is declared irrelevant to that target. It does not authorize replay, derivation, or historical attribution from the coarse record alone.

## False-collapse detectors

Flag a research formation as under-specified if any historical consequence is attributable only to a live logical reference when body identity could affect evaluation.

Candidate detector:

```text
if historical_consequence
and producer_ref is live/mutable
and exact_body missing
and target not declared invariant over body:
    HOLD / REFUSE
```

This is a research rule until an existing ALEX contract proves it belongs in runtime validation.

## Relation to CHRONOBODY

CHRONOBODY established that exact historical reasoning bodies are first-class and that lifecycle state is distinct from executability.

This specimen pressures the complementary direction:

```text
exact body identity matters historically
AND
continuing logical identity remains useful operationally
```

The live name is not defective. It is simply insufficient for body-sensitive historical claims.

## Relation to reification / carrier work

A stable logical reference may function as a `CARRIER_REF` without requiring the exact body to be quotiented into an atomic macrostate.

```text
HAS CARRIER != HAS BEEN QUOTIENTED
CONTINUING OWNER != EXACT EMBODIMENT
```

This is an operational candidate for the distinction; it does not settle the general reification problem.

## Resolution-time HOLD

Do not add a universal fourth clock yet.

Represent resolution as an attributable event first:

```yaml
resolution_receipt:
  logical_ref: ALEX
  occurrence: O1
  resolved_body: sha:A
  manifest: sha:M1
```

Promote a distinct `resolution_time` coordinate only if a controlled case demonstrates information not already representable with world time, observer time, body time, and the resolution event itself.

## Kill conditions

Kill or narrow this specimen if:

1. current ALEX receipts already make the proposed false collapse impossible with no new distinction;
2. exact body identity never changes an answer under any historical ALEX target;
3. the target-relative quotient rule cannot be declared before inspecting the output;
4. logical reference plus existing manifest provenance is already lossless for historical replay;
5. the fiber/section vocabulary adds notation without adding a testable discriminator.

## Promotion gate

No runtime promotion from this document alone.

Promotion requires an executable fixture showing at least:

- two exact bodies under one logical reference;
- distinct body-sensitive historical receipts;
- a current-resolution / historical-producer mismatch case;
- an honest UNRESOLVED case;
- a coarse owner-only target where quotienting is demonstrably safe.

## Seal

> **THE CURRENT BODY MAY CARRY THE NAME FORWARD. IT MAY NOT CLAIM THE CONSEQUENCES OF A BODY THAT CAME BEFORE IT.**
