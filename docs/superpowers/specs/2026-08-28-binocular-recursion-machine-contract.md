# BINOCULAR-RECURSION-001 — Machine Contract Appendix

**Date:** 2026-08-28  
**Status:** NORMATIVE APPENDIX TO `2026-08-28-binocular-recursion-design.md`  
**Implementation:** NOT YET ADMITTED

## 0. Why this appendix exists

The conceptual design states that discovery triggers must never become support and that expansion may not inject undeclared premises. Those laws must be machine-checkable rather than aspirational.

This appendix pins the minimum auditable envelope for the first evaluator.

Where a conceptual example in the parent design omits a field listed here, this appendix is authoritative for the first executable contract.

---

## 1. Public evaluator

```python
def evaluate_binocular_recursion_case(case: dict) -> dict[str, object]:
    ...
```

The evaluator audits a supplied formation trace. It does not generate compression proposals, perform open-ended consequence search, interpret prose, or decide whether a researched claim is true.

---

## 2. Required top-level envelope

```json
{
  "schema": "alex.binocular-recursion-case/v0",
  "case_id": "specimen-001",
  "initial_field_digest": "sha256:...",
  "authority_digest": "sha256:...",
  "admitted_premise_refs": ["p1", "p2"],
  "unresolved_premise_refs": ["u1"],
  "discovery_trigger_refs": ["trigger:prompt-001"],
  "support_refs": ["source:r1", "source:r2"],
  "passes": [],
  "terminal": "RESIDUAL"
}
```

Required terminal values:

```text
FIXED
CYCLE
RESIDUAL
DIVERGENT
```

`REFUSE` and `INSUFFICIENT_TO_TEST` are evaluator dispositions, not user-supplied successful terminal claims.

The following sets are semantically distinct:

```text
admitted_premise_refs
unresolved_premise_refs
discovery_trigger_refs
support_refs
```

The evaluator must never union them for convenience.

---

## 3. Pass envelope

Each pass must contain:

```json
{
  "pass_index": 0,
  "pre_field_digest": "sha256:...",
  "trajectory": ["A", "B", "A", "C"],
  "trajectory_order_material": true,
  "compression": {},
  "expansion": {},
  "tensions": [],
  "update": {},
  "post_field_digest": "sha256:..."
}
```

`pass_index` values must begin at zero and increase contiguously by one.

For pass `n > 0`:

```text
passes[n].pre_field_digest == passes[n-1].post_field_digest
```

Otherwise return:

```text
REFUSE / BROKEN_PASS_ANCESTRY
```

For pass zero:

```text
passes[0].pre_field_digest == initial_field_digest
```

---

## 4. Compression envelope

```json
{
  "proposal_digest": "sha256:...",
  "formation_basis_refs": ["p1", "p2"],
  "claim_support_refs": ["source:r1"],
  "reexpanded_live_consequence_refs": ["c1", "c2"]
}
```

Meanings:

- `formation_basis_refs` identifies the admitted/referenced material from which the compression proposal was formed;
- `claim_support_refs` identifies material asserted to support any external claim carried by the compression proposal;
- `reexpanded_live_consequence_refs` is the consequence set the supplied compression candidate can regenerate under the separately declared expansion profile.

Hard validation:

```text
claim_support_refs ∩ discovery_trigger_refs == ∅
```

Violation:

```text
REFUSE / DISCOVERY_TRIGGER_AS_SUPPORT
```

A formation basis may include a discovery trigger only when its role remains explicitly formation-only and the same ref is absent from `claim_support_refs`.

The evaluator does not itself judge whether remaining `claim_support_refs` are evidentially sufficient; that belongs to ALEX evidence-path machinery outside this operator.

---

## 5. Expansion envelope

```json
{
  "profile_digest": "sha256:...",
  "branches": [
    {
      "branch_id": "b1",
      "parent_refs": ["p1"],
      "rule_ref": "rule:r1",
      "condition_refs": [],
      "consequence_ref": "c1",
      "status": "INFERRED",
      "used_premise_refs": ["p1"],
      "introduced_premise_refs": []
    }
  ]
}
```

Allowed branch statuses:

```text
ENTAILED
INFERRED
SPECULATIVE
CONTRADICTED
UNRESOLVED
```

For every branch:

```text
used_premise_refs ⊆ admitted_premise_refs ∪ introduced_premise_refs
```

Every `introduced_premise_ref` must be explicitly marked as introduced in that branch. It does not become admitted globally inside the same pass.

If a branch uses a premise outside those sets:

```text
REFUSE / UNDECLARED_PREMISE_INJECTION
```

`SPECULATIVE` is a valid branch status. It is not an admitted premise and not support.

---

## 6. Live consequence surface

The pass must make the expansion surface explicit enough to test compression loss.

Define:

```text
live_consequence_refs = {
  consequence_ref(branch)
  for branch in expansion.branches
  if branch.status in {ENTAILED, INFERRED, UNRESOLVED}
}
```

`SPECULATIVE` branches remain visible but do not enter this minimum live-consequence loss check.

`CONTRADICTED` branches remain visible as contradictions but do not count as consequences the compression must regenerate.

Required invariant unless an explicit withdrawal/refutation receipt exists in the update:

```text
live_consequence_refs ⊆ compression.reexpanded_live_consequence_refs
```

Violation:

```text
REFUSE / COMPRESSION_ERASED_LIVE_CONSEQUENCE
```

This test checks only that the supplied compression trace did not silently omit a live branch. It does not certify the compression as correct or minimal.

---

## 7. Tension envelope

```json
{
  "type": "MISSING_CONSEQUENCE",
  "left_refs": ["proposal:cp1"],
  "right_refs": ["c2"],
  "receipt_refs": ["receipt:x1"]
}
```

Allowed first-version tension types:

```text
MISSING_CONSEQUENCE
SURPLUS_GENERATOR
UNEXPLAINED_RESIDUAL
BRANCH_DEPENDENCE
CONTRADICTION
TRAJECTORY_DEPENDENCE
STABLE_MATCH
```

The evaluator validates the vocabulary and receipt shape. It does not infer the correct tension type from arbitrary prose.

Unknown types:

```text
INSUFFICIENT_TO_TEST / UNKNOWN_TENSION_TYPE
```

---

## 8. Ordered traversal validation

If:

```text
trajectory_order_material == true
```

then `trajectory` must contain at least two non-empty refs and preserve order exactly as supplied.

An empty trajectory or a replacement field containing only unordered membership is insufficient:

```text
INSUFFICIENT_TO_TEST / TRAJECTORY_NOT_PRESERVED
```

The evaluator must not sort or deduplicate a valid trajectory.

Repeated positions are legal:

```text
["A", "B", "A", "C"]
```

is materially different from:

```text
["A", "A", "B", "C"]
```

when the specimen claims path dependence.

---

## 9. Update envelope

```json
{
  "kind": "NONE",
  "receipt_refs": [],
  "admit_premise_refs": [],
  "withdraw_premise_refs": [],
  "withdraw_consequence_refs": [],
  "authority_digest": "sha256:..."
}
```

Allowed first-version `kind` values:

```text
NONE
EVIDENCE_ADDED
PREMISE_ADMITTED
PREMISE_WITHDRAWN
READING_CORRECTED
RULE_PROFILE_CHANGED
CONTRADICTION_RESOLVED
OWNER_DECISION
```

If `pre_field_digest != post_field_digest` while `kind == NONE` or no receipt survives:

```text
REFUSE / UNATTRIBUTED_UPDATE
```

If any pass update carries an authority digest different from the case-level `authority_digest`:

```text
REFUSE / AUTHORITY_CHANGED
```

The binocular operator itself never mints authority.

---

## 10. One-eye collapse

Both `compression` and `expansion` must be present and valid in every claimed binocular pass.

If one is missing:

```text
INSUFFICIENT_TO_TEST / ONE_EYE_COLLAPSE
```

A compression-only or expansion-only research operation may still be useful; it simply is not a valid `BINOCULAR-RECURSION-001` specimen.

---

## 11. Terminal validation

### FIXED

Requires at least two passes and equality of canonical binocular-state digests for the last two passes under unchanged compression/expansion profile digests.

No truth promotion follows.

### CYCLE

Requires a repeated canonical binocular-state digest with at least one distinct intervening state.

### RESIDUAL

Requires at least one non-`STABLE_MATCH` tension in the final pass and no constitutional refusal.

### DIVERGENT

Requires a declared bounded pass limit, no repeated binocular-state digest inside the observed run, and a non-empty material tension delta on the final transition.

If the supplied terminal label is not supported by its structural conditions:

```text
INSUFFICIENT_TO_TEST / TERMINAL_NOT_DEMONSTRATED
```

---

## 12. Result envelope

```json
{
  "schema": "alex.binocular-recursion-result/v0",
  "case_id": "specimen-001",
  "disposition": "ACCEPT",
  "reason_code": null,
  "terminal": "RESIDUAL",
  "validated_passes": 2,
  "tension_types": ["MISSING_CONSEQUENCE"],
  "receipt_survivors": ["receipt:x1", "source:r1"],
  "authority_digest": "sha256:..."
}
```

Allowed dispositions:

```text
ACCEPT
REFUSE
INSUFFICIENT_TO_TEST
```

Again:

```text
ACCEPT == formation contract satisfied
ACCEPT != researched claim accepted as true
```

---

## 13. Minimum hostile test matrix

| Case | Expected |
|---|---|
| lawful dual-layer residual | `ACCEPT / RESIDUAL` |
| discovery trigger included in claim support | `REFUSE / DISCOVERY_TRIGGER_AS_SUPPORT` |
| undeclared premise consumed by expansion | `REFUSE / UNDECLARED_PREMISE_INJECTION` |
| live consequence omitted by compression re-expansion | `REFUSE / COMPRESSION_ERASED_LIVE_CONSEQUENCE` |
| compression missing | `INSUFFICIENT_TO_TEST / ONE_EYE_COLLAPSE` |
| order material but trajectory missing | `INSUFFICIENT_TO_TEST / TRAJECTORY_NOT_PRESERVED` |
| field changes without update receipt | `REFUSE / UNATTRIBUTED_UPDATE` |
| authority digest changes | `REFUSE / AUTHORITY_CHANGED` |
| fixed point structurally demonstrated | `ACCEPT / FIXED` |
| cycle structurally demonstrated | `ACCEPT / CYCLE` |
| divergent label without bounded evidence | `INSUFFICIENT_TO_TEST / TERMINAL_NOT_DEMONSTRATED` |

---

## 14. Non-collapse summary

```text
discovery_trigger_refs != claim_support_refs
formation_basis_refs != claim_support_refs
introduced_premise_refs != admitted_premise_refs
trajectory != focus membership
compression re-expansion match != truth
terminal stability != truth
ACCEPT != claim acceptance
authority before == authority after
```
