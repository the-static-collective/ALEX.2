# MEDIATED-SUPPORT-001 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add one pure ALEX evaluator that proves interest/selection may lawfully change support only through changed evidence, while any direct interest-to-support effect with the evidence basis held fixed is refused.

**Architecture:** `MEDIATED-SUPPORT-001` is a comparison wrapper over the existing `RELATION-DERIVATION-001` evaluator. It does not change Gate-2 support semantics, invent LOADOUT selection semantics, or duplicate 3rdi projection semantics. Each side supplies an already-attributable projection/context witness, interest/selection formation receipts, and an ordinary ALEX relation-derivation case; the wrapper evaluates both derivations, derives a semantic support signature and evidence-basis digest, then classifies the pair as direct-effect-zero, lawful mediation, semantic inflation, or insufficient to test.

**Tech Stack:** Python 3.12 standard library, `unittest`, immutable JSON fixtures, existing `alex_runtime.derivation.evaluate_relation_case`, existing `alex_runtime.digests.sha256_json`.

**Spec:** `docs/superpowers/specs/2026-08-28-mediated-support-counterfactual-rectangle-design.md`

## Global Constraints

- Implement `MEDIATED-SUPPORT-001` only. Do not implement `COUNTERFACTUAL-RECTANGLE-001` in this plan.
- Do not modify `RELATION-DERIVATION-001` semantics unless a failing hostile test proves the wrapper cannot express the contract compositionally.
- Do not import or reimplement LOADOUT or 3rdi kernels. Context, projection, selector, and consumption fields are attributable testimony consumed by ALEX, not ALEX-owned world semantics.
- `interest != evidence != support != authority` remains hard law.
- Selection/interest/consumption receipt references may survive as formation provenance but may not appear in the semantic support basis.
- A support difference is lawful only when the evaluated evidence basis differs and the change is attributable through a declared selector/consumption path.
- With the evaluated evidence basis fixed, a semantic support difference is `REFUSE / INTEREST_AS_SUPPORT`.
- Object-local evidence must not be weakened merely because interest guided discovery.
- Population/generalization comparison requires attributable selection formation; if it is stripped, return `INSUFFICIENT_TO_TEST / SELECTION_FORMATION_REQUIRED`. Do not build a statistical sampling engine.
- Result identity must preserve `case_id`, `claim_id`, projection/context identities, evidence-basis digests, support-result digests, formation receipt survivors, and reason/disposition.
- No result may emit canon, admission, publication, warrant, permission, or execution-authority state.
- Failed hostile controls remain committed alongside passing controls.
- Fixtures live under `tests/fixtures/mediated_support/`; do not expand the closed generic `crucible/specimens/` schema for this cross-run evaluator.

---

## File Structure

- Create `alex_runtime/mediated_support.py` — pure pair evaluator; the only new runtime module.
- Create `tests/fixtures/mediated_support/mediated-support-001.json` — stable neutral pair metadata for the direct-effect-zero control.
- Create `tests/test_mediated_support.py` — fixture materialization, hostile mutations, and all evaluator tests.
- Modify `crucible/README.md` — bounded conformance claim and explicit non-claims.
- Do not modify `alex_runtime/derivation.py`, `alex_runtime/projection_invariance.py`, or `alex_runtime/projection_break.py` in the first implementation.

The public interface is exactly:

```python
def evaluate_mediated_support_case(case: dict) -> dict[str, Any]:
    ...
```

The initial input shape is:

```python
{
    "case_id": "mediated-support-direct-zero",
    "claim_id": "C1",
    "claim_class": "OBJECT_LOCAL",  # or POPULATION_GENERALIZATION
    "left": {
        "projection_digest": "sha256:projection-shared",
        "bounded_context_digest": "sha256:context-shared",
        "interest_receipt_refs": [],
        "selection": {
            "policy_digest": "sha256:broad-policy-v1",
            "receipt_refs": ["selection:broad-left"],
            "consumed_interest_receipt_refs": [],
        },
        "derivation_case": {...},
    },
    "right": {
        "projection_digest": "sha256:projection-shared",
        "bounded_context_digest": "sha256:context-shared",
        "interest_receipt_refs": ["interest:q"],
        "selection": {
            "policy_digest": "sha256:broad-policy-v1",
            "receipt_refs": ["selection:broad-right"],
            "consumed_interest_receipt_refs": [],
        },
        "derivation_case": {...},
    },
}
```

The result preserves pair identity, per-side projection/context/evidence/support digests, `mediation_status`, `support_changed`, formation + Gate-2 receipt survivors, disposition, and reason code. Run-local evaluation/assertion identities are excluded from semantic support equality.

---

### Task 1: Freeze the neutral pair and first hostile contract

**Files:**
- Create: `tests/fixtures/mediated_support/mediated-support-001.json`
- Create: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: existing `relation-derivation-001-evidence-positive.json` through the Crucible blind-case builder.
- Produces: expected public callable `evaluate_mediated_support_case(case: dict) -> dict[str, Any]`.

- [x] **Step 1: Commit the neutral pair fixture.**
- [x] **Step 2: Write RED tests for fixed-evidence direct-effect zero, source immutability, malformed input, claim identity, and no-authority output.**
- [x] **Step 3: Verify RED on the full repository suite.**

Witness: GitHub Actions run `33213411950` / job `98991611410` left 107 existing tests green and failed only because `alex_runtime.mediated_support` did not yet exist.

---

### Task 2: Implement direct-effect zero and refuse semantic inflation

**Files:**
- Create: `alex_runtime/mediated_support.py`
- Modify: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: `evaluate_relation_case(case)` and canonical JSON digests.
- Produces: semantic support equality that ignores run-local occurrence IDs and a pair-level `DIRECT_EFFECT_ZERO` / `INTEREST_AS_SUPPORT` decision.

- [x] **Step 1: Implement the minimal pair evaluator for the neutral control.**
- [x] **Step 2: Verify the neutral pair GREEN on full CI.**
- [x] **Step 3: Add RED hostile control with an interest receipt inserted into Gate-2 proposal basis.**
- [x] **Step 4: Verify RED names the missing wrapper protection.**
- [x] **Step 5: Refuse any formation receipt that reaches Gate-2 semantic input basis.**
- [x] **Step 6: Re-run the full suite GREEN.**

Witness chain:
- neutral GREEN: run `33213461614`;
- hostile RED: run `33213499043`;
- semantic-inflation GREEN: run `33213545189`.

---

### Task 3: Distinguish lawful mediation from missing selection provenance

**Files:**
- Modify: `alex_runtime/mediated_support.py`
- Modify: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: attributable selector policy + receipt testimony, consumed-interest refs, bounded-context digest, and Gate-2 evidence basis.
- Produces: `LAWFUL_MEDIATION`, `SELECTION_FORMATION_REQUIRED`, and the object-local no-penalty control.

- [x] **Step 1: Add RED lawful-mediation test with consumed interest, changed bounded context, and changed genuine evidence basis.**
- [x] **Step 2: Add RED population-generalization test with stripped selection formation.**
- [x] **Step 3: Add object-local counter-control showing support is not weakened by absent selection history.**
- [x] **Step 4: Verify exactly the missing mediation/population cases fail while the object-local control passes.**
- [x] **Step 5: Implement attributable selection-formation checks and preserve formation survivors.**
- [x] **Step 6: Re-run full CI GREEN.**

RED witness: run `33213666128` ran 116 tests with exactly 2 failures and 114 passes: lawful mediation was not yet recognized and stripped population formation was still accepted. GREEN witness: run `33213734223` succeeded.

---

### Task 4: Harden semantic identity, Gate-2 comparability, and ancestry preservation

**Files:**
- Modify: `alex_runtime/mediated_support.py`
- Modify: `tests/test_mediated_support.py`

**Interfaces:**
- Consumes: nested Gate-2 disposition and `required_survivors`.
- Produces: strict pair identity, `DERIVATION_NOT_COMPARABLE`, semantic-digest immunity to run-local IDs, and unioned Gate-2 + formation ancestry.

- [x] **Step 1: Add RED blank `case_id` and `claim_id` identity tests.**
- [x] **Step 2: Add RED Gate-2-insufficient comparison test.**
- [x] **Step 3: Add RED survivor-union test.**
- [x] **Step 4: Add occurrence-ID metamorphic control.**
- [x] **Step 5: Verify RED produces four intended failures while occurrence-ID semantic equality already survives.**
- [x] **Step 6: Implement strict identity validation, Gate-2 comparability, and survivor union.**
- [x] **Step 7: Re-run full CI GREEN.**

RED witness: run `33213789361` ran 121 tests with exactly 4 failures and 117 passes. GREEN witness: run `33213856428` succeeded.

---

### Task 5: Document the bounded conformance claim and verify the whole branch

**Files:**
- Modify: `crucible/README.md`

**Interfaces:**
- Consumes: verified behavior of `MEDIATED-SUPPORT-001`.
- Produces: a durable statement of what the evaluator proves, what it refuses, and what remains HOLD.

- [x] **Step 1: Document `MEDIATED-SUPPORT-001` without claiming general runtime conformance.**
- [x] **Step 2: State explicitly that `COUNTERFACTUAL-RECTANGLE-001` remains unimplemented.**
- [x] **Step 3: Run the full repository test suite on the documentation head.**
- [x] **Step 4: Confirm the repository search-absence guard still passes.**

Final witness: GitHub Actions run `33213911646` / job `98993174692` executed `python -m unittest discover -s tests -v` and reported:

```text
Ran 121 tests in 1.141s

OK
PASS search-absence
```

## Self-Review

- Spec coverage: direct-effect-zero, semantic-inflation refusal, lawful mediation, population-selection provenance, object-local no-penalty, strict identity, Gate-2 comparability, ancestry preservation, immutability, and no-authority output are all exercised.
- Scope: no `COUNTERFACTUAL-RECTANGLE-001` runtime, policy-equivalence kernel, adaptive epistemic topology, statistical sampling engine, LOADOUT kernel, or 3rdi kernel was added.
- Existing Gate-2 semantics remain untouched; `alex_runtime/derivation.py` was not modified.
- Type consistency: one new public entry point only — `evaluate_mediated_support_case(case: dict) -> dict[str, Any]`.
- Dependency check: Python standard library + existing ALEX modules only.
- Final verification: 121 tests, 0 failures, fresh CI run `33213911646`.
