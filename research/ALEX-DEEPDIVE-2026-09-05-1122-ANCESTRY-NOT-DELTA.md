# ALEXDEEPDIVE — ANCESTRY-NOT-DELTA-001

**Status:** RESEARCH  
**Promotion:** none  
**Shape:** AUDIT  
**Created:** 2026-09-05 11:22 America/Chicago

## Ground

- **Question:** What materially changed in ALEX.2 since the previous `FRONTIER-HOLD` packet, and does the new reconciliation carrier change the live `PARTITION-SWAP-001` research semantics?
- **Desired consequence:** Distinguish provenance/history preservation from effective tree/content change, and avoid treating commit-ahead count as semantic novelty.
- **Stop condition:** Establish whether PR #105 faithfully reconstitutes the PR #99 experiment on current `main`, whether its executable/test blobs changed, and whether it resolves the pending `ORDER-SWAP-CONTROL-001` frontier.
- **Corpus:** `the-static-collective/ALEX.2`; PR #105, superseded PR #99, current `main`, governing ALEX files; current Git primary documentation only where useful for Git object semantics.
- **Authority/effect boundary:** Read/audit plus this durable research packet only. No merge, runtime promotion, schema promotion, or canon admission.
- **Formation trace active:** no.

## Orientation / world cut

The Static Collective GitBook Front Room was attempted first for orientation. The connected GitBook organization-list operation was blocked by the tool safety surface. This is **access fog**, not evidence about the Front Room's contents. No GitBook content was relied on in the evidence path.

Required ALEX governance was read before consequential claims:

- `AGENTS.md`: preserve evidence/interpretation/proposal distinctions, discovery/evidence split, and authority boundaries.
- `skills/alex/SKILL.md`: use the smallest adequate research shape; `AUDIT` is appropriate here.
- `skills/alex/references/research-receipt.md`: a receipt records what this run encountered and does not manufacture authority.

### Included exact heads

- observed `main`: `4ed35ee9352187be235de2f91ceb8ba3b1f9865c`
- PR #105 reconciled head: `9543fdca106718259ee7f1ad0b25df62564fdd69`
- original PR #99 witness head: `b81b8d5338e4043be56405d442dec439bf4852f7`

### Deliberately omitted doors

- WTC corkboard / PR #97: no new evidence made it stronger than the newly created reconciliation carrier.
- older draft experiments (#92, #87, #86, #85, etc.): unchanged relative to this pass's strongest live delta.
- Wolfram: no mathematical/statistical/temporal computation was material to this Git provenance audit.

## Discovery trace

1. Recent-commit inspection showed `main` still ended at the previous `FRONTIER-HOLD` research commit.
2. Open-PR inspection revealed newly created draft PR #105, explicitly described as a current-main reconciliation of PR #99.
3. That made reconciliation identity/provenance the strongest new frontier for this pass.

This discovery trace explains **why the audit was run**. It is not itself evidence for the audit conclusions.

## Evidence path

### E1 — PR #105 declares a two-parent reconciliation

GitHub's exact commit object for `9543fdca...` records two parents:

1. `4ed35ee9...` — then-current `main`
2. `b81b8d53...` — original PR #99 witness head

This is documented repository state.

### E2 — Effective tree delta against current main is only two added files

GitHub compare from `4ed35ee9...` to `9543fdca...` reports:

- status: ahead
- ahead-by: 7
- behind-by: 0
- effective file delta: exactly two added files
  - `experiments/partition_swap.py` (+185)
  - `tests/test_partition_swap_experiment.py` (+59)

The seven reachable commits are therefore an ancestry fact; they are not seven independent effective content changes against current `main`.

### E3 — Reconciled executable blob is byte-identical to the original witness blob

`experiments/partition_swap.py`:

- PR #99 head blob SHA: `2d0777efa32fdd7218efb90db51fc97771f4bbe1`
- PR #105 head blob SHA: `2d0777efa32fdd7218efb90db51fc97771f4bbe1`

Exact blob identity is stronger than a textual resemblance claim: the file content object is identical.

### E4 — Reconciled test blob is byte-identical to the original witness blob

`tests/test_partition_swap_experiment.py`:

- PR #99 head blob SHA: `56573a9d72efc673ce1d597c80bc307fa420e806`
- PR #105 head blob SHA: `56573a9d72efc673ce1d597c80bc307fa420e806`

Again, the test content object is identical.

### E5 — Fresh verification passed on the reconciled head

GitHub Actions for exact head `9543fdca...` reports `crucible-contract` run `33977224022` / run #395 as `completed: success`.

This witnesses technical compatibility on the reconciled head. It does **not** establish historical truth, graph-theoretic correctness beyond the tested contract, or merge authority.

### E6 — The pending order-sensitivity frontier remains unresolved

The reconciled `partition_swap.py` still implements:

```python
def _macro_graph_differs(left, right):
    return (
        left["macro_nodes"] != right["macro_nodes"]
        or left["macro_edges"] != right["macro_edges"]
    )
```

The reconciled test file still contains only:

- `PARTITION-SWAP-001`
- `RELABEL-CONTROL-001`
- `ISOLATED-NODE-CONTROL-001`

There is no `ORDER-SWAP-CONTROL-001` in the reconstituted blob pair.

## External primary-source check

Current Git documentation separates **commit history** from **tree/file state**:

- a commit records a tree plus parent commit IDs; merge commits can have multiple parents;
- a tree represents directory/file state;
- `git diff` compares tree/content states;
- Git's own user manual explicitly notes that equal project contents can be reached by different historical routes.

This supports the audit's conceptual distinction. It does not substitute for the repository-specific blob and compare evidence above.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #105 is a two-parent provenance-preserving reconciliation of current main with the PR #99 witness head. | observed | E1 | Parentage alone does not prove effective tree identity. | supported |
| C2 | `7 commits ahead` does not mean seven independent semantic/content changes against current main. | inference from observed Git state | E1 + E2 + Git object model | Commit ancestry can contain meaningful historical changes; this claim is only about effective delta relative to the chosen base. | supported |
| C3 | The two experimental files on PR #105 are exact content reconstitutions of the corresponding PR #99 witness files. | observed | E3 + E4 | This does not claim the entire repository trees are identical. | supported |
| C4 | Fresh CI establishes that the reconciled carrier is technically green under the current workflow. | observed | E5 | CI success != evidentiary correctness != merge authority. | supported |
| C5 | PR #105 does not resolve `ORDER-SWAP-CONTROL-001`. | observed/inference | E6 | A different unseen branch could contain such work; it is absent from this reconciled carrier. | supported |
| C6 | Reconciliation provenance and semantic novelty must be reported as separate dimensions. | proposal | C1-C5 | Could be unnecessary if all future carriers already state both explicitly. | proposed |

## Contradictions and alternatives

### Competing reading A — “Seven commits ahead means a large new implementation delta”

**Counterevidence:** the current-base compare reports only two added files; both files have the exact blob SHAs from PR #99. The extra reachable commits are ancestry retained through the second parent.

### Competing reading B — “Because the blobs are identical, PR #105 adds nothing”

Too strong. PR #105 adds a **new carrier relationship**: it attaches the old witness branch to current `main` with explicit two-parent ancestry and demonstrates fresh CI compatibility there. That provenance/landing-state delta is real even though the experimental file contents are unchanged.

### Nearest boring explanation

PR #105 is exactly what its body says: maintenance reconciliation. It restores a clean current-main landing carrier while intentionally preserving witness history and intentionally not widening the experiment.

## Audit pressure

- **Direct counterexample sought:** Could the reconciled carrier contain altered experiment bytes despite claiming exact reconstitution? Checked by blob SHA; no.
- **History/content collapse check:** Could `ahead_by=7` be mistaken for seven-file or seven-feature novelty? Yes; compare shows only two effective added files.
- **Replay impersonation check:** Exact blob reuse supports content identity for the two files, not identity of commit, branch, tree, historical context, or authority.
- **Authority check:** PR remains draft; `authority: none` remains in experiment outputs; no merge was performed.
- **Dependency/independence:** PR #105 is explicitly dependent on PR #99 ancestry. It is not an independent corroborating implementation.
- **Rights/egress:** only public repository text/metadata and public Git documentation were read. No corpus bytes or private research material were egressed.

## Finding

The new material fact is not a new graph result. It is a **lawful reconciliation carrier** whose history changed while the relevant experimental content did not.

```text
ANCESTRY DELTA != TREE DELTA
TREE DELTA != SEMANTIC DELTA
BLOB IDENTITY != COMMIT IDENTITY
RECONSTITUTION != INDEPENDENT CORROBORATION
GREEN CARRIER != PROMOTION
```

PR #105 therefore **does not supersede the live research frontier** identified by the prior packet. It strengthens provenance and current-main compatibility for the existing experiment, while leaving `ORDER-SWAP-CONTROL-001` untouched.

## Residual fog

- This audit did not inspect every reachable historical commit in PR #105 individually because exact parentage, base/head compare, exact blob identity, and fresh CI were sufficient for the bounded question.
- The GitBook Front Room remained inaccessible through the connected operation; no claim is made about its current orientation state.
- No claim is made that PR #105 should merge. Technical green plus exact reconstitution is not owner approval.

## Smallest next discriminators / repo-worthy moves

1. **`ORDER-SWAP-CONTROL-001`** remains the smallest semantic discriminator: preserve identical labeled macro-node and typed-edge content, permute only serialization order, and require an order-only/non-structural result.
2. If reconciliation carriers recur, add a tiny receipt convention that reports **ancestry delta** and **effective tree delta** separately; do not infer one from the other.
3. Keep PR #105 draft until the owner chooses whether to land the unchanged experiment before or after the pending order-control; do not silently fold the new discriminator into a maintenance carrier.

## Receipt

- **Created:** 2026-09-05 11:22 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE
- **Tool/model boundary:** connected GitHub reads/writes; connected GitBook orientation attempt blocked; current public Git primary documentation via web search; no Wolfram computation
- **External byte egress:** public repository metadata/text and public documentation only
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-05-1122-ANCESTRY-NOT-DELTA.md`
- **Promotion:** none
