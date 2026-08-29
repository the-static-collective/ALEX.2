# ALEX Research Formation Spine v0 + CHRONOBODY-001

**Status:** approved architecture / implementation not yet claimed  
**Date:** 2026-08-28  
**Owner:** ALEX.2  
**Primary law:** **BRANCH IS POSSIBILITY. SHA IS IDENTITY. REGISTRY IS MEMORY. ROUTING IS NOT PROMOTION.**

## 1. Purpose

ALEX now has enough executable descendants that the next problem is composition, not invention.

The repository already has a constituted evidence/derivation floor on `main`, while several useful research organs exist as tested but unmerged implementations. Requiring every useful organ to merge merely to become callable collapses developmental possibility into constituted present.

This design introduces two coupled structures:

1. **ALEX Research Formation Spine v0** — a bounded composition path that preserves stage receipts and formation ancestry without becoming a truth machine or authority router.
2. **`CHRONOBODY-001`** — a time-addressed organ registry/resolver that lets explicitly registered exact-SHA bodies participate without silently becoming present, constitutional, or authoritative.

The motivating law is:

> **DO NOT REQUIRE EVERY USEFUL POSSIBILITY TO BECOME THE PRESENT BEFORE IT CAN PARTICIPATE.**
>
> **A POSSIBILITY MAY PARTICIPATE ONLY THROUGH AN EXACT, DECLARED, RECEIPTED BODY-TIME.**

## 2. Non-collapse laws

```text
branch name != executable identity
branch head != stable body-time
executable != landed
landed != constitutional
constitutional != authoritative
route != promote
route != admit
same organ family != same organ body
same output != same body-time
current surface != formation history
replay != original occurrence
registry membership != execution permission
verification receipt != semantic truth
```

Existing ALEX laws remain unchanged:

```text
discovery path != evidence path
similarity != genealogy
agreement != independent corroboration
interest != evidence
projection != source != authority
```

## 3. Time enters the body

Git already preserves developmental ancestry. `CHRONOBODY-001` makes one bounded portion of that ancestry available to runtime provenance.

### 3.1 Constituted present

`main` is the repository's **constituted present**.

Ordinary `PRESENT_ONLY` execution is constrained to the exact clean `main` checkout currently running. The resolved checkout SHA is receipted before execution.

### 3.2 Developmental possibility

A branch is a **developmental possibility**, not an executable identity.

The branch name may be stored for navigation, but a non-present body must name an exact commit SHA before it can be addressed.

### 3.3 Exact body-time

```text
body_time_id := organ_id + "@" + exact_commit_sha
```

Examples:

```text
far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4
binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e
```

Branch labels are descriptive ancestry only.

## 4. Five body states

### `PRESENT`

Part of the constituted current body. May run under `PRESENT_ONLY` or `EXPERIMENTAL`.

### `INCUBATING`

Executable but deliberately not constituted as present. May run only under `EXPERIMENTAL` and only at the exact registered SHA.

### `HELD`

Known and visible, but not executable.

### `RETIRED`

Historical body. May run only under explicit exact `REPLAY` if locally materialized and contract-compatible.

### `RECONSTITUTED`

Fresh attributable descendant of an older implementation that was rebuilt rather than blindly rebased/copied. In v0 it follows `INCUBATING` execution rules until separately promoted.

## 5. Execution modes

### `PRESENT_ONLY`

Default.

- only `PRESENT` bodies;
- no experimental fallback;
- no branch lookup;
- no historical replay.

### `EXPERIMENTAL`

Explicit opt-in.

- `PRESENT`, `INCUBATING`, and `RECONSTITUTED` are eligible;
- non-present bodies require exact SHA;
- receipts must visibly preserve non-present status;
- execution grants no promotion.

### `REPLAY`

Explicit historical mode.

- exact `body_time_id` required;
- `RETIRED` may execute;
- no `latest` selection;
- execution occurrence remains new even though implementation body is historical.

## 6. Registry contract

Schema family:

```text
alex.chronobody-registry/v0
```

The registry is committed reviewable memory. It does not materialize code and is not a process supervisor.

### 6.1 FAR-SIDE body

```json
{
  "organ_id": "far-side-pass",
  "body_time_id": "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4",
  "status": "INCUBATING",
  "capabilities": ["far_side_pressure"],
  "source": {
    "repo": "the-static-collective/ALEX.2",
    "branch": "feature/far-side-pass-m0",
    "sha": "52c678767017c170506ce1895d3a610b6ef115b4"
  },
  "runtime": {
    "contract": "python-json-stdio/v0",
    "entrypoint": "tools/far_side_lab.py"
  },
  "verification": {
    "workflow": "crucible-contract",
    "run_id": 33219406091,
    "result": "GREEN"
  },
  "authority": "none",
  "parents": []
}
```

### 6.2 BINOCULAR body

```json
{
  "organ_id": "binocular-recursion",
  "body_time_id": "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e",
  "status": "INCUBATING",
  "capabilities": ["binocular_formation_audit"],
  "source": {
    "repo": "the-static-collective/ALEX.2",
    "branch": "impl/binocular-recursion-001",
    "sha": "c26620efc3c601eb0686825e1cfcbe1f1951f49e"
  },
  "runtime": {
    "contract": "python-json-stdio/v0",
    "entrypoint": "tools/run_binocular_recursion.py"
  },
  "verification": {
    "workflow": "crucible-contract",
    "run_id": 33219240427,
    "result": "GREEN"
  },
  "authority": "none",
  "parents": []
}
```

### 6.3 Registry invariants

For every non-`PRESENT` entry:

- repository is required;
- full 40-character lowercase hex SHA is required;
- `body_time_id` must end in that exact SHA;
- branch is optional navigation only;
- `authority` is exactly `none` in v0;
- runtime contract is allowlisted;
- entrypoint is repository-relative and traversal-free;
- no shell string exists;
- changed SHA creates a new body entry rather than mutating old identity.

Lineage may carry exact parent `body_time_id` values. Developmental ancestry grants no compatibility, truth, authority, or promotion.

## 7. Local materialization boundary

Runtime v0 does **not** clone, fetch, checkout, pull, merge, reset, or clean Git state.

A non-present body must already exist as an operator/CI supplied local checkout. The run envelope supplies machine-local materialization paths:

```json
{
  "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4": "/local/far-side",
  "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e": "/local/binocular"
}
```

Before execution the launcher verifies:

1. path exists;
2. path is a Git checkout of the registered repository;
3. `HEAD` equals registered SHA;
4. checkout is clean;
5. entrypoint exists below root;
6. runtime contract is allowed.

Mismatch is refusal. Runtime never repairs the checkout.

## 8. Invocation contract

V0 admits exactly:

```text
python-json-stdio/v0
```

Meaning:

- direct current Python interpreter;
- one validated repository-relative script;
- no shell;
- JSON stdin;
- one JSON stdout value;
- stderr preserved separately;
- explicit timeout;
- non-zero exit is visible execution failure;
- input/output receive deterministic SHA-256 digests.

Registry entries cannot inject flags or environment mutation in v0.

## 9. Resolver behavior

Consumes:

```text
capability
body_mode
optional organ_id
optional body_time_id
registry
```

Returns:

```text
ROUTED
AMBIGUOUS
UNAVAILABLE
REFUSED
```

Rules:

1. `PRESENT_ONLY` excludes non-present bodies.
2. `EXPERIMENTAL` admits only eligible states; no preference for incubating over present.
3. `REPLAY` requires exact `body_time_id`.
4. Explicit body still must satisfy capability and mode.
5. Exactly one eligible body => `ROUTED`.
6. More than one without explicit disambiguation => `AMBIGUOUS`.
7. No newest-SHA, timestamp, branch, or registry-order tie-break.
8. `HELD` never routes.
9. Registry absence => `UNAVAILABLE`.
10. Route cannot change `authority: none`.

## 10. Execution receipt

Schema family:

```text
alex.chronobody-execution/v0
```

Minimum receipt:

```json
{
  "receipt_type": "alex.chronobody-execution/v0",
  "organ_id": "far-side-pass",
  "body_time_id": "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4",
  "organ_status": "INCUBATING",
  "body_mode": "EXPERIMENTAL",
  "source_repo": "the-static-collective/ALEX.2",
  "source_sha": "52c678767017c170506ce1895d3a610b6ef115b4",
  "runtime_contract": "python-json-stdio/v0",
  "entrypoint": "tools/far_side_lab.py",
  "input_digest": "sha256:<digest>",
  "output_digest": "sha256:<digest>",
  "execution_state": "COMPLETED",
  "exit_code": 0,
  "authority": "none"
}
```

`COMPLETED` means process-contract completion only. It says nothing about truth, support, canon, admission, publication, or promotion.

## 11. Research Formation Spine v0

The first executable spine is intentionally fully time-addressed:

```text
CONSTITUTED MAIN
  CHRONOBODY registry + resolver + composition law
                  |
                  v
FAR-SIDE PASS @ 52c6787...  [INCUBATING]
                  |
         execution receipt
                  |
       DISCOVERY_TRIGGER_ONLY bridge
                  |
                  v
BINOCULAR @ c26620e...      [INCUBATING]
                  |
         execution receipt
                  |
                  v
RECEIPTED RESEARCH FORMATION RESULT
```

This is the first proof of the larger law: two off-main organs may participate in one present ALEX run without either becoming `PRESENT`.

### 11.1 Why FAR-SIDE remains incubating

- design/plan are already constituted on `main`;
- implementation is deliberately under `experiments/`;
- exact head `52c678...` is green;
- its PR withholds public task-shape/Crucible/skill promotion.

Its experimental location is therefore useful information, not technical debt to erase.

### 11.2 Why BINOCULAR also remains incubating in the first proof

BINOCULAR is a serious candidate for later constitution, but first proof does not need to settle that question.

Exact head `c26620e...` already has:

- pure evaluator;
- JSON file/stdin runner;
- hostile tests;
- successful `crucible-contract` run `33219240427`.

Routing it as `INCUBATING` keeps "usable" distinct from "merged" and makes future promotion a separate PR-completion decision.

## 12. The only v0 semantic bridge

FAR-SIDE output does not automatically become evidence or BINOCULAR support.

After FAR-SIDE completes, the spine computes a digest of its Chronobody execution receipt and adds that receipt reference only to BINOCULAR's `discovery_trigger_refs`.

```text
FAR-SIDE execution receipt
          |
          v
DISCOVERY_TRIGGER_ONLY
          |
          v
BINOCULAR discovery_trigger_refs
```

It must not be inserted into:

```text
support_refs
compression.claim_support_refs
admitted_premise_refs
```

This is a deliberate executable seam for:

> **DISCOVERY METHOD != EVIDENCE METHOD**

If the supplied BINOCULAR case launders that same trigger into support, the BINOCULAR organ should refuse under its own existing contract.

The spine composes provenance, not meanings: it does not map FAR-SIDE survivor fields into BINOCULAR compression/expansion semantics.

## 13. App-facing clarity

Normal UI should expose temporal state without making Git the user's primary mental model.

```text
ALEX BODY

PRESENT
  Crucible
  Derivation
  Projection
  Chronobody

INCUBATING
  FAR-SIDE     GREEN  @52c6787
  BINOCULAR    GREEN  @c26620e

HELD
  MADDCL0WN research method
  Decoder-Probe research packet

RETIRED
  exact historical bodies, replay-only
```

Organ detail shows:

```text
organ family
body state
exact SHA
branch / ancestry
verification receipt
capabilities
runtime contract
authority
```

No incubating organ may be presented simply as `enabled` without state.

## 14. Hostile controls

### `BRANCH-DRIFT-001`

Registry SHA A, local checkout SHA B -> `REFUSED / BODY_SHA_MISMATCH`.

### `DIRTY-BODY-001`

SHA matches but checkout has uncommitted changes -> `REFUSED / DIRTY_BODY`.

### `LATEST-WINS-001`

Two eligible bodies provide same capability -> `AMBIGUOUS`.

### `STATUS-LAUNDERING-001`

Incubating result presented as present -> receipt/UI contract failure.

### `ROUTE-PROMOTION-001`

Successful experimental execution interpreted as promotion -> refusal; registry unchanged.

### `OUTPUT-IDENTITY-001`

Two body-times produce identical output -> output equality allowed; execution identities remain distinct.

### `REPLAY-IMPERSONATION-001`

Historical body replay -> new execution occurrence referencing historical body.

### `HELD-EXECUTION-001`

Caller requests held body -> `REFUSED / BODY_NOT_EXECUTABLE`.

### `SHELL-INJECTION-001`

Registry attempts path traversal/shell semantics -> validator refusal before invocation.

### `DISCOVERY-LAUNDERING-001`

FAR-SIDE receipt appears in BINOCULAR support path -> BINOCULAR refusal; the spine must preserve it rather than normalize it away.

## 15. Relationship to LOADOUT and LOADIN.STEAD

```text
LOADOUT
  chooses required capability set
      |
      v
CHRONOBODY
  resolves exact registered body-time
      |
      v
ORGAN EXECUTION
      |
      v
ALEX formation / derivation
      |
      v
LOADIN.STEAD (optional later)
  routes a new outward occurrence
```

Ownership remains separate:

- LOADOUT does not choose truth.
- CHRONOBODY does not choose promotion or authority.
- Routability grants no authority.
- ALEX derivation does not admit external consequence.
- LOADIN.STEAD route still does not admit.

## 16. Relationship to GitHub

GitHub stores/reports body ancestry and verification evidence. It is not queried during v0 execution.

The committed registry may preserve workflow/run IDs. Runtime trusts the committed registry plus exact locally verifiable checkout identity.

CI may materialize pinned SHAs in separate `actions/checkout` directories to prove real branch-time execution. That is test fixture preparation, not runtime Git mutation.

A later artifact-backed implementation may replace local checkouts with immutable CI packages without changing the body-time model.

## 17. Promotion discipline

`CHRONOBODY-001` begins as an ALEX-local pattern.

Do not extract a new repo or eCODE-wide law because the metaphor is attractive.

Cross-project promotion should require:

1. a real ALEX run using at least one pinned incubating body;
2. hostile branch-drift refusal;
3. historical replay specimen;
4. a second materially different project with the same need;
5. evidence that a shared protocol removes duplication rather than creating a master ontology.

Until then:

> **ALEX IS THE PROVING GROUND.**

## 18. First executable target

Build only:

1. registry parser/validator;
2. deterministic body resolver;
3. local exact-SHA/repository/clean-checkout verification;
4. `python-json-stdio/v0` launcher;
5. execution receipts;
6. exact FAR-SIDE + BINOCULAR registry entries;
7. CI materialization of both exact SHAs;
8. actual off-main execution proofs for both;
9. Research Formation Spine runner with `DISCOVERY_TRIGGER_ONLY` bridge;
10. hostile tests for identity, ambiguity, dirt, held/replay modes, route/promotion separation, and discovery laundering.

Do not implement:

- Git clone/fetch/checkout in runtime;
- arbitrary shell execution;
- remote workers;
- background supervision;
- automatic branch discovery;
- newest-body selection;
- automatic merge/promotion;
- authority changes;
- network/model calls;
- Dogram dependency;
- MADDCL0WN execution before an executable contract exists;
- BOOKROOM reconstruction;
- cross-project Chronobody service.

## 19. Build sequence

```text
A1  implement CHRONOBODY registry + resolver on constituted main

A2  register FAR-SIDE@52c6787 as INCUBATING
    register BINOCULAR@c26620e as INCUBATING

A3  CI materializes both exact bodies separately
    -> prove both execute through CHRONOBODY

A4  implement Research Formation Spine
    -> FAR-SIDE receipt becomes discovery trigger only
    -> BINOCULAR audits supplied formation

A5  exact-head hostile verification + PR Completion

C1  later Decoder-Probe / MADDCL0WN executable descendants
    -> natural new incubating organs

B1  later reconstitute BOOKROOM on fresh main
    -> source-bearing body feeding the spine
```

Promotion of FAR-SIDE or BINOCULAR to `PRESENT` is not part of this build sequence.

## 20. Seal

```text
MAIN IS CONSTITUTED PRESENT.
BRANCH IS DEVELOPMENTAL POSSIBILITY.
SHA IS EXECUTABLE IDENTITY.
REGISTRY IS MEMORY.
ROUTING IS NOT PROMOTION.
REPLAY IS NOT ORIGINAL OCCURRENCE.
```

And the broader build law:

> **DON'T IMPLEMENT THE BACKLOG. IMPLEMENT THE RELATIONS THAT LET THE BACKLOG COMPOSE.**

`CHRONOBODY-001` adds time to the body only by making time attributable. If the exact body-time cannot be named and receipted, it does not get to act.