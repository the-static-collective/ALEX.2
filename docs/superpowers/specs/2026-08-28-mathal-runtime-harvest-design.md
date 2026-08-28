# Mathal Runtime Harvest — LOADOUT × 3rdi × ALEX

**Date:** 2026-08-28  
**Status:** approved direction; written-spec review pending; no runtime conformance claimed  
**Owning design world:** `the-static-collective/ALEX.2`  
**Projection contract owner:** `the-static-collective/3rdi`  
**Context constitution:** LOADOUT-compatible, without importing authority  
**Primary implementation slice:** `PROJECTION-INVARIANCE-001` + PEEL/LEEP formation replay  
**Experimental membrane:** adaptive topology/world-mechanic labs only after receipt invariants are proved

> **THE WORLD MAY CHANGE. THE GRAPH MAY CHANGE. THE VIEW REMAINS LOCAL. EVERY CHANGE MUST LEAVE AN ATTRIBUTABLE ROAD BACKWARD.**

## 0. Decision

The recent mathal work contains several executable ideas worth lowering into runtime tests and scripts. They will not be promoted as a shared ontology or a universal graph kernel.

The selected architecture is **hostile-lab first**:

```text
WORLD / FORMATION FIELD
        |
        | LOADOUT-compatible bounded constitution
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
```

Mathal-derived behavior enters this chain as small receipted transformations, deterministic helpers, and hostile specimens owned by the organ whose semantics they exercise.

The first implementation slice is deliberately narrow:

```text
PROJECTION-INVARIANCE-001
        +
PEEL / LEEP formation replay
```

The graph-rewriting/world-mechanic work remains quarantined behind an experimental membrane until the receipt and replay invariants survive hostile tests.

---

## 1. Why now

The current floor already contains enough executable structure to support this work without inventing a new platform:

- 3rdi already compiles deterministic observer-local projections, preserves receiver-dependent decoding, and runs hostile labs;
- ALEX already has a blind Crucible boundary, derivation adapter/profile, and LOADOUT handshake runtime;
- the projection-invariance frontier has already selected hidden-state invariance as the next executable question;
- the typed-occurrence-field research has already separated causal past, formation basis, semantic support, interest, observer projection, and serialization;
- the Daily Slice mathal harvest has already isolated executable candidates around PEEL/LEEP, decoder ladders, key-in-edge topology changes, ternary/adaptive state, ribbon topology, and Frobenius-style open/transfer/gather analogues.

The missing move is not another concept layer. It is to make a few of those distinctions fail loudly when code cheats.

---

## 2. Constitutional non-collapse laws

This design inherits all existing ALEX, 3rdi, and LOADOUT boundaries and adds no right to collapse them.

```text
world state != projected state
projected state != evidentiary support
loaded context != evidence
interest != attention
attention != support
support != authority
same surface != same formation
same projection != same world
same content != same occurrence
relation truth != relation discovery
relation discovery != relation assertion
relation assertion != semantic admission
semantic admission != external consequence
receiver != decoder
carrier != decoder
projection != source
replay != original occurrence
```

Hard laws:

```text
NO RELATION SILENTLY MINTS ANOTHER RELATION.
NO HIDDEN STATE MAY ALTER A DECLARED PROJECTION WITHOUT AN ATTRIBUTABLE PATH.
NO REPLAY MAY IMPERSONATE THE ORIGINAL OCCURRENCE.
NO DECODER MAY RETROACTIVELY REWRITE A PRIOR RECEIPT.
NO EXPERIMENTAL TOPOLOGY OPERATOR MAY ACQUIRE OWNING-WORLD AUTHORITY.
```

---

## 3. Ownership model

No new cross-repository authority layer is introduced.

### LOADOUT-compatible responsibility

LOADOUT compiles bounded means:

- selected context;
- capability surface;
- omissions and cold references;
- freshness / source-cut information;
- reasons material was loaded when available;
- immutable compile identity;
- recompile requirements.

LOADOUT does not determine semantic support, truth, canon, or consequence.

### 3rdi responsibility

3rdi owns observer-local projection semantics:

- occurrence / availability / focus / relevance separation;
- receiver constitution;
- decoder identity;
- lawful cut;
- channel visibility;
- projection receipt;
- deterministic projection equivalence helpers needed by its own contract.

3rdi does not determine evidence support or owning-world consequence.

### ALEX responsibility

ALEX owns research derivation pressure:

- formation trace;
- declared basis;
- semantic relation minting / refusal;
- blind Crucible evaluation;
- formation-sensitive comparison;
- hostile tests against hindsight leakage and premise smuggling.

ALEX does not gain authority merely because it can replay or explain a derivation.

### Owning-world responsibility

Any mutation, canonization, publication, execution, or project-local consequence remains outside this cross-stack design and must be admitted by the owning world.

---

## 4. Minimal cross-stack receipt envelope

The systems may share a **small structural envelope** for experiments. “Shared” here means shape-level convenience for testing and translation, not semantic interoperability, common persistence, or common authority. This is not a universal ontology and must remain semantically sparse.

Candidate descriptive shape:

```json
{
  "event_id": "e42",
  "operator": "EXPERIMENT_STEP",
  "operator_version": "1",
  "pre_state": null,
  "inputs": [],
  "basis_refs": [],
  "edge_receipts": [],
  "decoder_ref": null,
  "projection_scope": null,
  "post_state": null,
  "authority": "none"
}
```

Required principles:

1. `event_id` identifies the occurrence, not merely its payload.
2. `operator` identifies the transformation class actually executed.
3. `pre_state` and `post_state` bind stateful transformations when applicable and remain null when no state transition is claimed.
4. `basis_refs` are descriptive pointers only; each owner decides what they mean locally.
5. `edge_receipts` may record relation changes but do not imply semantic support.
6. `decoder_ref` is present only where decoding matters.
7. `projection_scope` is present only where a declared projection matters.
8. `authority` defaults to `none` for these experiments and may not be silently widened by consumers.

A project may wrap, extend, or translate this shape locally. No project is required to persist it verbatim, and matching field names do not imply matching semantics unless an explicit owner-level adapter says so.

---

## 5. Runtime family A — `PROJECTION-INVARIANCE-001`

### Question

If two worlds differ only outside an observer's declared lawful projection, must their observer-local receipts and deterministic downstream derivations remain equivalent?

```text
WORLD A --\
           > same declared projection -> RECEIPT A
WORLD B --/                          -> RECEIPT B

assert projection_equivalent(A, B)
```

### Invariant

For declared projection `P`:

```text
P(W1) == P(W2)
```

whenever the differences between `W1` and `W2` are outside `P` and no declared channel/decoder transform makes those differences visible.

This does **not** assert:

```text
W1 == W2
formation(W1) == formation(W2)
all downstream narratives are identical
all owning-world consequences are identical
```

### Candidate implementation ownership

3rdi:

```text
projection equivalence helper
hidden-state perturbation specimens
deterministic receipt normalization for comparison
```

ALEX:

```text
PROJECTION-INVARIANCE Crucible profile
positive sibling: hidden state changes, lawful projection unchanged
negative sibling: hidden state becomes reachable through declared transform
metamorphic siblings: fresh IDs, ordering noise, unrelated hidden distractors
```

### Failure conditions

Fail if:

- hidden out-of-scope data changes a receipt;
- a hidden identifier leaks through ordering, hashing, serialization, or iteration behavior;
- ALEX derives a relation using material not present in the declared projection basis;
- equivalence comparison erases a material difference that the projection contract declares visible.

---

## 6. Runtime family B — PEEL / LEEP

PEEL and LEEP are formation-accounting operations, not identity operators.

### PEEL

```text
PEEL(result)
    -> minimal attributable formation packet sufficient to explain/replay the tested result
```

A PEEL packet may contain:

```text
occurrence refs
explicit dependency / carrier edges
projection receipt refs
decoder version
rule/profile digest
declared basis
cut identifiers
ordered steps only where order was materially claimed
residual unknown / fog
```

PEEL must not silently convert transitive ancestry, attention traces, or mere temporal adjacency into support.

### LEEP

```text
LEEP(peel_packet)
    -> execute declared replay path in a fresh occurrence context
    -> emit replay receipt
```

LEEP is not resurrection. It creates a new occurrence whose formation is attributable to the PEEL packet.

### Four independent comparisons

A replay harness should be able to ask separately:

```text
surface_equal(original, replay)
projection_equal(original, replay)
derivation_equal(original, replay)
formation_equivalent(original, replay)
```

No one predicate implies the others.

### Minimum hostile specimens

1. **Counterfeit same** — same surface output, different undeclared basis.
2. **Order noise** — independent/concurrent events serialized differently but formation relation unchanged.
3. **Missing carrier** — replay tries to jump across an unreceipted dependency.
4. **Attention masquerade** — breadcrumb/attention ancestry offered as semantic support.
5. **Decoder drift** — replay uses a different decoder version without declaring it.
6. **Unknown preservation** — original PEEL contains unresolved fog; replay must not fill it by invention.

### Suggested first implementation shape

ALEX should initially own PEEL/LEEP as a Crucible-facing formation-replay helper because ALEX already owns formation trace and derivation rules. 3rdi receipts enter as immutable basis references; 3rdi projection logic must not be reimplemented inside PEEL.

---

## 7. Runtime family C — `DECODER-LADDER-001`

The useful engineering claim extracted from the decoder-ladder mathal is versioned self-revision with explicit ancestry.

```text
decoder_0
   |
   | decode
   v
projection_0
   |
   | receipt / observed error or limitation
   v
recalibration event
   |
   v
decoder_1
```

Required ancestry:

```text
decoder_1.parent = decoder_0
decoder_1.basis_refs includes attributable recalibration basis
```

Hard law:

```text
decoder_1 must not alter projection_0 or its receipt
```

A later decoder may produce a new projection over the same carrier, but that is a new occurrence with a new decoder reference.

### Hostile discriminator

Construct a case where later information makes a richer decoder possible. Re-run the historical cut.

The historical receipt must remain identical unless the test explicitly asks for a new counterfactual projection using the later decoder.

This distinguishes:

```text
historical projection
from
later reinterpretation of historical material
```

---

## 8. Runtime family D — `EDGE-BIRTH-001`

A single relation may have multiple attributable birthdays.

Candidate descriptive coordinates:

```text
world_birth
availability_birth
discovery_birth
assertion_birth
model_birth
admission_birth
```

These are not mandatory fields on every edge. They are an executable pressure vocabulary for preventing one timestamp from impersonating all relation history.

Example:

```text
world relation exists        1902
carrier becomes available    1984
researcher notices relation  2026
model proposes edge          2026
ALEX admits SUPPORTS         2026
```

Hostile tests must reject:

- backdating a model edge to world birth;
- treating discovery date as causal origin;
- treating availability as attention;
- treating admission as proof the relation was historically known.

3rdi owns visibility/relevance coordinates; ALEX owns semantic derivation/admission coordinates.

---

## 9. Runtime family E — `INTEREST-ENVELOPE-001`

Interest is a context/provenance relation, not a truth weight.

Required non-collapse:

```text
WHY LOADED
!= WHY INTERESTING
!= WHY ATTENDED
!= WHY SUPPORTED
```

Candidate envelope fragment:

```json
{
  "interest": {
    "actor_ref": "observer:lumi",
    "occurrence_ref": "e42",
    "basis": ["unexpected topology similarity"]
  }
}
```

Rules:

- interest may help LOADOUT decide what context to include;
- interest may be recorded as an attributable occurrence-local relation;
- interest does not increase evidence weight;
- interest does not imply attention unless attention is separately witnessed;
- interest must not become a permanent inferred personality/profile fact;
- ALEX must refuse any semantic rule that treats interest alone as support.

---

## 10. Experimental membrane — graph-changing world mechanics

The following runtime families are explicitly **experimental**. They must not be imported into ALEX or 3rdi constitutional kernels merely because the mathematics is elegant.

The experimental world state is modeled minimally as:

```text
W = (S, G)
```

where:

- `S` is local state;
- `G` is the currently constituted relation topology.

A transformation may change either or both:

```text
Delta_e : W^- -> W^+
```

This permits a bounded class of experiments in which an occurrence changes the topology that governs later reachability.

### 10.1 `KEY-IN-EDGE-001`

Canonical experimental rewrite:

```text
A ----- B

becomes

A -- K -- B
```

The key is not merely attached as metadata. The operator explicitly replaces one edge with two attributable edges.

Receipt requirements:

```text
operator = INSERT_IN_EDGE
pre_state digest
target edge identity
inserted occurrence identity
removed edge receipt
created edge receipts
post_state digest
optional topology invariants
```

The operator must refuse if the target edge is missing, ambiguous, already replaced in the current state, or not within the declared experimental scope.

### 10.2 `ADAPTIVE-S-001`

A state transition may lawfully change subsequent reachability:

```text
event e changes G
therefore reachable_after(e) may differ from reachable_before(e)
```

This is the strongest executable survivor from the adaptive-network mathal.

It must preserve:

```text
history changed the graph
!=
history was rewritten
```

Every topology mutation therefore requires pre/post digests and explicit edge deltas.

### 10.3 OPEN / TRANSFER / GATHER lab

Use the structural analogy only:

```text
OPEN       1 -> 2
TRANSFER   1 -> 1
GATHER     2 -> 1
```

These are typed experimental topology operators, not universal verbs.

Each owning specimen must declare:

- input ports;
- output ports;
- what state/carriers survive;
- what relations are removed/created;
- whether the operation is reversible;
- terminal receipt.

No Frobenius/cobordism interpretation is required for conformance. That mathematics is research ancestry, not runtime authority.

### 10.4 Ribbon / mirror topology lab

The ribbon/fatgraph work may become a visual/research lab in which cyclic ordering around nodes is part of state.

The same adjacency with different local cyclic order must be allowed to produce different thickened topology receipts.

This lab is useful for testing:

```text
same adjacency != same embedding / thickening
```

It remains outside the first implementation plan.

---

## 11. Data flow for the first implementation slice

```text
1. LOADOUT-compatible compile
   emits bounded context + compile receipt

2. 3rdi projection
   consumes bounded world/cut/receiver/decoder
   emits deterministic projection receipt

3. ALEX derivation
   consumes only declared projection/basis
   emits semantic disposition + formation trace

4. PEEL
   extracts the attributable formation packet for the tested result

5. LEEP
   replays the packet in a fresh occurrence context

6. comparison harness
   independently compares surface, projection, derivation, and formation

7. Crucible
   evaluates positive, negative, and metamorphic siblings
```

At no step does a successful comparison admit external consequence.

---

## 12. Determinism and canonical comparison

Projection and replay tests require deterministic comparison without mistaking incidental serialization for semantics.

Each owner should define its own comparison normalizer.

Allowed normalization examples:

- stable ordering of unordered receipt members;
- exclusion of fresh occurrence IDs where the test explicitly declares identity-insensitive equivalence;
- stable serialization of dictionaries/maps;
- comparison of declared semantic fields rather than raw stdout formatting.

Forbidden normalization examples:

- dropping decoder/version identity when it is material;
- erasing declared cut differences;
- ignoring a changed relation merely because final prose is unchanged;
- replacing unknown/fog with empty values;
- sorting an order-sensitive formation sequence and thereby destroying the claimed relation.

Every equivalence profile must state what is and is not normalized.

---

## 13. Error and refusal behavior

These runtimes should prefer typed refusal over guessed completion.

Candidate reason classes:

```text
MISSING_BASIS
UNDECLARED_DEPENDENCY
PROJECTION_LEAK
DECODER_MISMATCH
CUT_MISMATCH
FORMATION_GAP
AMBIGUOUS_EDGE
STALE_PRE_STATE
REPLAY_DIVERGENCE
FORBIDDEN_RELATION_MINT
UNKNOWN_NOT_PRESERVED
EXPERIMENTAL_SCOPE_REQUIRED
```

A refusal is itself receipted.

Errors must not be auto-repaired by widening context, swapping decoders, re-running on newer state, or importing hidden data unless that repair is a separately declared new occurrence.

---

## 14. Testing strategy

### Layer 1 — unit invariants

Pure tests for:

- receipt normalization;
- projection equivalence;
- PEEL packet validation;
- LEEP fresh-occurrence behavior;
- decoder ancestry validation;
- edge-birth non-collapse;
- interest/support separation.

### Layer 2 — blind Crucible profiles

Use the existing CASE/ORACLE separation.

The runtime adapter receives CASE only. ORACLE expectations remain harness-side.

Every family should have:

- one positive specimen;
- one negative specimen;
- one metamorphic positive sibling;
- one metamorphic negative sibling.

### Layer 3 — cross-organ integration specimen

One fixed specimen should pass through:

```text
LOADOUT-compatible compile
-> 3rdi projection
-> ALEX derivation
-> PEEL
-> LEEP
-> comparison
```

The test asserts only the declared receipt invariants, not a general cross-stack conformance claim.

### Layer 4 — experimental topology labs

Experimental graph rewriting uses separate profiles and cannot make the stable profile fail merely because a speculative operator changes.

---

## 15. File-shape guidance

Exact file paths remain implementation-plan decisions, but the intended locality is:

### ALEX

```text
tools/run_projection_invariance_profile.py
alex_runtime/formation_replay.py
crucible/specimens/projection-invariance-001/
crucible/specimens/formation-replay-001/
```

### 3rdi

```text
skills/3rdi/scripts/... projection equivalence helper
specimens/... hidden-state perturbation cases
tests/... deterministic invariance tests
```

### Experimental membrane

Prefer a clearly non-kernel lab location. Do not place `KEY-IN-EDGE`, `ADAPTIVE-S`, ribbon topology, or OPEN/TRANSFER/GATHER operators in a production namespace before they earn promotion through independent specimens.

---

## 16. Build sequence

### Gate M1 — projection invariance

Implement `PROJECTION-INVARIANCE-001` against the existing 3rdi projection contract and ALEX Crucible boundary.

Success:

- hidden out-of-scope differences do not perturb projection receipts;
- declared newly-visible differences do perturb them;
- ALEX derivation uses only declared projected basis;
- metamorphic siblings pass.

### Gate M2 — PEEL

Extract a minimal attributable formation packet from one tested ALEX derivation path.

Success:

- no relation is invented during extraction;
- unknown/fog survives;
- packet binds rule/profile and decoder/projection refs where applicable.

### Gate M3 — LEEP

Replay the packet as a fresh occurrence and compare four independent equality classes.

Success:

- replay cannot impersonate original occurrence;
- missing dependencies refuse;
- same surface with different formation remains distinguishable.

### Gate M4 — decoder ladder + edge birth

Add historical-cut pressure for decoder versioning and relation birthdays.

### Gate M5 — interest envelope

Prove `why loaded != why supported` through one real compile/derivation specimen.

### Experimental Gate X1 — key in edge

Only after M1-M3 are stable, build the first topology-rewrite lab with pre/post state digests and edge-delta receipts.

No later experimental gate is implied by X1 passing.

---

## 17. Success criteria

This design succeeds if the stack can demonstrate all of the following without introducing a master ontology:

1. hidden state cannot perturb a lawful observer projection unless a declared path exposes it;
2. a consequential derivation can PEEL backward to attributable formation inputs;
3. that formation can LEEP forward into a fresh replay without impersonating the original occurrence;
4. same surface, same projection, same derivation, and same formation remain independently testable claims;
5. later decoder improvement cannot back-edit historical projection receipts;
6. relation birth coordinates cannot silently collapse into one timestamp;
7. interest can influence context selection without becoming evidence;
8. experimental state transitions can rewrite graph topology while preserving explicit pre/post ancestry;
9. none of the above silently transfers authority or owning-world consequence.

---

## 18. Explicit non-goals

This design does not authorize:

- a universal event algebra;
- a universal cut calculus;
- a shared graph database;
- vector-clock infrastructure;
- a master ALEX/3rdi/LOADOUT schema;
- automatic project admission;
- ontology synchronization across repositories;
- metaphysical claims about consciousness, causality, symbols, or topology;
- production use of the 107/108-Y, ribbon, Frobenius, or adaptive-network models;
- replacing project-local receipt formats that already work.

---

## 19. Residual fog

Questions intentionally held for implementation evidence:

- How minimal can a PEEL packet become before LEEP loses lawful replayability?
- Which equivalence fields belong to 3rdi's projection contract versus ALEX's test harness?
- Should formation equivalence compare exact edges, typed edge classes, or a project-local relation profile?
- When a decoder changes only performance but not semantic output, what ancestry remains materially required?
- Is `EDGE-BIRTH-001` best implemented as a standalone profile or folded into existing temporal/formation Crucibles?
- Can the sparse cross-stack receipt envelope stay useful without becoming a de facto ontology?
- Where should the experimental topology lab ultimately live if it develops beyond a specimen?
- Which topology invariants, if any, are worth storing versus recomputing from the pre/post graph state?

These remain fog until code or specimens force a narrower answer.

---

## 20. Implementation boundary

This document approves architecture only.

The next step after human review is a separate implementation plan for:

```text
Gate M1 — PROJECTION-INVARIANCE-001
Gate M2 — PEEL
Gate M3 — LEEP
```

The plan must not include experimental topology operators unless the human explicitly expands scope after the stable receipt/replay gates are proved.

> **FIRST PROVE THAT THE VIEW CANNOT CHEAT. THEN PROVE THAT FORMATION CAN BE PEELED AND REPLAYED. ONLY THEN LET THE WORLD REWRITE ITS GRAPH.**
