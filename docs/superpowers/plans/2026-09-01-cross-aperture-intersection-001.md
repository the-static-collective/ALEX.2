# CROSS-APERTURE-INTERSECTION-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build one experimental ALEX evaluator that intersects finite, explicitly declared observer fibers while preserving ordered compatible-set lineage and refusing representative invention.

**Architecture:** Add one pure standard-library module under `alex_runtime/` with no imports from 3rdi, LOADOUT, Dogram, or existing projection evaluators. Drive it from one frozen JSON fixture and one focused `unittest` file, growing behavior through RED → GREEN commits. Keep the implementation private to the research branch: no `alex_runtime.__init__` export, public operator, schema, skill trigger, support predicate, or authority surface.

**Tech Stack:** Python 3.12 standard library, `unittest`, JSON fixtures, existing GitHub Actions `python -m unittest discover -s tests -v` workflow.

**Spec:** `docs/superpowers/specs/2026-09-01-cross-aperture-intersection-001-design.md`

## Global Constraints

- V0 input is a finite declared world domain plus one or more complete declared observation maps and observed outputs.
- Core recurrence is `F_i = F_(i-1) ∩ P_i^-1(y_i)` in supplied cut order.
- Cut effects are exactly `REFINE`, `REDUNDANT`, or `BREAK`.
- Terminal dispositions are exactly `FOG`, `IDENTIFIED_WITHIN_DECLARED_MODEL`, `MODEL_BREAK`, or `INSUFFICIENT_TO_TEST` for malformed input.
- Missing `relation_declaration` normalizes to `unknown`; supplied values are limited to `independent`, `correlated`, or `unknown`.
- Correlation/independence metadata never changes set intersection in v0.
- Non-singleton compatible sets never receive a representative or selection basis.
- Singleton exposure uses only `selection_basis = "singleton_in_declared_model"`; this is not a tie-break or universal truth claim.
- Empty intersection preserves lineage and does not diagnose why the model broke.
- Every returned result carries `authority = "none"`.
- No cross-repo runtime dependency, public operator/schema/skill promotion, support/evidence promotion, or existing projection semantic change.

---

### Task 1: Freeze the canonical specimen and earn the first executable path

**Files:**
- Create: `tests/fixtures/cross_aperture_intersection_001.json`
- Create: `tests/test_cross_aperture_intersection.py`
- Create after RED: `alex_runtime/cross_aperture_intersection.py`

**Interfaces:**
- Consumes: plain `dict` cases loaded from JSON.
- Produces: `evaluate_cross_aperture_case(case: dict) -> dict`.
- The module stays unexported from `alex_runtime/__init__.py`.

- [ ] **Step 1: Create the frozen canonical fixture**

Create `tests/fixtures/cross_aperture_intersection_001.json` with this exact first case and room for later hostile cases:

```json
{
  "canonical": {
    "case_id": "cross-aperture-001",
    "world_domain_id": "world-eight-v0",
    "world_states": ["a", "b", "c", "d", "e", "f", "g", "h"],
    "cuts": [
      {
        "cut_id": "A",
        "map_id": "P_A",
        "map": {"a":"0","b":"0","c":"0","d":"0","e":"1","f":"1","g":"1","h":"1"},
        "observed": "0",
        "relation_declaration": "unknown"
      },
      {
        "cut_id": "B",
        "map_id": "P_B",
        "map": {"a":"0","b":"0","c":"1","d":"1","e":"0","f":"0","g":"1","h":"1"},
        "observed": "0",
        "relation_declaration": "independent"
      },
      {
        "cut_id": "C",
        "map_id": "P_C",
        "map": {"a":"0","b":"1","c":"0","d":"1","e":"0","f":"1","g":"0","h":"1"},
        "observed": "0",
        "relation_declaration": "unknown"
      }
    ]
  }
}
```

- [ ] **Step 2: Write the first failing canonical test**

Create `tests/test_cross_aperture_intersection.py`:

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
        self.assertIsNone(result["reason_code"])
        self.assertEqual([len(step["compatible_after"]) for step in result["lineage"]], [4, 2, 1])
        self.assertEqual([step["effect"] for step in result["lineage"]], ["REFINE", "REFINE", "REFINE"])
        self.assertEqual(result["final_compatible_states"], ["a"])
        self.assertEqual(result["unique_representative"], "a")
        self.assertEqual(result["selection_basis"], "singleton_in_declared_model")
        self.assertEqual(result["authority"], "none")
```

- [ ] **Step 3: Verify RED on the exact test commit**

Run through the PR workflow or local checkout:

```bash
python -m unittest tests.test_cross_aperture_intersection.CrossApertureIntersectionTests.test_canonical_three_cut_lineage_identifies_only_within_declared_model -v
```

Expected: FAIL/ERROR because `alex_runtime.cross_aperture_intersection` does not exist. Record the exact failing commit/workflow receipt before production code is created.

- [ ] **Step 4: Implement the minimum canonical evaluator**

Create `alex_runtime/cross_aperture_intersection.py` with the smallest pure implementation that validates the canonical shape and computes ordered fibers from supplied map values. Use supplied `world_states` order when materializing every list. The result must include:

```python
{
    "case_id": case["case_id"],
    "world_domain_id": case["world_domain_id"],
    "disposition": "IDENTIFIED_WITHIN_DECLARED_MODEL",
    "reason_code": None,
    "initial_compatible_states": list(case["world_states"]),
    "lineage": lineage,
    "final_compatible_states": ["a"],
    "unique_representative": "a",
    "selection_basis": "singleton_in_declared_model",
    "authority": "none",
}
```

Do not add malformed-input reason codes or special hostile-case logic yet.

- [ ] **Step 5: Verify GREEN**

Run:

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
```

Expected: focused test PASS; whole suite PASS.

- [ ] **Step 6: Commit the canonical GREEN**

```bash
git add alex_runtime/cross_aperture_intersection.py tests/fixtures/cross_aperture_intersection_001.json tests/test_cross_aperture_intersection.py
git commit -m "experiment: add cross-aperture canonical intersection"
```

---

### Task 2: Preserve fog, redundancy, correlation metadata, and model break

**Files:**
- Modify: `tests/fixtures/cross_aperture_intersection_001.json`
- Modify: `tests/test_cross_aperture_intersection.py`
- Modify: `alex_runtime/cross_aperture_intersection.py`

**Interfaces:**
- Consumes: the same `evaluate_cross_aperture_case(case: dict) -> dict` API.
- Produces: generic valid-case terminal semantics and lineage effects without adding new public interfaces.

- [ ] **Step 1: Add hostile valid cases to the fixture**

Add these named cases, each using the same eight-state domain and complete maps:

```text
non_singleton_fog:
  cuts = canonical A, canonical B
  expected sizes = 4,2

redundant_aperture:
  A as canonical first cut
  A2 with distinct cut_id/map_id but identical map and observed output
  expected sizes = 4,4
  expected second effect = REDUNDANT

correlated_agreement:
  same set behavior as redundant_aperture
  second relation_declaration = correlated
  expected set result unchanged by metadata

model_break:
  first cut leaves {a,b,c,d}
  second complete map has observed output whose fiber is {e,f,g,h}
  expected sizes = 4,0
```

- [ ] **Step 2: Write failing terminal-behavior tests**

Append tests equivalent to:

```python
def test_non_singleton_fog_never_selects_representative(self) -> None:
    result = evaluate_cross_aperture_case(load_case("non_singleton_fog"))
    self.assertEqual(result["disposition"], "FOG")
    self.assertEqual(result["reason_code"], "NON_SINGLETON_COMPATIBLE_SET")
    self.assertEqual(result["final_compatible_states"], ["a", "b"])
    self.assertIsNone(result["unique_representative"])
    self.assertIsNone(result["selection_basis"])


def test_redundant_aperture_preserves_family(self) -> None:
    result = evaluate_cross_aperture_case(load_case("redundant_aperture"))
    self.assertEqual([step["effect"] for step in result["lineage"]], ["REFINE", "REDUNDANT"])
    self.assertEqual(result["lineage"][1]["compatible_before"], ["a", "b", "c", "d"])
    self.assertEqual(result["lineage"][1]["compatible_after"], ["a", "b", "c", "d"])


def test_correlation_metadata_does_not_change_intersection(self) -> None:
    result = evaluate_cross_aperture_case(load_case("correlated_agreement"))
    self.assertEqual(result["lineage"][1]["relation_declaration"], "correlated")
    self.assertEqual(result["lineage"][1]["effect"], "REDUNDANT")
    self.assertEqual(result["final_compatible_states"], ["a", "b", "c", "d"])


def test_empty_intersection_is_model_break_not_reality_verdict(self) -> None:
    result = evaluate_cross_aperture_case(load_case("model_break"))
    self.assertEqual(result["disposition"], "MODEL_BREAK")
    self.assertEqual(result["reason_code"], "INCONSISTENT_OBSERVATIONS")
    self.assertEqual(result["lineage"][-1]["effect"], "BREAK")
    self.assertEqual(result["final_compatible_states"], [])
    self.assertIsNone(result["unique_representative"])
    self.assertIsNone(result["selection_basis"])
    self.assertEqual(result["authority"], "none")
```

- [ ] **Step 3: Verify RED**

Run:

```bash
python -m unittest tests.test_cross_aperture_intersection -v
```

Expected: at least one new test fails because the Task 1 implementation only supports the canonical terminal path.

- [ ] **Step 4: Generalize valid-case evaluation minimally**

Refactor only enough to:

```python
if not compatible_after:
    effect = "BREAK"
elif compatible_after == compatible_before:
    effect = "REDUNDANT"
else:
    effect = "REFINE"
```

After all cuts:

```python
if len(final_states) == 0:
    disposition = "MODEL_BREAK"
    reason_code = "INCONSISTENT_OBSERVATIONS"
    unique_representative = None
    selection_basis = None
elif len(final_states) == 1:
    disposition = "IDENTIFIED_WITHIN_DECLARED_MODEL"
    reason_code = None
    unique_representative = final_states[0]
    selection_basis = "singleton_in_declared_model"
else:
    disposition = "FOG"
    reason_code = "NON_SINGLETON_COMPATIBLE_SET"
    unique_representative = None
    selection_basis = None
```

Normalize absent `relation_declaration` to `unknown` when constructing lineage, but do not yet add full malformed-input refusal handling.

- [ ] **Step 5: Verify GREEN and whole-suite non-regression**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
```

Expected: all focused and repository tests PASS.

- [ ] **Step 6: Commit the valid hostile controls**

```bash
git add alex_runtime/cross_aperture_intersection.py tests/fixtures/cross_aperture_intersection_001.json tests/test_cross_aperture_intersection.py
git commit -m "test: pressure cross-aperture terminal states"
```

---

### Task 3: Add stable malformed-input refusals and anti-laundering controls

**Files:**
- Modify: `tests/fixtures/cross_aperture_intersection_001.json`
- Modify: `tests/test_cross_aperture_intersection.py`
- Modify: `alex_runtime/cross_aperture_intersection.py`

**Interfaces:**
- Consumes: unchanged `evaluate_cross_aperture_case(case: dict) -> dict`.
- Produces: stable `INSUFFICIENT_TO_TEST` receipts for the spec's exact malformed-input reason codes.

- [ ] **Step 1: Add malformed cases**

Add fixture cases that isolate each refusal:

```text
invalid_world_domain        -> empty world_states
invalid_cuts                -> empty cuts
 duplicate_cut_id           -> two cuts share cut_id
 duplicate_map_id           -> two cuts share map_id
 incomplete_observation_map -> one world-state key omitted
 invalid_map_output         -> one map output is empty string
 invalid_observed_output    -> observed is empty string
 invalid_relation           -> relation_declaration = "trusted"
 missing_relation           -> omit relation_declaration entirely; this is VALID and normalizes to unknown
```

Also test a non-dict call directly for `MALFORMED_CASE`.

- [ ] **Step 2: Write failing refusal tests**

Add a table-driven test:

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
    self.assertEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
    self.assertEqual(result["reason_code"], "MALFORMED_CASE")


def test_missing_relation_declaration_normalizes_to_unknown(self) -> None:
    result = evaluate_cross_aperture_case(load_case("missing_relation"))
    self.assertNotEqual(result["disposition"], "INSUFFICIENT_TO_TEST")
    self.assertEqual(result["lineage"][0]["relation_declaration"], "unknown")
```

- [ ] **Step 3: Verify RED**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
```

Expected: malformed-input tests fail because stable validation receipts are not implemented yet.

- [ ] **Step 4: Implement validation with fixed precedence**

Add a private helper returning malformed receipts with exactly this shape:

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

Use this validation precedence so one malformed case cannot drift between reason codes:

```text
1. MALFORMED_CASE
2. INVALID_WORLD_DOMAIN
3. INVALID_CUTS
4. DUPLICATE_CUT_ID
5. DUPLICATE_MAP_ID
6. INCOMPLETE_OBSERVATION_MAP
7. INVALID_MAP_OUTPUT
8. INVALID_OBSERVED_OUTPUT
9. INVALID_RELATION_DECLARATION
```

Do not reject an observed value merely because no world maps to it; that is a valid observation producing an empty fiber and therefore `MODEL_BREAK`, not malformed input.

- [ ] **Step 5: Verify GREEN and whole suite**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
```

Expected: focused suite PASS; entire repository suite PASS.

- [ ] **Step 6: Commit validation**

```bash
git add alex_runtime/cross_aperture_intersection.py tests/fixtures/cross_aperture_intersection_001.json tests/test_cross_aperture_intersection.py
git commit -m "experiment: harden cross-aperture refusal receipts"
```

---

### Task 4: Final authority and isolation verification

**Files:**
- Modify only if a failing guard requires it: `tests/test_cross_aperture_intersection.py`
- Do not modify: `alex_runtime/__init__.py`, existing projection evaluators, workflow configuration, skills, schemas, or cross-repo packages.

**Interfaces:**
- No new interfaces. This task verifies the branch contract.

- [ ] **Step 1: Add a static isolation test if not already explicit**

```python
def test_experimental_module_does_not_import_owner_runtimes_or_mint_authority(self) -> None:
    source = (Path(__file__).parents[1] / "alex_runtime" / "cross_aperture_intersection.py").read_text(encoding="utf-8")
    for forbidden in ("3rdi", "loadout", "dogram", "projection_invariance", "projection_break"):
        self.assertNotIn(f"import {forbidden}", source.lower())
        self.assertNotIn(f"from {forbidden}", source.lower())
    self.assertNotIn('"authority": "', source.replace('"authority": "none"', ""))
```

If this test is newly added, first run it and confirm whether it passes or exposes an actual boundary defect. Do not manufacture a failure if the boundary is already satisfied.

- [ ] **Step 2: Run final verification**

```bash
python -m unittest tests.test_cross_aperture_intersection -v
python -m unittest discover -s tests -v
python -m compileall -q alex_runtime
```

Expected: all commands exit 0.

- [ ] **Step 3: Inspect the final diff**

Expected effective implementation delta against the approved design head:

```text
alex_runtime/cross_aperture_intersection.py
 tests/fixtures/cross_aperture_intersection_001.json
 tests/test_cross_aperture_intersection.py
 docs/superpowers/plans/2026-09-01-cross-aperture-intersection-001.md
```

No other runtime, schema, workflow, public export, or cross-repo file should change.

- [ ] **Step 4: Record the exact final head and CI receipt**

Require the PR-triggered GitHub Actions `crucible-contract` workflow on the exact final head to complete successfully before calling the implementation green.

- [ ] **Step 5: Leave implementation PR draft unless a separate landing approval is given**

The implementation PR is evidence for review. Technical GREEN does not itself authorize merge, public promotion, or runtime canonization.
