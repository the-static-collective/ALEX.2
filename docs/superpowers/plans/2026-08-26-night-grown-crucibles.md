# Night-Grown Crucibles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Plant four machine-readable ALEX Crucible specimens that preserve MADDCLOWN discovery freedom while refusing silent promotion into evidence, consensus, invariance, or independent recurrence.

**Architecture:** Extend only the portable Crucible fixture corpus. Do not add runtime behavior or a new ontology. Each specimen must fit the existing `crucible_specimen` contract and preserve residue required to explain the refusal or accepted descendant.

**Tech Stack:** JSON fixtures, Python `unittest`, existing ALEX Crucible harness.

**Spec:** `docs/superpowers/specs/2026-08-26-alex-constitutional-hardening-design.md`

## Global Constraints

- `discovery path != evidence path`
- `breadcrumb != evidence`
- `agreement != independent corroboration`
- `apparent multiplicity != independent ancestry`
- `replay success != dependency robustness`
- A crazy hypothesis earns promotion by surviving loss, not by accumulating resemblance.
- Do not claim ALEX runtime conformance.

---

### Task 1: Lock the new fixture corpus in a failing contract test

**Files:**
- Modify: `tests/test_crucible_contract.py`

- [ ] Add these required fixture names to `expected_names`: `attention-trace-support-independence.json`, `bounded-suspension.json`, `pressure-loss-survivor.json`, `creative-recurrence-independence.json`.
- [ ] Run the contract test and confirm RED because the four fixtures do not yet exist.

### Task 2: Add attention-trace and suspension specimens

**Files:**
- Create: `crucible/specimens/attention-trace-support-independence.json`
- Create: `crucible/specimens/bounded-suspension.json`

- [ ] Encode breadcrumb → query → evidence while refusing breadcrumb-as-support.
- [ ] Encode three unequal suspended hypotheses where one is killed without forcing consensus or equal confidence among survivors.
- [ ] Run the contract suite and confirm the remaining missing fixtures still keep it RED.

### Task 3: Add PRESSURE-loss and creative-recurrence specimens

**Files:**
- Create: `crucible/specimens/pressure-loss-survivor.json`
- Create: `crucible/specimens/creative-recurrence-independence.json`
- Modify: `crucible/README.md`

- [ ] Encode a positive PRESSURE descendant that survives declared losses while preserving what was removed and forbidding promotion of the fat parent.
- [ ] Encode a recurrence set that collapses into dependency families and refuses raw appearance count as independent-birth count.
- [ ] Document the new fixture family without claiming runtime conformance.
- [ ] Run `python -m unittest discover -s tests -v` and require GREEN.

### Task 4: Open a bounded PR

- [ ] Compare branch to `main`.
- [ ] Open a PR describing the four specimens and the explicit decision to leave seed–key and causal-debt tests outside ALEX ownership.
- [ ] Inspect the `crucible-contract` workflow result before claiming the branch proven.
