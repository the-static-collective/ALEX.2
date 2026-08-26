# Source routing

Read this reference when choosing where and how to search, acquire, inspect, or
process source material.

## Route by evidence need

| Need | Preferred route | Main caution |
| --- | --- | --- |
| Inspect user-held material | Local PDF, image, EPUB, or text | Do not send externally without authority |
| Read a digitized codex or rare book | IIIF Manifest and Canvas when available | Viewer access does not imply redistribution rights |
| Search a translated rare-book corpus | Source Library or another page-citing corpus | OCR and translations remain derived layers |
| Retrieve an archive scan | Institutional or Internet Archive APIs | Preserve item identifier, fileset, and rights metadata |
| Transcribe historical print | Layout-aware OCR plus page inspection | Printed ornament, columns, and ligatures can mislead |
| Transcribe handwriting or non-Latin scripts | HTR or ATR such as Kraken/eScriptorium | Model fit is script, hand, and corpus dependent |
| Find scholarly context | Primary papers, editions, and institutional docs | Scholarship interprets; it does not replace the witness |
| Find conceptual parallels | Semantic retrieval | Return to exact loci and pressure anachronism |

## Source precedence

Precedence depends on the claim.

- For what marks are visible: inspect the best available facsimile.
- For a diplomatic transcription: prefer an attributable scholarly or
  human-verified transcription, while retaining the image.
- For exact wording in a named edition: use that edition, not a modernized text.
- For translation: use the identified translation and consult source language
  when wording matters.
- For date, provenance, or authorship: compare catalog, edition, and scholarship;
  do not infer from text similarity alone.
- For current access or API behavior: use current provider documentation.

“Primary source” is not a synonym for “correct.” A forged, miscataloged, later,
or damaged witness can still be primary evidence of what that witness contains.

## Acquisition receipt

For a load-bearing retrieval, preserve:

- provider and collection;
- stable item, manifest, canvas, page, or file identifier;
- exact URL or local locator;
- acquisition time;
- query or operation;
- scope and pagination;
- truncation or missing ranges;
- returned media type and content digest when locally held;
- rights, license, terms, or unresolved status;
- authentication or access boundary without exposing credentials.

## OCR and HTR selection

Do not crown one universal reader.

1. Detect page type, script, language, layout, and scan defects.
2. Choose a model known to fit that material when available.
3. Preserve raw output and model identity.
4. Double-read only the pages or regions whose uncertainty affects the question.
5. Align variants; do not average them into invented certainty.
6. Escalate to human inspection for decisive loci.

External vision models may be useful readers. Record page egress and provider;
do not claim local-only handling when bytes crossed that boundary.

## No-result discipline

Keep these distinct:

- the source contains no match;
- the searched index contains no match;
- the query syntax or language failed;
- the result window was truncated;
- the source is inaccessible;
- the source is not digitized;
- OCR failed to expose a visible occurrence;
- access terms prevented acquisition.

Only the first can support a bounded textual absence claim, and even then the
searched edition and method must be named.

## Rights boundary

Record separately:

- public access;
- public-domain status of the underlying work;
- rights in the scan or photograph;
- rights in a modern edition or translation;
- permission for local research;
- permission for redistribution, publication, or model training.

Never infer one from another. Do not bypass paywalls, authentication, robots
rules, technical access controls, or provider rate limits.
