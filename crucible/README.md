# ALEX Crucible

ALEX Crucible is a portable constitutional fixture contract. It is not the ALEX research runtime and does not select a production implementation language.

## Adapter protocol

```text
stdin  -> one complete specimen JSON object
stdout -> one complete result JSON object
exit 0 -> adapter produced a parseable attempted result
nonzero -> adapter could not execute the specimen
```

Exit `0` is not conformance. The reference harness still compares the attempted result against the specimen's required disposition, refusal code, required receipt survivors, and forbidden promotions.

A refusal is incomplete if it discards the evidence or residue the specimen says must survive. A result also fails if it performs a forbidden promotion even when its headline disposition looks correct.

## Night-grown fixture family

The August 26 MADDCLOWN pass adds four bounded attacks without expanding ALEX into a master ontology:

- `attention-trace-support-independence` — a breadcrumb may cause a search without carrying support weight;
- `bounded-suspension` — evidence may kill one live hypothesis without forcing consensus or equal confidence among the survivors;
- `pressure-loss-survivor` — a narrower descendant may be accepted when it survives declared losses with counterexamples and boring explanations preserved;
- `creative-recurrence-independence` — raw recurrence count cannot impersonate independent-birth count when dependency families, shared pressure, or unknown ancestry remain.

These fixtures sharpen one shared failure mode: **no relation is promoted merely because an adjacent relation is true**. Discovery may cause attention without becoming evidence; recurrence may be real without proving independent invention; survival under loss may justify a narrower descendant without promoting its parent.

Seed–key separation and causal-debt admission are deliberately not encoded here as ALEX-owned laws. They remain cross-project frontier specimens until an owning runtime or explicitly shared constitutional layer earns executable semantics for them.

## Conformance boundary

Passing `crucible-contract` proves the fixture corpus and reference harness are internally consistent. It does not prove an ALEX runtime conforms. Runtime conformance begins only when a real adapter executes the applicable fixtures and the harness reports zero constitutional mismatches.

The fake adapters under `tests/fixtures/` exist only to test the harness. The expected-result adapter is not an ALEX implementation and must never be cited as runtime conformance evidence.
