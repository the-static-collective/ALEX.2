# ALEX Crucible

ALEX Crucible is a portable constitutional fixture contract. It is not the ALEX research runtime and does not select a production implementation language.

> **CRUCIBLE RUNTIME CONFORMANCE IS NOT YET CLAIMED.**

## Blind adapter boundary

A canonical specimen may contain its expected outcome because it is an authoring and historical artifact. Before process execution, the harness lowers that specimen into two separate objects:

- **CASE** — runtime-visible input;
- **ORACLE** — harness-only expectation used after execution for scoring.

The adapter receives **CASE only**. ORACLE remains harness-only and is never written to adapter stdin.

This means canonical fixtures can preserve their historical `expected` blocks without exposing those answers through the process boundary. The CASE carries the bounded operation input plus `case_id`, `operation_type`, `rule_profile`, `nonce`, and `input_digest`. A runtime result must return the matching case/input/ruleset identities, evaluator disposition, receipt survivors, derived assertions, and a separate execution-state summary.

Metamorphic sibling cases provide **metamorphic, not secret** pressure. This is an open repository: siblings may vary identifiers, nonces, irrelevant relation ordering, and explicitly declared distractors, but no cryptographic hiddenness is claimed. Their purpose is to expose brittle surface memorization and answer-key dependence, not to pretend the fixture corpus is unknowable.

## Adapter protocol

```text
stdin  -> one complete CASE JSON object
stdout -> one complete runtime-result JSON object
exit 0 -> adapter produced a parseable attempted result
nonzero -> adapter could not execute the CASE
```

Exit `0` is not conformance. The reference harness first verifies result identity and shape, then compares the attempted result against the harness-only ORACLE: required disposition, reason code, required receipt survivors, and forbidden derived outputs.

A refusal is incomplete if it discards the evidence or residue the specimen says must survive. A result also fails if it produces a forbidden derived output even when its headline disposition looks correct.

Evaluator disposition and execution state are separate axes. `ACCEPT` does not mean externally admitted, and an `ERRORED` execution state is not a `REFUSE` disposition.

## Night-grown fixture family

The August 26 MADDCLOWN pass adds four bounded attacks without expanding ALEX into a master ontology:

- `attention-trace-support-independence` — a breadcrumb may cause a search without carrying support weight;
- `bounded-suspension` — evidence may kill one live hypothesis without forcing consensus or equal confidence among the survivors;
- `pressure-loss-survivor` — a narrower descendant may be accepted when it survives declared losses with counterexamples and boring explanations preserved;
- `creative-recurrence-independence` — raw recurrence count cannot impersonate independent-birth count when dependency families, shared pressure, or unknown ancestry remain.

These fixtures sharpen one shared failure mode: **no relation is promoted merely because an adjacent relation is true**. Discovery may cause attention without becoming evidence; recurrence may be real without proving independent invention; survival under loss may justify a narrower descendant without promoting its parent.

Seed–key separation and causal-debt admission are deliberately not encoded here as ALEX-owned laws. They remain cross-project frontier specimens until an owning runtime or explicitly shared constitutional layer earns executable semantics for them.

## Scoped derivation profile

`alex.runtime/derivation-m0` is the first executable semantic profile. It is intentionally tiny: its only semantic predicate is `SUPPORTS`, evaluated by `RELATION-DERIVATION-001@1` through the real `tools/derivation_adapter.py@1` CASE-only process boundary.

The profile runs both the explicit attention-negative descendant and the attributable-evidence positive sibling, then reruns each as a metamorphic sibling with a fresh case identity and nonce, reversed irrelevant relation ordering, and an unrelated witnessed distractor relation. The historical `attention-trace-support-independence` specimen remains an unchanged ancestor rather than being rewritten into the runtime shape.

A clean `alex.runtime/derivation-m0` run testifies only that the exact tested runtime build, ruleset digest, adapter version, fixture-family version, and metamorphic pressure survived that scoped profile. It does **not** establish general ALEX runtime conformance, historical truth, source authority, canon, permission, external admission, publication, merge authority, or any other owning-world consequence. `alex.runtime/one-book-m1` and `alex.runtime/formation-trace-m2` remain explicitly outside this profile.

## Scoped LOADOUT handshake profile

`alex.runtime/loadout-handshake-m0` is the ALEX-side receiving boundary for a LOADOUT-issued `loadout.compile/v0` plus its bound `alex.run-envelope/v0`. ALEX validates testimony about the compile; it does not become the LOADOUT compiler and does not enlarge the carried fence.

The profile proves only the following scoped mechanics: exact compile/envelope binding, compile expiry, owner-evidence-digest drift detection, required-capability gaps, current attributable effect-fence membership, and non-inheritance of parent permission by a child compile. Five original specimens are each rerun with a fresh metamorphic sibling whose compile, trace, fence, run identity, nonce, and compile digest differ while the constitutional condition remains the same.

`ACCEPT` in this profile means only that the bounded run request may enter ALEX under that exact compile and fence testimony. It does **not** mean truth, source authority, canon, permission beyond the carried fence, publication, deployment, external admission, merge authority, or owning-world consequence. It also does not claim `alex.runtime/one-book-m1` or `alex.runtime/formation-trace-m2` conformance.

## Conformance boundary

Passing `crucible-contract` proves the fixture corpus and reference harness are internally consistent. It does not prove an ALEX runtime conforms. Runtime conformance begins only when a real adapter executes the applicable fixtures and the harness reports zero constitutional mismatches.

The fake adapters under `tests/fixtures/` exist only to test the harness. They are not ALEX implementations and must never be cited as runtime conformance evidence. The answer-echo and identity-switch fixtures are deliberately adversarial harness tests: their failure demonstrates that the harness refuses those cheating strategies, not that a production research runtime is correct.
