# SKySLICEY72 — prediction field / coincidence boundary

**Status:** ALEX research-method note · no runtime promotion

## Core distinction

ALEX must distinguish a relation recognized after the target was visible from a prediction committed before inspection.

```text
RETROSPECTIVE FIT
observe x
-> choose/find relation R
-> note that R includes x

PREDICTION TEST
declare R
-> derive expected x
-> freeze prediction receipt
-> inspect
-> hit / miss / ambiguous
```

Both may be interesting. They have different formation histories and therefore different evidentiary force.

## `PREDICTION-FIELD-001`

Given an observed node field `N` and a declared relation grammar `R`, define a candidate closure:

```text
Cl_R(N)
```

and the unobserved prediction frontier:

```text
P_R(N) = Cl_R(N) \ N
```

A node in `P_R(N)` is not evidence merely because the grammar predicts it. It is a **testable absence / expectation** whose existence and derivation can be frozen before the next search.

## Minimum prediction receipt

A useful ALEX prediction receipt should preserve:

```text
prediction_id
formed_at / known_at cut
source node refs
relation grammar ref
exact derivation or deterministic calculation ref
predicted node / property / interval
search boundary
allowed outcomes
failure condition
```

The most important field is chronology: the prediction must be attributable to a cut before the observation used to test it.

## Coincidence remains valuable

A weird coincidence may open a new research branch:

```text
OBSERVATION
-> CANDIDATE RELATION
-> NEW HYPOTHESIS
-> PROSPECTIVE TEST
```

It becomes scientifically stronger only when the relation survives a later precommitted test. Do not discard coincidence; **change its type**.

## Orientation / aperture

SKySLICEY72 also adds an aperture-design question:

> How should the next observation be oriented so surviving hypotheses yield maximally different outcomes?

The orientation/cut belongs in the receipt because:

```text
same carrier
+ different aperture
-> different projection
```

ALEX should therefore preserve the declared search/probe orientation alongside the result when it is material to the claim.

## Negative space

Negative space becomes a prediction field only after the grammar is frozen:

```text
unseen / missing
!=
predicted

unseen / missing
+ precommitted relation grammar
-> prediction candidate
```

## Hostile controls

```text
prediction hit != causal explanation
prediction hit != unique decoder
post-hoc relation != prospective prediction
many flexible degrees of freedom can manufacture hits
failed prediction must remain in formation history
ambiguous observation must not be scored as success
```

## Example color toy

Under a declared secondary-color triad grammar:

```text
{orange, green, purple}
```

if `orange` and `green` are observed and the grammar was frozen first, `purple` can be placed in the prediction field as the missing third vertex.

This is a toy for chronology and closure, not color physics.

> **A COINCIDENCE OPENS A QUESTION. A PREDICTION RISKS THE DECODER BEFORE THE ANSWER ARRIVES.**
