# ALEX evidence model

Read this reference when ingesting material, preserving multiple readings,
correcting derived text, comparing editions, PRESSURE-testing hypotheses,
preserving formation traces, or designing interoperable ALEX records.

## The witness stack

| Record | What it establishes | What it does not establish |
| --- | --- | --- |
| `work` | A bibliographic or conceptual identity claim | That every attributed carrier is identical |
| `carrier` | One physical or digital edition, object, or manifestation | Original composition or authorship |
| `acquisition` | What bytes or remote resource were received, when, and how | Permission to republish or historical authenticity |
| `canvas` | One ordered visual surface such as a page, folio, plate, or spread | That scan order equals printed pagination |
| `visual_surface` | One exact image state with dimensions, digest, and transform ancestry | That coordinates from another surface apply unchanged |
| `region` | A spatial target on one exact visual surface | The correct reading of that region |
| `reading` | One human, OCR, HTR, or model transcription | Normalized spelling, translation, or truth |
| `normalization` | A declared transformation of a reading | Exact source form |
| `translation` | A declared language transformation | Semantic identity or absence of interpretation |
| `assertion` | A claim supported, contradicted, or contextualized by evidence paths | Constitution by the substrate |
| `hypothesis` | One attributable formulation in a PRESSURE lineage | That later survivors were present in the original seed |
| `bridge` | One typed cross-domain move | Shared mechanism, genealogy, or authority by resemblance alone |
| `breadcrumb` | One attributable transition in discovery or formation | That the transition supplies evidence for the destination claim |
| `toast_ghost` | One attributable residue from an inactive, lost, killed, or divergent formation branch | Error, evidence, ancestry, or genealogy by persistence alone |
| `dossier` | A bounded research assembly and its receipt | A universal or permanently current truth store |

## Required ancestry

Every derived record should carry:

- a stable local identifier;
- one or more exact input identifiers;
- `derived_from` or a more precise typed relation;
- producer identity and method class;
- model, tool, prompt, ruleset, or editorial version when applicable;
- creation time;
- content digest;
- confidence and calibration scope when meaningful;
- status such as proposed, human-corrected, verified, refused, disproved, or unresolved.

Never attach confidence to an assertion merely because its OCR ancestor supplied
a numeric confidence.

## Visual surfaces and region addressing

Prefer existing stable coordinates:

- IIIF Manifest, Canvas, and Annotation identifiers;
- printed page, folio, column, and line labels;
- scan sequence number;
- W3C Web Annotation selectors such as `xywh` for image regions;
- text-position selectors for exact spans;
- byte or content hashes for locally held files.

Keep labels and machine addresses separate. “p. 57” may refer to printed page
57 while the scan sequence is 73.

A region selector is valid only in the coordinate space of the exact visual
surface it targets. Cropping, deskewing, splitting, rotation, resizing, or other
image derivation creates a new visual surface rather than silently mutating the
old one.

A derived visual surface should preserve:

```text
target_surface_id
target_surface_digest
dimensions
coordinate_space
derived_from
transform_to_parent
loss_declaration
```

A region should preserve the selector plus the exact target surface identifier.
If the transform to a requested parent surface is missing or declared lossy,
refuse exact spatial citation rather than guessing.

## Plural readings

Represent each reading independently. Align them with comparison records rather
than replacing one:

```text
region R
  -> OCR reading A
  -> HTR reading B
  -> human reading C
  -> unresolved alternatives D1 / D2
```

A human correction may be preferred for a task, but the corrected record must
point to the reading it corrects. Reprocessing with a new model creates another
reading.

Agreement among readings does not prove independence. Preserve known dependence
on a shared model family, OCR source, edition, scan, training or retrieval
lineage when material; otherwise record `independence: unknown`.

## Claim relations and evidence paths

Useful relations include:

- `quotes` — exact wording at a locus;
- `supports` — evidence bears positively on a claim;
- `contradicts` — evidence bears negatively;
- `contextualizes` — relevant without directly proving;
- `transcribes`, `normalizes`, and `translates` — declared transformations;
- `corrects` and `supersedes_for` — revision with a named purpose;
- `derived_from` — generic accountable descent;
- `resembles` — similarity without genealogy;
- `motivated_by` — formation or discovery cause without evidentiary implication;
- `left_residue` — inactive formation whose consequence remains attributable;
- `replays` — a receipt regenerated a tested surface or successor under declared conditions;
- `constitutes` — reserved for an owning human or project gate.

Do not use `same_as` as a convenience for uncertain identity.

Support should preserve the transformation path actually relied upon, not only
a naked page or region. For example:

```text
assertion C
  supported_by translation T
    derived_from normalization N
      derived_from reading R
        targets region X
          on visual surface S
```

A translation may bear a semantic claim while remaining insufficient for an
exact-form claim. A normalization may bear a lexical comparison while remaining
insufficient for original orthography.

## PRESSURE hypothesis lineage

Preserve a deliberately strange or overstrong hypothesis as an attributable
lineage rather than silently cleaning it up:

```text
H0 — verbatim seed
  -> H1 — literalized testable claim
  -> H2 — corrected survivor
  -> H3 — cross-domain survivor, if earned
```

Each descendant records what changed and why. A later survivor may be more
useful than `H0` without impersonating it.

When formation loss matters, a transition should also preserve:

```text
what_survived
what_was_removed
why_removed
recoverable_from_prior_state
```

A consequential PRESSURE run should seek:

- supporting precedent;
- a direct counterexample;
- the nearest boring explanation;
- an independent-domain recurrence.

The first three bear on the literal hypothesis. The fourth may generate a new
analogy or research question but does not establish common mechanism.

## Discovery trace and formation records

Read [formation-trace.md](formation-trace.md) when the path by which the inquiry
formed is itself worth preserving.

Keep two ledgers conceptually distinct:

```text
DISCOVERY TRACE — why we looked
EVIDENCE PATH — why we believe, doubt, or refuse
```

A `breadcrumb` records an attributable step in the discovery or formation path.
Its `role` should state whether it was motive, evidence, counterevidence,
inference, analogy, coincidence, wordplay, or discriminator.

A `toast_ghost` records residue from a branch that is no longer active but still
helps explain the present formation. It should preserve what was there, why it
left the active path, what consequence remains, and whether it can be revisited.

Hard boundaries:

```text
discovery path != evidence path
breadcrumb != evidence
toast_ghost != evidence
toast_ghost != genealogy
```

A breadcrumb can also be evidence only when it independently qualifies as an
evidence-bearing record or relation. Its role in causing a search does not grant
that status.

## SLEEP suspension state

When the formation protocol is active, keep one to three live formulations.
Three is a cap, not a quota.

Each suspended formulation may carry:

```text
formulation
supporting_paths
contradicting_paths
unknowns
toast_ghosts
next_discriminator
status
```

Evidence may strengthen, weaken, split, merge, kill, or replace a formulation.
Do not preserve a disproved formulation as live merely for symmetry.

## Replay relations

A `.LEEP` result must distinguish:

```text
EXACT REPLAY
ATTRIBUTABLE RECONSTITUTION
DIVERGENT REPLAY
INSUFFICIENT RECEIPT
```

`replays` does not imply `same_as`. A surface reproduced under declared
conditions does not establish historical identity or uniqueness of formation.
A replay delta should remain attributable rather than being cleaned away.

## Bridge Ledger

Cross-domain moves should be represented explicitly. Useful bridge types
include:

- `documented_mechanism`
- `documented_association`
- `scholarly_interpretation`
- `inference`
- `formal_analogy`
- `metaphor`
- `theological_interpretation`
- `unresolved_bridge`

A bridge should record source domain, destination domain, formulation, evidence
bearing, and promotion limit.

```text
similarity != genealogy
agreement != independent corroboration
analogy != shared mechanism
```

## Interoperability boundary

ALEX should be able to export or import without making external standards its
internal constitution:

- IIIF Presentation API for ordered canvases and image delivery;
- W3C Web Annotation for page and region targets;
- ALTO XML or hOCR for layout-aware OCR interchange;
- TEI P5 for scholarly transcription or edition export;
- plain UTF-8 and JSON Lines for durable, inspectable fallback.

Internal v0 records may remain simpler as long as exact ancestry, transformation
paths, coordinate spaces, hypothesis lineage, discovery/evidence separation,
and locators survive round-trip export.
