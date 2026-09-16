# ALEXDEEPDIVE — BITEMPORAL-RELABEL-001

Status: **RESEARCH**  
Promotion: **none**

## Ground
- Question: What is the strongest newly exposed research boundary in current ALEX.2 evidence?
- Desired consequence: isolate the smallest next discriminator without promoting an experimental control into runtime or canon.
- Stop condition: one material post-packet delta, one bounded audit, 1–3 next moves.
- Task shape: **AUDIT**.
- Formation trace active: no.
- Authority/effect boundary: research packet only; no runtime, schema, policy, evidence, or authority promotion.

## World cut
- GitBook Front Room was attempted first for orientation. Connected organization access was blocked before content retrieval. This is access fog, not evidence of absence.
- ALEX.2 governance read before consequential claims: `AGENTS.md`, `skills/alex/SKILL.md`, `skills/alex/references/research-receipt.md`.
- Pre-write `main`: `dbc8d5859e80a3b4306181d52114e5dcd0565e04`.
- Material delta inspected: PR #107 advanced from previously audited `4ade4542f6fa5603d608b604436e66a0ac61da69` to `33d53f44954eb9d78fa81dcb383a378bff46979b`, 17 commits ahead, changing `experiments/partition_swap.py`, adding `experiments/relabel_scope.py`, adding its tests, and extending partition-swap tests.
- Exact-head workflow: `crucible-contract` run 35147373224 completed SUCCESS.
- Adjacent repos deliberately omitted: current frontier is fully exposed inside PR #107 plus external temporal-data terminology; no cross-repo dependency was needed.

## Finding

The prior empty-block frontier is closed: `_partition_refusal()` now explicitly returns `REFUSE / partition-empty-block` when a declared partition contains an empty block.

The strongest newly exposed boundary is the chronology semantics in `run_posthoc_relabel_chronology_control_probe()`.

Current control:

```text
observation_at = 12:00
relabel_declared_at = 12:05
later declaration => REFUSE: relabeling-postdates-observation
```

This is correct **if the attempted operation is to rewrite what labels were available at the observation time**. It is too strong if read as a general prohibition on later, explicitly retrospective comparison. A later declaration can be unavailable-at-observation while still being validly applied later as a descendant analytical view, provided the original observation remains immutable and the later declaration's own time/provenance is retained.

The temporal-database literature supplies a useful independent distinction: **valid time** concerns when a fact is true in the modeled reality, while **transaction time** concerns when that fact is stored/current in the database. Bitemporal systems preserve both. Work on retroactive/retrospective updates explicitly treats later-entered information about past states as representable rather than logically impossible. This is terminology/mechanism pressure only; it does not impose database ontology on ALEX.

Therefore:

```text
AVAILABLE AT OBSERVATION != DECLARED LATER
DECLARED LATER != INVALID FOR RETROSPECTIVE ANALYSIS
RETROSPECTIVE RELABEL != REWRITE OF PRIOR RECEIPT
OBSERVATION TIME != RELABEL DECLARATION TIME != ANALYSIS/APPLICATION TIME
```

## Evidence path

### E1 — repository observation
PR #107 exact head `33d53f44954eb9d78fa81dcb383a378bff46979b`, `experiments/relabel_scope.py`:
- the posthoc control stores `observation_at` and `relabel_declared_at`;
- if declaration time is later than observation time it refuses with `relabeling-postdates-observation`;
- its observation string is `RELABELING_CANNOT_REWRITE_PRIOR_OBSERVATION`.

Class: **observed**.

### E2 — repository observation
At the same head, `_partition_refusal()` now computes `empty_blocks` and explicitly refuses them with `partition-empty-block`.

Class: **observed**. Consequence: previous `EMPTY-BLOCK-CONTROL-001` frontier is materially closed.

### E3 — external scholarly terminology
Christian S. Jensen and Richard T. Snodgrass define temporal databases around two prevalent temporal aspects: valid time (states of modeled reality) and transaction time (past/current database states), with bitemporal databases capturing both. Richard Snodgrass's temporal SQL material likewise distinguishes these dimensions. Literature surveying temporal models explicitly discusses retrospective/retroactive updates: later changes to information about the past.

Class: **scholarly claim / documented mechanism**.  
Independence: external to ALEX implementation; conceptual ancestry between the cited temporal-database sources is shared/related, not independent corroboration.

## Claims

| ID | Claim | Class | Support | Counterevidence / limit | Status |
| --- | --- | --- | --- | --- | --- |
| C1 | Empty-block refusal is now explicit in PR #107. | observed | E2 | Experimental branch, not main/canon. | supported locally |
| C2 | Current posthoc control conflates at least two possible operations if its refusal is generalized: rewriting an old observation vs creating a later retrospective view. | inference | E1 + E3 | The function may intentionally test only rewrite semantics, as its docstring/observation wording suggests. | survivor |
| C3 | A later relabel declaration need not alter the original observation to be usable in later analysis. | proposal/inference | E3 + ALEX descendant/provenance law | No current ALEX consumer demonstrates a need for retrospective relabel application. | unresolved but testable |
| C4 | ALEX should adopt a generic bitemporal runtime. | proposal | none | Grossly exceeds current evidence. | refused |

## Contradictions and alternatives

1. **Nearest boring explanation:** there is no bug. `POSTHOC-RELABEL-CHRONOLOGY-001` may deliberately mean only “do not rewrite the earlier receipt using vocabulary that did not yet exist.” Its current observation string strongly supports this narrow reading.
2. **Stronger reading:** if downstream code later interprets `relabeling-postdates-observation` as “this relabeling may never be applied to this historical object,” the control has collapsed declaration-time provenance into application-time eligibility.
3. **No demonstrated consumer:** current evidence does not show any runtime requiring retrospective relabeling. A discriminator is earned; a generalized temporal subsystem is not.

## Discovery trace — separate from evidence path

1. Prior packet left `EMPTY-BLOCK-CONTROL-001` live.
2. Compare of old PR #107 head to current head revealed 17 new commits and a new `relabel_scope.py` surface.
3. Inspection showed empty-block refusal had landed, closing the previous frontier.
4. The newly added chronology control exposed a temporal distinction.
5. External temporal-database literature was consulted only after the code-level distinction was identified; it did not cause the repository observation.

## Pressure
- Direct counterexample to an overstrong reading: an immutable observation at T0 can remain unchanged while a relabel mapping declared at T1>T0 is used at T2 to produce a separately receipted descendant analytical view of T0.
- Nearest boring explanation: the current function already intends exactly the narrow “no rewrite” rule, so only a positive retrospective control may be missing.
- Independence/lineage: Jensen/Snodgrass temporal sources share a research lineage; do not count them as multiple independent witnesses.
- Replay impersonation: a later relabelled descendant must not impersonate the original T0 observation.
- Rights/egress: only public repository text and public scholarly/technical pages were inspected; no source corpus bytes or private research material were sent externally.

## Residual fog
- No current ALEX consumer was found that needs retrospective relabel application.
- The intended semantics of “posthoc” may be intentionally narrower than the refusal reason's wording.
- Whether `application_at` deserves durable representation is unearned until a positive control demonstrates a useful distinction.

## Smallest next discriminators

1. **RETROSPECTIVE-RELABEL-DESCENDANT-001** — freeze T0 observation, T1 relabel declaration, T2 application; require original T0 receipt byte/field identity to remain unchanged while a new descendant view records `derived_from`, declaration time, application time, and `authority: none`.
2. If that positive control adds no observable value, **rename/narrow only**: make the current refusal explicitly `cannot-rewrite-prior-observation` rather than implying global ineligibility.
3. Stop there unless a real consumer appears. Do **not** introduce generic bitemporal storage or temporal-query machinery from this specimen alone.

## Receipt
- Created: 2026-09-16 17:21 America/Chicago run window.
- Researcher/agent: ALEXDEEPDIVE automation research agent.
- External research: University of Arizona temporal database / SQL temporal materials; IBM DB2 bitemporal documentation used as terminology/mechanism pressure only.
- External byte egress: public web/repository requests only; no local corpus bytes.
- Durable location: `research/ALEX-DEEPDIVE-2026-09-16-1721-BITEMPORAL-RELABEL.md`.
- **Promotion: none**.
