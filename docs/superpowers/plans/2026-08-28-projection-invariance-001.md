# PROJECTION-INVARIANCE-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one pure ALEX crucible evaluator that detects hidden-state influence across declared observer-local boundaries without duplicating 3rdi projection semantics or granting authority.

**Architecture:** ALEX receives already-formed projection witnesses from two materially different worlds and compares only their declared boundary digests in a fixed order. The evaluator classifies the first leaking boundary (`LOADOUT_LEAK`, `PROJECTION_LEAK`, `DERIVATION_LEAK`, `SERIALIZATION_LEAK`, `NARRATIVE_LEAK`) and separately refuses authority changes; a narrowly declared narrative transform may authorize one narrative difference when both sides carry the same transform receipt.

**Tech Stack:** Python 3.12 standard library, `unittest`, immutable JSON test fixtures.

**Spec:** `docs/superpowers/specs/2026-08-28-projection-invariance-frontier-design.md`

## Global Constraints

- Do not import or reimplement the 3rdi kernel; ALEX consumes compatible projection witnesses only.
- No new predicate manifest entries, persistence layer, network dependency, UI, authority surface, or cross-repository master runtime.
- `world_digest` must differ while each side's declared observer constraints and visible input remain equivalent for a valid invariance trial.
- Boundary comparison order is LOADOUT → PROJECTION → DERIVATION → SERIALIZATION → NARRATIVE → AUTHORITY.
- A declared transform can authorize only the narrative boundary and requires the same non-empty transform receipt on both sides.
- Passing the specimen never changes canon, admission, publication, warrant, or execution authority.
- Failed hostile fixtures remain committed alongside passing controls.
- Projection-pair fixtures live under `tests/fixtures/projection_invariance/`; `crucible/specimens/` remains the closed generic Crucible corpus.

---

### Task 1: Freeze the crucible contract with hostile fixtures

**Files:**
- Create: `tests/fixtures/projection_invariance/clean.json`
- Create: `tests/fixtures/projection_invariance/projection-leak.json`
- Create: `tests/fixtures/projection_invariance/foreshadow-control.json`
- Create: `tests/test_projection_invariance.py`

**Interfaces:**
- Consumes: JSON fixtures containing `case_id`, `left`, `right`, and optional `declared_transform`; each side carries world, observer-constraint, visible-input, boundary, authority, and receipt digests/refs.
- Produces: expected callable `evaluate_projection_invariance_case(case: dict) -> dict` in `alex_runtime.projection_invariance`.

- [x] **Step 1: Write failing tests for clean invariance, projection leak, declared narrative transform, no-authority behavior, observer/input equivalence, and input immutability.**
- [x] **Step 2: Run the full CI test suite and verify RED.**

Witness: GitHub Actions run `33141702492` failed with the existing suite green and only `ModuleNotFoundError: alex_runtime.projection_invariance` remaining after the fixture-location correction.

- [x] **Step 3: Preserve the test fixtures outside the closed canonical Crucible corpus.**

The first RED run also proved that `crucible/specimens/` is a closed schema-controlled corpus. Projection-pair fixtures were moved to `tests/fixtures/projection_invariance/` rather than weakening that invariant.

---

### Task 2: Implement the minimal pure evaluator

**Files:**
- Create: `alex_runtime/projection_invariance.py`
- Test: `tests/test_projection_invariance.py`

**Interfaces:**
- Consumes: `evaluate_projection_invariance_case(case: dict) -> dict` input contract frozen in Task 1.
- Produces: deterministic disposition, reason code, leaking boundary, and preserved receipt references.

- [x] **Step 1: Implement structural validation.**

Return `INSUFFICIENT_TO_TEST` for identical world digests, mismatched observer-constraint digests, mismatched visible-input digests, malformed side objects, or an invalid declared transform.

- [x] **Step 2: Implement ordered boundary comparison.**

```text
bounded_context_digest -> LOADOUT_LEAK
projection_digest      -> PROJECTION_LEAK
derivation_digest      -> DERIVATION_LEAK
serialization_digest   -> SERIALIZATION_LEAK
narrative_digest       -> NARRATIVE_LEAK
authority_digest       -> AUTHORITY_CHANGED
```

The evaluator stops at the first mismatch so downstream symptoms do not overwrite the actual leaking boundary.

- [x] **Step 3: Implement the one positive-control exception.**

A narrative mismatch is allowed only when `declared_transform.boundary == "NARRATIVE"`, `receipt_ref` is non-empty, and both side `receipt_refs` contain that exact receipt. No other boundary may be waived.

- [x] **Step 4: Preserve source inputs and receipt ancestry.**

The evaluator does not mutate `case`, returns the stable union of side receipt references, and emits no authority/canon/publication/admission surface.

- [x] **Step 5: Run full regression suite.**

Witness: GitHub Actions run `33141738957` completed successfully after the minimal evaluator landed.

---

### Task 3: Document and reverify the local conformance boundary

**Files:**
- Modify: `crucible/README.md`

**Interfaces:**
- Consumes: locally verified `PROJECTION-INVARIANCE-001` behavior.
- Produces: documentation stating what the evaluator checks and explicitly what it does not prove.

- [x] **Step 1: Add a compact `PROJECTION-INVARIANCE-001` section.**

The documentation states that ALEX compares already-formed observer-local witness digests, names the earliest hidden-state leak, permits only a doubly receipted narrative transform, preserves hostile fixtures, and grants no external authority.

- [x] **Step 2: Run the full suite after the documentation and plan reconciliation.**

Witness: GitHub Actions run `33141803348` completed successfully on the documentation + reconciled-plan head.

## Self-Review

- Spec coverage: core invariance, hostile projection leak, legal declared transform, no-authority control, leaking-boundary naming, observer/input equivalence, input immutability, and preserved failed fixtures are covered.
- Scope: no event-structure primitive, universal cut object, interpretation identity schema, edge-birth schema, aperture profile, or narrative-flow runtime is implemented.
- Type consistency: one public entry point only: `evaluate_projection_invariance_case(case: dict) -> dict`.
- Dependency check: Python standard library only.
