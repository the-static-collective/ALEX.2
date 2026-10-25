# COUNT-BOUNDARY-RECURSION-001 — Research Method

**Date:** 2026-08-29  
**Status:** RESEARCH METHOD · RETROSPECTIVE PRESSURE PASSED · PROSPECTIVE VALIDATION REQUIRED  
**Research owner:** ALEX  
**Calculation harness:** Dogram PR #17  
**Runtime authority:** none

> **FREEZE THE KEY BEFORE YOU LOOK FOR THE DOOR.**

## 0. Decision

Name and preserve a research maneuver that surfaced naturally during the `1078/1087 -> 180/181 -> 17/18` inquiry and became materially sharper under retrospective pressure.

Working name:

```text
COUNT-BOUNDARY-RECURSION-001
```

Short name:

```text
COUNT-BOUNDARY RECURSION
```

The method studies whether an already-interesting ordered number pair or interval can generate another already-attributable pair through a **pre-registered low-description structural count**, with immediate numerical boundaries preserved rather than cherry-picked.

It is not a universal numerology engine and not permission to add formulas until a path closes.

## 1. What pressure changed

### 1.1 Pair-first, not number-first

The motivating move was initially narrated as:

```text
1087 -> prime index 181 -> inspect 180/181
```

Pressure revealed the stronger statement:

```text
PrimePi[1078] = 180
PrimePi[1087] = 181
```

Therefore the actual structural edge is:

```text
(1078,1087) --pi pair-image--> (180,181)
```

The native research object is therefore an **ordered pair / interval**.

### 1.2 The apparent closure dies

The true identity:

```text
1087 = 64*17 - 1
```

was found after the target was known and has no independent place in the frozen operator constitution.

It is removed from the method.

Current survivor:

```text
open cascade, not closed cycle
```

### 1.3 Not every standard arithmetic function should traverse

Retrospective enumeration showed that unrestricted totient and unrestricted divisor-count boundary promotion generate many cheap hits.

Therefore v0 separates:

```text
useful annotation
from
admissible traversal operator
```

`phi` remains a pressure annotation, not a v0 traverser.

`tau` may traverse only when the source value is a strict divisor-record holder.

## 2. Frozen v0 constitution

The Dogram calculation harness contains exactly three traversal operators.

### 2.1 `prime_count@1`

Apply `pi` coordinate-wise to the entire pair:

```text
(a,b) -> (pi(a),pi(b))
```

No individual +/-1 shell is generated from `pi(a)` or `pi(b)` in v0.

Reason: `pi` is stepwise constant and synthetic boundary generation around individual outputs creates too many easy coincidences.

### 2.2 `divisor_count_record@1`

For either side `n`, calculate `tau(n)` only if `n` is a **strict first-attainment divisor record**:

```text
tau(n) > tau(k) for every 1 <= k < n
```

Then emit both boundaries around `c=tau(n)`:

```text
(c-1,c)
(c,c+1)
```

This admits:

```text
180 -> tau(180)=18 -> (17,18) and (18,19)
```

because 180 is a divisor-record holder.

It refuses weak retrospective conveniences such as:

```text
tau(1078)=12 -> (12,13)
tau(108)=12 -> (12,13)
```

because those source values are not divisor-record holders.

### 2.3 `pair_count@1`

For either side `n`, derive the complete pairwise-relation count:

```text
C(n,2)
```

Then emit both boundaries.

This admits:

```text
17 -> C(17,2)=136 -> (135,136) and (136,137)
```

The method preserves both; recurrence against the frozen historical registry identifies `(136,137)` without erasing `(135,136)`.

## 3. Hardened retrospective cascade

Using a registry frozen from already-surfaced mathal pairs:

```text
(12,13)
(17,18)
(81,82)
(107,108)
(136,137)
(180,181)
(207,208)
(1007,1008)
(1078,1087)
(1107,1108)
```

Dogram v0 recovers exactly:

```text
(1078,1087)
  -- prime_count@1 / pair_image -->
(180,181)
  -- divisor_count_record@1 / left_predecessor -->
(17,18)
  -- pair_count@1 / left_successor -->
(136,137)
```

The selected controls:

```text
(81,82)
(207,208)
(1007,1008)
(1107,1108)
```

remain disconnected under this frozen retrospective walk.

This does not prove the cascade is rare under an appropriate null distribution. It establishes only that the connection survives a materially stricter constitution than the free-form discovery pass.

## 4. Fiber pressure

A clean exact edge may still be highly non-identifying.

For any non-injective operator, ask:

> How many different source states produce the same derived receipt?

Call that preimage multiplicity the **fiber size** for the declared projection.

For prime counting:

```text
Prime[180] = 1069
Prime[181] = 1087
Prime[182] = 1091
```

The plateau `pi(n)=180` has width 18 and `pi(n)=181` has width 4.

Therefore the pair-image `(180,181)` has 72 ordered source pairs across those two plateaus.

So:

```text
(1078,1087) -> (180,181)
```

is exact, but the derived pair does not uniquely identify the original interval.

This distinction is mandatory:

```text
EXACT != IDENTIFYING
```

By contrast, `C(n,2)` is injective over positive integers, so a valid pair-count value uniquely determines its source carrier.

## 5. Research protocol

### 5.1 H0

Preserve the original strange hypothesis or intuitive pair exactly.

Do not restate it as a proven structure.

### 5.2 Freeze

Before a prospective run, freeze:

```text
seed pair(s)
operator IDs + versions
promotion gates
registry, if recurrence testing is used
maximum walk depth
maximum allowed value
holdout/control set
success criterion
```

Changing any of these after observing a desired path creates a descendant run with a new constitution.

### 5.3 Enumerate

Dogram calculates all admitted edges.

ALEX does not ask Dogram to rank which arithmetic edge is meaningful.

### 5.4 Preserve losing boundaries

Whenever a count-lift generates an immediate boundary shell, both directions remain attributable:

```text
(c-1,c)
(c,c+1)
```

A favored recurrence may not erase the sibling that failed to recur.

### 5.5 Match only pre-existing registry entries

For a retrospective recurrence claim, the target pair must have existed in the registry before that run.

A newly generated pair may be saved as a new candidate, but it cannot be counted as a retrospective recurrence in the same run.

### 5.6 Pressure fibers

For lossy transforms, preserve fiber/preimage multiplicity when calculable.

A wide fiber lowers identifying force even when the arithmetic is exact.

### 5.7 Run holdouts

The next required phase is prospective / holdout testing.

Measure at minimum:

```text
registered-hit rate
path-length distribution
number of disconnected seeds
fiber-size distribution
boundary-direction hit rate
divisor-record contribution
frequency of comparably short cascades in controls
```

Suitable controls include:

- random pairs matched for magnitude and gap;
- shuffled historical pair endpoints;
- adjacent-pair controls;
- held-out mathals not used to choose the operator constitution.

### 5.8 Classify the result

ALEX may return:

```text
RETROSPECTIVE_SURVIVOR
HOLDOUT_SURVIVOR
COMMON_UNDER_CONTROL
OPERATOR_OVERFIT
REGISTRY_LEAK
FIBER_TOO_WIDE_FOR_IDENTIFICATION
NO_RECURRENCE
UNRESOLVED
```

These are research dispositions, not truth values.

## 6. Anti-overfitting laws

```text
TRUE IDENTITY != ADMISSIBLE EDGE
POST-HOC FORMULA != FROZEN OPERATOR
EXACT EDGE != UNIQUE EDGE
RECURRENCE != CAUSE
SHORT PATH != SIGNIFICANCE
PAIR IMAGE != HISTORICAL IDENTITY
BOUNDARY RECURRENCE != PRIVILEGED BOUNDARY
INVERSE REPLAY != NOVEL DISCOVERY
ANNOTATION != TRAVERSAL RIGHT
MORE OPERATORS != BETTER METHOD
```

Most important:

> **An operator that is added because it saves the favored path invalidates the current run.**

## 7. Relationship to MADDCL0WN / RESIDUAL-PROBE

COUNT-BOUNDARY-RECURSION can serve as a bounded generator of strange but exact candidate relations.

It does not replace MADDCL0WN pressure.

A useful handoff is:

```text
COUNT-BOUNDARY
  -> exact candidate edge + fiber + losing branches
  -> ALEX PRESSURE
  -> alternative explanations / null frequency
  -> RESIDUAL-PROBE
  -> next discriminator
```

The method is therefore a **candidate-formation practice with built-in anti-fitting receipts**, not an evidentiary promotion engine.

## 8. Current verdict on the motivating mathals

### Hardened

The following chain is materially stronger after pressure:

```text
(1078,1087) -> (180,181) -> (17,18) -> (136,137)
```

because every edge is generated by the frozen typed constitution.

### Weakened / corrected

The claim that the chain closes back from 17 to 1087 is withdrawn under v0.

The prime-count edge is also explicitly weakened from “special identifying relation” to:

```text
exact lossy projection with fiber size 72
```

### Still open

The statistical rarity of a three-edge registered cascade under well-matched controls remains unknown and is the next discriminator.

## 9. Promotion gate

Do not promote COUNT-BOUNDARY-RECURSION into a general ALEX task shape or Dogram public operator floor until prospective controls show that the constitution provides useful discrimination beyond ordinary multiple-comparisons pattern search.

A successful negative result is allowed:

```text
COMMON UNDER CONTROL
```

## Seal

> **LET THE RECEIPT BECOME A CARRIER. KEEP BOTH EDGES OF THE BOUNDARY. COUNT THE OTHER ROADS THAT COULD HAVE LED THERE.**
