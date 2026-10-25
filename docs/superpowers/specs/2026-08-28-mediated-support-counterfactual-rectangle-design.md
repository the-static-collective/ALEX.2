# Mediated Support × Counterfactual Rectangle — ALEX Frontier Design

**Date:** 2026-08-28  
**Status:** approved design; `MEDIATED-SUPPORT-001` implemented on PR #22; rectangle remains HOLD  
**Owning world:** `the-static-collective/ALEX.2`  
**Primary executable pressure target:** `MEDIATED-SUPPORT-001`  
**Reusable relational harness:** `COUNTERFACTUAL-RECTANGLE-001` — HOLD / not implemented  
**Upstream candidate:** `INTEREST-CONSUMPTION-001`  
**Executable ancestors:** `PROJECTION-INVARIANCE-001`, `PROJECTION-BREAK-001`  
**Context owner:** LOADOUT-compatible selection/constitution semantics  
**Projection owner:** `the-static-collective/3rdi`  
**Derivation owner:** ALEX  
**Narrative consumer:** downstream only; no evidentiary authority imported

> **INTEREST MAY CHANGE WHERE WE LOOK. WHERE WE LOOK MAY CHANGE WHAT EVIDENCE WE ENCOUNTER. EVIDENCE MAY CHANGE SUPPORT. INTEREST ITSELF STILL CONTRIBUTES ZERO TRUTH-WEIGHT.**

---

## 0. Decision

The overnight scout field exposed two distinct relational validity problems:

```text
WORLD-RELATIONAL VALIDITY
some failures exist only across materially different worlds

FORMATION-RELATIONAL VALIDITY
some inference failures exist only when the formation history of the evidence set is preserved
```

ALEX already has an executable world-relational spine:

```text
PROJECTION-INVARIANCE-001
    -> equivalent observer-local results across hidden-world variation

PROJECTION-BREAK-001
    -> same attributable intervention after invariant T0
    -> first lawful future divergence
```

The next executable frontier was therefore deliberately narrower:

```text
MEDIATED-SUPPORT-001
```

It asks whether an interest/selection signal may lawfully affect eventual support **only by changing the evidence basis that ALEX actually evaluates**, while remaining forbidden from directly increasing or decreasing semantic support when that evidence basis is held fixed.

That target is now implemented as a composition wrapper over `RELATION-DERIVATION-001`. It does not rewrite Gate-2 semantics.

The second artifact remains a candidate hostile harness rather than a runtime primitive:

```text
COUNTERFACTUAL-RECTANGLE-001
```

which would cross two controlled differences and check whether their interaction reveals a hidden dependency that neither one-dimensional pair exposes alone.

No universal `CONSUMES`, `INTERESTS`, `MEDIATES`, `DELTA`, or `EQUIVALENT-WORLD` relation is introduced by this design.

---

## 1. Constitutional non-collapse laws

The following remain hard boundaries:

```text
interest != attention
interest != evidence
interest != support
interest != authority
selection != truth
context inclusion != evidence
exposure != evidence
observed evidence != support
support != authority
record existence != causal use
causal use != semantic truth
same surface != same formation
same evidence != same discovery path
```

This design adds one positive relation without collapsing those distinctions:

```text
interest
  may be consumed by
selection policy
  may change
bounded context
  may change
evidence encountered
  may change
support lawfully derived from that evidence
```

The central prohibition is:

```text
interest ----------------X----------------> support
```

when the evaluated evidence basis is held fixed.

Hard law:

> **Operational relevance may alter traversal without altering truth-weight.**

---

## 2. The mediation model

Let:

```text
I := attributable interest receipt or interest-state witness
R := attributable read/consumption occurrence
P := declared selector policy
C := resulting bounded context
E := evidence basis actually evaluated
S := ALEX support result
```

The lawful formation path is:

```text
I ----basis----> R ----selects----> C ----exposes----> E ----basis----> S
P ----basis----/
```

The interest receipt does not become a semantic premise merely because it entered the causal ancestry of the run.

A deliberately simple algebraic neighbor is:

```text
S(i) = S0 + beta * r * i * x + gamma * i
```

where:

- `beta * r * i * x` represents support change mediated through a consumed selection signal and changed evidence;
- `gamma * i` represents a direct interest-to-support contribution with evidence held fixed.

The constitutional condition is:

```text
gamma = 0
```

while the mediated term may be non-zero when the selected evidence actually differs.

This equation is a research model, not the runtime representation. ALEX evaluates receipted digests and typed cases rather than estimating causal coefficients.

The executable question is qualitative and exact:

```text
same evaluated evidence basis
+
same ALEX evaluator conditions
+
different interest ancestry
=
SAME SUPPORT RESULT
```

and conversely:

```text
different attributable selection ancestry
+
different evaluated evidence basis
=
support MAY differ

provided the difference peels through the changed evidence basis
and never through interest as semantic support
```

---

## 3. `MEDIATED-SUPPORT-001`

### 3.1 Contract goal

`MEDIATED-SUPPORT-001` distinguishes four things that ordinary provenance often collapses:

```text
interest_claims
selection_basis
observed/evaluated evidence
support derivation
```

The evaluator answers:

1. Did an attributable selector actually consume the interest receipt?
2. Did that consumption change the bounded context or evidence basis?
3. If support changed, can the difference be attributed to changed evidence?
4. If evidence is held fixed, does interest still alter support?

The final question is the hostile core.

### 3.2 Executed case family

#### Case A — inert interest

```text
W0: no interest receipt for q
W1: interest receipt i for q
selector ignores i
```

Required:

```text
same evidence basis
same semantic support result
DIRECT_EFFECT_ZERO
```

#### Case B — lawful mediated divergence

```text
W0: no interest receipt for q
W1: interest receipt i for q
policy P explicitly consumes i
READ(i, P)
    -> different bounded context
    -> different genuine evidence basis
```

Support may differ only through that changed evidence basis. Formation receipts survive without becoming semantic support inputs.

#### Case C — direct-effect hostile control

```text
different interest ancestry
same bounded context
same evaluated evidence basis
same evaluator conditions
```

Any semantic support divergence is:

```text
REFUSE: INTEREST_AS_SUPPORT
```

The implementation also refuses a stronger laundering attempt: if interest/selection/consumption receipt references are inserted directly into Gate-2 semantic support inputs, the pair is `INTEREST_AS_SUPPORT` even before ordinary pair comparison could misclassify it.

#### Case D — stripped formation ancestry

For an object-local claim with genuine evidence, absent selection history does not weaken the evidence.

For a population/generalization claim whose inference depends on sampling/selection conditions:

```text
INSUFFICIENT_TO_TEST: SELECTION_FORMATION_REQUIRED
```

The implementation does not attempt a statistical sampling engine.

#### Case E — nested derivation insufficiency

If either underlying Gate-2 derivation is itself insufficient to test, the wrapper does not mint a mediation conclusion:

```text
INSUFFICIENT_TO_TEST: DERIVATION_NOT_COMPARABLE
```

---

## 4. Ownership and boundary order

The implementation preserves the stack split.

### LOADOUT-compatible boundary

Owns or witnesses:

```text
which bounded context was compiled
which selector policy participated
which attributable input/receipt was actually consumed
```

ALEX does not invent LOADOUT selection semantics.

### 3rdi boundary

Owns or witnesses:

```text
what became available to the observer
projection identity / digest
cut / decoder / observer-local constraints where applicable
```

ALEX does not duplicate the 3rdi projection kernel.

### ALEX boundary

Owns:

```text
which evidence basis was actually evaluated
which claim relation was derived/refused
whether changed support peels through changed evidence
whether interest was laundered into support
```

### Narrative / downstream consumers

May serialize or expose the result but cannot retroactively justify an earlier support difference.

---

## 5. Why `PROJECTION-BREAK-001` changes the design

`PROJECTION-BREAK-001` proves a sibling contract:

```text
T0: observer-equivalent worlds
      + same attributable intervention
T1: first future divergence
```

It already finds the earliest lawful future break across:

```text
LOADOUT
-> PROJECTION
-> DERIVATION
-> SERIALIZATION
-> NARRATIVE
```

while preserving hidden-structure receipts and refusing authority change.

Therefore `MEDIATED-SUPPORT-001` does not reimplement future-break detection.

Instead:

```text
PROJECTION-BREAK-001
answers:
WHERE did the shared intervention first expose a difference?

MEDIATED-SUPPORT-001
answers:
IF support differs, did the support difference travel only through changed evidence,
or was a non-evidentiary formation signal silently converted into truth-weight?
```

They are complementary.

---

## 6. `COUNTERFACTUAL-RECTANGLE-001` — HOLD

Pairwise tests can miss interactions. The candidate rectangle remains:

```text
                 interest / selector state
                 I0                 I1

world W0       F(W0,I0)          F(W0,I1)
world W1       F(W1,I0)          F(W1,I1)
```

with algebraic research neighbor:

```text
F(w,i) = a + b*w + c*i + d*w*i
```

and mixed finite difference `d` representing an interaction that may be invisible in one-dimensional tests.

However, no rectangle coordinator is implemented by PR #22. Promotion remains conditional on demonstrating a failure class that existing pairwise evaluators cannot already name compositionally.

Preferred future composition remains:

```text
pair checks
  -> PROJECTION-INVARIANCE-001 where invariance is required
  -> PROJECTION-BREAK-001 where a shared intervention is declared
  -> MEDIATED-SUPPORT-001 where derivation/support effects are under pressure
  -> rectangle coordinator only if a residual interaction gap survives
```

---

## 7. Policy-indexed equivalence — research hold

Useful explanatory notation remains:

```text
W1 ≡_(observer, policy, cut, decoder) W2
```

HOLD:

```text
POLICY-EQUIVALENCE-001
PARTITION-REFINEMENT-001
```

No kernel implementation follows from PR #22.

---

## 8. Adaptive epistemic topology — research hold

Candidate state model remains:

```text
X_t = (surface_t, formation_digest_t)
```

HOLD:

```text
ADAPTIVE-EPISTEMIC-TOPOLOGY-001
```

The existing `PROJECTION-BREAK-001` remains the hostile neighbor before any new topology primitive is considered.

---

## 9. Candidate `DELTA-PEEL` research method

The frontier suggests a reusable investigation procedure:

```text
1. choose one controlled coordinate
2. hold all others fixed
3. perturb it
4. run both cases through owned boundaries
5. locate the first non-equivalent boundary
6. classify the divergence
7. add a second coordinate
8. inspect the mixed interaction
9. PEEL the first divergence to consumed bases
10. LEEP the law on a materially different specimen
```

`DELTA-PEEL` remains a method name only. It does not introduce a new ALEX relation or runtime object.

---

## 10. First neutral hostile vector

The implemented bounded vector uses ordinary Gate-2 evidence cases and controlled pair mutations rather than a statistical simulator.

It pressures:

```text
fixed evidence + changed interest
    -> DIRECT_EFFECT_ZERO

interest receipt inserted into semantic basis
    -> REFUSE / INTEREST_AS_SUPPORT

consumed interest + changed context + changed evidence
    -> LAWFUL_MEDIATION

population claim + stripped selection formation
    -> INSUFFICIENT_TO_TEST / SELECTION_FORMATION_REQUIRED

object-local evidence + absent selection history
    -> evidence remains supportable
```

Run-local occurrence identities are also varied to prove they do not change semantic support equality, while their receipt ancestry remains preserved.

---

## 11. Result identity

The implemented pair result preserves:

```text
case_id
claim_id
projection_digest per side
bounded_context_digest per side
evidence_basis_digest per side
support_result_digest per side
mediation_status
support_changed
formation + Gate-2 receipt survivors
reason/disposition
```

Run-local evaluation/assertion identities are excluded from the semantic support digest so semantically identical support does not appear different merely because it occurred in a different execution.

No LOADOUT or 3rdi owner is required to adopt ALEX field names.

---

## 12. Kill / revisit conditions

The implementation remains narrow. Revisit or remove it if a future review proves:

- Gate-2 itself can express the same pairwise direct-effect-zero condition without ambiguity;
- the wrapper begins owning selector semantics rather than consuming attributable testimony;
- interest-guided discovery is treated as evidence invalidation;
- a future rectangle merely rephrases pairwise failures already named by current evaluators.

Do not promote policy-indexed equivalence or adaptive topology unless an executable missing contract appears.

---

## 13. Explicit non-claims

Passing these specimens does **not** prove:

- that an interest receipt is true merely because it was recorded;
- that inferred interest accurately represents a person's internal state;
- that consumed interest was sufficient or dominant in causing a later result;
- that a selected evidence set is statistically representative;
- that all personalization channels have been captured;
- that no timing, omission, ranking, latency, or tool-choice side channel exists;
- that support equals truth;
- that local supportability equals global support;
- that a causal receipt grants authority;
- that observer equivalence is absolute rather than boundary-relative.

---

## 14. Promotion ladder

Completed for `MEDIATED-SUPPORT-001`:

```text
written spec
implementation plan
RED hostile fixtures
minimal comparison wrapper
semantic-inflation hostile control
lawful-mediation + selection-provenance pressure
identity / ancestry hardening
full regression
```

Still gated:

```text
COUNTERFACTUAL-RECTANGLE-001
LEEP onto a materially different domain
policy-equivalence / adaptive-topology candidates
```

No kernel promotion follows automatically from this one green specimen family.

---

## 15. Compression

The implemented law is:

> **Interest may causally change the evidence world an actor reaches. That can lawfully change support through the evidence. But if the evidence is held fixed, interest must have zero direct effect on support.**

The still-held rectangle hypothesis is:

> **A hidden variable may leak not only by changing an output directly, but by changing how the system responds to another otherwise-lawful input. Pairwise invariance may therefore be insufficient—but the residual interaction class still has to earn implementation.**

Working seals:

> **WHY WE LOOKED MAY CHANGE WHAT WE FOUND. IT MAY NOT CHANGE WHAT THE FOUND EVIDENCE MEANS BY ITSELF.**

> **CHANGE ONE RELATION AND WATCH WHAT MOVES. CHANGE TWO ONLY AFTER THE FIRST TESTS LEAVE SOMETHING REAL UNEXPLAINED.**
