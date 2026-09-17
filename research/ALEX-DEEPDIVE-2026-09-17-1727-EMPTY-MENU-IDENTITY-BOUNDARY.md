# ALEXDEEPDIVE — EMPTY-MENU-IDENTITY-BOUNDARY-001

Status: **RESEARCH**
Promotion: **none**

## Ground
- Question: What is the strongest live ALEX research frontier after the latest `MENU-PROVENANCE-001` change?
- Desired consequence: identify the smallest evidence-earned discriminator without promoting research into runtime authority.
- Stop condition: one bounded frontier with direct repository evidence and 1–3 next moves.
- Task shape: **AUDIT**
- Formation trace active: no.
- Authority/effect boundary: research only; no canon, runtime, merge, or execution authority.

## Orientation and world cut
GitBook Front Room orientation was attempted first. The connected organization call was blocked before content retrieval, so Front Room content is **access fog**, not absence.

Required governance was read before consequential claims:
- `AGENTS.md`
- `skills/alex/SKILL.md`
- `skills/alex/references/research-receipt.md`

Included evidence:
- ALEX.2 `main` pre-write head: `0dfba6b91aa364215ba53dce4058de2717319103`.
- PR #121 `MENU-PROVENANCE-001`, exact inspected head: `1aadae09d73bdf1528bd0f3ea2818321291a1275`.
- Exact runtime file `alex_runtime/menu_provenance.py` at that head.
- Exact test file `tests/test_menu_provenance.py` at that head.
- Compare from previously audited PR head `ec5725a243bd0b27b766e6714d6b293d2c413e00` to current head.

Deliberately omitted: broad adjacent-repo traversal, scholarship, and computation. The live issue is a local executable identity/provenance contract and does not require them.

## Material delta
Since the preceding ALEXDEEPDIVE, PR #121 advanced by one commit:

`1aadae09d73bdf1528bd0f3ea2818321291a1275` — `test: preserve empty representative menu provenance`

The new controls establish two useful semantics:
1. a representative with an empty local successor menu remains present in `representatives` rather than disappearing from the receipt;
2. an entirely empty representative family is refused.

This is a real strengthening of provenance around **emptiness**.

## Finding
The new empty-menu controls do **not** close the previously exposed representative-identity boundary.

The runtime still constructs the receipt with:

```python
representatives = {
    str(representative): sorted(set(successors))
    for representative, successors in representative_successors.items()
}
```

The function annotation says `Mapping[str, Iterable[str]]`, but Python annotations are not runtime enforcement. A caller can still supply distinct hashable keys whose string renderings collide, e.g. integer `1` and string `"1"`. Both normalize to the same receipt key `"1"`; the later entry overwrites the earlier entry before `may`, `must`, and `contributors` are computed.

Therefore the live distinction remains:

```text
EMPTY LOCAL MENU != ABSENT REPRESENTATIVE
DISTINCT INPUT IDENTITY != DISTINCT STRING RENDERING
DISPLAY NORMALIZATION != PROVENANCE-PRESERVING IDENTITY
TYPE ANNOTATION != RUNTIME REFUSAL
```

### Claim classification
- **Documented fact:** the current implementation calls `str(representative)` while building the representative map.
- **Documented fact:** the latest tests cover empty local menus and empty representative families, but not heterogeneous/colliding representative keys.
- **Inference:** distinct caller keys can collapse before aggregate provenance is calculated.
- **Proposal:** refuse non-string representative identifiers, or otherwise define and test an injective identity encoding before normalization.
- **Unresolved:** whether ALEX intends this function to have a runtime-enforced string-only domain or to accept a wider identifier domain.

## Counterevidence / competing reading
The strongest boring reading is that `Mapping[str, Iterable[str]]` is the intended complete contract and all callers are trusted to honor it. Under that reading, `str()` is merely defensive/deterministic display normalization and the collision is outside the supported domain.

That reading does not eliminate the ambiguity, because ALEX contributor law treats refusal paths as first-class outcomes and this function already runtime-refuses an empty family. If string-only identity is consequential to provenance, explicit refusal would make the boundary replayable rather than relying on caller discipline.

The new empty-menu test is positive counterevidence against a broader claim that the implementation casually drops all zero-information representatives: it now explicitly preserves them. The remaining issue is specifically **identity normalization**, not emptiness.

## Discovery trace != evidence path
### Discovery trace
Previous audit exposed `str()` coercion → later PR commit added empty-menu provenance controls → re-audit asked whether the new control also closed identity collapse.

### Evidence path
Exact PR head → exact runtime source + exact tests → compare against previous audited head → bounded identity/provenance inference.

The prior audit motivated this inspection; it is not evidence for the current claim.

## Rights / egress
Only public repository text and metadata were inspected. No source corpus, private research material, page bytes, or copyrighted scan was exported. No external model received local page bytes.

## Residual fog
- No caller audit was required for this bounded contract finding, so it remains unknown whether any current production caller can actually supply non-string identifiers.
- GitBook Front Room content remained inaccessible during orientation.
- Exact-head CI for `1aadae09...` was not established in this pass; no GREEN claim is made for that head.

## Smallest next discriminators / repo-worthy moves
1. **`REPRESENTATIVE-IDENTITY-COLLISION-001`** — freeze `{1: {"green"}, "1": {"hold"}}` and require explicit refusal rather than normalization/overwrite.
2. Add the positive control `{"1": {"green"}, "01": {"hold"}}` proving two valid distinct string identifiers survive through `representatives`, `contributors`, `may`, and `must`.
3. If the function is intentionally trusted/internal and runtime validation is judged unnecessary, document `representative IDs MUST already be strings` beside the experiment contract and stop; do not grow a generic identifier subsystem.

## Receipt
- Created: 2026-09-17 17:27 America/Chicago
- Researcher/agent: ALEXDEEPDIVE automation
- Tool/model boundary: GitBook connector for orientation attempt; GitHub connector for repository evidence and durable write.
- External byte egress: none beyond public repository/API retrieval.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-17-1727-EMPTY-MENU-IDENTITY-BOUNDARY.md`
- Promotion: none
