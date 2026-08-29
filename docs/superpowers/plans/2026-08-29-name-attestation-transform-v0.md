# NAME Attestation + Transform v0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add deterministic executable ALEX receipts for one NAME attestation and one declared text-transformation edge without allowing transformed text or downstream decoder output to impersonate the source witness.

**Architecture:** Add one focused standard-library module, `alex_runtime/name_attestation.py`, with two pure evaluators: `evaluate_name_attestation()` and `evaluate_text_transform()`. Both validate bounded JSON-like mappings and return canonical deterministic `ACCEPT` or `REFUSE` receipts with `authority: none`; digests reuse `alex_runtime.digests.sha256_json`.

**Tech Stack:** Python 3.12 standard library, `unittest`, existing `alex_runtime.digests` canonical JSON helpers.

**Spec:** `docs/superpowers/specs/2026-08-29-name-attestation-transform-v0-design.md`

## Global Constraints

- Production runtime remains Python standard library only.
- `raw_form` and transformation text are data; ALEX does not infer linguistic correctness in v0.
- Numeric decoding is out of scope.
- Every output freezes `authority` to `none`.
- Attestation identity includes `source_world` and the exact supplied `raw_form`.
- Transformation occurrence identity and output-carrier identity remain distinct digests.
- Invalid research records return deterministic `REFUSE`; they do not mint claims.

---

### Task 1: NAME-ATTESTATION-001 evaluator

**Files:**
- Create: `tests/test_name_attestation.py`
- Create: `alex_runtime/name_attestation.py`

**Interfaces:**
- Consumes: `sha256_json(value: dict) -> str` from `alex_runtime.digests`.
- Produces: `evaluate_name_attestation(record: object) -> dict`.

- [ ] **Step 1: Write failing attestation tests**

Create `tests/test_name_attestation.py` with these first tests:

```python
import copy
import unittest

from alex_runtime.name_attestation import evaluate_name_attestation


BASE_ATTESTATION = {
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
    "referent_confidence": "high",
}


class NameAttestationTests(unittest.TestCase):
    def test_accepts_bounded_attestation_and_freezes_authority(self):
        record = copy.deepcopy(BASE_ATTESTATION)
        record["authority"] = "canon"
        result = evaluate_name_attestation(record)
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["schema"], "alex.name-attestation-result/v0")
        self.assertEqual(result["receipt"]["raw_form"], "Ἰησοῦς")
        self.assertEqual(result["receipt"]["source_world"], "B")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertTrue(result["receipt"]["attestation_digest"].startswith("sha256:"))

    def test_unicode_change_changes_attestation_identity(self):
        first = evaluate_name_attestation(copy.deepcopy(BASE_ATTESTATION))
        second_record = copy.deepcopy(BASE_ATTESTATION)
        second_record["raw_form"] = "ΙΗΣΟΥΣ"
        second = evaluate_name_attestation(second_record)
        self.assertNotEqual(
            first["receipt"]["attestation_digest"],
            second["receipt"]["attestation_digest"],
        )

    def test_source_world_is_part_of_attestation_identity(self):
        first = evaluate_name_attestation(copy.deepcopy(BASE_ATTESTATION))
        second_record = copy.deepcopy(BASE_ATTESTATION)
        second_record["source_world"] = "D"
        second = evaluate_name_attestation(second_record)
        self.assertNotEqual(
            first["receipt"]["attestation_digest"],
            second["receipt"]["attestation_digest"],
        )

    def test_rejects_invalid_source_world(self):
        record = copy.deepcopy(BASE_ATTESTATION)
        record["source_world"] = "Z"
        result = evaluate_name_attestation(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_source_world")
        self.assertEqual(result["authority"], "none")

    def test_rejects_blank_required_field(self):
        record = copy.deepcopy(BASE_ATTESTATION)
        record["raw_form"] = ""
        result = evaluate_name_attestation(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "missing_required_field")
```

- [ ] **Step 2: Run RED and verify the feature is absent**

Run:

```bash
python -m unittest tests.test_name_attestation -v
```

Expected: import failure because `alex_runtime.name_attestation` does not yet exist. This is the required RED checkpoint.

- [ ] **Step 3: Implement the minimal attestation evaluator**

Create `alex_runtime/name_attestation.py` with constants and helpers sufficient for Task 1:

```python
from __future__ import annotations

from typing import Any

from alex_runtime.digests import sha256_json

ATTESTATION_SCHEMA = "alex.name-attestation/v0"
ATTESTATION_RESULT_SCHEMA = "alex.name-attestation-result/v0"
ATTESTATION_RECEIPT_SCHEMA = "alex.name-attestation-receipt/v0"
SOURCE_WORLDS = frozenset({"A", "B", "C", "D"})
REFERENT_CONFIDENCE = frozenset({"high", "medium", "low", "unresolved"})
ATTESTATION_REQUIRED = (
    "attestation_id",
    "source_world",
    "artifact_id",
    "locus",
    "language",
    "script",
    "raw_form",
    "reading_status",
    "referent",
    "referent_confidence",
)


def _refuse(schema: str, reason: str) -> dict[str, Any]:
    return {
        "schema": schema,
        "disposition": "REFUSE",
        "reason": reason,
        "authority": "none",
    }


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def evaluate_name_attestation(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(ATTESTATION_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != ATTESTATION_SCHEMA:
        return _refuse(ATTESTATION_RESULT_SCHEMA, "wrong_schema")
    if any(not _nonempty_string(record.get(field)) for field in ATTESTATION_REQUIRED):
        return _refuse(ATTESTATION_RESULT_SCHEMA, "missing_required_field")
    if record["source_world"] not in SOURCE_WORLDS:
        return _refuse(ATTESTATION_RESULT_SCHEMA, "invalid_source_world")
    if record["referent_confidence"] not in REFERENT_CONFIDENCE:
        return _refuse(ATTESTATION_RESULT_SCHEMA, "invalid_referent_confidence")

    digest = sha256_json(record)
    return {
        "schema": ATTESTATION_RESULT_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "receipt": {
            "schema": ATTESTATION_RECEIPT_SCHEMA,
            "attestation_id": record["attestation_id"],
            "attestation_digest": digest,
            "source_world": record["source_world"],
            "raw_form": record["raw_form"],
            "authority": "none",
        },
        "authority": "none",
    }
```

- [ ] **Step 4: Run Task 1 GREEN**

Run:

```bash
python -m unittest tests.test_name_attestation -v
```

Expected: all Task 1 tests pass.

- [ ] **Step 5: Commit Task 1**

```bash
git add tests/test_name_attestation.py alex_runtime/name_attestation.py
git commit -m "feat: add NAME attestation evaluator"
```

---

### Task 2: ORTHO-LADDER-001 transformation evaluator

**Files:**
- Modify: `tests/test_name_attestation.py`
- Modify: `alex_runtime/name_attestation.py`

**Interfaces:**
- Consumes: `_refuse`, `_nonempty_string`, `sha256_json` from Task 1.
- Produces: `evaluate_text_transform(record: object) -> dict`.

- [ ] **Step 1: Add failing transform tests**

Append:

```python
from alex_runtime.name_attestation import evaluate_text_transform


BASE_TRANSFORM = {
    "schema": "alex.text-transform/v0",
    "transform_id": "case-normalize-001",
    "input_ref": "sha256:" + "a" * 64,
    "operation": "CASE_NORMALIZE",
    "input_text": "Ἰησοῦς",
    "output_text": "ΙΗΣΟΥΣ",
    "producer": "declared-test-producer",
    "method_version": "v1",
    "declared_loss": ["case", "accent", "breathing"],
}


class TextTransformTests(unittest.TestCase):
    def test_accepts_declared_transform_and_keeps_two_identities(self):
        result = evaluate_text_transform(copy.deepcopy(BASE_TRANSFORM))
        self.assertEqual(result["disposition"], "ACCEPT")
        receipt = result["receipt"]
        self.assertEqual(receipt["operation"], "CASE_NORMALIZE")
        self.assertEqual(receipt["output_text"], "ΙΗΣΟΥΣ")
        self.assertNotEqual(receipt["transform_digest"], receipt["output_digest"])
        self.assertEqual(receipt["authority"], "none")

    def test_transform_digest_is_key_order_invariant(self):
        first = evaluate_text_transform(copy.deepcopy(BASE_TRANSFORM))
        reversed_record = dict(reversed(list(BASE_TRANSFORM.items())))
        second = evaluate_text_transform(reversed_record)
        self.assertEqual(
            first["receipt"]["transform_digest"],
            second["receipt"]["transform_digest"],
        )

    def test_rejects_invalid_input_ref(self):
        record = copy.deepcopy(BASE_TRANSFORM)
        record["input_ref"] = "attestation:matt-1-21"
        result = evaluate_text_transform(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_input_ref")

    def test_rejects_duplicate_declared_loss(self):
        record = copy.deepcopy(BASE_TRANSFORM)
        record["declared_loss"] = ["case", "case"]
        result = evaluate_text_transform(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_declared_loss")

    def test_rejects_unknown_operation(self):
        record = copy.deepcopy(BASE_TRANSFORM)
        record["operation"] = "MYSTICALLY_EQUIVALENT_TO"
        result = evaluate_text_transform(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_operation")
```

- [ ] **Step 2: Run RED and verify the new function is absent**

Run:

```bash
python -m unittest tests.test_name_attestation.TextTransformTests -v
```

Expected: import failure for `evaluate_text_transform` or test failure because the function is not implemented.

- [ ] **Step 3: Implement the minimal transformation evaluator**

Add to `alex_runtime/name_attestation.py`:

```python
import re

TRANSFORM_SCHEMA = "alex.text-transform/v0"
TRANSFORM_RESULT_SCHEMA = "alex.text-transform-result/v0"
TRANSFORM_RECEIPT_SCHEMA = "alex.text-transform-receipt/v0"
TRANSFORM_OPERATIONS = frozenset({
    "EDITORIAL_TRANSCRIPTION",
    "UNICODE_NORMALIZE",
    "CASE_NORMALIZE",
    "REMOVE_DIACRITICS",
    "TRANSLITERATE",
    "PRONUNCIATION_PROPOSAL",
    "OTHER_DECLARED",
})
TRANSFORM_REQUIRED = (
    "transform_id",
    "input_ref",
    "operation",
    "input_text",
    "output_text",
    "producer",
    "method_version",
)
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")


def _valid_declared_loss(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(_nonempty_string(item) for item in value)
        and len(value) == len(set(value))
    )


def evaluate_text_transform(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != TRANSFORM_SCHEMA:
        return _refuse(TRANSFORM_RESULT_SCHEMA, "wrong_schema")
    if any(not _nonempty_string(record.get(field)) for field in TRANSFORM_REQUIRED):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "missing_required_field")
    if record["operation"] not in TRANSFORM_OPERATIONS:
        return _refuse(TRANSFORM_RESULT_SCHEMA, "invalid_operation")
    if not SHA256_REF.fullmatch(record["input_ref"]):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "invalid_input_ref")
    if not _valid_declared_loss(record.get("declared_loss")):
        return _refuse(TRANSFORM_RESULT_SCHEMA, "invalid_declared_loss")

    transform_digest = sha256_json(record)
    output_digest = sha256_json({"text": record["output_text"]})
    return {
        "schema": TRANSFORM_RESULT_SCHEMA,
        "disposition": "ACCEPT",
        "reason": None,
        "receipt": {
            "schema": TRANSFORM_RECEIPT_SCHEMA,
            "transform_id": record["transform_id"],
            "input_ref": record["input_ref"],
            "transform_digest": transform_digest,
            "output_digest": output_digest,
            "operation": record["operation"],
            "output_text": record["output_text"],
            "declared_loss": list(record["declared_loss"]),
            "authority": "none",
        },
        "authority": "none",
    }
```

- [ ] **Step 4: Run Task 2 GREEN**

Run:

```bash
python -m unittest tests.test_name_attestation -v
```

Expected: all NAME tests pass.

- [ ] **Step 5: Commit Task 2**

```bash
git add tests/test_name_attestation.py alex_runtime/name_attestation.py
git commit -m "feat: receipt declared text transformations"
```

---

### Task 3: Hostile boundary completion and whole-floor verification

**Files:**
- Modify: `tests/test_name_attestation.py`
- Optional documentation-only modification after GREEN: `README.md`

**Interfaces:**
- Consumes: both evaluators from Tasks 1–2.
- Produces: regression proof that exact text/world identity survives hostile input and that no authority can be laundered through either evaluator.

- [ ] **Step 1: Add hostile tests before any production changes**

Add tests for:

```python
def test_wrong_attestation_schema_refuses(self):
    record = copy.deepcopy(BASE_ATTESTATION)
    record["schema"] = "alex.name-attestation/v1"
    self.assertEqual(evaluate_name_attestation(record)["reason"], "wrong_schema")


def test_invalid_referent_confidence_refuses(self):
    record = copy.deepcopy(BASE_ATTESTATION)
    record["referent_confidence"] = "certain-because-I-said-so"
    self.assertEqual(
        evaluate_name_attestation(record)["reason"],
        "invalid_referent_confidence",
    )


def test_transform_input_authority_is_not_propagated(self):
    record = copy.deepcopy(BASE_TRANSFORM)
    record["authority"] = "historical_truth"
    result = evaluate_text_transform(record)
    self.assertEqual(result["authority"], "none")
    self.assertEqual(result["receipt"]["authority"], "none")
```

These should already pass if Tasks 1–2 implemented the spec correctly. If any fail, treat that as RED for the missing boundary and make the smallest production correction.

- [ ] **Step 2: Run the focused suite**

```bash
python -m unittest tests.test_name_attestation -v
```

Expected: all tests pass.

- [ ] **Step 3: Run the entire ALEX suite**

```bash
python -m unittest discover -s tests -v
```

Expected: zero failures and zero errors.

- [ ] **Step 4: Inspect the diff for scope creep**

```bash
git diff main...HEAD -- alex_runtime/name_attestation.py tests/test_name_attestation.py docs/superpowers/specs/2026-08-29-name-attestation-transform-v0-design.md docs/superpowers/plans/2026-08-29-name-attestation-transform-v0.md
```

Confirm there are no changes to derivation semantics, Crucible authority, CHRONOBODY routing, LOADOUT code, 3rdi code, or Dogram.

- [ ] **Step 5: Commit any final test/doc-only changes**

```bash
git add tests/test_name_attestation.py README.md
git commit -m "test: harden NAME ancestry boundaries"
```

## Self-review

- Spec coverage: attestation identity, world identity, exact raw form, transformation occurrence identity, output-carrier identity, declared loss, deterministic refusal, and frozen authority are covered.
- Out of scope remains out of scope: no gematria/isopsephy, no pronunciation inference, no source retrieval, no cross-world inference.
- Type consistency: both public functions accept `object` and return dictionaries; all machine-facing schema/reason strings match the design.
- Placeholder scan: no implementation step depends on unspecified code or deferred error handling.
