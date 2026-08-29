# MORTAL-ACTOR-001 — LOADOUT Handoff

> **LOADOUT gives the actor a mortal world.**

The v0 flow is:

```text
C0 -> 3rdi projection -> no new context needed -> evaluate under C0
C0 -> 3rdi projection -> context gap -> compile C1(child of C0) -> evaluate under C1
```

`recompile != mutate`

`selection != evidence`

`capability != authority`

`binding receipt != side effect`

`mortal_actor.loadout-binding/v0` binds an opaque projection reference to one immutable entry compile and one immutable evaluation compile. They may be the same compile. If they differ in v0, the evaluation compile must be a direct child of the entry compile.

A projection-triggered child may change bounded context or world-cut references, but it may not silently widen `effect_fence_ref`, `effective_effects`, or `egress_policy_ref`.

The portable LOADOUT package validates only the compile identity fields this handoff needs. ALEX may independently validate the same compile for expiry, owner-evidence drift, run-envelope matching, or research semantics. That compatibility does not make LOADOUT depend on ALEX.

A successful binding says only that the declared compile ancestry and authority fence are coherent for this run. It does not say that any selected source is evidence, that any claim is supported or true, or that any effect has executed.
