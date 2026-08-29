# ALEX Research Formation Spine v0 + CHRONOBODY-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic exact-SHA organ registry/resolver and a first ALEX Research Formation Spine that executes FAR-SIDE and BINOCULAR as two `INCUBATING` bodies without merging either implementation into `main`.

**Architecture:** `main` owns only the time-addressing law: registry, resolver, local body verification, allowlisted launcher, receipts, and composition. FAR-SIDE and BINOCULAR remain off-main at exact green SHAs. The first spine executes FAR-SIDE, receipts that execution as a discovery trigger only, injects that reference into a caller-supplied BINOCULAR formation, then executes BINOCULAR at its own exact SHA.

**Tech Stack:** Python 3.12 standard library, JSON, existing `alex_runtime.digests`, Git CLI for read-only local identity verification, `unittest`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-28-research-formation-spine-chronobody-design.md`

## Global Constraints

- `main` is constituted present; non-present bodies are exact-SHA pinned.
- Branch names are navigation only, never executable identity.
- Body states are exactly `PRESENT | INCUBATING | HELD | RETIRED | RECONSTITUTED`.
- Modes are exactly `PRESENT_ONLY | EXPERIMENTAL | REPLAY`.
- `HELD` never executes; `RETIRED` executes only under exact `REPLAY`; `INCUBATING` and `RECONSTITUTED` execute only under `EXPERIMENTAL`.
- Runtime never clones, fetches, checks out, pulls, merges, resets, or cleans Git state.
- Runtime never uses shell command strings; only `python-json-stdio/v0` is admitted in v0.
- Every non-present result preserves exact source SHA and body state.
- Every v0 registry entry and execution receipt carries `authority: none`.
- Routing does not promote, admit, merge, publish, canonize, or authorize consequence.
- FAR-SIDE output/receipt may enter BINOCULAR only as discovery provenance, never support.
- No semantic mapping from FAR-SIDE result fields into BINOCULAR compression/expansion fields.
- No Dogram dependency and no network/model calls.
- Repository verification remains `python -m unittest discover -s tests -v`.

## Frozen first body-times

```text
FAR-SIDE
  organ_id: far-side-pass
  branch: feature/far-side-pass-m0
  sha: 52c678767017c170506ce1895d3a610b6ef115b4
  workflow run: 33219406091
  capability: far_side_pressure
  entrypoint: tools/far_side_lab.py

BINOCULAR
  organ_id: binocular-recursion
  branch: impl/binocular-recursion-001
  sha: c26620efc3c601eb0686825e1cfcbe1f1951f49e
  workflow run: 33219240427
  capability: binocular_formation_audit
  entrypoint: tools/run_binocular_recursion.py
```

If either branch moves later, do not mutate these identities. A later SHA is a new body-time.

---

## File Structure

### Create

- `alex_runtime/chronobody.py` — registry types, validation, resolution, local materialization checks, direct JSON-stdio invocation, execution receipts.
- `chronobody/registry.v0.json` — FAR-SIDE and BINOCULAR immutable body-memory entries.
- `tools/run_chronobody.py` — one-body JSON file/stdin runner.
- `alex_runtime/research_formation.py` — outer composition; FAR-SIDE receipt -> discovery-trigger-only bridge -> BINOCULAR.
- `tools/run_research_formation.py` — spine JSON file/stdin runner.
- `tests/test_chronobody_registry.py`
- `tests/test_chronobody_materialization.py`
- `tests/test_chronobody_execution.py`
- `tests/test_chronobody_incubating_integration.py`
- `tests/test_research_formation.py`
- `tests/test_run_chronobody.py`
- `tests/test_run_research_formation.py`
- `tests/fixtures/chronobody/echo_organ.py`
- `tests/fixtures/research_formation/lawful.json`

### Modify

- `.github/workflows/crucible.yml` — second/third exact-SHA checkouts for FAR-SIDE and BINOCULAR integration proof.
- `README.md` — bounded executable-state note after green implementation.

Do not modify `alex_runtime/derivation.py`, projection evaluators, LOADOUT/LOADIN.STEAD runtime, predicate manifests, or Crucible schemas.

---

## Task 1: Freeze registry/body-time contract

**Files:**
- Create: `alex_runtime/chronobody.py`
- Create: `tests/test_chronobody_registry.py`

**Interfaces:**
- Produces: `BodyStatus`, `BodyMode`, `ChronobodyEntry`, `RegistryError`, `parse_registry(value: object) -> tuple[ChronobodyEntry, ...]`

- [ ] **Step 1: Write the failing registry tests**

Start with explicit fixtures:

```python
import copy
import unittest

from alex_runtime.chronobody import RegistryError, parse_registry

FAR_SIDE_SHA = "52c678767017c170506ce1895d3a610b6ef115b4"


def registry_value():
    return {
        "schema": "alex.chronobody-registry/v0",
        "organs": [{
            "organ_id": "far-side-pass",
            "body_time_id": f"far-side-pass@{FAR_SIDE_SHA}",
            "status": "INCUBATING",
            "capabilities": ["far_side_pressure"],
            "source": {
                "repo": "the-static-collective/ALEX.2",
                "branch": "feature/far-side-pass-m0",
                "sha": FAR_SIDE_SHA,
            },
            "runtime": {
                "contract": "python-json-stdio/v0",
                "entrypoint": "tools/far_side_lab.py",
            },
            "verification": {
                "workflow": "crucible-contract",
                "run_id": 33219406091,
                "result": "GREEN",
            },
            "authority": "none",
            "parents": [],
        }],
    }


class ChronobodyRegistryTests(unittest.TestCase):
    def test_exact_body_time_is_accepted(self):
        entries = parse_registry(registry_value())
        self.assertEqual(entries[0].body_time_id, f"far-side-pass@{FAR_SIDE_SHA}")

    def test_branch_without_sha_is_refused(self):
        value = copy.deepcopy(registry_value())
        del value["organs"][0]["source"]["sha"]
        with self.assertRaises(RegistryError) as raised:
            parse_registry(value)
        self.assertEqual(raised.exception.code, "BODY_SHA_REQUIRED")
```

Add cases for unknown status, non-`none` authority, malformed SHA, body-time/SHA mismatch, duplicate body IDs, duplicate capability values, absolute/traversing entrypoints, and non-allowlisted runtime contracts.

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_chronobody_registry -v
```

Expected: import failure for missing `alex_runtime.chronobody`.

- [ ] **Step 3: Implement minimal registry types**

```python
class BodyStatus(str, Enum):
    PRESENT = "PRESENT"
    INCUBATING = "INCUBATING"
    HELD = "HELD"
    RETIRED = "RETIRED"
    RECONSTITUTED = "RECONSTITUTED"


class BodyMode(str, Enum):
    PRESENT_ONLY = "PRESENT_ONLY"
    EXPERIMENTAL = "EXPERIMENTAL"
    REPLAY = "REPLAY"


@dataclass(frozen=True)
class ChronobodyEntry:
    organ_id: str
    body_time_id: str
    status: BodyStatus
    capabilities: tuple[str, ...]
    source_repo: str
    source_branch: str | None
    source_sha: str | None
    runtime_contract: str
    entrypoint: str
    verification_workflow: str | None
    verification_run_id: int | None
    verification_result: str | None
    authority: str
    parents: tuple[str, ...]
```

`RegistryError` has stable `.code` and `.message`. Reject malformed input; do not silently normalize it.

- [ ] **Step 4: Run GREEN**

```bash
python -m unittest tests.test_chronobody_registry -v
```

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/chronobody.py tests/test_chronobody_registry.py
git commit -m "feat: freeze CHRONOBODY registry contract"
```

---

## Task 2: Implement deterministic resolver

**Files:**
- Modify: `alex_runtime/chronobody.py`
- Modify: `tests/test_chronobody_registry.py`

**Interfaces:**
- Produces: `Resolution`, `resolve_body(entries, capability, mode, organ_id=None, body_time_id=None) -> Resolution`
- `Resolution.disposition`: `ROUTED | AMBIGUOUS | UNAVAILABLE | REFUSED`

- [ ] **Step 1: Add RED state/mode tests**

```python
def test_present_only_excludes_incubating(self):
    result = resolve_body(self.entries, "far_side_pressure", BodyMode.PRESENT_ONLY)
    self.assertEqual(result.disposition, "UNAVAILABLE")


def test_experimental_routes_single_incubating(self):
    result = resolve_body(self.entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
    self.assertEqual(result.disposition, "ROUTED")


def test_two_eligible_bodies_are_ambiguous(self):
    result = resolve_body(self.two_entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
    self.assertEqual(result.disposition, "AMBIGUOUS")


def test_replay_requires_exact_body_time(self):
    result = resolve_body(self.entries, "far_side_pressure", BodyMode.REPLAY)
    self.assertEqual(result.disposition, "REFUSED")
    self.assertEqual(result.reason_code, "EXACT_BODY_TIME_REQUIRED")
```

Also cover `HELD`, `RETIRED`, `RECONSTITUTED`, explicit organ mismatch, and explicit body disambiguation.

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_chronobody_registry -v
```

- [ ] **Step 3: Implement pure eligibility table**

```python
_ALLOWED_BY_MODE = {
    BodyMode.PRESENT_ONLY: {BodyStatus.PRESENT},
    BodyMode.EXPERIMENTAL: {
        BodyStatus.PRESENT,
        BodyStatus.INCUBATING,
        BodyStatus.RECONSTITUTED,
    },
    BodyMode.REPLAY: {BodyStatus.RETIRED},
}
```

Never tie-break by timestamp, branch, SHA lexicographic order, registry order, or recency.

- [ ] **Step 4: Run GREEN**

```bash
python -m unittest tests.test_chronobody_registry -v
```

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/chronobody.py tests/test_chronobody_registry.py
git commit -m "feat: resolve exact CHRONOBODY body-times"
```

---

## Task 3: Verify local body materializations without mutating Git

**Files:**
- Modify: `alex_runtime/chronobody.py`
- Create: `tests/test_chronobody_materialization.py`

**Interfaces:**
- Produces: `MaterializationCheck`, `verify_materialization(entry: ChronobodyEntry, root: Path) -> MaterializationCheck`

- [ ] **Step 1: Build temporary Git repo tests**

Use `tempfile.TemporaryDirectory()` plus subprocess Git to create exact committed bodies with an `origin` matching `https://github.com/the-static-collective/ALEX.2.git`.

Required cases:

```text
exact clean SHA + matching repo -> VERIFIED
wrong HEAD -> BODY_SHA_MISMATCH
dirty checkout -> DIRTY_BODY
wrong origin -> SOURCE_REPO_MISMATCH
missing entrypoint -> ENTRYPOINT_MISSING
non-Git path -> NOT_A_GIT_BODY
```

- [ ] **Step 2: Run RED**

```bash
python -m unittest tests.test_chronobody_materialization -v
```

- [ ] **Step 3: Implement read-only Git checks**

Only:

```python
["git", "-C", str(root), "rev-parse", "HEAD"]
["git", "-C", str(root), "status", "--porcelain"]
["git", "-C", str(root), "remote", "get-url", "origin"]
```

Normalize these repository URL forms only:

```text
https://github.com/owner/repo
https://github.com/owner/repo.git
git@github.com:owner/repo.git
```

- [ ] **Step 4: Run GREEN**

```bash
python -m unittest tests.test_chronobody_materialization -v
```

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/chronobody.py tests/test_chronobody_materialization.py
git commit -m "feat: verify exact local CHRONOBODY bodies"
```

---

## Task 4: Add direct JSON-stdio execution and receipts

**Files:**
- Modify: `alex_runtime/chronobody.py`
- Create: `tests/fixtures/chronobody/echo_organ.py`
- Create: `tests/test_chronobody_execution.py`

**Interfaces:**
- Produces: `ExecutionResult`, `execute_body(entry, root, payload, mode, timeout_seconds=30) -> ExecutionResult`
- Receipt schema: `alex.chronobody-execution/v0`

- [ ] **Step 1: Add deterministic synthetic organ**

```python
import json
import sys

payload = json.load(sys.stdin)
json.dump({"schema": "test.echo/v0", "payload": payload}, sys.stdout, sort_keys=True, separators=(",", ":"))
sys.stdout.write("\n")
```

- [ ] **Step 2: Write RED process tests**

Cover completion, input/output digests, exact body receipt fields, non-zero exit, invalid JSON output, timeout, and pre-invocation materialization refusal.

- [ ] **Step 3: Run RED**

```bash
python -m unittest tests.test_chronobody_execution -v
```

- [ ] **Step 4: Implement no-shell invocation**

```python
completed = subprocess.run(
    [sys.executable, str(entrypoint_path)],
    input=canonical_json_bytes(payload),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    timeout=timeout_seconds,
    check=False,
)
```

Use `canonical_json_bytes()` and `sha256_json()` from `alex_runtime.digests`. Keep stderr separate from stdout.

- [ ] **Step 5: Run GREEN**

```bash
python -m unittest tests.test_chronobody_execution -v
```

- [ ] **Step 6: Commit**

```bash
git add alex_runtime/chronobody.py tests/fixtures/chronobody/echo_organ.py tests/test_chronobody_execution.py
git commit -m "feat: execute receipted CHRONOBODY organs"
```

---

## Task 5: Commit FAR-SIDE + BINOCULAR body memory and CLI

**Files:**
- Create: `chronobody/registry.v0.json`
- Create: `tools/run_chronobody.py`
- Modify: `tests/test_chronobody_registry.py`
- Create: `tests/test_run_chronobody.py`

**Interfaces:**
- Request schema: `alex.chronobody-run-request/v0`

- [ ] **Step 1: Write registry with two immutable entries**

Use the exact frozen body-times at the top of this plan. Both have `status: INCUBATING`, `authority: none`, and `runtime.contract: python-json-stdio/v0`.

- [ ] **Step 2: Add committed registry test**

Assert both exact body IDs:

```python
self.assertEqual(
    {entry.body_time_id for entry in entries},
    {
        "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4",
        "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e",
    },
)
```

- [ ] **Step 3: Add RED CLI tests**

Test stdin/file input, malformed request, missing materialization, exact body selection, and canonical JSON result.

- [ ] **Step 4: Implement CLI**

CLI exit semantics:

```text
evaluated route/materialization/execution result -> 0
malformed/unreadable request -> 2
unexpected host exception -> 2
```

No evaluated research refusal is converted into host failure.

- [ ] **Step 5: Run GREEN**

```bash
python -m unittest tests.test_chronobody_registry tests.test_run_chronobody -v
```

- [ ] **Step 6: Commit**

```bash
git add chronobody/registry.v0.json tools/run_chronobody.py tests/test_chronobody_registry.py tests/test_run_chronobody.py
git commit -m "feat: register first ALEX incubating body-times"
```

---

## Task 6: Prove both real off-main bodies in CI

**Files:**
- Modify: `.github/workflows/crucible.yml`
- Create: `tests/test_chronobody_incubating_integration.py`

**CI environment:**

```text
ALEX_FAR_SIDE_BODY_ROOT
ALEX_BINOCULAR_BODY_ROOT
```

- [ ] **Step 1: Add integration tests**

Skip each real-body test only when its environment path is absent. In CI assert:

### FAR-SIDE

- resolved under `EXPERIMENTAL`;
- root SHA equals `52c678...`;
- body is clean and repository-matched;
- load its own `tests/fixtures/far_side/survivor.json`;
- execute through `execute_body()`;
- receipt says `INCUBATING` and exact SHA;
- native result schema matches FAR-SIDE result contract.

### BINOCULAR

- resolved under `EXPERIMENTAL`;
- root SHA equals `c26620e...`;
- body is clean and repository-matched;
- load its own `tests/fixtures/binocular_recursion/lawful-residual.json`;
- execute through `execute_body()`;
- receipt says `INCUBATING` and exact SHA;
- native result schema is `alex.binocular-recursion-result/v0`.

- [ ] **Step 2: Verify local suite**

```bash
python -m unittest discover -s tests -v
```

Expected: both real-body tests skip locally if materializations are not supplied; all other tests pass.

- [ ] **Step 3: Add exact CI materializations**

Preserve current checkout and add:

```yaml
      - uses: actions/checkout@v4
      - uses: actions/checkout@v4
        with:
          ref: 52c678767017c170506ce1895d3a610b6ef115b4
          path: .chronobody/far-side-pass-52c6787
      - uses: actions/checkout@v4
        with:
          ref: c26620efc3c601eb0686825e1cfcbe1f1951f49e
          path: .chronobody/binocular-c26620e
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m unittest discover -s tests -v
        env:
          ALEX_FAR_SIDE_BODY_ROOT: ${{ github.workspace }}/.chronobody/far-side-pass-52c6787
          ALEX_BINOCULAR_BODY_ROOT: ${{ github.workspace }}/.chronobody/binocular-c26620e
```

This is CI fixture materialization; runtime still performs no network/Git mutation.

- [ ] **Step 4: Require exact-head GREEN with both tests executed**

Do not accept a green run in which either integration test skipped.

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/crucible.yml tests/test_chronobody_incubating_integration.py
git commit -m "test: prove off-main ALEX body-time execution"
```

---

## Task 7: Build Research Formation Spine with typed discovery bridge

**Files:**
- Create: `alex_runtime/research_formation.py`
- Create: `tests/test_research_formation.py`
- Create: `tests/fixtures/research_formation/lawful.json`

**Interfaces:**
- Consumes: registry/resolver/executor only; does not import FAR-SIDE or BINOCULAR runtime modules.
- Produces: `evaluate_research_formation_run(request: dict, entries: tuple[ChronobodyEntry, ...]) -> dict`
- Result schema: `alex.research-formation-result/v0`

- [ ] **Step 1: Freeze outer request**

```json
{
  "schema": "alex.research-formation-run/v0",
  "run_id": "formation-001",
  "body_mode": "EXPERIMENTAL",
  "materializations": {
    "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4": "/injected/far-side",
    "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e": "/injected/binocular"
  },
  "far_side": {
    "body_time_id": "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4",
    "case": {}
  },
  "binocular": {
    "body_time_id": "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e",
    "case": {}
  }
}
```

Fixture stores structural content; tests inject machine-local paths.

- [ ] **Step 2: Freeze only permitted bridge**

After FAR-SIDE completes:

```python
far_side_receipt_ref = sha256_json(far_side_execution.receipt)
binocular_case = copy.deepcopy(request["binocular"]["case"])
if far_side_receipt_ref not in binocular_case["discovery_trigger_refs"]:
    binocular_case["discovery_trigger_refs"].append(far_side_receipt_ref)
```

Bridge receipt:

```json
{
  "schema": "alex.research-formation-bridge/v0",
  "kind": "DISCOVERY_TRIGGER_ONLY",
  "from_stage": "far_side",
  "to_stage": "binocular",
  "receipt_ref": "sha256:far-side-execution-receipt-digest",
  "authority": "none"
}
```

Do not insert that reference into support, claim-support, or admitted-premise fields.

- [ ] **Step 3: Add hostile RED tests**

Required cases:

```text
lawful FAR-SIDE + lawful BINOCULAR -> outer COMPLETED
both execution receipts preserve different body-times
FAR-SIDE receipt becomes BINOCULAR discovery trigger only
same receipt preloaded by caller into BINOCULAR claim_support_refs -> BINOCULAR native REFUSE / DISCOVERY_TRIGGER_AS_SUPPORT
FAR-SIDE body mismatch -> stop before BINOCULAR
FAR-SIDE process failure -> no fabricated BINOCULAR result
BINOCULAR native refusal -> outer formation completed with native refusal preserved
PRESENT_ONLY -> incubating FAR-SIDE unavailable; no fallback
```

- [ ] **Step 4: Run RED**

```bash
python -m unittest tests.test_research_formation -v
```

- [ ] **Step 5: Implement composition without semantic conversion**

The outer result preserves:

```text
run_id
body_mode
far_side execution receipt
far_side native result
bridge receipt
binocular execution receipt
binocular native result
execution_state
authority: none
```

The spine never derives BINOCULAR compression/expansion data from FAR-SIDE output. Caller supplies that formation.

- [ ] **Step 6: Run GREEN**

```bash
python -m unittest tests.test_research_formation -v
python -m unittest discover -s tests -v
```

- [ ] **Step 7: Commit**

```bash
git add alex_runtime/research_formation.py tests/test_research_formation.py tests/fixtures/research_formation/lawful.json
git commit -m "feat: compose time-addressed ALEX research formation"
```

---

## Task 8: Add formation CLI

**Files:**
- Create: `tools/run_research_formation.py`
- Create: `tests/test_run_research_formation.py`

- [ ] **Step 1: Add RED CLI tests**

Cover stdin, file input, malformed JSON, bad schema, and deterministic output.

- [ ] **Step 2: Implement CLI**

```python
ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"
```

Evaluated formation results return exit 0; malformed host input returns 2.

- [ ] **Step 3: Run GREEN**

```bash
python -m unittest tests.test_run_research_formation -v
python -m unittest discover -s tests -v
```

- [ ] **Step 4: Commit**

```bash
git add tools/run_research_formation.py tests/test_run_research_formation.py
git commit -m "feat: expose ALEX research formation spine CLI"
```

---

## Task 9: Documentation, hostile audit, exact-head gate

**Files:**
- Modify: `README.md`

- [ ] **Step 1: Document only proven capability**

Add:

```text
ALEX can resolve explicitly registered exact-SHA incubating organs from operator/CI-supplied local materializations, verify body identity, invoke the allowlisted JSON-stdio contract, preserve body-time receipts, and compose FAR-SIDE -> BINOCULAR through a discovery-trigger-only bridge.
```

Also state:

```text
This does not make arbitrary branches executable, does not perform Git checkout/network operations at runtime, and does not promote either incubating organ.
```

- [ ] **Step 2: Hostile source audit**

Confirm runtime code contains none of:

```text
git fetch
git checkout
git pull
git reset --hard
shell=True
os.system
```

Confirm no newest/timestamp tie-break exists.

- [ ] **Step 3: Full verification**

```bash
python -m unittest discover -s tests -v
```

- [ ] **Step 4: Exact-head CI verification**

Require:

- `crucible-contract` success;
- both off-main integration tests executed, not skipped;
- exact implementation head recorded;
- fresh comparison against current `main` reviewed.

- [ ] **Step 5: Commit**

```bash
git add README.md
git commit -m "docs: document time-addressed ALEX research spine"
```

---

## Task 10: PR Completion

- [ ] Compare exact head to current `main`.
- [ ] Refresh if behind; rerun full gate.
- [ ] Confirm no predicate, derivation, projection, LOADOUT/LOADIN.STEAD, or authority semantics changed.
- [ ] Confirm registry contains exact SHAs, not mutable branch-only references.
- [ ] Confirm successful execution never mutates body status.
- [ ] Confirm FAR-SIDE and BINOCULAR remain `INCUBATING` after the test.
- [ ] Confirm two distinct execution receipts prove two distinct software body-times.
- [ ] Confirm discovery trigger is not support.
- [ ] Perform code review under Superpowers discipline.
- [ ] Merge only the exact reviewed green head after explicit integration decision.

---

## Self-Review Receipt

### Spec coverage

- five states / three modes -> Tasks 1–2;
- exact SHA identity -> Tasks 1, 3, 5, 6;
- committed registry memory -> Task 5;
- no runtime Git mutation -> Tasks 3, 9;
- allowlisted JSON-stdio -> Task 4;
- execution receipts -> Task 4;
- two real off-main organs -> Tasks 5–6;
- fully temporal spine -> Task 7;
- discovery != support seam -> Task 7;
- no automatic promotion -> Tasks 2, 5–7, 10;
- no cross-project extraction -> no task creates one.

### Placeholder scan

No `TODO`, `TBD`, ellipsis placeholder, or unspecified implementation step remains.

### Type consistency

```text
ChronobodyEntry
BodyStatus
BodyMode
Resolution
MaterializationCheck
ExecutionResult
parse_registry
resolve_body
verify_materialization
execute_body
evaluate_research_formation_run
```

These names are used consistently throughout the plan.

## Execution Handoff

Plan saved at `docs/superpowers/plans/2026-08-28-research-formation-spine-chronobody.md`.

Recommended implementation: subagent-driven development when available; otherwise execute this plan inline with TDD checkpoints and exact-head GitHub Actions evidence.