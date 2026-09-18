# DIALOGIC TRACE v0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a first-class ALEX living-source research mode that preserves public artifact, question, response, model delta, and independent retest without allowing creator testimony to rewrite earlier evidence or become automatic corroboration.

**Architecture:** Implement DIALOGIC TRACE as a small semantic/runtime module alongside existing ALEX evaluators, backed by explicit JSON-like records and hostile Crucible fixtures. Update the ALEX evidence/receipt references and skill routing first, then implement deterministic validators that always freeze authority at `none` and preserve artifact/response separation.

**Tech Stack:** Python 3 standard library, `unittest`, existing `alex_runtime.digests.sha256_json`, existing Crucible JSON contracts.

**Spec:** `docs/superpowers/specs/2026-09-17-alex-commons-library-card-dialogic-trace-design.md`

## Global Constraints

- `creator response != retroactive proof`
- `creator agreement != independent corroboration`
- `creator disagreement != automatic falsification`
- `current stated intent != historical intent`
- `silence != rejection`
- `question wording != neutral observation`
- `receipt != promotion`
- `authority = none` unless a separate owning-world gate admits a consequence.
- Preserve private/publication boundaries; private correspondence must not be emitted into public fixtures.
- Do not hard-code Haven, David Wollen, Terrence Howard, or any other living person into the protocol.

---

## File map

- Create `skills/alex/references/modes/dialogic-trace.md` — human-facing protocol and refusal laws.
- Modify `skills/alex/SKILL.md` — route living-source discriminators to DIALOGIC TRACE.
- Modify `skills/alex/references/evidence-model.md` — add question/response/model-delta records and typed relations.
- Modify `skills/alex/references/research-receipt.md` — add compact/full DIALOGIC TRACE receipt fields.
- Create `alex_runtime/dialogic_trace.py` — deterministic record validators and model-delta evaluator.
- Create `tests/test_dialogic_trace.py` — unit tests for lawful and hostile cases.
- Add `crucible/specimens/dialogic-*.json` — hostile constitutional specimens.
- Modify `crucible/README.md` — register the new specimen family.

---

### Task 1: Add the DIALOGIC TRACE reference mode

**Files:**
- Create: `skills/alex/references/modes/dialogic-trace.md`
- Modify: `skills/alex/SKILL.md`
- Modify: `skills/alex/references/evidence-model.md`
- Modify: `skills/alex/references/research-receipt.md`

**Interfaces:**
- Consumes: existing PRESSURE and formation-trace distinctions.
- Produces: documented records `source_question`, `source_response`, `model_delta`; relation vocabulary used by later runtime code.

- [ ] **Step 1: Write the mode document**

Create `skills/alex/references/modes/dialogic-trace.md` with these required sections and exact core loop:

```text
PUBLIC ARTIFACT
  -> ALEX READING
  -> MODEL / HYPOTHESIS
  -> PRESSURE
  -> QUESTION
  -> SOURCE RESPONSE
  -> RESPONSE CLASSIFICATION
  -> MODEL DELTA
  -> INDEPENDENT RETEST
  -> SURVIVOR / REFUSAL / OPEN
```

Require the following refusal laws verbatim:

```text
creator response != retroactive proof
creator agreement != independent corroboration
creator disagreement != automatic falsification
current stated intent != historical intent
silence != rejection
question wording != neutral observation
```

Document that a response may establish a responder's current stated position when identity/carrier conditions are sufficient, but cannot by itself establish external mathematical, historical, scientific, or genealogical claims.

- [ ] **Step 2: Route the mode from the ALEX skill**

In `skills/alex/SKILL.md`, add `DIALOGIC TRACE` to the research-shape table and a routing paragraph:

```markdown
| `DIALOGIC TRACE` | Ask a reachable living source a discriminating question after ALEX has formed and pressured a precise model; preserve the response as testimony plus a model delta, never as retroactive proof |
```

Add:

```markdown
For DIALOGIC TRACE, read [references/modes/dialogic-trace.md](references/modes/dialogic-trace.md). Prefer PRESSURE before contact so the question can discriminate between explicit live models.
```

- [ ] **Step 3: Extend the evidence model**

In `skills/alex/references/evidence-model.md`, add three rows:

```markdown
| `source_question` | Exact question, target, framing, channel, and privacy state | That the question is neutral or answered |
| `source_response` | Attributable response occurrence and bounded testimony | External truth, historical intent, or independent corroboration |
| `model_delta` | What changed in ALEX's model after a response | That the response-dependent changes survived independent retest |
```

Add relations:

```text
asks
answers
clarifies_current_position
clarifies_current_intent
disputes_our_reading
confirms_our_reading
supplies_source
supplies_counterexample
opens_discriminator
claims_historical_intent
claims_authorship
```

- [ ] **Step 4: Extend the research receipt**

Add this compact form to `skills/alex/references/research-receipt.md`:

```text
TARGET:
TARGET IDENTITY STATUS:
PUBLIC ARTIFACT:
PRE-QUESTION MODEL:
QUESTION:
LEADING-RISK:
CHANNEL:
PRIVACY / PUBLICATION BOUNDARY:
RESPONSE:
RESPONSE IDENTITY STATUS:
RESPONSE CLASS:
MODEL DELTA:
WHAT CHANGED:
WHAT DID NOT CHANGE:
RESPONSE-DEPENDENT CLAIMS:
INDEPENDENT RETEST:
RESIDUAL DISAGREEMENT:
NEXT DISCRIMINATOR:
PROMOTION: none
```

- [ ] **Step 5: Run documentation consistency checks**

Run:

```bash
python - <<'PY'
from pathlib import Path
paths = [
    Path("skills/alex/SKILL.md"),
    Path("skills/alex/references/modes/dialogic-trace.md"),
    Path("skills/alex/references/evidence-model.md"),
    Path("skills/alex/references/research-receipt.md"),
]
text = "\n".join(p.read_text(encoding="utf-8") for p in paths)
for required in [
    "creator response != retroactive proof",
    "source_question",
    "source_response",
    "model_delta",
    "DIALOGIC TRACE",
]:
    assert required in text, required
print("dialogic docs: OK")
PY
```

Expected: `dialogic docs: OK`

- [ ] **Step 6: Commit**

```bash
git add skills/alex/SKILL.md skills/alex/references/modes/dialogic-trace.md skills/alex/references/evidence-model.md skills/alex/references/research-receipt.md
git commit -m "docs: define dialogic trace"
```

---

### Task 2: Implement question and response validation

**Files:**
- Create: `alex_runtime/dialogic_trace.py`
- Create: `tests/test_dialogic_trace.py`

**Interfaces:**
- Produces:
  - `evaluate_source_question(record: object) -> dict[str, Any]`
  - `evaluate_source_response(record: object) -> dict[str, Any]`
- Receipts always contain `authority: "none"`.

- [ ] **Step 1: Write failing question tests**

Create `tests/test_dialogic_trace.py` with:

```python
import copy
import unittest

from alex_runtime.dialogic_trace import (
    evaluate_source_question,
    evaluate_source_response,
)

BASE_QUESTION = {
    "schema": "alex.source-question/v0",
    "question_id": "q-001",
    "target_ref": "person:reachable-source",
    "target_identity_status": "VERIFIED_NAMED",
    "derived_from_claim_ids": ["claim:model-001"],
    "exact_question": "Are you changing the operator, the object type, or adding a transformation?",
    "leading_risk": "LOW",
    "channel": "EMAIL",
    "visibility": "PRIVATE",
    "publication_permission": "NO",
    "status": "SENT",
}

BASE_RESPONSE = {
    "schema": "alex.source-response/v0",
    "response_id": "r-001",
    "question_id": "q-001",
    "responder_claimed_identity": "person:reachable-source",
    "responder_identity_status": "VERIFIED_NAMED",
    "channel": "EMAIL",
    "visibility": "PRIVATE",
    "quotation_permission": "NO",
    "publication_permission": "NO",
    "response_class": "CLARIFIES_CURRENT_POSITION",
    "response_reading": "I mean an additional transformation, not ordinary multiplication.",
    "carrier_ref": "sha256:" + "a" * 64,
}

class SourceQuestionTests(unittest.TestCase):
    def test_accepts_bounded_question_and_freezes_authority(self):
        result = evaluate_source_question(copy.deepcopy(BASE_QUESTION))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertEqual(result["receipt"]["exact_question"], BASE_QUESTION["exact_question"])

    def test_silence_is_not_a_response_status(self):
        record = copy.deepcopy(BASE_QUESTION)
        record["status"] = "REJECTED_BY_SILENCE"
        result = evaluate_source_question(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_question_status")

class SourceResponseTests(unittest.TestCase):
    def test_private_response_accepts_without_publication_promotion(self):
        result = evaluate_source_response(copy.deepcopy(BASE_RESPONSE))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["publication_permission"], "NO")
        self.assertEqual(result["receipt"]["authority"], "none")

    def test_response_requires_exact_question_parent(self):
        record = copy.deepcopy(BASE_RESPONSE)
        record["question_id"] = ""
        result = evaluate_source_response(record)
        self.assertEqual(result["reason"], "missing_required_field")

if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run tests to verify RED**

Run:

```bash
python -m unittest tests.test_dialogic_trace -v
```

Expected: import failure because `alex_runtime.dialogic_trace` does not yet exist.

- [ ] **Step 3: Implement minimal validators**

Create `alex_runtime/dialogic_trace.py` with constants:

```python
QUESTION_SCHEMA = "alex.source-question/v0"
QUESTION_RESULT_SCHEMA = "alex.source-question-result/v0"
RESPONSE_SCHEMA = "alex.source-response/v0"
RESPONSE_RESULT_SCHEMA = "alex.source-response-result/v0"

IDENTITY_STATUSES = frozenset({"VERIFIED_NAMED", "NAMED", "PERSISTENT_PSEUDONYM", "ONE_SHOT_ANONYMOUS", "UNKNOWN"})
LEADING_RISKS = frozenset({"LOW", "MEDIUM", "HIGH", "UNASSESSED"})
QUESTION_STATUSES = frozenset({"DRAFT", "SENT", "ANSWERED", "DECLINED", "UNANSWERED", "UNDELIVERABLE", "WITHDRAWN"})
VISIBILITIES = frozenset({"PUBLIC", "PRIVATE", "RESTRICTED"})
PERMISSIONS = frozenset({"YES", "NO", "UNRESOLVED"})
RESPONSE_CLASSES = frozenset({
    "CLARIFIES_CURRENT_POSITION",
    "CLARIFIES_CURRENT_INTENT",
    "DISPUTES_OUR_READING",
    "CONFIRMS_OUR_READING",
    "CORRECTS_FACTUAL_CLAIM",
    "SUPPLIES_SOURCE",
    "SUPPLIES_COUNTEREXAMPLE",
    "OPENS_DISCRIMINATOR",
    "REFUSES_QUESTION",
    "CLAIMS_HISTORICAL_INTENT",
    "CLAIMS_AUTHORSHIP",
    "CLAIMS_PROVENANCE",
})
```

Use `sha256_json(record)` for immutable receipt identity. Do not honor incoming `authority`.

- [ ] **Step 4: Run tests to verify GREEN**

Run:

```bash
python -m unittest tests.test_dialogic_trace -v
```

Expected: all question/response tests PASS.

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/dialogic_trace.py tests/test_dialogic_trace.py
git commit -m "feat: validate dialogic questions and responses"
```

---

### Task 3: Implement MODEL DELTA with independent-retest separation

**Files:**
- Modify: `alex_runtime/dialogic_trace.py`
- Modify: `tests/test_dialogic_trace.py`

**Interfaces:**
- Produces: `evaluate_model_delta(record: object) -> dict[str, Any]`.
- Requires exact digest refs for pre-model, response, and post-model.
- Keeps `response_dependent_claims` and `independently_retested_claims` as separate unique lists.

- [ ] **Step 1: Write failing model-delta tests**

Append:

```python
from alex_runtime.dialogic_trace import evaluate_model_delta

BASE_DELTA = {
    "schema": "alex.model-delta/v0",
    "delta_id": "delta-001",
    "pre_response_model_ref": "sha256:" + "1" * 64,
    "response_ref": "sha256:" + "2" * 64,
    "post_response_model_ref": "sha256:" + "3" * 64,
    "changed_claims": ["claim:operator-semantics"],
    "unchanged_claims": ["claim:public-artifact-wording"],
    "killed_claims": [],
    "new_questions": ["question:what-transformation"],
    "new_source_paths": [],
    "response_dependent_claims": ["claim:creator-current-position"],
    "independently_retested_claims": [],
    "residual_disagreement": [],
}

class ModelDeltaTests(unittest.TestCase):
    def test_response_dependent_claim_is_not_auto_retested(self):
        result = evaluate_model_delta(copy.deepcopy(BASE_DELTA))
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(
            result["receipt"]["response_dependent_claims"],
            ["claim:creator-current-position"],
        )
        self.assertEqual(result["receipt"]["independently_retested_claims"], [])

    def test_same_claim_cannot_be_declared_response_only_and_independently_retested(self):
        record = copy.deepcopy(BASE_DELTA)
        record["independently_retested_claims"] = ["claim:creator-current-position"]
        result = evaluate_model_delta(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "retest_status_conflict")
```

- [ ] **Step 2: Run the new tests and verify RED**

Run:

```bash
python -m unittest tests.test_dialogic_trace.ModelDeltaTests -v
```

Expected: import or missing-function failure.

- [ ] **Step 3: Implement `evaluate_model_delta`**

Add:

```python
MODEL_DELTA_SCHEMA = "alex.model-delta/v0"
MODEL_DELTA_RESULT_SCHEMA = "alex.model-delta-result/v0"
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")
```

Validation rules:

```text
- delta_id non-empty
- all three *_ref fields match SHA256_REF
- all list fields are arrays of unique non-empty strings
- response_dependent_claims ∩ independently_retested_claims must be empty
- incoming authority is discarded
```

Receipt must preserve all fields plus `delta_digest` and `authority: "none"`.

- [ ] **Step 4: Run all dialogic tests**

Run:

```bash
python -m unittest tests.test_dialogic_trace -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/dialogic_trace.py tests/test_dialogic_trace.py
git commit -m "feat: preserve dialogic model deltas"
```

---

### Task 4: Add hostile DIALOGIC TRACE Crucible specimens

**Files:**
- Create:
  - `crucible/specimens/dialogic-agreeable-author.json`
  - `crucible/specimens/dialogic-retrospective-intent.json`
  - `crucible/specimens/dialogic-authority-laundering.json`
  - `crucible/specimens/dialogic-leading-question.json`
  - `crucible/specimens/dialogic-silence.json`
  - `crucible/specimens/dialogic-private-leakage.json`
  - `crucible/specimens/dialogic-creator-veto.json`
- Modify: `crucible/README.md`

**Interfaces:**
- Consumes: existing `crucible/schema/specimen.schema.json`.
- Produces: seven schema-valid fixtures with stable refusal/acceptance expectations.

- [ ] **Step 1: Copy the existing specimen shape**

Inspect:

```bash
cat crucible/specimens/shared-lineage-corroboration.json
cat crucible/schema/specimen.schema.json
```

Use the exact existing schema fields; do not introduce a new Crucible schema.

- [ ] **Step 2: Create the agreeable-author specimen**

Its attempted promotion must encode:

```text
creator says "yes, exactly"
-> therefore interpretation is independently corroborated
```

Expected disposition: `REFUSE`.

Forbidden promotion must include `independent_corroboration`.

Required survivor must include `creator_agreement_as_testimony`.

- [ ] **Step 3: Create the remaining six fixtures**

Required hostile attempts:

```text
retrospective-intent:
current recollection -> overwrite earlier artifact

authority-laundering:
verified/credentialed creator -> all external claims true

leading-question:
question embeds preferred answer -> agreement treated as spontaneous confirmation

silence:
UNANSWERED -> rejection/agreement inference

private-leakage:
private response with publication_permission=NO -> public quotation

creator-veto:
creator disagreement -> erase independently supported artifact interpretation
```

- [ ] **Step 4: Validate Crucible fixtures**

Run:

```bash
python tools/crucible.py
```

Expected: schema validation passes and existing specimen suite remains green under its normal invocation contract.

- [ ] **Step 5: Document the family**

In `crucible/README.md`, add `dialogic-*` under specimen families with the law:

```text
living-source testimony may change the active model without rewriting earlier artifacts or becoming independent corroboration by agreement alone
```

- [ ] **Step 6: Commit**

```bash
git add crucible/specimens/dialogic-*.json crucible/README.md
git commit -m "test: add dialogic trace constitutional specimens"
```

---

### Task 5: Whole-slice verification

**Files:**
- No new files unless a failing check exposes a scoped defect.

**Interfaces:**
- Produces: verified semantic + runtime slice; no public networking or Tor endpoint.

- [ ] **Step 1: Run DIALOGIC TRACE tests**

```bash
python -m unittest tests.test_dialogic_trace -v
```

Expected: PASS.

- [ ] **Step 2: Run existing ALEX unit suite**

```bash
python -m unittest discover -s tests -v
```

Expected: all non-environmental tests PASS; tests that already require unavailable exact Chronobody materializations may SKIP for their documented reason.

- [ ] **Step 3: Validate Crucible**

```bash
python tools/crucible.py
```

Expected: all registered static specimens validate.

- [ ] **Step 4: Inspect git delta**

```bash
git status --short
git diff --check
```

Expected: clean whitespace check; only DIALOGIC TRACE files modified.

- [ ] **Step 5: Final commit if verification required fixes**

If verification produced no changes, do not create an empty commit. Otherwise:

```bash
git add <exact-fixed-files>
git commit -m "fix: harden dialogic trace verification"
```

## Completion receipt

The slice is complete when:

```text
public artifact != creator response
creator agreement != independent corroboration
current stated intent != historical intent
silence remains UNANSWERED
private response cannot become public fixture content
model delta explicitly separates response-dependent claims from independently retested claims
authority remains none
```
