# NAME Six-Specimen Gate 001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a deterministic ALEX packet evaluator and six-specimen dive gate that can distinguish READY, BLOCKED, and malformed research packets without evaluating the underlying hypothesis.

**Architecture:** Create one standard-library module, `alex_runtime/name_specimen_gate.py`, with two pure evaluators: `evaluate_name_specimen_packet(record)` and `evaluate_name_six_specimen_gate(record)`. Packet evaluation validates attributable occurrence references and preserves a first-class `BLOCKED` state for missing material evidence; family evaluation requires exactly one of each fixed specimen type and returns `DIVE_READY` only when all packet receipts are READY.

**Tech Stack:** Python 3.12 standard library, `unittest`, existing `alex_runtime.digests.sha256_json`.

**Spec:** `docs/superpowers/specs/2026-08-29-name-six-specimen-gate-001-design.md`

## Global Constraints

- Standard library only.
- Packet completeness is not historical or theological truth.
- `BLOCKED` is distinct from `REFUSE` and from disproval.
- `NOMEN_SACRUM` requires an explicit material-witness occurrence reference.
- Explicit answer-bearing fields are forbidden.
- Every output freezes `authority` to `none`.

---

### Task 1: RED — packet evaluator contract

**Files:**
- Create: `tests/test_name_specimen_gate.py`

**Interfaces:**
- Produces expected API: `evaluate_name_specimen_packet(record: object) -> dict`.

- [ ] **Step 1: Write failing packet tests**

Create tests for: ordinary text-first READY; nomen-sacrum BLOCKED without material witness; nomen-sacrum READY with material witness; malformed ref refusal; duplicate transform/receipt ref refusal; forbidden answer field refusal; authority freeze; deterministic digest under key reorder.

- [ ] **Step 2: Verify RED**

Run:

```bash
python -m unittest tests.test_name_specimen_gate -v
```

Expected: import failure because `alex_runtime.name_specimen_gate` does not yet exist.

- [ ] **Step 3: Commit RED tests**

```bash
git add tests/test_name_specimen_gate.py
git commit -m "test: define NAME specimen packet gate"
```

### Task 2: GREEN — packet evaluator

**Files:**
- Create: `alex_runtime/name_specimen_gate.py`

**Interfaces:**
- Consumes: `sha256_json(value: dict) -> str`.
- Produces: `evaluate_name_specimen_packet(record: object) -> dict`.

- [ ] **Step 1: Implement minimal packet validation**

Implement exact schema, fixed specimen vocabulary, SHA validation, unique transform/receipt refs, forbidden-answer scan, material-witness requirement for `NOMEN_SACRUM`, deterministic packet digest, and frozen authority.

- [ ] **Step 2: Verify focused GREEN**

Run:

```bash
python -m unittest tests.test_name_specimen_gate -v
```

Expected: packet tests pass.

- [ ] **Step 3: Commit implementation**

```bash
git add alex_runtime/name_specimen_gate.py
git commit -m "feat: add NAME specimen packet evaluator"
```

### Task 3: RED/GREEN — six-specimen family gate

**Files:**
- Modify: `tests/test_name_specimen_gate.py`
- Modify: `alex_runtime/name_specimen_gate.py`

**Interfaces:**
- Produces: `evaluate_name_six_specimen_gate(record: object) -> dict`.

- [ ] **Step 1: Add failing family tests**

Add tests for: one blocked nomen-sacrum produces `DIVE_BLOCKED` naming `NOMEN_SACRUM`; six READY packets produce `DIVE_READY`; missing specimen refuses; duplicate specimen refuses; packet-level REFUSE causes family REFUSE; authority remains none.

- [ ] **Step 2: Verify RED**

Run the focused suite and confirm failure because `evaluate_name_six_specimen_gate` is absent.

- [ ] **Step 3: Implement the minimal family evaluator**

Validate exact six-type coverage from packet-evaluation receipts and map dispositions to `DIVE_READY`, `DIVE_BLOCKED`, or `REFUSE` without inspecting hypothesis content.

- [ ] **Step 4: Verify GREEN and whole floor**

Run:

```bash
python -m unittest tests.test_name_specimen_gate -v
python -m unittest discover -s tests -v
```

Expected: all tests pass.

- [ ] **Step 5: Commit**

```bash
git add tests/test_name_specimen_gate.py alex_runtime/name_specimen_gate.py
git commit -m "feat: add six-specimen dive gate"
```

### Task 4: Owner review gate

**Files:**
- Modify only when a concrete correctness hole is found.

- [ ] Inspect the full diff for answer smuggling, status collapse, fake material completion, occurrence/carrier identity collapse, and authority leakage.
- [ ] If a hole exists, add a failing hostile test before correction.
- [ ] Run the focused and full suite after any correction.
- [ ] Preserve any material review correction in a durable amendment file.
