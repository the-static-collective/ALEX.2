# BINOCULAR-RECURSION-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement a pure ALEX evaluator and JSON CLI that audit supplied binocular research traces for lawful compression/expansion tension without generating claims, adding premises, or minting authority.

**Architecture:** Add one pure `dict -> dict` evaluator in `alex_runtime/binocular_recursion.py`, following the existing `projection_break.py` style. The evaluator validates the machine contract, classifies refusals/insufficiency, computes canonical binocular-state digests for terminal checks, and returns only formation-contract results. A thin standard-library CLI reads one JSON case from stdin or a file and writes one JSON result. Fixtures and `unittest` cover lawful and hostile cases. The ALEX skill receives a reference page explaining when to use the protocol and its non-collapse laws.

**Tech Stack:** Python standard library only; `json`, `hashlib`, `argparse`, `sys`, `pathlib`, `copy`; `unittest` for tests.

**Spec:** `docs/superpowers/specs/2026-08-28-binocular-recursion-design.md`, `docs/superpowers/specs/2026-08-28-binocular-recursion-machine-contract.md`, and `docs/superpowers/specs/2026-08-28-binocular-recursion-machine-contract-amendment.md`

## Global Constraints

- Public evaluator signature is exactly `evaluate_binocular_recursion_case(case: dict) -> dict[str, object]`.
- The evaluator audits a supplied trace; it does not generate compression proposals, perform open-ended consequence search, interpret prose, or decide whether a researched claim is true.
- `discovery_trigger_refs`, `support_refs`, `admitted_premise_refs`, and `unresolved_premise_refs` remain distinct sets and are never unioned for convenience.
- `claim_support_refs ∩ discovery_trigger_refs` must be empty or return `REFUSE / DISCOVERY_TRIGGER_AS_SUPPORT`.
- Expansion may use only admitted premises plus branch-local explicitly introduced premises; otherwise return `REFUSE / UNDECLARED_PREMISE_INJECTION`.
- Live consequences with status `ENTAILED`, `INFERRED`, or `UNRESOLVED` may not be erased by compression unless explicitly withdrawn by the update; otherwise return `REFUSE / COMPRESSION_ERASED_LIVE_CONSEQUENCE`.
- When trajectory order is material, the evaluator preserves order and repetitions exactly and never sorts or deduplicates the trajectory.
- Field changes require an attributable update receipt; authority must remain equal to the case-level authority digest.
- Successful terminal labels are only `FIXED`, `CYCLE`, `RESIDUAL`, and `DIVERGENT`; stability is a formation result, not a truth claim.
- `pass_limit` is required, integer, at least 1, and must bound `len(passes)`.
- No new external dependency, network call, filesystem mutation inside evaluator logic, model call, hidden time dependence, or random behavior.
- The evaluator must not mutate the input case.
- `ACCEPT` means only that the formation contract is satisfied; it does not accept the researched claim as true.

---

### Task 1: Establish the lawful residual nucleus

**Files:**
- Create: `alex_runtime/binocular_recursion.py`
- Create: `tests/fixtures/binocular_recursion/lawful-residual.json`
- Create: `tests/test_binocular_recursion.py`

**Interfaces:**
- Consumes: a decoded case matching `alex.binocular-recursion-case/v0`.
- Produces: `evaluate_binocular_recursion_case(case: dict) -> dict[str, object]` with result keys `schema`, `case_id`, `disposition`, `reason_code`, `terminal`, `validated_passes`, `tension_types`, `receipt_survivors`, and `authority_digest`.

- [ ] **Step 1: Add a complete lawful residual fixture**

Create `tests/fixtures/binocular_recursion/lawful-residual.json` with two contiguous passes, a stable authority digest, distinct discovery/support refs, explicit compression and expansion profiles, one `UNEXPLAINED_RESIDUAL` tension in the final pass, and attributable `NONE` updates whose pre/post field digests are equal. Use this exact structural nucleus:

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
      "tensions": [{"type": "STABLE_MATCH", "left_refs": ["sha256:proposal-0"], "right_refs": ["c1"], "receipt_refs": ["receipt:t0"]}],
      "update": {"kind": "NONE", "receipt_refs": [], "admit_premise_refs": [], "withdraw_premise_refs": [], "withdraw_consequence_refs": [], "authority_digest": "sha256:authority-0"},
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
          {"branch_id": "b1", "parent_refs": ["p1"], "rule_ref": "rule:r1", "condition_refs": [], "consequence_ref": "c1", "status": "INFERRED", "used_premise_refs": ["p1"], "introduced_premise_refs": []},
          {"branch_id": "b2", "parent_refs": ["p2"], "rule_ref": "rule:r2", "condition_refs": [], "consequence_ref": "c2", "status": "UNRESOLVED", "used_premise_refs": ["p2"], "introduced_premise_refs": []}
        ]
      },
      "tensions": [{"type": "UNEXPLAINED_RESIDUAL", "left_refs": ["sha256:proposal-1"], "right_refs": ["c2"], "receipt_refs": ["receipt:t1"]}],
      "update": {"kind": "NONE", "receipt_refs": [], "admit_premise_refs": [], "withdraw_premise_refs": [], "withdraw_consequence_refs": [], "authority_digest": "sha256:authority-0"},
      "post_field_digest": "sha256:field-0"
    }
  ]
}
```

- [ ] **Step 2: Write the first failing unit tests**

In `tests/test_binocular_recursion.py`, add:

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
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["terminal"], "RESIDUAL")
        self.assertEqual(result["validated_passes"], 2)
        self.assertIn("UNEXPLAINED_RESIDUAL", result["tension_types"])

    def test_evaluator_does_not_mutate_source_case(self):
        case = load_case()
        before = copy.deepcopy(case)
        evaluate_binocular_recursion_case(case)
        self.assertEqual(case, before)
```

- [ ] **Step 3: Run the test and verify import failure**

Run:

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: failure because `alex_runtime.binocular_recursion` does not yet exist.

- [ ] **Step 4: Implement the minimum envelope validator and residual success path**

Create `alex_runtime/binocular_recursion.py` with constants and helpers for non-empty strings/lists, pass ancestry, tension vocabulary, and result construction. The public function must begin by validating the top-level schema, `case_id`, authority, `pass_limit`, terminal vocabulary, and non-empty `passes`; then validate contiguous `pass_index` and pre/post ancestry; then validate both eyes exist. For the lawful fixture, collect unique tension types and receipt refs without mutating input and return:

```python
{
    "schema": "alex.binocular-recursion-result/v0",
    "case_id": case_id,
    "disposition": "ACCEPT",
    "reason_code": None,
    "terminal": terminal,
    "validated_passes": len(passes),
    "tension_types": sorted(tension_types),
    "receipt_survivors": sorted(receipt_survivors),
    "authority_digest": authority_digest,
}
```

Keep ordinary malformed data as `INSUFFICIENT_TO_TEST`, not uncaught exceptions.

- [ ] **Step 5: Run the focused tests**

Run:

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: both tests pass.

- [ ] **Step 6: Commit the nucleus**

```bash
git add alex_runtime/binocular_recursion.py tests/test_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
git commit -m "feat: add binocular recursion evaluator nucleus"
```

---

### Task 2: Enforce constitutional refusals and trajectory preservation

**Files:**
- Modify: `alex_runtime/binocular_recursion.py`
- Modify: `tests/test_binocular_recursion.py`

**Interfaces:**
- Consumes: Task 1 evaluator and lawful fixture.
- Produces: deterministic reason codes `DISCOVERY_TRIGGER_AS_SUPPORT`, `UNDECLARED_PREMISE_INJECTION`, `COMPRESSION_ERASED_LIVE_CONSEQUENCE`, `ONE_EYE_COLLAPSE`, `TRAJECTORY_NOT_PRESERVED`, `BROKEN_PASS_ANCESTRY`, `UNATTRIBUTED_UPDATE`, `AUTHORITY_CHANGED`, `INVALID_PASS_LIMIT`, and `UNKNOWN_TENSION_TYPE`.

- [ ] **Step 1: Add failing hostile tests using copies of the lawful fixture**

Add tests that mutate one contract boundary at a time:

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


def test_compression_cannot_erase_live_consequence(self):
    case = load_case()
    case["passes"][1]["compression"]["reexpanded_live_consequence_refs"] = ["c1"]
    result = evaluate_binocular_recursion_case(case)
    self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "COMPRESSION_ERASED_LIVE_CONSEQUENCE"))


def test_material_trajectory_must_preserve_ordered_path(self):
    case = load_case()
    case["passes"][0]["trajectory"] = []
    result = evaluate_binocular_recursion_case(case)
    self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TRAJECTORY_NOT_PRESERVED"))


def test_authority_may_not_change_inside_update(self):
    case = load_case()
    case["passes"][0]["update"]["authority_digest"] = "sha256:authority-changed"
    result = evaluate_binocular_recursion_case(case)
    self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "AUTHORITY_CHANGED"))
```

Also add tests for missing compression, broken ancestry, field change with `kind == "NONE"`, invalid `pass_limit`, unknown tension type, and an explicitly withdrawn consequence that is allowed to disappear from `reexpanded_live_consequence_refs` when its withdrawal receipt is present.

- [ ] **Step 2: Run the hostile tests and verify failures**

Run:

```bash
python -m unittest tests.test_binocular_recursion.BinocularRecursionTests -v
```

Expected: the new constitutional tests fail until validation is implemented.

- [ ] **Step 3: Implement validation in contract order**

Add focused helpers with these exact responsibilities:

```python
def _live_consequence_refs(expansion: dict) -> set[str]:
    live_statuses = {"ENTAILED", "INFERRED", "UNRESOLVED"}
    return {
        branch["consequence_ref"]
        for branch in expansion["branches"]
        if branch["status"] in live_statuses
    }


def _validate_support_boundary(compression: dict, discovery_triggers: set[str]) -> str | None:
    support = set(compression["claim_support_refs"])
    return "DISCOVERY_TRIGGER_AS_SUPPORT" if support & discovery_triggers else None


def _validate_branch_premises(branch: dict, admitted: set[str]) -> bool:
    used = set(branch["used_premise_refs"])
    introduced = set(branch["introduced_premise_refs"])
    return used <= (admitted | introduced)
```

Validate every branch status against the approved vocabulary. Treat branch-local introduced premises as local only; do not add them to the case-level admitted set.

For compression loss, calculate:

```python
required_live = _live_consequence_refs(expansion) - set(update["withdraw_consequence_refs"])
regenerated = set(compression["reexpanded_live_consequence_refs"])
```

and refuse when `required_live - regenerated` is non-empty.

For trajectory, require at least two non-empty string refs only when `trajectory_order_material is True`; inspect without sorting or deduplicating.

For updates, if `pre_field_digest != post_field_digest`, require `kind != "NONE"` and at least one non-empty update `receipt_ref`.

- [ ] **Step 4: Run all binocular tests**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: all constitutional and lawful tests pass.

- [ ] **Step 5: Commit the constitutional evaluator**

```bash
git add alex_runtime/binocular_recursion.py tests/test_binocular_recursion.py
git commit -m "feat: enforce binocular recursion refusals"
```

---

### Task 3: Implement canonical terminal classification

**Files:**
- Modify: `alex_runtime/binocular_recursion.py`
- Create: `tests/fixtures/binocular_recursion/fixed.json`
- Create: `tests/fixtures/binocular_recursion/cycle.json`
- Create: `tests/fixtures/binocular_recursion/divergent.json`
- Modify: `tests/test_binocular_recursion.py`

**Interfaces:**
- Consumes: validated pass envelopes from Tasks 1–2.
- Produces: canonical binocular-state digests and structural terminal validation for all four admitted terminal labels.

- [ ] **Step 1: Define the canonical binocular-state payload in tests**

The digest must represent formation state without smuggling evidence authority into it. Pin the payload to these fields:

```python
{
    "compression_profile_digest": pass_["compression"]["profile_digest"],
    "compression_proposal_digest": pass_["compression"]["proposal_digest"],
    "expansion_profile_digest": pass_["expansion"]["profile_digest"],
    "live_consequence_refs": sorted(_live_consequence_refs(pass_["expansion"])),
    "tensions": [
        {
            "type": tension["type"],
            "left_refs": sorted(tension["left_refs"]),
            "right_refs": sorted(tension["right_refs"]),
        }
        for tension in pass_["tensions"]
    ],
}
```

Preserve the order of the tension list itself because the trace may claim ordered formation; only sort set-like refs inside each tension.

- [ ] **Step 2: Write failing terminal tests**

Add fixtures/tests proving:

```python
def test_fixed_requires_last_two_equal_states_under_same_profiles(self):
    result = evaluate_binocular_recursion_case(load_case("fixed.json"))
    self.assertEqual((result["disposition"], result["terminal"]), ("ACCEPT", "FIXED"))


def test_cycle_requires_repeated_state_with_distinct_intervening_state(self):
    result = evaluate_binocular_recursion_case(load_case("cycle.json"))
    self.assertEqual((result["disposition"], result["terminal"]), ("ACCEPT", "CYCLE"))


def test_divergent_requires_reaching_declared_bound(self):
    case = load_case("divergent.json")
    case["pass_limit"] += 1
    result = evaluate_binocular_recursion_case(case)
    self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))
```

Also test that a `FIXED` label with changed compression profile is not demonstrated, and that `RESIDUAL` requires at least one final tension other than `STABLE_MATCH`.

- [ ] **Step 3: Run terminal tests and verify failure**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: terminal-specific cases fail until digest/classification helpers exist.

- [ ] **Step 4: Implement deterministic canonical hashing**

Use only stdlib:

```python
import hashlib
import json


def _sha256_json(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()
```

Add `_binocular_state_digest(pass_: dict) -> str` using the pinned payload from Step 1.

Terminal rules:

- `FIXED`: at least two passes; last two state digests equal; their compression and expansion profile digests equal.
- `CYCLE`: some state digest repeats with at least one different digest between the two occurrences.
- `RESIDUAL`: final pass contains at least one tension whose type is not `STABLE_MATCH`.
- `DIVERGENT`: `len(passes) == pass_limit`; no state digest repeats; final transition changes the multiset/list of material tension signatures; at least two passes.

If the supplied terminal label fails its rule, return `INSUFFICIENT_TO_TEST / TERMINAL_NOT_DEMONSTRATED`.

- [ ] **Step 5: Run all binocular tests**

```bash
python -m unittest tests.test_binocular_recursion -v
```

Expected: lawful residual, fixed, cycle, divergent, and hostile cases all pass.

- [ ] **Step 6: Run the full repository unit suite**

```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

Expected: existing ALEX tests and new binocular tests pass.

- [ ] **Step 7: Commit terminal semantics**

```bash
git add alex_runtime/binocular_recursion.py tests/test_binocular_recursion.py tests/fixtures/binocular_recursion/fixed.json tests/fixtures/binocular_recursion/cycle.json tests/fixtures/binocular_recursion/divergent.json
git commit -m "feat: validate binocular terminal states"
```

---

### Task 4: Add the JSON command-line runner

**Files:**
- Create: `tools/run_binocular_recursion.py`
- Create: `tests/test_run_binocular_recursion.py`

**Interfaces:**
- Consumes: one JSON case from `stdin` or one optional positional file path.
- Produces: one compact JSON result on stdout; exit code `0` for `ACCEPT`, `1` for `REFUSE` or `INSUFFICIENT_TO_TEST`, and `2` for unreadable/invalid JSON transport failures.

- [ ] **Step 1: Write failing CLI tests**

Use `subprocess.run` with the repository Python executable and the lawful fixture. Pin these behaviors:

```python
completed = subprocess.run(
    [sys.executable, str(ROOT / "tools" / "run_binocular_recursion.py"), str(SPECIMENS / "lawful-residual.json")],
    capture_output=True,
    text=True,
    check=False,
)
self.assertEqual(completed.returncode, 0)
result = json.loads(completed.stdout)
self.assertEqual(result["disposition"], "ACCEPT")
```

Add a stdin case, a constitutional refusal case returning exit `1`, and malformed JSON returning exit `2` with the error on stderr and no fabricated result.

- [ ] **Step 2: Run the CLI tests and verify failure**

```bash
python -m unittest tests.test_run_binocular_recursion -v
```

Expected: failure because the runner does not exist.

- [ ] **Step 3: Implement the thin runner**

Create `tools/run_binocular_recursion.py` following existing tool path bootstrapping:

```python
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from alex_runtime.binocular_recursion import evaluate_binocular_recursion_case
```

Parse an optional `path`; read UTF-8 file content when supplied, otherwise read `sys.stdin`; decode JSON; require a JSON object; call the evaluator; print `json.dumps(result, sort_keys=True, separators=(",", ":"))`.

Exit mapping:

```python
if result["disposition"] == "ACCEPT":
    return 0
return 1
```

Transport/decode exceptions print `binocular recursion failed to execute: <message>` to stderr and return `2`.

- [ ] **Step 4: Run CLI and evaluator tests**

```bash
python -m unittest tests.test_run_binocular_recursion tests.test_binocular_recursion -v
```

Expected: all pass.

- [ ] **Step 5: Commit the CLI**

```bash
git add tools/run_binocular_recursion.py tests/test_run_binocular_recursion.py
git commit -m "feat: add binocular recursion json runner"
```

---

### Task 5: Expose the research protocol through the ALEX skill and verify the whole slice

**Files:**
- Create: `skills/alex/references/binocular-recursion.md`
- Modify: `skills/alex/SKILL.md`
- Create: `tests/test_binocular_recursion_reference.py`

**Interfaces:**
- Consumes: the executable contract from Tasks 1–4.
- Produces: human-facing routing instructions that point users to the executable protocol without claiming it performs research autonomously.

- [ ] **Step 1: Write a failing documentation contract test**

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
        self.assertIn("binocular-recursion.md", text)
```

- [ ] **Step 2: Run the documentation contract test and verify failure**

```bash
python -m unittest tests.test_binocular_recursion_reference -v
```

Expected: failure because the reference file and skill routing line are absent.

- [ ] **Step 3: Write the reference**

`skills/alex/references/binocular-recursion.md` must include:

```text
BINOCULAR-RECURSION-001
FREEZE → COMPRESS || EXPAND → TENSION → UPDATE → REPEAT
```

Explain:

- use it when a bounded inquiry benefits from simultaneously asking “what is the smallest generator that survives?” and “what follows from NOW under the admitted rules?”;
- compression is proposal pressure, not truth;
- expansion is consequence tracing, not premise invention;
- tension is preserved data, not automatic contradiction resolution;
- discovery trigger != support;
- introduced premise != admitted premise;
- trajectory != focus membership;
- terminal stability != truth;
- `ACCEPT != researched claim accepted as true`;
- the executable runner audits supplied traces and does not generate the compression/expansion content itself.

Include one minimal JSON invocation example and one shell example:

```bash
python tools/run_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
```

- [ ] **Step 4: Add one routing paragraph to `skills/alex/SKILL.md`**

Place it beside the existing optional formation protocols. The paragraph must say that `BINOCULAR-RECURSION-001` is appropriate when compression and lawful implication should remain simultaneously live, and direct the reader to `references/binocular-recursion.md`. Do not replace PRESSURE, PEEL/SLEEP/LEEP, UNGATE, or ordinary TRACE/DOSSIER flows.

- [ ] **Step 5: Run the reference test and complete suite**

```bash
python -m unittest tests.test_binocular_recursion_reference -v
python -m unittest discover -s tests -p "test_*.py" -v
```

Expected: all tests pass.

- [ ] **Step 6: Smoke-test the script on the lawful fixture**

```bash
python tools/run_binocular_recursion.py tests/fixtures/binocular_recursion/lawful-residual.json
```

Expected stdout contains compact JSON with:

```json
{"disposition":"ACCEPT","terminal":"RESIDUAL"}
```

along with the remaining required result fields.

- [ ] **Step 7: Commit the skill exposure**

```bash
git add skills/alex/references/binocular-recursion.md skills/alex/SKILL.md tests/test_binocular_recursion_reference.py
git commit -m "docs: expose binocular recursion research protocol"
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

Then inspect `git diff main...HEAD` and confirm:

```text
no Dogram runtime dependency
no network/model calls
no new authority field beyond authority_digest preservation
no mutation of input case
no support/discovery-trigger union
no sorting/deduplication of material trajectory
no claim-truth verdict emitted by evaluator
```

The implementation PR should describe `ACCEPT` as formation-contract acceptance only and explicitly note that Dogram remains a downstream deterministic disparity calculator rather than an ALEX runtime dependency.
