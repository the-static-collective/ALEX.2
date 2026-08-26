---
name: alex
description: Investigate questions through scanned books, manuscripts, historical editions, and other page-addressable source witnesses. Use when the user invokes @alex or $alex, asks to find, read, compare, quote, or audit older source material with page-level provenance, OCR or HTR uncertainty, competing readings, source-to-claim traceability, deliberate PRESSURE on a strange or overstrong hypothesis, or asks to PEEL/SLEEP/LEEP a research formation path. Do not use for ordinary web research that does not benefit from inspecting source witnesses, explicit hypothesis pressure, or formation trace.
---

# ALEX

Build inquiry upward from visible, attributable source material.

## Constitutional line

Keep these distinctions live:

```text
historical object != scan or photograph
scan != transcription
transcription != normalization
normalization != translation
translation != interpretation
interpretation != claim
search result != evidence
similarity != genealogy
agreement != independent corroboration
discovery path != evidence path
breadcrumb != evidence
toast-ghost != evidence
replay match != historical identity
access != permission to redistribute
```

No descendant silently overwrites or impersonates the layer before it. Preserve
plural readings, corrections, contradictions, missing pages, illegible marks,
and unresolved questions.

A spatial citation must name the exact visual surface whose coordinates it
addresses. Derived crops, deskews, splits, rotations, resizes, and layout
surfaces preserve their parent mapping or declare spatial loss.

## Choose the smallest task shape

- **FIND** — locate likely works, editions, pages, or collections.
- **READ** — inspect a bounded page range or source locus.
- **COMPARE** — align multiple pages, editions, readings, or translations.
- **TRACE** — walk a quotation or claim backward to its source witness.
- **DOSSIER** — answer a bounded research question with claim-level evidence.
- **AUDIT** — test an existing answer, citation, transcription, or source chain.
- **PRESSURE** — preserve a deliberately compressed, strange, or overstrong
  hypothesis verbatim, attack its literal form, search its nearest established
  neighbors, and return the strongest formulation that survives.

Combine shapes only when the request needs them. Do not ingest a whole
collection merely because one page may answer the question. PRESSURE is a
hypothesis wrapper over the smaller shapes, not a new corpus subsystem.

`{ PEEL. SLEEP .LEEP }` is an optional formation-trace protocol that may wrap a
TRACE, DOSSIER, AUDIT, or PRESSURE run when the path by which the inquiry formed
is materially worth preserving. Read
[formation-trace.md](references/formation-trace.md) before using it.

## 1. Establish the inquiry cut

Before searching, record:

- the actual question and useful stopping condition;
- date, language, geography, genre, or corpus limits that matter;
- the kind of witness sought: manuscript, printed edition, facsimile,
  transcription, translation, catalog record, or scholarship;
- whether exact quotation, visual inspection, comparison, or broad discovery is
  required;
- user authority for local reads, downloads, external model egress, durable
  writes, or publication.

For PRESSURE, preserve the user's original seed verbatim as `H0` before
literalizing or correcting it. Later formulations are descendants, not
rewrites:

```text
H0 — verbatim crazy seed
  -> H1 — literalized testable claim
  -> H2 — corrected survivor
  -> H3 — cross-domain survivor, if earned
```

Record what changed at each transition and why. When loss is consequential,
also record what survived, what was removed, why it was removed, and whether the
prior state remains recoverable.

Name missing constraints as fog. Do not turn an unavailable archive or an
unindexed language into historical absence.

## 2. Route to sources

Read [source-routing.md](references/source-routing.md) when selecting archives,
local files, OCR or HTR, external research, or model adapters.

Prefer the route that preserves the strongest useful locator and the least
unnecessary transfer:

1. user-provided local material;
2. stable page or canvas APIs such as IIIF;
3. open institutional or corpus APIs;
4. institutional viewers and catalogs;
5. general web discovery leading back to a source witness.

Connected search services are doors, not foundations. Preserve provider,
query, acquisition time, result scope, truncation, and access boundary for
every load-bearing retrieval.

## 3. Build the witness stack

Read [evidence-model.md](references/evidence-model.md) when ingesting,
comparing, correcting, or designing machine-readable records.

For each relied-upon source, preserve the smallest adequate chain:

```text
work or claimed work
  -> carrier or edition
  -> acquisition event
  -> page or canvas
  -> exact visual surface
  -> region or text span
  -> reading
  -> optional normalization
  -> optional translation
  -> assertion
```

Record producer, method, version, time, inputs, and confidence for machine
readings. Confidence is useful only within the calibration that produced it.
Human correction creates a new attributable revision; it does not rewrite the
machine output.

If a region was produced on a derived visual surface, preserve the surface
digest, coordinate space, parent transform, and any declared loss. Refuse exact
spatial citation when a selector cannot be mapped to the cited surface.

If only extracted text is available, state that the image was not inspected.
If only a catalog record is available, do not speak as though the work was
read.

## 4. Search and read

Use exact search for names, phrases, formulae, dates, shelfmarks, and unusual
orthography. Use semantic search for discovery and contextual parallels, then
return to exact pages before relying on a result.

When OCR is uncertain:

- inspect the page image when available;
- preserve the raw reading;
- compare another OCR or HTR engine when the uncertainty matters;
- keep plausible alternatives rather than forcing one string;
- use neighboring lines, scribal habits, edition context, and language models
  as pressure, not self-authenticating proof.

When a model proposes a restoration, translation, date, location, or parallel,
label it as a proposal and show uncertainty. Expert or human choice remains a
separate act.

Treat agreement as a finding, not proof of independence. When material, record
known shared ancestry among readers, models, OCR sources, editions, training or
retrieval systems; otherwise use `independence: unknown`.

## 5. Form claims without collapse

Classify each important statement as one of:

- **observed** — directly inspected in this run;
- **source testimony** — attributable content of a source;
- **scholarly claim** — attributable interpretation by a scholar or edition;
- **inference** — reasoning introduced in this run;
- **proposal** — a candidate reading, relation, or test;
- **unresolved** — evidence is insufficient or conflicting.

An edition can settle practical reading without erasing its critical
apparatus. A translation may support a semantic claim while remaining
insufficient for exact-form claims. A surviving witness may establish survival
without establishing origin, completeness, authorship, canon, or authority.

Machine-readable support should preserve the evidence path actually relied
upon rather than pointing only to a naked page or locus. For example:

```text
CLAIM
  supported_by
    translation T
      derived_from normalization N
        derived_from reading R
          targets region X
```

The layer that bears the claim remains visible in the support relation.

## 6. Quote and cite

Before using quotation marks, retrieve the exact cited locus. Prefer a stable
page or canvas URL plus human-readable page, folio, column, line, or region.
Preserve printed pagination separately from scan sequence.

For image-region citations, preserve the exact target surface and coordinate
space. Never render derivative coordinates against a parent image without a
proved transform.

For a claim based on translation, identify the translator or producing model
and edition. When the wording is decisive, include or inspect the source
language. Never fabricate a page number from a chunk index.

## 7. Apply adversarial pressure

Before finishing a consequential dossier, try to break:

- quote-to-page alignment;
- visual-surface and coordinate-space alignment;
- edition and scan identity;
- OCR or HTR confidence;
- translation and normalization assumptions;
- apparent independence between sources derived from one lineage;
- semantic parallels that may be anachronistic;
- claims inferred from catalog metadata alone;
- model recitation or memorization mistaken for visual reading;
- absence claims drawn from bounded or truncated search.

A test that cannot refuse the favored conclusion is another search, not a
test.

### PRESSURE — “this is insane; prove around it”

Use PRESSURE when the user intentionally supplies a compressed, strange,
overstrong, or cross-domain hypothesis. The seed creates search pressure; it
receives no evidentiary privilege.

Core law:

> **A crazy hypothesis earns promotion by surviving loss, not by accumulating resemblance.**

Run this loop:

```text
CRAZY SEED
  ↓ preserve verbatim
LITERALIZE
  ↓ what exact claims would have to be true?
ATTACK
  ↓ direct counterexamples / null models / alternative explanations
NEIGHBOR SEARCH
  ↓ established phenomena adjacent to parts of the seed
SEPARATE BRIDGES
  ↓ evidence != inference != analogy != theological or symbolic reading
KILL OVERCLAIMS
  ↓
SURVIVOR
  ↓ strongest formulation still standing
PREDICT
  ↓ what should become observable if the survivor is useful?
PRESSURE AGAIN
```

Explicitly seek four pressures:

1. **supporting precedent** — real mechanisms or observations bearing positively;
2. **direct counterexample** — evidence capable of killing the literal claim;
3. **nearest boring explanation** — the simplest plausible account of the same observations;
4. **independent-domain recurrence** — a similar structure arising for a materially different reason.

The fourth may justify an analogy or a new question. It does not establish a
shared mechanism, genealogy, or authority by resemblance alone.

For cross-domain moves, use the Bridge Ledger in
[research-receipt.md](references/research-receipt.md). Type each bridge as a
documented mechanism, documented association, scholarly interpretation,
inference, formal analogy, metaphor, theological interpretation, or unresolved
bridge.

A PRESSURE run must be allowed to return `disproved`. If it cannot, it is not
adversarial research.

### Formation trace — `{ PEEL. SLEEP .LEEP }`

Use formation trace when discovery itself has a meaningful causal history: a
coincidence chose a door, an overclaim died but redirected inquiry, multiple
live readings remain, or a replayable operation is part of what needs to be
preserved.

Read [formation-trace.md](references/formation-trace.md) and keep two ledgers
separate:

```text
DISCOVERY TRACE — why we looked
EVIDENCE PATH — why we believe, doubt, or refuse
```

- **BREADCRUMBS** preserve attributable formation steps and their roles.
- **TOAST-GHOSTS** preserve inactive residue without promoting it to evidence.
- **PEEL.** exposes the road and roadside backward, then stops.
- **SLEEP** suspends one to three materially live formulations in a
  self-correcting equilibrium. Three is a cap, not a quota; disproved states
  die.
- **.LEEP** replays an attributable receipt forward and returns `EXACT REPLAY`,
  `ATTRIBUTABLE RECONSTITUTION`, `DIVERGENT REPLAY`, or
  `INSUFFICIENT RECEIPT`.

Treat replay identity and serendipity as adversarial boundaries:

```text
search motive != support
replay match != historical identity
```

The phi/ternary operator in the formation-trace reference is a bounded
mathematical specimen showing operation-as-receipt. Do not generalize it into a
universal historical, symbolic, or theological mechanism without independent
evidence.

## 8. Return an evidence-bearing result

Lead with the answer or finding. Then provide only the apparatus the stakes
require:

- claim-to-evidence-path support;
- competing readings or counterevidence;
- residual fog;
- rights or egress boundaries that affected the result;
- the smallest next action capable of resolving uncertainty.

For PRESSURE, preserve at minimum:

```text
SEED
LITERAL VERDICT
WHAT BROKE
WHAT SURVIVED
WHY IT SURVIVED
BRIDGE LEDGER
NEW PREDICTIONS
RESIDUAL WEIRDNESS
NEXT DISCRIMINATOR
```

For formation-trace runs, preserve at minimum:

```text
SURFACE
BREADCRUMBS
TOAST-GHOSTS
SLEEP STATES (1–3)
NEXT DISCRIMINATOR
.LEEP RESULT
REPLAY DELTA
EVIDENCE-PATH BOUNDARY
```

Read [research-receipt.md](references/research-receipt.md) for durable dossiers,
audits, PRESSURE runs, formation traces, or machine-readable handoffs.
Lightweight answers need not emit the full template.

## Side-effect boundary

Research authorization permits relevant inspection, not automatic bulk
download, corpus mirroring, external model upload, public annotation, or
publication. Resolve rights and user authority before those effects. A local
ALEX runtime may provide stronger custody and replay, but this skill remains
usable with whatever lawful source adapters are actually available.

## Completion check

Before finishing, confirm:

- every load-bearing claim has a resolvable source and transformation chain;
- image inspection and text-only retrieval remain distinguishable;
- every quotation was checked at its cited locus;
- spatial selectors remain attached to the exact surface they address;
- plural readings and contradictions were not cleaned away;
- agreement was not promoted to independent corroboration without lineage evidence;
- search projections did not become source authority;
- rights, privacy, external egress, truncation, and inaccessible sources remain
  visible;
- uncertainty has a proposed discriminator rather than decorative caveating;
- a PRESSURE run preserved `H0`, attacked the literal claim, typed its bridges,
  and could have returned `disproved`;
- a formation-trace run kept discovery motive separate from evidence, preserved
  relevant breadcrumbs and toast-ghosts, killed disproved SLEEP states, and did
  not promote replay match into historical identity.
