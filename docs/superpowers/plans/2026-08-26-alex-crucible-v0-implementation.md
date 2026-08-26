# ALEX Crucible v0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a language-neutral constitutional fixture contract plus a tiny reference harness that can prove an ALEX implementation refuses false inference without choosing ALEX's production runtime language.

**Architecture:** Canonical specimens and record contracts live as JSON / JSON Schema under `crucible/`. A Python 3.12 standard-library harness is only reference machinery: it sends one specimen JSON document to an external adapter on stdin, receives one result JSON document on stdout, and checks disposition, refusal code, required receipt survivors, and forbidden promotions. The harness is not the ALEX runtime.

**Tech Stack:** JSON; JSON Schema Draft 2020-12 documents; Python 3.12 standard library (`argparse`, `json`, `pathlib`, `subprocess`, `tempfile`, `unittest`); GitHub Actions after local tests pass.

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
- A refusal is incomplete if it drops anything named in `required_receipt_survivors`.
- A result fails if it contains anything named in `forbidden_promotions`.
- The reference harness must not import OCR, database, web, model, GUI, or ALEX runtime libraries.
- Adapter protocol is process-language-neutral: one JSON specimen on stdin, one JSON result on stdout.
- Python is a reference harness choice only, not a production ALEX runtime decision.

---

## File Structure

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

---

### Task 1: Define the Crucible specimen/result contracts

**Files:**
- Create: `crucible/schema/specimen.schema.json`
- Create: `crucible/schema/result.schema.json`
- Create: `crucible/README.md`
- Create: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: hardening spec fixture shape.
- Produces: canonical specimen/result vocabulary used by every later task.

- [ ] **Step 1: Write failing schema contract tests**

Create `tests/test_crucible_contract.py`:

```python
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "crucible" / "schema"


class CrucibleContractTests(unittest.TestCase):
    def load(self, name: str) -> dict:
        return json.loads((SCHEMA / name).read_text(encoding="utf-8"))

    def test_specimen_contract(self):
        schema = self.load("specimen.schema.json")
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        for key in ["id", "title", "constitutional_laws", "given", "attempt", "expected", "version"]:
            self.assertIn(key, schema["required"])
        expected = schema["properties"]["expected"]
        for key in ["disposition", "required_receipt_survivors", "forbidden_promotions"]:
            self.assertIn(key, expected["required"])

    def test_result_dispositions(self):
        schema = self.load("result.schema.json")
        self.assertEqual(
            schema["properties"]["disposition"]["enum"],
            ["ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"],
        )
```

- [ ] **Step 2: Run and verify RED**

```bash
python -m unittest tests.test_crucible_contract -v
```

Expected: errors because the schemas do not exist.

- [ ] **Step 3: Create `specimen.schema.json`**

Use Draft 2020-12. Require:

```text
id
title
constitutional_laws[]
given
attempt
expected
  disposition
  refusal_code?
  required_receipt_survivors[]
  forbidden_promotions[]
version
```

Disposition enum must be exactly:

```json
["ACCEPT", "REFUSE", "UNRESOLVED", "INSUFFICIENT_TO_TEST"]
```

- [ ] **Step 4: Create `result.schema.json`**

Require:

```text
specimen_id
disposition
receipt_survivors[]
promotions[]
```

Allow optional `refusal_code` and `notes`. Use the same disposition enum.

- [ ] **Step 5: Document the adapter protocol**

`crucible/README.md` must state:

```text
stdin  -> one complete specimen JSON object
stdout -> one complete result JSON object
exit 0 -> adapter produced a parseable attempted result
nonzero -> adapter could not execute the specimen
```

Also state that exit `0` is not conformance; the harness still compares constitutional expectations.

- [ ] **Step 6: Run and verify GREEN**

```bash
python -m unittest tests.test_crucible_contract -v
```

Expected: pass.

- [ ] **Step 7: Commit**

```bash
git add crucible/schema/specimen.schema.json crucible/schema/result.schema.json crucible/README.md tests/test_crucible_contract.py
git commit -m "test: define ALEX Crucible contracts"
```

---

### Task 2: Build the reference harness and prove it detects cheating

**Files:**
- Create: `tools/crucible.py`
- Create: `tests/test_crucible_runner.py`
- Create: `tests/fixtures/adapter_accepts_everything.py`
- Create: `tests/fixtures/adapter_refuses_correctly.py`

**Interfaces:**
- Consumes: specimen dict + adapter result dict.
- Produces: `compare_result(specimen: dict, actual: dict) -> list[str]` and CLI process runner.

- [ ] **Step 1: Write failing result-comparison tests**

```python
import unittest
from tools.crucible import compare_result


class CompareResultTests(unittest.TestCase):
    def specimen(self):
        return {
            "id": "search-absence",
            "expected": {
                "disposition": "REFUSE",
                "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_receipt_survivors": ["search_observation:S1"],
                "forbidden_promotions": ["source_absence"],
            },
        }

    def test_cheating_result_fails(self):
        errors = compare_result(self.specimen(), {
            "specimen_id": "search-absence",
            "disposition": "ACCEPT",
            "receipt_survivors": [],
            "promotions": ["source_absence"],
        })
        joined = " ".join(errors)
        self.assertIn("disposition", joined)
        self.assertIn("search_observation:S1", joined)
        self.assertIn("source_absence", joined)

    def test_required_refusal_passes(self):
        errors = compare_result(self.specimen(), {
            "specimen_id": "search-absence",
            "disposition": "REFUSE",
            "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
            "receipt_survivors": ["search_observation:S1"],
            "promotions": [],
        })
        self.assertEqual(errors, [])
```

- [ ] **Step 2: Run and verify RED**

```bash
python -m unittest tests.test_crucible_runner -v
```

Expected: import failure because `tools/crucible.py` does not exist.

- [ ] **Step 3: Implement `compare_result` minimally**

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

- [ ] **Step 4: Add process-runner tests using temporary specimens**

In `tests/test_crucible_runner.py`, use `tempfile.TemporaryDirectory()` to write a complete temporary specimen. Invoke the CLI with `subprocess.run` against each fake adapter. Assert:

```text
adapter_accepts_everything.py -> exit 1
adapter_refuses_correctly.py  -> exit 0
```

This keeps Task 2 independently testable before canonical fixtures exist.

- [ ] **Step 5: Implement CLI runner**

`tools/crucible.py` must:

1. load `--fixture PATH`;
2. accept adapter argv after `--adapter` using `argparse.REMAINDER`;
3. run adapter with `shell=False`;
4. send fixture JSON through stdin;
5. parse exactly one stdout JSON object;
6. compare via `compare_result`;
7. print stable `PASS <id>` or `FAIL <id>: ...`;
8. exit `1` on mismatch or adapter execution failure.

- [ ] **Step 6: Create fake adapters**

`adapter_accepts_everything.py` always returns `ACCEPT`, no survivors, and promotion `source_absence`.

`adapter_refuses_correctly.py` echoes the fixture's expected disposition/refusal code/survivors with no promotions. Add a top comment:

```python
# HARNESS TEST DOUBLE ONLY. NEVER EVIDENCE OF ALEX RUNTIME CONFORMANCE.
```

- [ ] **Step 7: Run and verify GREEN**

```bash
python -m unittest tests.test_crucible_runner -v
```

Expected: pass, including process tests that prove the cheating adapter fails.

- [ ] **Step 8: Commit**

```bash
git add tools/crucible.py tests/test_crucible_runner.py tests/fixtures
git commit -m "test: add ALEX Crucible reference harness"
```

---

### Task 3: Encode the initial constitutional fixture corpus

**Files:**
- Create: all `crucible/specimens/*.json` listed in File Structure
- Modify: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: specimen contract.
- Produces: stable refusal specimens for old and new ALEX laws.

- [ ] **Step 1: Add a failing fixture-set test**

Require the exact 12 filenames from File Structure and require every fixture to have:

```text
id == filename stem
constitutional_laws non-empty
expected.required_receipt_survivors non-empty
expected.forbidden_promotions present
```

- [ ] **Step 2: Run and verify RED**

```bash
python -m unittest tests.test_crucible_contract -v
```

Expected: missing fixture failures.

- [ ] **Step 3: Encode the four new hardening fixtures**

Use these stable refusal expectations:

```text
search-absence:
  REFUSE / SEARCH_COVERAGE_INSUFFICIENT
  preserve search_observation:S1 + coverage_status:PARTIAL
  forbid source_absence

shared-lineage-corroboration:
  REFUSE / INDEPENDENCE_NOT_ESTABLISHED
  preserve all witness IDs + shared ancestry
  forbid independent_corroboration

inherited-premise-smuggling:
  REFUSE / PREMISE_NOT_ADMITTED
  preserve inherited_premise:P1 + arrival source
  forbid admitted_authority

remove-one-collapse:
  REFUSE / STRUCTURAL_DEPENDENCY_COLLAPSE
  preserve base replay receipt + removed dependency + collapse result
  forbid robustness_from_remaining_count
```

- [ ] **Step 4: Encode existing refusal fixtures without weakening them**

```text
broken-ancestry -> refuse exact claim; preserve broken path
coordinate-drift -> refuse unmapped exact spatial citation; preserve target/parent surfaces
favored-hypothesis -> refuse PRESSURE that cannot return disproved; preserve H0
serendipity-promotion -> refuse motive -> evidence; preserve breadcrumb and real evidence path
replay-impersonation -> refuse replay -> historical identity; preserve replay receipt

ghost-promotion -> refuse ghost -> evidence/genealogy; preserve toast-ghost

yarn-promotion -> refuse visual/proposed yarn -> evidence; preserve proposed relation
constitution-smuggling -> refuse inferred constitution; preserve any external constitution receipt separately
```

Every refusal must preserve at least one named survivor.

- [ ] **Step 5: Run contract + runner tests**

```bash
python -m unittest tests.test_crucible_contract tests.test_crucible_runner -v
python tools/crucible.py --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_accepts_everything.py
```

Expected: unit tests pass; cheating adapter exits `1`.

Then:

```bash
python tools/crucible.py --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_refuses_correctly.py
```

Expected: exit `0`. Documentation must still call this a harness test double only.

- [ ] **Step 6: Commit**

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
- Consumes: exact fields/enums from hardening spec.
- Produces: portable contracts for later one-book runtime behavior.

- [ ] **Step 1: Add failing tests for required fields/enums**

Require:

```text
search_observation.coverage_status:
  DECLARED_COMPLETE_FOR_SCOPE | PARTIAL | TRUNCATED | UNKNOWN | NOT_APPLICABLE

inherited_premise.status:
  UNEXAMINED | EXAMINED_SUPPORTED | EXAMINED_CONTRADICTED | EXAMINED_UNRESOLVED | REPLACED | REFUSED

dependency_family.independence_status:
  DEPENDENT | PARTIALLY_DEPENDENT | INDEPENDENT_WITHIN_DECLARED_SCOPE | UNKNOWN

counterfactual_replay.consequence_class:
  SURVIVES_REMOVAL | DEGRADES | CHANGES_VERDICT | COLLAPSES | INSUFFICIENT_TO_TEST
```

- [ ] **Step 2: Run and verify RED**

```bash
python -m unittest tests.test_crucible_contract -v
```

- [ ] **Step 3: Create the four schemas**

Match the record names and required fields from the hardening spec exactly. Two non-negotiable details:

```text
inherited_premise keeps authority_claimed and authority_admitted separate
counterfactual_replay requires base_replay_receipt_id
```

Do not add an unqualified `COMPLETE` search coverage status.

- [ ] **Step 4: Run and verify GREEN**

```bash
python -m unittest tests.test_crucible_contract tests.test_crucible_runner -v
```

Expected: pass.

- [ ] **Step 5: Commit**

```bash
git add crucible/schema tests/test_crucible_contract.py
git commit -m "docs: publish ALEX hardening record contracts"
```

---

### Task 5: Add CI without faking runtime conformance

**Files:**
- Create: `.github/workflows/crucible.yml`
- Modify: `crucible/README.md`
- Modify: `tests/test_crucible_runner.py`

**Interfaces:**
- Consumes: Tasks 1–4.
- Produces: repeatable fixture/harness verification only.

- [ ] **Step 1: Add an all-fixture loading test**

Iterate every canonical fixture and assert it parses and contains the required contract surface.

- [ ] **Step 2: Run local verification**

```bash
python -m unittest discover -s tests -v
```

Expected: pass.

- [ ] **Step 3: Create CI workflow**

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

- [ ] **Step 4: State the conformance boundary in README**

Add verbatim:

> Passing `crucible-contract` proves the fixture corpus and reference harness are internally consistent. It does not prove an ALEX runtime conforms. Runtime conformance begins only when a real adapter executes the applicable fixtures and the harness reports zero constitutional mismatches.

- [ ] **Step 5: Verify cheating still fails**

```bash
python tools/crucible.py --fixture crucible/specimens/search-absence.json --adapter python tests/fixtures/adapter_accepts_everything.py
```

Expected: exit `1`.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/crucible.yml crucible/README.md tests
git commit -m "ci: verify ALEX Crucible contract"
```

---

### Task 6: Gate future runtime claims on Crucible

**Files:**
- Modify: `README.md`
- Modify: `docs/superpowers/specs/2026-08-25-alexandria-floor-design.md`
- Modify: `docs/superpowers/specs/2026-08-26-alex-constitutional-hardening-design.md`
- Modify: `tests/test_crucible_contract.py`

**Interfaces:**
- Consumes: verified contract/harness.
- Produces: explicit no-smuggling gate for later runtime work.

- [ ] **Step 1: Add failing documentation assertion test**

Require all three Markdown files to contain:

```text
CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED
```

- [ ] **Step 2: Run and verify RED**

```bash
python -m unittest tests.test_crucible_contract -v
```

- [ ] **Step 3: Add the boundary phrase and gate rule**

Add near runtime status:

> Before the one-book runtime claims constitutional conformance, a real runtime adapter must execute the applicable Crucible specimens. Contract self-tests and fake adapters are insufficient.

- [ ] **Step 4: Run full verification**

```bash
python -m unittest discover -s tests -v
git diff --check
git grep -n "production.*Python\|Python.*production" README.md docs skills crucible tools || true
```

Expected: tests pass; no accidental text promoting the Python harness into the production runtime.

- [ ] **Step 5: Commit**

```bash
git add README.md docs/superpowers/specs tests/test_crucible_contract.py
git commit -m "docs: gate ALEX runtime claims on Crucible"
```

---

## Self-Review Checklist

Before execution is called complete, verify:

- every new hardening law is named in at least one fixture or published record contract;
- every refusal fixture requires at least one receipt survivor;
- the cheating adapter demonstrably fails;
- the fake correct adapter is never represented as runtime conformance;
- refusal codes `SEARCH_COVERAGE_INSUFFICIENT`, `INDEPENDENCE_NOT_ESTABLISHED`, `PREMISE_NOT_ADMITTED`, and `STRUCTURAL_DEPENDENCY_COLLAPSE` are stable in fixtures;
- remove-one replay preserves its base receipt;
- dependency-family membership never merges witness identity;
- no UI, OCR, database, embedding, archive adapter, or production model dependency appears in Crucible v0;
- there are no placeholder implementation steps.

## Later Gates Intentionally Deferred

This plan publishes contracts for Search Coverage, Inherited Premises, Remove-One Replay, and Dependency Families but does not implement their production behavior. After the first runtime technology is selected against the one-book specimen, create separate implementation plans in this order:

```text
Gate B — exact search emits real search_observation records
Gate C — inquiry preserves inherited_premise records
Gate D — .LEEP runs one-dependency counterfactual replay
Gate E — ancestry analysis emits dependency_family records
```
