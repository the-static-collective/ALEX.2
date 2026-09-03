# ALEXDEEPDIVE — RELABELING-NOT-IDENTITY-001

**Status:** RESEARCH  
**Promotion:** none  
**Shape:** AUDIT  
**Created:** 2026-09-03 11:22 America/Chicago

## Finding

The previous ALEXDEEPDIVE frontier has materially advanced.

Draft PR #92 now implements the exact `GRAMMAR-ID-RELABELED-001` discriminator proposed by the prior packet. The same hostile row is evaluated twice under two different `grammar_id` strings, and the fixed tiny-grammar evaluator produces the same semantic observation. The experiment returns:

```text
GRAMMAR_ID_UNBOUND
```

That is a useful executable result, but its lawful interpretation is narrower than the label can sound in isolation:

```text
RELABELING WITNESSES NON-SELECTION.
IT DOES NOT WITNESS GRAMMAR IDENTITY.
```

More explicitly:

```text
grammar_id changes
+ fixed evaluator semantics do not change
=> grammar_id does not select those semantics in this experimental function

!=
this string names no grammar anywhere
!=
the named grammars are semantically identical
!=
a grammar registry is required
!=
provenance is globally broken
```

The implementation's own docstring already states this boundary correctly: `GRAMMAR_ID_UNBOUND` is a measurement about the fixed experimental function and does not establish what either named grammar actually means. This pass therefore hardens the interpretation rather than discovering a defect that requires an immediate production fix.

## Ground

- **Question:** What does the newly executed `GRAMMAR-ID-RELABELED-001` discriminator actually establish, and what is the smallest justified next move?
- **Desired consequence:** Convert the newly available executable witness into a precise ALEX research statement without laundering an inert-label observation into a claim about global grammar identity, provenance, or required infrastructure.
- **Stop condition:** Stop once the current PR delta, evaluator dependency, test witness, strongest alternative reading, and one next discriminating condition are explicit.
- **Corpus/date:** `the-static-collective/ALEX.2`, current `main` plus draft PR #92 at head `5385255c37fe6a9ddef8ac942b992fe930a76d02`, inspected 2026-09-03.
- **Authority/effect boundary:** Research receipt only. No runtime, schema, grammar registry, resolver, signature, merge, authorization, or canon promotion.
- **Formation trace:** yes, minimal.

## World cut

### Orientation

The Static Collective GitBook Front Room was attempted first through the connected GitBook surface. Organization access was blocked by the connector safety layer. This is **access fog**, not evidence that the Front Room is absent, unchanged, or irrelevant.

### Included

- `ALEX.2/AGENTS.md` on current main.
- `skills/alex/SKILL.md` on current main.
- `skills/alex/references/research-receipt.md` on current main.
- Current ALEX.2 commit history.
- Draft PR #92 and its exact current head.
- Exact PR #92 experiment module and focused test at head `5385255c37fe6a9ddef8ac942b992fe930a76d02`.
- Previous packet `ALEX-DEEPDIVE-2026-09-03-0522-FRONTIER-HOLD.md`.
- A narrow software-testing literature comparison concerning metamorphic relations.

### Deliberately omitted

- Adjacent Static Collective repositories: the new discriminator is self-contained inside ALEX.2; no neighboring runtime or semantic contract is needed to interpret it.
- Wolfram: no mathematical, statistical, temporal, geometric, or scientific computation is material to the finding.
- OPA/SLSA/RATS architecture comparisons: those were useful in prior provenance packets but would not discriminate the present question.

### Sufficiency

Sufficient for a narrow evaluator-semantics audit. Insufficient to decide whether any future ALEX consumer requires portable/versioned grammar identity because no such owner requirement is established by this evidence path.

## Acquisitions

| ID | Provider | Item and locus | Resolution | Role | Rights / egress |
| --- | --- | --- | --- | --- | --- |
| A1 | GitHub | `ALEX.2/AGENTS.md` | current main | constitutional boundary | public repo text only |
| A2 | GitHub | `skills/alex/SKILL.md` | current main | research method | public repo text only |
| A3 | GitHub | `skills/alex/references/research-receipt.md` | current main | receipt contract | public repo text only |
| A4 | GitHub | prior frontier-hold packet | current main | formation ancestry | public repo text only |
| A5 | GitHub | PR #92 metadata/diff | head `5385255c...` | discovery + evidence routing | public repo text only |
| A6 | GitHub | `experiments/eligibility_independence.py` | exact PR head | primary implementation evidence | public repo text only |
| A7 | GitHub | `tests/test_eligibility_independence_experiment.py` | exact PR head | executable witness | public repo text only |
| A8 | GitHub | compare `ba0c9a9...` → `5385255...` | exact refs | delta proof | public metadata only |
| A9 | scholarly web | 2024 systematic review of metamorphic-relation derivation | published article | methodological comparison only | public scholarly metadata/text; no project bytes egressed |

No local/private source corpus or copyrighted project payload was sent to an external model or service during this pass.

## Evidence path

### E1 — the previously requested discriminator is now a real code delta

The preceding HOLD packet observed PR #92 at:

```text
ba0c9a975c98dd2938ce3f693cb029466f462946
```

and explicitly left `GRAMMAR-ID-RELABELED-001` as the next discriminator.

Current PR #92 is:

```text
5385255c37fe6a9ddef8ac942b992fe930a76d02
```

A direct commit comparison reports:

```text
ahead_by: 2
behind_by: 0
files changed: 2

experiments/eligibility_independence.py
  +39

tests/test_eligibility_independence_experiment.py
  +17
```

This is a material post-packet delta rather than repeated inspection of the old state.

### E2 — the evaluator semantics remain fixed and independent of `grammar_id`

The tiny grammar evaluator computes rejection solely from row fields:

```python
rejected = row.get("grammar_eligible") is True and (
    row.get("observer_available") is not True
    or row.get("capability_reachable") is not True
)
```

The supplied `grammar_id` is copied into the result but does not participate in that predicate.

Therefore, for the current function body, changing only `grammar_id` cannot change `rejected`, `disposition`, `reason`, or `reachable_under_tiny_grammar`.

This is stronger than a coincidental equality on one test input because it follows directly from the current implementation dependency structure. It is still local to this exact implementation body and can change in a later descendant.

### E3 — the new discriminator intentionally performs a relabel metamorphism

`audit_grammar_id_relabeling()` evaluates the same row twice, changes only the grammar label, and compares these fields:

```text
schema
disposition
reason
row_id
reachable_under_tiny_grammar
authority
```

If the labels differ while those observed semantic fields remain equal, it returns:

```text
GRAMMAR_ID_UNBOUND
```

The function's docstring sharply scopes the result:

> the measurement concerns this fixed experimental function and does not establish what either named grammar actually means.

This is the governing interpretation for the present packet.

### E4 — the focused hostile test witnesses the expected invariance

The test applies the same `eligible-hidden` row under:

```text
jubilee-little-yes-probe
totally-different-grammar
```

and asserts:

```text
disposition == GRAMMAR_ID_UNBOUND
semantic_observation_equal == true
authority == none
```

PR #92's execution receipt reports a test-first sequence:

```text
RED  07305eb3de5a6155f389c4fbc295bea04210b526
     Actions 33762299178
     262 tests; exactly the new discriminator errored because the function was absent

GREEN 5385255c37fe6a9ddef8ac942b992fe930a76d02
      Actions 33762382783
      full unittest discovery SUCCESS
```

This is source testimony from the PR receipt plus directly inspectable code/test evidence. The present pass did not independently rerun that GitHub Actions job in a local checkout, so the CI statement remains attributed to the repository receipt rather than silently converted into a new local observation.

### E5 — the testing shape has a standard methodological analogue

Metamorphic testing evaluates relations between multiple executions connected by a declared input transformation and checks the corresponding output relation. A 2024 systematic review describes metamorphic relations as relations over test inputs and their corresponding outputs and surveys ways to derive such relations.

The ALEX experiment is methodologically analogous in a narrow sense:

```text
input transformation: change grammar_id, hold row fixed
expected output relation: selected semantic fields remain equal
```

This analogy supports naming the experiment as an invariance/non-selection test. It does **not** establish ALEX grammar semantics, correctness of the tiny grammar, or any external standard that ALEX must adopt.

Scholarly comparison:
- S. F. Iakusheva / Yakusheva & A. S. Khritankov, “A systematic review of methods for deriving metamorphic relations,” *Program Systems: Theory and Applications* 15(2), 2024, DOI 10.25209/2079-3316-2024-15-2-37-86.

## Claims

| ID | Statement | Class | Support | Counterevidence / limit | Disposition |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #92 materially advanced after the prior HOLD packet by adding the exact requested relabeling discriminator. | documented fact | E1 | Draft PR; not landed on main. | supported |
| C2 | In the exact current `audit_tiny_grammar_row()` implementation, `grammar_id` does not select or alter the rejection predicate. | documented fact / code observation | E2 | A future descendant may change the function. | supported |
| C3 | The current relabeling experiment is a valid witness that the grammar label is semantically inert **for the compared output fields of this fixed evaluator**. | inference from code + executable specimen | E2-E4 | The test itself uses one row; globality comes from current source inspection, not test coverage alone. | supported, scoped |
| C4 | `GRAMMAR_ID_UNBOUND` proves that neither label corresponds to any real grammar semantics. | inference | none | Directly contradicted by the experiment docstring and scope. | rejected |
| C5 | The two named grammars are semantically identical. | inference | none | No grammar definitions were resolved or compared. | rejected |
| C6 | ALEX must now build a registry, resolver, digest/signature scheme, or portable grammar-provenance layer. | proposal | none | No owner/consumer requirement establishes that cost. | HOLD / not earned |
| C7 | If a future consumer expects one field to select among materially different grammars, semantic identity must become operationally bound to the selected definition somehow. | conditional proposal | E2-E4 | Condition is not yet established as current product need. | live conditional |

## Competing readings

### Reading A — `GRAMMAR_ID_UNBOUND` means “grammar provenance is broken”

Too strong.

The current function may simply be a fixed tiny countermodel whose caller-supplied label exists for fixture context. In that design, the label is not supposed to select semantics. The experiment accurately measures that fact.

### Reading B — the label is pure decoration and should be deleted now

Not established.

A context label can remain useful for formation trace or reporting even when it does not select behavior. Deletion would require a consumer-level reason, not merely semantic inertness.

### Reading C — the field should immediately become a content digest or registry key

Premature.

Binding mechanisms solve a stronger problem: portable or selectable semantic identity. This pass finds no current owner contract requiring that problem to be solved.

### Reading D — the relabeling test is worthless because the source already visibly ignores the label

Also too strong.

The test has value as an executable regression witness: it freezes the current non-selection behavior and will fail or change meaning if later work makes grammar identity semantically operative. It converts a code-reading observation into a durable behavioral discriminator.

## Direct counterevidence / hostile pressure

The strongest pressure against overreading is already inside the implementation:

```text
It does not establish what either named grammar actually means.
```

A second hostile thought specimen:

```text
fixed predicate P
label = "grammar-A"
label = "grammar-B"

P(row) is identical in both runs
```

This proves only that labels do not alter `P`. It does not prove grammar A and grammar B are equal, because no semantics for A or B were evaluated.

Conversely, suppose a later experimental dispatcher defines:

```text
G1: eligible -> observer_available AND capability_reachable
G2: eligible -> capability_reachable
```

For a row with:

```text
grammar_eligible = true
observer_available = false
capability_reachable = true
```

G1 would reject while G2 would admit. Only in a system that actually selects between such declared semantics would a grammar identity field need to bind to the selected definition to make the result attributable.

That is a **future discriminator**, not evidence that such a dispatcher should exist now.

## Dependency / independence uncertainty

- The relabeling result is not an independent replication of the preceding code audit; it was deliberately built from that prior frontier and is therefore genealogically dependent.
- The scholarly metamorphic-testing comparison is methodologically independent but does not independently support ALEX's project-specific semantics.
- The reported GREEN CI is project-generated evidence from PR #92; this run did not recreate it on an independent machine.
- No adjacent repo was imported as corroboration, avoiding false cross-project independence.

## Nearest boring explanation

PR #92 contains one fixed experimental countermodel. `grammar_id` is a human-readable context field copied into results, not a runtime selector. The new test merely freezes that simple fact so future descendants cannot accidentally reinterpret the label as semantic provenance without crossing an explicit contract boundary.

This boring explanation currently fits all evidence and requires no additional infrastructure.

## Discovery trace

Discovery trace is preserved separately from the evidence path:

| ID | From | To | Move | Why we looked | Evidence role |
| --- | --- | --- | --- | --- | --- |
| D1 | run request | GitBook Front Room | orientation attempt | required first door | none; access blocked |
| D2 | access fog | ALEX governing files | constitutional read | required before consequential claims | routing only |
| D3 | prior HOLD packet | current `main` + PR #92 | delta comparison | prefer newly revealed material | led to E1 |
| D4 | new PR commits | exact experiment/test | source inspection | previous discriminator appeared | led to E2-E4 |
| D5 | relabel structure | metamorphic-testing literature | narrow methodological comparison | test-shape pressure | led to E5 only |
| D6 | result label | alternative interpretations | adversarial audit | prevent semantic overreach | inference discipline |

Discovery motive is not evidentiary support. Load-bearing project claims rest on E1-E4.

## Toast ghosts / replay resistance

- Prior packet was used as an ancestry marker, not substituted for current repo inspection.
- The PR remains draft; this packet does not call it landed or canonical.
- The test's successful result does not authorize merge.
- `GRAMMAR_ID_UNBOUND` is not promoted into a universal ALEX law.
- No future grammar semantics are retrojected into the current tiny evaluator.

## SLEEP

The clean survivor is smaller than the prior open question:

```text
THE PARAMETER IS PRESENT.
THE PARAMETER DOES NOT SELECT THE CURRENT PREDICATE.
THE EXPERIMENT NOW WITNESSES THAT NON-SELECTION.
```

The temptation to continue immediately into registries, hashes, signatures, policy engines, or semantic-version machinery is not supported by a current consumer need.

## .LEEP

The useful higher-order distinction is:

```text
IDENTIFIER AS LABEL
!=
IDENTIFIER AS SELECTOR
!=
IDENTIFIER AS CONTENT BINDING
!=
IDENTIFIER AS AUTHENTICATED PROVENANCE
```

A system may lawfully use the first without promising the latter three.

## Bridge ledger

| Neighbor | Relation | Status |
| --- | --- | --- |
| Prior `GRAMMAR-ID-NOT-SEMANTICS-001` | direct formation ancestor | established |
| Prior `FRONTIER-HOLD-001` | held this exact discriminator pending delta | established |
| Metamorphic testing | methodological analogue for relabel→invariance check | comparison only |
| Grammar registry/resolver | possible future implementation if semantic selection becomes a requirement | proposal / not earned |
| OPA / signed policy systems | stronger provenance architectures | deliberately not imported; unnecessary for current discriminator |

## Residual fog

- GitBook Front Room contents were inaccessible in this run.
- PR #92 is draft and not on `main`.
- The current repo evidence does not establish whether any owner intends `grammar_id` to become a selector, a provenance handle, or remain contextual metadata.
- One focused test row is not exhaustive behavioral testing, although direct source inspection establishes label non-dependence for the current predicate.
- The exact CI run was reported by the PR receipt; this run did not independently execute the suite locally.
- No statement is made about unpushed/private/local work outside the inspected repository surfaces.

## Smallest next discriminators / repo-worthy moves

1. **Freeze the interpretation, not new machinery.** Keep or add one sentence beside `GRAMMAR_ID_UNBOUND`: it means “changing this label did not change the declared semantic observation of this fixed evaluator.” It does not compare grammar definitions.
2. **Require a real selection need before binding identity.** If an actual consumer needs multiple grammar semantics, create one tiny two-grammar experimental dispatcher and one row on which the grammars intentionally diverge. That would establish that semantic selection—not mere labeling—is now part of the contract.
3. **Otherwise stop.** Do not add a registry, resolver, digest/signature scheme, or portable grammar-provenance layer merely because an inert metadata field exists.

## Compact law

```text
RELABELING CAN WITNESS NON-SELECTION.
RELABELING CANNOT WITNESS GRAMMAR IDENTITY.

LABEL != SELECTOR != CONTENT BINDING != AUTHENTICATED PROVENANCE.
```

## Verdict

**SURVIVES, NARROWED.**

The prior frontier was real and its requested discriminator now exists. The discriminator supports the local claim that `grammar_id` is semantically inert for the current fixed tiny evaluator. It does not support a larger claim about the meanings or equivalence of named grammars, and it does not yet earn infrastructure for semantic provenance.

## Receipt

- **Researcher/agent:** ALEXDEEPDIVE research pass
- **Tool/model boundary:** GitBook orientation attempt; GitHub governing-file, commit, PR, exact-source, exact-test, and compare inspection; narrow public scholarly web comparison. No Wolfram result used because no materially relevant computation was required.
- **External byte egress:** public repository metadata/text and public scholarly sources only; no private/local corpus bytes sent externally
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-03-1122-RELABELING-NOT-IDENTITY.md`
- **Promotion:** none
