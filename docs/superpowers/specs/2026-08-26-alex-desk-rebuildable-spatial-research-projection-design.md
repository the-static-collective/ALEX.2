# ALEX DESK — Rebuildable Spatial Research Projection v0

**Date:** 2026-08-26

**Status:** approved architectural amendment; design-only, no runtime claimed

**Applies to:** `docs/superpowers/specs/2026-08-25-alexandria-floor-design.md`

## Design sentence

> **ALEX DESK is a rebuildable spatial projection of ALEX evidence records: movable cards, typed red-yarn relations, lenses, and formation traces that let a researcher think by arrangement without allowing arrangement to become evidence, ancestry, identity, or authority.**

The durable research reality remains the ALEX witness stack. A desk is one inspectable way of arranging part of that reality for a bounded question.

## Architectural correction

The original Alexandria Floor described the Evidence Desk as a human research interface. This amendment narrows and strengthens that idea:

```text
ALEX evidence floor
    -> rebuildable desk projection
        -> zero or more renderers
```

The desk projection is durable enough to replay and compare. Any HTML, SVG, canvas, printable board, graph renderer, or future local viewer is replaceable.

The renderer is not the desk.

The desk is not the evidence floor.

## Constitutional invariants

```text
desk position != evidence
proximity != relation
yarn != proof
grouping != identity
hidden != absent
same pile != same lineage
visual resemblance != genealogy
desk arrangement != canon
rearrangement != source mutation
same endpoint != same path
same visible surface != same formation
trace != lineage
```

Additional rules:

1. Moving, stacking, rotating, hiding, or grouping cards changes only the projection.
2. A relation becomes evidentiary only through its underlying typed ALEX evidence path, never through visual proximity.
3. Spatial placement may preserve discovery motive without being promoted into support.
4. A proposed relation and a demonstrated relation must remain visibly and machine-readably distinct.
5. Refused, contradicted, killed, or unresolved relations remain addressable when useful.
6. A destroyed desk must be reconstructible from its projection receipt without changing source records.
7. Multiple desks may project the same evidence floor differently without one becoming canonical by default.
8. A desk may expose only a bounded neighborhood; omission from a desk is not absence from the corpus.
9. Renderers may decorate relations, but relation semantics live in typed records, not color or geometry alone.
10. No desk operation may silently constitute a historical, interpretive, or project claim.

## Borrowed eCODE mechanisms

ALEX DESK deliberately reuses existing Static Collective ideas only where their invariants survive translation.

### Material Grammar — lawful operations depend on the thing

The desk should not flatten every object into a generic node.

Examples:

- a visual surface may be cropped or spatially targeted;
- a reading may be corrected;
- a normalization may descend from a reading;
- a translation may descend from source-language text;
- a hypothesis may fork into descendants;
- an assertion may be supported, contradicted, contextualized, or refused.

The common shape is:

```text
material
  + lawful operation
  + preserved ancestry
  -> changed affordance
  -> explicit consequence
```

The visual metaphor must not manufacture operations that the underlying record type does not support.

### Pocket Web Hypermath — path identity survives endpoint equality

ALEX DESK adopts the narrow invariant:

```text
same endpoint != same path != same trace
```

Two research paths may reach equivalent conclusions while retaining different ancestry, independence, counterevidence, and formation receipts.

A lens may temporarily treat two endpoints as equivalent for a named purpose. It may not erase the route by which either was reached.

### Free Graph — portable relation membrane

ALEX may export a bounded desk neighborhood through Free Graph without making Free Graph the ALEX research ontology.

The portable verbs remain useful as a reduced interchange layer:

```text
connects
descends-from
tests
bears-on
constitutes
```

`constitutes` is display/export-only from the desk's perspective: it may serialize an already-existing constitution receipt owned by a human or participating project. A desk action, lens, arrangement, or renderer may never create, infer, or promote a relation to `constitutes`.

ALEX-local relations remain richer where required, including `transcribes`, `normalizes`, `translates`, `corrects`, `quotes`, `supports`, `contradicts`, `contextualizes`, `resembles`, `motivated_by`, `left_residue`, and `replays`.

### Palimpsest Continuity — transformation before sameness

The desk should preserve typed transformation rather than visually imply sameness.

Useful local relation classes include:

```text
DEMONSTRATED_ANCESTRY
CLAIMED_ANCESTRY
SHARED_PRECURSOR
DOCUMENTED_INFLUENCE
TRANSLATION
TRANSLITERATION
REENCODING
REINTERPRETATION
FORMAL_RESEMBLANCE
STRUCTURAL_ISOMORPHISM
CONTEXTUAL_ASSOCIATION
CONTRADICTION
REFUSED_ANCESTRY
UNKNOWN
```

A renderer may use marks such as knots, breaks, arrows, or glyphs on visually similar red strands, but machine semantics never depend on those glyphs alone.

### Mathematics Before Number / μ0 — minimal desk operations

The desk can remain structurally useful before numerical scoring, ranking, or probability is introduced.

Candidate minimal verbs:

```text
PIN    distinguish and place a record
YARN   declare a typed relation proposal or projection
FORK   create or expose an attributable descendant or alternative
PEEL   expose ancestry and formation backward
TRACE  preserve what happened on the desk
```

`CONSTITUTE` is intentionally absent from the desk operator set. Constitution remains outside the desk at a human or owning-world gate.

### Narrative Solver — the field is richer than one arrangement

The transferable invariant is:

> **The evidence world is richer than any desk arrangement.**

Chronology desks, hypothesis desks, contradiction desks, genealogy desks, PRESSURE desks, and claim-focused desks may all project the same underlying records.

No selected arrangement erases neighboring possibilities.

## Record floor

A v0 desk projection should be able to preserve:

```text
desk_projection
  id
  question_cut
  source_record_ids[]
  placements[]
  relations[]
  lenses[]
  active_lens
  formation_receipt
  created_at
  producer
  version
```

### Placement

```text
placement
  placement_id
  record_id
  x
  y
  scale
  rotation
  z_order
  group_id?
  visible
  annotation?
```

A placement references an existing ALEX record. It does not copy or become that record.

### Relation projection — the red yarn

```text
relation_projection
  relation_projection_id
  from_record_id
  to_record_id
  relation_record_id?
  evidence_path_ids[]?
  relation_type
  status
  direction
  annotation?
  discovery_role?
  evidence_bearing
  created_from
```

Suggested `status` values:

```text
PROPOSED
TESTING
SUPPORTED
CONTRADICTED
REFUSED
UNKNOWN
INACTIVE
```

`SUPPORTED` means the underlying evidence path bears positively within its declared scope. It does not mean universally proven.

`PROPOSED` may arise from researcher intuition or spatial juxtaposition and carry no evidence at all.

If `evidence_bearing` is true, `relation_record_id` and/or `evidence_path_ids` must resolve to the underlying ALEX evidence records that earn that status. A renderer or placement action cannot set evidentiary bearing by itself.

### Lens

A lens is a declared projection rule, not a transformation of the evidence floor.

```text
lens
  lens_id
  name
  visible_record_types[]
  visible_relation_types[]
  hidden_statuses[]
  equivalence_rule?
  temporal_cut?
  question_focus?
  independence_filter?
  evidence_layer_filter?
```

Examples:

- exact-form lens;
- semantic-support lens;
- genealogy lens;
- contradiction lens;
- independent-corroboration lens;
- discovery-trace lens;
- PRESSURE survivor lens.

## Spatial hypothesis without evidentiary promotion

ALEX DESK explicitly permits research by arrangement.

A researcher may place two or more records near one another because they feel related, look similar, arose in the same conversation, or simply deserve comparison.

That spatial act may become an attributable discovery breadcrumb:

```text
PROXIMITY
  -> PROPOSED RELATION
  -> TEST
  -> SUPPORTED | CONTRADICTED | REFUSED | UNKNOWN
```

Hard rule:

> **A strange arrangement may choose the next test. It does not supply the result of the test.**

This is the desk analogue of ALEX's discovery-path / evidence-path split.

## Red-yarn rendering law

The default visual metaphor may use mostly one strand color—red—while semantics remain in labels or deterministic strand marks.

Illustrative renderer vocabulary:

```text
----●----  ancestry / descent
---->----  translation / directed transform
----⊢----  support
----×----  contradiction
----≈----  resemblance
----?----  unresolved
----✂----  refused or broken relation
```

These marks are rendering cues only.

A monochrome printout or different renderer must remain semantically complete through textual relation labels and IDs.

## PEEL / SLEEP / .LEEP as desk operations

### PEEL

Selecting a card or relation may project its attributable ancestry outward without mutating the current evidence records.

A peel may show:

```text
record
  -> parents
  -> transformations
  -> supporting evidence paths
  -> breadcrumbs
  -> toast-ghosts
  -> losses
  -> alternatives
```

### SLEEP

A desk may hold one to three materially live hypothesis cards as a bounded comparison arrangement.

Each state retains its own support, contradiction, unknowns, toast-ghosts, and next discriminator.

Disproved states leave the active comparison but may remain visible as inactive residue.

### .LEEP

A desk formation receipt may replay placements, relation proposals, forks, and selected lenses forward.

Allowed replay outcomes remain:

```text
EXACT REPLAY
ATTRIBUTABLE RECONSTITUTION
DIVERGENT REPLAY
INSUFFICIENT RECEIPT
```

Exact visual replay never establishes historical identity of the underlying source world.

## Destruction and reconstruction

ALEX DESK should be disposable by design.

Given:

```text
evidence floor E
desk receipt R
renderer X
```

it should be possible to delete the rendered desk and regenerate an equivalent projection from `E + R`.

If a renderer cannot reconstruct a cosmetic detail, that loss must remain cosmetic. If it cannot reconstruct relation semantics, record identity, or the selected lens, the receipt is insufficient.

This protects the architecture from becoming trapped inside one UI framework.

## Interchange boundary

Optional interchange formats may be supported later as adapters or projections, including:

- Free Graph packets for bounded portable neighborhoods;
- W3C Web Annotation-compatible targets for page and region references;
- JSON/JSON Lines as the durable boring fallback;
- spatial-canvas export formats when they preserve IDs and typed edges without becoming canonical storage.

No interchange format becomes ALEX constitution merely because a renderer supports it.

## RED YARN 001 — first proving specimen

Do not begin with a full research application.

Use one bounded dossier with approximately 10–15 records containing at least:

- one source page or region;
- two rival readings;
- one normalization or translation;
- one supported assertion;
- one contradicted candidate;
- one unresolved candidate;
- one cross-domain or resemblance proposal;
- one killed hypothesis or toast-ghost;
- one relation whose apparent agreement is not independent corroboration.

### Required actions

1. Build one desk projection from existing record IDs.
2. Rearrange cards without changing any ALEX source record.
3. Create one proximity-motivated proposed yarn relation.
4. Test that relation and preserve its resulting status.
5. PEEL one supported assertion to the exact source locus through its real transformation path.
6. Show two paths to an equivalent endpoint while preserving different receipts.
7. Switch between at least two declared lenses without changing the evidence floor.
8. Move one disproved SLEEP state to inactive residue rather than keeping it live.
9. Destroy the rendered desk.
10. Rebuild it from the evidence floor plus desk receipt.

### Acceptance tests

| Test | Required result |
| --- | --- |
| Proximity trap | Nearby cards do not acquire a relation automatically |
| Yarn promotion trap | A proposed strand does not become evidence without an evidence path |
| Hidden-is-absent trap | Hiding a card or relation under a lens does not create a source-level absence claim |
| Stack identity trap | Stacking equivalent cards does not merge record identity |
| Path collapse trap | Equivalent conclusions reached through different routes retain distinct paths and receipts |
| Independence trap | Agreement from shared ancestry cannot render as independent corroboration |
| Ghost promotion trap | Killed hypotheses or toast-ghosts remain residue unless a new evidence path earns stronger status |
| Renderer authority trap | Changing visual glyphs or strand style cannot change relation semantics |
| Destructive rearrangement trap | Moving cards cannot mutate canonical source, reading, translation, assertion, or lineage records |
| Replay impersonation | Rebuilt desk equivalence does not establish identity with the historical research occurrence |
| Receipt sufficiency | Delete renderer state and rebuild the desk from evidence records plus desk receipt |
| Constitution smuggling | A desk may display an existing `constitutes` receipt but cannot create or infer one |

## Failure conditions

Redesign if ALEX DESK:

- requires one particular GUI framework to preserve research meaning;
- turns free spatial placement into implicit evidentiary relation;
- encodes essential relation meaning only in color, shape, or proximity;
- mutates canonical source records when a card is moved or grouped;
- hides contradictions or rival readings to make a desk cleaner;
- cannot distinguish discovery motive from evidence support;
- treats a pretty arrangement as explanatory or causal proof;
- collapses multiple research paths because their conclusions look equivalent;
- requires a master graph before a bounded desk can exist;
- can create constitutional authority by arranging or exporting records;
- cannot be destroyed and reconstructed without research loss.

## Relationship to the Alexandria Floor

ALEX DESK does not add a new authority layer or widen the first one-book proof into a full visual application.

For the first vertical slice, the minimum implementation consequence is only this:

> **The record model and receipts must not foreclose a later rebuildable desk projection.**

The one-book proof may remain text-first or minimally rendered. RED YARN 001 should become its own separately approved implementation slice after the evidence floor exists strongly enough to project.

## Seal

> **Move the pieces. Keep the witnesses still.**
>
> **Let proximity ask. Let yarn propose. Let evidence decide.**
>
> **Burn the desk if you want. The road back must remain.**
