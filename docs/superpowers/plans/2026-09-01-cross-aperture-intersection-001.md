# CROSS-APERTURE-INTERSECTION-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build one experimental ALEX evaluator that intersects finite declared observer fibers while preserving ordered compatible-set lineage and refusing representative invention.

**Architecture:** Add one pure standard-library module under `alex_runtime/`, one frozen JSON fixture, and one focused `unittest` file. Grow the evaluator through explicit RED → GREEN commits. Do not export it from `alex_runtime.__init__`, alter existing projection evaluators, or add cross-repo runtime dependencies.

**Tech Stack:** Python 3.12 standard library, `unittest`, JSON fixtures, existing GitHub Actions `python -m unittest discover -s tests -v` workflow.

**Spec:** `docs/superpowers/specs/2026-09-01-cross-aperture-intersection-001-design.md`

## Global Constraints

- Compute `F_i = F_(i-1) ∩ P_i^-1(y_i)` in supplied cut order.
- Preserve supplied `world_states` order in every emitted state list.
- Cut effects are exactly `REFINE`, `REDUNDANT`, or `BREAK`.
- Terminal dispositions are `FOG`, `IDENTIFIED_WITHIN_DECLARED_MODEL`, `MODEL_BREAK`, or `INSUFFICIENT_TO_TEST` for malformed input.
- Missing `relation_declaration` normalizes to `unknown`; valid supplied values are `independent`, `correlated`, `unknown`.
- Relation metadata never changes set intersection in v0.
- Non-singleton compatible sets never receive a representative or selection basis.
- Singleton exposure uses only `selection_basis = "singleton_in_declared_model"`.
- Empty intersection preserves lineage and does not diagnose cause.
- Every result carries `authority = "none"`.
- No 3rdi/LOADOUT/Dogram imports, public operator/schema/skill promotion, support/evidence promotion, or existing projection semantic changes.

---

### Task 1: Canonical RED → GREEN

**Files:**
- Create: `tests/fixtures/cross_aperture_intersection_001.json`
- Create: `tests/test_cross_aperture_intersection.py`
- Create after RED: `alex_runtime/cross_aperture_intersection.py`

**Interfaces:**
- Produces: `evaluate_cross_aperture_case(case: dict) -> dict`.

- [ ] **Step 1: Freeze the canonical fixture**

```json
{
  "canonical": {
    "case_id": "cross-aperture-001",
    "world_domain_id": "world-eight-v0",
    "world_states": ["a","b","c","d","e","f","g","h"],
    "cuts": [
      {"cut_id":"A","map_id":"P_A","map":{"a":"0","b":"0","c":"0","d":"0","e":"1","f":"1","g":"1","h":"1"},"observed":"0","relation_declaration":"unknown"},
      {"cut_id":"B","map_id":"P_B","map":{"a":"0","b":"0","c":"1","d":"1","e":"0","f":"0","g":"1","h":"1"},"observed":"0","relation_declaration":"independent"},
      {"cut_id":"C","map_id":"P_C","map":{"a":"0","b":"1","c":"0","d":"1","e":"0","f":"1","g":"0","h":"1"},"observed":"0","relation_declaration":"unknown"}
    ]
  }
}
```

- [ ] **Step 2: Write the failing canonical test**

```python
from __future__ import annotations

import json
import unittest
from pathlib import Path

from alex_runtime.cross_aperture_intersection import evaluate_cross_aperture_case

FIXTURE = Path(__file__).parent / "fixtures" / "cross_aperture_intersection_001.json"


def load_case(name: str) -> dict:
    return json.loads(FIXTURE.read_text(encoding="utf-8"))[name]


class CrossApertureIntersectionTests(unittest.TestCase):
    def test_canonical_three_cut_lineage_identifies_only_within_declared_model(self) -> None:
        result = evaluate_cross_aperture_case(load_case("canonical"))
        self.assertEqual(result["disposition"], "IDENTIFIED_WITHIN_DECLARED_MODEL")
        self.assertEqual([len(step["compatible_after"]) for step in result["lineage"]], [4, 2, 1])
        self.assertEqual([step["effect"] for step in result["lineage"]], ["REFINE", "REFINE", "REFINE"])
        self.assertEqual(result["final_compatible_states"], ["a"])
        self.assertEqual(result["unique_representative"], "a")
        self.assertEqual(result["selection_basis"], "singleton_in_declared_model")
        self.assertEqual(result["authority"], "none")
```

- [ ] **Step 3: Verify RED**

Run:

```bash
python -m unittest tests.test_cross_aperture_intersection.CrossApertureIntersectionTests.test_canonical_three_cut_lineage_identifies_only_within_declared_model -v
```

Expected: import failure because `alex_runtime.cross_aperture_intersection` does not yet exist.

- [ ] **Step 4: Implement the minimum canonical evaluator**

Create `alex_runtime/cross_aperture_intersection.py` with only enough generic set-intersection logic to make the canonical test pass. Preserve world-state order when materializing fibers and compatible sets. Do not add malformed-input reason codes yet.

- [ ] **Step 5: Verify GREEN**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
```

Expected: focused and whole-suite PASS.

---

### Task 2: Valid hostile states

**Files:**
- Modify: `tests/fixtures/cross_aperture_intersection_001.json`
- Modify: `tests/test_cross_aperture_intersection.py`
- Modify: `alex_runtime/cross_aperture_intersection.py`

**Interfaces:** unchanged `evaluate_cross_aperture_case(case: dict) -> dict`.

- [ ] **Step 1: Add fixture cases**

Add:

```text
non_singleton_fog: canonical A+B -> {a,b}
redundant_aperture: canonical A followed by a distinct id with same map/output -> 4 then 4
correlated_agreement: same as redundant but relation_declaration=correlated
model_break: first cut -> {a,b,c,d}; second observed fiber -> {e,f,g,h}; intersection -> empty
```

- [ ] **Step 2: Add failing tests**

```python
def test_non_singleton_fog_never_selects_representative(self) -> None:
    result = evaluate_cross_aperture_case(load_case("non_singleton_fog"))
    self.assertEqual(result["disposition"], "FOG")
    self.assertEqual(result["reason_code"], "NON_SINGLETON_COMPATIBLE_SET")
    self.assertEqual(result["final_compatible_states"], ["a", "b"])
    self.assertIsNone(result["unique_representative"])
    self.assertIsNone(result["selection_basis"])


def test_redundant_and_correlated_cuts_do_not_gain_information_by_title(self) -> None:
    redundant = evaluate_cross_aperture_case(load_case("redundant_aperture"))
    correlated = evaluate_cross_aperture_case(load_case("correlated_agreement"))
    self.assertEqual(redundant["lineage"][-1]["effect"], "REDUNDANT")
    self.assertEqual(correlated["lineage"][-1]["effect"], "REDUNDANT")
    self.assertEqual(correlated["lineage"][-1]["relation_declaration"], "correlated")
    self.assertEqual(redundant["final_compatible_states"], correlated["final_compatible_states"])


def test_empty_intersection_is_model_break(self) -> None:
    result = evaluate_cross_aperture_case(load_case("model_break"))
    self.assertEqual(result["disposition"], "MODEL_BREAK")
    self.assertEqual(result["reason_code"], "INCONSISTENT_OBSERVATIONS")
    self.assertEqual(result["lineage"][-1]["effect"], "BREAK")
    self.assertEqual(result["final_compatible_states"], [])
    self.assertIsNone(result["unique_representative"])
```

- [ ] **Step 3: Verify RED**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
```

Expected: at least one new terminal-state test fails.

- [ ] **Step 4: Generalize valid-case terminal logic**

Use exactly:

```python
if not compatible_after:
    effect = "BREAK"
elif compatible_after == compatible_before:
    effect = "REDUNDANT"
else:
    effect = "REFINE"
```

and:

```python
if len(final_states) == 0:
    disposition, reason = "MODEL_BREAK", "INCONSISTENT_OBSERVATIONS"
    representative, basis = None, None
elif len(final_states) == 1:
    disposition, reason = "IDENTIFIED_WITHIN_DECLARED_MODEL", None
    representative, basis = final_states[0], "singleton_in_declared_model"
else:
    disposition, reason = "FOG", "NON_SINGLETON_COMPATIBLE_SET"
    representative, basis = None, None
```

Normalize absent `relation_declaration` to `unknown` in lineage.

- [ ] **Step 5: Verify GREEN**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
```

Expected: PASS.

---

### Task 3: Stable malformed-input refusals

**Files:** same three implementation/test files.

**Interfaces:** malformed inputs return `INSUFFICIENT_TO_TEST` with empty lineage and `authority: none`.

- [ ] **Step 1: Add malformed fixture cases**

```text
invalid_world_domain        -> empty world_states
invalid_cuts                -> empty cuts
duplicate_cut_id            -> repeated cut_id
duplicate_map_id            -> repeated map_id
incomplete_observation_map  -> one world key omitted
invalid_map_output          -> one empty map output
invalid_observed_output     -> observed=""
invalid_relation            -> relation_declaration="trusted"
missing_relation            -> relation_declaration omitted; VALID and normalizes to unknown
```

- [ ] **Step 2: Add failing refusal tests**

```python
def test_malformed_cases_return_stable_reason_codes(self) -> None:
    expectations = {
        "invalid_world_domain": "INVALID_WORLD_DOMAIN",
        "invalid_cuts": "INVALID_CUTS",
        "duplicate_cut_id": "DUPLICATE_CUT_ID",
        "duplicate_map_id": "DUPLICATE_MAP_ID",
        "incomplete_observation_map": "INCOMPLETE_OBSERVATION_MAP",
        "invalid_map_output": "INVALID_MAP_OUTPUT",
        "invalid_observed_output": "INVALID_OBSERVED_OUTPUT",
        "invalid_relation": "INVALID_RELATION_DECLARATION",
    }
    for name, reason in expectations.items():
        with self.subTest(name=name):
            result = evaluate_cross_aperture_case(load_case(name))
            self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
            self.assertEqual(result["reason_code"], reason)
            self.assertEqual(result["lineage"], [])
            self.assertEqual(result["authority"], "none")


def test_non_dict_case_is_malformed(self) -> None:
    result = evaluate_cross_aperture_case(None)
    self.assertEqual(result["reason_code"], "MALFORMED_CASE")


def test_missing_relation_normalizes_to_unknown(self) -> None:
    result = evaluate_cross_aperture_case(load_case("missing_relation"))
    self.assertNotEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
    self.assertEqual(result["lineage"][0]["relation_declaration"], "unknown")
```

- [ ] **Step 3: Verify RED**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
```

Expected: malformed-input tests fail.

- [ ] **Step 4: Implement validation with fixed precedence**

Use this exact precedence:

```text
MALFORMED_CASE
INVALID_WORLD_DOMAIN
INVALID_CUTS
DUPLICATE_CUT_ID
DUPLICATE_MAP_ID
INCOMPLETE_OBSERVATION_MAP
INVALID_MAP_OUTPUT
INVALID_OBSERVED_OUTPUT
INVALID_RELATION_DECLARATION
```

Malformed result shape:

```python
{
    "case_id": best_case_id,
    "world_domain_id": best_world_domain_id,
    "disposition": "INSUFFICIENT_TO_TEST",
    "reason_code": reason_code,
    "initial_compatible_states": [],
    "lineage": [],
    "final_compatible_states": [],
    "unique_representative": None,
    "selection_basis": None,
    "authority": "none",
}
```

Do not reject an observed output merely because its fiber is empty; that is valid input leading to `MODEL_BREAK`.

- [ ] **Step 5: Verify GREEN**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
```

Expected: PASS.

---

### Task 4: Isolation and final verification

**Files:**
- Modify if needed: `tests/test_cross_aperture_intersection.py`
- Do not modify: `alex_runtime/__init__.py`, existing projection evaluators, workflows, schemas, skills.

- [ ] **Step 1: Add/verify a static isolation guard**

```python
def test_experimental_module_stays_owner_local_and_authority_free(self) -> None:
    source = (Path(__file__).parents[1] / "alex_runtime" / "cross_aperture_intersection.py").read_text(encoding="utf-8").lower()
    for forbidden in ("3rdi", "loadout", "dogram", "projection_invariance", "projection_break"):
        self.assertNotIn(f"import {forbidden}", source)
        self.assertNotIn(f"from {forbidden}", source)
```

- [ ] **Step 2: Run final verification**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
python -m compileall -q alex_runtime
```

Expected: all exit 0.

- [ ] **Step 3: Diff gate**

Effective implementation delta against the design branch must be exactly:

```text
alex_runtime/cross_aperture_intersection.py
tests/fixtures/cross_aperture_intersection_001.json
tests/test_cross_aperture_intersection.py
docs/superpowers/plans/2026-09-01-cross-aperture-intersection-001.md
```

- [ ] **Step 4: Exact-head CI gate**

Require the existing `crucible-contract` GitHub Actions workflow on the exact final implementation head to succeed before calling the branch GREEN.

- [ ] **Step 5: Landing boundary**

Leave the implementation PR draft. Technical GREEN does not authorize merge or semantic/runtime promotion.
