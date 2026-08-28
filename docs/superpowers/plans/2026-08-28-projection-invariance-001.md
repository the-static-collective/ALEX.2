# PROJECTION-INVARIANCE-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one pure ALEX crucible evaluator that detects hidden-state influence across declared observer-local boundaries without duplicating 3rdi projection semantics or granting authority.

**Architecture:** ALEX receives already-formed projection witnesses from two materially different worlds and compares only their declared boundary digests in a fixed order. The evaluator classifies the first leaking boundary (`LOADOUT_LEAK`, `PROJECTION_LEAK`, `DERIVATION_LEAK`, `SERIALIZATION_LEAK`, `NARRATIVE_LEAK`) and separately refuses authority changes; a narrowly declared narrative transform may authorize one narrative difference when both sides carry the same transform receipt.

**Tech Stack:** Python 3.12 standard library, `unittest`, immutable JSON fixtures.

**Spec:** `docs/superpowers/specs/2026-08-28-projection-invariance-frontier-design.md`

## Global Constraints

- Do not import or reimplement the 3rdi kernel; ALEX consumes compatible projection witnesses only.
- No new predicate manifest entries, persistence layer, network dependency, UI, authority surface, or cross-repository master runtime.
- `world_digest` must differ while declared observer constraints and visible input remain equivalent for a valid invariance trial.
- Boundary comparison order is LOADOUT → PROJECTION → DERIVATION → SERIALIZATION → NARRATIVE → AUTHORITY.
- A declared transform can authorize only the boundary it names and requires the same non-empty transform receipt on both sides.
- Passing the specimen never changes canon, admission, publication, warrant, or execution authority.
- Failed hostile fixtures remain committed alongside passing controls.

---

### Task 1: Freeze the crucible contract with hostile fixtures

**Files:**
- Create: `crucible/specimens/projection-invariance-001-clean.json`
- Create: `crucible/specimens/projection-invariance-001-projection-leak.json`
- Create: `crucible/specimens/projection-invariance-001-foreshadow-control.json`
- Create: `tests/test_projection_invariance.py`

**Interfaces:**
- Consumes: JSON fixtures containing `case_id`, `observer_constraints_digest`, `visible_input_digest`, `left`, `right`, and optional `declared_transform`.
- Produces: expected callable `evaluate_projection_invariance_case(case: dict) -> dict` in `alex_runtime.projection_invariance`.

- [ ] **Step 1: Write failing tests for clean invariance, projection leak, declared narrative transform, no-authority behavior, and input immutability.**

Expected result shape:

```python
{
    "case_id": "...",
    "disposition": "ACCEPT" | "REFUSE" | "INSUFFICIENT_TO_TEST",
    "reason_code": None | "...",
    "leaking_boundary": None | "LOADOUT" | "PROJECTION" | "DERIVATION" | "SERIALIZATION" | "NARRATIVE" | "AUTHORITY",
    "receipt_survivors": ["..."],
}
```

- [ ] **Step 2: Run `python -m unittest tests.test_projection_invariance -v`.**

Expected: FAIL because `alex_runtime.projection_invariance` does not yet exist.

- [ ] **Step 3: Commit only the plan, fixtures, and failing tests.**

```bash
git add docs/superpowers/plans/2026-08-28-projection-invariance-001.md crucible/specimens/projection-invariance-001-*.json tests/test_projection_invariance.py
git commit -m "test: freeze projection invariance crucible"
```

---

### Task 2: Implement the minimal pure evaluator

**Files:**
- Create: `alex_runtime/projection_invariance.py`
- Test: `tests/test_projection_invariance.py`

**Interfaces:**
- Consumes: `evaluate_projection_invariance_case(case: dict) -> dict` input contract frozen in Task 1.
- Produces: deterministic disposition, reason code, leaking boundary, and preserved receipt references.

- [ ] **Step 1: Implement structural validation.**

Return `INSUFFICIENT_TO_TEST` for: identical world digests, mismatched observer-constraint digests, mismatched visible-input digests, malformed side objects, or an invalid declared transform.

- [ ] **Step 2: Implement ordered boundary comparison.**

Compare exact digest fields in this order:

```text
bounded_context_digest -> LOADOUT_LEAK
projection_digest      -> PROJECTION_LEAK
derivation_digest      -> DERIVATION_LEAK
serialization_digest   -> SERIALIZATION_LEAK
narrative_digest       -> NARRATIVE_LEAK
authority_digest       -> AUTHORITY_CHANGED
```

Stop at the first mismatch so the receipt names the earliest leaking boundary rather than laundering downstream symptoms.

- [ ] **Step 3: Implement the one positive-control exception.**

A mismatch at the declared transform boundary is allowed only when `declared_transform.boundary == "NARRATIVE"`, `declared_transform.receipt_ref` is non-empty, and both side `receipt_refs` contain that exact reference. No other boundary may be waived.

- [ ] **Step 4: Preserve source inputs and receipt ancestry.**

Do not mutate `case`. Return the stable union of both sides' `receipt_refs` plus the transform receipt when applicable. Emit no authority/canon/publication/admission keys.

- [ ] **Step 5: Run focused tests.**

```bash
python -m unittest tests.test_projection_invariance -v
```

Expected: PASS.

- [ ] **Step 6: Run full regression suite.**

```bash
python -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 7: Commit implementation.**

```bash
git add alex_runtime/projection_invariance.py
git commit -m "feat: add projection invariance crucible"
```

---

### Task 3: Document the local conformance boundary

**Files:**
- Modify: `crucible/README.md`
- Test: `tests/test_crucible_readme.py` only if its existing contract requires an explicit marker.

**Interfaces:**
- Consumes: locally verified `PROJECTION-INVARIANCE-001` behavior.
- Produces: documentation stating what the specimen proves and explicitly what it does not prove.

- [ ] **Step 1: Add a compact `PROJECTION-INVARIANCE-001` section.**

State that ALEX compares already-formed observer-local witness digests, classifies the first hidden-state leak, permits only receipted narrative transforms, and grants no external authority.

- [ ] **Step 2: Run the full suite again.**

```bash
python -m unittest discover -s tests -v
```

Expected: all tests PASS.

- [ ] **Step 3: Commit documentation.**

```bash
git add crucible/README.md tests/test_crucible_readme.py
git commit -m "docs: receipt projection invariance crucible"
```

## Self-Review

- Spec coverage: core invariance, hostile projection leak, legal declared transform, no-authority control, leaking-boundary naming, and preserved failed fixtures are all assigned to tasks.
- Scope: no event-structure primitive, universal cut object, interpretation identity schema, edge-birth schema, aperture profile, or narrative-flow runtime is implemented.
- Type consistency: one public entry point only: `evaluate_projection_invariance_case(case: dict) -> dict`.
- Dependency check: Python standard library only.
