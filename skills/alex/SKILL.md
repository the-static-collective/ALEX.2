---
name: alex
description: Investigate questions through scanned books, manuscripts, historical editions, and other page-addressable source witnesses. Use when the user invokes @alex or $alex, or asks to find, read, compare, quote, or audit older source material with page-level provenance, OCR or HTR uncertainty, competing readings, or source-to-claim traceability. Do not use for ordinary web research that does not benefit from inspecting source witnesses.
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
access != permission to redistribute
```

No descendant silently overwrites or impersonates the layer before it. Preserve
plural readings, corrections, contradictions, missing pages, illegible marks,
and unresolved questions.

## Choose the smallest task shape

- **FIND** — locate likely works, editions, pages, or collections.
- **READ** — inspect a bounded page range or source locus.
- **COMPARE** — align multiple pages, editions, readings, or translations.
- **TRACE** — walk a quotation or claim backward to its source witness.
- **DOSSIER** — answer a bounded research question with claim-level evidence.
- **AUDIT** — test an existing answer, citation, transcription, or source chain.

Combine shapes only when the request needs them. Do not ingest a whole
collection merely because one page may answer the question.

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

## 6. Quote and cite

Before using quotation marks, retrieve the exact cited locus. Prefer a stable
page or canvas URL plus human-readable page, folio, column, line, or region.
Preserve printed pagination separately from scan sequence.

For a claim based on translation, identify the translator or producing model
and edition. When the wording is decisive, include or inspect the source
language. Never fabricate a page number from a chunk index.

## 7. Apply adversarial pressure

Before finishing a consequential dossier, try to break:

- quote-to-page alignment;
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

## 8. Return an evidence-bearing result

Lead with the answer or finding. Then provide only the apparatus the stakes
require:

- claim-to-locus evidence;
- competing readings or counterevidence;
- residual fog;
- rights or egress boundaries that affected the result;
- the smallest next action capable of resolving uncertainty.

Read [research-receipt.md](references/research-receipt.md) for durable dossiers,
audits, or machine-readable handoffs. Lightweight answers need not emit the
full template.

## Side-effect boundary

Research authorization permits relevant inspection, not automatic bulk
download, corpus mirroring, external model upload, public annotation, or
publication. Resolve rights and user authority before those effects. A local
ALEX runtime may provide stronger custody and replay, but this skill remains
usable with whatever lawful source adapters are actually available.

## Completion check

Before finishing, confirm:

- every load-bearing claim has a resolvable source chain;
- image inspection and text-only retrieval remain distinguishable;
- every quotation was checked at its cited locus;
- plural readings and contradictions were not cleaned away;
- search projections did not become source authority;
- rights, privacy, external egress, truncation, and inaccessible sources remain
  visible;
- uncertainty has a proposed discriminator rather than decorative caveating.
