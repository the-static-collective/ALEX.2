# NAME Attestation + Transform v0 — Review Amendment

**Date:** 2026-08-29

**Applies to:** `docs/superpowers/plans/2026-08-29-name-attestation-transform-v0.md`

**Reason:** independent owner-style review found that the original plan overloaded one SHA-shaped `input_ref` with two different jobs: occurrence ancestry and exact text-carrier identity.

This amendment supersedes only those transform-ancestry details. The implementation plan's broader scope, TDD sequence, authority freeze, and decoder boundary remain unchanged.

## Review finding

The first GREEN transform evaluator proved only:

```text
input_ref looks like sha256:<64 lowercase hex chars>
```

It did **not** prove:

```text
input_ref == digest(exact input_text)
```

A valid but unrelated SHA could therefore masquerade as the consumed carrier.

The first correction bound `input_ref` to `sha256_json({"text": input_text})`, which fixed carrier impersonation but exposed a second distinction:

> two distinct source occurrences can carry identical text.

A carrier digest alone therefore cannot preserve occurrence ancestry.

## Corrected data model

The final v0 uses four identities across one transform edge:

```text
PARENT OCCURRENCE
  parent_ref
      ↓
EXACT INPUT TEXT CARRIER
  input_ref
      ↓
TRANSFORM OCCURRENCE
  transform_digest
      ↓
EXACT OUTPUT TEXT CARRIER
  output_digest
```

### Attestation receipt

```text
attestation_digest
  = sha256_json(full attestation occurrence)

raw_form_digest
  = sha256_json({"text": raw_form})
```

The first identifies the occurrence. The second identifies the exact text carrier.

### Transform input

```text
parent_ref
  = declared attestation_digest or prior transform_digest

input_ref
  = sha256_json({"text": input_text})
```

`parent_ref` preserves declared occurrence ancestry. In v0, the isolated evaluator validates its digest shape but does not claim a persistent parent store exists.

`input_ref` is locally verifiable and MUST equal the digest of the supplied exact `input_text`.

### Transform output

```text
transform_digest
  = sha256_json(full transform occurrence)

output_digest
  = sha256_json({"text": output_text})
```

A subsequent transform can use:

```text
parent_ref = prior transform_digest
input_ref  = prior output_digest
```

## Added refusal reasons

```text
invalid_parent_ref
input_ref_mismatch
```

`missing_required_field` also covers a missing `parent_ref`.

## TDD evidence preserved

The review correction itself followed RED → GREEN:

1. RED: attestation lacked `raw_form_digest`; valid-but-unrelated `input_ref` was accepted.
2. GREEN: added exact carrier digests and `input_ref_mismatch` refusal.
3. RED: malformed or absent `parent_ref` was still accepted.
4. GREEN: made `parent_ref` required and SHA-shaped, preserving it in the transform receipt.

## Hostile invariants added

- same exact text + different source world:
  - same `raw_form_digest`;
  - different `attestation_digest`.
- one Unicode/code-point change:
  - different text-carrier digest;
  - different attestation occurrence digest.
- valid SHA for unrelated text:
  - `REFUSE / input_ref_mismatch`.
- missing or malformed occurrence parent:
  - `REFUSE`.
- user-supplied authority:
  - never propagates beyond `authority: none`.

## Final verification gate

Before marking PR #51 ready:

```text
1. GitHub Actions must run on the exact final branch head.
2. crucible-contract must complete successfully.
3. The job step `python -m unittest discover -s tests -v` must complete successfully.
4. PR diff must remain limited to NAME design/plan/tests/runtime surfaces.
5. No derivation, CHRONOBODY, Crucible authority, LOADOUT, 3rdi, or Dogram production semantics may change in this PR.
```

## Seal

> **SAME TEXT MAY HAVE DIFFERENT HISTORY. DIFFERENT HISTORY MUST REMAIN ADDRESSABLE.**

> **THE TRANSFORM MUST NAME BOTH WHERE IT CAME FROM AND WHAT IT ACTUALLY TOUCHED.**
