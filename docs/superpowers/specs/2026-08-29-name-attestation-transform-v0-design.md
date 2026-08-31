# NAME Attestation + Transform v0 — Design

**Date:** 2026-08-29

**Status:** approved proving-slice design; no historical, theological, or numeric conclusion is constituted here.

**Owning world:** `the-static-collective/ALEX.2`

## Design sentence

ALEX must preserve an exact textual attestation and every declared transformation applied to it so that a later decoder can say **which occurrence it descended from, what exact text state it consumed, how that state changed, and what was declared lost**, without allowing a normalized, transliterated, pronunciation, or numeric descendant to impersonate the source witness.

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

One further distinction is necessary for durable ancestry:

```text
OCCURRENCE IDENTITY != TEXT-CARRIER IDENTITY != TRANSFORM OCCURRENCE IDENTITY
```

Two distinct attestations may expose byte-identical text. Their text-carrier digest may therefore match while their attestation digests remain distinct. A transform must preserve both the occurrence it claims ancestry from and the exact text carrier it actually consumes.

The portable ALEX skill already states the higher-level constitution. This slice gives the narrowest useful part executable teeth.

## Scope

v0 adds two deterministic record validators/builders:

1. `NAME-ATTESTATION-001` — validates and receipts one bounded textual occurrence and exposes a separate raw-text carrier digest.
2. `ORTHO-LADDER-001` — validates and receipts one declared text transformation with explicit parent-occurrence ancestry and exact input-carrier binding.

v0 does **not**:

- retrieve manuscripts or scans;
- perform OCR/HTR;
- infer historical pronunciation;
- decide that two forms are historically identical;
- calculate gematria/isopsephy;
- infer authorial intent from a numeric result;
- cross source worlds automatically;
- prove that a declared `parent_ref` exists in a persistent store;
- issue historical, theological, canon, admission, publication, or execution authority.

## Governing laws

```text
RAW FORM != NORMALIZED FORM
NORMALIZED FORM != TRANSLITERATION
TRANSLITERATION != PRONUNCIATION
DECODER INPUT != SOURCE WITNESS
NUMERIC RESULT != HISTORICAL INTENT
OCCURRENCE DIGEST != TEXT-CARRIER DIGEST
PARENT OCCURRENCE != CONSUMED TEXT CARRIER
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
- `raw_form` must be non-empty and is preserved exactly as supplied to canonical JSON encoding;
- `referent_confidence` must be one of `high|medium|low|unresolved`;
- optional fields remain opaque occurrence data, not promoted semantics.

### Output receipt

```json
{
  "schema": "alex.name-attestation-receipt/v0",
  "attestation_id": "matt-1-21-iesous",
  "attestation_digest": "sha256:...",
  "raw_form_digest": "sha256:...",
  "source_world": "B",
  "raw_form": "Ἰησοῦς",
  "authority": "none"
}
```

Identity rules:

- `attestation_digest = sha256_json(full validated attestation input)` identifies the bounded attestation occurrence.
- `raw_form_digest = sha256_json({"text": raw_form})` identifies only the exact text carrier.
- Changing source-world or other occurrence metadata changes `attestation_digest` without necessarily changing `raw_form_digest`.
- Changing one code point in `raw_form` changes both identities.

This distinction permits **same text, different history** without collapse.

## ORTHO-LADDER-001

A transformation record describes **one edge**, not a whole undocumented pipeline.

### Required input

```json
{
  "schema": "alex.text-transform/v0",
  "transform_id": "strip-diacritics-001",
  "parent_ref": "sha256:<attestation-digest-or-prior-transform-digest>",
  "input_ref": "sha256:<exact-input-text-carrier-digest>",
  "operation": "REMOVE_DIACRITICS",
  "input_text": "Ἰησοῦς",
  "output_text": "Ιησους",
  "producer": "declared-human-or-tool",
  "method_version": "v1",
  "declared_loss": ["breathing", "accent", "subscript_or_diacritic_distinction"]
}
```

### Two ancestry refs, two jobs

`parent_ref` preserves the declared occurrence ancestry:

```text
attestation occurrence
  or prior transform occurrence
        ↓
     parent_ref
```

`input_ref` binds the exact text carrier consumed by this operation:

```text
input_text
  ↓ sha256_json({"text": input_text})
input_ref
```

They must not be overloaded into one field.

In v0, ALEX can prove the local carrier binding because `input_text` is present. It can validate `parent_ref` shape and preserve it, but cannot independently prove that the named parent occurrence exists without a higher-level store/composition context. That future verification is a separate gate rather than an invented certainty here.

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
- non-empty `transform_id`, `parent_ref`, `input_ref`, `operation`, `input_text`, `output_text`, `producer`, and `method_version`;
- operation belongs to the v0 vocabulary;
- `parent_ref` is `sha256:` plus a 64-character lowercase hexadecimal digest;
- `input_ref` is `sha256:` plus a 64-character lowercase hexadecimal digest;
- `input_ref` must exactly equal `sha256_json({"text": input_text})`;
- `declared_loss` is a list of unique non-empty strings;
- v0 records declared loss but does not independently infer whether the declaration is linguistically complete;
- authority is frozen to `none`.

### Output receipt

```json
{
  "schema": "alex.text-transform-receipt/v0",
  "transform_id": "strip-diacritics-001",
  "parent_ref": "sha256:...",
  "input_ref": "sha256:...",
  "transform_digest": "sha256:...",
  "output_digest": "sha256:...",
  "operation": "REMOVE_DIACRITICS",
  "output_text": "Ιησους",
  "declared_loss": ["breathing", "accent", "subscript_or_diacritic_distinction"],
  "authority": "none"
}
```

Identity rules:

- `parent_ref` carries declared occurrence ancestry.
- `input_ref` proves the exact input text carrier consumed locally.
- `transform_digest = sha256_json(full validated transform input)` identifies the complete transformation occurrence.
- `output_digest = sha256_json({"text": output_text})` identifies the exact output text carrier.
- `transform_digest` and `output_digest` are deliberately different identities.

A later transform can therefore use the prior transform occurrence as its `parent_ref` and the prior `output_digest` as its `input_ref`.

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

Malformed programmer inputs that are not mappings are also represented as deterministic refusal rather than process failure.

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
- `invalid_parent_ref`
- `invalid_input_ref`
- `input_ref_mismatch`
- `invalid_declared_loss`

## Hostile specimens

The tests must prove at least:

1. Greek `Ἰησοῦς` and uppercase unaccented `ΙΗΣΟΥΣ` produce different occurrence and text-carrier identities.
2. Two attestations with the same `raw_form` but different source worlds retain the same text-carrier digest while keeping different attestation digests.
3. A transform explicitly relates states without collapsing parent occurrence, input carrier, transform occurrence, or output carrier.
4. Reordering JSON keys does not change a digest.
5. A valid-looking but unrelated input-carrier SHA refuses with `input_ref_mismatch`.
6. A malformed or missing parent occurrence ref refuses.
7. Duplicate declared-loss entries refuse.
8. `authority` supplied by input cannot widen output authority; output remains `none`.
9. An attestation in world `D` cannot silently become world `B`; world is part of occurrence identity.

## Relationship to neighboring systems

### LOADOUT

LOADOUT may bind this evaluator inside a NAME research compile. Router/binding choice is not evidence and does not alter attestation or text-carrier identity.

### 3rdi

3rdi may expose only attestations visible at an exact observer cut. ALEX receives projected occurrence identity; it does not infer hidden evidence into the cut.

### Dogram / Wolfram

Numeric systems consume an explicit transformed text carrier digest and identify the decoder body/configuration that acted on it. Their output may cite occurrence ancestry for context, but arithmetic consumes the exact carrier. They do not modify ALEX ancestry.

## Next gates

After this proving slice survives unrelated tests:

1. refresh and land `LOCAL-SUPPORT-001` on the current ALEX spine;
2. `WORLD-BRIDGE-001` — machine pressure for A/B/C/D crossings;
3. `NAME-NULLS-001` — common-name, Joshua, Barabbas, Sceva, referent-shuffle, label-blind, decoder-swap, and edge-ablation controls;
4. material witness slice — exact image surface / region / plural reading for nomina sacra and inscriptions.

No next gate is automatically admitted by this implementation.

## Seal

> **THE NUMBER MAY BE EXACT. THE ROAD TO THE NUMBER MUST BE EQUALLY EXACT.**

> **ALEX RECEIPTS THE ROAD; IT DOES NOT PREDECLARE WHAT WAITS AT THE END.**
