# NAME Attestation + Transform v0 — Design

**Date:** 2026-08-29

**Status:** approved proving-slice design; no historical, theological, or numeric conclusion is constituted here.

**Owning world:** `the-static-collective/ALEX.2`

## Design sentence

ALEX must preserve an exact textual attestation and every declared transformation applied to it so that a later decoder can say **what exact state it consumed, how that state was produced, and what was lost**, without allowing a normalized/transliterated/numeric descendant to impersonate the source witness.

## Problem

The NAME-of-JESUS research packet stresses ALEX at a dangerous boundary:

```text
Ἰησοῦς
  -> ΙΗΣΟΥΣ
  -> IESOUS
  -> numeric mapping
  -> 888
```

Each arrow can be useful. None is identity by default.

The same pressure exists across Hebrew forms and across manuscript/editorial layers:

```text
historical object
  != image
  != reading
  != normalized string
  != transliteration
  != pronunciation proposal
  != decoder input
  != decoder output
```

The portable ALEX skill already states this constitutionally. This slice gives the narrowest useful part executable teeth.

## Scope

v0 adds two deterministic record validators/builders:

1. `NAME-ATTESTATION-001` — validates and receipts one bounded textual occurrence.
2. `ORTHO-LADDER-001` — validates and receipts one declared text transformation whose input identity is explicit.

v0 does **not**:

- retrieve manuscripts or scans;
- perform OCR/HTR;
- infer historical pronunciation;
- decide that two forms are historically identical;
- calculate gematria/isopsephy;
- infer authorial intent from a numeric result;
- cross source worlds automatically;
- issue historical, theological, canon, admission, publication, or execution authority.

## Governing laws

```text
RAW FORM != NORMALIZED FORM
NORMALIZED FORM != TRANSLITERATION
TRANSLITERATION != PRONUNCIATION
DECODER INPUT != SOURCE WITNESS
NUMERIC RESULT != HISTORICAL INTENT
```

And:

> **A descendant may carry the witness forward. It may not impersonate its ancestor.**

## NAME-ATTESTATION-001

### Required input

```json
{
  "schema": "alex.name-attestation/v0",
  "attestation_id": "matt-1-21-iesous",
  "source_world": "B",
  "artifact_id": "na28-matthew",
  "locus": "Matthew 1:21",
  "language": "grc",
  "script": "Greek",
  "raw_form": "Ἰησοῦς",
  "reading_status": "editorial_transcription",
  "referent": "Jesus of Nazareth",
  "referent_confidence": "high"
}
```

### v0 source worlds

- `A` — Hebrew Bible / Second Temple Jewish source world
- `B` — earliest Jesus movement / New Testament source world
- `C` — early material Christianity
- `D` — later reception

### Required validation

- the input must be a mapping;
- `schema` must be exactly `alex.name-attestation/v0`;
- required textual identifiers must be non-empty strings;
- `source_world` must be one of `A|B|C|D`;
- `raw_form` must be non-empty and is preserved byte-for-byte as supplied to canonical JSON encoding;
- `referent_confidence` must be one of `high|medium|low|unresolved`;
- optional fields remain opaque data, not promoted semantics.

### Output receipt

```json
{
  "schema": "alex.name-attestation-receipt/v0",
  "attestation_id": "matt-1-21-iesous",
  "attestation_digest": "sha256:...",
  "source_world": "B",
  "raw_form": "Ἰησοῦς",
  "authority": "none"
}
```

The digest is over the full validated attestation input using ALEX canonical JSON.

## ORTHO-LADDER-001

A transformation record describes **one edge**, not a whole undocumented pipeline.

### Required input

```json
{
  "schema": "alex.text-transform/v0",
  "transform_id": "strip-diacritics-001",
  "input_ref": "sha256:<attestation-or-transform-output-digest>",
  "operation": "REMOVE_DIACRITICS",
  "input_text": "Ἰησοῦς",
  "output_text": "Ιησους",
  "producer": "declared-human-or-tool",
  "method_version": "v1",
  "declared_loss": ["breathing", "accent", "subscript_or_diacritic_distinction"]
}
```

### v0 operation vocabulary

The operation is declared, not executed by ALEX:

- `EDITORIAL_TRANSCRIPTION`
- `UNICODE_NORMALIZE`
- `CASE_NORMALIZE`
- `REMOVE_DIACRITICS`
- `TRANSLITERATE`
- `PRONUNCIATION_PROPOSAL`
- `OTHER_DECLARED`

ALEX validates the receipt. It does not recompute linguistic correctness in v0.

### Required validation

- exact schema;
- non-empty `transform_id`, `input_ref`, `operation`, `input_text`, `output_text`, `producer`, `method_version`;
- operation belongs to the v0 vocabulary;
- `input_ref` begins with `sha256:` and contains a 64-character lowercase hex digest;
- `declared_loss` is a list of unique non-empty strings;
- if `input_text != output_text`, `declared_loss` may be empty only for operations where the researcher explicitly claims no semantic/orthographic loss; v0 records the empty declaration but does not infer loss itself;
- authority is frozen to `none`.

### Output receipt

```json
{
  "schema": "alex.text-transform-receipt/v0",
  "transform_id": "strip-diacritics-001",
  "input_ref": "sha256:...",
  "transform_digest": "sha256:...",
  "output_digest": "sha256:...",
  "operation": "REMOVE_DIACRITICS",
  "output_text": "Ιησους",
  "declared_loss": ["breathing", "accent", "subscript_or_diacritic_distinction"],
  "authority": "none"
}
```

`transform_digest` identifies the full transformation occurrence. `output_digest` identifies the exact output text carrier through canonical JSON of `{"text": output_text}`. The two identities are deliberately different.

## Refusal behavior

Public builders return deterministic evaluator receipts rather than raising for research-invalid input:

```json
{
  "schema": "alex.name-attestation-result/v0",
  "disposition": "REFUSE",
  "reason": "invalid_source_world",
  "authority": "none"
}
```

Malformed programmer inputs that are not mappings may also be represented as deterministic refusal rather than process failure.

v0 refusal reasons are stable machine-facing strings:

### Attestation

- `not_an_object`
- `wrong_schema`
- `missing_required_field`
- `invalid_source_world`
- `invalid_referent_confidence`

### Transform

- `not_an_object`
- `wrong_schema`
- `missing_required_field`
- `invalid_operation`
- `invalid_input_ref`
- `invalid_declared_loss`

## Hostile specimens

The tests must prove at least:

1. Greek `Ἰησοῦς` and uppercase unaccented `ΙΗΣΟΥΣ` produce different attestation identities.
2. A transform explicitly relates those states without collapsing them.
3. Reordering JSON keys does not change a digest.
4. Changing one Unicode code point changes the digest.
5. Duplicate declared-loss entries refuse.
6. A fake input reference refuses.
7. `authority` cannot be supplied by the input to widen output authority; output remains `none`.
8. An attestation in world `D` cannot silently become world `B`; world is part of attestation identity.

## Relationship to neighboring systems

### LOADOUT

LOADOUT may bind this evaluator inside a NAME research compile. Router/binding choice is not evidence and does not alter attestation identity.

### 3rdi

3rdi may expose only attestations visible at an exact observer cut. ALEX receives the projected occurrence identity; it does not infer hidden evidence into the cut.

### Dogram / Wolfram

Numeric systems consume an explicit transformed text state or carrier digest. Their output should cite the exact consumed digest and decoder identity. They do not modify ALEX ancestry.

## Next gates

After this proving slice survives unrelated tests:

1. `WORLD-BRIDGE-001` — machine pressure for A/B/C/D crossings.
2. `NAME-NULLS-001` — common-name, Joshua, Barabbas, Sceva, referent-shuffle, label-blind, decoder-swap, and edge-ablation controls.
3. material witness slice — exact image surface / region / plural reading for nomina sacra and inscriptions.

No next gate is automatically admitted by this implementation.

## Seal

> **THE NUMBER MAY BE EXACT. THE ROAD TO THE NUMBER MUST BE EQUALLY EXACT.**

> **ALEX RECEIPTS THE ROAD; IT DOES NOT PREDECLARE WHAT WAITS AT THE END.**
