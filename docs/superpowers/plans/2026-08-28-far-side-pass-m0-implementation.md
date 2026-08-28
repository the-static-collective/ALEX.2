# FAR-SIDE PASS m0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build an ALEX-local, deterministic hostile lab that evaluates a supplied FAR-SIDE formation receipt for baseline sufficiency, traversal diversity, invariant survival, regeneration strength, novelty delta, and adversarial pressure without generating claims or changing the public ALEX skill/runtime contract.

**Architecture:** Keep generation outside the executable slice. MMathalM or a human supplies a receipted candidate; the new `experiments.far_side` package only validates and pressures that candidate. A small CLI adapter under `tools/` reads JSON and emits a deterministic result. No Crucible schema, `alex_runtime` integration, skill trigger, Dogram dependency, network access, or authority surface is added.

**Tech Stack:** Python 3 standard library only (`json`, `argparse`, `pathlib`, `subprocess`, `unittest`), existing `alex_runtime.digests.sha256_json` helper, JSON fixtures.

**Spec:** `docs/superpowers/specs/2026-08-28-far-side-pass-practice-design.md`

## Global Constraints

- FAR-SIDE PASS remains an experimental research practice; this plan does not claim ALEX runtime conformance.
- MMathalM generation stays outside the evaluator. The lab consumes supplied receipts and never invents a simplicity candidate, invariant, novelty claim, or pressure result.
- ALEX may pressure and classify the supplied formation but may not mint evidence, support, authority, canon, publication, admission, or execution rights.
- `SEARCH FOR NOVELTY != PRODUCTION OF NOVELTY` is executable: `NO_NEW_DIMENSION_EARNED` must be a first-class successful terminal state.
- `NEW_WORDING != NEW_REPRESENTATION != NEW_DERIVATION != NEW_RELATION != NEW_INVARIANT != NEW_PREDICTION` remains explicit in output.
- Novelty is measured relative to a declared pre-pass baseline. Missing or malformed baseline data returns `INSUFFICIENT_BASELINE` rather than fabricated novelty.
- Regeneration is not historical reconstruction. A candidate may regenerate declared targets without impersonating the original occurrence.
- At least three materially distinct traversal axes are required before a candidate can earn `FAR_SIDE_SURVIVOR`.
- Hostile checks must be able to kill the favored candidate. A missing hostile receipt returns `INSUFFICIENT_RECEIPT`; a failed hostile check prevents `FAR_SIDE_SURVIVOR`.
- Dogram remains optional and external; no Dogram import or RPC is introduced.
- Do not modify `skills/alex/SKILL.md`, Crucible schemas/profiles, `alex_runtime/*`, LOADOUT code, or README in this implementation slice.
- Use deterministic ordering in all emitted lists and JSON output.
- Tests use the repository's existing `unittest` style.

---

## File Structure

Create these focused files:

```text
experiments/
  __init__.py
  far_side/
    __init__.py
    model.py
    engine.py

tools/
  far_side_lab.py

tests/
  fixtures/
    far_side/
      survivor.json
      no-new-dimension.json
      partial-regeneration.json
      metaphor-failure.json
      insufficient-baseline.json
  test_far_side_model.py
  test_far_side_engine.py
  test_far_side_cli.py
```

Responsibilities:

- `experiments/far_side/model.py` — constants, exact input-shape validation, whitespace-only statement normalization, and pressure/traversal requirement helpers. No semantic inference.
- `experiments/far_side/engine.py` — deterministic invariant intersection, regeneration comparison, exact baseline novelty comparison, hostile-pressure gate, and final disposition.
- `tools/far_side_lab.py` — file/stdin JSON adapter only; no additional semantics.
- `tests/fixtures/far_side/*` — positive, no-novelty, partial, hostile-failure, and insufficient-baseline specimens.

The package name `experiments` is intentional: it keeps this proof outside `alex_runtime` until the promotion gates in the spec are earned.

---

### Task 1: Establish the experimental data contract and baseline validation

**Files:**
- Create: `experiments/__init__.py`
- Create: `experiments/far_side/__init__.py`
- Create: `experiments/far_side/model.py`
- Create: `tests/test_far_side_model.py`

**Interfaces:**
- Produces: `normalize_statement(text: str) -> str`
- Produces: `validate_far_side_case(case: object) -> tuple[bool, str | None]`
- Produces constants: `TRAVERSAL_AXES`, `NOVELTY_TYPES`, `PRESSURE_KINDS`, `REQUIRED_PRESSURES`, `DIMENSIONAL_NOVELTY_TYPES`
- Later tasks import these exact names.

- [ ] **Step 1: Write the failing model tests**

Create `tests/test_far_side_model.py`:

```python
import copy
import unittest

from experiments.far_side.model import (
    DIMENSIONAL_NOVELTY_TYPES,
    NOVELTY_TYPES,
    REQUIRED_PRESSURES,
    TRAVERSAL_AXES,
    normalize_statement,
    validate_far_side_case,
)


VALID_CASE = {
    "case_id": "far-side:minimal",
    "h0": "Something new may become visible.",
    "baseline": {
        "claims": [
            {"id": "b:1", "statement": "Route is not host topology."},
            {"id": "b:2", "statement": "Opening is not transition."},
        ],
        "invariants": ["inv:route-host-distinction", "inv:opening-transition-distinction"],
    },
    "traversals": [
        {
            "id": "t:scale",
            "axis": "SCALE",
            "transform": "whole-to-parts",
            "invariants": ["inv:route-host-distinction"],
            "losses": [],
            "receipt_ref": "receipt:t:scale",
        },
        {
            "id": "t:direction",
            "axis": "DIRECTION",
            "transform": "result-to-formation",
            "invariants": ["inv:route-host-distinction"],
            "losses": [],
            "receipt_ref": "receipt:t:direction",
        },
        {
            "id": "t:representation",
            "axis": "REPRESENTATION",
            "transform": "prose-to-graph",
            "invariants": ["inv:route-host-distinction"],
            "losses": [],
            "receipt_ref": "receipt:t:representation",
        },
    ],
    "candidate": {
        "statement": "The selected route does not exhaust the available field.",
        "required_targets": ["inv:route-host-distinction"],
        "regenerated_targets": ["inv:route-host-distinction"],
        "novelty": [],
    },
    "pressure": [
        {"kind": kind, "status": "PASS", "receipt_ref": f"receipt:pressure:{kind.lower()}"}
        for kind in sorted(REQUIRED_PRESSURES)
    ],
}


class FarSideModelTests(unittest.TestCase):
    def test_statement_normalization_is_whitespace_only(self):
        self.assertEqual(
            normalize_statement("  Route  is\nnot   topology. "),
            "Route is not topology.",
        )

    def test_validation_accepts_minimal_receipted_case(self):
        valid, reason = validate_far_side_case(VALID_CASE)
        self.assertTrue(valid)
        self.assertIsNone(reason)

    def test_validation_requires_a_nonempty_baseline(self):
        case = copy.deepcopy(VALID_CASE)
        case["baseline"]["claims"] = []
        case["baseline"]["invariants"] = []
        valid, reason = validate_far_side_case(case)
        self.assertFalse(valid)
        self.assertEqual(reason, "INSUFFICIENT_BASELINE")

    def test_validation_requires_receipted_traversals(self):
        case = copy.deepcopy(VALID_CASE)
        del case["traversals"][0]["receipt_ref"]
        valid, reason = validate_far_side_case(case)
        self.assertFalse(valid)
        self.assertEqual(reason, "INSUFFICIENT_RECEIPT")

    def test_enums_preserve_spec_distinctions(self):
        self.assertEqual(
            NOVELTY_TYPES,
            {
                "NEW_WORDING",
                "NEW_REPRESENTATION",
                "NEW_DERIVATION",
                "NEW_RELATION",
                "NEW_INVARIANT",
                "NEW_PREDICTION",
            },
        )
        self.assertEqual(
            DIMENSIONAL_NOVELTY_TYPES,
            {"NEW_DERIVATION", "NEW_RELATION", "NEW_INVARIANT", "NEW_PREDICTION"},
        )
        self.assertIn("REPRESENTATION", TRAVERSAL_AXES)
        self.assertIn("METAPHOR_REMOVAL", REQUIRED_PRESSURES)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the model tests and verify RED**

Run:

```bash
python -m unittest tests.test_far_side_model -v
```

Expected: import failure because `experiments.far_side.model` does not exist.

- [ ] **Step 3: Implement the minimal model contract**

Create empty `experiments/__init__.py` and `experiments/far_side/__init__.py`.

Create `experiments/far_side/model.py`:

```python
from __future__ import annotations

from typing import Any


TRAVERSAL_AXES = {
    "SCALE",
    "DIRECTION",
    "OBJECT_RELATION",
    "REPRESENTATION",
    "TIME",
    "COMPRESSION_REGENERATION",
}

NOVELTY_TYPES = {
    "NEW_WORDING",
    "NEW_REPRESENTATION",
    "NEW_DERIVATION",
    "NEW_RELATION",
    "NEW_INVARIANT",
    "NEW_PREDICTION",
}

DIMENSIONAL_NOVELTY_TYPES = {
    "NEW_DERIVATION",
    "NEW_RELATION",
    "NEW_INVARIANT",
    "NEW_PREDICTION",
}

PRESSURE_KINDS = {
    "NEAREST_BORING",
    "METAPHOR_REMOVAL",
    "REPRESENTATION_SWAP",
    "RELABEL",
    "PARAMETER_SWAP",
    "HOLDOUT",
    "REGENERATION_FAILURE",
}

REQUIRED_PRESSURES = {
    "NEAREST_BORING",
    "METAPHOR_REMOVAL",
    "REPRESENTATION_SWAP",
    "RELABEL",
    "HOLDOUT",
    "REGENERATION_FAILURE",
}


def normalize_statement(text: str) -> str:
    return " ".join(text.split())


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _valid_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_string(item) for item in value)


def validate_far_side_case(case: object) -> tuple[bool, str | None]:
    if not isinstance(case, dict):
        return False, "INSUFFICIENT_RECEIPT"

    if not _nonempty_string(case.get("case_id")) or not _nonempty_string(case.get("h0")):
        return False, "INSUFFICIENT_RECEIPT"

    baseline = case.get("baseline")
    if not isinstance(baseline, dict):
        return False, "INSUFFICIENT_BASELINE"
    claims = baseline.get("claims")
    invariants = baseline.get("invariants")
    if not isinstance(claims, list) or not isinstance(invariants, list) or (not claims and not invariants):
        return False, "INSUFFICIENT_BASELINE"
    for claim in claims:
        if not isinstance(claim, dict):
            return False, "INSUFFICIENT_BASELINE"
        if not _nonempty_string(claim.get("id")) or not _nonempty_string(claim.get("statement")):
            return False, "INSUFFICIENT_BASELINE"
    if not _valid_string_list(invariants):
        return False, "INSUFFICIENT_BASELINE"

    traversals = case.get("traversals")
    if not isinstance(traversals, list) or not traversals:
        return False, "INSUFFICIENT_RECEIPT"
    for traversal in traversals:
        if not isinstance(traversal, dict):
            return False, "INSUFFICIENT_RECEIPT"
        if traversal.get("axis") not in TRAVERSAL_AXES:
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(traversal.get("id")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(traversal.get("transform")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(traversal.get("receipt_ref")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _valid_string_list(traversal.get("invariants")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _valid_string_list(traversal.get("losses")):
            return False, "INSUFFICIENT_RECEIPT"

    candidate = case.get("candidate")
    if not isinstance(candidate, dict) or not _nonempty_string(candidate.get("statement")):
        return False, "INSUFFICIENT_RECEIPT"
    if not _valid_string_list(candidate.get("required_targets")):
        return False, "INSUFFICIENT_RECEIPT"
    if not _valid_string_list(candidate.get("regenerated_targets")):
        return False, "INSUFFICIENT_RECEIPT"

    novelty = candidate.get("novelty")
    if not isinstance(novelty, list):
        return False, "INSUFFICIENT_RECEIPT"
    for item in novelty:
        if not isinstance(item, dict):
            return False, "INSUFFICIENT_RECEIPT"
        if item.get("type") not in NOVELTY_TYPES:
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(item.get("statement")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(item.get("discriminator")):
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(item.get("receipt_ref")):
            return False, "INSUFFICIENT_RECEIPT"

    pressure = case.get("pressure")
    if not isinstance(pressure, list):
        return False, "INSUFFICIENT_RECEIPT"
    for check in pressure:
        if not isinstance(check, dict):
            return False, "INSUFFICIENT_RECEIPT"
        if check.get("kind") not in PRESSURE_KINDS:
            return False, "INSUFFICIENT_RECEIPT"
        if check.get("status") not in {"PASS", "FAIL", "NOT_APPLICABLE"}:
            return False, "INSUFFICIENT_RECEIPT"
        if not _nonempty_string(check.get("receipt_ref")):
            return False, "INSUFFICIENT_RECEIPT"

    return True, None
```

- [ ] **Step 4: Run the model tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_far_side_model -v
```

Expected: 5 tests pass.

- [ ] **Step 5: Commit Task 1**

```bash
git add experiments/__init__.py experiments/far_side/__init__.py experiments/far_side/model.py tests/test_far_side_model.py
git commit -m "test: define FAR-SIDE experimental receipt contract"
```

---

### Task 2: Implement invariant survival and regeneration pressure

**Files:**
- Create: `experiments/far_side/engine.py`
- Create: `tests/test_far_side_engine.py`

**Interfaces:**
- Consumes: `validate_far_side_case`, `normalize_statement`, `REQUIRED_PRESSURES`, `DIMENSIONAL_NOVELTY_TYPES`
- Produces: `evaluate_far_side_case(case: object) -> dict[str, object]`
- Result keys are exactly: `case_id`, `final_status`, `reason_code`, `baseline_digest`, `traversal_axes`, `surviving_invariants`, `regenerated_targets`, `missing_targets`, `novelty_delta`, `pressure_failures`, `receipt_survivors`.

- [ ] **Step 1: Write failing engine tests for traversal diversity and regeneration**

Create `tests/test_far_side_engine.py` initially with:

```python
import copy
import unittest

from experiments.far_side.engine import evaluate_far_side_case
from tests.test_far_side_model import VALID_CASE


class FarSideEngineTests(unittest.TestCase):
    def test_three_distinct_axes_and_full_regeneration_can_reach_no_novelty_success(self):
        result = evaluate_far_side_case(copy.deepcopy(VALID_CASE))

        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(
            result["traversal_axes"],
            ["DIRECTION", "REPRESENTATION", "SCALE"],
        )
        self.assertEqual(result["surviving_invariants"], ["inv:route-host-distinction"])
        self.assertEqual(result["missing_targets"], [])
        self.assertEqual(result["novelty_delta"], [])

    def test_fewer_than_three_material_axes_is_insufficient(self):
        case = copy.deepcopy(VALID_CASE)
        case["traversals"][2]["axis"] = "SCALE"

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "INSUFFICIENT_RECEIPT")
        self.assertEqual(result["reason_code"], "INSUFFICIENT_TRAVERSAL_DIVERSITY")

    def test_some_but_not_all_required_targets_yields_partial_survivor(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["required_targets"] = [
            "inv:route-host-distinction",
            "inv:opening-transition-distinction",
        ]
        case["candidate"]["regenerated_targets"] = ["inv:route-host-distinction"]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "PARTIAL_SURVIVOR")
        self.assertEqual(result["missing_targets"], ["inv:opening-transition-distinction"])

    def test_zero_required_targets_regenerated_is_compression_failure(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["regenerated_targets"] = []

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "COMPRESSION_FAILED_REGENERATION")
        self.assertEqual(result["reason_code"], "NO_REQUIRED_TARGET_REGENERATED")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the engine tests and verify RED**

Run:

```bash
python -m unittest tests.test_far_side_engine -v
```

Expected: import failure because `experiments.far_side.engine` does not exist.

- [ ] **Step 3: Implement invariant intersection, regeneration comparison, and stable result envelope**

Create `experiments/far_side/engine.py` with these helpers and evaluator skeleton:

```python
from __future__ import annotations

from typing import Any

from alex_runtime.digests import sha256_json
from experiments.far_side.model import (
    DIMENSIONAL_NOVELTY_TYPES,
    REQUIRED_PRESSURES,
    normalize_statement,
    validate_far_side_case,
)


def _baseline_digest(case: dict[str, Any]) -> str:
    return sha256_json(case["baseline"])


def _receipt_survivors(case: dict[str, Any]) -> list[str]:
    refs = [item["receipt_ref"] for item in case["traversals"]]
    refs.extend(item["receipt_ref"] for item in case["candidate"]["novelty"])
    refs.extend(item["receipt_ref"] for item in case["pressure"])
    return sorted(set(refs))


def _surviving_invariants(case: dict[str, Any]) -> list[str]:
    invariant_sets = [set(item["invariants"]) for item in case["traversals"]]
    if not invariant_sets:
        return []
    return sorted(set.intersection(*invariant_sets))


def _result(
    case_id: str,
    final_status: str,
    reason_code: str | None,
    baseline_digest: str | None,
    traversal_axes: list[str],
    surviving_invariants: list[str],
    regenerated_targets: list[str],
    missing_targets: list[str],
    novelty_delta: list[dict[str, str]],
    pressure_failures: list[str],
    receipt_survivors: list[str],
) -> dict[str, object]:
    return {
        "case_id": case_id,
        "final_status": final_status,
        "reason_code": reason_code,
        "baseline_digest": baseline_digest,
        "traversal_axes": traversal_axes,
        "surviving_invariants": surviving_invariants,
        "regenerated_targets": regenerated_targets,
        "missing_targets": missing_targets,
        "novelty_delta": novelty_delta,
        "pressure_failures": pressure_failures,
        "receipt_survivors": receipt_survivors,
    }


def evaluate_far_side_case(case: object) -> dict[str, object]:
    case_id = case.get("case_id", "unknown-case") if isinstance(case, dict) else "unknown-case"
    if not isinstance(case_id, str) or not case_id:
        case_id = "unknown-case"

    valid, reason = validate_far_side_case(case)
    if not valid:
        return _result(case_id, reason or "INSUFFICIENT_RECEIPT", reason, None, [], [], [], [], [], [], [])

    assert isinstance(case, dict)
    baseline_digest = _baseline_digest(case)
    axes = sorted({item["axis"] for item in case["traversals"]})
    survivors = _surviving_invariants(case)
    receipts = _receipt_survivors(case)

    if len(axes) < 3:
        return _result(
            case_id,
            "INSUFFICIENT_RECEIPT",
            "INSUFFICIENT_TRAVERSAL_DIVERSITY",
            baseline_digest,
            axes,
            survivors,
            [],
            [],
            [],
            [],
            receipts,
        )

    required = sorted(set(case["candidate"]["required_targets"]))
    regenerated = sorted(set(case["candidate"]["regenerated_targets"]))
    regenerated_required = sorted(set(required) & set(regenerated))
    missing = sorted(set(required) - set(regenerated))

    if required and not regenerated_required:
        return _result(
            case_id,
            "COMPRESSION_FAILED_REGENERATION",
            "NO_REQUIRED_TARGET_REGENERATED",
            baseline_digest,
            axes,
            survivors,
            regenerated,
            missing,
            [],
            [],
            receipts,
        )

    if missing:
        return _result(
            case_id,
            "PARTIAL_SURVIVOR",
            "PARTIAL_REGENERATION",
            baseline_digest,
            axes,
            survivors,
            regenerated,
            missing,
            [],
            [],
            receipts,
        )

    # Novelty and pressure gates are added in Task 3.
    return _result(
        case_id,
        "NO_NEW_DIMENSION_EARNED",
        None,
        baseline_digest,
        axes,
        survivors,
        regenerated,
        [],
        [],
        [],
        receipts,
    )
```

- [ ] **Step 4: Run the engine tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_far_side_engine -v
```

Expected: 4 tests pass.

- [ ] **Step 5: Add immutability and forbidden-authority tests**

Append to `FarSideEngineTests`:

```python
    def test_evaluator_does_not_mutate_input(self):
        case = copy.deepcopy(VALID_CASE)
        before = copy.deepcopy(case)
        evaluate_far_side_case(case)
        self.assertEqual(case, before)

    def test_result_has_no_authority_surface(self):
        result = evaluate_far_side_case(copy.deepcopy(VALID_CASE))
        forbidden = {
            "authority",
            "support",
            "evidence",
            "canon",
            "admitted",
            "publication",
            "execution_authority",
        }
        self.assertTrue(forbidden.isdisjoint(result))
```

Run:

```bash
python -m unittest tests.test_far_side_engine -v
```

Expected: 6 tests pass.

- [ ] **Step 6: Commit Task 2**

```bash
git add experiments/far_side/engine.py tests/test_far_side_engine.py
git commit -m "feat: pressure FAR-SIDE regeneration receipts"
```

---

### Task 3: Add exact novelty-delta accounting and hostile-pressure gates

**Files:**
- Modify: `experiments/far_side/engine.py`
- Modify: `tests/test_far_side_engine.py`

**Interfaces:**
- `evaluate_far_side_case` result shape remains unchanged.
- Novelty comparison is deliberately exact/structural: whitespace-normalized statement equality against the frozen baseline is the only automatic duplicate detector in m0.
- `NEW_WORDING` and `NEW_REPRESENTATION` are reported in `novelty_delta` but do not by themselves qualify as a new dimension.

- [ ] **Step 1: Write failing tests for novelty and hostile checks**

Append to `FarSideEngineTests`:

```python
    def test_dimensional_novelty_plus_passing_pressure_earns_survivor(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_DERIVATION",
                "statement": "A closed cubic route leaves a 1-regular residual field.",
                "discriminator": "Compare the Hamiltonian-cycle sibling with a Hamiltonian path.",
                "receipt_ref": "receipt:novelty:residual",
            }
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "FAR_SIDE_SURVIVOR")
        self.assertEqual(len(result["novelty_delta"]), 1)
        self.assertEqual(result["novelty_delta"][0]["type"], "NEW_DERIVATION")

    def test_exact_baseline_duplicate_does_not_count_as_novelty(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_RELATION",
                "statement": "  Route   is not\n host topology. ",
                "discriminator": "Would differ under an exhaustive-host claim.",
                "receipt_ref": "receipt:novelty:duplicate",
            }
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")
        self.assertEqual(result["novelty_delta"], [])

    def test_wording_only_delta_is_reported_but_does_not_earn_new_dimension(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_WORDING",
                "statement": "The traveled road is smaller than the road field.",
                "discriminator": "Compare semantic content against baseline manually.",
                "receipt_ref": "receipt:novelty:wording",
            }
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")
        self.assertEqual(result["novelty_delta"][0]["type"], "NEW_WORDING")

    def test_failed_metaphor_removal_prevents_survivor(self):
        case = copy.deepcopy(VALID_CASE)
        case["candidate"]["novelty"] = [
            {
                "type": "NEW_INVARIANT",
                "statement": "A residual relation remains after removing the route.",
                "discriminator": "Compute graph difference after relabeling all metaphors.",
                "receipt_ref": "receipt:novelty:invariant",
            }
        ]
        for check in case["pressure"]:
            if check["kind"] == "METAPHOR_REMOVAL":
                check["status"] = "FAIL"

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "PARTIAL_SURVIVOR")
        self.assertEqual(result["reason_code"], "HOSTILE_PRESSURE_FAILED")
        self.assertEqual(result["pressure_failures"], ["METAPHOR_REMOVAL"])

    def test_missing_required_pressure_receipt_is_insufficient(self):
        case = copy.deepcopy(VALID_CASE)
        case["pressure"] = [
            check for check in case["pressure"] if check["kind"] != "HOLDOUT"
        ]

        result = evaluate_far_side_case(case)

        self.assertEqual(result["final_status"], "INSUFFICIENT_RECEIPT")
        self.assertEqual(result["reason_code"], "MISSING_REQUIRED_PRESSURE")
```

- [ ] **Step 2: Run the targeted tests and verify RED**

Run:

```bash
python -m unittest tests.test_far_side_engine -v
```

Expected: the new novelty/pressure tests fail because Task 2 returns `NO_NEW_DIMENSION_EARNED` before evaluating them.

- [ ] **Step 3: Implement exact baseline comparison and pressure gating**

Add these helpers to `experiments/far_side/engine.py`:

```python
def _baseline_statements(case: dict[str, Any]) -> set[str]:
    return {
        normalize_statement(item["statement"])
        for item in case["baseline"]["claims"]
    }


def _novelty_delta(case: dict[str, Any]) -> list[dict[str, str]]:
    baseline = _baseline_statements(case)
    delta: list[dict[str, str]] = []
    for item in case["candidate"]["novelty"]:
        normalized = normalize_statement(item["statement"])
        if normalized in baseline:
            continue
        delta.append(
            {
                "type": item["type"],
                "statement": normalized,
                "discriminator": normalize_statement(item["discriminator"]),
                "receipt_ref": item["receipt_ref"],
            }
        )
    return sorted(delta, key=lambda item: (item["type"], item["statement"], item["receipt_ref"]))


def _pressure_state(case: dict[str, Any]) -> tuple[list[str], list[str]]:
    by_kind = {item["kind"]: item for item in case["pressure"]}
    missing = sorted(REQUIRED_PRESSURES - set(by_kind))
    failures = sorted(
        kind
        for kind, item in by_kind.items()
        if kind in REQUIRED_PRESSURES and item["status"] == "FAIL"
    )
    return missing, failures
```

Replace the Task 2 terminal block after regeneration succeeds with:

```python
    missing_pressure, pressure_failures = _pressure_state(case)
    if missing_pressure:
        return _result(
            case_id,
            "INSUFFICIENT_RECEIPT",
            "MISSING_REQUIRED_PRESSURE",
            baseline_digest,
            axes,
            survivors,
            regenerated,
            [],
            [],
            [],
            receipts,
        )

    novelty_delta = _novelty_delta(case)

    if pressure_failures:
        return _result(
            case_id,
            "PARTIAL_SURVIVOR",
            "HOSTILE_PRESSURE_FAILED",
            baseline_digest,
            axes,
            survivors,
            regenerated,
            [],
            novelty_delta,
            pressure_failures,
            receipts,
        )

    dimensional_delta = [
        item for item in novelty_delta if item["type"] in DIMENSIONAL_NOVELTY_TYPES
    ]
    final_status = "FAR_SIDE_SURVIVOR" if dimensional_delta else "NO_NEW_DIMENSION_EARNED"

    return _result(
        case_id,
        final_status,
        None,
        baseline_digest,
        axes,
        survivors,
        regenerated,
        [],
        novelty_delta,
        [],
        receipts,
    )
```

- [ ] **Step 4: Run the full engine tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_far_side_engine -v
```

Expected: 11 tests pass.

- [ ] **Step 5: Add a relabel-control test proving labels do not alter structural status**

Append:

```python
    def test_relabeling_case_and_receipt_ids_does_not_change_structural_status(self):
        left = copy.deepcopy(VALID_CASE)
        right = copy.deepcopy(VALID_CASE)
        right["case_id"] = "far-side:banana-labels"
        for index, traversal in enumerate(right["traversals"]):
            traversal["id"] = f"banana:{index}"
            traversal["receipt_ref"] = f"receipt:banana:{index}"
        for index, check in enumerate(right["pressure"]):
            check["receipt_ref"] = f"receipt:pressure:banana:{index}"

        left_result = evaluate_far_side_case(left)
        right_result = evaluate_far_side_case(right)

        self.assertEqual(left_result["final_status"], right_result["final_status"])
        self.assertEqual(left_result["traversal_axes"], right_result["traversal_axes"])
        self.assertEqual(left_result["surviving_invariants"], right_result["surviving_invariants"])
        self.assertEqual(left_result["missing_targets"], right_result["missing_targets"])
```

Run:

```bash
python -m unittest tests.test_far_side_engine.FarSideEngineTests.test_relabeling_case_and_receipt_ids_does_not_change_structural_status -v
```

Expected: PASS.

- [ ] **Step 6: Commit Task 3**

```bash
git add experiments/far_side/engine.py tests/test_far_side_engine.py
git commit -m "feat: receipt FAR-SIDE novelty and hostile pressure"
```

---

### Task 4: Add durable hostile specimens and verify the major terminal states

**Files:**
- Create: `tests/fixtures/far_side/survivor.json`
- Create: `tests/fixtures/far_side/no-new-dimension.json`
- Create: `tests/fixtures/far_side/partial-regeneration.json`
- Create: `tests/fixtures/far_side/metaphor-failure.json`
- Create: `tests/fixtures/far_side/insufficient-baseline.json`
- Modify: `tests/test_far_side_engine.py`

**Interfaces:**
- Fixtures are plain JSON inputs to `evaluate_far_side_case`.
- No new schema is admitted; fixture shape remains experimental and local to this package.

- [ ] **Step 1: Create the positive survivor fixture**

Create `tests/fixtures/far_side/survivor.json` with three distinct traversal axes, full regeneration, all six required hostile checks as `PASS`, and one `NEW_DERIVATION` novelty item. Use this exact semantic nucleus:

```json
{
  "case_id": "far-side:residual-topology-survivor",
  "h0": "A recursive backscan may expose a simpler relation between route and topology.",
  "baseline": {
    "claims": [
      {"id": "b:route", "statement": "The path taken is not the topology available."}
    ],
    "invariants": ["inv:route-host-distinction"]
  },
  "traversals": [
    {
      "id": "t:scale",
      "axis": "SCALE",
      "transform": "whole-to-local-degree",
      "invariants": ["inv:route-host-distinction"],
      "losses": [],
      "receipt_ref": "receipt:t:scale"
    },
    {
      "id": "t:direction",
      "axis": "DIRECTION",
      "transform": "route-to-residual",
      "invariants": ["inv:route-host-distinction"],
      "losses": [],
      "receipt_ref": "receipt:t:direction"
    },
    {
      "id": "t:representation",
      "axis": "REPRESENTATION",
      "transform": "prose-to-graph-difference",
      "invariants": ["inv:route-host-distinction"],
      "losses": [],
      "receipt_ref": "receipt:t:representation"
    }
  ],
  "candidate": {
    "statement": "A regular host minus a regular spanning route has a regular residual degree field.",
    "required_targets": ["inv:route-host-distinction"],
    "regenerated_targets": ["inv:route-host-distinction"],
    "novelty": [
      {
        "type": "NEW_DERIVATION",
        "statement": "For a k-regular host and spanning r-regular route, the residual is (k-r)-regular.",
        "discriminator": "Compare a cubic Hamiltonian cycle with a Hamiltonian path and a 4-regular host.",
        "receipt_ref": "receipt:novelty:degree-law"
      }
    ]
  },
  "pressure": [
    {"kind": "NEAREST_BORING", "status": "PASS", "receipt_ref": "receipt:p:boring"},
    {"kind": "METAPHOR_REMOVAL", "status": "PASS", "receipt_ref": "receipt:p:metaphor"},
    {"kind": "REPRESENTATION_SWAP", "status": "PASS", "receipt_ref": "receipt:p:representation"},
    {"kind": "RELABEL", "status": "PASS", "receipt_ref": "receipt:p:relabel"},
    {"kind": "HOLDOUT", "status": "PASS", "receipt_ref": "receipt:p:holdout"},
    {"kind": "REGENERATION_FAILURE", "status": "PASS", "receipt_ref": "receipt:p:regeneration"}
  ]
}
```

- [ ] **Step 2: Derive the four hostile sibling fixtures by changing only the discriminating field**

Create:

`no-new-dimension.json` — same structural case, but set `candidate.novelty` to `[]`; expected `NO_NEW_DIMENSION_EARNED`.

`partial-regeneration.json` — set baseline invariants and required targets to include `inv:opening-transition-distinction`, but regenerate only `inv:route-host-distinction`; expected `PARTIAL_SURVIVOR`.

`metaphor-failure.json` — keep the positive novelty but change only the `METAPHOR_REMOVAL` pressure status to `FAIL`; expected `PARTIAL_SURVIVOR` with `HOSTILE_PRESSURE_FAILED`.

`insufficient-baseline.json` — set `baseline.claims` and `baseline.invariants` both to empty lists; expected `INSUFFICIENT_BASELINE`.

Do not alter unrelated fields in each sibling; the fixtures are discriminators, not narrative variants.

- [ ] **Step 3: Add fixture-driven disposition tests**

Add imports to `tests/test_far_side_engine.py`:

```python
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FAR_SIDE_FIXTURES = ROOT / "tests" / "fixtures" / "far_side"


def load_far_side_fixture(name: str) -> dict:
    return json.loads((FAR_SIDE_FIXTURES / name).read_text(encoding="utf-8"))
```

Append tests:

```python
    def test_durable_survivor_fixture(self):
        result = evaluate_far_side_case(load_far_side_fixture("survivor.json"))
        self.assertEqual(result["final_status"], "FAR_SIDE_SURVIVOR")

    def test_durable_no_novelty_fixture(self):
        result = evaluate_far_side_case(load_far_side_fixture("no-new-dimension.json"))
        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")

    def test_durable_partial_fixture(self):
        result = evaluate_far_side_case(load_far_side_fixture("partial-regeneration.json"))
        self.assertEqual(result["final_status"], "PARTIAL_SURVIVOR")

    def test_durable_hostile_failure_fixture(self):
        result = evaluate_far_side_case(load_far_side_fixture("metaphor-failure.json"))
        self.assertEqual(result["final_status"], "PARTIAL_SURVIVOR")
        self.assertEqual(result["reason_code"], "HOSTILE_PRESSURE_FAILED")

    def test_durable_insufficient_baseline_fixture(self):
        result = evaluate_far_side_case(load_far_side_fixture("insufficient-baseline.json"))
        self.assertEqual(result["final_status"], "INSUFFICIENT_BASELINE")
```

- [ ] **Step 4: Run fixture tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_far_side_engine -v
```

Expected: all engine tests pass, including the five fixture-driven dispositions.

- [ ] **Step 5: Commit Task 4**

```bash
git add tests/fixtures/far_side tests/test_far_side_engine.py
git commit -m "test: add FAR-SIDE hostile sibling specimens"
```

---

### Task 5: Add a deterministic CLI adapter without promoting a public operator

**Files:**
- Create: `tools/far_side_lab.py`
- Create: `tests/test_far_side_cli.py`

**Interfaces:**
- CLI: `python tools/far_side_lab.py [PATH|-]`
- `PATH` omitted or `-` means read one JSON object from stdin.
- stdout is one canonical JSON result plus newline.
- exit code is `0` for all evaluated dispositions, including refusals/insufficient states; malformed JSON or unreadable input exits `2` and writes a concise error to stderr.

- [ ] **Step 1: Write failing CLI tests**

Create `tests/test_far_side_cli.py`:

```python
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOL = ROOT / "tools" / "far_side_lab.py"
FIXTURES = ROOT / "tests" / "fixtures" / "far_side"


class FarSideCliTests(unittest.TestCase):
    def test_file_input_emits_survivor_result(self):
        completed = subprocess.run(
            [sys.executable, str(TOOL), str(FIXTURES / "survivor.json")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["final_status"], "FAR_SIDE_SURVIVOR")

    def test_stdin_input_emits_no_novelty_as_success(self):
        payload = (FIXTURES / "no-new-dimension.json").read_text(encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(TOOL), "-"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            input=payload,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        result = json.loads(completed.stdout)
        self.assertEqual(result["final_status"], "NO_NEW_DIMENSION_EARNED")

    def test_malformed_json_exits_two_without_traceback(self):
        completed = subprocess.run(
            [sys.executable, str(TOOL), "-"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            input="{not-json",
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("invalid JSON", completed.stderr)
        self.assertNotIn("Traceback", completed.stderr)
```

- [ ] **Step 2: Run CLI tests and verify RED**

Run:

```bash
python -m unittest tests.test_far_side_cli -v
```

Expected: failure because `tools/far_side_lab.py` does not exist.

- [ ] **Step 3: Implement the CLI adapter**

Create `tools/far_side_lab.py`:

```python
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.digests import canonical_json_bytes
from experiments.far_side.engine import evaluate_far_side_case


def _read_payload(path: str) -> object:
    text = sys.stdin.read() if path == "-" else Path(path).read_text(encoding="utf-8")
    return json.loads(text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Evaluate one experimental FAR-SIDE receipt.")
    parser.add_argument("path", nargs="?", default="-", help="JSON file path or - for stdin")
    args = parser.parse_args(argv)

    try:
        payload = _read_payload(args.path)
    except (OSError, json.JSONDecodeError) as exc:
        message = "invalid JSON" if isinstance(exc, json.JSONDecodeError) else f"cannot read input: {exc}"
        print(message, file=sys.stderr)
        return 2

    result = evaluate_far_side_case(payload)
    sys.stdout.buffer.write(canonical_json_bytes(result) + b"\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: Run CLI tests and verify GREEN**

Run:

```bash
python -m unittest tests.test_far_side_cli -v
```

Expected: 3 tests pass.

- [ ] **Step 5: Verify byte-stable output for repeated identical input**

Run:

```bash
python tools/far_side_lab.py tests/fixtures/far_side/survivor.json > /tmp/far-side-a.json
python tools/far_side_lab.py tests/fixtures/far_side/survivor.json > /tmp/far-side-b.json
cmp /tmp/far-side-a.json /tmp/far-side-b.json
```

Expected: `cmp` exits `0` with no output.

- [ ] **Step 6: Commit Task 5**

```bash
git add tools/far_side_lab.py tests/test_far_side_cli.py
git commit -m "feat: add deterministic FAR-SIDE hostile lab CLI"
```

---

### Task 6: Full hostile verification and promotion-gate report

**Files:**
- Modify only if verification finds a defect in files created by Tasks 1–5.
- Do not modify public skill/runtime/schema files as part of this task.

**Interfaces:**
- No new interfaces. This task proves the executable slice and records what remains unearned.

- [ ] **Step 1: Run the FAR-SIDE focused suite**

Run:

```bash
python -m unittest \
  tests.test_far_side_model \
  tests.test_far_side_engine \
  tests.test_far_side_cli \
  -v
```

Expected: all FAR-SIDE tests pass with zero failures/errors.

- [ ] **Step 2: Run the entire existing repository suite**

Run:

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Expected: zero failures and zero errors.

- [ ] **Step 3: Verify the public ALEX surfaces were not changed**

Run:

```bash
git diff --name-only main...HEAD
```

Confirm the implementation commit set contains only:

```text
experiments/__init__.py
experiments/far_side/__init__.py
experiments/far_side/model.py
experiments/far_side/engine.py
tools/far_side_lab.py
tests/fixtures/far_side/...
tests/test_far_side_model.py
tests/test_far_side_engine.py
tests/test_far_side_cli.py
docs/superpowers/specs/2026-08-28-far-side-pass-practice-design.md
docs/superpowers/plans/2026-08-28-far-side-pass-m0-implementation.md
```

If `skills/alex/SKILL.md`, `alex_runtime/*`, `crucible/schema/*`, `crucible/profiles/*`, `README.md`, or LOADOUT files appear because of this feature branch, stop and separate/revert those edits before claiming completion.

- [ ] **Step 4: Run the explicit no-novelty proof**

Run:

```bash
python tools/far_side_lab.py tests/fixtures/far_side/no-new-dimension.json
```

Expected JSON contains:

```json
{"final_status":"NO_NEW_DIMENSION_EARNED"}
```

among its fields, exits `0`, and emits no claim of failure merely because the novelty delta is empty.

- [ ] **Step 5: Run the hostile kill proof**

Run:

```bash
python tools/far_side_lab.py tests/fixtures/far_side/metaphor-failure.json
```

Expected JSON contains:

```json
{
  "final_status": "PARTIAL_SURVIVOR",
  "reason_code": "HOSTILE_PRESSURE_FAILED",
  "pressure_failures": ["METAPHOR_REMOVAL"]
}
```

among its fields. This proves the favored candidate can lose status under a hostile sibling.

- [ ] **Step 6: Record the still-unearned promotion gates in the PR summary, not code**

The completion report must explicitly state that m0 still does **not** prove:

```text
semantic paraphrase equivalence
meaning-level novelty detection
automatic representation mutation
automatic simplicity generation
Dogram orchestration
public ALEX task-shape admission
Crucible conformance profile admission
skill-trigger admission
historical reconstruction
support / evidence / authority promotion
```

These are future gates, not defects to patch into m0.

- [ ] **Step 7: Commit any verification-only fixture/test corrections if needed**

If no corrections were necessary, do not create an empty commit.

If corrections were necessary:

```bash
git add experiments/far_side tools/far_side_lab.py tests/fixtures/far_side tests/test_far_side_*.py
git commit -m "test: harden FAR-SIDE hostile lab verification"
```

---

## Plan Self-Review

### Spec coverage

- Baseline capture: Tasks 1–2.
- At least three traversal axes: Tasks 1–3 and positive fixture in Task 4.
- Compression/regeneration distinction: Task 2.
- `(I, S, Delta)` executable pressure: invariants and regeneration in Task 2; novelty delta in Task 3; candidate statement remains in input receipt rather than being generated by the lab.
- `NO_NEW_DIMENSION_EARNED`: Tasks 2–5, explicitly re-proved in Task 6.
- Novelty typing: Tasks 1 and 3.
- Metaphor removal / representation swap / relabel / holdout / nearest-boring / regeneration-failure pressure: Task 3 contract and Task 4 fixtures.
- Search-for-novelty without forced novelty: exact no-novelty fixture and CLI success path.
- No authority minting: Task 2 test and Global Constraints.
- Dogram optional: no Dogram dependency anywhere in the plan.
- Replay/regeneration != historical identity: no historical occurrence API is exposed; output is limited to structural pressure fields.
- Implementation smaller than an autonomous research loop: generation and semantic interpretation are intentionally external.

### Intentional m0 limitations

The first slice does not attempt semantic equivalence, model-driven traversal generation, automatic hypothesis generation, or cross-repository orchestration. Exact normalized statement comparison is intentionally conservative and is documented as such. A future promotion would require independent pressure on paraphrase/relabel invariance before changing this boundary.

### Placeholder scan

No `TBD`, `TODO`, “implement later,” unspecified error handling, or unnamed tests are present. Every task has exact files, commands, expected results, and interfaces.

### Type consistency

The plan uses one evaluator signature throughout:

```python
evaluate_far_side_case(case: object) -> dict[str, object]
```

and one stable result envelope throughout Tasks 2–6. Novelty and pressure constants are defined once in Task 1 and imported by Task 2 onward.
