# ALEXDEEPDIVE — RULE-DOMAIN-NOT-RETAINED-DISTINCTION-001

**Status:** RESEARCH  
**Promotion:** none

## Ground
- Question: What is the strongest live ALEX research frontier newly exposed since the previous ALEXDEEPDIVE packet?
- Desired consequence: one bounded, replayable discriminator; no runtime or canon promotion.
- Stop condition: identify the smallest consequential ambiguity in the new retrospective-information-floor control and state a hostile test that can distinguish the live readings.
- Corpus: ALEX.2 current main plus PR #107 exact head `707f2f7ca106e8864b1fa156ba36017fb59ceac6`; no adjacent repo was needed.
- Authority/effect boundary: research only; authority none.
- Task shape: AUDIT.
- Formation trace active: no.

## Orientation and world cut
GitBook Front Room orientation was attempted first. Organization discovery was blocked by the connector safety boundary before content retrieval. This is access fog, not evidence of absence.

Required governance was then read before consequential claims:
- `AGENTS.md`
- `skills/alex/SKILL.md`
- `skills/alex/references/research-receipt.md`

Pre-write `main` was `0614e2173bc2fe0fe2ddea3926ce39b60d805873`. Its three newest commits since the previous substantive packet were ALEXDEEPDIVE no-material-delta receipts, so they were not treated as semantic implementation deltas.

The material change is PR #107 advancing from the previously inspected `33d53f44954eb9d78fa81dcb383a378bff46979b` to `707f2f7ca106e8864b1fa156ba36017fb59ceac6`. The compare reports five commits ahead. The exact head adds `tests/test_retrospective_information_floor.py`; the inspected implementation is `experiments/retrospective_information_floor.py` at that exact head.

## Finding
The new control correctly freezes an important information law:

```text
LATER RULE != RESURRECTION OF ERASED DISTINCTION
```

But its implementation exposes a narrower unresolved boundary. When more than one `source_candidate` remains, it sets:

```python
source_value = None
derived_value = later_rule.get(str(retained_value))
status = "DISTINCTION_UNRECOVERABLE_FROM_RETAINED_CARRIER"
```

That means the same `later_rule` object is implicitly allowed to address either:
1. original/source distinctions such as `a -> P`, `b -> Q`; or
2. a collapsed retained-carrier value such as `X -> R`.

Those are different domains. A lawful later rule over the retained carrier does not resurrect `a` or `b`; it derives from `X`. Conversely, a rule whose domain is the erased source alphabet cannot lawfully infer which erased source produced `X`.

Therefore the live boundary is:

```text
RULE DOMAIN != RETAINED CARRIER DOMAIN
DERIVATION FROM X != RESURRECTION OF a OR b
UNRECOVERABLE SOURCE DISTINCTION != NO POSSIBLE LATER DERIVATION
```

## Evidence path
1. PR #107 exact head `707f2f7ca106e8864b1fa156ba36017fb59ceac6` adds the hostile test `test_collapsed_carrier_does_not_resurrect_a_or_b` with retained value `X`, candidates `(a,b)`, and later rule `{a:P,b:Q}`. It expects status `DISTINCTION_UNRECOVERABLE_FROM_RETAINED_CARRIER` and `derived_value is None`.
2. The exact-head implementation computes `derived_value` from `later_rule[str(retained_value)]` in the non-unique branch.
3. Therefore adding `X:R` to the later rule would produce `derived_value=R` while retaining the status `DISTINCTION_UNRECOVERABLE_FROM_RETAINED_CARRIER`.

No external scholarship is required to establish this executable ambiguity; it follows directly from the inspected code and fixture. No Wolfram computation is material.

## Claim ledger
| ID | Claim | Class | Support | Counterevidence / alternative | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #107 has materially advanced beyond the previously inspected head. | observed | GitHub compare `33d53f4...707f2f7` | none observed | supported |
| C2 | The new test explicitly protects against resurrecting erased `a/b` distinction. | observed | exact-head test file | none | supported |
| C3 | In the non-unique branch, the implementation still queries the later rule with the retained collapsed value. | observed | exact-head implementation | none | supported |
| C4 | This creates an unresolved rule-domain ambiguity, not necessarily a defect. | inference | C2 + C3 | the experiment may intentionally permit rules over both domains | live |
| C5 | A later rule over `X` can be lawful without recovering whether the source was `a` or `b`. | inference | domain separation | requires explicit contract to become project semantics | live |

## Competing readings
### Reading A — source-domain-only rule
`later_rule` is meant to map original distinctions only. Then the non-unique branch should not query it with `retained_value`; `derived_value` should remain `None` and the current status is sufficient.

### Reading B — retained-carrier rule permitted
A later rule may legitimately map the retained value `X`. Then `X -> R` is a new derivation from retained information, not resurrection of erased source identity. The current status alone is too coarse because it conflates `source distinction unrecoverable` with `no later derivation available`.

### Reading C — mixed domain by convention
The rule may intentionally contain both source and carrier keys. This is possible in the current code but currently has no explicit domain declaration, making replay interpretation depend on implicit key meaning.

## Direct counterexample
Freeze:

```python
retained = {
    "receipt_id": "receipt:t0-collapsed",
    "value": "X",
    "source_candidates": ("a", "b"),
}
later_rule = {"a": "P", "b": "Q", "X": "R"}
```

Current code can return both:

```text
status = DISTINCTION_UNRECOVERABLE_FROM_RETAINED_CARRIER
derived_value = R
```

Those statements are not logically contradictory if `R` is explicitly a derivation from `X`. They are semantically ambiguous because the receipt does not say which domain the rule inhabits or what `derived_value` is derived from in this branch.

## Nearest boring explanation
The function is a deliberately tiny experiment. `later_rule.get(str(retained_value))` may simply be convenience code intended to demonstrate that only actually retained information can be used. If so, the correct move is not a general type system; it is one explicit rule-domain field or one narrower refusal/branch contract.

## Rights / egress
Only repository text and metadata were inspected. No source corpus, private research material, or external page bytes were exported. GitBook content was not retrieved. No adjacent repository traversal was needed.

## Residual fog
- The intended semantic domain of `later_rule` is not explicit in the inspected function signature.
- It is unresolved whether the branch should support lawful transformation of collapsed retained values or only source-distinction reinterpretation.
- Full PR CI state was not needed to establish this code-level ambiguity and is not claimed here.

## Smallest next discriminators
1. **RULE-DOMAIN-CONTROL-001:** run the exact collapsed specimen with `{a:P,b:Q,X:R}` and require the receipt to distinguish `source_distinction_recoverable=false` from a lawful `derived_from_retained_value=X -> R`, or explicitly refuse mixed/undeclared rule domains.
2. If rules are source-domain-only by design, remove/forbid the collapsed-value lookup in the non-unique branch and freeze that narrower contract.
3. If both domains are needed, add only the smallest explicit domain declaration (`source` vs `retained_carrier`) before considering any generalized transformation machinery.

## Receipt
- Created: 2026-09-19 23:25 America/Chicago
- Researcher/agent: ALEXDEEPDIVE
- Tool/model boundary: GitBook connector for orientation attempt; GitHub connector for exact repository/PR evidence; no Wolfram or external scholarship used because not material.
- Discovery trace: PR recency selected the door; it is not evidence for the finding.
- Evidence path: exact PR head -> exact test -> exact implementation -> hostile mixed-domain specimen.
- External byte egress: none beyond connected repository/API reads.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-19-2325-RULE-DOMAIN-NOT-RETAINED-DISTINCTION.md`
- Promotion: none
