# LOCAL-SUPPORT-001

`LOCAL-SUPPORT-001` is a bounded ALEX evaluation profile for `MORTAL-ACTOR-001`.

It asks one narrow question:

> Given an exact 3rdi projection handoff, an exact LOADOUT evaluation compile, and candidate `SUPPORTS` proposal, is the attributable evidence basis lawfully present inside this actor's projected world?

The profile does not create a new semantic predicate. It gates the existing `RELATION-DERIVATION-001` evaluator.

```text
GLOBALLY SUPPORTED != LOCALLY SUPPORTABLE
```

If an attributable support path exists globally but any record in its basis is absent from `visible_occurrence_ids`, the profile returns `basis_outside_projection` and does not run semantic derivation over that hidden basis.

If the basis is locally present, the unchanged ALEX derivation kernel evaluates the proposal and the wrapper maps its disposition to:

- `local_basis_accept`
- `local_basis_counterpressured`
- `local_basis_unresolved`

Exact projection and compile identity are checked before semantic evaluation. Mismatches produce `projection_mismatch` or `compile_mismatch` with no derivation.

Every result preserves the neutral claim request ID, cut ID, observer, projection digest, compile ID/digest, required/missing local basis IDs, and receipt survivors.

The profile never consumes global truth or the private oracle. A locally acceptable claim may later prove globally false. `ACCEPT` remains evaluator disposition only: it is not authority, canon, admission, publication, or permission to execute a side effect.
