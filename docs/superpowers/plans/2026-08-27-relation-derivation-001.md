# RELATION-DERIVATION-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first real ALEX semantic derivation microkernel and prove, through the Blind Crucible, that attention/discovery does not inherit evidentiary support while an attributable evidence path can earn scoped `SUPPORTS`.

**Architecture:** Add a small `alex_runtime` package containing a static predicate-minting registry and one versioned partial evaluator, `RELATION-DERIVATION-001@1`. The evaluator consumes an explicit proof-carrying relation proposal plus bounded records/relations/evidence paths, returns a scoped evaluation record, and never mints authority/admission/consequence relations. A real subprocess adapter lowers that evaluation into the existing Blind Crucible runtime-result contract, and a pinned `alex.runtime/derivation-m0` profile runs both negative and positive descendants plus metamorphic siblings.

**Tech Stack:** Python 3.12 standard library, dataclasses/plain dictionaries, JSON Schema Draft 2020-12, SHA-256 canonical JSON digests, `unittest`, subprocess CLI/JSON boundary.

**Spec:** `docs/superpowers/specs/2026-08-26-alex-loadout-runtime-boundary-design.md`, especially §§9–14.

## Global Constraints

- Preserve `crucible/specimens/attention-trace-support-independence.json` unchanged as the historical constitutional ancestor.
- Do not invent missing target-claim data inside that historical fixture. Gate 2 creates explicit descendant fixtures that preserve its law and add the relation-proposal fields required by the runtime contract.
- `SUPPORTS` is the only semantic predicate executable in `alex.runtime/derivation-m0`.
- Undefined derivation is the default. No global pairwise relation-conversion table exists.
- Mechanical/witnessed relations are not semantic conclusions merely because they are edges.
- Authority, admission, publication, merge, warrant, canon, or consequence relations are never minted by this evaluator.
- `ACCEPT` means only that the declared evaluator satisfied the declared rule for the declared scope and may emit a scoped conclusion assertion plus evaluation receipt.
- `ACCEPT != ADMITTED`; `REFUSE != ERRORED`; execution state remains a separate axis.
- Source relations and proposals are immutable inputs. Evaluation appends a result; it does not mutate the proposal.
- Use opaque proposal/evaluation/step identifiers supplied by the case. Do not use a payload hash as occurrence identity.
- `recorded_at`/persistent occurrence storage is outside Gate 2. This gate produces proof-carrying evaluation objects but does not claim an occurrence ledger exists.
- Preserve public language: `CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED` globally. Only the scoped profile `alex.runtime/derivation-m0` may be reported as passing, and only for the exact tested adapter/ruleset/profile.
- No graph database, workflow engine, dynamic policy DSL, generic truth score, automatic canon mutation, or LOADOUT implementation enters this gate.

---

## File Structure

- `alex_runtime/__init__.py` — package marker and exported Gate-2 profile constants.
- `alex_runtime/predicates.py` — static predicate minting classes and Gate-2 semantic allowlist.
- `alex_runtime/derivation.py` — `RELATION-DERIVATION-001@1` rule manifest, validation, partial evaluator, and evaluation-result construction.
- `tools/derivation_adapter.py` — real Blind Crucible subprocess adapter for `alex.runtime/derivation-m0`.
- `tools/run_derivation_profile.py` — executes the exact conformance profile, including metamorphic siblings, through the subprocess boundary.
- `crucible/schema/conformance-profile.schema.json` — narrow profile manifest contract.
- `crucible/profiles/alex.runtime.derivation-m0.json` — pinned Gate-2 profile.
- `crucible/specimens/relation-derivation-001-attention-negative.json` — explicit descendant of the historical attention fixture.
- `crucible/specimens/relation-derivation-001-evidence-positive.json` — genuine positive sibling with an attributable evidence path.
- `tests/test_derivation_predicates.py` — minting-boundary unit tests.
- `tests/test_derivation_kernel.py` — evaluator RED→GREEN tests.
- `tests/test_derivation_adapter.py` — subprocess adapter and identity/result-shape tests.
- `tests/test_derivation_profile.py` — profile-manifest and end-to-end original/metamorphic tests.
- `tests/test_crucible_contract.py` — adds the two descendant fixtures to the canonical fixture set without editing the historical ancestor.
- `tools/crucible.py` — expose exact `operation_type` and `rule_profile` into `run_fixture()`/CLI and add a reusable prepared-CASE subprocess seam.
- `tools/crucible_blind.py` — resolve the Gate-2 ruleset digest from the static rule manifest while preserving legacy `alex-crucible-v1` digest behavior.

---

## Task 1 — Static predicate-minting boundary and ruleset manifest

**Files:**
- Create: `alex_runtime/__init__.py`
- Create: `alex_runtime/predicates.py`
- Create: `alex_runtime/derivation.py`
- Create: `tests/test_derivation_predicates.py`
- Create: `tests/test_derivation_kernel.py`
- Modify: `tools/crucible_blind.py`

**Interfaces:**
- Produces: `predicate_minting_class(predicate: str) -> str | None`
- Produces: `semantic_predicate_allowed(profile: str, predicate: str) -> bool`
- Produces: `ruleset_manifest(profile: str) -> dict | None`
- Produces: `ruleset_manifest_digest(profile: str) -> str | None`
- Produces: `evaluate_relation_case(case: dict) -> dict`
- Preserves: `tools.crucible_blind.ruleset_digest(rule_profile: str) -> str`

The static registry for this gate is:

```python
MECHANICAL_PREDICATES = {
    "caused_by",
    "input_of",
    "output_of",
    "derived_from",
    "exact_transform_of",
    "targets",
    "acquired_from",
}

SEMANTIC_PREDICATES = {"SUPPORTS"}

MINTING_MECHANICAL = "MECHANICAL_WITNESSED"
MINTING_SEMANTIC = "SEMANTIC_EVALUATED"
```

Unknown predicates return `None`; they are not silently classified. Gate 2 does not invent exact authority-predicate spellings merely to populate a denylist: the semantic evaluator is positively allowlisted to `SUPPORTS`, so every non-`SUPPORTS` proposal is outside the profile.

The exact ruleset manifest is:

```python
DERIVATION_M0_MANIFEST = {
    "profile": "alex.runtime/derivation-m0",
    "rules": [
        {
            "rule_id": "RELATION-DERIVATION-001",
            "rule_version": 1,
            "predicate": "SUPPORTS",
            "negative_reason_code": "ATTENTION_NOT_SUPPORT",
            "undefined_reason_code": "NO_ATTRIBUTABLE_SUPPORT_PATH",
        }
    ],
}
```

- [ ] **Step 1: Write failing predicate-boundary tests**

Create `tests/test_derivation_predicates.py` with tests equivalent to:

```python
import unittest
from alex_runtime.predicates import predicate_minting_class, semantic_predicate_allowed


class PredicateMintingTests(unittest.TestCase):
    def test_mechanical_relation_is_not_semantic(self):
        self.assertEqual(predicate_minting_class("derived_from"), "MECHANICAL_WITNESSED")
        self.assertFalse(semantic_predicate_allowed("alex.runtime/derivation-m0", "derived_from"))

    def test_supports_is_the_only_m0_semantic_predicate(self):
        self.assertEqual(predicate_minting_class("SUPPORTS"), "SEMANTIC_EVALUATED")
        self.assertTrue(semantic_predicate_allowed("alex.runtime/derivation-m0", "SUPPORTS"))
        self.assertFalse(semantic_predicate_allowed("alex.runtime/derivation-m0", "RESEMBLES"))

    def test_unknown_predicate_is_not_silently_classified(self):
        self.assertIsNone(predicate_minting_class("MAGICALLY_AUTHORIZES"))
```

- [ ] **Step 2: Write failing ruleset-manifest tests**

Add to `tests/test_derivation_kernel.py`:

```python
import unittest
from alex_runtime.derivation import ruleset_manifest, ruleset_manifest_digest


class RulesetManifestTests(unittest.TestCase):
    def test_derivation_m0_manifest_pins_rule_and_version(self):
        manifest = ruleset_manifest("alex.runtime/derivation-m0")
        self.assertEqual(manifest["profile"], "alex.runtime/derivation-m0")
        self.assertEqual(manifest["rules"][0]["rule_id"], "RELATION-DERIVATION-001")
        self.assertEqual(manifest["rules"][0]["rule_version"], 1)
        self.assertEqual(manifest["rules"][0]["predicate"], "SUPPORTS")

    def test_ruleset_digest_changes_if_manifest_changes(self):
        digest = ruleset_manifest_digest("alex.runtime/derivation-m0")
        self.assertTrue(digest.startswith("sha256:"))
        self.assertEqual(len(digest), 71)
```

- [ ] **Step 3: Run focused tests and confirm RED**

Run:

```bash
python -m unittest tests.test_derivation_predicates tests.test_derivation_kernel -v
```

Expected: FAIL because `alex_runtime` and the Gate-2 functions do not exist.

- [ ] **Step 4: Implement the minimum package/registry/manifest**

`alex_runtime/predicates.py` implements the exact static sets above and no dynamic registration API.

`alex_runtime/derivation.py` exposes the exact immutable manifest via a deep copy and computes its digest with canonical JSON:

```python
import copy
from tools.crucible_blind import sha256_json


def ruleset_manifest(profile: str) -> dict | None:
    if profile != "alex.runtime/derivation-m0":
        return None
    return copy.deepcopy(DERIVATION_M0_MANIFEST)


def ruleset_manifest_digest(profile: str) -> str | None:
    manifest = ruleset_manifest(profile)
    return None if manifest is None else sha256_json(manifest)
```

Avoid a circular import by moving canonical JSON helpers to a dependency-neutral location if required. The preferred minimal move is `alex_runtime/digests.py` containing `canonical_json_bytes()` and `sha256_json()`, imported by both `tools/crucible_blind.py` and `alex_runtime/derivation.py`. If that move is necessary, update the existing Blind Crucible tests to prove digest behavior is unchanged.

- [ ] **Step 5: Make `ruleset_digest()` manifest-aware without breaking Gate 1**

`tools.crucible_blind.ruleset_digest(profile)` must behave as follows:

```python
def ruleset_digest(rule_profile: str) -> str:
    manifest = ruleset_manifest(rule_profile)
    if manifest is not None:
        return sha256_json(manifest)
    return sha256_json({"rule_profile": rule_profile})
```

This preserves legacy `alex-crucible-v1` behavior while making `alex.runtime/derivation-m0` pin actual rule content.

- [ ] **Step 6: Run focused and legacy digest tests GREEN**

Run:

```bash
python -m unittest tests.test_derivation_predicates tests.test_derivation_kernel tests.test_crucible_blind -v
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add alex_runtime tools/crucible_blind.py tests/test_derivation_predicates.py tests/test_derivation_kernel.py
git commit -m "feat: define derivation predicate boundary"
```

---

## Task 2 — Implement `RELATION-DERIVATION-001@1` as a partial proof-carrying evaluator

**Files:**
- Modify: `alex_runtime/derivation.py`
- Modify: `tests/test_derivation_kernel.py`
- Create: `crucible/specimens/relation-derivation-001-attention-negative.json`
- Create: `crucible/specimens/relation-derivation-001-evidence-positive.json`
- Modify: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: a Blind Crucible CASE with `operation_type == "relation_derivation"`, `rule_profile == "alex.runtime/derivation-m0"`, `given.records`, `given.relations`, `given.evidence_paths`, and `attempt.relation_proposal`.
- Produces: `evaluate_relation_case(case: dict) -> dict` containing `proposal`, `evaluation`, `conclusion_assertion`, and `execution`.

### Exact Gate-2 case shape

Both descendant fixtures lower into CASE objects whose runtime-visible payload has this structure:

```json
{
  "given": {
    "records": [
      {"id": "B1", "kind": "breadcrumb"},
      {"id": "Q1", "kind": "search"},
      {"id": "E1", "kind": "evidence"},
      {"id": "C1", "kind": "candidate_claim"}
    ],
    "relations": [
      {"id": "R1", "subject_id": "B1", "predicate": "caused_by", "object_id": "Q1", "direction_note": "Q1 caused_by B1"},
      {"id": "R2", "subject_id": "E1", "predicate": "acquired_from", "object_id": "Q1", "direction_note": "E1 acquired_from search Q1"}
    ],
    "evidence_paths": []
  },
  "attempt": {
    "relation_proposal": {
      "id": "RP1",
      "subject_id": "B1",
      "predicate": "SUPPORTS",
      "object_id": "C1",
      "scope": "candidate_claim:C1",
      "proposed_by": "crucible-fixture",
      "basis_ids": ["B1", "Q1", "E1"]
    },
    "evaluation_id": "EV1",
    "execution_step_id": "STEP1"
  }
}
```

The positive fixture changes the proposal subject to `E1` and adds:

```json
{
  "id": "EP1",
  "source_id": "E1",
  "claim_id": "C1",
  "basis_ids": ["E1"],
  "witness_ids": ["independent_source:S1"],
  "status": "ATTRIBUTABLE"
}
```

to `given.evidence_paths`.

The awkward `direction_note` field is forbidden in the actual fixture; it appears only in this explanatory example. Actual relation records use only `id`, `subject_id`, `predicate`, and `object_id`, with `Q1 --caused_by--> B1` represented as `{"subject_id":"Q1","predicate":"caused_by","object_id":"B1"}`.

### Evaluator outcomes

The evaluator follows this order:

1. If `operation_type != "relation_derivation"`, return execution `FINISHED`, disposition `INSUFFICIENT_TO_TEST`, reason `OPERATION_OUTSIDE_PROFILE`, no conclusion.
2. If the proposal predicate is not positively allowed for `alex.runtime/derivation-m0`, return `REFUSE`, reason `PREDICATE_OUTSIDE_PROFILE`, no conclusion.
3. Validate proposal subject/object IDs exist in `given.records`; missing IDs return `INSUFFICIENT_TO_TEST`, reason `MISSING_PROPOSAL_RECORD`.
4. Find an attributable evidence path where `source_id == proposal.subject_id`, `claim_id == proposal.object_id`, `status == "ATTRIBUTABLE"`, `witness_ids` is non-empty, and every `basis_id` exists. If found, return `ACCEPT` and append exactly one scoped conclusion assertion.
5. Otherwise, if the proposal subject is a `breadcrumb` and there is a witnessed path `search --caused_by--> breadcrumb` plus `evidence --acquired_from--> search`, return `REFUSE`, reason `ATTENTION_NOT_SUPPORT`.
6. Otherwise return `INSUFFICIENT_TO_TEST`, reason `NO_ATTRIBUTABLE_SUPPORT_PATH`.

No transitive graph closure is performed. No resemblance, motivation, genealogy, authority, or admission inference is attempted.

The returned evaluation object is:

```python
{
    "proposal_id": "RP1",
    "evaluation_id": "EV1",
    "rule_id": "RELATION-DERIVATION-001",
    "rule_version": 1,
    "ruleset_digest": ruleset_manifest_digest("alex.runtime/derivation-m0"),
    "input_ids": [...],
    "input_digest": case["input_digest"],
    "execution_step_id": "STEP1",
    "disposition": "ACCEPT | REFUSE | INSUFFICIENT_TO_TEST",
    "reason_code": "...",
    "required_survivors": [...],
    "conclusion_assertion_id": "AS1" or None,
    "residual_fog": [...],
}
```

The accepted conclusion assertion is:

```python
{
    "id": "AS1",
    "subject_id": proposal["subject_id"],
    "predicate": "SUPPORTS",
    "object_id": proposal["object_id"],
    "scope": proposal["scope"],
    "derived_by_evaluation_id": "EV1",
}
```

- [ ] **Step 1: Add the explicit negative descendant fixture**

Create `crucible/specimens/relation-derivation-001-attention-negative.json` with:

```json
{
  "id": "relation-derivation-001-attention-negative",
  "title": "Attention/discovery ancestry does not grant support",
  "constitutional_laws": [
    "DISCOVERY PATH != EVIDENCE PATH",
    "BREADCRUMB != EVIDENCE",
    "SEARCH MOTIVE != SUPPORT WEIGHT"
  ],
  "given": {
    "records": [
      {"id": "B1", "kind": "breadcrumb"},
      {"id": "Q1", "kind": "search"},
      {"id": "E1", "kind": "evidence"},
      {"id": "C1", "kind": "candidate_claim"}
    ],
    "relations": [
      {"id": "R1", "subject_id": "Q1", "predicate": "caused_by", "object_id": "B1"},
      {"id": "R2", "subject_id": "E1", "predicate": "acquired_from", "object_id": "Q1"}
    ],
    "evidence_paths": []
  },
  "attempt": {
    "relation_proposal": {
      "id": "RP1",
      "subject_id": "B1",
      "predicate": "SUPPORTS",
      "object_id": "C1",
      "scope": "candidate_claim:C1",
      "proposed_by": "crucible-fixture",
      "basis_ids": ["B1", "Q1", "E1"]
    },
    "evaluation_id": "EV1",
    "execution_step_id": "STEP1",
    "conclusion_assertion_id": "AS1"
  },
  "expected": {
    "disposition": "REFUSE",
    "refusal_code": "ATTENTION_NOT_SUPPORT",
    "required_receipt_survivors": [
      "record:B1",
      "record:Q1",
      "record:E1",
      "record:C1",
      "relation_proposal:RP1",
      "evaluation:EV1"
    ],
    "forbidden_promotions": ["B1 --SUPPORTS--> C1"]
  },
  "notes": "Runtime descendant of attention-trace-support-independence. The historical fixture remains unchanged; this descendant adds the explicit candidate claim and proof-carrying proposal required by RELATION-DERIVATION-001.",
  "version": 1
}
```

- [ ] **Step 2: Add the genuine positive sibling fixture**

Create `crucible/specimens/relation-derivation-001-evidence-positive.json` with the same records and mechanical relations, plus `evidence_paths:[EP1]`, proposal subject `E1`, basis `E1,EP1`, and expected:

```json
{
  "disposition": "ACCEPT",
  "required_receipt_survivors": [
    "record:E1",
    "record:C1",
    "evidence_path:EP1",
    "relation_proposal:RP1",
    "evaluation:EV1",
    "conclusion_assertion:AS1"
  ],
  "forbidden_promotions": []
}
```

The positive fixture omits `refusal_code`; Blind Crucible ORACLE therefore expects `reason_code: null`.

- [ ] **Step 3: Extend canonical-corpus test without touching the ancestor**

Add only the two new filenames to `expected_names` in `tests/test_crucible_contract.py`. Add a regression test that reads `attention-trace-support-independence.json` and asserts its SHA-sensitive semantic shape remains historical: it still contains `given.breadcrumb`, `given.search`, `given.evidence`, and does not contain `given.records` or `attempt.relation_proposal`.

- [ ] **Step 4: Write evaluator RED tests**

Add tests in `tests/test_derivation_kernel.py` for:

```python
def test_attention_chain_refuses_support(): ...
def test_attributable_evidence_path_accepts_support(): ...
def test_missing_evidence_path_is_insufficient_when_not_attention_case(): ...
def test_non_supports_predicate_is_outside_profile(): ...
def test_accept_does_not_emit_admission_state(): ...
def test_source_case_is_not_mutated(): ...
```

`test_accept_does_not_emit_admission_state` must assert neither the evaluation nor conclusion contains `admitted`, `authority`, `canon`, `publication`, or `warrant` keys.

- [ ] **Step 5: Run Task-2 tests RED**

Run:

```bash
python -m unittest tests.test_derivation_kernel tests.test_crucible_contract -v
```

Expected: FAIL because the evaluator and/or new fixtures are not implemented yet.

- [ ] **Step 6: Implement the minimum partial evaluator**

Implement exact-match helper functions in `alex_runtime/derivation.py`; do not add generic graph traversal. Deep-copy proposal/inputs before returning output so caller-owned CASE data cannot be mutated.

- [ ] **Step 7: Run Task-2 tests GREEN**

Run:

```bash
python -m unittest tests.test_derivation_kernel tests.test_crucible_contract -v
```

Expected: PASS.

- [ ] **Step 8: Commit**

```bash
git add alex_runtime/derivation.py crucible/specimens tests/test_derivation_kernel.py tests/test_crucible_contract.py
git commit -m "feat: add first proof-carrying relation derivation"
```

---

## Task 3 — Real Blind Crucible adapter and prepared-CASE execution seam

**Files:**
- Create: `tools/derivation_adapter.py`
- Modify: `tools/crucible.py`
- Create: `tests/test_derivation_adapter.py`
- Modify: `tests/test_crucible_runner.py`

**Interfaces:**
- Produces: `tools.derivation_adapter.runtime_result_from_case(case: dict) -> dict`
- Produces: `tools.crucible.run_case(case: dict, oracle: dict, adapter_argv: list[str]) -> int`
- Extends: `run_fixture(..., operation_type: str = "constitutional_evaluation", rule_profile: str = "alex-crucible-v1")`
- CLI adds: `--operation-type` and `--rule-profile` before `--adapter`.

The adapter maps the microkernel result into the existing runtime-result contract:

```python
{
    "case_id": case["case_id"],
    "input_digest": case["input_digest"],
    "ruleset_digest": evaluation["ruleset_digest"],
    "disposition": evaluation["disposition"],
    "reason_code": None if evaluation["disposition"] == "ACCEPT" else evaluation["reason_code"],
    "receipt_survivors": evaluation["required_survivors"],
    "derived_assertions": [] if conclusion is None else [
        f'{conclusion["subject_id"]} --{conclusion["predicate"]}--> {conclusion["object_id"]}'
    ],
    "execution_trace_summary": {
        "terminal_state": "FINISHED",
        "step_count": 1
    }
}
```

- [ ] **Step 1: Write adapter process RED tests**

`tests/test_derivation_adapter.py` must subprocess-run `tools/crucible.py` against each new fixture using:

```bash
python tools/crucible.py \
  --fixture crucible/specimens/relation-derivation-001-attention-negative.json \
  --operation-type relation_derivation \
  --rule-profile alex.runtime/derivation-m0 \
  --adapter python tools/derivation_adapter.py
```

and the positive fixture equivalent. Both must be expected to exit `0`; tests are RED before the CLI/adapter exist.

- [ ] **Step 2: Add runner API regression tests**

In `tests/test_crucible_runner.py`, assert:

```python
case = build_case(specimen, nonce="n", operation_type="relation_derivation", rule_profile="alex.runtime/derivation-m0")
oracle = build_oracle(specimen, case)
self.assertEqual(run_case(case, oracle, correct_adapter_argv), 0)
```

Also assert `run_fixture()` forwards explicit `operation_type`/`rule_profile` instead of silently using Gate-1 defaults.

- [ ] **Step 3: Run adapter tests RED**

Run:

```bash
python -m unittest tests.test_derivation_adapter tests.test_crucible_runner -v
```

Expected: FAIL because the adapter, CLI flags, and prepared-CASE seam do not exist.

- [ ] **Step 4: Refactor the Blind Crucible runner minimally**

Extract subprocess execution/validation/scoring from `run_fixture()` into `run_case()`. `run_fixture()` remains responsible only for reading the canonical specimen, building CASE/ORACLE, and delegating.

Add `operation_type` and `rule_profile` parameters to `run_fixture()` and matching CLI options. Preserve all existing Gate-1 defaults and tests.

- [ ] **Step 5: Implement the real derivation adapter**

`tools/derivation_adapter.py` reads exactly one CASE JSON object from stdin, refuses non-object input with non-zero exit, calls `evaluate_relation_case()`, writes exactly one runtime-result JSON object to stdout, and writes diagnostics only to stderr.

The adapter must not read the fixture filesystem, ORACLE, GitHub, or environment variables to determine an expected result.

- [ ] **Step 6: Run focused adapter/runner tests GREEN**

Run:

```bash
python -m unittest tests.test_derivation_adapter tests.test_crucible_runner tests.test_crucible_blind -v
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add tools/derivation_adapter.py tools/crucible.py tests/test_derivation_adapter.py tests/test_crucible_runner.py
git commit -m "feat: run derivation through blind adapter"
```

---

## Task 4 — Pin and execute `alex.runtime/derivation-m0` with metamorphic siblings

**Files:**
- Create: `crucible/schema/conformance-profile.schema.json`
- Create: `crucible/profiles/alex.runtime.derivation-m0.json`
- Create: `tools/run_derivation_profile.py`
- Create: `tests/test_derivation_profile.py`
- Modify: `crucible/README.md`

**Interfaces:**
- Produces CLI: `python tools/run_derivation_profile.py`
- Exit `0`: every original and metamorphic case in the exact profile passed.
- Exit non-zero: at least one case failed identity, runtime-result validation, ORACLE comparison, or expected semantic invariance.

### Profile manifest

The profile JSON is exactly:

```json
{
  "$schema": "https://the-static-collective.invalid/alex/crucible/conformance-profile.schema.json",
  "id": "alex.runtime/derivation-m0",
  "operation_types": ["relation_derivation"],
  "rule_profile": "alex.runtime/derivation-m0",
  "fixture_families": [
    {
      "id": "RELATION-DERIVATION-001",
      "version": 1,
      "fixtures": [
        "relation-derivation-001-attention-negative",
        "relation-derivation-001-evidence-positive"
      ]
    }
  ],
  "runtime_adapter": {
    "path": "tools/derivation_adapter.py",
    "version": 1
  },
  "excluded_profiles": ["alex.runtime/one-book-m1", "alex.runtime/formation-trace-m2"]
}
```

Do not store a hand-copied digest in the manifest. The runner computes the ruleset digest from the versioned static manifest and prints it in the profile receipt, avoiding a second manually synchronized source of truth.

### Metamorphic pressure

For each original fixture:

1. Build a CASE with nonce `profile-original-<fixture-id>`.
2. Build its ORACLE.
3. Run the original through `run_case()` and the real adapter.
4. Create `metamorphic_sibling()` with:
   - suffix `-meta`;
   - nonce `profile-meta-<fixture-id>`;
   - reversed `given.relations` order;
   - distractor relation `{"id":"RD","subject_id":"D1","predicate":"derived_from","object_id":"D0"}`.
5. Before adding the distractor, add records `D0` and `D1` to the sibling's `given.records`; the distractor must remain irrelevant to the proposal and evidence path.
6. Update the sibling ORACLE `case_id` only; expected disposition/reason/survivors/forbidden outputs remain identical.
7. Run the sibling through the same subprocess adapter.

The profile runner prints one deterministic summary object after all cases:

```json
{
  "profile": "alex.runtime/derivation-m0",
  "ruleset_digest": "sha256:...",
  "runtime_adapter": "tools/derivation_adapter.py@1",
  "families": {"RELATION-DERIVATION-001": 4},
  "passed": 4,
  "failed": 0
}
```

The four executions are negative-original, negative-meta, positive-original, positive-meta.

- [ ] **Step 1: Write profile-schema and manifest RED tests**

`tests/test_derivation_profile.py` asserts the profile file exists, pins only `relation_derivation`, contains exactly the two fixture IDs, adapter version `1`, and excludes one-book/formation-trace profiles.

- [ ] **Step 2: Write metamorphic end-to-end RED test**

Subprocess-run `python tools/run_derivation_profile.py`; expect exit `0`, `failed == 0`, `passed == 4`, and an exact current `ruleset_digest`. This test is RED before the runner exists.

- [ ] **Step 3: Run profile tests RED**

Run:

```bash
python -m unittest tests.test_derivation_profile -v
```

Expected: FAIL because profile contract/runner do not exist.

- [ ] **Step 4: Implement the profile schema/manifest and runner**

Use only standard library. The runner imports profile data, fixture JSON, `build_case`, `build_oracle`, `metamorphic_sibling`, `ruleset_digest`, and `run_case`; it does not duplicate evaluator semantics.

When mutating the prepared sibling to add distractor records, recompute `input_digest` after all sibling changes with `sha256_json()`.

- [ ] **Step 5: Update Crucible README with scoped claim language**

Add a Gate-2 section that says, substantively:

```text
`alex.runtime/derivation-m0` is a scoped executable conformance profile for the exact derivation adapter/ruleset tested here. A passing run proves only that build/profile survived RELATION-DERIVATION-001 original and metamorphic cases. It does not establish general ALEX runtime conformance, source truth, canon, authority, admission, or consequence.
```

Keep the existing all-caps global non-conformance warning intact.

- [ ] **Step 6: Run the complete suite and explicit profile**

Run:

```bash
python -m unittest discover -s tests -v
python tools/run_derivation_profile.py
```

Expected: unittest exit `0`; profile exit `0`; summary reports `passed: 4`, `failed: 0`.

- [ ] **Step 7: Commit**

```bash
git add crucible/schema/conformance-profile.schema.json crucible/profiles tools/run_derivation_profile.py tests/test_derivation_profile.py crucible/README.md
git commit -m "feat: prove derivation m0 profile"
```

---

## Task 5 — Final pressure and PR readiness

**Files:**
- Review all Gate-2 changed files only.
- No new implementation scope unless a failing verification or review finding requires a targeted regression.

- [ ] **Step 1: Verify the historical ancestor is unchanged**

Compare `crucible/specimens/attention-trace-support-independence.json` on the branch to `main`; expected: byte-identical/no diff.

- [ ] **Step 2: Verify no authority/admission vocabulary leaked into outputs**

Search changed runtime code for output keys matching `admitted`, `authority`, `canon`, `publish`, `merge`, `warrant`. Any such result-producing key is a blocker unless it appears only in an explicit refusal/negative test assertion.

- [ ] **Step 3: Run fresh full verification**

Run:

```bash
python -m unittest discover -s tests -v
python tools/run_derivation_profile.py
```

Expected: both exit `0`; profile reports exactly four passing executions.

- [ ] **Step 4: Diff audit**

Confirm changed files are limited to the Gate-2 plan, `alex_runtime`, Gate-2 fixtures/profile/schema, Crucible runner/README, adapter/profile tools, and Gate-2 tests. No LOADOUT, one-book, Desk/MCP, GitBook, external admission, or corpus-ingestion implementation belongs in this PR.

- [ ] **Step 5: Request code review**

Review against:

```text
BASE: main at branch fork
HEAD: Gate-2 feature head
Requirements: §§9–14 of the merged runtime-boundary design + this plan
```

Fix every Critical or Important finding with a preserved failing regression before proceeding.

- [ ] **Step 6: Mark PR ready only after final green**

The PR body must report:

- exact ruleset/profile/adapter identity;
- preserved RED→GREEN receipts;
- historical ancestor unchanged;
- negative + positive + metamorphic results;
- explicit exclusions;
- `CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED` globally.

Do not merge without a separate human merge instruction.
