# ALEXDEEPDIVE — IDENTITY-COERCION-NOT-PROVENANCE

**Status:** RESEARCH  
**Promotion:** none  
**Created:** 2026-09-17 11:21 America/Chicago  
**Task shape:** AUDIT

## Ground

- **Question:** What is the strongest newly exposed research frontier in current ALEX.2?
- **Desired consequence:** one bounded discriminator, not a runtime promotion.
- **Stop condition:** identify a concrete current-head behavior capable of defeating the provenance guarantee of the newest live specimen.
- **Authority/effect boundary:** research only; no canon, runtime authority, merge authority, evidence promotion, or causal promotion.
- **Formation trace active:** no. Discovery trace is recorded separately below.

## Orientation

The Static Collective GitBook Front Room was attempted first. Connected organization discovery was blocked before Front Room content could be retrieved. This is **access fog, not absence**. No GitBook claim is formed from the failed retrieval.

Before consequential claims, this run read:

- `ALEX.2/AGENTS.md` on current `main`;
- `skills/alex/SKILL.md` on current `main`;
- `skills/alex/references/research-receipt.md` on current `main`.

Those surfaces require provenance-layer separation, first-class refusal, discovery/evidence separation, and no silent authority promotion.

## World cut

### Included

- ALEX.2 `main` pre-write head: `9b7fccaef9d942933e7e853a7f18264588869c7c`.
- ALEX.2 issue #118, `MENU-PROVENANCE-001`.
- ALEX.2 PR #121, exact inspected head `ec5725a243bd0b27b766e6714d6b293d2c413e00`.
- PR #121 patches for `alex_runtime/menu_provenance.py`, `tests/test_menu_provenance.py`, and `research/MENU-PROVENANCE-001.md`.
- Exact-head GitHub Actions witness: `crucible-contract` run `35243812084`, completed `success`.

### Deliberately omitted

No broad adjacent-repository roam. Dogram is relevant as upstream formation for #118, but the new failure is directly visible in the ALEX implementation and does not require a new Dogram claim. No external scholarship or Wolfram computation is required for this Python identity/coercion audit.

### Missing / inaccessible

- GitBook Front Room content: connector blocked.

**Sufficiency:** sufficient for the bounded audit below.

## Material delta

Since the previous ALEXDEEPDIVE packet, ALEX.2 gained a materially new live implementation surface: PR #121 `MENU-PROVENANCE-001`.

The specimen's stated purpose is to preserve representative-local successor provenance so an aggregate `may` union cannot impersonate a possibility owned by every representative. It returns representative-local families, `may`, `must`, a successor-to-contributor relation, and `authority: none`.

This is a real delta and supersedes the previous no-material-delta hold as the strongest current audit target.

## Finding

The implementation currently normalizes every representative identity with:

```python
str(representative)
```

inside a dictionary comprehension *before* it computes `may`, `must`, and contributor provenance.

Therefore distinct supplied representatives whose string forms collide can silently collapse into one representative.

Hostile finite control:

```python
{
    1: {"green"},
    "1": {"hold"},
}
```

Python mappings can contain integer `1` and string `"1"` as distinct keys. The current comprehension maps both to the same output key `"1"`. One representative-local family overwrites the other before the aggregate and contributor calculations are made.

So the failure is stronger than cosmetic label loss: under this hostile input, the receipt can lose a supplied representative **and its successor possibility**, changing the computed `may`, `must`, and contributor relation.

```text
DISTINCT INPUT IDENTITY != DISTINCT STRING RENDERING
NORMALIZATION != PROVENANCE-PRESERVING IDENTITY
DISPLAY LABEL != REPRESENTATIVE KEY
```

## Claims

| ID | Claim | Class | Evidence path | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #121 is a new material ALEX surface implementing menu provenance. | observed | GitHub PR #121 metadata + patches | PR remains unmerged; this is a live branch surface, not `main` runtime authority. | supported |
| C2 | The implementation applies `str(representative)` before downstream set calculations. | observed | exact PR #121 patch, `alex_runtime/menu_provenance.py` | none observed at inspected head | supported |
| C3 | Two distinct input keys can collide after that coercion and silently overwrite a representative family. | inference from documented code semantics | C2 + finite hostile control | The intended input domain may implicitly be string-only, but the function signature does not declare that restriction and no refusal freezes it. | supported within declared Python input surface |
| C4 | Such a collision can change `may`, `must`, and contributor provenance, not merely presentation. | inference | downstream calculations consume the already-coerced `representatives` dictionary | If callers are externally guaranteed to provide collision-free strings, hostile input is outside their domain; that guarantee is not established by the inspected specimen. | supported / domain boundary unresolved |
| C5 | Exact-head repository CI is GREEN. | observed | Actions run `35243812084` at `ec5725a...` | GREEN does not cover the hostile identity-collision case. | supported |

## Direct counterevidence and competing readings

### Reading A — implementation hole

The public Python function accepts `Mapping[str, Iterable[str]]` by annotation, but Python annotations are not runtime enforcement. Because the function actively coerces keys rather than refusing malformed identity types, it appears to claim normalization behavior. On this reading, silent identity collision violates the specimen's core purpose: preserve which representative contributed which possibility.

### Reading B — fixture-local closed domain

The intended experimental domain may be strictly string representative IDs supplied only by controlled fixtures. On that reading, integer/string collision is malformed input outside the experiment, and no generic identity system is needed.

Reading B does **not** erase the frontier. It makes the smallest fix even smaller: freeze and refuse non-string representative identities rather than silently coercing them.

## Nearest boring explanation

`str(representative)` was likely added as deterministic output normalization, not as an intended identity quotient. The ordinary coding convenience accidentally sits on an identity-bearing provenance boundary.

No evidence suggests a deeper ontology problem.

## Pressure

- **Direct counterexample:** `{1: {"green"}, "1": {"hold"}}`.
- **Dependency/independence:** the failure is local to PR #121 and does not depend on Dogram semantics once the representative mapping reaches `summarize_menu()`.
- **Replay impersonation:** not implicated.
- **Rights/egress:** repository text only; no corpus bytes or private source material egressed.
- **Authority:** `authority: none` remains intact; this audit does not promote the specimen.
- **Serendipity trap:** none. The discriminator follows directly from the identity-preservation purpose and exact implementation.

## Discovery trace

| ID | From | To | Move | Role | Reason |
| --- | --- | --- | --- | --- | --- |
| D1 | current open ALEX PRs | PR #121 | newest material implementation | motive | changed after prior packet |
| D2 | PR #121 purpose | implementation patch | inspect provenance-bearing transformation | discriminator | core guarantee depends on representative identity surviving |
| D3 | `str(representative)` | hostile mixed-type keys | adversarial collision | counterexample | tests whether normalization preserves identity |

**Evidence-path boundary:** D1 explains why this run looked at #121. Claims C2–C4 are supported by the exact implementation patch and the finite counterexample, not by discovery recency.

## Residual fog

- Whether the intended runtime contract is strictly `str -> iterable[str]` or intentionally accepts coercible identifiers is not explicitly frozen by the inspected tests.
- Successor identities are also normalized only indirectly through `sorted(set(successors))`; malformed/non-string successor inputs may expose a separate type/identity boundary, but that is not needed to establish this run's finding.
- PR #121 is live and mergeable but not merged; future head movement may close this audit before landing.

## Smallest next discriminators / repo-worthy moves

1. **`REPRESENTATIVE-IDENTITY-COLLISION-001`** — freeze `{1: {"green"}, "1": {"hold"}}` and require explicit `REFUSE` rather than coercion or overwrite.
2. If the intended domain is string-only, replace `str(representative)` with validation that every representative key is already a string and preserve it exactly. Do not build a generic identifier framework.
3. Add a positive control proving two distinct valid string IDs remain distinct through `representatives`, `contributors`, `may`, and `must`; stop if that closes the boundary.

## Receipt

- Researcher/agent: ALEXDEEPDIVE
- Tool/model boundary: connected GitBook attempt; connected GitHub repository/PR/Actions inspection; no Wolfram needed.
- External byte egress: none beyond ordinary connector/API requests; no local corpus bytes sent to external models.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-17-1121-IDENTITY-COERCION-NOT-PROVENANCE.md`
- Promotion: none
