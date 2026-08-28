# BINOCULAR-RECURSION-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a pure ALEX evaluator and JSON CLI that audit supplied binocular research traces for lawful compression/expansion tension without generating claims, adding premises, or minting authority.

**Architecture:** Add one pure `dict -> dict` evaluator in `alex_runtime/binocular_recursion.py`, following the existing `projection_break.py` pattern. The evaluator validates the approved machine contract, preserves ordered traversal, enforces constitutional refusals, computes deterministic binocular-state digests for terminal checks, and returns formation-contract results only. A thin standard-library CLI reads one JSON object from stdin or a file and writes one JSON result. The ALEX skill gets a reference page that explains when to use the protocol and what it cannot establish.

**Tech Stack:** Python standard library only: `json`, `hashlib`, `argparse`, `sys`, `pathlib`, `copy`, `subprocess`; `unittest` for tests.

**Spec:** `docs/superpowers/specs/2026-08-28-binocular-recursion-design.md`, `docs/superpowers/specs/2026-08-28-binocular-recursion-machine-contract.md`, `docs/superpowers/specs/2026-08-28-binocular-recursion-machine-contract-amendment.md`

## Global Constraints

- Public evaluator signature: `evaluate_binocular_recursion_case(case: dict) -> dict[str, object]`.
- The evaluator audits a supplied trace; it does not generate compression proposals, perform open-ended consequence search, interpret prose, or decide whether a researched claim is true.
- `discovery_trigger_refs`, `support_refs`, `admitted_premise_refs`, and `unresolved_premise_refs` remain distinct sets.
- `claim_support_refs ∩ discovery_trigger_refs == ∅` or return `REFUSE / DISCOVERY_TRIGGER_AS_SUPPORT`.
- Expansion may use only admitted premises plus branch-local explicitly introduced premises or return `REFUSE / UNDECLARED_PREMISE_INJECTION`.
- Live consequences with status `ENTAILED`, `INFERRED`, or `UNRESOLVED` may not be erased by compression unless explicitly withdrawn by the update.
- A material trajectory is an ordered list with repetitions preserved exactly; it is never sorted or deduplicated.
- Field changes require an attributable update receipt; authority must remain equal to the case-level authority digest.
- Successful terminal labels are only `FIXED`, `CYCLE`, `RESIDUAL`, and `DIVERGENT`.
- `pass_limit` is required, integer, at least 1, and bounds `len(passes)`.
- No external dependency, network call, model call, hidden time dependence, randomness, or filesystem mutation inside evaluator logic.
- The evaluator must not mutate the input case.
- `ACCEPT` means formation-contract acceptance only; it is not acceptance of a researched claim as true.

---

## File map

```text
alex_runtime/binocular_recursion.py
  Pure evaluator, validation helpers, canonical state digest, terminal checks.

tools/run_binocular_recursion.py
  JSON transport only; no research semantics.

tests/fixtures/binocular_recursion/lawful-residual.json
  Canonical accepted residual specimen.

tests/fixtures/binocular_recursion/fixed.json
  Canonical fixed specimen.

tests/fixtures/binocular_recursion/cycle.json
  Canonical cycle specimen.

tests/fixtures/binocular_recursion/divergent.json
  Canonical bounded divergent specimen.

tests/test_binocular_recursion.py
  Evaluator and hostile-contract tests.

tests/test_run_binocular_recursion.py
  CLI transport tests.

skills/alex/references/binocular-recursion.md
  Human-facing research protocol and non-collapse rules.

skills/alex/SKILL.md
  One routing paragraph to the new reference.

tests/test_binocular_recursion_reference.py
  Documentation contract test.
```

---

### Task 1: Build the pure evaluator around one lawful residual specimen

**Files:**
- Create: `alex_runtime/binocular_recursion.py`
- Create: `tests/fixtures/binocular_recursion/lawful-residual.json`
- Create: `tests/test_binocular_recursion.py`

**Interfaces:**
- Consumes: a decoded `alex.binocular-recursion-case/v0` dictionary.
- Produces: `evaluate_binocular_recursion_case(case: dict) -> dict[str, object]`.

- [ ] **Step 1: Create the lawful residual fixture**

Use this complete fixture as `tests/fixtures/binocular_recursion/lawful-residual.json`:

```json
{
  "schema": "alex.binocular-recursion-case/v0",
  "case_id": "lawful-residual",
  "initial_field_digest": "sha256:field-0",
  "authority_digest": "sha256:authority-0",
  "pass_limit": 4,
  "admitted_premise_refs": ["p1", "p2"],
  "unresolved_premise_refs": ["u1"],
  "discovery_trigger_refs": ["trigger:prompt-001"],
  "support_refs": ["source:r1", "source:r2"],
  "terminal": "RESIDUAL",
  "passes": [
    {
      "pass_index": 0,
      "pre_field_digest": "sha256:field-0",
      "trajectory": ["A", "B", "A"],
      "trajectory_order_material": true,
      "compression": {
        "profile_digest": "sha256:compress-v1",
        "proposal_digest": "sha256:proposal-0",
        "formation_basis_refs": ["p1", "p2", "trigger:prompt-001"],
        "claim_support_refs": ["source:r1"],
        "reexpanded_live_consequence_refs": ["c1"]
      },
      "expansion": {
        "profile_digest": "sha256:expand-v1",
        "branches": [
          {
            "branch_id": "b1",
            "parent_refs": ["p1"],
            "rule_ref": "rule:r1",
            "condition_refs": [],
            "consequence_ref": "c1",
            "status": "INFERRED",
            "used_premise_refs": ["p1"],
            "introduced_premise_refs": []
          }
        ]
      },
      "tensions": [
        {
          "type": "STABLE_MATCH",
          "left_refs": ["sha256:proposal-0"],
          "right_refs": ["c1"],
          "receipt_refs": ["receipt:t0"]
        }
      ],
      "update": {
        "kind": "NONE",
        "receipt_refs": [],
        "admit_premise_refs": [],
        "withdraw_premise_refs": [],
        "withdraw_consequence_refs": [],
        "authority_digest": "sha256:authority-0"
      },
      "post_field_digest": "sha256:field-0"
    },
    {
      "pass_index": 1,
      "pre_field_digest": "sha256:field-0",
      "trajectory": ["A", "B", "A", "C"],
      "trajectory_order_material": true,
      "compression": {
        "profile_digest": "sha256:compress-v1",
        "proposal_digest": "sha256:proposal-1",
        "formation_basis_refs": ["p1", "p2"],
        "claim_support_refs": ["source:r1", "source:r2"],
        "reexpanded_live_consequence_refs": ["c1", "c2"]
      },
      "expansion": {
        "profile_digest": "sha256:expand-v1",
        "branches": [
          {
            "branch_id": "b1",
            "parent_refs": ["p1"],
            "rule_ref": "rule:r1",
            "condition_refs": [],
            "consequence_ref": "c1",
            "status": "INFERRED",
            "used_premise_refs": ["p1"],
            "introduced_premise_refs": []
          },
          {
            "branch_id": "b2",
            "parent_refs": ["p2"],
            "rule_ref": "rule:r2",
            "condition_refs": [],
            "consequence_ref": "c2",
            "status": "UNRESOLVED",
            "used_premise_refs": ["p2"],
            "introduced_premise_refs": []
          }
        ]
      },
      "tensions": [
        {
          "type": "UNEXPLAINED_RESIDUAL",
          "left_refs": ["sha256:proposal-1"],
          "right_refs": ["c2"],
          "receipt_refs": ["receipt:t1"]
        }
      ],
      "update": {
        "kind": "NONE",
        "receipt_refs": [],
        "admit_premise_refs": [],
        "withdraw_premise_refs": [],
        "withdraw_consequence_refs": [],
        "authority_digest": "sha256:authority-0"
      },
      "post_field_digest": "sha256:field-0"
    }
  ]
}
```

- [ ] **Step 2: Write the initial failing tests**

Create `tests/test_binocular_recursion.py` with this nucleus:

```python
import copy
import json
import unittest
from pathlib import Path

from alex_runtime.binocular_recursion import evaluate_binocular_recursion_case

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "tests" / "fixtures" / "binocular_recursion"


def load_case(name: str = "lawful-residual.json") -> dict:
    return json.loads((SPECIMENS / name).read_text(encoding="utf-8"))


class BinocularRecursionTests(unittest.TestCase):
    def test_lawful_dual_layer_residual_is_accepted(self):
        result = evaluate_binocular_recursion_case(load_case())
        self.assertEqual(result["schema"], "alex.binocular-recursion-result/v0")
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["terminal"], "RESIDUAL")
        self.assertEqual(result["validated_passes"], 2)
        self.assertIn("UNEXPLAINED_RESIDUAL", result["tension_types"])
        self.assertEqual(result["authority_digest"], "sha256:authority-0")

    def test_evaluator_does_not_mutate_source_case(self):
        case = load_case()
        before = copy.deepcopy(case)
        evaluate_binocular_recursion_case(case)
        self.assertEqual(case, before)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Run the focused test and verify it fails**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: import failure for `alex_runtime.binocular_recursion`.

- [ ] **Step 4: Implement the minimum evaluator**

Create `alex_runtime/binocular_recursion.py` with these constants and result shape:

```python
from __future__ import annotations

from typing import Any

_TERMINALS = {"FIXED", "CYCLE", "RESIDUAL", "DIVERGENT"}
_TENSION_TYPES = {
    "MISSING_CONSEQUENCE",
    "SURPLUS_GENERATOR",
    "UNEXPLAINED_RESIDUAL",
    "BRANCH_DEPENDENCE",
    "CONTRADICTION",
    "TRAJECTORY_DEPENDENCE",
    "STABLE_MATCH",
}
_BRANCH_STATUSES = {"ENTAILED", "INFERRED", "SPECULATIVE", "CONTRADICTED", "UNRESOLVED"}
_UPDATE_KINDS = {
    "NONE",
    "EVIDENCE_ADDED",
    "PREMISE_ADMITTED",
    "PREMISE_WITHDRAWN",
    "READING_CORRECTED",
    "RULE_PROFILE_CHANGED",
    "CONTRADICTION_RESOLVED",
    "OWNER_DECISION",
}


def _result(
    case_id: str,
    disposition: str,
    reason_code: str | None,
    authority_digest: str,
    terminal: str | None,
    validated_passes: int,
    tension_types: set[str] | None = None,
    receipt_survivors: set[str] | None = None,
) -> dict[str, object]:
    return {
        "schema": "alex.binocular-recursion-result/v0",
        "case_id": case_id,
        "disposition": disposition,
        "reason_code": reason_code,
        "terminal": terminal,
        "validated_passes": validated_passes,
        "tension_types": sorted(tension_types or set()),
        "receipt_survivors": sorted(receipt_survivors or set()),
        "authority_digest": authority_digest,
    }
```

Implement top-level checks for dictionary input, exact schema, non-empty case/authority digests, valid terminal, integer `pass_limit >= 1`, `1 <= len(passes) <= pass_limit`, contiguous pass indices, pass-zero ancestry, pass-to-pass ancestry, and both `compression` and `expansion` being dictionaries. Malformed/absent structural data returns `INSUFFICIENT_TO_TEST` with a stable reason code; it does not raise an ordinary validation exception.

For the lawful fixture, validate the declared tension vocabulary and return `ACCEPT` only after Task 2–3 validations are implemented; during this first task, implement enough structure for the two initial tests to pass without adding any truth or authority verdict.

- [ ] **Step 5: Run the focused test**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: 2 tests pass.

- [ ] **Step 6: Commit Task 1**

```bash
git add alex_runtime/binocular_recursion.py tests/test_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
git commit -m "feat: add binocular recursion evaluator nucleus"
```

---

### Task 2: Enforce constitutional refusals and update attribution

**Files:**
- Modify: `alex_runtime/binocular_recursion.py`
- Modify: `tests/test_binocular_recursion.py`

**Interfaces:**
- Consumes: Task 1 evaluator and lawful fixture.
- Produces stable reason codes for the approved refusal/insufficiency boundaries.

- [ ] **Step 1: Add explicit hostile tests**

Append these tests to `BinocularRecursionTests`:

```python
    def test_discovery_trigger_cannot_be_claim_support(self):
        case = load_case()
        case["passes"][0]["compression"]["claim_support_refs"].append("trigger:prompt-001")
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "DISCOVERY_TRIGGER_AS_SUPPORT"))

    def test_expansion_cannot_consume_undeclared_premise(self):
        case = load_case()
        case["passes"][0]["expansion"]["branches"][0]["used_premise_refs"] = ["p999"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "UNDECLARED_PREMISE_INJECTION"))

    def test_branch_local_introduced_premise_is_not_global_but_is_locally_legal(self):
        case = load_case()
        branch = case["passes"][0]["expansion"]["branches"][0]
        branch["used_premise_refs"] = ["local:p3"]
        branch["introduced_premise_refs"] = ["local:p3"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual(result["disposition"], "ACCEPT")

    def test_compression_cannot_erase_live_consequence(self):
        case = load_case()
        case["passes"][1]["compression"]["reexpanded_live_consequence_refs"] = ["c1"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "COMPRESSION_ERASED_LIVE_CONSEQUENCE"))

    def test_explicitly_withdrawn_consequence_may_leave_reexpansion_surface(self):
        case = load_case()
        case["passes"][1]["compression"]["reexpanded_live_consequence_refs"] = ["c1"]
        case["passes"][1]["update"] = {
            "kind": "EVIDENCE_ADDED",
            "receipt_refs": ["receipt:withdraw-c2"],
            "admit_premise_refs": [],
            "withdraw_premise_refs": [],
            "withdraw_consequence_refs": ["c2"],
            "authority_digest": "sha256:authority-0"
        }
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual(result["disposition"], "ACCEPT")

    def test_missing_compression_is_one_eye_collapse(self):
        case = load_case()
        del case["passes"][0]["compression"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "ONE_EYE_COLLAPSE"))

    def test_material_trajectory_must_preserve_ordered_path(self):
        case = load_case()
        case["passes"][0]["trajectory"] = []
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TRAJECTORY_NOT_PRESERVED"))

    def test_material_trajectory_repetitions_survive_validation(self):
        case = load_case()
        original = list(case["passes"][0]["trajectory"])
        evaluate_binocular_recursion_case(case)
        self.assertEqual(case["passes"][0]["trajectory"], original)
        self.assertEqual(original, ["A", "B", "A"])

    def test_broken_pass_ancestry_is_refused(self):
        case = load_case()
        case["passes"][1]["pre_field_digest"] = "sha256:unrelated-field"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "BROKEN_PASS_ANCESTRY"))

    def test_field_change_without_update_receipt_is_refused(self):
        case = load_case()
        case["passes"][0]["post_field_digest"] = "sha256:field-1"
        case["passes"][1]["pre_field_digest"] = "sha256:field-1"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "UNATTRIBUTED_UPDATE"))

    def test_authority_may_not_change_inside_update(self):
        case = load_case()
        case["passes"][0]["update"]["authority_digest"] = "sha256:authority-changed"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "AUTHORITY_CHANGED"))

    def test_pass_limit_must_be_positive_integer(self):
        case = load_case()
        case["pass_limit"] = 0
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "INVALID_PASS_LIMIT"))

    def test_unknown_tension_type_is_insufficient(self):
        case = load_case()
        case["passes"][0]["tensions"][0]["type"] = "MYSTERY"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "UNKNOWN_TENSION_TYPE"))
```

- [ ] **Step 2: Run the hostile tests and verify failures**

```bash
python -m unittest tests.test_binocular_recursion.BinocularRecursionTests -v
```

Expected: the new hostile tests fail until the contract checks are implemented.

- [ ] **Step 3: Implement support, premise, live-consequence, trajectory, ancestry, update, and authority validation**

Add these exact helpers:

```python
def _live_consequence_refs(expansion: dict[str, Any]) -> set[str]:
    live_statuses = {"ENTAILED", "INFERRED", "UNRESOLVED"}
    return {
        branch["consequence_ref"]
        for branch in expansion["branches"]
        if branch["status"] in live_statuses
    }


def _support_uses_discovery_trigger(compression: dict[str, Any], discovery_triggers: set[str]) -> bool:
    return bool(set(compression["claim_support_refs"]) & discovery_triggers)


def _branch_uses_only_declared_premises(branch: dict[str, Any], admitted: set[str]) -> bool:
    used = set(branch["used_premise_refs"])
    introduced = set(branch["introduced_premise_refs"])
    return used <= (admitted | introduced)
```

Validation order inside each pass:

```text
1. both eyes and required dictionaries/lists exist
2. trajectory validity
3. branch/tension/update vocabularies
4. discovery-trigger/support separation
5. branch premise declaration
6. live consequence preservation after explicit withdrawals
7. authority equality
8. field-change attribution
```

For compression loss use:

```python
required_live = _live_consequence_refs(expansion) - set(update["withdraw_consequence_refs"])
regenerated = set(compression["reexpanded_live_consequence_refs"])
if required_live - regenerated:
    return REFUSE / COMPRESSION_ERASED_LIVE_CONSEQUENCE
```

For field updates use:

```python
field_changed = pass_["pre_field_digest"] != pass_["post_field_digest"]
attributed = update["kind"] != "NONE" and bool(update["receipt_refs"])
```

Refuse only when `field_changed and not attributed`.

- [ ] **Step 4: Run the evaluator tests**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: all Task 1–2 tests pass.

- [ ] **Step 5: Commit Task 2**

```bash
git add alex_runtime/binocular_recursion.py tests/test_binocular_recursion.py
git commit -m "feat: enforce binocular recursion refusals"
```

---

### Task 3: Add deterministic terminal-state validation

**Files:**
- Modify: `alex_runtime/binocular_recursion.py`
- Create: `tests/fixtures/binocular_recursion/fixed.json`
- Create: `tests/fixtures/binocular_recursion/cycle.json`
- Create: `tests/fixtures/binocular_recursion/divergent.json`
- Modify: `tests/test_binocular_recursion.py`

**Interfaces:**
- Consumes: constitutionally valid pass envelopes.
- Produces: deterministic state digests and structural validation of `FIXED`, `CYCLE`, `RESIDUAL`, and `DIVERGENT`.

- [ ] **Step 1: Create terminal fixtures from the lawful fixture**

Create `fixed.json` by using two passes whose compression profile, proposal digest, expansion profile, live consequence set, and tension signature are identical, with terminal `FIXED`.

Create `cycle.json` with three passes whose canonical states are `A, B, A`, with terminal `CYCLE`.

Create `divergent.json` with `pass_limit: 3`, exactly three distinct canonical states, no repeated state digest, and a final transition whose material tension signature differs from pass 1, with terminal `DIVERGENT`.

Use only the same allowed branch/tension/update vocabularies as `lawful-residual.json`; keep authority unchanged and field ancestry contiguous.

- [ ] **Step 2: Add terminal tests**

Append:

```python
    def test_fixed_requires_last_two_equal_states_under_same_profiles(self):
        result = evaluate_binocular_recursion_case(load_case("fixed.json"))
        self.assertEqual((result["disposition"], result["terminal"]), ("ACCEPT", "FIXED"))

    def test_fixed_fails_when_compression_profile_changes(self):
        case = load_case("fixed.json")
        case["passes"][-1]["compression"]["profile_digest"] = "sha256:compress-v2"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_cycle_requires_repeated_state_with_distinct_intervening_state(self):
        result = evaluate_binocular_recursion_case(load_case("cycle.json"))
        self.assertEqual((result["disposition"], result["terminal"]), ("ACCEPT", "CYCLE"))

    def test_residual_requires_final_nonstable_tension(self):
        case = load_case()
        case["passes"][-1]["tensions"] = [
            {"type": "STABLE_MATCH", "left_refs": ["sha256:proposal-1"], "right_refs": ["c1", "c2"], "receipt_refs": ["receipt:stable"]}
        ]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_divergent_requires_reaching_declared_bound(self):
        case = load_case("divergent.json")
        case["pass_limit"] = 4
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_divergent_rejects_repeated_state(self):
        case = load_case("divergent.json")
        case["passes"][2]["compression"] = copy.deepcopy(case["passes"][0]["compression"])
        case["passes"][2]["expansion"] = copy.deepcopy(case["passes"][0]["expansion"])
        case["passes"][2]["tensions"] = copy.deepcopy(case["passes"][0]["tensions"])
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))
```

- [ ] **Step 3: Run terminal tests and verify failure**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: terminal-specific tests fail until canonical hashing and classifiers exist.

- [ ] **Step 4: Implement canonical binocular-state hashing**

Add:

```python
import hashlib
import json


def _sha256_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _tension_signature(tension: dict[str, Any]) -> dict[str, object]:
    return {
        "type": tension["type"],
        "left_refs": sorted(tension["left_refs"]),
        "right_refs": sorted(tension["right_refs"]),
    }


def _binocular_state_digest(pass_: dict[str, Any]) -> str:
    payload = {
        "compression_profile_digest": pass_["compression"]["profile_digest"],
        "compression_proposal_digest": pass_["compression"]["proposal_digest"],
        "expansion_profile_digest": pass_["expansion"]["profile_digest"],
        "live_consequence_refs": sorted(_live_consequence_refs(pass_["expansion"])),
        "tensions": [_tension_signature(t) for t in pass_["tensions"]],
    }
    return _sha256_json(payload)
```

The tension-list order is preserved. Only set-like refs within each tension are sorted.

Implement terminal rules exactly:

```text
FIXED
  len(passes) >= 2
  last two state digests equal
  last two compression.profile_digest equal
  last two expansion.profile_digest equal

CYCLE
  some state digest repeats
  at least one distinct state occurs between its two occurrences

RESIDUAL
  final pass has at least one tension type != STABLE_MATCH

DIVERGENT
  len(passes) == pass_limit
  len(passes) >= 2
  all state digests unique
  final transition changes the ordered material tension-signature list
```

Return `INSUFFICIENT_TO_TEST / TERMINAL_NOT_DEMONSTRATED` when the supplied terminal fails its structural rule.

- [ ] **Step 5: Run evaluator and full repository tests**

```bash
python -m unittest tests.test_binocular_recursion -v
python -m unittest discover -s tests -p "test_*.py" -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit Task 3**

```bash
git add alex_runtime/binocular_recursion.py tests/test_binocular_recursion.py tests/fixtures/binocular_recursion/fixed.json tests/fixtures/binocular_recursion/cycle.json tests/fixtures/binocular_recursion/divergent.json
git commit -m "feat: validate binocular terminal states"
```

---

### Task 4: Add the JSON runner and ALEX research-method reference

**Files:**
- Create: `tools/run_binocular_recursion.py`
- Create: `tests/test_run_binocular_recursion.py`
- Create: `skills/alex/references/binocular-recursion.md`
- Modify: `skills/alex/SKILL.md`
- Create: `tests/test_binocular_recursion_reference.py`

**Interfaces:**
- CLI consumes one JSON object from an optional file path or stdin.
- CLI writes one compact JSON result; exit `0` for `ACCEPT`, `1` for evaluator refusal/insufficiency, `2` for transport/JSON failures.
- Skill reference explains the human research protocol without claiming autonomous research generation.

- [ ] **Step 1: Write failing CLI tests**

Create `tests/test_run_binocular_recursion.py`:

```python
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools" / "run_binocular_recursion.py"
SPECIMENS = ROOT / "tests" / "fixtures" / "binocular_recursion"


class BinocularRunnerTests(unittest.TestCase):
    def test_file_input_accepts_lawful_case(self):
        completed = subprocess.run(
            [sys.executable, str(RUNNER), str(SPECIMENS / "lawful-residual.json")],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(json.loads(completed.stdout)["disposition"], "ACCEPT")

    def test_stdin_input_accepts_lawful_case(self):
        payload = (SPECIMENS / "lawful-residual.json").read_text(encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(RUNNER)],
            input=payload,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 0)
        self.assertEqual(json.loads(completed.stdout)["terminal"], "RESIDUAL")

    def test_evaluator_refusal_maps_to_exit_one(self):
        case = json.loads((SPECIMENS / "lawful-residual.json").read_text(encoding="utf-8"))
        case["passes"][0]["compression"]["claim_support_refs"].append("trigger:prompt-001")
        completed = subprocess.run(
            [sys.executable, str(RUNNER)],
            input=json.dumps(case),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 1)
        self.assertEqual(json.loads(completed.stdout)["reason_code"], "DISCOVERY_TRIGGER_AS_SUPPORT")

    def test_malformed_json_maps_to_exit_two(self):
        completed = subprocess.run(
            [sys.executable, str(RUNNER)],
            input="{not-json",
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertEqual(completed.stdout, "")
        self.assertIn("binocular recursion failed to execute:", completed.stderr)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run CLI tests and verify failure**

```bash
python -m unittest tests.test_run_binocular_recursion -v
```

Expected: runner-not-found failures.

- [ ] **Step 3: Implement the thin CLI**

Create `tools/run_binocular_recursion.py`:

```python
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.binocular_recursion import evaluate_binocular_recursion_case


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit an ALEX BINOCULAR-RECURSION-001 trace")
    parser.add_argument("path", nargs="?", help="JSON case path; omit to read stdin")
    args = parser.parse_args()

    try:
        raw = Path(args.path).read_text(encoding="utf-8") if args.path else sys.stdin.read()
        case = json.loads(raw)
        if not isinstance(case, dict):
            raise ValueError("case must decode to a JSON object")
        result = evaluate_binocular_recursion_case(case)
    except Exception as exc:
        print(f"binocular recursion failed to execute: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(result, sort_keys=True, separators=(",", ":")))
    return 0 if result["disposition"] == "ACCEPT" else 1


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run CLI tests**

```bash
python -m unittest tests.test_run_binocular_recursion -v
```

Expected: 4 tests pass.

- [ ] **Step 5: Write the documentation contract test**

Create `tests/test_binocular_recursion_reference.py`:

```python
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = ROOT / "skills" / "alex" / "references" / "binocular-recursion.md"
SKILL = ROOT / "skills" / "alex" / "SKILL.md"


class BinocularReferenceTests(unittest.TestCase):
    def test_reference_preserves_core_non_collapses(self):
        text = REFERENCE.read_text(encoding="utf-8")
        for phrase in (
            "FREEZE → COMPRESS || EXPAND → TENSION → UPDATE → REPEAT",
            "discovery trigger != support",
            "introduced premise != admitted premise",
            "ACCEPT != researched claim accepted as true",
        ):
            self.assertIn(phrase, text)

    def test_alex_skill_routes_binocular_recursion(self):
        text = SKILL.read_text(encoding="utf-8")
        self.assertIn("references/binocular-recursion.md", text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 6: Run the documentation test and verify failure**

```bash
python -m unittest tests.test_binocular_recursion_reference -v
```

Expected: missing-reference failure.

- [ ] **Step 7: Create the exact research-method reference**

Create `skills/alex/references/binocular-recursion.md` with this content:

```markdown
# BINOCULAR-RECURSION-001

Use this protocol when a bounded inquiry benefits from holding two pressures live at the same time:

- **COMPRESS:** what is the smallest generator or explanation that still preserves the live field?
- **EXPAND:** what follows from NOW under the currently admitted premises and declared relations?

The loop is:

```text
FREEZE → COMPRESS || EXPAND → TENSION → UPDATE → REPEAT
```

`||` means epistemically simultaneous, even if software computes the two traces sequentially. Neither eye may silently close the other.

## Laws

```text
discovery trigger != support
introduced premise != admitted premise
trajectory != focus membership
compression match != truth
terminal stability != truth
ACCEPT != researched claim accepted as true
```

Compression may propose a compact generator. It may not erase a live consequence merely because that consequence complicates the model.

Expansion may follow declared premises and relations to their consequence frontier. It may introduce a proposed premise only if that premise is visibly marked as branch-local; the proposal does not become globally admitted inside the same pass.

Tension is preserved formation data. It may identify missing consequences, surplus generator machinery, unexplained residuals, branch dependence, contradiction, trajectory dependence, or stable match. Tension does not by itself support an external claim.

A field changes only through an attributable update. The binocular operator does not mint authority.

## Executable auditor

The runtime audits an already supplied trace. It does not generate the compression or expansion content.

```bash
python tools/run_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
```

Exit `0` means the formation contract was accepted. Exit `1` means the supplied trace was refused or insufficient to test. Exit `2` means the JSON transport could not be executed.
```

- [ ] **Step 8: Add this routing paragraph to `skills/alex/SKILL.md`**

Insert near the other optional research protocols:

```markdown
`BINOCULAR-RECURSION-001` is an optional dual-pressure research protocol for cases where compression toward a minimum surviving generator and expansion through the lawful consequences of NOW should remain simultaneously live. Read [binocular-recursion.md](references/binocular-recursion.md) before using it. The executable auditor validates a supplied formation trace; it does not generate claims, admit premises, or promote tension into evidence.
```

- [ ] **Step 9: Run documentation, CLI, evaluator, and full-suite verification**

```bash
python -m unittest tests.test_binocular_recursion_reference -v
python -m unittest tests.test_run_binocular_recursion -v
python -m unittest tests.test_binocular_recursion -v
python -m unittest discover -s tests -p "test_*.py" -v
python tools/run_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
```

Expected: all unit tests pass; the smoke command exits `0` and prints a result whose `disposition` is `ACCEPT` and `terminal` is `RESIDUAL`.

- [ ] **Step 10: Commit Task 4**

```bash
git add tools/run_binocular_recursion.py tests/test_run_binocular_recursion.py skills/alex/references/binocular-recursion.md skills/alex/SKILL.md tests/test_binocular_recursion_reference.py
git commit -m "feat: expose binocular recursion research protocol"
```

---

## Final verification before PR

Run exactly:

```bash
python -m unittest tests.test_binocular_recursion -v
python -m unittest tests.test_run_binocular_recursion -v
python -m unittest tests.test_binocular_recursion_reference -v
python -m unittest discover -s tests -p "test_*.py" -v
python tools/run_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
```

Inspect `git diff main...HEAD` and confirm all seven boundaries:

```text
1. no Dogram runtime dependency
2. no network/model calls
3. no authority promotion beyond equality checking
4. no input-case mutation
5. no discovery-trigger/support union
6. no sorting/deduplication of material trajectory
7. no researched-claim truth verdict emitted by the evaluator
```

The implementation PR must state that Dogram remains a downstream deterministic disparity calculator rather than an ALEX runtime dependency, and that `ACCEPT` denotes formation-contract acceptance only.
