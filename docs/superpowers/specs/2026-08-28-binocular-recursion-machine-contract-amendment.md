# BINOCULAR-RECURSION-001 — Machine Contract Amendment 1

**Date:** 2026-08-28  
**Status:** NORMATIVE AMENDMENT  
**Parent:** `docs/superpowers/specs/2026-08-28-binocular-recursion-machine-contract.md`

## Purpose

The approved machine contract defines `FIXED` in terms of an unchanged compression profile digest and defines `DIVERGENT` in terms of a bounded pass limit, but the corresponding fields were omitted from the example envelopes. This amendment makes those already-approved terminal requirements machine-testable without changing their semantics.

## Amendment A — compression profile digest

Every pass `compression` envelope MUST include:

```json
{
  "profile_digest": "sha256:compression-profile-v1",
  "proposal_digest": "sha256:...",
  "formation_basis_refs": [],
  "claim_support_refs": [],
  "reexpanded_live_consequence_refs": []
}
```

`profile_digest` identifies the compression rule/profile under which the proposal was formed. It is formation metadata, not support or authority.

For `FIXED`, the final two passes MUST have equal:

```text
compression.profile_digest
expansion.profile_digest
```

before equality of binocular-state digests can demonstrate the fixed terminal.

## Amendment B — bounded pass limit

The top-level case envelope MUST include:

```json
{
  "pass_limit": 4
}
```

Validation:

```text
pass_limit is an integer
pass_limit >= 1
len(passes) <= pass_limit
```

If invalid:

```text
INSUFFICIENT_TO_TEST / INVALID_PASS_LIMIT
```

For a claimed `DIVERGENT` terminal:

```text
len(passes) == pass_limit
```

is required in addition to the parent contract's requirements of no repeated binocular-state digest and a non-empty material tension delta on the final transition.

A run that stops before its declared bound cannot demonstrate divergence:

```text
INSUFFICIENT_TO_TEST / TERMINAL_NOT_DEMONSTRATED
```

## Non-collapse

```text
compression profile identity != compression truth
pass limit reached != proof of unbounded divergence
DIVERGENT == bounded observed formation behavior only
```
