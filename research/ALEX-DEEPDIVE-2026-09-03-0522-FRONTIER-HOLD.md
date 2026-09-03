# ALEXDEEPDIVE — FRONTIER-HOLD-001

**Status:** RESEARCH  
**Promotion:** none  
**Shape:** AUDIT  
**Created:** 2026-09-03 05:22 America/Chicago

## Finding

No materially new ALEX.2 evidence has appeared since the immediately previous ALEXDEEPDIVE packet `GRAMMAR-ID-NOT-SEMANTICS-001`.

Current `main` is still headed by the prior research commit `82a8fe66d3796b752ac5654844f2a29c3e2f894b`, and open draft PR #92 is still headed by `ba0c9a975c98dd2938ce3f693cb029466f462946`. The PR's current implementation still applies one hard-coded tiny-grammar predicate while copying a caller-supplied `grammar_id` into the result. The prior frontier therefore remains live but unchanged:

```text
GRAMMAR LABEL != GRAMMAR SEMANTICS
```

This run does **not** force a new frontier. The correct research disposition is HOLD pending a material code, contract, test, or owner-intent delta.

## Ground

- **Question:** Has ALEX.2 materially changed since the prior ALEXDEEPDIVE such that a new strongest research frontier is warranted?
- **Desired consequence:** Avoid novelty-for-novelty's-sake while preserving an attributable state check and the next smallest discriminator.
- **Stop condition:** Compare current main, current open PR #92, and the prior deep-dive packet; stop if no new evidence changes the frontier.
- **Corpus/date:** `the-static-collective/ALEX.2`, current main and current PR #92 state encountered on 2026-09-03.
- **Authority/effect boundary:** Research receipt only. No runtime, schema, merge, policy, authorization, or canon promotion.
- **Formation trace:** yes, minimal.

## World cut

### Included

- `ALEX.2/AGENTS.md` on current main.
- `skills/alex/SKILL.md` on current main.
- `skills/alex/references/research-receipt.md` on current main.
- Current main commit history.
- Current open PR list.
- PR #92 changed files and commit history.
- Prior packet `research/ALEX-DEEPDIVE-2026-09-02-2322-GRAMMAR-ID-NOT-SEMANTICS.md`.

### Deliberately omitted

- Adjacent repos: no current ALEX.2 delta required importing neighboring project semantics.
- External scholarship and framework research: no new consequential claim required external support; repeating prior OPA comparison would add no discriminating evidence.
- Wolfram: no mathematical, statistical, temporal, geometric, or scientific computation was material to this state audit.

### Missing / inaccessible

The Static Collective GitBook Front Room was attempted first for orientation through the available GitBook connector. The organization-read operation was blocked by the connector safety layer. This is **access fog**, not evidence that the Front Room is absent or unchanged.

**Sufficiency:** sufficient for the narrow repo-delta audit.

## Acquisitions

| ID | Provider | Item and locus | Method/time | Resolution | Rights/egress |
| --- | --- | --- | --- | --- | --- |
| A1 | GitHub | `ALEX.2/AGENTS.md` | direct file fetch | current main | public repo text only |
| A2 | GitHub | `skills/alex/SKILL.md` | direct file fetch | current main | public repo text only |
| A3 | GitHub | `skills/alex/references/research-receipt.md` | direct file fetch | current main | public repo text only |
| A4 | GitHub | repository commits | REST collection | current main head observed | public metadata only |
| A5 | GitHub | open PRs | REST collection | PR #92 current head observed | public metadata only |
| A6 | GitHub | PR #92 changed files | patch fetch | current PR head | public repo text only |
| A7 | GitHub | prior deep-dive packet | direct file fetch | current main | public repo text only |

## Evidence path

### E1 — current main has no post-packet implementation delta

The current commit list is headed by `82a8fe66d3796b752ac5654844f2a29c3e2f894b`, whose message is `research: add ALEXDEEPDIVE grammar identity binding audit`. Its parent is the prior deep-dive commit `db761bd974a3ab21b4bc8da7a8451aea24779e94`.

Current history endpoint: <https://api.github.com/repos/the-static-collective/ALEX.2/commits?per_page=20>

### E2 — PR #92 has no post-packet code delta

Open draft PR #92 is currently headed by `ba0c9a975c98dd2938ce3f693cb029466f462946`, last committed at 2026-09-03T03:38:39Z. Its two changed files remain:

- `experiments/eligibility_independence.py`
- `tests/test_eligibility_independence_experiment.py`

PR: <https://github.com/the-static-collective/ALEX.2/pull/92>

### E3 — the prior live frontier remains structurally unchanged

The current PR implementation still contains:

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

The supplied `grammar_id` does not select, resolve, hash, version, or otherwise determine the predicate being executed. It remains copied metadata beside fixed semantics.

### E4 — prior packet already captured this exact consequence

`GRAMMAR-ID-NOT-SEMANTICS-001` already concluded that the result can witness execution of the fixed tiny-grammar function, but `grammar_id` alone cannot witness that the named grammar semantics were the semantics actually evaluated. It proposed `GRAMMAR-ID-RELABELED-001` as the smallest next executable discriminator.

Prior packet: <https://github.com/the-static-collective/ALEX.2/blob/main/research/ALEX-DEEPDIVE-2026-09-02-2322-GRAMMAR-ID-NOT-SEMANTICS.md>

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | No material ALEX.2 implementation change has landed on main since the prior deep-dive packet. | observed | E1 | An inaccessible or unpushed local branch could exist; not part of current repo evidence. | supported |
| C2 | PR #92's current head is unchanged relative to the state inspected by the prior packet. | observed | E2, E4 | PR metadata can change without code; no such change found that alters the research frontier. | supported |
| C3 | `grammar_id` remains metadata rather than a semantic selector/binding in the tiny-grammar evaluator. | observed | E3 | It may intentionally be only a fixture/context label. | supported |
| C4 | A new law or external research branch is warranted now. | proposal | none | No material delta supports it. | rejected |
| C5 | The prior smallest discriminator should remain next. | proposal | E3, E4 | Owner intent or a new PR change could supersede it. | held |

## Contradictions and alternatives

### Alternative A — manufacture a deeper semantic frontier now

It is possible to speculate further about grammar fingerprints, policy registries, signed definitions, resolver semantics, or decision provenance.

**Rejected for this run:** none is required by new evidence. Doing so would violate the instruction to prefer newly revealed material and not force novelty.

### Alternative B — treat lack of repo delta as absence of work

**Rejected:** this audit only establishes no material delta in the inspected current GitHub surfaces. It does not establish that no local, private, unpushed, or inaccessible work exists.

## Discovery trace — why we looked

| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | scheduled ALEXDEEPDIVE | GitBook Front Room | orientation attempt | motive | Required first door. Connector blocked. |
| D2 | Front Room access fog | ALEX.2 constitutional files | establish rules | evidence-routing | Required before consequential claims. |
| D3 | prior packet | current main + PR #92 | delta audit | discriminator | Prefer newly revealed material. |
| D4 | unchanged code state | HOLD | refusal of forced novelty | inference | No new evidence changed the frontier. |

Discovery motive is not evidence; load-bearing support is E1-E4 above.

## Pressure

- **Direct counterexample:** none newly needed; the prior arbitrary-relabel counterexample still addresses the live frontier.
- **Nearest boring explanation:** nothing has materially changed yet. The project may simply be waiting for the next executable discriminator or owner review.
- **Independence/lineage check:** the present finding is repo-local and does not depend on external architecture analogies.
- **Replay impersonation check:** this run did not treat the prior packet as current evidence until current main and PR #92 were re-inspected.
- **Ghost-promotion check:** no prior research law was promoted into runtime or canon.

## Residual fog

- Front Room contents were inaccessible during this run.
- PR #92 remains draft and can change after this receipt.
- No owner-intent document was found that resolves whether `grammar_id` is merely fixture context or intended semantic provenance.
- Unpushed/private/local work is outside this repo evidence path.

## Smallest next discriminators / repo-worthy moves

1. **Keep `GRAMMAR-ID-RELABELED-001` next:** evaluate the same row with two arbitrary grammar labels and freeze that the semantic result is unchanged.
2. **After that test, choose the contract:** either make the fixed evaluator emit a fixed grammar-contract identity, or make a supplied grammar identity actually select/resolve semantics.
3. **Do nothing larger until a consumer requires portability or versioned grammar provenance.** No registry, signatures, or policy-engine import is justified yet.

## Compact law

```text
NO MATERIAL DELTA != NO LIVE FRONTIER

THE FRONTIER MAY HOLD.
ALEX DOES NOT OWE NOVELTY TO THE CLOCK.
```

## Receipt

- **Researcher/agent:** ALEXDEEPDIVE automated research pass
- **Tool/model boundary:** GitBook orientation attempt; GitHub repository, commit, PR, patch, and prior-receipt inspection. No external scholarly source or Wolfram result used because no new claim required them.
- **External byte egress:** public repository metadata/text only
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-03-0522-FRONTIER-HOLD.md`
- **Promotion:** none
