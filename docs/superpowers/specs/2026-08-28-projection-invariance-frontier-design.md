# Projection Invariance Frontier — ALEX × 3rdi × LOADOUT × Novelist

**Date:** 2026-08-28  
**Status:** approved direction; written-spec review pending; no runtime conformance claimed  
**Owning world:** `the-static-collective/ALEX.2`  
**Primary executable pressure target:** `PROJECTION-INVARIANCE-001`  
**Projection contract owner:** `the-static-collective/3rdi`  
**Context constitution:** LOADOUT-compatible, without importing authority  
**Narrative consumer:** Novelist-compatible, without granting evidentiary authority  
**Architectural ancestors:** `WHEN IS A PARTIAL ORDER`, `RELATION-DERIVATION-001`, `KNOWABILITY-CONE-001`, `BOOKROOM-001`, 3rdi phase-0 projection floor

> **THE WORLD MAY BE ONE. THE VIEW IS LOCAL. THE INTERPRETATION HAS FORMATION. THE NARRATIVE IS A PROJECTION. NONE MAY SILENTLY REWRITE THE FIELD.**

## 0. Decision

The next frontier will not be promoted as a master ontology.

Instead, ALEX will preserve and pressure-test four distinct transformations that are already independently present across the Collective:

```text
WORLD / FORMATION FIELD
        |
        | LOADOUT-compatible constitution
        v
BOUNDED WORLD
        |
        | 3rdi observer-local projection
        v
LOCAL PROJECTION
        |
        | ALEX derivation / relation minting / refusal
        v
INTERPRETATION FIELD
        |
        | Novelist-compatible viewpoint / reveal / serialization
        v
NARRATIVE / ENCOUNTER
```

The first executable target is deliberately narrower than the whole chain:

```text
PROJECTION-INVARIANCE-001
```

It asks whether two materially different worlds that are identical inside an observer's declared lawful projection produce equivalent observer-local receipts and derivations.

The frontier remains a family of crucibles and receipts before it becomes any shared primitive.

---

## 1. Constitutional non-collapse laws

Existing ALEX and 3rdi boundaries remain authoritative.

This design adds no right to collapse:

```text
world occurrence != observer exposure
observer exposure != supplied context
supplied context != attention
attention != interest
interest != evidence
available premise != actually derived premise
semantic derivation != external admission
causal order != serialization order
surface-equivalent interpretation != formation-equivalent interpretation
relation truth != relation discovery
relation discovery != relation assertion
relation assertion != model admission
narrative order != formation order
```

Hard law:

> **No projection operation may silently acquire authority from the field it projects.**

ALEX may evaluate support. 3rdi may compile a view. LOADOUT may constitute a bounded run world. Novelist may organize reader-facing information. None of these actions independently determines historical truth, canon, publication, execution authority, or owning-world consequence.

---

## 2. Formation is provisionally a field, not a diary

The current partial-order work establishes that an attributable formation history need not be one chain.

At minimum, the frontier must preserve:

```text
E       attributable occurrences
<       causal precedence / dependency
||      causal concurrency / unorderedness
```

But ALEX and neighboring systems also preserve things that a realized DAG alone cannot naturally express:

```text
refused possibility
incompatible branch
latent reachability
unresolved crossing
```

Therefore this design records a stronger **candidate research model**:

```text
F = (E, prec, conflict, enables)
```

where:

- `E` is a set of attributable occurrences;
- `prec` records supported causal precedence;
- `conflict` records mutually incompatible realizations where the owner can justify that claim;
- `enables` records conditions under which an event or crossing becomes reachable.

This is inspired by event-structure-style semantics but is **not** promoted as an ALEX or eCODE primitive.

For now:

```text
FORMATION-DAG
```

means the realized causal contribution projection of a richer possible field.

```text
NARRATED-FORMATION
```

means one chosen serialization or traversal of that formation projection.

Hard law:

```text
narrated first != causally first
```

---

## 3. Cut calculus: one word currently hides several controls

`BOOKROOM-001` already introduces a source-relative textual cut. 3rdi independently binds projection to observer-local receiver constitution. Together they require the following distinctions to remain explicit:

```text
SOURCE CUT
which carrier regions are permitted to be consulted

CONTEXT CUT
which material is actually supplied to this run

HISTORICAL / EPISTEMIC CUT
which information could lawfully have reached this receiver through attributable channels by this point

ATTENTION CUT
which available material was actually encountered / selected / noticed when that fact is witnessed

DERIVATION CUT
which declared basis and rule were actually used to form a result
```

These may coincide. They may also diverge.

A source cut may justify only a source-availability claim unless stronger receiver-state controls are evidenced.

For example:

```text
chapter <= 5 supplied
```

does not prove:

```text
receiver had no chapter-12 knowledge
```

Likewise:

```text
fact available to receiver
```

does not prove:

```text
fact noticed or used in derivation
```

No universal `CUT` object is introduced by this design. The immediate requirement is only that crucibles name which cut they are asserting.

---

## 4. Projection as a receipted transformation

For this frontier, observer-local projection is represented conceptually as:

```text
P = project(W, cut, observer, receiver, decoder, channels)
```

where:

- `W` is the fixed world / occurrence field supplied to the projection owner;
- `cut` identifies the bounded temporal/source constraints in force;
- `observer` identifies the local viewpoint;
- `receiver` identifies the receiving constitution where material receiver differences matter;
- `decoder` identifies the declared interpretation/projection mechanism where required;
- `channels` records attributable information paths relevant to the epistemic claim.

3rdi remains the owner of its concrete phase-0 projection contract. ALEX must not duplicate or silently fork that kernel.

ALEX may consume a 3rdi receipt or a compatible projection witness as basis for a separate derivation test.

Hard law:

```text
projection receipt != evidence support
```

The projection receipt answers what was exposed and how. ALEX separately answers what relations are supportable from that basis.

---

## 5. Formation-sensitive interpretation identity

The same prose may arise through materially different formation conditions.

A research interpretation therefore cannot be fully identified by its surface text alone.

Candidate descriptive tuple:

```text
J = {
  surface,
  declared_basis,
  source_cut,
  context_cut,
  observer_cut,
  receiver,
  decoder,
  derivation_rule,
  formed_at,
  formation_refs
}
```

This is a receipt shape, not a required persistent schema.

The crucial invariant is:

```text
surface(J1) == surface(J2)
```

does not imply:

```text
formation(J1) == formation(J2)
```

This distinction is required for:

- clean prospective prediction vs hindsight-contaminated prediction;
- independent rediscovery vs copied assertion;
- source-bounded interpretation vs latent prior familiarity;
- recurrence vs attributable continuation;
- identical answer under distinct evidence paths.

`BOOKCUT-LEAK-001` is an immediate consumer of this law.

---

## 6. Relation birth requires four separate clocks

The current edge-birth research is useful but must not imply that a world relation begins when ALEX notices it.

For any candidate relation `R(A,B)`, preserve the distinction among:

```text
WORLD-RELATION BIRTH
when the relation became true in the represented world, if knowable

DISCOVERY BIRTH
when an observer first encountered evidence or a candidate for the relation

ASSERTION BIRTH
when an attributable actor first proposed the relation

MODEL-EDGE BIRTH
when a bounded research model admitted / recorded the edge
```

These times may all differ.

Example:

```text
A caused B in 1997
observer discovers evidence in 2026
researcher proposes CAUSES(A,B) in 2026
evaluator admits SUPPORTS(evidence, claim) later in 2026
```

The 2026 model event does not manufacture the 1997 causal fact.

Hard law:

```text
model bookkeeping != ontology
```

This distinction should pressure `EDGE-BIRTH-001` before any global relation-birth schema is promoted.

---

## 7. Aperture provenance: why loaded is not why believed

LOADOUT-compatible context constitution may be influenced by task relevance, explicit user request, dependency, recency, random exploration, or interest.

The frontier therefore records a candidate **aperture-selection receipt** answering:

> Why did this material enter this bounded run world?

Candidate reasons may include:

```text
explicit-request
direct-dependency
causal-dependency
neighbor-traversal
random-exploration
interest
recency
manual-pin
```

This receipt is selection provenance only.

Hard law:

```text
WHY INCLUDED != WHY SUPPORTED
```

This prevents a dangerous feedback loop:

```text
interest in X
    -> load more X
    -> encounter X more often
    -> treat recurrence as support
    -> load still more X
```

Interest may explain traversal. It may not become evidence for the traversed claim.

No persistent psychological profile is required. Declared, witnessed, inferred, and unknown interest remain distinct evidence classes where interest provenance is recorded.

---

## 8. Narrative information flow

Novelist-compatible narrative work introduces another observer-local projection problem.

At minimum, narrative systems must preserve:

```text
WORLD TRUTH
what is established in the story world / source canon

AUTHOR STATE
what the writing system or author-side process knows

VIEWPOINT STATE
what the current viewpoint character can know

READER EXPOSURE
what has actually appeared in publishable prose

READER INFERENCE
what the exposed material supports a reader inferring
```

These are separate information states.

A future secret may lawfully influence earlier prose only through an attributable narrative transform such as foreshadowing.

Conceptual lawful path:

```text
SECRET S
    |
    | declared clue / foreshadow transform
    v
CLUE C
    |
    | reader exposure
    v
HYPOTHESIS H
```

This differs from an undeclared spoiler leak:

```text
SECRET S ----------> early prose
```

Therefore narrative noninterference is **controlled**, not absolute: hidden author-state may affect reader-facing material through explicitly intended transforms, but not by accidental contamination that gives the reader unsupported future knowledge.

ALEX may evaluate whether an inference is supportable from reader-visible material. Novelist owns story-flow semantics. Neither acquires authority over the other's source-of-truth layer.

---

## 9. `PROJECTION-INVARIANCE-001`

### 9.1 Core specimen

Construct two materially different immutable worlds:

```text
W_A != W_B
```

but define one observer constitution `O` such that the lawful observer-local projection is equivalent:

```text
project_O(W_A) == project_O(W_B)
```

The difference between the worlds must exist strictly outside the observer's declared aperture / cut.

Then run the same deterministic projection and bounded ALEX derivation.

Required:

```text
observer_receipt(W_A) == observer_receipt(W_B)
```

and, where deterministic derivation is declared:

```text
derivation(W_A) == derivation(W_B)
```

modulo explicitly declared nondeterminism.

If a result changes because of hidden world state outside the lawful projection, the specimen fails.

### 9.2 Failure classes

At minimum distinguish:

```text
LOADOUT LEAK
hidden world state changed what entered the bounded run

PROJECTION LEAK
3rdi-visible output changed because of hidden state

DERIVATION LEAK
ALEX result changed because an unavailable premise influenced reasoning

SERIALIZATION LEAK
a UI / narrative ordering exposed or implied hidden precedence

NARRATIVE LEAK
future / author-only knowledge contaminated reader-facing material outside a declared reveal transform
```

### 9.3 Positive-control exception

For a narrative fixture, create a declared foreshadow transform available in both worlds.

A hidden future fact may alter the visible clue **only** when the clue transform is part of the declared world/story construction being tested. The receipt must expose that dependency.

The test therefore distinguishes:

```text
AUTHORIZED INFORMATION TRANSFORM
```

from:

```text
UNDECLARED INFORMATION LEAK
```

### 9.4 No-authority control

Passing `PROJECTION-INVARIANCE-001` grants no truth, canon, publication, or execution authority.

It demonstrates only that the bounded projection/derivation respected the declared noninterference boundary for that specimen.

---

## 10. Companion hostile specimens

This frontier recommends, but does not yet implement, the following family:

```text
BOOKCUT-LEAK-001
same source cut; clean receiver vs previously contaminated receiver

BOOKCUT-NONINTERFERENCE-001
same visible prefix; different withheld suffixes

EDGE-BIRTH-001
fixed endpoints; separately receipted relation discovery/assertion/admission

SERIALIZATION-001
same partial order; two lawful linearizations + one illegal causality-inventing serialization

FORMATION-DAG-001
one real multi-source artifact; several lawful narrated walks over one attributable formation DAG

APERTURE-FEEDBACK-001
interest affects retrieval frequency but must not inflate evidence weight or independent-corroboration counts

NARRATIVE-FORESHADOW-001
declared clue transform passes; undeclared spoiler path fails
```

Each fixture must state which owner is under test. A failure in one organ must not be mislabeled as another organ's failure.

---

## 11. Ownership boundaries

### ALEX owns

- research-claim formation receipts;
- relation-derivation evaluation;
- distinction between basis, support, evaluator disposition, and external admission;
- historical/epistemic crucible semantics when ALEX makes the claim;
- `PROJECTION-INVARIANCE-001` as a cross-organ adversarial research specimen.

### 3rdi owns

- concrete observer-local projection semantics;
- receiver / decoder / exposure receipts inside its declared contract;
- deterministic phase-0 projection behavior;
- its own projection noninterference tests.

### LOADOUT-compatible constitution owns

- what context/capabilities are made available to a bounded run;
- omissions, freshness, compression, and selection provenance where supplied;
- no evidentiary or external authority.

### Novelist-compatible narrative systems own

- viewpoint, reader exposure, narrative sequencing, clue/reveal transforms, and story-flow organization;
- no ALEX evidence authority.

### Owning project / human gate retains

- canon;
- publication;
- merge/admission;
- execution consequence;
- external authority.

No new cross-repository master runtime is introduced.

---

## 12. Promotion discipline

This design intentionally promotes **one executable question**, not six primitives.

Promoted to implementation-planning candidate after written-spec review:

```text
PROJECTION-INVARIANCE-001
```

Held as research candidates:

```text
formation event-structure semantics
universal cut calculus
interpretation identity schema
relation-birth schema
aperture-selection schema
narrative information-flow schema
```

Promotion criteria for any held candidate:

1. at least two materially different owner-world specimens require the distinction;
2. the candidate survives hostile null controls;
3. it remains useful without importing owner-specific authority;
4. it does not collapse existing ALEX or 3rdi invariants;
5. a smaller local receipt cannot solve the same problem more cleanly.

---

## 13. Acceptance criteria for the first executable descendant

`PROJECTION-INVARIANCE-001` is ready to claim local conformance only when:

- two worlds are materially different outside the declared projection;
- observer-local visible input is equivalent by construction;
- receipts prove the relevant source/context/observer constraints;
- the deterministic projection result is equivalent;
- the bounded ALEX derivation result is equivalent when deterministic derivation is part of the fixture;
- one hostile hidden-state leak is detected;
- one legal declared transform is preserved as a positive control;
- no external authority changes as a consequence of passing;
- failure reporting names the actual leaking boundary;
- prior failed receipts remain preserved rather than rewritten.

---

## 14. Compression

```text
OBJECTS OCCUR.
RELATIONS ARE MINTED.
OBSERVERS STAND SOMEWHERE.
CONTEXT IS AN APERTURE.
INTERPRETATIONS HAVE FORMATION.
NARRATIVES SERIALIZE.
NONE OF THOSE OPERATIONS GETS TO REWRITE THE FIELD.
```

And the executable frontier law:

> **If two worlds are indistinguishable inside a declared lawful projection, hidden differences outside that projection must not change the observer-local result unless an attributable transform explicitly permits them to.**
