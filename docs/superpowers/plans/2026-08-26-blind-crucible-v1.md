# Blind Crucible v1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing ALEX Crucible from an internally consistent fixture harness into a genuinely blind process boundary where the runtime receives a CASE but never the ORACLE, while preserving the existing fixture corpus and refusing to overclaim production ALEX runtime conformance.

**Architecture:** Canonical specimen files remain the authoring/historical corpus. The harness splits each specimen in memory into a runtime-visible CASE and harness-only ORACLE. The CASE carries a deterministic input digest and rule profile; the runtime result must echo the exact case/input/ruleset identity and a narrow execution summary. Metamorphic siblings vary identifiers, nonce, ordering, and distractors without pretending secrecy in an open repository.

**Tech Stack:** Python 3.12 standard library, JSON Schema Draft 2020-12 contracts, SHA-256 canonical JSON digests, `unittest`, subprocess CLI/JSON boundary.

**Spec:** `docs/superpowers/specs/2026-08-26-alex-loadout-runtime-boundary-design.md`, especially §§12–13.

## Global Constraints

- Preserve all existing canonical specimen files and their `expected` blocks; the split happens at the harness boundary.
- The adapter/runtime must never receive `expected`, `constitutional_laws`, fixture notes, or any ORACLE field.
- Do not claim cryptographic secrecy. The pressure mechanism is CASE/ORACLE separation plus metamorphic siblings.
- Do not implement `RELATION-DERIVATION-001` semantics in this gate; that is Gate 2.
- Keep `CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED` in public docs until a real ALEX runtime adapter passes the applicable profile.
- `ACCEPT` remains evaluator disposition only. `ERRORED` remains execution state only.
- No external dependencies are introduced for Gate 1.

---

## Task 1 — Define the blind public contracts

**Files**
- Create: `crucible/schema/case.schema.json`
- Create: `crucible/schema/oracle.schema.json`
- Create: `crucible/schema/runtime-result.schema.json`
- Create: `tools/crucible_blind.py`
- Create: `tests/test_crucible_blind.py`
- Modify: `tests/test_crucible_contract.py`

**Interfaces**

```python
def canonical_json_bytes(value: dict) -> bytes: ...
def sha256_json(value: dict) -> str: ...
def ruleset_digest(rule_profile: str) -> str: ...
def build_case(specimen: dict, *, nonce: str, operation_type: str = "constitutional_evaluation", rule_profile: str = "alex-crucible-v1") -> dict: ...
def build_oracle(specimen: dict, case: dict, *, metamorphic_family: str | None = None) -> dict: ...
```

CASE contract:

```json
{
  "case_id": "search-absence",
  "operation_type": "constitutional_evaluation",
  "rule_profile": "alex-crucible-v1",
  "given": {},
  "attempt": {},
  "nonce": "...",
  "input_digest": "sha256:..."
}
```

ORACLE contract:

```json
{
  "case_id": "search-absence",
  "expected_disposition": "REFUSE",
  "expected_reason_code": "SEARCH_COVERAGE_INSUFFICIENT",
  "required_survivors": ["search_observation:S1"],
  "forbidden_outputs": ["source_absence"],
  "metamorphic_family": null
}
```

Runtime result contract:

```json
{
  "case_id": "search-absence",
  "input_digest": "sha256:...",
  "ruleset_digest": "sha256:...",
  "disposition": "REFUSE",
  "reason_code": "SEARCH_COVERAGE_INSUFFICIENT",
  "receipt_survivors": ["search_observation:S1"],
  "derived_assertions": [],
  "execution_trace_summary": {
    "terminal_state": "FINISHED",
    "step_count": 1
  }
}
```

`execution_trace_summary.terminal_state` enum: `FINISHED | SUSPENDED | ERRORED | CANCELLED`.

- [ ] **RED:** Add schema tests asserting the three new contracts exist, use Draft 2020-12, reject extra conceptual fields by contract (`additionalProperties: false`), and keep evaluator disposition separate from execution terminal state.
- [ ] **RED:** Add unit tests asserting `build_case()` excludes `expected`, `constitutional_laws`, `title`, and `notes`; `build_oracle()` contains the expected answer but no `given` or `attempt`.
- [ ] **RED:** Add digest tests proving canonical object-key ordering yields the same SHA-256 digest and changed semantic content yields a different digest.
- [ ] Run `python -m unittest tests.test_crucible_blind tests.test_crucible_contract -v` and confirm failure because contracts/helpers do not yet exist.
- [ ] **GREEN:** Implement the three JSON Schemas and the minimum helper functions.
- [ ] Compute `input_digest` over the CASE payload *before* the `input_digest` field is inserted.
- [ ] Define `ruleset_digest(rule_profile)` as SHA-256 over canonical JSON serialization of `{"rule_profile": rule_profile}`.
- [ ] Run the focused tests and confirm green.
- [ ] Commit: `feat: define Blind Crucible case and oracle contracts`.

---

## Task 2 — Make the subprocess boundary actually blind

**Files**
- Modify: `tools/crucible.py`
- Modify: `tests/test_crucible_runner.py`
- Modify: `tests/fixtures/adapter_accepts_everything.py`
- Modify: `tests/fixtures/adapter_refuses_correctly.py`
- Create: `tests/fixtures/adapter_answer_echo_cheater.py`
- Create: `tests/fixtures/adapter_id_switch_cheater.py`

**Interfaces**

```python
def validate_runtime_result(case: dict, actual: dict) -> list[str]: ...
def compare_result(case: dict, oracle: dict, actual: dict) -> list[str]: ...
def run_fixture(fixture_path: Path, adapter_argv: list[str], *, nonce: str | None = None) -> int: ...
```

Runner boundary:

```python
specimen = json.loads(fixture_path.read_text(encoding="utf-8"))
case = build_case(specimen, nonce=nonce or secrets.token_hex(16))
oracle = build_oracle(specimen, case)
completed = subprocess.run(
    adapter_argv,
    input=json.dumps(case, sort_keys=True, separators=(",", ":")),
    text=True,
    capture_output=True,
    check=False,
    shell=False,
)
```

- [ ] **RED:** Replace process tests so a correct adapter must consume CASE and return the new runtime-result shape.
- [ ] **RED:** Add an answer-echo cheater fixture. It may cheat only if an `expected`/ORACLE key is visible; otherwise it returns a deterministic wrong result. Assert the harness rejects it.
- [ ] **RED:** Add an ID-switch cheater returning a valid-looking result under another `case_id`. Assert the harness rejects it.
- [ ] **RED:** Add tests for mismatched `input_digest`, mismatched `ruleset_digest`, malformed `execution_trace_summary`, missing required survivor, and forbidden derived assertion.
- [ ] Run `python -m unittest tests.test_crucible_runner -v` and confirm the new tests fail against the old full-specimen boundary.
- [ ] **GREEN:** Change `tools/crucible.py` to construct CASE + ORACLE, send CASE only, validate runtime identity/result shape, then score against ORACLE.
- [ ] `validate_runtime_result()` must require exactly the public runtime-result keys and reject malformed terminal state or non-integer/negative `step_count`.
- [ ] `compare_result()` must compare disposition/reason code, require survivor subset, and reject any `derived_assertions` matching `forbidden_outputs`.
- [ ] Update the two existing reference adapters to compute `ruleset_digest` from the visible `rule_profile` and echo the visible `input_digest`; no fixture adapter may read an ORACLE.
- [ ] Run focused runner tests and confirm green.
- [ ] Run `python -m unittest discover -s tests -v` and confirm the whole corpus contract remains green.
- [ ] Commit: `feat: blind the Crucible adapter boundary`.

---

## Task 3 — Add metamorphic sibling pressure without pretending secrecy

**Files**
- Modify: `tools/crucible_blind.py`
- Modify: `tests/test_crucible_blind.py`
- Create: `tests/fixtures/adapter_relation_surface_reference.py`

**Interface**

```python
def metamorphic_sibling(
    case: dict,
    *,
    suffix: str,
    nonce: str,
    distractor_relation: dict | None = None,
) -> dict: ...
```

Rules:
- deep-copy the CASE;
- append `suffix` to `case_id`;
- replace `nonce`;
- when `given["relations"]` is a list, reverse its order;
- append `distractor_relation` only when supplied;
- recompute `input_digest`;
- preserve `operation_type`, `rule_profile`, and `attempt` exactly.

- [ ] **RED:** Add a unit test proving sibling identity/nonce/digest change while operation/rule profile/attempt remain invariant.
- [ ] **RED:** Add a test proving a relation-list sibling reverses ordering and can carry one unrelated distractor without mutating the original CASE.
- [ ] **RED:** Add a tiny reference adapter and an integration test showing a declared surface-only sibling family yields the same evaluator disposition when only identifier/order/distractor surface changes.
- [ ] Run focused tests and confirm red before helper implementation.
- [ ] **GREEN:** Implement `metamorphic_sibling()` with `copy.deepcopy()` and digest recomputation only.
- [ ] Keep semantic interpretation out of the helper; Gate 1 varies surfaces, Gate 2 owns derivation semantics.
- [ ] Run focused and full test suites; confirm green.
- [ ] Commit: `feat: add Crucible metamorphic sibling pressure`.

---

## Task 4 — Document the exact proof boundary and open the implementation PR

**Files**
- Modify: `crucible/README.md`
- Modify: `tests/test_crucible_runner.py` or `tests/test_crucible_contract.py` for documentation invariants
- Do not modify `.github/workflows/crucible.yml` unless the existing `python -m unittest discover -s tests -v` command fails to collect the new tests.
- Do not remove the existing runtime-conformance disclaimer from `README.md` or specs.

Required documentation language/meaning:

```text
A canonical specimen may contain its expected outcome because it is an authoring/historical artifact.
The adapter boundary never receives that object. The harness lowers it into CASE + ORACLE and sends only CASE.
Metamorphic siblings are anti-overfitting pressure, not secret tests; this is an open repository.
A green crucible-contract run proves the harness/contracts are internally consistent. It does not prove a production ALEX runtime conforms until a real runtime adapter is tested.
```

- [ ] **RED:** Add tests requiring the README to state CASE-only adapter visibility and “metamorphic, not secret” semantics while preserving the existing no-runtime-conformance disclaimer.
- [ ] **GREEN:** Update `crucible/README.md` narrowly; do not rewrite historical fixture documentation.
- [ ] Run `python -m unittest discover -s tests -v` and confirm all tests pass.
- [ ] Inspect `git diff --check` or equivalent diff review for whitespace and accidental fixture mutation.
- [ ] Verify the 16 canonical specimen filenames and file contents remain untouched in this gate.
- [ ] Commit: `docs: define Blind Crucible proof boundary`.
- [ ] Open a pull request from `feat/blind-crucible-v1` to `main` titled `Blind the ALEX Crucible boundary`.
- [ ] In the PR body, explicitly state: CASE/ORACLE split proven; cheater fixtures rejected; metamorphic surface pressure added; canonical fixtures preserved; production ALEX runtime conformance still not claimed.
- [ ] Require the `crucible-contract` workflow to finish green before declaring Gate 1 implementation complete.

---

## Gate 1 Exit Receipt

Gate 1 is complete only when all of these are simultaneously true:

```text
canonical specimen corpus preserved
AND adapter receives CASE only
AND ORACLE remains harness-only
AND input digest is verified
AND ruleset digest is verified
AND wrong case identity is rejected
AND malformed execution summary is rejected
AND missing required residue is rejected
AND forbidden derived output is rejected
AND answer-echo cheater cannot recover the ORACLE from stdin
AND metamorphic sibling generation is deterministic and non-mutating
AND full unittest suite is green
AND crucible-contract CI is green
AND production ALEX runtime conformance is still NOT claimed
```

Only after this receipt may Gate 2 (`RELATION-DERIVATION-001` and the derivation microkernel) begin.