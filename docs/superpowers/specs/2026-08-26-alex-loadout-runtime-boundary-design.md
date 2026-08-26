# ALEX × LOADOUT Runtime Boundary — Constitutional Runtime Amendment v0

**Date:** 2026-08-26  
**Status:** approved architecture; written amendment awaiting human review; no runtime conformance claimed  
**Owning world:** `the-static-collective/ALEX.2`  
**Applies to:** Alexandria Floor, ALEX constitutional hardening, ALEX DESK, `@alex`, future ALEX runtime work, and the bounded ALEX ↔ LOADOUT handshake

> **LOADOUT compiles the means. ALEX accounts for meaning. Neither admits consequence.**

The more exact constitutional form is:

> **LOADOUT compiles a bounded world-cut and the means available within it. ALEX accounts for encounters, transformations, assertions, and lawful derivations. Authority may be carried but is never manufactured. Consequence is admitted only by the owning world.**

This amendment does not merge LOADOUT and ALEX into one ontology. It establishes the smallest protocol by which they may work together without either silently inheriting the other's jurisdiction.

---

## 1. Why this amendment exists

The current ALEX floor already has the correct substrate:

- immutable/content-addressed source custody;
- exact source-to-claim ancestry;
- plural readings and transformations;
- typed evidence paths;
- rebuildable projections;
- explicit refusal;
- `PRESSURE` and `{ PEEL. SLEEP .LEEP }` as bounded research methods;
- a portable Crucible contract whose fixture self-tests do **not** claim runtime conformance.

The next implementation step introduces new failure pressure that the original floor intentionally deferred:

1. a real runtime needs a bounded execution context;
2. the agent needs more than a tool list — it needs an attributable context cut;
3. runtime evaluation needs to distinguish relation semantics from execution and admission;
4. a useful Desk must be able to originate proposals without becoming a source of evidence;
5. replay must not impersonate a changed external world;
6. the current Crucible process boundary exposes each fixture's `expected` oracle to the adapter and therefore cannot yet be called a blind conformance test.

The runtime must solve those problems without becoming a general eCODE operating system.

---

## 2. Selected architecture

The selected shape is:

```text
MORTAL LOADOUT SHELL
  compiles this run's bounded world
        │
        │  alex.run-envelope/v0
        ▼
INDEPENDENT ALEX RESEARCH KERNEL
  preserves encounters and tests meaning
        │
        │  alex.run-receipt/v0
        ▼
OWNING-WORLD GATE
  decides what consequence becomes real

BLIND CRUCIBLE
  remains outside the production runtime
```

The systems share protocol, not identity.

### Non-collapse laws

```text
LOADOUT != ALEX
ALEX != owning-world gate
Crucible != ALEX
Crucible pass != truth
Crucible pass != admission
context selection != evidence
capability availability != authority
carried authority != minted authority
relation proposal != relation conclusion
ACCEPT != ADMITTED
ERRORED != REFUSE
same payload != same occurrence
reacquisition != exact replay
projection gesture != source mutation
```

---

# 3. Jurisdictions

## 3.1 LOADOUT owns mortal session constitution

LOADOUT owns the compile that determines what this run can presently see and attempt.

It may:

- freeze the task's initial semantic state;
- cut a bounded task world;
- compile a bounded context pack;
- expose cold references and omitted doors;
- declare compression and selection loss;
- discover and bind available capabilities;
- carry attributable effect authorization from external owners;
- intersect that authorization with local policy and current availability;
- enforce compile expiry and decay;
- identify capability gaps;
- request a child recompile when the frozen world materially changes;
- audit what the compile actually made available.

LOADOUT does **not**:

- establish historical facts;
- evaluate evidentiary support;
- mint project authority;
- enlarge a received permission;
- admit publication, deployment, messaging, mutation, canon, or other consequence;
- become ALEX's durable evidence store.

Its constitutional profile is:

```text
authority minted: none
promotion: none
durability: mortal compile + attributable receipt
```

### LOADOUT authority law

> **Knowledge may load. Capability may bind. Authority does not silently expand.**

LOADOUT may carry authority testimony. It does not author that testimony.

---

## 3.2 ALEX owns research accounting and semantic derivation

ALEX owns:

- acquisitions and exact source witnesses;
- transformations and plural readings;
- assertions and typed semantic relation proposals;
- evidence paths and dependency families;
- discovery trace and evidence path;
- attributable transformation trace where the research operation actually transforms representation;
- versioned constitutional evaluation;
- research run execution trace, suspension, and replay;
- receipts, contradictions, refusal residue, and residual fog;
- rebuildable research projections.

ALEX may discover, inspect, compare, propose, evaluate, preserve, and return receipts.

ALEX does **not**:

- issue historical canon;
- manufacture source authority;
- authenticate a human merely because an actor identifier arrived;
- make a Human Witness encounter legally or project-authoritatively binding;
- issue a Corpus OS Action Warrant;
- admit project canon, publication, deployment, messaging, deletion, or irreversible external consequence;
- become the universal relation engine for every Static Collective project.

---

## 3.3 The owning-world gate owns consequence

The relevant owning world decides what a receipt changes outside ALEX.

Examples include:

- project canon or architectural adoption;
- publication;
- deployment;
- messaging;
- mutation or deletion;
- execution under an authority-bearing runtime;
- human acceptance of an interpretation for a stated purpose;
- merger of a repository change.

ALEX may return an `admission_request_ref` or receive later gate testimony. It does not perform the constitutive act itself.

This is intentionally compatible with existing project boundaries such as Corpus OS admission/warrant semantics and Human Witness encounter evidence. ALEX imports attributable testimony from those owners when relevant; it does not duplicate their authority models.

---

## 3.4 The Crucible owns no production authority

The Crucible is an external pressure harness.

It may demonstrate that an exact runtime build survived an exact conformance profile.

It cannot:

- make the research true;
- admit an architectural change;
- establish future conformance for changed rules or runtime versions;
- substitute fixture success for source evidence.

---

# 4. The shared boundary is a run envelope, not a merged ontology

LOADOUT lowers a mortal compile into a bounded ALEX request:

```text
load_in_state
  -> task_world_cut
  -> context_pack
  -> capability_bindings
  -> effective_effect_fence
  -> alex.run-envelope/v0
```

## 4.1 Run envelope

```yaml
schema: alex.run-envelope/v0
run_id:
compile_id:
compile_digest:
compile_trace_ref:
phase:
expires_at:
question:
task_shape: FIND | READ | COMPARE | TRACE | DOSSIER | AUDIT | PRESSURE
world_cut_ref:
context_pack_ref:
input_record_ids: []
capability_bindings: []
effect_fence_ref:
egress_policy_ref:
rule_profile:
stop_condition:
requested_outputs: []
```

The envelope carries exact handles and bounded material. It does not copy the entire ambient conversation or every reachable source into ALEX.

---

# 5. LOADOUT compiles context, not merely tools

The runtime should optimize for relevance, resolution, recoverability, and declared loss rather than raw context volume.

```yaml
schema: loadout.context-pack/v0
load_bearing:
  - mission
  - invariants
  - owner_heads
  - accepted_constraints
  - stop_condition
working_set:
  - exact excerpts or record handles needed now
cold_refs:
  - resolvable sources available on demand
omitted_doors:
  - deliberately unloaded but nearby material
compression_receipts:
  - source_ref
    method
    preserved_invariants: []
    declared_loss: []
    freshness:
budget:
  tokens:
  adapter_calls:
freshness:
residual_fog: []
```

A context pack is not evidence. It is an attributable transformation of a larger reachable world into this run's bounded room.

---

# 6. Compile Trace — the narrow runtime admission of Transformation Trace

The August 26 ALEX PATH research slice proposed a third formation ledger:

```text
DISCOVERY TRACE
EVIDENCE PATH
TRANSFORMATION TRACE
```

That slice remains research with `promotion: NONE`. This amendment does **not** promote `PATH` into the public task-shape contract or promote every PATH proposal into runtime constitution.

It admits one narrow consequence because the runtime cannot truthfully replay its own context without it:

> **A LOADOUT compile that selects, compresses, omits, normalizes, or otherwise transforms context MUST preserve an attributable compile trace.**

Minimum compile transformation occurrence:

```text
source world / representation
  -> selection or compression operation
  -> output context representation
  -> preserved invariants
  -> declared omissions / losses
  -> changed role tags when material
  -> actor/tool/version
  -> freshness / acquisition cut
  -> evidence for the transformation
```

This permits ALEX to PEEL how the room was constructed without promoting the room-construction process into support for any claim discovered inside it.

Hard distinction:

```text
context caused attention != context supplied evidence
```

---

# 7. Effect fence — authority may only narrow

A bare list such as `authorized_effects: [read, write]` is insufficient. It hides source, scope, expiry, revocation, and the distinction between availability and authority.

Each consequential effect must resolve to attributable testimony:

```yaml
effect:
status: allowed | refused | unresolved
authorization_source_ref:
scope:
valid_from:
expires_at:
revocation_ref:
owner_gate_ref:
```

The effective fence for one compile is the intersection:

```text
effective_effect
  = requested_effect
    ∩ currently_available_capability
    ∩ externally_authorized_effect
    ∩ local_policy_allowance
```

No union-like rule is permitted.

### Non-escalation invariant

For every effective effect `e`:

```text
e ∈ effective_effects
  => e ∈ externally_authorized_effects
```

A recompile may reduce or replace the effective fence. It may enlarge the fence only when a new attributable external authorization independently earns that enlargement.

---

# 8. Recompile, never ambient patch

A mortal compile is immutable after issuance.

The public tool surface therefore uses:

```text
loadout.compile
loadout.recompile
loadout.audit
```

Do not expose a mutation-semantic `loadout.patch` in v0.

A recompile creates a child:

```text
compile C0
  -> material change / expiry / capability gap
  -> close or suspend dependent run
  -> compile C1 derived from C0
```

Context references may descend where still valid. Permissions do not ambiently inherit.

Every child compile recomputes its effective effect fence from current authority testimony.

Hard law:

> **Context may descend. Permission must be re-earned from the current cut.**

---

# 9. Predicate-minting boundary

ALEX must not route every relation through one universal semantic evaluator.

Relation records belong to at least three minting classes.

## 9.1 Mechanical / witnessed occurrence relations

Examples:

```text
caused_by
input_of
output_of
derived_from
exact_transform_of
targets
acquired_from
```

These may be appended by the operation that actually witnessed the occurrence, provided the operation preserves the required receipt and ancestry.

They are not semantic conclusions merely because they are edges.

## 9.2 Semantic relation proposals and conclusions

Examples:

```text
SUPPORTS
CONTRADICTS
CONTEXTUALIZES
RESEMBLES
MOTIVATED_BY
DOCUMENTED_INFLUENCE
SHARED_PRECURSOR
```

These enter through:

```text
proposal
  -> versioned scoped evaluator
  -> ACCEPT | REFUSE | UNRESOLVED | INSUFFICIENT_TO_TEST
  -> optional conclusion assertion
  -> evaluation receipt
```

No global pairwise conversion table exists.

## 9.3 Authority / admission / consequence relations

Examples include project adoption, legal or administrative authority, executable warrant, publication admission, merge/admission, or constitution of external state.

ALEX never mints these.

It may store an attributable imported testimony produced by the owning system.

This prevents the Derivation Kernel from becoming a universal relation authority.

---

# 10. Semantic derivation is partial and proof-carrying

Remove the idea of relation conversion.

Do not implement:

```text
CAUSES_ATTENTION -> SUPPORTS
PRESERVES -> AUTHORIZES
RESEMBLES -> DESCENDS_FROM
```

Those are not transformations of one true edge into another.

Instead evaluate a versioned sequent:

```text
premises + bridge witnesses + declared scope + rule version
  |- proposed conclusion relation
```

Semantically:

```text
derive(rule, context, premises, bridge_witnesses) ⇀ conclusion
```

The function is partial. Undefined is the default.

Graph reachability remains free. Semantic derivability does not.

## 10.1 Proof-carrying relation proposal

```yaml
relation_proposal:
  id:
  subject_id:
  predicate:
  object_id:
  scope:
  proposed_by:
  proposed_at:
  basis_ids: []

evaluation:
  proposal_id:
  rule_id:
  rule_version:
  ruleset_digest:
  input_ids: []
  input_digest:
  execution_step_id:
  disposition: ACCEPT | REFUSE | UNRESOLVED | INSUFFICIENT_TO_TEST
  reason_code:
  required_survivors: []
  conclusion_assertion_id:
  residual_fog: []
```

`ACCEPT` means only:

> The declared evaluator completed and the proposal satisfied the declared rule for the declared scope, so ALEX may append the scoped conclusion assertion and its evaluation receipt.

It does not mean universal truth, source authority, permission, canon, external admission, or consequence.

Source relations remain unchanged. Later status is a projection over attributable evaluation occurrences rather than a mutable field on the original proposal.

---

# 11. Four orthogonal axes

Do not encode these in one status enum.

| Axis | Question | Examples |
| --- | --- | --- |
| **Semantic relation** | What is being asserted? | `SUPPORTS`, `CONTRADICTS`, `RESEMBLES` |
| **Evaluation disposition** | What did this declared evaluator decide? | `ACCEPT`, `REFUSE`, `UNRESOLVED`, `INSUFFICIENT_TO_TEST` |
| **Execution state** | What happened to the executable step? | `PLANNED`, `READY`, `RUNNING`, `FINISHED`, `SUSPENDED`, `ERRORED`, `CANCELLED` |
| **Admission state** | What did the external owning gate do? | `PENDING`, `ADMITTED`, `REFUSED`, `DEFERRED`, `NOT_REQUIRED` |

Hard rules:

```text
evaluation disposition exists only if its evaluator finished
REFUSE != execution failure
ERRORED != evidentiary refusal
SUSPENDED != unresolved unless an evaluator separately said so
ACCEPT != ADMITTED
NOT_REACHED carries no evaluator disposition
```

`NOT_REACHED` is a derived closure fact, not an evaluator result and not a normal live execution state.

It may be emitted only after a run/branch is closed or a dependency path is conclusively cut.

---

# 12. Blind Crucible v1 is the first executable gate

The current Crucible contract is valuable and the current fixture corpus remains preserved.

The current process boundary, however, sends the complete specimen object to the adapter while `expected` lives in that same object. Therefore the adapter receives the answer key.

Runtime conformance may not be claimed through that boundary.

## 12.1 CASE / ORACLE split

```text
CASE — sent to runtime
  case_id
  operation_type
  rule_profile
  given
  attempt
  nonce
  input_digest

ORACLE — harness only
  case_id
  expected_disposition
  expected_reason_code
  required_survivors
  forbidden_outputs
  metamorphic_family
```

The runtime never receives the ORACLE.

## 12.2 Runtime result

```yaml
case_id:
input_digest:
ruleset_digest:
disposition:
reason_code:
receipt_survivors: []
derived_assertions: []
execution_trace_summary:
```

The harness rejects:

- mismatched input digest;
- stale rule profile;
- unexpected output;
- missing required residue;
- forbidden promotion;
- malformed execution summary.

## 12.3 Metamorphic siblings

The contract uses **metamorphic siblings**, not a promise of permanent secret fixtures.

A conformance family must be able to vary surface form while preserving or deliberately flipping the semantic law:

- rename record and specimen IDs;
- reorder irrelevant arrays;
- add unrelated distractor relations;
- vary non-load-bearing wording;
- generate a positive sibling and negative sibling;
- use a fresh nonce;
- omit public fixture titles from runtime input.

A runtime that switches on fixture IDs or echoes expected output must fail these siblings.

## 12.4 Scoped conformance profiles

Never claim plain `ALEX conformant`.

Initial profiles:

```text
alex.runtime/derivation-m0
alex.runtime/one-book-m1
alex.runtime/formation-trace-m2
```

Each profile pins:

- operation types;
- fixture family versions;
- ruleset digest;
- runtime adapter version;
- excluded/not-yet-implemented families.

A passing profile testifies only to the exact tested runtime build and profile.

---

# 13. First derivation family

The first runtime conformance family is:

> **`RELATION-DERIVATION-001 — attention does not inherit support`**

This family should reuse the constitutional law already preserved by the merged `attention-trace-support-independence` specimen rather than rewriting history or pretending a prior `EDGE-CONVERSION-001` exists on main.

## 13.1 Negative sibling

Given:

```text
B1 --CAUSES_ATTENTION--> Q1
Q1 --FOUND--> E1
E1 is relevant to candidate claim C1
no evidence path makes B1 support C1
```

Attempt:

```text
derive B1 --SUPPORTS--> C1
```

Required result:

```text
execution: FINISHED
evaluation: REFUSE
reason: ATTENTION_NOT_SUPPORT
survivors: B1, Q1, E1, attempted proposal, refusal receipt
forbidden: B1 --SUPPORTS--> C1
downstream append step: NOT_REACHED at closure
```

## 13.2 Positive sibling

Add an attributable evidence path from `E1` to `C1` and attempt:

```text
derive E1 --SUPPORTS--> C1
```

Required result:

```text
execution: FINISHED
evaluation: ACCEPT for declared scope
append: conclusion assertion + evaluation receipt
admission: still PENDING or NOT_REQUIRED
```

## 13.3 Metamorphic pressure

Run both siblings with renamed IDs, reordered inputs, a fresh nonce, and an unrelated distractor relation.

The semantic outcome must remain invariant.

---

# 14. Occurrence identity is not content identity

Content addressing identifies bytes. It does not identify historical occurrence.

Two events may produce or encounter identical bytes while remaining distinct because they differ in:

- acquisition source;
- producer;
- run;
- compile;
- causal ancestry;
- observation time;
- effective time;
- transformation history.

Every occurrence therefore requires an opaque occurrence identity plus content digest where relevant.

Minimum occurrence spine:

```text
id
kind
run_id
compile_id
payload_ref
payload_digest?
producer
recorded_at
observed_at?
effective_at?
caused_by
input_digest
ruleset_digest?
idempotency_key?
```

Hard rule:

> **same payload != same occurrence**

---

# 15. Runtime components

The first runtime remains a small modular monolith.

## A. LOADOUT shell

Compiles world cut, context pack, capability bindings, effective effect fence, expiry, and compile trace.

## B. Command port

Accepts typed commands with idempotency keys and an exact run envelope.

It refuses:

- expired compiles;
- malformed envelopes;
- effect requests outside the effective fence;
- direct projection writes;
- stale ruleset profiles where exact replay/conformance requires the old one.

## C. Occurrence ledger

Append-oriented records for commands, acquisitions, transformations, proposals, evaluations, step transitions, suspensions, replays, egress, and imported gate testimony.

## D. Witness store

Preserves the existing ALEX source stack:

```text
work
  -> carrier
  -> acquisition
  -> canvas / exact visual surface
  -> region
  -> reading
  -> normalization
  -> translation
  -> assertion
  -> evidence path
```

Large/binary payloads remain in content-addressed filesystem custody. SQLite stores metadata, ancestry, and references.

## E. Derivation Kernel / Bridge Gate

Runs versioned scoped semantic evaluators.

It may append evaluation receipts and earned conclusion assertions.

It cannot admit external consequence.

## F. Run engine

A deliberately small DAG executor with:

- preconditions and dependency reachability;
- idempotent commands;
- explicit suspension/wake conditions;
- `ERRORED` distinct from `REFUSE`;
- `NOT_REACHED` derived at closure;
- no distributed-workflow ambition in v0.

## G. Receipt Press

Pins inputs, rules, runtime versions, compile identity, survivors, losses, failures, egress, replay conditions, and fog.

## H. Projection Builder + Proposal Port

Projection queries rebuild Desk, search, narrative, graph, dependency, and formation lenses.

They have no direct write authority over source or semantic relation records.

A Desk action becomes:

```text
Desk gesture
  -> proposal command
  -> command port
  -> witnessed operation OR semantic evaluation
  -> new occurrence
  -> rebuilt projection
```

> **The Desk may ask. The Desk may not mint.**

## I. Blind Crucible harness

Runs outside the runtime and retains the ORACLE.

It tests through the same public command contract used by real callers.

---

# 16. Replay, SLEEP, and changing worlds

## 16.1 Pure replay

A deterministic evaluation may claim exact replay only when all material dependencies are pinned:

- input record digests;
- compile identity or exact admitted replay substitute;
- ruleset digest;
- evaluator version;
- runtime version;
- relevant configuration;
- random seeds;
- declared environment dependencies.

## 16.2 External encounters

Search results, archive responses, model calls, mutable URLs, and remote APIs are historical encounters.

ALEX may:

1. replay recorded response bytes/testimony;
2. reacquire from the external world as a **new acquisition**;
3. compare the new acquisition with the old and preserve the delta.

Option 2 is never exact replay of option 1.

## 16.3 Counterfactual `.LEEP`

Counterfactual `.LEEP` is pure by default.

It may replay decisions and transformations against frozen evidence or declared effect stubs.

It cannot silently:

- republish;
- redeploy;
- resend;
- delete;
- mutate an external owner;
- repeat an irreversible side effect.

## 16.4 SLEEP custody

A suspended evaluation preserves:

```text
live formulations (1–3)
unequal support
contradictions
unknowns
wake conditions
expiry / abandonment condition
owner of next discriminator
```

Waking after compile expiry requires a child compile and current rule/effect evaluation. The old compile is historical evidence of what was previously available, not ambient authority for the resumed run.

---

# 17. First executable implementation floor

The first ALEX runtime implementation is now selected as:

- **Python 3.12** modular monolith;
- **SQLite** with foreign keys, WAL, and explicit transactions;
- **SQLite FTS5** for exact/phrase search;
- **content-addressed filesystem storage** for held bytes;
- **JSON Schema** for public contracts;
- **deterministic CLI/JSON process boundary first**;
- **local MCP adapter after the CLI contract is proven**.

This is an ALEX v0 choice, not an eCODE-wide production-language decision.

Do not add in v0:

- graph database;
- distributed queue;
- generic workflow framework;
- dynamic policy DSL;
- web UI;
- universal ontology;
- universal relation-composition algebra.

### Append-oriented enforcement

The implementation must enforce append orientation rather than merely describe it:

- immutable source and occurrence tables reject update/delete in normal runtime paths;
- corrections append descendants;
- mutable state is limited to disposable projections, locks, and caches;
- commands use idempotency keys;
- occurrence append and required projection checkpoint changes share an explicit transaction boundary;
- schema migrations preserve historical payloads, rule IDs, and version identifiers.

---

# 18. Agent-facing tool surface

After the deterministic CLI proves the commands, a local adapter may expose:

```text
loadout.compile
loadout.recompile
loadout.audit

alex.run
alex.open
alex.trace
alex.resume
alex.receipt
alex.project
alex.propose
```

Default responses should be context-efficient:

- compact findings;
- exact handles;
- omitted doors;
- residual fog;
- next discriminators;
- lazily loadable witness handles.

The tool surface is an adapter over the kernel. It is not the kernel and does not acquire authority by being convenient.

---

# 19. Build gates

## Gate 0 — architectural amendment

Admit this document and no runtime implementation.

**Proof:** public project semantics clearly separate LOADOUT, ALEX, Crucible, and owning-world admission; the first executable target is narrow enough to plan independently.

## Gate 1 — Blind Crucible v1

- split CASE from ORACLE;
- stop sending `expected` to adapters;
- add input/ruleset digests;
- add metamorphic sibling generation;
- publish scoped conformance profiles;
- include explicit answer-echo and fixture-ID-switch cheating adapters.

**Proof:** both cheating adapters fail while the harness remains able to score honest results.

## Gate 2 — derivation microkernel

- append-oriented occurrence floor;
- one versioned derivation rule;
- negative and positive `RELATION-DERIVATION-001` siblings;
- refusal residue;
- downstream closure truth;
- replay from pinned inputs.

**Proof:** `alex.runtime/derivation-m0` passes blindly.

## Gate 3 — LOADOUT handshake

- validate immutable run envelopes and compile digests;
- preserve compile trace;
- carry attributable effect fences;
- refuse expired compiles;
- emit capability gaps and `recompile_required`;
- prove a child compile receives no ambient permission inheritance.

**Proof:** stale compile, owner-evidence change, permission drift, and capability-gap specimens pass.

## Gate 4 — one-book research loop

Route the existing approved vertical through the same runtime:

```text
ASK -> LOCATE -> ACQUIRE -> READ -> COMPARE -> CLAIM -> CITE -> RECEIPT
```

**Proof:** exact quote-to-page return, plural readings, correction ancestry, exact search coverage, offline replay, egress refusal, and applicable Crucible families pass on one held book.

## Gate 5 — rebuildable Desk + local agent port

- rebuild bounded Desk projections from receipts;
- route yarn/placement-originated research actions through Proposal Port;
- expose the proven deterministic commands through local MCP;
- delete and rebuild a projection.

**Proof:** projection gestures can request tests but cannot directly create evidence or authority.

---

# 20. Adversarial acceptance matrix

| Attack | Required outcome |
| --- | --- |
| Adapter receives ORACLE/`expected` | Harness design fails before any conformance claim |
| Adapter branches on public fixture ID | Metamorphic sibling catches it |
| Graph path exists without semantic bridge | Reachability preserved; derivation undefined/refused |
| Explicit bridge witness exists | Proposal becomes testable; not automatically true |
| Evaluator returns `ACCEPT` | Scoped conclusion may append; external admission unchanged |
| Upstream refusal cuts downstream evaluator | Downstream becomes `NOT_REACHED` at closure with no disposition |
| Runtime crashes inside evaluator | `ERRORED`, not `REFUSE` |
| Context pack selected a source | Selection may explain attention; it carries no support weight by selection alone |
| Compile is expired | Run refuses/suspends; no ambient permission |
| New owner evidence changes the frozen world | Parent closes/suspends; child compile required |
| Child compile has no new authority testimony | It may not inherit parent's effective permission merely by descent |
| Desk attempts direct semantic relation write | Refuse direct write; preserve proposal command |
| Desk attempts authority/admission write | Refuse as outside ALEX jurisdiction |
| Ruleset changed since receipt | Exact evaluation replay refused; new evaluation becomes descendant |
| External search changed | New acquisition + delta; no false exact replay |
| Duplicate command delivered twice | One lawful effect; idempotent return/duplicate receipt |
| Same bytes arrive through two acquisitions | Payload may deduplicate; occurrence identities remain distinct |
| Projection deleted | Rebuild from ledger/receipt without source loss |
| Pretty diagram claims conformance | Refuse; projection is not runtime evidence |

---

# 21. Explicit non-goals

Do **not** build into ALEX v0:

- a master eCODE ontology;
- a global authority service;
- Corpus OS warrant/admission semantics;
- Human Witness identity/signature/legal-validity semantics;
- a graph database;
- a universal semantic relation algebra;
- a generic distributed workflow engine;
- a dynamic policy language;
- collection-scale ingestion;
- a full visual Desk UI;
- automatic Free Graph or GitBook writes;
- a truth score;
- autonomous publication or admission;
- permanent model-memory claims;
- a requirement that every runtime operation pass every Crucible family;
- promotion of the full ALEX PATH research slice into runtime law merely because compile trace is admitted here.

The first runtime should remain one process understandable in one sitting, one inspectable database, one local content store, and one public command protocol whose receipts survive replacement of the implementation.

---

# 22. Failure conditions

Redesign if any implementation:

- lets context selection impersonate evidence;
- lets LOADOUT mint or enlarge authority;
- lets ALEX admit project consequence;
- lets the Desk directly mint semantic or authority-bearing relations;
- routes mechanical provenance relations through an unnecessary universal truth evaluator;
- lets semantic conclusions appear without a versioned rule and attributable premises;
- treats `ACCEPT` as `ADMITTED`;
- treats `ERRORED` as `REFUSE`;
- gives `NOT_REACHED` an evaluator disposition;
- mutates a compile in place;
- lets a child compile inherit permissions without current authority testimony;
- treats content digest as historical occurrence identity;
- calls a fresh external acquisition an exact replay;
- allows a conformance adapter to read the harness ORACLE;
- requires a graph database, workflow framework, or UI before the derivation microkernel can be proven;
- silently turns the ALEX/LOADOUT protocol into a shared master ontology.

---

# 23. Repository slicing after this amendment

This amendment intentionally separates design admission from implementation.

After human review of this written spec, the next implementation plan should cover only:

```text
PR A — Blind Crucible v1
PR B — derivation microkernel
PR C — LOADOUT handshake
```

The one-book runtime plan should then bind the existing OCR/PDF/search vertical to the proven kernel rather than create a parallel execution architecture.

Desk/MCP work remains after the same kernel survives the one-book loop.

---

# 24. Seal

> **LOADOUT decides what enters the room and what may be attempted there under carried authority.**
>
> **ALEX preserves what was encountered, records what changed, and tests what may be inferred.**
>
> **The Crucible tries to catch the runtime lying about those distinctions.**
>
> **The owning world decides what becomes consequential.**

Short form:

> **Compile the means. Account for meaning. Admit nothing silently.**

And the runtime's smallest truthful claim:

> **Remember exactly what was encountered. Preserve how the room and evidence were transformed. Earn every semantic promotion. Replay only what is actually replayable. Carry authority without manufacturing it.**
