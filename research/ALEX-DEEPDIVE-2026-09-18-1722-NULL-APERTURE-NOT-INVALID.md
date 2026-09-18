# ALEXDEEPDIVE — NULL-APERTURE-NOT-INVALID-001

**Status:** RESEARCH  
**Promotion:** none  
**Authority:** none  
**Created:** 2026-09-18 17:22 America/Chicago  
**Shape:** AUDIT

## Finding

The newly merged `TARGET-DETERMINACY-ERASURE-001` harness correctly implements finite fiber constancy for nonempty declared projections, but it currently refuses the mathematically legitimate **zero-coordinate projection**.

That is the strongest live boundary found in this pass.

```text
NO OBSERVED COORDINATES
!=
NO PROJECTION

EMPTY PROJECTION
=
CONSTANT / ONE-FIBER PROJECTION

GLOBAL TARGET CONSTANCY
=
TARGET DETERMINACY UNDER THE ZERO-INFORMATION CUT
```

This is not yet classified as a product bug. It is a research-contract mismatch between the general factorization skeleton stated by the merged packet and the narrower executable input grammar.

## Ground

- **Question:** What is the strongest newly exposed ALEX research frontier after the target-determinacy / fiber-sufficiency skeleton landed?
- **Desired consequence:** one bounded discriminator or repo-worthy move, not a new generic runtime.
- **Stop condition:** identify one exact mismatch that can be frozen with a hostile/positive control and does not require importing domain semantics.
- **World cut:** current `ALEX.2` main at pre-write head `ac3dabe75af0b514e800b78708995ee0ff351279`; newly merged target-determinacy packet, harness, fixture, and tests only.
- **Authority/effect boundary:** research audit only; no canon/runtime promotion; durable write permitted only as a new research packet.
- **Formation trace:** no. Discovery trace remains separate below.

## Orientation / access fog

The Static Collective GitBook organization was reached first for orientation. Front Room content search was blocked by the connector safety boundary before retrieval. This is **access fog**, not evidence of absence and not a reason to substitute GitBook claims from memory.

After that orientation attempt, the required ALEX governance files were read before consequential claims:

- `AGENTS.md`
- `skills/alex/SKILL.md`
- `skills/alex/references/research-receipt.md`

They require smallest-adequate research shape, first-class refusal paths, discovery/evidence separation, and no silent promotion.

## Material delta

Current main materially advanced since the prior scheduled ALEXDEEPDIVE frontier. The pre-write head is:

```text
ac3dabe75af0b514e800b78708995ee0ff351279
```

It merges PR #135, `Research: map target determinacy / fiber sufficiency skeleton`.

The merged packet states the general criterion:

```text
pi : X -> Y
q  : X -> Z

Y is sufficient for q
iff
there exists g : Y -> Z
such that
q = g o pi
```

and equivalently:

```text
pi(x) = pi(y) => q(x) = q(y).
```

It then lands a finite executable harness that groups states by the declared `projection_fields` and tests target constancy on each fiber.

## Evidence path

### E1 — merged research statement

`research/ALEX-DEEPDIVE-2026-09-18-TARGET-DETERMINACY-FIBER-SUFFICIENCY-SKELETON.md` at pre-write head.

Observed: the packet explicitly presents target determinacy as factorization through an arbitrary lawful quotient/projection and says the harness enumerates fibers and checks target constancy.

### E2 — executable harness

`research/target_determinacy_erasure_001.py` at the same head.

Observed:

```python
if not _string_list(projection_fields):
    return _invalid(case_id, "INVALID_PROJECTION_FIELDS")
```

`_string_list(..., allow_empty=False)` requires the list to be nonempty. Therefore:

```json
"projection_fields": []
```

is refused before `_find_violation()` runs.

Yet `_find_violation()` itself is already structurally capable of the zero-coordinate case: for every state,

```python
key = tuple(... for field in projection_fields)
```

would produce `()`, placing the entire finite state family in one fiber.

So the mathematical operation is already latent in the implementation; the input validator blocks it.

### E3 — current tests

`tests/test_target_determinacy_erasure_001.py` includes:

- five negative coarse-projection specimens;
- a positive already-determines specimen;
- duplicate-ID refusal;
- repeated-coordinate refinement refusal;
- immutability.

There is no zero-coordinate projection control.

### E4 — external mathematical neighbor

Peter McCullagh's *Partition models* (University of Chicago, 2015; surfaced through Encyclopedia of Mathematics) defines a finite-set partition as disjoint nonempty blocks whose union is the set and explicitly lists `123` as one of the partitions of `[3]`: the one-block / indiscrete partition. This is external terminology pressure only, not ALEX authority.

Database query-determinacy literature likewise treats determinacy as whether equal view images force equal query answers; nothing in that general criterion requires a view to expose at least one informative coordinate. This is a structural neighbor, not imported runtime semantics.

## Exact finite check

No Wolfram computation is needed: the result follows directly from the harness's own key construction.

For states `a,b,c` and `projection_fields=[]`:

```text
pi(a) = ()
pi(b) = ()
pi(c) = ()
```

so there is exactly one fiber:

```text
F = {a,b,c}.
```

Then:

```text
DETERMINES_FOR_TARGET
iff
q(a) = q(b) = q(c).
```

This is the useful baseline question:

> Does the target already have one answer across the entire constituted state family before observing any coordinate at all?

## Claims

| ID | Claim | Class | Support | Counterevidence / limit | Status |
|---|---|---|---|---|---|
| C1 | The current harness refuses `projection_fields=[]`. | documented fact | E2 | none observed | supported |
| C2 | `_find_violation()` would naturally map an empty field list to one fiber if validation allowed it. | inference from executable code | E2 | not presently reachable through public evaluator | supported locally |
| C3 | The merged mathematical skeleton does not require a nonempty projection coordinate list. | documented research statement + mathematical inference | E1 | implementation grammar is narrower | supported |
| C4 | A one-block partition is ordinary finite partition mathematics. | scholarly/mathematical claim | E4 | terminology varies by domain, but the finite-set example is explicit | supported |
| C5 | ALEX should therefore accept empty projections. | proposal | C1–C4 | harness may intentionally require at least one declared observed coordinate | unresolved pending discriminator |

## Competing reading / nearest boring explanation

The boring explanation is credible:

`TARGET-DETERMINACY-ERASURE-001` may have been intentionally scoped to **erasure from an already declared observed surface**, not to the absolute zero-information baseline. Under that local product contract, requiring at least one projection field is defensible.

If that is the intended scope, the right correction is documentation/naming, not code expansion:

```text
GENERAL FACTORIZATION SKELETON
!=
EVERY POSSIBLE PROJECTION MUST BE ACCEPTED BY THIS HARNESS
```

However, because the merged packet presents the executable landing as a finite test of the general fiber criterion, the current refusal is worth making explicit rather than leaving accidental.

## Direct counterpressure

Allowing `[]` must not be misread as proving anything from absence of evidence. It only constitutes the coarsest possible observation map over an already frozen finite state family.

```text
ZERO OBSERVED COORDINATES
!=
ZERO WORLD ASSUMPTIONS

ONE FIBER
!=
ONE WORLD

TARGET CONSTANT ON DECLARED FAMILY
!=
TARGET UNIVERSALLY CONSTANT
```

The constituted state family remains an upstream assumption. If omitted worlds would change `q`, the finite result does not survive expansion of `X`.

## Dependency / independence uncertainty

This audit depends directly on the newly merged target-determinacy packet and its executable implementation. The external partition and query-determinacy neighbors are independent terminology/formal analogues, not independent evidence about ALEX's intended API contract.

No adjacent repository traversal was needed. Dogram, 3rdi, and LOADOUT ownership boundaries remain relevant conceptually, but no current claim here depends on their live heads.

## Rights / egress

- GitBook orientation attempted; content retrieval blocked.
- GitHub repository text inspected through the connected GitHub source.
- External web research used only for public mathematical/scholarly terminology pressure.
- No source corpora, private artifacts, credentials, or page bytes were exported.
- No runtime or canonical interface was modified.

## Residual fog

1. Whether `projection_fields=[]` was intentionally excluded as a harness-scope decision or merely omitted during implementation.
2. Whether the project wants a zero-information baseline in this research harness, or prefers to preserve the narrower meaning of "declared projection" as at least one coordinate.
3. Whether future active-discrimination work would benefit from measuring a probe against the explicit null aperture rather than an arbitrary first aperture.

## Smallest next discriminators

1. **`NULL-APERTURE-CONTROL-001`** — freeze two cases with `projection_fields=[]`: one family whose target is globally constant and one whose target differs. If null aperture is admitted, require respectively `DETERMINES_FOR_TARGET` with `fiber_count=1` and `DOES_NOT_DETERMINE` with an explicit violating pair.
2. If empty projections are intentionally outside scope, add one sentence to the executable packet declaring that restriction and why; preserve the general factorization skeleton separately.
3. Only if (1) proves useful for active discrimination, test whether the null aperture provides a cleaner baseline for "what did this probe actually buy?" Do not add scoring/minimality machinery yet.

## Discovery trace

```text
new merge #135
-> inspect general target-factorization claim
-> inspect executable evaluator
-> compare mathematical domain to validator domain
-> notice nonempty projection requirement
-> pressure whether empty projection is malformed
-> one-fiber / indiscrete partition survives
-> stop at bounded control
```

This trace explains why the seam was noticed. The evidence path above carries the claim.

## Receipt

- **Researcher/agent:** ALEXDEEPDIVE
- **Tool/model boundary:** connected GitBook orientation attempt; connected GitHub exact repository reads/writes; public web scholarship search; no Wolfram result used
- **Pre-write ALEX.2 head:** `ac3dabe75af0b514e800b78708995ee0ff351279`
- **External byte egress:** none from repository to external models/services
- **Durable location:** `research/ALEX-DEEPDIVE-2026-09-18-1722-NULL-APERTURE-NOT-INVALID.md`
- **Promotion:** none

## Seal

```text
NO COORDINATES != NO MAP.
THE NULL APERTURE HAS ONE FIBER.
A TARGET THAT SURVIVES THAT CUT NEEDED NO OBSERVED DISTINCTION
WITHIN THE DECLARED FAMILY.

DECLARED FAMILY != WHOLE WORLD.
RESEARCH RESULT != AUTHORITY.
```
