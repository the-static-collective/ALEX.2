# Mediated Support × Counterfactual Rectangle — ALEX Frontier Design

**Date:** 2026-08-28  
**Status:** approved direction; written-spec review pending; no runtime conformance claimed  
**Owning world:** `the-static-collective/ALEX.2`  
**Primary executable pressure target:** `MEDIATED-SUPPORT-001`  
**Reusable relational harness:** `COUNTERFACTUAL-RECTANGLE-001`  
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

The next executable frontier should therefore not duplicate either one.

The new target is narrower:

```text
MEDIATED-SUPPORT-001
```

It asks whether an interest/selection signal may lawfully affect eventual support **only by changing the evidence basis that ALEX actually evaluates**, while remaining forbidden from directly increasing or decreasing semantic support when that evidence basis is held fixed.

The second artifact is not a new ontology primitive. It is a reusable hostile harness:

```text
COUNTERFACTUAL-RECTANGLE-001
```

which crosses two controlled differences and checks whether their interaction reveals a hidden dependency that neither one-dimensional pair exposes alone.

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

This equation is a research model, not the planned runtime representation. ALEX currently evaluates receipted digests and typed cases rather than estimating causal coefficients.

The executable question is therefore qualitative and exact:

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

`MEDIATED-SUPPORT-001` must distinguish four things that ordinary provenance often collapses:

```text
interest_claims
selection_basis
observed/evaluated evidence
support derivation
```

The evaluator should answer:

1. Did an attributable selector actually consume the interest receipt?
2. Did that consumption change the bounded context or evidence basis?
3. If support changed, can the difference be attributed to changed evidence?
4. If evidence is held fixed, does interest still alter support?

The final question is the hostile core.

### 3.2 Required case family

#### Case A — inert interest

```text
W0: no interest receipt for q
W1: interest receipt i for q
selector ignores i
```

Expected:

```text
bounded_context(W0) == bounded_context(W1)
evidence_basis(W0) == evidence_basis(W1)
support(W0) == support(W1)
```

The interest difference remains causally inert for this run.

#### Case B — lawful mediated divergence

```text
W0: no interest receipt for q
W1: interest receipt i for q
policy P explicitly consumes i
```

and:

```text
READ(i, P)
    -> different bounded context
    -> different genuine evidence basis
```

Expected:

```text
support MAY differ
```

but the support receipt must peel through:

```text
support result
  -> evaluated evidence
  -> changed bounded context
  -> selector consumption occurrence
  -> interest receipt + selector policy
```

The receipt chain records why the evidence field changed without treating that history as evidence for the claim.

#### Case C — direct-effect hostile control

Provide two runs with:

```text
different interest ancestry
same bounded context
same evaluated evidence basis
same evaluator conditions
```

Expected:

```text
support_left == support_right
```

Any support divergence is:

```text
REFUSE: INTEREST_AS_SUPPORT
```

This is the exact runtime analogue of requiring the direct coefficient `gamma` to be zero.

#### Case D — stripped formation ancestry

Give two runs the same final evidence set, but remove the selection/consumption ancestry from one.

For an object-local claim whose evidence is sufficient:

```text
support may remain identical
```

because formation provenance does not invalidate genuine object evidence.

For a population/generalization claim that depends on sampling conditions:

```text
formation ancestry may condition whether the inference is testable
```

The first implementation should **not** attempt a general statistical-sampling engine. It should preserve the distinction and refuse to infer population validity merely from matching final evidence sets.

Recommended initial disposition for such a generalization case:

```text
INSUFFICIENT_TO_TEST: SELECTION_FORMATION_REQUIRED
```

#### Case E — semantic inflation despite valid mediation

Even if interest lawfully changed the evidence set, an evaluator that adds independent support weight because the actor was interested must fail.

Expected:

```text
REFUSE: INTEREST_AS_SUPPORT
```

Lawful indirect effect does not legalize a direct semantic edge.

---

## 4. Ownership and boundary order

The implementation must preserve the current stack split.

### LOADOUT-compatible boundary

Owns or witnesses:

```text
which bounded context was compiled
which selector policy participated
which attributable input/receipt was actually consumed
```

ALEX must not invent LOADOUT selection semantics.

### 3rdi boundary

Owns or witnesses:

```text
what became available to the observer
projection identity / digest
cut / decoder / observer-local constraints where applicable
```

ALEX must not duplicate the 3rdi projection kernel.

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

`PROJECTION-BREAK-001` now proves a useful sibling contract:

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

Therefore `MEDIATED-SUPPORT-001` should not reimplement future-break detection.

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

## 6. `COUNTERFACTUAL-RECTANGLE-001`

### 6.1 Purpose

Pairwise tests can miss interactions.

Construct a four-run family over two controlled binary coordinates:

```text
                 interest / selector state
                 I0                 I1

world W0       F(W0,I0)          F(W0,I1)
world W1       F(W1,I0)          F(W1,I1)
```

The first practical coordinate pair should be:

```text
W := hidden-world difference that should remain outside the observer-local basis
I := interest/selection difference
```

At each declared boundary, compare:

```text
world delta
interest delta
mixed interaction
```

### 6.2 Algebraic research model

For a binary response surface:

```text
F(w,i) = a + b*w + c*i + d*w*i
```

then:

```text
world effect at i=0 = b
world effect at i=1 = b + d
mixed finite difference = d
```

A hidden-world invariance requirement therefore fails if either:

```text
b != 0
```

or:

```text
d != 0
```

The second case is important: hidden state may fail to leak by itself yet still alter how the system reacts to a selector or interest signal.

Again, the runtime should not require numeric subtraction over digests. The algebra only defines the pattern we are looking for.

### 6.3 Operational digest harness

For each boundary `B`, define an equality indicator:

```text
EQ_B(run_x, run_y)
```

The harness evaluates the rectangle's equality pattern.

A hostile interaction exists when, for example:

```text
W0/I0 == W1/I0 at B
```

but after an interest/selection state is introduced:

```text
W0/I1 != W1/I1 at B
```

and no declared world-sensitive selector or release explains the difference.

This is not ordinary direct hidden leakage. It is a **conditional leak / interaction leak**.

Recommended reason code:

```text
HIDDEN_SELECTION_INTERACTION
```

The harness must report the earliest boundary where the conditional divergence appears.

### 6.4 Composition requirement

`COUNTERFACTUAL-RECTANGLE-001` should compose existing evaluators rather than become a parallel epistemic engine.

Preferred architecture:

```text
pair checks
  -> PROJECTION-INVARIANCE-001 where invariance is required
  -> PROJECTION-BREAK-001 where a shared intervention is declared
  -> MEDIATED-SUPPORT-001 where derivation/support effects are under pressure
  -> rectangle coordinator reports interaction pattern
```

The rectangle owns orchestration and comparison, not projection semantics or support semantics.

---

## 7. Policy-indexed equivalence — research hold

The combined frontier suggests a useful mathematical description:

```text
W1 ≡_(observer, policy, cut, decoder) W2
```

Two worlds may be equivalent for one observer/policy boundary and distinguishable for another.

A lawful reveal, decoder change, or selector consumption may refine the observer's partition of possible worlds without changing the worlds themselves.

This is useful explanatory language for 3rdi and future visualization work, but it is **not** an implementation target in this spec.

HOLD:

```text
POLICY-EQUIVALENCE-001
PARTITION-REFINEMENT-001
```

Do not add either to the kernel until the mediation and rectangle specimens demonstrate a concrete missing contract.

---

## 8. Adaptive epistemic topology — research hold

The AFTERMATHALS and access-engineering slices add a further frontier:

```text
observation history
  -> selection state
  -> reachability topology
  -> next observation possibilities
```

If consuming a receipt changes which relations are reachable next, two runs may have the same rendered surface while carrying different lawful futures.

Candidate state model:

```text
X_t = (surface_t, formation_digest_t)
```

where the formation digest is only promoted into necessary runtime state if deleting it makes future reachability ambiguous or unreplayable.

This remains outside the first implementation.

HOLD:

```text
ADAPTIVE-EPISTEMIC-TOPOLOGY-001
```

The existing `PROJECTION-BREAK-001` should be used as the hostile neighbor before any new topology primitive is considered.

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

Possible classifications:

```text
FORBIDDEN_LEAK
DECLARED_RELEASE
LAWFUL_MEDIATION
ORDINARY_DOWNSTREAM_CONSEQUENCE
INSUFFICIENT_TO_TEST
```

`DELTA-PEEL` is a method name only. It does not introduce a new ALEX relation or runtime object.

---

## 10. First neutral hostile vector

The implementation plan should freeze one compact deterministic fixture family before runtime changes.

Suggested world:

```text
100 bounded objects
10 have property P
```

Two claims:

```text
C_local:
object x has property P

C_population:
P is common in the underlying world
```

Three selection paths:

```text
BROAD
selection independent of P

INTEREST_GUIDED
selector consumes an attributable interest receipt and preferentially exposes likely-P objects

STRIPPED
receives the same final object set as INTEREST_GUIDED but without sufficient selection-formation ancestry
```

Required behavior:

```text
C_local:
genuine object evidence is not weakened merely because interest guided discovery

C_population:
selection formation materially conditions the inference
```

The first runtime target should remain deterministic and synthetic. It does not need to prove a complete statistical sampling model.

Add the direct hostile pair:

```text
same evidence set
same claim
same evaluator
interest differs
```

Expected:

```text
same support result
```

Then add the rectangle hostile case:

```text
hidden world difference alone does not alter the projection
interest state alone follows declared behavior
combined hidden-world + interest state causes an undeclared boundary divergence
```

Expected:

```text
REFUSE at earliest boundary
reason: HIDDEN_SELECTION_INTERACTION
```

---

## 11. Required result identity

To remain attributable and comparable across runs, the future evaluator/harness should preserve at least:

```text
case_id
claim_id
projection_digest
compile/context identity where supplied
evidence_basis_digest
selection/consumption receipt refs where supplied
evaluator identity or rule profile
support disposition/result digest
first divergent boundary where applicable
receipt survivors
reason code
```

Exact field names belong to the implementation plan after existing runtime contracts are inspected.

Do not force LOADOUT or 3rdi to adopt ALEX field names merely to satisfy this harness.

---

## 12. Kill conditions

### Kill or narrow `MEDIATED-SUPPORT-001` if:

- existing Gate-2 support provenance already proves the direct-effect-zero condition without ambiguity;
- no hostile fixture can distinguish valid mediation from ordinary evidence-basis change;
- the proposed evaluator would require ALEX to own LOADOUT selection semantics;
- the design accidentally weakens valid evidence merely because interest influenced discovery.

### Kill or narrow `COUNTERFACTUAL-RECTANGLE-001` if:

- it is only a verbose wrapper around existing pairwise evaluators and finds no interaction class they cannot already name;
- interaction detection requires invented semantics rather than declared boundary equivalence;
- it duplicates `PROJECTION-BREAK-001` instead of composing it;
- the four-run fixture cannot identify a materially different failure mode from ordinary hidden leakage.

### Do not promote policy-indexed equivalence or adaptive topology if:

- they remain explanatory metaphors with no executable missing contract;
- they require a shared cross-repo ontology;
- they import authority from projection or retrieval history.

---

## 13. Explicit non-claims

Passing these specimens would **not** prove:

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

The approved sequence is:

```text
1. written spec review
2. implementation plan for MEDIATED-SUPPORT-001
3. RED hostile fixture family
4. minimal ALEX evaluator / composition
5. full regression
6. COUNTERFACTUAL-RECTANGLE-001 coordinator only if pairwise tests leave the interaction gap real
7. LEEP onto a materially different domain
8. only then revisit policy-equivalence / adaptive-topology candidates
```

The first materially different LEEP candidate should be one of:

```text
Novelist reveal / foreshadowing
Free Graph neutral-vs-interest-guided traversal
RAG/personalization retrieval
Derek-style same-surface / different-reachability world state
```

No kernel promotion follows automatically from one green specimen.

---

## 15. Compression

The frontier now has a sharper law than `interest != evidence`:

> **Interest may causally change the evidence world an actor reaches. That can lawfully change support through the evidence. But if the evidence is held fixed, interest must have zero direct effect on support.**

And the rectangle adds the second law:

> **A hidden variable may leak not only by changing an output directly, but by changing how the system responds to another otherwise-lawful input. Pairwise invariance is therefore sometimes insufficient; the interaction itself must be tested.**

Working seals:

> **WHY WE LOOKED MAY CHANGE WHAT WE FOUND. IT MAY NOT CHANGE WHAT THE FOUND EVIDENCE MEANS BY ITSELF.**

> **CHANGE ONE RELATION AND WATCH WHAT MOVES. CHANGE TWO AND WATCH WHETHER THE SECOND ONE REVEALS A DEPENDENCE THE FIRST COULD NOT SEE.**
