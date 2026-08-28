# ALEX Gate 4 — BOOKROOM-001

**Date:** 2026-08-27  
**Status:** approved architecture specification; no implementation or runtime conformance claimed  
**Owning world:** `the-static-collective/ALEX.2`  
**Selected approach:** ALEX evidence core + Novelist-compatible Book Room projection  
**Primary architectural ancestor:** MEMENTO narrative membrane  
**Research ancestor:** `WHEN IS A PARTIAL ORDER`  
**Provisional transform notation:** `S(MEMENTO) -> BOOKROOM`

> **THE BOOK GETS A WORLD. THE RESEARCH GETS ANOTHER. ALEX KEEPS THE RECEIPTS BETWEEN THEM.**

## 0. Decision

Gate 4 will no longer be treated as only a one-book ingestion demo. The existing one-book vertical slice becomes the first executable **Book Room**.

A Book Room is a bounded research world organized around one exact acquired book/carrier. It preserves two explicitly separate models:

```text
BOOK MODEL
what the source can be shown to contain, say, organize, or expose

RESEARCH MODEL
what the researcher currently proposes, infers, tests, accepts, doubts, or leaves unresolved about it
```

Hard law:

```text
BOOK MODEL != RESEARCH MODEL
```

Corollaries:

```text
BOOK SAYS X != ALEX ASSERTS X IS TRUE
BOOK CONTAINS RELATION R != R EXISTS OUTSIDE THE BOOK
RESEARCHER INTERPRETS X AS Y != BOOK STATES Y
ROOM LEDGER != HISTORICAL TRUTH
SUMMARY != SOURCE
NOVELIST CARD != EVIDENCE
```

The Book Room is therefore not a note-taking convention layered over detached prose. It is a rebuildable cognitive projection over ALEX's provenance floor.

---

## 1. Why this architecture exists

The original Alexandria floor already has the correct evidence substrate:

```text
Intake Gate
  -> Immutable Shelf
  -> Scriptorium
  -> Witness Stack
  -> Rebuildable Indexes
  -> Evidence Desk
  -> Receipt Press
```

That architecture preserves exact acquisitions, page/canvas identity, plural readings, transformations, claims, and residual fog. What it lacks is a durable **book-scale research room** that helps a human or agent remain oriented inside a long work without flattening the work into a summary.

MEMENTO contributes the useful structural mutation. Its narrative membrane separates source, encounter, interpretation, proposal, local admission, ledger state, and narrative rendering. Its Novelist-compatible scaffold supplies bounded context packs, entity/world/thread/material organization, continuity state, and reader-knowledge tracking.

Gate 4 adopts that organizational strength without importing MEMENTO's narrative canon semantics or granting Novelist authority over evidence.

The selected architecture is therefore:

```text
ALEX WITNESS FLOOR
      |
      | lawful, rebuildable projection
      v
BOOK MODEL / BOOK ROOM
      |
      | separately receipted interpretation
      v
RESEARCH MODEL
```

---

## 2. Constitutional boundaries

The existing ALEX non-collapse laws remain in force, including:

```text
historical object != scan
scan != acquisition occurrence
scan != transcription
transcription != normalization
normalization != translation
translation != interpretation
interpretation != claim
search hit != evidence
similarity != genealogy
same payload != same occurrence
ACCEPT != ADMITTED
capability availability != authority
```

BOOKROOM-001 adds:

```text
book model != research model
book-local claim != world truth
book-local relation != cross-book relation
projection != evidence
projection order != causal order
chapter order != universal temporal order
book cut != universal world state
local motif recurrence != genealogy
cross-room resemblance != support
room identity != authority
room rebuild != historical replay
later-text availability != earlier-cut availability
```

No Book Room, Book Model, Research Model, Novelist projection, room ledger, or generated summary may issue external authority, canon, publication, merge, or owning-world consequence.

---

## 3. One room, one exact carrier for the first proof

BOOKROOM-001 begins with **one exact locally held carrier/acquisition**, not an abstract work assembled from multiple editions.

The first room binds:

```text
work_ref
carrier_ref
acquisition_ref
held byte digest
page/canvas map
rights / access / egress testimony
```

This preserves:

```text
work != edition
edition != acquisition
acquisition != reading
```

Multi-edition synthesis is deliberately deferred. Later architecture may introduce a work-level room with multiple carrier witnesses, but Gate 4 must first prove one room against one exact evidence lineage.

---

## 4. ALEX evidence floor beneath the room

The Book Room must remain peelable to ALEX source witnesses.

Conceptual floor:

```text
BOOKROOM
|
+-- work
+-- carrier / edition
+-- acquisition occurrence
+-- canvases / pages
+-- regions
+-- readings
+-- transformations
+-- source-local assertions
+-- research assertions
+-- dossiers / receipts
```

A consequential Book Model item must be able to descend toward exact source ancestry, for example:

```text
BOOK:AHAB_IS_CAPTAIN
  -> extracted_from READING:R184
  -> targets REGION:P37-R2
  -> part_of CANVAS:P37
  -> acquired_from ACQUISITION:E1
```

A Research Model claim may cite Book Model entries, exact loci, or both, but it may not treat a Book Model card as evidence merely because the card exists.

Rule:

> **The room may summarize. The receipt must still know where the page is.**

---

## 5. The Book Model

The Book Model is the current attributable model of **what this source contains or presents** at a declared carrier and textual cut.

It may organize material into Novelist-compatible research projections such as:

```text
entities/
world/
threads/
materials/
sections/
ledger/
front-room/
```

These names describe useful views, not a universal ontology.

### 5.1 Entities

May include:

- fictional characters;
- historical persons named by the book;
- institutions;
- narrators;
- named agents;
- formally introduced mathematical or conceptual actors where useful.

An entity card records how the book presents the entity. It does not establish that the represented person, event, object, or relation exists outside the source.

### 5.2 World

May include:

- places;
- systems;
- internal rules;
- conceptual spaces;
- source-local timelines;
- cosmologies or formal models asserted by the source.

For nonfiction this may model an argument's assumed world rather than a fictional setting.

### 5.3 Threads

May include:

- argument sequences;
- narrative arcs;
- unresolved source-local questions;
- recurring tensions;
- proof dependencies;
- promises or problems the book itself carries forward.

### 5.4 Materials

May include:

- motifs;
- objects;
- symbols;
- recurring terminology;
- definitions;
- equations;
- diagrams;
- notable quotations;
- textual formulae.

### 5.5 Sections

Represents the source's navigable textual structure: chapters, books, propositions, scenes, sermons, entries, or other source-native divisions.

A section order is a presentation/textual order. It does not automatically establish causal order, historical chronology, or composition history.

### 5.6 Book ledger

The Book ledger records the current attributable source-local model and its supersession history.

It is not a historical-truth ledger.

Corrections produce descendants. They do not rewrite earlier extraction occurrences into inevitability.

---

## 6. The Research Model

The Research Model is a separate sibling world owned by ALEX inquiry rather than by the book.

Conceptual shape:

```text
research/
+-- questions/
+-- hypotheses/
+-- interpretations/
+-- comparisons/
+-- decoder-runs/
+-- evidence-paths/
+-- contradictions/
+-- holdouts/
+-- pressure-runs/
+-- fog/
```

It may use existing ALEX methods including:

```text
PEEL
SLEEP
LEEP
PRESSURE
RELATION-DERIVATION-001
Blind Crucible patterns
formation-trace receipts
future Gate 3.5 relation/formation provenance
```

A Research Model assertion must preserve the distinction between:

```text
discovery path
formation basis
evidence path
semantic evaluation
external admission
```

No interpretation may silently write itself backward into the Book Model as though the source had stated it.

---

## 7. The membrane between models

The two models are connected by attributable crossings, not shared mutable truth fields.

Conceptual crossing:

```text
BOOK MODEL ITEM / EXACT LOCUS
        |
        | bears on / is used in formation of
        v
RESEARCH PROPOSAL
        |
        | independent semantic evaluation
        v
SUPPORTED | CONTRADICTED | UNRESOLVED | REFUSED
```

The crossing itself must preserve its jurisdiction.

Examples:

```text
BOOK:MOTIF_M1 caused_attention_to RESEARCH:Q17
```

does not imply:

```text
BOOK:MOTIF_M1 SUPPORTS RESEARCH:H17
```

Likewise:

```text
BOOK:CLAIM_C1 present_in_source
```

does not imply:

```text
C1 true_in_world
```

This membrane is a concrete consumer of Gate 2's relation-derivation law.

---

## 8. Book cuts: temporal blindness inside a text

BOOKROOM-001 introduces a bounded textual cut as a first-class research control.

Conceptual notation:

```text
BOOKCUT(carrier=E1, through=section_or_locus)
```

A Book Cut answers:

> What source material is lawfully available to this inquiry from this carrier at this declared textual boundary?

Example:

```text
BOOKCUT(E1, chapter <= 5)
```

A Research Model run bound to that cut may not silently use material first available in chapter 12.

This creates a local Temporal-Crucible-like pressure:

```text
EARLIER TEXT CUT
      +
VISIBLE / AVAILABLE MATERIAL
      ->
INTERPRETATION

FUTURE TEXT WITHHELD
```

Hard law:

```text
later chapter knowledge != earlier-cut knowledge
```

A Book Cut is source-relative. It is not a universal clock, a claim about composition chronology, or a claim about when a historical reader encountered the source unless separately evidenced.

This preserves the `WHEN IS A PARTIAL ORDER` correction:

```text
textual order != causal order
textual order != historical order
chosen serialization != causal precedence
```

---

## 9. Novelist compatibility boundary

The Novelist scaffold is used as a **cognitive organization and projection grammar**, not as an evidentiary authority.

Useful inherited capabilities include:

- bounded context-pack construction;
- entity/world/thread/material organization;
- continuity checking;
- source-linked state summaries;
- reader/information-state modeling;
- open-question tracking;
- chapter/section traversal support.

BOOKROOM-001 does **not** require ALEX to depend permanently on a particular Novelist plugin implementation.

The durable contract is the Book Room projection semantics and receipt ancestry. A compatible tool may later render or manipulate that projection.

Therefore:

```text
Novelist implementation != Book Room identity
Novelist projection != ALEX witness floor
projection loss != evidence loss
```

The projection must be deletable and rebuildable from ALEX-owned receipts and source-local records.

---

## 10. Front Room for each book

Every room may expose a compact entry surface analogous to MEMENTO's Front Room.

It should orient, not replace the source.

A room doorway may contain:

```text
source / carrier identity
held-page coverage
known missing or illegible regions
room map counts
active research questions
residual fog
high-value doors into entities / threads / materials / source
```

It must not present generated orientation prose as evidence.

The Front Room is a navigational projection and may be rebuilt.

---

## 11. Bounded context packs

A Book Room should support query-specific context rather than loading the whole book or whole room indiscriminately.

A context pack may prioritize:

```text
explicitly linked loci
active Book Model cards
current question
nearby source sections
relevant Research Model receipts
recent corrections
declared hard invariants
residual fog
```

It must preserve source references so any consequential inference can be peeled back to its evidence path.

Context selection explains **what was made available to this run**. It does not establish evidentiary weight.

```text
context selection != evidence
```

This makes BOOKROOM-001 a natural downstream consumer of the LOADOUT/ALEX handshake without merging LOADOUT and Book Room semantics.

---

## 12. Cross-room jurisdiction

Book Rooms remain locally sovereign as source models.

Suppose:

```text
ROOM A: Exodus
ROOM B: Ezekiel
ROOM C: 1 Enoch
```

Each may expose local Book Model items. A cross-book relation such as:

```text
A:MOTIF_X RESEMBLES B:MOTIF_Y
```

belongs to the ALEX research field, not inside either source-local Book Model unless the source itself makes that comparison.

Cross-room rules:

```text
same name != identity
same motif != genealogy
same claim != independent corroboration
quotation != agreement
chronological proximity != descent
cross-room resemblance != support
```

A future Library layer may coordinate many rooms, but Gate 4 proves only one room.

---

## 13. Formation provenance integration

The Book Room is designed to accept the emerging Gate 3.5 formation/relationship provenance layer without depending on a generalized relation ontology.

A source extraction occurrence may preserve:

```text
source locus
reading/version
method/tool/model version
book cut
available context
transformation/decoder version when applicable
confidence or status
alternative reading
residual fog
```

A Research Model assertion may additionally preserve:

```text
formation basis
discovery trace
evidence path
decoder selection
counterevidence
evaluation receipt
```

This enables the system to distinguish:

```text
THIS PASSAGE CAUSED US TO LOOK
```

from:

```text
THIS PASSAGE SUPPORTS THE CLAIM
```

without widening the production predicate vocabulary merely to mirror every research concept.

---

## 14. BOOKROOM-001 Gate 4 proof

### 14.1 Input

Use one exact locally held historical printed book of approximately 100–300 pages, including:

- one research question requiring several loci;
- at least one difficult page, region, or reading;
- a single declared carrier/acquisition identity.

The exact specimen book is an implementation-plan choice, not part of this architecture decision.

### 14.2 Observable loop

```text
ACQUIRE
  -> PAGE MAP
  -> READ
  -> BOOK MODEL
  -> NOVELIST-COMPATIBLE ROOM PROJECTION
  -> RESEARCH QUESTION
  -> BOUNDED BOOK CONTEXT
  -> RESEARCH MODEL
  -> SUPPORTED / CONTRADICTED / UNRESOLVED
  -> RECEIPT
```

### 14.3 Minimum positive witness

The proof should produce at least:

```text
1 exact Book Room

Book Model:
  >= 3 attributable entities/concepts
  >= 2 world/system/place records where applicable
  >= 3 materials/motifs/terms
  >= 2 internal threads
  >= 3 source-local claims or assertions

Research Model:
  1 supported research claim
  1 contradicted hypothesis
  1 unresolved hypothesis
```

Every consequential item must preserve exact source ancestry.

The proof must also include:

1. one Book Cut run in which later textual material is unavailable;
2. one difficult reading with disagreement or explicit fog preserved;
3. one bounded context pack with source references;
4. one deletion-and-rebuild test for the Novelist-compatible room projection;
5. one dossier/receipt that can replay the research encounter from held bytes without relying on the generated room prose as source evidence.

### 14.4 Rebuild requirement

Delete the Book Room projection while preserving the ALEX witness floor and durable source-local records.

Rebuild an equivalent room projection.

Expected:

```text
source/evidence ancestry survives
room navigation can be regenerated
projection identifiers may change where declared non-semantic
semantic/source-local identity remains stable according to explicit identity rules
no lost projection can erase source evidence
```

This proves the architecture is facing the correct direction.

---

## 15. Hostile specimens

The first implementation plan should preserve RED -> GREEN receipts for a bounded hostile family.

### `BOOKROOM-SUMMARY-001`

Attack: generated summary attempts to replace exact source witness.

Expected: refuse evidence promotion; preserve summary as projection only.

### `BOOKROOM-SOURCE-TRUTH-001`

Attack: a Book Model statement is promoted directly to world/historical truth.

Expected: refuse; preserve source-local assertion.

### `BOOKROOM-INTERPRETATION-001`

Attack: a Research Model interpretation is written into the Book Model as though directly stated by the source.

Expected: refuse; preserve the research proposal separately.

### `BOOKROOM-CUT-LEAK-001`

Attack: material outside a declared Book Cut enters an earlier-cut interpretation.

Expected: refuse or mark contaminated; preserve which material was unavailable.

### `BOOKROOM-RESEMBLANCE-001`

Attack: motif recurrence across source-local records is promoted to genealogy or external identity.

Expected: refuse without deleting the resemblance observation.

### `BOOKROOM-ROOMLOSS-001`

Attack: delete the generated room projection.

Expected: evidence and source-local durable records survive; room rebuild succeeds.

### `BOOKROOM-CARRIER-001`

Attack: a quotation or locus from another edition/carrier impersonates the active carrier.

Expected: refuse exact-carrier attribution unless a separately attributable cross-carrier relation is established.

### `BOOKROOM-FOG-001`

Attack: illegible, inaccessible, or contradictory source material is synthesized into confident Book Model state.

Expected: preserve fog / competing readings; no forced resolution.

### `BOOKROOM-CONTEXT-001`

Attack: inclusion in a bounded context pack is treated as support weight.

Expected: refuse `context selection -> support` laundering.

---

## 16. Failure paths

- **Acquisition incomplete:** room exists only for held scope; missing pages remain explicit.
- **OCR/reading fails:** successful neighboring readings survive; failed locus remains fog.
- **Book Model extraction ambiguous:** preserve competing candidates or unresolved status.
- **Research interpretation unsupported:** preserve proposal/refusal without rewriting the Book Model.
- **Projection corrupt or deleted:** rebuild from ALEX records; do not reacquire merely to repair a view.
- **Later correction changes a reading:** append descendant reading and affected source-local model descendants; preserve previous occurrence.
- **Cross-room question appears during Gate 4:** record as future research proposal; do not create Library-wide semantics inside BOOKROOM-001.
- **Novelist tooling unavailable:** evidence floor and Book Room durable records remain valid; compatible projection may be generated later.
- **LOADOUT compile invalid or stale once Gate 3 is active:** Book Room operation does not bypass the handshake.

---

## 17. Scope deliberately NOT crossed

BOOKROOM-001 does not yet:

- implement multiple rooms at once;
- merge editions into one work identity;
- create a universal book ontology;
- add every Book Room relation to the ALEX production predicate manifest;
- treat character/entity extraction as historical fact;
- infer composition chronology from chapter order;
- implement vector clocks or distributed-snapshot infrastructure;
- make MEMENTO a runtime dependency;
- make Novelist a source-of-truth dependency;
- build the final spatial Desk;
- create a cross-library graph database;
- automatically publish research conclusions;
- grant source, room, model, or tool authority;
- collapse BOOK MODEL and RESEARCH MODEL under a shared mutable `truth` field.

---

## 18. Relationship to existing gates

```text
Gate 0  ALEX x LOADOUT constitutional boundary
Gate 1  Blind Crucible
Gate 2  RELATION-DERIVATION-001
Gate 3  LOADOUT handshake
Gate 3.5 formation / relation provenance   [candidate seam]
Gate 4  BOOKROOM-001                       [this spec]
Gate 5  Library: multiple rooms + cross-room Desk
Gate 6  rebuildable spatial Desk / local agent port
```

Gate 4 must consume earlier constitutional laws rather than reimplement them.

In particular:

- Gate 2 owns scoped semantic support derivation;
- Gate 3 owns compile validity, capability/effect-fence testimony, expiry, and non-inherited authority;
- Gate 3.5, if separately admitted, owns formation/relationship provenance pressure;
- Book Room owns book-scale source/research organization and textual-cut behavior;
- owning-world gates remain the only source of external consequence.

Gate 3.5 is not silently promoted by this spec. BOOKROOM-001 is designed to use such a seam if and when it is separately admitted.

---

## 19. Library successor

Only after BOOKROOM-001 proves one room should ALEX generalize toward the literal Library:

```text
ALEX LIBRARY
|
+-- ROOM A
+-- ROOM B
+-- ROOM C
+-- ...
|
+-- GLOBAL RESEARCH DESK
      proposes and evaluates cross-room relations
```

The Library does not merge source-local worlds. It provides a higher-level research plane where cross-room relations can be proposed, receipted, evaluated, refused, or left unresolved.

This future gate earns the library metaphor mechanically rather than rhetorically.

---

## 20. Decision record

### Context

ALEX already has a provenance-first evidence floor and a one-book vertical slice. MEMENTO demonstrates a useful membrane around a Novelist-compatible narrative workspace: source, interpretation, local decision, ledger, and rendered traversal remain distinct. Recent temporal/partial-order work also requires ALEX to distinguish textual order, causal order, observer availability, and chosen projection.

### Options considered

#### A. Literal Novelist project per book

Fast and conceptually clear, but fiction-oriented canon semantics and full scaffold replication would become heavy and could make planning structures look evidentiary.

**Rejected as the durable core.**

#### B. Rewrite Novelist concepts into a wholly new ALEX book ontology

Cleaner terminology but discards mature context/continuity machinery and risks rebuilding the same cognitive scaffold from scratch.

**Rejected for Gate 4.**

#### C. ALEX evidence core + Novelist-compatible Book Room projection

Preserves ALEX custody and source ancestry while reusing the strongest organizational ideas from MEMENTO/Novelist as a rebuildable view.

**Selected.**

### Consequences

ALEX gains a book-scale research place rather than only a document pipeline. The cost is a stricter membrane: callers must state whether a fact belongs to the source-local Book Model or to the Research Model, and cross-room inference becomes explicit rather than convenient.

That cost is aligned with ALEX's purpose.

---

## 21. Seal

> **A Book Room preserves two worlds without confusing them: what the book can be shown to contain, and what the researcher currently thinks follows from it.**

And the shorter law:

> **THE BOOK GETS A WORLD. THE RESEARCH GETS ANOTHER. ALEX KEEPS THE RECEIPTS BETWEEN THEM.**

No runtime implementation, Gate 4 conformance, cross-library inference, or external admission is claimed by this specification.
