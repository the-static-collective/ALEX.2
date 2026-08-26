# ALEX Crucible v0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a language-neutral constitutional fixture contract plus a tiny reference harness that can prove an ALEX implementation refuses false inference without choosing ALEX's production runtime language.

**Architecture:** Canonical specimens and record contracts live as boring JSON / JSON Schema under `crucible/`. A Python 3.12 standard-library harness is only a reference validator and adapter runner: it sends one specimen JSON document to an external implementation on stdin and compares the returned result against required disposition, refusal code, required receipt survivors, and forbidden promotions. The harness is not the ALEX runtime and owns no research semantics beyond the Crucible contract.

**Tech Stack:** JSON; JSON Schema Draft 2020-12 documents; Python 3.12 standard library (`argparse`, `json`, `pathlib`, `subprocess`, `unittest`); GitHub Actions only after local contract tests pass.

**Spec:** `docs/superpowers/specs/2026-08-26-alex-constitutional-hardening-design.md`

## Global Constraints

- `SEARCH MISS != ABSENCE`.
- `ABSENCE CLAIM REQUIRES DECLARED COVERAGE`.
- `RECEIVED PREMISE != ADMITTED PREMISE`.
- `HISTORICAL INHERITANCE != EVIDENTIARY AUTHORITY`.
- `APPARENT MULTIPLICITY != INDEPENDENT ANCESTRY`.
- `AGREEMENT != INDEPENDENT CORROBORATION`.
- `REPLAY SUCCESS != DEPENDENCY ROBUSTNESS`.
- `SUPPORT COUNT != LOAD-BEARING DIVERSITY`.
- A Crucible refusal must preserve every item named in `required_receipt_survivors`.
- A Crucible result fails if it contains any item named in `forbidden_promotions`.
- The reference harness must not import OCR, database, web, model, GUI, or ALEX runtime libraries.
- The adapter protocol must be process-language-neutral: JSON document on stdin, JSON result on stdout, exit status `0` for a well-formed attempted result.
- The first implementation must not make Python the production ALEX runtime by implication.

---

## File structure

```text
crucible/
  README.md
  schema/
    specimen.schema.json
    result.schema.json
    search-observation.schema.json
    inherited-premise.schema.json
    dependency-family.schema.json
    counterfactual-replay.schema.json
  specimens/
    broken-ancestry.json
    coordinate-drift.json
    search-absence.json
    shared-lineage-corroboration.json
    favored-hypothesis.json
    serendipity-promotion.json
    replay-impersonation.json
    ghost-promotion.json
    yarn-promotion.json
    constitution-smuggling.json
    inherited-premise-smuggling.json
    remove-one-collapse.json

tools/
  crucible.py

tests/
  test_crucible_contract.py
  test_crucible_runner.py
  fixtures/
    adapter_accepts_everything.py
    adapter_refuses_correctly.py

.github/workflows/
  crucible.yml
```

`crucible/` is the portable contract. `tools/crucible.py` is replaceable reference machinery. `tests/fixtures/` contains intentionally fake adapters used only to prove the harness can detect constitutional cheating.

---

### Task 1: Define the Crucible specimen and result contracts

**Files:**
- Create: `crucible/schema/specimen.schema.json`
- Create: `crucible/schema/result.schema.json`
- Create: `crucible/README.md`
- Create: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: the fixture shape in the hardening spec.
- Produces: `specimen.schema.json`, `result.schema.json`, and the canonical result vocabulary consumed by every later task.

- [ ] **Step 1: Write the failing contract tests**

Create `tests/test_crucible_contract.py` with standard-library tests that load every schema as JSON and assert the contract's required names are present:

```python
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "crucible" / "schema"


class CrucibleSchemaTests(unittest.TestCase):
    def load(self, name: str) -> dict:
        return json.loads((SCHEMA / name).read_text(encoding="utf-8"))

    def test_specimen_schema_declares_required_contract(self):
        schema = self.load("specimen.schema.json")
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertEqual(schema["type"], "object")
        for key in ["id", "title", "constitutional_laws", "given", "attempt", "expected", "version"]:
            self.assertIn(key, schema["required"])
        expected = schema["properties"]["expected"]
        self.assertEqual(expected["type"], "object")
        for key in ["disposition", "required_receipt_survivors", "forbidden_promotions"]:
            self.assertIn(key, expected["required"])

    def test_result_schema_limits_disposition(self):
        schema = self.load("result.schema.json")
        values = schema["properties"]["disposition"]["enum"]
        self.assertEqual(values, ["ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"])
```

- [ ] **Step 2: Run the tests to verify they fail**

Run:

```bash
python -m unittest tests.test_crucible_contract -v
```

Expected: `ERROR` because the schema files do not yet exist.

- [ ] **Step 3: Create the minimal specimen schema**

`crucible/schema/specimen.schema.json` must use Draft 2020-12 and require exactly the constitutional comparison surface:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://the-static-collective.invalid/alex/crucible/specimen.schema.json",
  "title": "ALEX Crucible specimen",
  "type": "object",
  "additionalProperties": false,
  "required": ["id", "title", "constitutional_laws", "given", "attempt", "expected", "version"],
  "properties": {
    "id": {"type": "string", "minLength": 1},
    "title": {"type": "string", "minLength": 1},
    "constitutional_laws": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 1}},
    "given": {"type": "object"},
    "attempt": {"type": "object"},
    "expected": {
      "type": "object",
      "additionalProperties": false,
      "required": ["disposition", "required_receipt_survivors", "forbidden_promotions"],
      "properties": {
        "disposition": {"enum": ["ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"]},
        "refusal_code": {"type": "string", "minLength": 1},
        "required_receipt_survivors": {"type": "array", "items": {"type": "string", "minLength": 1}},
        "forbidden_promotions": {"type": "array", "items": {"type": "string", "minLength": 1}}
      }
    },
    "notes": {"type": "string"},
    "version": {"type": "integer", "minimum": 1}
  }
}
```

Create `result.schema.json` with required fields:

```text
specimen_id
disposition
refusal_code?
receipt_survivors[]
promotions[]
notes?
```

Require `specimen_id`, `disposition`, `receipt_survivors`, and `promotions`; use the same disposition enum.

- [ ] **Step 4: Document the adapter protocol**

`crucible/README.md` must state:

```text
stdin:  one complete Crucible specimen JSON object
stdout: one complete Crucible result JSON object
exit 0: adapter produced a well-formed attempted result
nonzero: adapter could not execute the specimen
```

Also state: an adapter is not conformant merely because it exits `0`; the reference harness compares its result with the specimen expectations.

- [ ] **Step 5: Run the contract tests**

Run:

```bash
python -m unittest tests.test_crucible_contract -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit**

```bash
git add crucible/schema/specimen.schema.json crucible/schema/result.schema.json crucible/README.md tests/test_crucible_contract.py
git commit -m "test: define ALEX Crucible contracts"
```

---

### Task 2: Build the reference harness and prove it catches a cheating adapter

**Files:**
- Create: `tools/crucible.py`
- Create: `tests/test_crucible_runner.py`
- Create: `tests/fixtures/adapter_accepts_everything.py`
- Create: `tests/fixtures/adapter_refuses_correctly.py`

**Interfaces:**
- Consumes: specimen JSON and adapter stdout result JSON.
- Produces: `compare_result(specimen: dict, actual: dict) -> list[str]` and CLI `python tools/crucible.py run --adapter ...`.

- [ ] **Step 1: Write failing comparison tests**

`tests/test_crucible_runner.py`:

```python
import unittest

from tools.crucible import compare_result


class CompareResultTests(unittest.TestCase):
    def specimen(self) -> dict:
        return {
            "id": "search-absence",
            "expected": {
                "disposition": "REFUSE",
                "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_receipt_survivors": ["search_observation:S1"],
                "forbidden_promotions": ["source_absence"]
            }
        }

    def test_accept_everything_adapter_fails(self):
        errors = compare_result(self.specimen(), {
            "specimen_id": "search-absence",
            "disposition": "ACCEPT",
            "receipt_survivors": [],
            "promotions": ["source_absence"]
        })
        self.assertIn("disposition", " ".join(errors))
        self.assertIn("search_observation:S1", " ".join(errors))
        self.assertIn("source_absence", " ".join(errors))

    def test_required_refusal_passes(self):
        errors = compare_result(self.specimen(), {
            "specimen_id": "search-absence",
            "disposition": "REFUSE",
            "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
            "receipt_survivors": ["search_observation:S1"],
            "promotions": []
        })
        self.assertEqual(errors, [])
```

- [ ] **Step 2: Run the tests to verify they fail**

```bash
python -m unittest tests.test_crucible_runner -v
```

Expected: import failure because `tools/crucible.py` does not exist.

- [ ] **Step 3: Implement `compare_result` minimally**

`tools/crucible.py` must compare:

```python
def compare_result(specimen: dict, actual: dict) -> list[str]:
    expected = specimen["expected"]
    errors: list[str] = []

    if actual.get("specimen_id") != specimen["id"]:
        errors.append("specimen_id mismatch")
    if actual.get("disposition") != expected["disposition"]:
        errors.append("disposition mismatch")
    if expected.get("refusal_code") != actual.get("refusal_code"):
        errors.append("refusal_code mismatch")

    survivors = set(actual.get("receipt_survivors", []))
    for required in expected["required_receipt_survivors"]:
        if required not in survivors:
            errors.append(f"missing required receipt survivor: {required}")

    promotions = set(actual.get("promotions", []))
    for forbidden in expected["forbidden_promotions"]:
        if forbidden in promotions:
            errors.append(f"forbidden promotion: {forbidden}")

    return errors
```

- [ ] **Step 4: Add the process adapter runner**

The CLI should:

1. load one fixture or all fixtures;
2. invoke adapter command with `subprocess.run(..., input=json.dumps(specimen), text=True, capture_output=True)`;
3. require exit `0`;
4. parse one stdout JSON object;
5. call `compare_result`;
6. print one stable PASS/FAIL line per specimen;
7. exit `1` if any specimen fails.

Do not shell-expand the adapter command. Accept adapter arguments as an `argparse.REMAINDER` list to avoid quoting differences.

- [ ] **Step 5: Create intentionally fake adapters**

`adapter_accepts_everything.py` must always emit:

```json
{"specimen_id":"<input id>","disposition":"ACCEPT","receipt_survivors":[],"promotions":["source_absence"]}
```

`adapter_refuses_correctly.py` should inspect only the test fixture's `expected` block and echo the expected disposition/refusal code/survivors with no promotions. Mark it clearly as a **harness test double that must never be used as evidence of ALEX conformance**.

- [ ] **Step 6: Run unit tests and CLI tests**

```bash
python -m unittest tests.test_crucible_runner -v
python tools/crucible.py run --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_accepts_everything.py
```

At this stage the CLI fixture command may fail because the fixture is introduced in Task 3. Unit tests must pass; do not claim full CLI proof yet.

- [ ] **Step 7: Commit**

```bash
git add tools/crucible.py tests/test_crucible_runner.py tests/fixtures
git commit -m "test: add ALEX Crucible reference harness"
```

---

### Task 3: Encode the first constitutional refusal fixtures

**Files:**
- Create all files under `crucible/specimens/`
- Modify: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: Task 1 specimen contract.
- Produces: a stable fixture corpus for existing ALEX refusal laws plus the new hardening laws.

- [ ] **Step 1: Add a failing test requiring the complete initial fixture set**

Add:

```python
EXPECTED = {
    "broken-ancestry.json",
    "coordinate-drift.json",
    "search-absence.json",
    "shared-lineage-corroboration.json",
    "favored-hypothesis.json",
    "serendipity-promotion.json",
    "replay-impersonation.json",
    "ghost-promotion.json",
    "yarn-promotion.json",
    "constitution-smuggling.json",
    "inherited-premise-smuggling.json",
    "remove-one-collapse.json",
}


def test_initial_fixture_names_exist(self):
    actual = {p.name for p in (ROOT / "crucible" / "specimens").glob("*.json")}
    self.assertEqual(actual, EXPECTED)
```

- [ ] **Step 2: Run to verify failure**

```bash
python -m unittest tests.test_crucible_contract -v
```

Expected: failure showing the missing fixture names.

- [ ] **Step 3: Create `search-absence.json` exactly around coverage**

Use a fixture whose `given` contains a partial `search_observation:S1`, whose attempt promotes `0 results` into `source_absence`, and whose expected result is:

```json
{
  "disposition": "REFUSE",
  "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
  "required_receipt_survivors": ["search_observation:S1", "coverage_status:PARTIAL"],
  "forbidden_promotions": ["source_absence"]
}
```

- [ ] **Step 4: Create `shared-lineage-corroboration.json`**

Given three apparent supports where two quote the same edition and the third inherits the same editorial reading, attempt to assert `three_independent_witnesses`.

Require:

```text
disposition: REFUSE
refusal_code: INDEPENDENCE_NOT_ESTABLISHED
survivors: dependency ancestry + all three witness identities
forbidden promotion: independent_corroboration
```

- [ ] **Step 5: Create `inherited-premise-smuggling.json`**

Given an `inherited_premise:P1` with `authority_claimed: true` and `authority_admitted: false`, attempt to use it as admitted evidence without examination.

Require:

```text
disposition: REFUSE
refusal_code: PREMISE_NOT_ADMITTED
survivors: inherited_premise:P1 + its arrival source
forbidden promotion: admitted_authority
```

- [ ] **Step 6: Create `remove-one-collapse.json`**

Given twelve visible support records that all descend from one translation `T1`, remove `T1` and require classification `COLLAPSES` rather than a claim that eleven independent supports remain.

The attempt should be refused if it promotes `support_count:11` to structural robustness.

- [ ] **Step 7: Encode the existing ALEX refusal fixtures without weakening them**

For each remaining file, preserve the relevant existing law:

```text
broken-ancestry              -> refuse exact claim when required ancestry is missing
coordinate-drift             -> refuse exact spatial citation in an unproved coordinate space
favored-hypothesis            -> refuse one-sided PRESSURE that cannot return disproved
serendipity-promotion         -> preserve search motive; refuse motive -> evidence
replay-impersonation          -> preserve replay; refuse replay -> historical identity
ghost-promotion               -> preserve residue; refuse ghost -> evidence/genealogy
yarn-promotion                -> preserve proposed relation; refuse visual yarn -> evidence
constitution-smuggling        -> preserve external constitution receipt if present; refuse desk/runtime inference -> constitutes
```

Every fixture must name at least one required survivor so refusal cannot be implemented by simply deleting the troublesome record.

- [ ] **Step 8: Run contract and harness tests**

```bash
python -m unittest tests.test_crucible_contract tests.test_crucible_runner -v
python tools/crucible.py run --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_accepts_everything.py
python tools/crucible.py run --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_refuses_correctly.py
```

Expected:
- unit tests pass;
- accept-everything adapter exits `1` with disposition/survivor/promotion failures;
- test-double correct adapter exits `0`.

- [ ] **Step 9: Commit**

```bash
git add crucible/specimens tests/test_crucible_contract.py
git commit -m "test: encode ALEX constitutional refusal specimens"
```

---

### Task 4: Publish the four new hardening record contracts

**Files:**
- Create: `crucible/schema/search-observation.schema.json`
- Create: `crucible/schema/inherited-premise.schema.json`
- Create: `crucible/schema/dependency-family.schema.json`
- Create: `crucible/schema/counterfactual-replay.schema.json`
- Modify: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: exact record fields from the hardening spec.
- Produces: portable data contracts that the one-book runtime may implement in its chosen language/storage model.

- [ ] **Step 1: Write failing schema presence tests**

Require all four schema files and assert their `required` arrays include these fields:

```text
search_observation:
  id corpus_id query index_id index_version fields_searched result_count observed_at producer coverage_status

inherited_premise:
  id formulation arrived_from entered_as examined authority_claimed authority_admitted consequences_if_false status created_at producer

dependency_family:
  id member_record_ids shared_ancestor_ids dependency_basis independence_status scope evidence_record_ids created_at producer

counterfactual_replay:
  base_replay_receipt_id removed_dependency_id removed_dependency_type base_result counterfactual_result consequence_class lost_outputs surviving_outputs changed_assertions residual_fog created_at producer
```

- [ ] **Step 2: Run to verify failure**

```bash
python -m unittest tests.test_crucible_contract -v
```

- [ ] **Step 3: Create `search-observation.schema.json`**

Use exact enums:

```json
["DECLARED_COMPLETE_FOR_SCOPE", "PARTIAL", "TRUNCATED", "UNKNOWN", "NOT_APPLICABLE"]
```

Do not create a value named `COMPLETE` without the `FOR_SCOPE` qualifier.

- [ ] **Step 4: Create `inherited-premise.schema.json`**

Use exact status enum:

```json
["UNEXAMINED", "EXAMINED_SUPPORTED", "EXAMINED_CONTRADICTED", "EXAMINED_UNRESOLVED", "REPLACED", "REFUSED"]
```

Keep `authority_claimed` and `authority_admitted` as separate booleans.

- [ ] **Step 5: Create `dependency-family.schema.json`**

Use exact independence enum:

```json
["DEPENDENT", "PARTIALLY_DEPENDENT", "INDEPENDENT_WITHIN_DECLARED_SCOPE", "UNKNOWN"]
```

Do not infer merged identity from family membership.

- [ ] **Step 6: Create `counterfactual-replay.schema.json`**

Use exact consequence enum:

```json
["SURVIVES_REMOVAL", "DEGRADES", "CHANGES_VERDICT", "COLLAPSES", "INSUFFICIENT_TO_TEST"]
```

Require the base receipt reference so the counterfactual remains a descendant test rather than a rewrite.

- [ ] **Step 7: Run tests and commit**

```bash
python -m unittest tests.test_crucible_contract tests.test_crucible_runner -v
git add crucible/schema tests/test_crucible_contract.py
git commit -m "docs: publish ALEX hardening record contracts"
```

---

### Task 5: Make the Crucible runnable in CI without promoting the test double

**Files:**
- Create: `.github/workflows/crucible.yml`
- Modify: `crucible/README.md`
- Modify: `tests/test_crucible_runner.py`

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: a repeatable contract/harness verification job; **not** a claim that ALEX runtime passes the Crucible.

- [ ] **Step 1: Write a failing test for all-fixture structural loading**

Add a test that iterates every `crucible/specimens/*.json`, loads it with `json.loads`, and asserts:

```text
id matches filename stem
constitutional_laws is non-empty
expected.disposition is in the canonical enum
required_receipt_survivors is non-empty
forbidden_promotions exists
```

- [ ] **Step 2: Run the full local suite**

```bash
python -m unittest discover -s tests -v
```

Fix only fixture/contract defects; do not add production research behavior.

- [ ] **Step 3: Create the CI workflow**

`.github/workflows/crucible.yml`:

```yaml
name: crucible-contract

on:
  pull_request:
  push:
    branches: [main]

jobs:
  contract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m unittest discover -s tests -v
```

Do **not** run `adapter_refuses_correctly.py` as a conformance check in CI. It is only a harness test double.

- [ ] **Step 4: Add the conformance boundary to README**

State explicitly:

> Passing `crucible-contract` proves the fixture corpus and reference harness are internally consistent. It does not prove an ALEX runtime conforms. Runtime conformance begins only when a real adapter executes the fixtures and the harness reports zero constitutional mismatches.

- [ ] **Step 5: Run final verification**

```bash
python -m unittest discover -s tests -v
python tools/crucible.py run --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_accepts_everything.py
```

Expected:
- unittest suite exits `0`;
- cheating adapter exits `1`.

Then run:

```bash
python tools/crucible.py run --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_refuses_correctly.py
```

Expected: exit `0`, with documentation making clear this proves the harness test double only.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/crucible.yml crucible/README.md tests
git commit -m "ci: verify ALEX Crucible contract"
```

---

### Task 6: Gate later ALEX implementation on the Crucible contract

**Files:**
- Modify: `README.md`
- Modify: `docs/superpowers/specs/2026-08-25-alexandria-floor-design.md`
- Modify: `docs/superpowers/specs/2026-08-26-alex-constitutional-hardening-design.md`

**Interfaces:**
- Consumes: verified Crucible contract and harness.
- Produces: an explicit architectural gate for the future one-book runtime.

- [ ] **Step 1: Add a failing documentation assertion test**

In `tests/test_crucible_contract.py`, load the three Markdown files as text and require the exact phrase:

```text
CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED
```

The test should fail before documentation is updated.

- [ ] **Step 2: Add the boundary phrase to all three documents**

Place it next to runtime status, not as a hidden footnote.

Then add this rule to the floor design:

> Before the one-book runtime claims constitutional conformance, a real runtime adapter must execute the applicable Crucible specimens. Contract self-tests and the fake adapter are insufficient.

- [ ] **Step 3: Run the full suite**

```bash
python -m unittest discover -s tests -v
```

Expected: pass.

- [ ] **Step 4: Review the diff for accidental runtime choice**

```bash
git diff --check
git grep -n "Python.*runtime\|production.*Python" README.md docs skills crucible tools || true
```

Expected: no text that promotes the Python reference harness into the production ALEX runtime.

- [ ] **Step 5: Commit**

```bash
git add README.md docs/superpowers/specs tests/test_crucible_contract.py
git commit -m "docs: gate ALEX runtime claims on Crucible"
```

---

## Self-review checklist

Before calling this plan complete during execution, verify:

- every hardening law in the spec is named in at least one fixture or record contract;
- every initial refusal specimen requires at least one receipt survivor;
- the cheating adapter demonstrably fails;
- the fake correct adapter is never represented as runtime conformance;
- `SEARCH_COVERAGE_INSUFFICIENT`, `INDEPENDENCE_NOT_ESTABLISHED`, and `PREMISE_NOT_ADMITTED` are stable refusal codes in fixtures;
- remove-one replay preserves its base receipt rather than rewriting it;
- dependency-family membership never merges witness identity;
- no UI, OCR, database, embedding, archive adapter, or production model dependency appears in Crucible v0;
- the plan contains no `TODO`, `TBD`, or unspecified implementation step.

## Later gates intentionally not implemented by this plan

This plan publishes the contracts for Search Coverage, Inherited Premises, Remove-One Replay, and Dependency Families, but does not implement their production behavior. Those behaviors belong to the one-book runtime after its language/storage choice is made against the specimen.

The required order after Crucible v0 is:

```text
Gate B — exact search emits real search_observation records
Gate C — inquiry can preserve inherited_premise records
Gate D — .LEEP can run one-dependency counterfactual replay
Gate E — ancestry analysis can emit dependency_family records
```

Each later gate should receive its own implementation plan once the corresponding runtime surface exists.
