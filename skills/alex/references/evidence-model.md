# ALEX evidence model

Read this reference when ingesting material, preserving multiple readings,
correcting derived text, comparing editions, or designing interoperable ALEX
records.

## The witness stack

| Record | What it establishes | What it does not establish |
| --- | --- | --- |
| `work` | A bibliographic or conceptual identity claim | That every attributed carrier is identical |
| `carrier` | One physical or digital edition, object, or manifestation | Original composition or authorship |
| `acquisition` | What bytes or remote resource were received, when, and how | Permission to republish or historical authenticity |
| `canvas` | One ordered visual surface such as a page, folio, plate, or spread | That scan order equals printed pagination |
| `region` | A spatial target on a canvas | The correct reading of that region |
| `reading` | One human, OCR, HTR, or model transcription | Normalized spelling, translation, or truth |
| `normalization` | A declared transformation of a reading | Exact source form |
| `translation` | A declared language transformation | Semantic identity or absence of interpretation |
| `assertion` | A claim supported, contradicted, or contextualized by loci | Constitution by the substrate |
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
- status such as proposed, human-corrected, verified, refused, or unresolved.

Never attach confidence to an assertion merely because its OCR ancestor supplied
a numeric confidence.

## Page and region addressing

Prefer existing stable coordinates:

- IIIF Manifest, Canvas, and Annotation identifiers;
- printed page, folio, column, and line labels;
- scan sequence number;
- W3C Web Annotation selectors such as `xywh` for image regions;
- text-position selectors for exact spans;
- byte or content hashes for locally held files.

Keep labels and machine addresses separate. “p. 57” may refer to printed page
57 while the scan sequence is 73.

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

## Claim relations

Useful relations include:

- `quotes` — exact wording at a locus;
- `supports` — evidence bears positively on a claim;
- `contradicts` — evidence bears negatively;
- `contextualizes` — relevant without directly proving;
- `transcribes`, `normalizes`, and `translates` — declared transformations;
- `corrects` and `supersedes_for` — revision with a named purpose;
- `derived_from` — generic accountable descent;
- `resembles` — similarity without genealogy;
- `constitutes` — reserved for an owning human or project gate.

Do not use `same_as` as a convenience for uncertain identity.

## Interoperability boundary

ALEX should be able to export or import without making external standards its
internal constitution:

- IIIF Presentation API for ordered canvases and image delivery;
- W3C Web Annotation for page and region targets;
- ALTO XML or hOCR for layout-aware OCR interchange;
- TEI P5 for scholarly transcription or edition export;
- plain UTF-8 and JSON Lines for durable, inspectable fallback.

Internal v0 records may remain simpler as long as exact ancestry and locators
survive round-trip export.
