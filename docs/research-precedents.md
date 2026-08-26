# Research precedents

These projects supplied pressure and reusable mechanisms. They are ancestry and
adapters, not ALEX constitution.

## Source Library

[Source Library](https://sourcelibrary.org/) demonstrates that a large corpus of
rare books can expose scanned pages beside OCR and AI-assisted translations,
stable page citations, exact-quote endpoints, semantic search, a public API,
and an MCP surface. Its published
[pipeline architecture](https://sourcelibrary.org/developers/pipeline) also
preserves page revisions and separates automated processing from human
curation and correction.

**Carry:** page-return, open adapters, revision history, human correction,
operational backpressure, and reproducible research.

**Do not import:** dependence on one hosted corpus, one database, one model
family, or one translation field as ALEX's local constitution.

## Ithaca and Aeneas

Google DeepMind's
[Ithaca](https://deepmind.google/blog/predicting-the-past-with-ithaca/) returned
multiple restoration hypotheses, probability distributions for place and date,
and saliency aids rather than a single unexplained completion. Its successor,
[Aeneas](https://deepmind.google/blog/aeneas-transforms-how-historians-connect-the-past/),
adds multimodal input and contextual parallels across a harmonized corpus of
Latin inscriptions. The published evaluations emphasize historian-plus-model
work rather than model sovereignty.

**Carry:** plural hypotheses, calibrated distributions, contextual-parallel
retrieval, visible model influence, multimodal comparison, and expert gates.

**Do not import:** epigraphic task assumptions as a universal book or manuscript
ontology; model similarity as genealogy; benchmark accuracy as proof about a
new script or collection.

## In Codice Ratio

[In Codice Ratio](https://arxiv.org/pdf/1803.03200) explored scalable
transcription of medieval Vatican registers with limited training material.
Its character-segmentation lattice generated candidate readings that a language
model ranked, while paleographers retained local correction work.

**Carry:** candidate lattices, low-resource adaptation, script-specific
evaluation, and human correction.

**Do not import:** a 2018 Latin-register pipeline as today's universal OCR or
HTR answer.

## DigiVatLib and IIIF

The [Digital Vatican Library](https://digi.vatlib.it/) separates long-term
high-resolution image preservation from online access and uses the
International Image Interoperability Framework. The
[IIIF Presentation API](https://iiif.io/api/presentation/3.0/) supplies ordered
canvases and Web Annotations suitable for page, region, OCR, and transcription
layers.

**Carry:** manifest and canvas addressing, tiled images, ordered surfaces,
region-level annotation, and archive interoperability.

**Do not import:** public viewer access as redistribution permission, shelfmark
metadata as authorship proof, or institutional custody as interpretive
authority.

## Open scholarly standards and readers

- [W3C Web Annotation](https://www.w3.org/TR/annotation-model/) provides
  interoperable bodies, targets, selectors, and provenance for page regions.
- [TEI P5](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/MS.html)
  supports detailed manuscript description and source-to-facsimile links.
- [Kraken](https://kraken.re/) and
  [eScriptorium](https://escriptorium.eu/about) provide open OCR and HTR tooling
  oriented toward historical and non-Latin material.

ALEX v0 should interoperate with these where the use case earns it. It should
not begin by implementing every standard or making TEI/XML the internal storage
engine.
