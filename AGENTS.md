# ALEX.2 contributor instructions

Read the current design under `docs/superpowers/specs/` and the `alex` skill
before changing architecture or research semantics.

## Preserve the stack

Never silently collapse:

- object, carrier, scan, and acquisition;
- page image and extracted text;
- OCR, HTR, human transcription, and correction;
- transcription, normalization, and translation;
- similarity and genealogy;
- evidence, interpretation, proposal, and admitted claim;
- discovery path and evidence path;
- breadcrumb and evidence;
- toast-ghost and evidence or genealogy;
- replay match and historical identity;
- public access and permission to redistribute.

Corrections and reprocessing create descendants. Preserve prior outputs and
their provenance.

## Keep the floor local and replaceable

- Raw held bytes are immutable and content-addressed.
- Search, vector, graph, thumbnails, summaries, and caches are rebuildable.
- Provider-specific behavior stays inside adapters.
- No external model receives local page bytes without an explicit egress record
  and user authority.
- Do not commit source corpora, credentials, copyrighted scans, or private
  research material to this repository.

## Work at the current gate

The repository currently contains an architectural blueprint and portable
skill. Do not report a working ingestion or OCR runtime until executable tests
prove it. The first implementation must remain one-book vertical-slice scale.

When implementation begins:

- preserve failing specimens and source receipts;
- test refusal paths as first-class outcomes;
- validate exact quote-to-page return, revision ancestry, offline replay, and
  rights/egress boundaries;
- preserve discovery motive separately from evidence support when formation
  tracing is active;
- treat `{ PEEL. SLEEP .LEEP }` as an optional research protocol, not a universal
  ontology;
- update the design when an accepted change alters a public interface or
  invariant.

## Authority

ALEX may discover, read, compare, and propose. It does not decide historical
canon or manufacture source authority. Human and owning-project gates admit
consequences.
