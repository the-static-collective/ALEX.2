# ALEX Research Formation Spine v0 + CHRONOBODY-001

**Status:** approved architecture / implementation not yet claimed  
**Date:** 2026-08-28  
**Owner:** ALEX.2  
**Primary law:** **BRANCH IS POSSIBILITY. SHA IS IDENTITY. REGISTRY IS MEMORY. ROUTING IS NOT PROMOTION.**

## 1. Purpose

ALEX now has enough executable organs that the next problem is composition, not invention.

The current repository already contains or has separately proven executable descendants for Blind Crucible, `RELATION-DERIVATION-001`, LOADOUT handshake, projection invariance/break, LOADIN.STEAD, BINOCULAR-RECURSION, FAR-SIDE PASS m0, and other bounded research evaluators. Treating every useful experimental organ as something that must first merge into `main` creates the wrong pressure: developmental possibility gets flattened into constituted present merely to make it callable.

This design introduces two coupled structures:

1. **ALEX Research Formation Spine v0** — a small composition path that turns a supplied research formation into attributable stage receipts without creating a truth machine or authority router.
2. **`CHRONOBODY-001`** — a time-addressed organ registry and resolver that permits explicitly registered, exact-SHA experimental bodies to participate without silently becoming present, constitutional, or authoritative.

The motivating insight is:

> **DO NOT REQUIRE EVERY USEFUL POSSIBILITY TO BECOME THE PRESENT BEFORE IT CAN PARTICIPATE.**
>
> **A POSSIBILITY MAY PARTICIPATE ONLY THROUGH AN EXACT, DECLARED, RECEIPTED BODY-TIME.**

## 2. Non-collapse laws

This design extends the existing ALEX floor with the following local distinctions:

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

Existing laws remain unchanged, including:

```text
discovery path != evidence path
similarity != genealogy
agreement != independent corroboration
interest != evidence
projection != source != authority
```

## 3. Time enters the body

Git already preserves developmental ancestry, but ordinary application architecture usually treats that ancestry as build plumbing. `CHRONOBODY-001` makes one bounded part of it explicit in runtime provenance.

### 3.1 Constituted present

`main` is the repository's **constituted present**.

This does not mean every commit on `main` is eternally canonical. It means ordinary `PRESENT_ONLY` execution is constrained to the exact clean `main` checkout that is currently running, and that checkout SHA is receipted before execution.

### 3.2 Developmental possibility

A branch is a **developmental possibility**, not an executable identity.

A human-facing branch name may be stored for navigation, but an `INCUBATING`, `HELD`, `RETIRED`, or `RECONSTITUTED` body must name an exact commit SHA before it can be addressed.

### 3.3 Exact body-time

The executable identity is:

```text
body_time_id := organ_id + "@" + exact_commit_sha
```

Examples:

```text
far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4
binocular-recursion@<resolved-main-sha>
```

The branch label is descriptive ancestry only.

## 4. Five body states

`CHRONOBODY-001` uses exactly five body states in v0.

### `PRESENT`

The organ is part of the constituted current body. It may run in `PRESENT_ONLY` or `EXPERIMENTAL` mode. Runtime resolves and receipts the exact clean checkout SHA before invocation.

### `INCUBATING`

The organ is executable but deliberately not constituted as present. It may run only in `EXPERIMENTAL` mode and only at the exact registered SHA.

### `HELD`

The body is known and visible but not executable. Research packets, design branches, or implementations awaiting sufficient proof may live here.

### `RETIRED`

The body is no longer a current execution candidate. It may be invoked only in explicit `REPLAY` mode when the exact historical body is locally materialized and its original contract remains satisfiable.

### `RECONSTITUTED`

A fresh body is an attributable descendant of an older body whose implementation was rebuilt rather than blindly rebased or copied. In v0 it follows `INCUBATING` execution rules until separately promoted to `PRESENT`.

## 5. Execution modes

The normal application must make the temporal mode visible.

### `PRESENT_ONLY`

Default mode.

- only `PRESENT` bodies are eligible;
- no experimental fallback;
- no implicit branch lookup;
- no historical replay.

### `EXPERIMENTAL`

Explicit opt-in.

- `PRESENT`, `INCUBATING`, and `RECONSTITUTED` bodies may be eligible;
- every non-present body must be exact-SHA pinned;
- output receipts must visibly record the non-present state;
- experimental execution grants no semantic or authority promotion.

### `REPLAY`

Explicit historical mode.

- caller must request an exact `body_time_id`;
- `RETIRED` bodies may be eligible;
- no "latest" resolution;
- replay remains a new execution occurrence over a historical implementation body.

## 6. Registry contract

The registry is committed, reviewable memory. It is not a process supervisor and does not materialize code.

Proposed schema family:

```text
alex.chronobody-registry/v0
```

Illustrative entry:

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

### 6.1 Registry invariants

For every non-`PRESENT` entry:

- `source.repo` is required;
- `source.sha` is a full 40-character lowercase hex commit SHA;
- `body_time_id` must end in that exact SHA;
- branch is optional descriptive navigation and never used as identity;
- `authority` must be `none` in v0;
- runtime contract must be from an explicit allowlist;
- entrypoint must be a repository-relative path without `..` traversal;
- no shell command string is accepted;
- a changed SHA is a new body entry, not an in-place identity mutation.

For lineage:

- `parents` contains zero or more exact prior `body_time_id` values;
- parentage records developmental ancestry only;
- ancestry does not grant compatibility, correctness, authority, or promotion.

## 7. Local materialization boundary

`CHRONOBODY-001` v0 does **not** clone, fetch, checkout, pull, merge, or otherwise mutate Git state during a research run.

That is deliberate.

A routable non-present body must already exist as an operator-supplied local checkout/materialization. The run envelope supplies a machine-local map:

```json
{
  "far-side-pass@52c6787...": "/local/path/to/materialized/body"
}
```

The launcher then verifies before execution:

1. path exists;
2. it is a Git checkout of the registered repository;
3. `HEAD` equals the exact registered SHA;
4. checkout is clean;
5. registered entrypoint exists under that root;
6. runtime contract is allowed.

Any mismatch is a refusal. There is no implicit repair or checkout.

This keeps Git transport/deployment outside the research semantics.

## 8. Invocation contract

V0 admits one execution adapter:

```text
python-json-stdio/v0
```

It means:

- invoke the current Python interpreter directly;
- invoke one validated repository-relative script path;
- no shell;
- JSON input on stdin;
- one JSON value on stdout;
- stderr preserved separately;
- non-zero process exit is a visible execution failure;
- bounded timeout is explicit in the run request;
- input and output bytes receive deterministic SHA-256 digests.

The registry cannot add arbitrary flags or environment mutation in v0.

## 9. Resolver behavior

The resolver consumes:

```text
capability
body_mode
optional explicit organ_id
optional explicit body_time_id
registry
```

and returns one of:

```text
ROUTED
AMBIGUOUS
UNAVAILABLE
REFUSED
```

Rules:

1. `PRESENT_ONLY` filters out every non-`PRESENT` body.
2. `EXPERIMENTAL` admits only the states defined above; it never silently prefers incubating over present.
3. `REPLAY` requires exact `body_time_id`.
4. If an explicit `body_time_id` is supplied, capability and mode must still agree.
5. If exactly one eligible body remains, return `ROUTED`.
6. If more than one eligible body remains and caller did not explicitly disambiguate, return `AMBIGUOUS`.
7. No "newest SHA wins" or branch-name tie-break exists.
8. `HELD` never routes.
9. Registry absence is `UNAVAILABLE`, not permission to improvise.
10. Routing never changes `authority: none`.

This follows the existing LOADIN.STEAD discipline: deterministic routing may identify a door/body without granting admission or consequence.

## 10. Execution receipt

Every invocation produces a receipt even when the organ refuses or fails.

Proposed family:

```text
alex.chronobody-execution/v0
```

Minimum fields:

```json
{
  "receipt_type": "alex.chronobody-execution/v0",
  "organ_id": "far-side-pass",
  "body_time_id": "far-side-pass@52c6787...",
  "organ_status": "INCUBATING",
  "body_mode": "EXPERIMENTAL",
  "source_repo": "the-static-collective/ALEX.2",
  "source_sha": "52c6787...",
  "runtime_contract": "python-json-stdio/v0",
  "entrypoint": "tools/far_side_lab.py",
  "input_digest": "sha256:...",
  "output_digest": "sha256:...",
  "execution_state": "COMPLETED",
  "exit_code": 0,
  "authority": "none"
}
```

`COMPLETED` means only that the registered organ process completed under the stated contract. It does not mean its research conclusion is true, supported, admitted, canonical, or promoted.

## 11. Research Formation Spine v0

The first spine is intentionally narrow:

```text
SUPPLIED RESEARCH FORMATION
          |
          v
   capability request
          |
          v
      CHRONOBODY
 exact body-time resolution
          |
          v
     FAR-SIDE PASS
 candidate survivor / no-new-dimension / refusal
          |
          v
 BINOCULAR-RECURSION
 formation-law audit
          |
          v
 optional ALEX derivation
          |
          v
 RECEIPTED RESEARCH PACKET
```

The composition itself is not a new epistemic authority.

### 11.1 FAR-SIDE as the first temporal organ

FAR-SIDE PASS m0 is the canonical first `INCUBATING` body because:

- its design and plan are already constituted on `main`;
- its executable implementation lives under `experiments/`;
- exact head `52c678767017c170506ce1895d3a610b6ef115b4` has a successful `crucible-contract` workflow;
- it is only one commit behind the current observed `main` at design time;
- its own PR explicitly withholds public task-shape, Crucible, and skill-trigger promotion.

Therefore it demonstrates the desired law more cleanly if it remains experimental while becoming callable through an exact-SHA route.

### 11.2 BINOCULAR as constituted formation audit

BINOCULAR-RECURSION is a stronger candidate for `PRESENT` because it audits whether a supplied research formation preserves already-approved ALEX distinctions: discovery/support separation, premise admission, live consequence preservation, attributable updates, and frozen authority.

Its integration remains a normal PR-completion decision. `CHRONOBODY-001` does not authorize that merge.

### 11.3 Derivation remains derivation

`RELATION-DERIVATION-001` remains the semantic relation gate. A FAR-SIDE survivor or lawful BINOCULAR formation is not automatically support.

```text
interesting survivor != evidence
lawful formation != truth
lawful formation != SUPPORTS
```

## 12. App-facing clarity

The application should expose temporal state without exposing Git mechanics as the primary UI.

Conceptual body panel:

```text
ALEX BODY

PRESENT
  Crucible
  Derivation
  Projection
  Binocular (after separate landing)

INCUBATING
  FAR-SIDE    GREEN   @52c6787

HELD
  MADDCL0WN research method
  Decoder-Probe research packet

RETIRED
  historical bodies available only by exact replay
```

Clicking an organ should show:

```text
organ family
body state
exact SHA
birth branch / ancestry
verification receipt
capabilities
runtime contract
authority
```

The app must not label a routed incubating organ simply as "enabled" without its state.

## 13. Confusion controls

The system is specifically designed to prevent temporal/body confusion.

### `BRANCH-DRIFT-001`

Registry says SHA A; supplied local checkout is SHA B.

Expected: `REFUSED / BODY_SHA_MISMATCH`.

### `DIRTY-BODY-001`

Exact SHA matches but checkout has uncommitted modifications.

Expected: `REFUSED / DIRTY_BODY`.

### `LATEST-WINS-001`

Two eligible incubating bodies provide the same capability.

Expected: `AMBIGUOUS`; no recency tie-break.

### `STATUS-LAUNDERING-001`

`INCUBATING` result is presented as if it came from present ALEX.

Expected: receipt/UI contract failure.

### `ROUTE-PROMOTION-001`

Successful experimental execution is interpreted as promotion to `PRESENT`.

Expected: refusal; registry status is unchanged.

### `OUTPUT-IDENTITY-001`

Two body-times produce byte-identical output.

Expected: outputs may compare equal; execution receipts and body-time identities remain distinct.

### `REPLAY-IMPERSONATION-001`

Historical body is re-executed successfully.

Expected: new replay occurrence referencing historical body; never original occurrence identity.

### `HELD-EXECUTION-001`

Caller requests a `HELD` body.

Expected: `REFUSED / BODY_NOT_EXECUTABLE`.

### `SHELL-INJECTION-001`

Registry entry attempts shell metacharacters or path traversal.

Expected: schema/validator refusal before invocation.

## 14. Relationship to LOADOUT and LOADIN.STEAD

The intended path is:

```text
LOADOUT
  chooses the smallest capability set
        |
        v
CHRONOBODY
  resolves which exact registered body-time may provide a capability
        |
        v
ORGAN EXECUTION
  returns organ-native result + execution receipt
        |
        v
ALEX FORMATION / DERIVATION
        |
        v
LOADIN.STEAD (optional later)
  routes a newly formed outward occurrence toward a declared destination
```

Ownership remains separate:

- LOADOUT does not choose semantic truth.
- CHRONOBODY does not choose authority or promotion.
- an organ does not acquire authority from being routable.
- ALEX derivation does not admit external consequence.
- LOADIN.STEAD route still does not admit.

## 15. Relationship to GitHub

GitHub is evidence and storage for body ancestry, not a runtime authority oracle.

V0 runtime does not call GitHub during execution.

A registry entry may preserve a GitHub workflow/run identifier as provenance, but the local execution boundary only trusts the committed registry plus the exact local checkout identity it can verify.

A later artifact-backed implementation may replace local worktrees with immutable CI packages without changing the body-time model.

## 16. Promotion discipline

`CHRONOBODY-001` is initially an ALEX-local pattern.

Do not extract a new neutral repository or eCODE-wide law merely because the metaphor is attractive.

Promotion beyond ALEX should require:

1. one real ALEX research run that uses a pinned incubating organ and preserves correct receipts;
2. one hostile branch-drift/refusal specimen;
3. one historical replay specimen;
4. a second materially different project demonstrating the same need without importing ALEX semantics;
5. evidence that a shared protocol removes duplication rather than creating a master ontology.

Until then:

> **ALEX IS THE PROVING GROUND.**

## 17. First executable target

The first implementation should prove only:

1. a registry parser/validator;
2. deterministic body resolution;
3. local exact-SHA/clean-checkout verification;
4. `python-json-stdio/v0` invocation;
5. execution receipts;
6. one canonical `INCUBATING` FAR-SIDE body entry;
7. one small Research Formation Spine runner that consumes a caller-supplied FAR-SIDE formation and then audits a caller-supplied/derived BINOCULAR formation using constituted code;
8. hostile tests for temporal identity, ambiguity, dirty/mismatched bodies, held bodies, and route/promotion separation.

It must not implement:

- Git clone/fetch/checkout;
- arbitrary shell execution;
- remote workers;
- background process supervision;
- automatic branch discovery;
- "latest" body selection;
- automatic merge/promotion;
- authority changes;
- model/network calls;
- Dogram as a runtime dependency;
- MADDCL0WN execution before its own executable contract exists;
- BOOKROOM reconstruction;
- a cross-project Chronobody service.

## 18. Build sequence

The preferred build order is now:

```text
A0  finish PR-completion review for BINOCULAR
    -> if separately admitted, constitute it on main

A1  implement CHRONOBODY registry + resolver

A2  keep FAR-SIDE implementation off-main
    -> register exact green SHA as INCUBATING
    -> prove branch-time execution

A3  implement Research Formation Spine composition runner

C1  executable Decoder-Probe / MADDCL0WN descendants
    -> remain incubating until separately promoted

B1  reconstitute BOOKROOM on fresh main
    -> use it as a source-bearing body feeding the spine
```

This intentionally revises the earlier assumption that FAR-SIDE should merge first. Its experimental location is now an asset: it is the clean first proof that useful possibility can participate without becoming the present.

## 19. Seal

```text
MAIN IS CONSTITUTED PRESENT.
BRANCH IS DEVELOPMENTAL POSSIBILITY.
SHA IS EXECUTABLE IDENTITY.
REGISTRY IS MEMORY.
ROUTING IS NOT PROMOTION.
REPLAY IS NOT ORIGINAL OCCURRENCE.
```

And the broader build law is:

> **DON'T IMPLEMENT THE BACKLOG. IMPLEMENT THE RELATIONS THAT LET THE BACKLOG COMPOSE.**

`CHRONOBODY-001` adds time to the body only by making time attributable. If the exact body-time cannot be named and receipted, it does not get to act.