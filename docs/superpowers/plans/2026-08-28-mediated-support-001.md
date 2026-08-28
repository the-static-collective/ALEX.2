# MEDIATED-SUPPORT-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one pure ALEX evaluator that proves interest/selection may lawfully change support only through changed evidence, while any direct interest-to-support effect with the evidence basis held fixed is refused.

**Architecture:** `MEDIATED-SUPPORT-001` is a comparison wrapper over the existing `RELATION-DERIVATION-001` evaluator. It does not change Gate-2 support semantics, invent LOADOUT selection semantics, or duplicate 3rdi projection semantics. Each side supplies an already-attributable projection/context witness, interest/selection formation receipts, and an ordinary ALEX relation-derivation case; the wrapper evaluates both derivations, derives a semantic support signature and evidence-basis digest, then classifies the pair as direct-effect-zero, lawful mediation, semantic inflation, or insufficient to test.

**Tech Stack:** Python 3.12 standard library, `unittest`, immutable JSON fixtures, existing `alex_runtime.derivation.evaluate_relation_case`, existing `alex_runtime.digests.sha256_json`.

**Spec:** `docs/superpowers/specs/2026-08-28-mediated-support-counterfactual-rectangle-design.md`

## Global Constraints

- Implement `MEDIATED-SUPPORT-001` only. Do not implement `COUNTERFACTUAL-RECTANGLE-001` in this plan.
- Do not modify `RELATION-DERIVATION-001` semantics unless a failing hostile test proves the wrapper cannot express the contract compositionally.
- Do not import or reimplement LOADOUT or 3rdi kernels. Context, projection, selector, and consumption fields are attributable testimony consumed by ALEX, not ALEX-owned world semantics.
- `interest != evidence != support != authority` remains hard law.
- Selection/interest/consumption receipt references may survive as formation provenance but may not appear in the semantic support basis.
- A support difference is lawful only when the evaluated evidence basis differs and the change is attributable through a declared selector/consumption path.
- With the evaluated evidence basis fixed, a semantic support difference is `REFUSE / INTEREST_AS_SUPPORT`.
- Object-local evidence must not be weakened merely because interest guided discovery.
- Population/generalization comparison requires attributable selection formation; if it is stripped, return `INSUFFICIENT_TO_TEST / SELECTION_FORMATION_REQUIRED`. Do not build a statistical sampling engine.
- Result identity must preserve `case_id`, `claim_id`, projection/context identities, evidence-basis digests, support-result digests, formation receipt survivors, and reason/disposition.
- No result may emit canon, admission, publication, warrant, permission, or execution-authority state.
- Failed hostile controls remain committed alongside passing controls.
- Fixtures live under `tests/fixtures/mediated_support/`; do not expand the closed generic `crucible/specimens/` schema for this cross-run evaluator.

---

## File Structure

- Create `alex_runtime/mediated_support.py` — pure pair evaluator; the only new runtime module.
- Create `tests/fixtures/mediated_support/mediated-support-001.json` — stable neutral pair metadata for the direct-effect-zero control.
- Create `tests/test_mediated_support.py` — fixture materialization, hostile mutations, and all evaluator tests.
- Modify `crucible/README.md` — bounded conformance claim and explicit non-claims.
- Do not modify `alex_runtime/derivation.py`, `alex_runtime/projection_invariance.py`, or `alex_runtime/projection_break.py` in the first implementation.

The public interface is exactly:

```python
def evaluate_mediated_support_case(case: dict) -> dict[str, Any]:
    ...
```

The initial input shape is:

```python
{
    "case_id": "mediated-support-direct-zero",
    "claim_id": "C1",
    "claim_class": "OBJECT_LOCAL",  # or POPULATION_GENERALIZATION
    "left": {
        "projection_digest": "sha256:projection-shared",
        "bounded_context_digest": "sha256:context-shared",
        "interest_receipt_refs": [],
        "selection": {
            "policy_digest": "sha256:broad-policy-v1",
            "receipt_refs": ["selection:broad-left"],
            "consumed_interest_receipt_refs": [],
        },
        "derivation_case": {...},
    },
    "right": {
        "projection_digest": "sha256:projection-shared",
        "bounded_context_digest": "sha256:context-shared",
        "interest_receipt_refs": ["interest:q"],
        "selection": {
            "policy_digest": "sha256:broad-policy-v1",
            "receipt_refs": ["selection:broad-right"],
            "consumed_interest_receipt_refs": [],
        },
        "derivation_case": {...},
    },
}
```

The initial result shape is:

```python
{
    "case_id": "mediated-support-direct-zero",
    "claim_id": "C1",
    "disposition": "ACCEPT",
    "reason_code": None,
    "mediation_status": "DIRECT_EFFECT_ZERO",
    "support_changed": False,
    "left": {
        "projection_digest": "sha256:projection-shared",
        "bounded_context_digest": "sha256:context-shared",
        "evidence_basis_digest": "sha256:...",
        "support_result_digest": "sha256:...",
    },
    "right": {
        "projection_digest": "sha256:projection-shared",
        "bounded_context_digest": "sha256:context-shared",
        "evidence_basis_digest": "sha256:...",
        "support_result_digest": "sha256:...",
    },
    "receipt_survivors": [...],
}
```

`mediation_status` is one of:

```text
DIRECT_EFFECT_ZERO
LAWFUL_MEDIATION
null
```

No additional ontology enum is introduced.

---

### Task 1: Freeze the neutral pair and RED contract

**Files:**
- Create: `tests/fixtures/mediated_support/mediated-support-001.json`
- Create: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: existing `crucible/specimens/relation-derivation-001-evidence-positive.json` through the same `build_case()` test helper already used by `tests/test_derivation_kernel.py`.
- Produces: failing imports/tests for `evaluate_mediated_support_case(case: dict) -> dict[str, Any]`.

- [ ] **Step 1: Create the neutral pair fixture.**

Write `tests/fixtures/mediated_support/mediated-support-001.json` exactly with pair metadata; the test helper will materialize each `derivation_fixture` into a normal Gate-2 CASE:

```json
{
  "case_id": "mediated-support-direct-zero",
  "claim_id": "C1",
  "claim_class": "OBJECT_LOCAL",
  "left": {
    "projection_digest": "sha256:projection-shared",
    "bounded_context_digest": "sha256:context-shared",
    "interest_receipt_refs": [],
    "selection": {
      "policy_digest": "sha256:broad-policy-v1",
      "receipt_refs": ["selection:broad-left"],
      "consumed_interest_receipt_refs": []
    },
    "derivation_fixture": "relation-derivation-001-evidence-positive.json"
  },
  "right": {
    "projection_digest": "sha256:projection-shared",
    "bounded_context_digest": "sha256:context-shared",
    "interest_receipt_refs": ["interest:q"],
    "selection": {
      "policy_digest": "sha256:broad-policy-v1",
      "receipt_refs": ["selection:broad-right"],
      "consumed_interest_receipt_refs": []
    },
    "derivation_fixture": "relation-derivation-001-evidence-positive.json"
  }
}
```

- [ ] **Step 2: Add exact fixture materialization helpers to `tests/test_mediated_support.py`.**

```python
import copy
import json
import unittest
from pathlib import Path

from alex_runtime.mediated_support import evaluate_mediated_support_case
from tools.crucible_blind import build_case

ROOT = Path(__file__).resolve().parents[1]
PAIR_FIXTURES = ROOT / "tests" / "fixtures" / "mediated_support"
DERIVATION_SPECIMENS = ROOT / "crucible" / "specimens"


def load_derivation_case(name: str, nonce: str) -> dict:
    specimen = json.loads((DERIVATION_SPECIMENS / name).read_text(encoding="utf-8"))
    return build_case(
        specimen,
        nonce=nonce,
        operation_type="relation_derivation",
        rule_profile="alex.runtime/derivation-m0",
    )


def load_pair() -> dict:
    pair = json.loads((PAIR_FIXTURES / "mediated-support-001.json").read_text(encoding="utf-8"))
    for side_name in ("left", "right"):
        side = pair[side_name]
        fixture = side.pop("derivation_fixture")
        side["derivation_case"] = load_derivation_case(fixture, nonce=f"mediated-{side_name}")
    return pair
```

- [ ] **Step 3: Add the first direct-effect-zero test.**

```python
class MediatedSupportTests(unittest.TestCase):
    def test_interest_difference_with_fixed_evidence_has_zero_direct_support_effect(self):
        result = evaluate_mediated_support_case(load_pair())

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["mediation_status"], "DIRECT_EFFECT_ZERO")
        self.assertFalse(result["support_changed"])
        self.assertEqual(
            result["left"]["evidence_basis_digest"],
            result["right"]["evidence_basis_digest"],
        )
        self.assertEqual(
            result["left"]["support_result_digest"],
            result["right"]["support_result_digest"],
        )
```

- [ ] **Step 4: Add RED tests for immutability, no authority surface, malformed side, and claim identity.**

```python
    def test_evaluator_does_not_mutate_source_case(self):
        case = load_pair()
        before = copy.deepcopy(case)
        evaluate_mediated_support_case(case)
        self.assertEqual(case, before)

    def test_result_carries_no_external_authority_surface(self):
        result = evaluate_mediated_support_case(load_pair())
        forbidden = {"authority", "admitted", "canon", "publication", "warrant", "execution_authority"}
        self.assertTrue(forbidden.isdisjoint(result))

    def test_claim_identity_must_match_both_derivation_cases(self):
        case = load_pair()
        case["right"]["derivation_case"]["attempt"]["relation_proposal"]["object_id"] = "OTHER"
        result = evaluate_mediated_support_case(case)
        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "CLAIM_ID_MISMATCH")
```

- [ ] **Step 5: Run only the new test file and verify RED.**

Run:

```bash
python -m unittest tests.test_mediated_support -v
```

Expected: import failure for `alex_runtime.mediated_support` while the existing suite remains untouched.

- [ ] **Step 6: Commit the RED contract.**

```bash
git add tests/fixtures/mediated_support/mediated-support-001.json tests/test_mediated_support.py
git commit -m "test: freeze mediated support hostile contract"
```

---

### Task 2: Implement direct-effect-zero and semantic-inflation refusal

**Files:**
- Create: `alex_runtime/mediated_support.py`
- Test: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: two ordinary `RELATION-DERIVATION-001` CASE objects plus pair-level formation testimony.
- Produces: deterministic pair comparison with evidence-basis and semantic-support digests.

- [ ] **Step 1: Add the minimal module skeleton and structural validators.**

Start with:

```python
from __future__ import annotations

import copy
from typing import Any

from alex_runtime.derivation import evaluate_relation_case
from alex_runtime.digests import sha256_json

MEDIATED_SUPPORT_RULE_ID = "MEDIATED-SUPPORT-001"
_ALLOWED_CLAIM_CLASSES = {"OBJECT_LOCAL", "POPULATION_GENERALIZATION"}


def _string_list(value: Any) -> list[str] | None:
    if not isinstance(value, list):
        return None
    if any(not isinstance(item, str) or not item for item in value):
        return None
    if len(value) != len(set(value)):
        return None
    return list(value)


def _valid_side(side: Any) -> bool:
    if not isinstance(side, dict):
        return False
    if not isinstance(side.get("projection_digest"), str) or not side["projection_digest"]:
        return False
    if not isinstance(side.get("bounded_context_digest"), str) or not side["bounded_context_digest"]:
        return False
    if _string_list(side.get("interest_receipt_refs")) is None:
        return False
    selection = side.get("selection")
    if not isinstance(selection, dict):
        return False
    if selection.get("policy_digest") is not None and (
        not isinstance(selection["policy_digest"], str) or not selection["policy_digest"]
    ):
        return False
    if _string_list(selection.get("receipt_refs")) is None:
        return False
    if _string_list(selection.get("consumed_interest_receipt_refs")) is None:
        return False
    return isinstance(side.get("derivation_case"), dict)
```

- [ ] **Step 2: Add semantic support and evidence-basis canonicalization.**

Do not compare raw Gate-2 result objects because run-local `evaluation_id` and assertion IDs are occurrence identities, not semantic support meaning.

```python
def _support_signature(result: dict) -> dict[str, Any]:
    evaluation = result.get("evaluation") if isinstance(result, dict) else None
    conclusion = result.get("conclusion_assertion") if isinstance(result, dict) else None
    if not isinstance(evaluation, dict):
        return {"disposition": "INVALID", "reason_code": "INVALID_DERIVATION_RESULT", "conclusion": None}

    semantic_conclusion = None
    if isinstance(conclusion, dict):
        semantic_conclusion = {
            "subject_id": conclusion.get("subject_id"),
            "predicate": conclusion.get("predicate"),
            "object_id": conclusion.get("object_id"),
            "scope": conclusion.get("scope"),
        }

    return {
        "disposition": evaluation.get("disposition"),
        "reason_code": evaluation.get("reason_code"),
        "conclusion": semantic_conclusion,
    }


def _evidence_basis(result: dict) -> list[str]:
    evaluation = result.get("evaluation") if isinstance(result, dict) else None
    ids = evaluation.get("input_ids") if isinstance(evaluation, dict) else None
    if not isinstance(ids, list):
        return []
    return [item for item in ids if isinstance(item, str) and item]
```

Hash with:

```python
evidence_basis_digest = sha256_json({"input_ids": evidence_basis})
support_result_digest = sha256_json(_support_signature(result))
```

- [ ] **Step 3: Refuse formation metadata inside semantic support inputs.**

Add:

```python
def _formation_refs(side: dict) -> set[str]:
    selection = side["selection"]
    return set(side["interest_receipt_refs"]) | set(selection["receipt_refs"]) | set(
        selection["consumed_interest_receipt_refs"]
    )
```

After evaluating each side, if `_formation_refs(side)` intersects that side's Gate-2 `evaluation.input_ids`, return:

```text
REFUSE / INTEREST_AS_SUPPORT
```

This catches the concrete current gap where `RELATION-DERIVATION-001` allows additional proposal basis IDs as long as the attributable evidence source/path are also present. The wrapper, not Gate 2, owns the cross-run non-collapse test.

- [ ] **Step 4: Implement direct-effect-zero comparison.**

The control is valid only when the pair actually differs in interest ancestry:

```python
def _interest_signature(side: dict) -> dict[str, Any]:
    return {
        "interest_receipt_refs": sorted(side["interest_receipt_refs"]),
        "consumed_interest_receipt_refs": sorted(side["selection"]["consumed_interest_receipt_refs"]),
    }
```

If the signatures are identical, return:

```text
INSUFFICIENT_TO_TEST / INTEREST_CONTROL_NOT_DIFFERENT
```

If evidence-basis digests are identical and semantic support digests are identical, return:

```text
ACCEPT / mediation_status=DIRECT_EFFECT_ZERO / support_changed=false
```

If evidence-basis digests are identical but support digests differ, return:

```text
REFUSE / INTEREST_AS_SUPPORT
```

- [ ] **Step 5: Add a semantic-inflation hostile test.**

In `tests/test_mediated_support.py`:

```python
    def test_interest_receipt_may_not_enter_gate2_support_basis(self):
        case = load_pair()
        right = case["right"]
        right["selection"]["consumed_interest_receipt_refs"] = ["interest:q"]
        right["derivation_case"]["attempt"]["relation_proposal"]["basis_ids"].append("interest:q")

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason_code"], "INTEREST_AS_SUPPORT")
```

- [ ] **Step 6: Run focused tests to GREEN.**

```bash
python -m unittest tests.test_mediated_support -v
```

Expected: all Task-1/2 tests pass.

- [ ] **Step 7: Commit the minimal evaluator.**

```bash
git add alex_runtime/mediated_support.py tests/test_mediated_support.py
git commit -m "feat: enforce zero direct interest support effect"
```

---

### Task 3: Add lawful mediation and stripped-formation pressure

**Files:**
- Modify: `alex_runtime/mediated_support.py`
- Modify: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: direct-effect evaluator from Task 2.
- Produces: `LAWFUL_MEDIATION` when changed evidence peels through attributable selection/consumption; `SELECTION_FORMATION_REQUIRED` for population/generalization comparison with stripped formation ancestry.

- [ ] **Step 1: Add a test helper that creates a genuinely different evidence basis without changing the claim.**

```python
def rename_evidence_basis(case: dict, suffix: str) -> dict:
    updated = copy.deepcopy(case)
    old_source = updated["attempt"]["relation_proposal"]["subject_id"]
    new_source = f"{old_source}-{suffix}"
    old_path = updated["attempt"]["relation_proposal"]["basis_ids"][1]
    new_path = f"{old_path}-{suffix}"

    for record in updated["given"]["records"]:
        if record.get("id") == old_source:
            record["id"] = new_source

    for path in updated["given"]["evidence_paths"]:
        if path.get("id") == old_path:
            path["id"] = new_path
            path["source_id"] = new_source
            path["basis_ids"] = [new_source if value == old_source else value for value in path["basis_ids"]]

    proposal = updated["attempt"]["relation_proposal"]
    proposal["subject_id"] = new_source
    proposal["basis_ids"] = [new_source, new_path]
    updated["attempt"]["conclusion_assertion_id"] = f"AS-{suffix}"
    return updated
```

This deliberately changes the actual support source/path while keeping `object_id == claim_id`.

- [ ] **Step 2: Add the lawful mediation test.**

```python
    def test_consumed_interest_may_change_support_only_through_changed_evidence(self):
        case = load_pair()
        right = case["right"]
        right["selection"] = {
            "policy_digest": "sha256:interest-selector-v1",
            "receipt_refs": ["selection:interest-guided"],
            "consumed_interest_receipt_refs": ["interest:q"],
        }
        right["bounded_context_digest"] = "sha256:context-interest-guided"
        right["projection_digest"] = "sha256:projection-interest-guided"
        right["derivation_case"] = rename_evidence_basis(right["derivation_case"], "guided")

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["mediation_status"], "LAWFUL_MEDIATION")
        self.assertNotEqual(
            result["left"]["evidence_basis_digest"],
            result["right"]["evidence_basis_digest"],
        )
        self.assertIn("interest:q", result["receipt_survivors"])
        self.assertIn("selection:interest-guided", result["receipt_survivors"])
```

- [ ] **Step 3: Implement attributable-selection validation.**

```python
def _selection_formation_complete(side: dict) -> bool:
    selection = side["selection"]
    policy = selection["policy_digest"]
    receipts = selection["receipt_refs"]
    consumed = selection["consumed_interest_receipt_refs"]
    if not isinstance(policy, str) or not policy or not receipts:
        return False
    return set(consumed).issubset(set(side["interest_receipt_refs"]))
```

A changed evidence basis may be classified as `LAWFUL_MEDIATION` only when:

```text
left evidence basis != right evidence basis
AND bounded context differs
AND at least one side consumed an interest receipt
AND every consumed interest ref is present in that side's declared interest receipts
AND the consuming side has a non-empty selector policy digest and selection receipt refs
```

Otherwise return:

```text
INSUFFICIENT_TO_TEST / SELECTION_FORMATION_REQUIRED
```

Do not infer which context was statistically better or whether the interest signal was dominant.

- [ ] **Step 4: Add the population/generalization stripped-formation test.**

```python
    def test_population_claim_requires_selection_formation(self):
        case = load_pair()
        case["claim_class"] = "POPULATION_GENERALIZATION"
        case["right"]["selection"] = {
            "policy_digest": None,
            "receipt_refs": [],
            "consumed_interest_receipt_refs": [],
        }

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "SELECTION_FORMATION_REQUIRED")
```

- [ ] **Step 5: Add the object-local counter-control.**

The same stripped selection history must not invalidate genuine object evidence:

```python
    def test_object_local_support_does_not_require_selection_history(self):
        case = load_pair()
        case["right"]["selection"] = {
            "policy_digest": None,
            "receipt_refs": [],
            "consumed_interest_receipt_refs": [],
        }

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["mediation_status"], "DIRECT_EFFECT_ZERO")
```

This test is essential: `interest present -> evidence invalid` is as forbidden as `interest present -> evidence stronger`.

- [ ] **Step 6: Run focused tests.**

```bash
python -m unittest tests.test_mediated_support -v
```

Expected: all mediated-support tests pass.

- [ ] **Step 7: Commit lawful mediation behavior.**

```bash
git add alex_runtime/mediated_support.py tests/test_mediated_support.py
git commit -m "feat: distinguish mediated support from selection provenance"
```

---

### Task 4: Harden identity, survivors, and error classification

**Files:**
- Modify: `alex_runtime/mediated_support.py`
- Modify: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: Tasks 1–3 behavior.
- Produces: stable result identity suitable for a later rectangle coordinator without implementing the coordinator.

- [ ] **Step 1: Require `claim_id` and `claim_class`.**

Validation rules:

```text
case_id                  non-empty string
claim_id                 non-empty string
claim_class              OBJECT_LOCAL | POPULATION_GENERALIZATION
left/right               valid side objects
left derivation object   claim_id must equal proposal.object_id
right derivation object  claim_id must equal proposal.object_id
```

Malformed structure returns:

```text
INSUFFICIENT_TO_TEST / MALFORMED_CASE
```

Claim mismatch returns:

```text
INSUFFICIENT_TO_TEST / CLAIM_ID_MISMATCH
```

- [ ] **Step 2: Preserve pair-level and Gate-2 receipt survivors.**

For each side, union:

```python
side["interest_receipt_refs"]
side["selection"]["receipt_refs"]
side["selection"]["consumed_interest_receipt_refs"]
result["evaluation"]["required_survivors"]
```

Return one sorted unique `receipt_survivors` list. Do not claim these refs are semantic evidence merely because they survive.

- [ ] **Step 3: Add nested Gate-2 failure propagation tests.**

If either derivation is malformed or outside profile, the wrapper must not manufacture a pair-level support conclusion. Add:

```python
    def test_gate2_insufficient_result_prevents_mediation_claim(self):
        case = load_pair()
        case["right"]["derivation_case"]["given"]["evidence_paths"] = []

        result = evaluate_mediated_support_case(case)

        self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["reason_code"], "DERIVATION_NOT_COMPARABLE")
        self.assertIsNone(result["mediation_status"])
```

The wrapper may compare semantic support only when both nested Gate-2 results are structurally valid. It does not rewrite their individual reason codes; preserve them under optional nested fields such as `left_derivation_disposition` and `right_derivation_disposition` if useful.

- [ ] **Step 4: Verify occurrence IDs do not cause false direct-effect failures.**

Mutate only `evaluation_id`, `execution_step_id`, and `conclusion_assertion_id` on the right while keeping the evidence and semantic relation identical. The pair must remain `DIRECT_EFFECT_ZERO` because `_support_signature()` excludes run-local occurrence identity.

- [ ] **Step 5: Run focused tests.**

```bash
python -m unittest tests.test_mediated_support -v
```

- [ ] **Step 6: Commit hardening.**

```bash
git add alex_runtime/mediated_support.py tests/test_mediated_support.py
git commit -m "test: harden mediated support identity and ancestry"
```

---

### Task 5: Document the bounded claim and run full regression

**Files:**
- Modify: `crucible/README.md`
- Test: all existing tests plus `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: verified `MEDIATED-SUPPORT-001` implementation.
- Produces: explicit documentation and fresh regression evidence; no rectangle implementation.

- [ ] **Step 1: Add a `MEDIATED-SUPPORT-001` section after `PROJECTION-BREAK-001`.**

Document this exact distinction:

```text
interest / selection provenance
        -> may change bounded context
        -> may change genuine evidence basis
        -> may therefore change Gate-2 support

interest / selection provenance
        -X-> semantic support basis
```

State explicitly that:

- the evaluator composes `RELATION-DERIVATION-001`; it does not replace it;
- a fixed evidence basis must produce the same semantic support result despite changed interest ancestry;
- changed support may be accepted only when the changed evidence basis peels through attributable selector/consumption formation;
- population/generalization claims with stripped selection formation are insufficient, not automatically false;
- object-local evidence remains valid when its attributable evidence path is valid, regardless of why the object was inspected;
- passing does not prove representative sampling, hidden motive accuracy, causal sufficiency/dominance, global truth, or authority;
- `COUNTERFACTUAL-RECTANGLE-001` remains unimplemented pending evidence that pairwise tests leave a real interaction gap.

- [ ] **Step 2: Run the focused file once more.**

```bash
python -m unittest tests.test_mediated_support -v
```

Expected: PASS.

- [ ] **Step 3: Run the full repository regression suite.**

```bash
python -m unittest discover -s tests -v
```

Expected: all existing tests plus the mediated-support tests pass.

- [ ] **Step 4: Run an absence guard for accidental rectangle/kernel promotion.**

```bash
python - <<'PY'
from pathlib import Path

forbidden = (
    "evaluate_counterfactual_rectangle_case",
    "POLICY-EQUIVALENCE-001",
    "PARTITION-REFINEMENT-001",
    "ADAPTIVE-EPISTEMIC-TOPOLOGY-001",
)
paths = [Path("alex_runtime"), Path("tests")]
text = "\n".join(
    p.read_text(encoding="utf-8")
    for root in paths
    for p in root.rglob("*.py")
)
for token in forbidden:
    assert token not in text, token
print("PASS no rectangle/topology kernel promotion")
PY
```

- [ ] **Step 5: Commit documentation.**

```bash
git add crucible/README.md
git commit -m "docs: bound mediated support conformance claim"
```

---

## Self-Review

### Spec coverage

- Case A / inert interest: Task 1 + Task 2 direct-effect-zero control.
- Case B / lawful mediated divergence: Task 3.
- Case C / direct-effect hostile control: Task 2 fixed-evidence comparison.
- Case D / stripped formation ancestry: Task 3 population/generalization and object-local sibling controls.
- Case E / semantic inflation: Task 2 forbids interest/selection refs inside Gate-2 semantic support inputs.
- Ownership boundary: wrapper consumes context/projection testimony and delegates support to existing `evaluate_relation_case()`; no LOADOUT/3rdi implementation enters ALEX.
- Result identity: Task 4.
- No-authority/non-claim membrane: Tasks 1, 4, 5.
- Rectangle remains conditional: Global Constraints + Task 5 absence guard.

### Placeholder scan

The implementation target, public function, input fields, result fields, reason codes, test fixture, focused commands, full regression command, and commit boundaries are explicit. No `TBD`, `TODO`, generic “add tests,” or unowned follow-up step is required to execute this plan.

### Type consistency

Public entry point throughout:

```python
evaluate_mediated_support_case(case: dict) -> dict[str, Any]
```

Stable pair fields throughout:

```text
case_id
claim_id
claim_class
projection_digest
bounded_context_digest
interest_receipt_refs
selection.policy_digest
selection.receipt_refs
selection.consumed_interest_receipt_refs
derivation_case
```

Stable result fields throughout:

```text
case_id
claim_id
disposition
reason_code
mediation_status
support_changed
left/right.projection_digest
left/right.bounded_context_digest
left/right.evidence_basis_digest
left/right.support_result_digest
receipt_survivors
```

### Scope check

This plan produces working, independently testable `MEDIATED-SUPPORT-001` software on its own. `COUNTERFACTUAL-RECTANGLE-001` remains a separate future plan only if this implementation and existing pairwise evaluators demonstrate a residual interaction class that cannot already be named compositionally.
