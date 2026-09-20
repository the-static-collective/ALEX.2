# ALEXDEEPDIVE — INDEPENDENCE-LABEL-NOT-INDEPENDENCE-001

**Status:** RESEARCH  
**Promotion:** none  
**Research shape:** AUDIT  
**Created:** 2026-09-20 11:28 America/Chicago

## Finding

A materially new ALEX.2 frontier appeared after the preceding no-material-delta hold: draft PR #141, `RELATION-NURSERY-001`, exact inspected head `f561cf61305e25d14dab9893f048599400768497`.

The proposal correctly content-addresses the original relation proposal and refuses a pressure attachment after proposal tampering. The narrower live boundary is the pressure receipt's `interpretation="independently_supported"` value: the runtime can emit that label without carrying any independent supporting reference, dependency-family declaration, or lineage check.

Therefore the current executable surface can preserve proposal immutability while still allowing **an independence conclusion to outrun its receipt**.

```text
INDEPENDENTLY_SUPPORTED LABEL != INDEPENDENT SUPPORT
SECOND REFERENCE != INDEPENDENT ANCESTRY
PRESSURE RESULT != LINEAGE CHECK
IMMUTABLE PROPOSAL != SUFFICIENT PRESSURE RECEIPT
```

This is an audit finding about receipt sufficiency, not a claim that PR #141 currently misclassifies any historical sources.

## Ground

- **Question:** What is the strongest newly revealed ALEX research frontier since the previous ALEXDEEPDIVE packet?
- **Desired consequence:** identify one smallest executable discriminator without promoting research into canon or runtime authority.
- **Stop condition:** one material new surface, one bounded failure mode, and 1–3 smallest next moves.
- **Corpus/date:** current ALEX.2 main and open PRs as inspected 2026-09-20; GitBook Front Room used only for orientation.
- **Authority/effect boundary:** research only; no merge, canon, evidence, historical, theological, or execution authority.
- **Task shape:** AUDIT.
- **Formation trace active:** no.

## World cut

### Included

- GitBook `The Front Room` orientation surface. It restates the intended topology: stable landmark -> relevant door -> bounded traversal -> encounter -> new illumination -> changed world.
- `ALEX.2/AGENTS.md` on current main.
- `skills/alex/SKILL.md` on current main.
- `skills/alex/references/research-receipt.md` on current main.
- ALEX.2 recent commits through main `9b8a0892201e073631bceb235ffcd27b9b1b4119`.
- Open PR inventory, selecting newly created draft PR #141 as the material delta.
- PR #141 exact head `f561cf61305e25d14dab9893f048599400768497`.
- PR #141 changed files:
  - `alex_runtime/relation_nursery.py`
  - `tests/test_relation_nursery.py`
- GitHub Actions exact-head `contract` check: completed successfully.

### Deliberately omitted

- No broad adjacent-repository traversal: PR #141's strongest boundary is already decidable against ALEX's own independence/lineage law.
- No external scholarship or Wolfram computation: neither is needed to establish the executable receipt mismatch.
- No strange/symbolic hypothesis was advanced, so PRESSURE/H0 machinery was not invoked.

### Sufficiency

**Sufficient for the bounded audit.** Not sufficient to infer how future callers will use `independently_supported`, nor whether a later composition layer is intended to supply the missing lineage proof.

## Acquisitions

| ID | Provider | Item and locus | Method/time | Resolution | Rights/egress |
| --- | --- | --- | --- | --- | --- |
| A1 | GitBook | The Front Room | organization search, 2026-09-20 | orientation text | connected account; no external byte egress |
| A2 | GitHub | ALEX.2 `AGENTS.md` | exact file read | full text | repository read |
| A3 | GitHub | `skills/alex/SKILL.md` | exact file read | full text | repository read |
| A4 | GitHub | `skills/alex/references/research-receipt.md` | exact file read | full text | repository read |
| A5 | GitHub | PR #141 metadata and patches | PR/file patch reads | exact head + both changed-file patches | repository read |
| A6 | GitHub | exact-head check-runs for `f561cf...` | API read | `contract`: success | repository read |

## Evidence path

### E1 — constitutional independence rule

`skills/alex/SKILL.md` explicitly requires that agreement not be promoted to independent corroboration without lineage evidence and says to record independence as unknown when it cannot be established.

### E2 — receipt law

`research-receipt.md` repeats: agreement does not establish independence; shared ancestry should be preserved when known and `independence: unknown` used when it cannot be established.

### E3 — executable PR surface

At PR #141 head, `attach_pressure()` accepts:

```python
interpretation in (
    "not_assessed",
    "independently_supported",
    "contradicted",
    "unresolved",
)
```

but its pressure receipt carries only:

```text
proposal_ref
experiment_ref
result
observation_ref
interpretation
non_claim
```

There is no support reference for `independently_supported`, no dependency-family/ancestry field, and no executable check establishing that an alleged supporting witness is independent of the proposal's source family.

### E4 — tests

The three current tests verify:

1. a failed pressure result does not rewrite the proposal;
2. tampering with a source reference invalidates the proposal digest;
3. duplicate source references and an out-of-domain result value are refused.

No test exercises `interpretation="independently_supported"` or requires evidence for that disposition.

## Claims

| ID | Claim | Class | Supporting evidence path | Counterevidence | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | PR #141 is material new ALEX.2 work since the preceding packet. | observed | recent commit/PR inventory -> PR #141 | none found | supported |
| C2 | The proposal body is content-addressed and tamper-checked before pressure attachment. | observed | PR patch -> `_digest`, `proposal_digest`, `attach_pressure` verification | pressure receipt itself is not content-addressed | supported |
| C3 | `independently_supported` can currently be emitted without an independent-support or lineage receipt. | observed | PR patch -> allowed interpretation values + returned pressure fields | a future caller/composition layer could impose an external contract | supported for this function surface |
| C4 | ALEX's current research law requires independence claims to preserve/check lineage rather than infer independence from agreement. | documented project law | SKILL + research-receipt | none | supported |
| C5 | Therefore the smallest live frontier is receipt sufficiency for the `independently_supported` disposition. | inference | C3 + C4 | could be intentionally deferred to a later resolver | supported as audit frontier, not bug verdict |

## Contradictions and alternatives

### Nearest boring explanation

`attach_pressure()` may intentionally be a low-level structural constructor. Under that reading, `interpretation` is caller testimony, not a conclusion computed by ALEX, and a later composition layer may own validation of independence.

That explanation is viable. If it is the intended contract, the field name or receipt should make the testimony boundary explicit rather than allowing a bare `independently_supported` value to resemble an established lineage result.

### Stronger but unearned reading

It would be too strong to conclude that PR #141 launders false historical corroboration. No historical source pair was evaluated in this audit, and no caller behavior was inspected.

## Pressure / adversarial checks

- **Direct counterexample:** construct any valid proposal, then call `attach_pressure(..., result="pass", observation_ref="fixture:anything", interpretation="independently_supported")`. The current validation path has no requirement for a second support witness or independence lineage.
- **Dependency/independence check:** absent from the returned schema beyond the interpretation label itself.
- **Nearest boring explanation:** caller-owned testimony or deferred resolver, as above.
- **Replay impersonation check:** proposal digest protects proposal identity from mutation, but does not establish evidentiary identity or independence of the pressure observation.
- **Ghost-promotion check:** `non_claim` and PR boundaries correctly keep authority at none; the concern is narrower—semantic strength of one receipt field.

## Rights / egress boundary

No source corpora, private material, scans, or local page bytes were inspected or exported. This run used connected GitBook/GitHub text surfaces only. No external model egress of repository source bytes was required for scholarship or computation.

## Residual fog

- Whether `interpretation` is intended as researcher testimony, validated ALEX conclusion, or merely an enum has not yet been frozen in an executable contract.
- Whether a future store/composition layer already plans to resolve `observation_ref` and dependency ancestry is unknown.
- Exact-head GitHub Actions `contract` is GREEN; this audit therefore identifies a semantic frontier not covered by the present tests, not a failing CI state.

## Smallest next discriminators

1. **`INDEPENDENCE-REQUIRES-LINEAGE-001`** — attempt `interpretation="independently_supported"` with only the current opaque `observation_ref`; require either explicit refusal or downgrade to `independence: unknown`.
2. Add one positive control where a separately referenced support receipt carries an explicit dependency/ancestry declaration sufficient for the owning layer to establish independence; only then permit an established-independence disposition.
3. If `interpretation` is intentionally testimony-only, rename/type it accordingly (for example `interpretation_testimony`) and preserve `independence_status: unknown` separately. Stop there rather than growing a generic corroboration engine.

## Discovery trace

Separate from evidence support:

```text
Front Room orientation
  -> current ALEX governance
  -> recent main delta check
  -> newly created PR #141
  -> exact changed-file audit
  -> independence-label receipt mismatch
```

The discovery order explains why this frontier was inspected. It is not evidence for the finding; the evidence path is E1–E4 above.

## Receipt

- **Created:** 2026-09-20 11:28 America/Chicago
- **Researcher/agent:** ALEXDEEPDIVE
- **Tool/model boundary:** connected GitBook + GitHub inspection; no local checkout claimed
- **External byte egress:** none beyond connected service reads
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-20-1128-INDEPENDENCE-LABEL-NOT-INDEPENDENCE.md`
- **Promotion:** none
