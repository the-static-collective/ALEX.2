# ALEX Research Formation Spine v0 + CHRONOBODY-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deterministic, exact-SHA organ registry/resolver and a first ALEX Research Formation Spine that can execute the green FAR-SIDE implementation as an `INCUBATING` body without merging it into constituted `main`, while preserving temporal identity and authority boundaries.

**Architecture:** `main` remains the constituted body. `CHRONOBODY-001` resolves a capability to an explicitly registered body-time, verifies an operator-supplied local checkout against the registered SHA and repository, invokes only an allowlisted JSON-stdio Python entrypoint, and emits a body-time execution receipt. The first spine runs FAR-SIDE through this boundary, receipts its output as a discovery trigger only, then audits a supplied BINOCULAR formation with constituted ALEX code.

**Tech Stack:** Python 3.12 standard library, JSON, SHA-256 via existing `alex_runtime.digests`, Git CLI for local identity verification, `unittest`, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-28-research-formation-spine-chronobody-design.md`

## Global Constraints

- `main` is constituted present; non-present bodies must be exact-SHA pinned.
- Branch names are navigation only and must never establish executable identity.
- V0 body states are exactly `PRESENT | INCUBATING | HELD | RETIRED | RECONSTITUTED`.
- V0 modes are exactly `PRESENT_ONLY | EXPERIMENTAL | REPLAY`.
- `HELD` never executes; `RETIRED` executes only under exact `REPLAY`; `INCUBATING` and `RECONSTITUTED` execute only under `EXPERIMENTAL`.
- No Git clone/fetch/checkout/pull/merge occurs inside runtime execution.
- No shell command strings. V0 invocation contract is only `python-json-stdio/v0`.
- Every non-present execution must preserve exact source SHA in the receipt.
- Every v0 Chronobody entry and execution receipt carries `authority: none`.
- Routing does not promote, admit, merge, publish, canonize, or authorize consequence.
- FAR-SIDE result/receipt may enter the BINOCULAR formation only as a discovery trigger, never as support.
- Dogram is not a runtime dependency.
- No network/model calls are added.
- ALEX runtime tests use `unittest` and the repository-wide gate remains `python -m unittest discover -s tests -v`.

---

## Pre-execution Gate: Constitute BINOCULAR separately

This plan assumes `alex_runtime.binocular_recursion.evaluate_binocular_recursion_case` is available on the implementation base.

Before Task 1:

- use PR Completion discipline on PR #36 (`Implement BINOCULAR-RECURSION-001 auditor`);
- refresh/review against the then-current `main`;
- verify whole-repository `crucible-contract` on the exact candidate head;
- land it only through its own integration decision.

Do **not** merge PR #36 merely because this plan needs it. If it is not separately admitted, stop this plan before Task 7; Tasks 1–6 can still be implemented and reviewed independently.

FAR-SIDE PR #35 is different: do **not** merge its implementation merely to satisfy this plan. Exact green body `52c678767017c170506ce1895d3a610b6ef115b4` is the first intended `INCUBATING` specimen.

---

## File Structure

### Create

- `alex_runtime/chronobody.py` — immutable registry model, validation, resolution, local materialization verification, process invocation, execution receipts.
- `chronobody/registry.v0.json` — committed body-memory registry; first real non-present entry is FAR-SIDE at exact SHA.
- `tools/run_chronobody.py` — JSON file/stdin CLI for one explicit capability/body execution.
- `alex_runtime/research_formation.py` — pure outer composition that bridges FAR-SIDE execution receipt into BINOCULAR discovery provenance.
- `tools/run_research_formation.py` — JSON file/stdin CLI for one spine run.
- `tests/test_chronobody_registry.py` — registry/type/state/mode/resolution tests.
- `tests/test_chronobody_materialization.py` — temporary Git repositories for SHA/repo/dirty/path hostile tests.
- `tests/test_chronobody_execution.py` — deterministic JSON-stdio invocation/receipt tests using a synthetic local organ.
- `tests/test_chronobody_far_side_integration.py` — exact real FAR-SIDE materialization integration test, skipped unless CI provides path.
- `tests/test_research_formation.py` — composition tests proving discovery/support separation and body-time receipt preservation.
- `tests/fixtures/chronobody/echo_organ.py` — deterministic local synthetic JSON-stdio organ used only for execution-contract tests.
- `tests/fixtures/research_formation/lawful.json` — lawful FAR-SIDE + BINOCULAR outer specimen after BINOCULAR lands.

### Modify

- `.github/workflows/crucible.yml` — materialize exact FAR-SIDE SHA in a second checkout and expose its path only to the integration test.
- `README.md` — one bounded executable-state section after implementation proves green; no general conformance claim.

Do not modify `alex_runtime/derivation.py`, `alex_runtime/projection_*`, `loadout_runtime/`, predicate manifests, or Crucible schemas in v0.

---

## Task 1: Freeze registry enums and immutable body identity

**Files:**
- Create: `alex_runtime/chronobody.py`
- Create: `tests/test_chronobody_registry.py`

**Interfaces:**
- Produces: `BodyStatus`, `BodyMode`, `ChronobodyEntry`, `RegistryError`, `parse_registry(value: object) -> tuple[ChronobodyEntry, ...]`
- Later tasks consume these exact names.

- [ ] **Step 1: Write failing enum/body-identity tests**

Add tests equivalent to:

```python
from alex_runtime.chronobody import RegistryError, parse_registry

FAR_SIDE_SHA = "52c678767017c170506ce1895d3a610b6ef115b4"


def test_nonpresent_body_requires_exact_sha_and_matching_body_time_id():
    registry = {
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

    entries = parse_registry(registry)
    assert entries[0].body_time_id == f"far-side-pass@{FAR_SIDE_SHA}"


def test_branch_name_without_sha_is_refused():
    # same entry, remove source.sha
    # assert parse_registry raises RegistryError with code BODY_SHA_REQUIRED
    ...
```

Replace the ellipsis before commit with explicit fixture mutation/assertion; no placeholder remains in committed tests.

Also test:

- unknown status;
- unknown mode is refused by the later resolver type constructor;
- `authority != none` is refused;
- short/non-hex SHA is refused;
- `body_time_id` SHA mismatch is refused;
- duplicate `body_time_id` is refused;
- duplicate capability strings inside an entry are refused;
- entrypoint containing `..` or starting `/` is refused;
- runtime contract other than `python-json-stdio/v0` is refused.

- [ ] **Step 2: Run the focused test and confirm RED**

Run:

```bash
python -m unittest tests.test_chronobody_registry -v
```

Expected: import failure because `alex_runtime.chronobody` does not exist.

- [ ] **Step 3: Implement immutable registry types and validation**

Use standard-library dataclasses/enums:

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

Implement `RegistryError` with stable `.code` and `.message` fields. Reject malformed input rather than normalizing it silently.

- [ ] **Step 4: Run focused tests GREEN**

```bash
python -m unittest tests.test_chronobody_registry -v
```

Expected: all Task-1 tests pass.

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/chronobody.py tests/test_chronobody_registry.py
git commit -m "feat: freeze CHRONOBODY registry contract"
```

---

## Task 2: Implement deterministic body resolution without latest-wins

**Files:**
- Modify: `alex_runtime/chronobody.py`
- Modify: `tests/test_chronobody_registry.py`

**Interfaces:**
- Consumes: `ChronobodyEntry`, `BodyStatus`, `BodyMode`
- Produces: `Resolution`, `resolve_body(entries, capability, mode, organ_id=None, body_time_id=None) -> Resolution`

`Resolution.disposition` is exactly `ROUTED | AMBIGUOUS | UNAVAILABLE | REFUSED`.

- [ ] **Step 1: Write failing resolution tests**

Cover the matrix explicitly:

```python
def test_present_only_excludes_incubating():
    result = resolve_body(entries, "far_side_pressure", BodyMode.PRESENT_ONLY)
    assert result.disposition == "UNAVAILABLE"


def test_experimental_routes_single_incubating_body():
    result = resolve_body(entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
    assert result.disposition == "ROUTED"
    assert result.entry.body_time_id.endswith(FAR_SIDE_SHA)


def test_two_eligible_bodies_are_ambiguous_not_latest_wins():
    result = resolve_body(two_incubating_entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
    assert result.disposition == "AMBIGUOUS"


def test_replay_requires_exact_body_time_id():
    result = resolve_body(entries, "far_side_pressure", BodyMode.REPLAY)
    assert result.disposition == "REFUSED"
    assert result.reason_code == "EXACT_BODY_TIME_REQUIRED"
```

Also test `HELD` refusal, `RETIRED` replay-only, explicit body mismatch, and explicit organ disambiguation.

- [ ] **Step 2: Run focused tests RED**

```bash
python -m unittest tests.test_chronobody_registry -v
```

Expected: missing `resolve_body`/`Resolution` failures only.

- [ ] **Step 3: Implement resolver**

Implement state eligibility as a pure table; do not sort by SHA, branch, timestamp, or registry position to choose a winner.

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

For `REPLAY`, require exact `body_time_id` before filtering. For an explicit non-retired exact body in replay mode, return `REFUSED / BODY_MODE_MISMATCH` rather than silently widening eligibility.

- [ ] **Step 4: Run focused tests GREEN**

```bash
python -m unittest tests.test_chronobody_registry -v
```

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/chronobody.py tests/test_chronobody_registry.py
git commit -m "feat: resolve exact CHRONOBODY body-times"
```

---

## Task 3: Verify local materialization identity and cleanliness

**Files:**
- Modify: `alex_runtime/chronobody.py`
- Create: `tests/test_chronobody_materialization.py`

**Interfaces:**
- Produces: `MaterializationCheck`, `verify_materialization(entry: ChronobodyEntry, root: Path) -> MaterializationCheck`

- [ ] **Step 1: Write temporary-Git-repo hostile tests**

Use `tempfile.TemporaryDirectory()` and subprocess Git commands to create a tiny local repository. Configure an origin URL matching `https://github.com/the-static-collective/ALEX.2.git` so repository identity is testable.

Test exact cases:

```text
clean exact SHA + matching origin -> VERIFIED
wrong HEAD -> REFUSED / BODY_SHA_MISMATCH
dirty worktree -> REFUSED / DIRTY_BODY
wrong origin repo -> REFUSED / SOURCE_REPO_MISMATCH
missing entrypoint -> REFUSED / ENTRYPOINT_MISSING
non-git directory -> REFUSED / NOT_A_GIT_BODY
```

- [ ] **Step 2: Run focused tests RED**

```bash
python -m unittest tests.test_chronobody_materialization -v
```

- [ ] **Step 3: Implement Git identity checks without mutation**

Only use read-only commands:

```python
["git", "-C", str(root), "rev-parse", "HEAD"]
["git", "-C", str(root), "status", "--porcelain"]
["git", "-C", str(root), "remote", "get-url", "origin"]
```

Normalize only these equivalent GitHub repository forms:

```text
https://github.com/owner/repo
https://github.com/owner/repo.git
git@github.com:owner/repo.git
```

Do not call fetch, checkout, reset, clean, pull, or merge.

- [ ] **Step 4: Run focused tests GREEN**

```bash
python -m unittest tests.test_chronobody_materialization -v
```

- [ ] **Step 5: Commit**

```bash
git add alex_runtime/chronobody.py tests/test_chronobody_materialization.py
git commit -m "feat: verify exact local CHRONOBODY materializations"
```

---

## Task 4: Add allowlisted JSON-stdio invocation and execution receipts

**Files:**
- Modify: `alex_runtime/chronobody.py`
- Create: `tests/fixtures/chronobody/echo_organ.py`
- Create: `tests/test_chronobody_execution.py`

**Interfaces:**
- Produces: `ExecutionResult`, `execute_body(entry, root, payload, mode, timeout_seconds=30) -> ExecutionResult`
- `ExecutionResult.receipt` schema is `alex.chronobody-execution/v0`.

- [ ] **Step 1: Add a deterministic synthetic organ**

`tests/fixtures/chronobody/echo_organ.py` must read exactly one JSON value from stdin and emit canonical JSON such as:

```python
import json
import sys

payload = json.load(sys.stdin)
json.dump({"schema": "test.echo/v0", "payload": payload}, sys.stdout, sort_keys=True, separators=(",", ":"))
sys.stdout.write("\n")
```

- [ ] **Step 2: Write RED execution tests**

Create a temporary Git repository containing the synthetic organ, register its exact commit SHA, and test:

- exact clean body completes;
- stdout parses as one JSON value;
- `input_digest` equals existing `sha256_json(payload)`;
- `output_digest` equals `sha256_json(parsed_output)`;
- receipt includes exact `body_time_id`, status, mode, SHA, runtime contract, entrypoint, exit code, `authority: none`;
- non-zero child exit returns visible `FAILED` execution state;
- invalid JSON stdout returns `FAILED / INVALID_JSON_OUTPUT`;
- timeout returns `FAILED / TIMEOUT`;
- materialization refusal prevents child invocation.

- [ ] **Step 3: Run execution tests RED**

```bash
python -m unittest tests.test_chronobody_execution -v
```

- [ ] **Step 4: Implement direct subprocess invocation**

Use no shell:

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

Parse stdout with `json.loads`. Preserve stderr as a decoded diagnostic field or its digest; never merge stderr into JSON stdout.

Use existing `canonical_json_bytes()` and `sha256_json()` from `alex_runtime.digests` rather than creating a second canonicalization implementation.

- [ ] **Step 5: Run execution tests GREEN**

```bash
python -m unittest tests.test_chronobody_execution -v
```

- [ ] **Step 6: Commit**

```bash
git add alex_runtime/chronobody.py tests/fixtures/chronobody/echo_organ.py tests/test_chronobody_execution.py
git commit -m "feat: execute receipted CHRONOBODY organs"
```

---

## Task 5: Commit the first real body-memory entry and one CLI

**Files:**
- Create: `chronobody/registry.v0.json`
- Create: `tools/run_chronobody.py`
- Modify: `tests/test_chronobody_registry.py`
- Create or modify: `tests/test_run_chronobody.py`

**Interfaces:**
- CLI request schema:

```json
{
  "schema": "alex.chronobody-run-request/v0",
  "capability": "far_side_pressure",
  "mode": "EXPERIMENTAL",
  "organ_id": "far-side-pass",
  "body_time_id": "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4",
  "materializations": {
    "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4": "/absolute/local/path"
  },
  "payload": {}
}
```

- [ ] **Step 1: Add the exact FAR-SIDE registry entry**

Use:

```text
organ_id: far-side-pass
status: INCUBATING
capability: far_side_pressure
repo: the-static-collective/ALEX.2
branch: feature/far-side-pass-m0
sha: 52c678767017c170506ce1895d3a610b6ef115b4
contract: python-json-stdio/v0
entrypoint: tools/far_side_lab.py
workflow: crucible-contract
run_id: 33219406091
verification result: GREEN
authority: none
```

Do not update this entry if the branch later moves. A later SHA is a later body entry.

- [ ] **Step 2: Add registry-file validation test**

Read the committed file and pass it through `parse_registry()`; assert the exact FAR-SIDE `body_time_id`.

- [ ] **Step 3: Write CLI RED tests**

Test stdin and file input, malformed request, missing materialization, and deterministic JSON output shape.

- [ ] **Step 4: Implement `tools/run_chronobody.py`**

CLI behavior:

```text
path arg absent or '-' -> stdin
valid evaluated run -> exit 0 even if organ-native research result is a refusal
malformed/unreadable request -> exit 2
Chronobody route/materialization/execution refusal -> emit structured result JSON and exit 0
unexpected host exception -> stderr + exit 2
```

This matches the repository's distinction between evaluated refusal and harness failure.

- [ ] **Step 5: Run focused tests GREEN**

```bash
python -m unittest tests.test_chronobody_registry tests.test_run_chronobody -v
```

- [ ] **Step 6: Commit**

```bash
git add chronobody/registry.v0.json tools/run_chronobody.py tests/test_chronobody_registry.py tests/test_run_chronobody.py
git commit -m "feat: register FAR-SIDE as an incubating body-time"
```

---

## Task 6: Prove real exact-SHA FAR-SIDE execution in CI without merging it

**Files:**
- Modify: `.github/workflows/crucible.yml`
- Create: `tests/test_chronobody_far_side_integration.py`

**Interfaces:**
- CI environment variable: `ALEX_FAR_SIDE_BODY_ROOT`

- [ ] **Step 1: Write integration test with local skip boundary**

The test must skip only when `ALEX_FAR_SIDE_BODY_ROOT` is absent. When present it must:

1. load the committed registry;
2. resolve `far_side_pressure` under `EXPERIMENTAL`;
3. verify the supplied body root exactly matches `52c678...`;
4. load a valid FAR-SIDE case from the materialized body's own `tests/fixtures/far_side/survivor.json`;
5. execute it through `execute_body()`;
6. assert `execution_state == COMPLETED`;
7. assert receipt `organ_status == INCUBATING` and exact source SHA;
8. assert organ-native output schema is the FAR-SIDE result schema;
9. assert registry remains unchanged and no promotion field exists.

- [ ] **Step 2: Run local full suite**

```bash
python -m unittest discover -s tests -v
```

Expected: integration test skips locally; all other tests pass.

- [ ] **Step 3: Modify GitHub Actions to materialize exact body**

Preserve the existing primary checkout, then add a second checkout:

```yaml
      - uses: actions/checkout@v4
      - uses: actions/checkout@v4
        with:
          ref: 52c678767017c170506ce1895d3a610b6ef115b4
          path: .chronobody/far-side-pass-52c6787
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: python -m unittest discover -s tests -v
        env:
          ALEX_FAR_SIDE_BODY_ROOT: ${{ github.workspace }}/.chronobody/far-side-pass-52c6787
```

The second checkout is CI materialization only. Runtime code still performs no network or Git mutation.

- [ ] **Step 4: Push and require exact-head GitHub Actions GREEN**

Expected integration evidence must show the test did not skip in CI.

- [ ] **Step 5: Commit workflow/test**

```bash
git add .github/workflows/crucible.yml tests/test_chronobody_far_side_integration.py
git commit -m "test: prove exact-SHA incubating FAR-SIDE execution"
```

---

## Task 7: Build the Research Formation Spine bridge

**Prerequisite:** BINOCULAR implementation is present on the base through its own landed integration.

**Files:**
- Create: `alex_runtime/research_formation.py`
- Create: `tests/test_research_formation.py`
- Create: `tests/fixtures/research_formation/lawful.json`

**Interfaces:**
- Consumes: `execute_body()`, Chronobody registry/resolution, `evaluate_binocular_recursion_case()`
- Produces: `evaluate_research_formation_run(request: dict, registry: tuple[ChronobodyEntry, ...]) -> dict`
- Result schema: `alex.research-formation-result/v0`

- [ ] **Step 1: Freeze the outer request contract in tests**

Use this shape:

```json
{
  "schema": "alex.research-formation-run/v0",
  "run_id": "formation-001",
  "body_mode": "EXPERIMENTAL",
  "materializations": {
    "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4": "/path/injected-by-test"
  },
  "far_side": {
    "organ_id": "far-side-pass",
    "body_time_id": "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4",
    "case": {}
  },
  "binocular_case": {
    "schema": "alex.binocular-recursion-case/v0"
  }
}
```

The fixture file stores the structural specimen but the test injects the machine-local materialization path at runtime.

- [ ] **Step 2: Define the only v0 bridge**

After FAR-SIDE execution, compute:

```python
far_side_receipt_ref = sha256_json(far_side_execution.receipt)
```

Deep-copy the supplied BINOCULAR case and append `far_side_receipt_ref` to `discovery_trigger_refs` if not already present.

Do **not** append it to:

```text
support_refs
compression.claim_support_refs
admitted_premise_refs
```

The result must include a bridge receipt:

```json
{
  "schema": "alex.research-formation-bridge/v0",
  "kind": "DISCOVERY_TRIGGER_ONLY",
  "from_stage": "far_side",
  "to_stage": "binocular",
  "receipt_ref": "sha256:...",
  "authority": "none"
}
```

- [ ] **Step 3: Write hostile RED tests**

Required cases:

```text
lawful FAR-SIDE completion + lawful BINOCULAR case -> outer COMPLETED
FAR-SIDE receipt appears in BINOCULAR discovery_trigger_refs only -> preserved
caller preloads same FAR-SIDE receipt into claim_support_refs -> BINOCULAR refuses DISCOVERY_TRIGGER_AS_SUPPORT
Chronobody body mismatch -> spine stops before BINOCULAR and preserves refusal
FAR-SIDE process failure -> spine does not fabricate BINOCULAR result
BINOCULAR refusal -> outer run remains completed formation with binocular disposition REFUSE; not host failure
body mode PRESENT_ONLY with only incubating FAR-SIDE -> route unavailable; no fallback
```

- [ ] **Step 4: Run RED**

```bash
python -m unittest tests.test_research_formation -v
```

- [ ] **Step 5: Implement the pure outer composition**

Do not make semantic mappings from FAR-SIDE result fields into BINOCULAR compression/expansion fields. The caller still supplies the BINOCULAR formation. V0 composes provenance, not meanings.

The outer result should preserve:

```text
run_id
body_mode
chronobody execution receipt
far_side result
bridge receipt
binocular result
execution_state
authority: none
```

- [ ] **Step 6: Run focused + full suite GREEN**

```bash
python -m unittest tests.test_research_formation -v
python -m unittest discover -s tests -v
```

- [ ] **Step 7: Commit**

```bash
git add alex_runtime/research_formation.py tests/test_research_formation.py tests/fixtures/research_formation/lawful.json
git commit -m "feat: compose receipted ALEX research formation spine"
```

---

## Task 8: Add the formation CLI without widening semantics

**Files:**
- Create: `tools/run_research_formation.py`
- Create: `tests/test_run_research_formation.py`

**Interfaces:**
- CLI delegates to `evaluate_research_formation_run()` and committed registry.

- [ ] **Step 1: Write CLI RED tests**

Test stdin, file path, malformed JSON, missing required schema, and deterministic output.

- [ ] **Step 2: Implement CLI**

Follow repository conventions:

```python
ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"
```

Use canonical JSON output. Evaluated research refusals return exit 0; malformed host input returns 2.

- [ ] **Step 3: Run focused and full GREEN**

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

## Task 9: Documentation, hostile audit, and exact-head verification

**Files:**
- Modify: `README.md`
- Review: all files from Tasks 1–8

- [ ] **Step 1: Add bounded README executable-state note**

Document only what tests prove:

```text
ALEX can resolve an explicitly registered exact-SHA incubating organ from an operator-supplied local materialization, verify its body identity, invoke the allowlisted JSON-stdio contract, and preserve a body-time execution receipt.
```

Also state:

```text
This does not make arbitrary branches executable, does not clone or checkout code at runtime, and does not promote incubating organs to present ALEX.
```

- [ ] **Step 2: Run hostile string/search audit**

Confirm implementation contains no runtime use of:

```text
git fetch
git checkout
git pull
git reset --hard
shell=True
os.system
```

Confirm no `latest` or timestamp-based body tie-break exists.

- [ ] **Step 3: Run whole repository verification**

```bash
python -m unittest discover -s tests -v
```

Expected: all tests pass; FAR-SIDE integration skips only outside CI.

- [ ] **Step 4: Push and verify exact-head `crucible-contract`**

Required evidence:

- workflow conclusion `success`;
- FAR-SIDE integration test executed rather than skipped;
- exact implementation head recorded in PR body;
- branch comparison against then-current `main` reviewed for accidental files.

- [ ] **Step 5: Commit documentation**

```bash
git add README.md
git commit -m "docs: document time-addressed ALEX organ routing"
```

---

## Task 10: PR Completion gate

Use the repository's PR Completion discipline. This task is review/landing only and must not manufacture code changes to make a stale review look current.

- [ ] Compare exact head to current `main`.
- [ ] If behind, refresh and rerun the full exact-head gate.
- [ ] Confirm no unexpected changes to ALEX predicate semantics, LOADOUT, LOADIN.STEAD, derivation, projection, or authority surfaces.
- [ ] Confirm registry contains FAR-SIDE exact SHA rather than a mutable branch-only reference.
- [ ] Confirm UI/README language says `INCUBATING`, not merely `enabled`.
- [ ] Confirm successful route/execution never mutates registry status.
- [ ] Confirm the branch-time integration proves actual off-main code execution from the pinned SHA.
- [ ] Request/perform code review per Superpowers discipline.
- [ ] Merge only after the exact reviewed head is green and the integration decision is explicit.

---

## Self-Review Receipt

### Spec coverage

- five body states -> Tasks 1–2;
- three execution modes -> Task 2;
- exact SHA identity -> Tasks 1, 3, 6;
- registry memory -> Tasks 1, 5;
- no runtime Git mutation -> Tasks 3, 9;
- allowlisted process contract -> Task 4;
- body-time execution receipt -> Task 4;
- FAR-SIDE remains off-main -> Tasks 5–6;
- branch-drift / dirty / ambiguity / held / replay hostile controls -> Tasks 2–4;
- Research Formation Spine -> Tasks 7–8;
- discovery trigger != support at composition seam -> Task 7;
- no automatic promotion -> Tasks 2, 5, 6, 10;
- no cross-project protocol extraction -> no implementation task creates one.

### Placeholder scan

Implementation steps contain no intended `TODO`, `TBD`, or "implement later" instructions. The illustrative ellipsis in Task 1 is explicitly required to be replaced before the test commit; an executor must not commit it.

### Type consistency

The plan consistently uses:

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
evaluate_binocular_recursion_case
```

No alternate spellings are introduced.

## Execution Handoff

Plan complete at `docs/superpowers/plans/2026-08-28-research-formation-spine-chronobody.md`.

Recommended execution path after design review: **subagent-driven development**, one fresh implementation/review context per task. If subagents are unavailable in the host, use the executing-plans discipline inline with checkpoints and exact-head verification.