# ALEXDEEPDIVE — GRAMMAR-ID-NOT-SEMANTICS-001

**Status:** RESEARCH  
**Promotion:** none  
**Shape:** AUDIT  
**Created:** 2026-09-02 23:22 America/Chicago

## Finding

The newest `ELIGIBILITY-INDEPENDENCE-001` work successfully separates **matrix representability** from **grammar admissibility**, but the new tiny-grammar evaluator exposes a narrower attribution boundary:

```text
GRAMMAR LABEL != GRAMMAR SEMANTICS
```

At PR #92 head `ba0c9a975c98dd2938ce3f693cb029466f462946`, `audit_tiny_grammar_row(row, *, grammar_id)` applies one hard-coded invariant regardless of the supplied `grammar_id`, then copies that caller-supplied identifier into the result.

Therefore the current result can truthfully witness:

```text
this row was evaluated by this fixed tiny-grammar function
```

but it cannot, from `grammar_id` alone, witness:

```text
this row was evaluated under the grammar whose semantics are identified by grammar_id
```

The distinction matters only if `grammar_id` is later treated as provenance for a policy/grammar definition. PR #92 remains experimental and non-canonical, so this is a cheap boundary to freeze now rather than a claim of runtime vulnerability.

## Ground

- **Question:** Does the newly added tiny-grammar discriminator bind its returned grammar identity to the semantics actually evaluated?
- **Desired consequence:** Prevent a useful local experiment from quietly teaching later consumers that a caller-provided grammar label proves which grammar semantics produced the result.
- **Stop condition:** Establish whether changing only `grammar_id` can change the evaluated invariant, and identify the smallest adequate correction if not.
- **Corpus/date:** `the-static-collective/ALEX.2`, current `main` and open PR #92 as encountered during this run; current primary OPA documentation used only as an external architecture comparison.
- **Authority/effect boundary:** Research receipt only. No runtime, schema, merge, policy, authorization, or canon promotion.
- **Formation trace:** yes, kept separate below.

## World cut

### Included

- `ALEX.2/AGENTS.md` on current main.
- `skills/alex/SKILL.md` on current main.
- `skills/alex/references/research-receipt.md` on current main.
- Current `main@db761bd974a3ab21b4bc8da7a8451aea24779e94`.
- Open draft PR #92, `agent/crater-eligibility-independence-001@ba0c9a975c98dd2938ce3f693cb029466f462946`.
- PR #92 changed files, especially `experiments/eligibility_independence.py` and `tests/test_eligibility_independence_experiment.py`.
- Open Policy Agent primary documentation on decision logs and bundles, strictly as an external comparison for attributable policy revision.

### Deliberately omitted

- LOADOUT, 3rdi, Dogram, and Jubilee Engine sources: the live question can be decided inside ALEX.2 without importing adjacent semantics.
- Generic authorization frameworks and broader formal-method literature: unnecessary for this narrow attribution audit.
- Wolfram: no mathematical, statistical, temporal, or geometric computation is needed to decide this code-level binding question.

### Missing / inaccessible

The Static Collective GitBook Front Room was attempted first for orientation through the available GitBook connector, but the connector call was blocked by the safety layer. A public web search did not return a resolvable Front Room surface. This is **access fog**, not evidence that the Front Room is absent or unchanged.

**Sufficiency:** sufficient for the narrow code-level audit.

## Evidence path

### E1 — repository constitutional floor

`AGENTS.md` requires ALEX to preserve provenance distinctions and states that ALEX may discover/read/compare/propose but does not manufacture authority. It also requires corrections and reprocessing to preserve prior outputs and provenance.

Source: <https://github.com/the-static-collective/ALEX.2/blob/main/AGENTS.md>

### E2 — ALEX research law

`skills/alex/SKILL.md` requires consequential claims to preserve source/transformation chains, keeps discovery path distinct from evidence path, and says executable body identity/state and evidentiary correctness must not collapse.

Source: <https://github.com/the-static-collective/ALEX.2/blob/main/skills/alex/SKILL.md>

### E3 — newest live change

PR #92 added a second evaluator after the preceding `ROW-PRESENT-NOT-REACHABLE` packet:

```python
def audit_tiny_grammar_row(row: dict[str, Any], *, grammar_id: str) -> dict[str, Any]:
    rejected = row.get("grammar_eligible") is True and (
        row.get("observer_available") is not True
        or row.get("capability_reachable") is not True
    )
    return {
        ...
        "grammar_id": grammar_id,
        ...
    }
```

The evaluated predicate is fixed in the function body. `grammar_id` is not used to select, resolve, hash, version, or otherwise bind a grammar definition; it is copied to output metadata.

Source branch: <https://github.com/the-static-collective/ALEX.2/blob/ba0c9a975c98dd2938ce3f693cb029466f462946/experiments/eligibility_independence.py>

### E4 — test scope

The new test proves that one representable row can be `MATRIX_WITNESSED` and separately `GRAMMAR_REJECTED`. This is a real improvement over the prior state. The test supplies `BASE["grammar_id"]` and checks that the same identifier is returned, but it does not test that the identifier resolves to or commits the invariant used by the evaluator.

Source branch: <https://github.com/the-static-collective/ALEX.2/blob/ba0c9a975c98dd2938ce3f693cb029466f462946/tests/test_eligibility_independence_experiment.py>

### E5 — external primary comparison

Open Policy Agent decision logs record bundle metadata including the **bundle revision at the time of evaluation**; OPA bundle manifests can carry an explicit `revision` identifying the policy/data bundle. This is not evidence that ALEX should adopt OPA, but it is a mature independent example of keeping a decision attributable to the specific policy revision that produced it.

Sources:
- <https://www.openpolicyagent.org/docs/management-decision-logs>
- <https://www.openpolicyagent.org/docs/management-bundles>

## Claims

| ID | Claim | Class | Support | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #92 now separates representability from one tiny grammar's admissibility check. | observed | E3, E4 | It still does not prove path reachability. | supported |
| C2 | The returned `grammar_id` is currently caller-provided metadata, not a verified binding to evaluated grammar semantics. | observed | E3 | The function is explicitly a toy experiment, so the label may be intended only as local context. | supported |
| C3 | If later consumers treat that field as provenance for the grammar definition, they can misattribute a result without changing evaluated behavior. | inference | E3 | No current consumer was found that performs that promotion. | supported as risk, not current failure |
| C4 | Exact grammar/policy revision binding is a known useful audit pattern in mature policy systems. | documented comparison | E5 | OPA architecture is not ALEX authority and need not be copied. | supported |
| C5 | ALEX should add cryptographic grammar signing now. | proposal | none required | Far larger than the demonstrated need. | rejected |

## Direct counterexample

The current function permits this pair in principle:

```python
r1 = audit_tiny_grammar_row(row, grammar_id="restrictive-v1")
r2 = audit_tiny_grammar_row(row, grammar_id="permissive-v99")
```

For the same `row`, `r1` and `r2` execute exactly the same hard-coded predicate. Their semantic dispositions are identical; only the copied label differs.

This does **not** prove that either named grammar exists. That is precisely the point: the function does not require the label to resolve to anything.

A label change therefore changes claimed identity metadata without changing the decision procedure.

## Nearest boring explanation

This is an experimental discriminator, not a general grammar engine. The author may simply have intended `grammar_id` to mean “caller context for this one fixed toy grammar,” not “identifier of the semantics evaluated.” Under that reading there is no substantive bug in the experiment.

The smallest correction would then be vocabulary, not machinery: make the fixed contract explicit and prevent the field from looking stronger than it is.

## Competing readings

### Reading A — harmless fixture label

`grammar_id` is merely a tag copied through the experiment. No consumer should infer semantic identity from it.

**Consequence:** document that fact or make the ID constant. No resolver/version system is needed.

### Reading B — intended grammar provenance

`grammar_id` is meant to identify whichever grammar made the decision.

**Consequence:** current implementation is under-bound. The evaluator must either resolve semantics from the ID or return an attributable contract/revision identifier for the actual fixed predicate.

Current evidence does not establish which reading the owning design intends. Keep this unresolved rather than silently choosing one.

## Dependency / independence

The internal finding is code-local and does not depend on OPA. OPA is an independent architectural recurrence used only to show that policy-revision attribution is a normal solved concern elsewhere. Agreement between ALEX's provenance instincts and OPA's audit design does not establish common genealogy or mandate shared implementation.

## Discovery trace — why this door was opened

| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | previous packet `ROW-PRESENT-NOT-REACHABLE` | PR #92 latest commits | inspect current delta | motive | Prefer newly revealed material. |
| D2 | new tiny-grammar function | `grammar_id` parameter | compare input use vs output claim | discriminator | Parameter is copied but does not select semantics. |
| D3 | attribution question | OPA docs | narrow external comparison | analogy | Check whether mature policy systems bind decisions to policy revision. |

None of D1–D3 is promoted into evidence merely because it motivated the search; load-bearing support is E1–E5 above.

## Rights / egress

- Only public repository text and public documentation were inspected externally.
- No source corpora, private research material, credentials, scans, or local page bytes were sent to external models.
- No copyrighted source corpus was copied into this receipt.
- Durable effect is this new research Markdown file only.

## Residual fog

- The Front Room could not be freshly inspected due connector blocking.
- PR #92 is draft and may change before review/merge.
- No current downstream consumer was located that treats `grammar_id` as semantic provenance; risk is prospective.
- The intended meaning of `grammar_id` in this experiment is not separately specified.

## Smallest next discriminators / repo-worthy moves

1. **`GRAMMAR-ID-RELABELED-001` hostile test:** evaluate the same row twice with two different arbitrary `grammar_id` values and freeze that the semantic result is unchanged. This makes the metadata/semantics split executable without claiming it is wrong.
2. **Choose the field contract explicitly:** either replace caller-supplied `grammar_id` with a fixed `grammar_contract_id` for this hard-coded predicate, or make `grammar_id` resolve/select the grammar definition actually evaluated. Do not add both unless a consumer needs both.
3. **Only if portable grammar decisions become real:** add an attributable revision/digest of the evaluated grammar definition. Do not jump directly to signatures, policy engines, or a generic grammar registry.

## Compact law

```text
ROW PRESENT != GRAMMAR ADMISSIBLE
GRAMMAR ADMISSIBLE != REACHABLE
GRAMMAR LABEL != GRAMMAR SEMANTICS

A DECISION MAY CARRY A NAME.
THE NAME DOES NOT PROVE WHICH RULES RAN.
```

## Receipt

- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitBook orientation attempt; GitHub repository/PR inspection; public web primary-doc lookup. No Wolfram result used.
- **External byte egress:** public repository/documentation text only
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-02-2322-GRAMMAR-ID-NOT-SEMANTICS.md`
- **Promotion:** none
