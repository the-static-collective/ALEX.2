# LOADOUT Handshake v0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Gate 3 of the approved ALEX × LOADOUT boundary: accept an immutable `alex.run-envelope/v0` only when it matches an attributable LOADOUT compile, preserve compile trace/effect-fence testimony, refuse stale or drifting compiles, surface capability gaps, and prove child compiles do not inherit ambient permission.

**Architecture:** Add an ALEX-side handshake module, not a LOADOUT implementation. LOADOUT-issued compile records and current audit witnesses remain external testimony. ALEX verifies shape, canonical compile digest, envelope/compile identity, expiry, owner-evidence drift, required capability presence, and requested effects against the compile's already-effective attributable fence. It never unions permissions, interprets owner authority, mutates a compile, or manufactures a child compile. A real Blind Crucible adapter and scoped `alex.runtime/loadout-handshake-m0` profile prove the boundary.

**Tech Stack:** Python 3.12 standard library, JSON Schema Draft 2020-12, canonical JSON SHA-256, `unittest`, subprocess CLI/JSON boundary, existing Blind Crucible harness.

**Spec:** `docs/superpowers/specs/2026-08-26-alex-loadout-runtime-boundary-design.md`, especially §§4–8, 14–15, 19–22.

## Global Constraints

- `LOADOUT != ALEX`; this PR implements only ALEX's receiving/validation side of the handshake.
- `alex.run-envelope/v0` must preserve the approved public fields and task-shape enum; do not add permission semantics to the envelope.
- Compile records are immutable testimony. ALEX validates their digest; it never patches or recompiles them.
- `compile_digest` identifies compile payload integrity, not historical occurrence identity.
- `compile_trace_ref` is mandatory and must match the carried compile trace occurrence.
- Context selection/compile trace may explain attention but never supplies evidentiary support by selection alone.
- Effect fences are carried attributable testimony. ALEX may only check membership/identity/scope status; it does not infer new authorization.
- Effective permission is intersection-shaped upstream; ALEX must never use union/inheritance logic.
- A child compile may reuse context references but receives no parent permission unless the child itself carries current attributable allowed testimony.
- Expired compile, owner-evidence drift, and capability gaps set `recompile_required`; they do not silently reuse the parent.
- `ACCEPT` at this handshake means only “this run request may enter ALEX under this compile.” It does not admit external consequence.
- Preserve Gate-1/2 conformance language. No claim of general ALEX runtime conformance.
- No one-book runtime, Desk/MCP, SQLite ledger, universal authority service, dynamic policy DSL, or generalized workflow engine in this gate.

---

## File Structure

- `alex_runtime/handshake.py` — compile/envelope digest validation and ALEX-side handshake evaluation.
- `crucible/schema/run-envelope.schema.json` — exact public `alex.run-envelope/v0` contract.
- `crucible/schema/loadout-compile.schema.json` — minimal immutable compile testimony contract.
- `crucible/specimens/loadout-handshake-valid.json` — positive baseline.
- `crucible/specimens/loadout-handshake-stale-compile.json` — expired compile.
- `crucible/specimens/loadout-handshake-owner-drift.json` — current owner-evidence digest differs from frozen compile.
- `crucible/specimens/loadout-handshake-permission-drift.json` — child compile lacks parent's previously allowed effect.
- `crucible/specimens/loadout-handshake-capability-gap.json` — required capability absent from the compile.
- `tools/loadout_handshake_adapter.py` — real CASE-only subprocess adapter.
- `crucible/profiles/alex.runtime.loadout-handshake-m0.json` — scoped Gate-3 profile.
- `tools/run_loadout_handshake_profile.py` — original + fresh metamorphic profile runner.
- `tests/test_loadout_handshake.py` — digest, identity, expiry, trace, effect/capability and child non-inheritance tests.
- `tests/test_loadout_handshake_adapter.py` — real subprocess boundary tests.
- `tests/test_loadout_handshake_profile.py` — profile and metamorphic proof.
- `tests/test_crucible_contract.py` — admit Gate-3 specimens without rewriting earlier fixtures.
- `tools/crucible_blind.py` — resolve the Gate-3 profile digest from a pinned handshake manifest.
- `crucible/README.md` — document the scoped proof boundary.

---

## Task 1 — Public compile/envelope contracts and canonical compile identity

**Interfaces:**
- `compile_payload_digest(compile_record: dict) -> str`
- `validate_compile_record(compile_record: dict) -> list[str]`
- `validate_run_envelope(envelope: dict, compile_record: dict) -> list[str]`
- `handshake_ruleset_manifest(profile: str) -> dict | None`
- `handshake_ruleset_digest(profile: str) -> str | None`

- [ ] Write schema/identity tests first: exact envelope keys/task enum, compile digest excludes its own digest field, trace ref is required, and envelope compile ID/digest/trace/context/world/effect/egress/capability fields must match the compile.
- [ ] Run focused tests and preserve RED because `alex_runtime.handshake` and schemas do not exist.
- [ ] Implement the minimum schemas, digest helpers, pinned `alex.runtime/loadout-handshake-m0` ruleset manifest, and structural validators.
- [ ] Make `tools.crucible_blind.ruleset_digest()` manifest-aware for the handshake profile without changing Gate-1 or Gate-2 digests.
- [ ] Run focused + legacy digest suites GREEN and commit.

---

## Task 2 — Accept valid compiles; refuse stale compiles while preserving compile trace

**Handshake result:**
```json
{
  "compile_id": "...",
  "compile_digest": "sha256:...",
  "compile_trace_ref": "...",
  "disposition": "ACCEPT | REFUSE | INSUFFICIENT_TO_TEST",
  "reason_code": null,
  "recompile_required": false,
  "capability_gaps": [],
  "receipt_survivors": [],
  "execution": {"terminal_state": "FINISHED", "step_count": 1}
}
```

- [ ] Add positive-baseline and stale-compile fixtures/tests first.
- [ ] RED must show missing `evaluate_loadout_handshake()` behavior only.
- [ ] Implement deterministic `evaluate_loadout_handshake(case, now=...)` using an explicit ISO-8601 audit time supplied by the CASE; do not read wall-clock time implicitly.
- [ ] Valid matching compile => `ACCEPT`; expired compile => `REFUSE/COMPILE_EXPIRED`, `recompile_required=true`, with compile/trace/fence residues preserved.
- [ ] Prove input CASE is not mutated; run focused tests GREEN and commit.

---

## Task 3 — Capability gaps and attributable effect-fence non-escalation

The CASE `attempt` may request `required_capabilities` and `requested_effects`; these are command requirements, not new run-envelope fields.

Each compile carries already-effective fence entries with `effect`, `status`, `authorization_source_ref`, `scope`, `valid_from`, `expires_at`, `revocation_ref`, and `owner_gate_ref`.

- [ ] Write tests first for: missing required capability; requested effect absent/refused/unattributable in child fence; valid allowed effect; and no parent-fence fallback.
- [ ] Preserve RED.
- [ ] Implement membership-only checks: missing capability => `INSUFFICIENT_TO_TEST/CAPABILITY_GAP` + `recompile_required`; out-of-fence effect => `REFUSE/EFFECT_OUTSIDE_FENCE`; allowed effect requires current attributable `status=allowed` entry in this compile.
- [ ] Never union parent and child fences. No parent permission lookup exists in the evaluator.
- [ ] Run focused tests GREEN and commit.

---

## Task 4 — Owner-evidence drift and child-compile non-inheritance

A fresh LOADOUT audit witness may carry only identity/digest facts needed to detect drift; ALEX does not interpret the owner's authority semantics.

- [ ] Write RED tests for `current_owner_evidence_digest != compile.owner_evidence_digest` and for a child compile that retains context refs but omits the parent's allowed effect.
- [ ] Implement owner drift => `INSUFFICIENT_TO_TEST/OWNER_EVIDENCE_CHANGED`, `recompile_required=true`.
- [ ] Preserve parent/child compile IDs as distinct occurrences even when context payload refs are identical.
- [ ] Prove child permission must appear in the child's own fence; no ambient inheritance path exists.
- [ ] Run focused tests GREEN and commit.

---

## Task 5 — Real Blind Crucible adapter and scoped Gate-3 profile

- [ ] Write adapter/profile tests before code. The profile must include five originals (valid, stale, owner drift, permission drift, capability gap) and fresh metamorphic siblings with rewritten case/compile identities, fresh nonces, reordered capability/effect arrays, and recomputed compile/input digests.
- [ ] Preserve RED because adapter/profile runner do not exist.
- [ ] Implement `tools/loadout_handshake_adapter.py` and `tools/run_loadout_handshake_profile.py` through the existing CASE-only harness.
- [ ] Pin `crucible/profiles/alex.runtime.loadout-handshake-m0.json`; exclude one-book/formation-trace profiles.
- [ ] Profile must pass 10/10 while the adapter never receives ORACLE.
- [ ] Document exactly what Gate 3 proves and what remains unclaimed.
- [ ] Run the full `python -m unittest discover -s tests -v` suite GREEN.
- [ ] Static review: verify no authority/admission/canon/publication mutation vocabulary is emitted, no mutable compile API exists, and prior Gate-1/2 fixtures remain unchanged.
- [ ] Update PR body with preserved RED→GREEN receipts and final clean-tree workflow; mark ready for review, but do not merge without human gate.
