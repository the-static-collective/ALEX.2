# LOADINSTEAD Door Router m0 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement one pure, deterministic LOADINSTEAD router that validates typed eCODE route bits and door declarations, resolves exactly one owning destination or preserves ambiguity/unroutability, selects independent witness doors, and emits a canonical no-authority route receipt.

**Architecture:** Add a sibling `loadout_runtime` package beside `alex_runtime`; do not import LOADINSTEAD from ALEX kernel code. The router consumes explicit typed consequence classes rather than performing semantic classification. It returns route proposals and delivery envelopes only; no transport, destination write, admission, merge, publish, canon, or other side effect occurs in m0.

**Tech Stack:** Python 3.12, standard library only, repository-local `alex_runtime.digests.sha256_json` for incubation-time canonical SHA-256 identity, `unittest` for tests.

**Spec:** `docs/superpowers/specs/2026-08-28-loadout-loadinstead-door-router-design.md`

## Global Constraints

- `LOADOUT != LOADINSTEAD`.
- `LOADINSTEAD != destination gate`.
- Routing consumes an explicit `consequence_class`; m0 performs no LLM, embedding, keyword, or heuristic classification.
- Exactly one available destination owner may be selected; zero is `UNROUTABLE`; more than one is `AMBIGUOUS`.
- Witness selection is independent from destination selection.
- Matching unavailable doors remain visible in `rejections`.
- Every delivery envelope carries `authority: none`.
- Every route result carries `authority_transferred: false` and `admission_status: NOT_ATTEMPTED`.
- Invalid inputs raise `ValueError` with stable machine-readable codes; the router never silently repairs malformed bits or doors.
- No runtime code under `alex_runtime/` imports `loadout_runtime` in m0.
- No network, filesystem write, provider call, repository mutation, queue publish, or destination admission is performed by the router.

---

## File Structure

```text
loadout_runtime/
  __init__.py             # public m0 exports only
  loadinstead.py          # contracts, validation, deterministic router

tests/
  test_loadinstead_router.py

docs/superpowers/specs/
  2026-08-28-loadout-loadinstead-door-router-design.md

docs/superpowers/plans/
  2026-08-28-loadinstead-door-router-m0.md
```

`loadinstead.py` owns only the pure routing boundary. No transport adapter is added in this slice.

---

### Task 1: Red — define executable LOADINSTEAD behavior

**Files:**
- Create: `tests/test_loadinstead_router.py`

**Interfaces under test:**
- `validate_route_bit(bit_record: dict) -> list[str]`
- `validate_door(door_record: dict) -> list[str]`
- `route_bit(bit_record: dict, doors: list[dict]) -> dict`
- constants `LOADINSTEAD_M0_PROFILE`, `ROUTE_BIT_SCHEMA`, `DOOR_SCHEMA`, `ROUTE_PROPOSAL_SCHEMA`

- [ ] **Step 1: Write the failing test module**

Use these imports at the top so RED is caused by the missing production package:

```python
import copy
import unittest

from loadout_runtime.loadinstead import (
    DOOR_SCHEMA,
    LOADINSTEAD_M0_PROFILE,
    ROUTE_BIT_SCHEMA,
    ROUTE_PROPOSAL_SCHEMA,
    route_bit,
    validate_door,
    validate_route_bit,
)
```

Define these fixture helpers exactly:

```python
def make_bit(**overrides):
    bit = {
        "schema": ROUTE_BIT_SCHEMA,
        "bit_id": "bit-001",
        "occurred_at": "2026-08-28T19:00:00Z",
        "source_world": "daily-slice",
        "consequence_class": "repository_work",
        "payload_ref": "receipt://daily-slice/bit-001",
        "formation_ref": "ecode://history/bit-001",
        "compile_ref": {
            "compile_id": "loadout-compile-001",
            "compile_digest": "sha256:" + "a" * 64,
        },
        "witness_classes": ["research_accounting"],
    }
    bit.update(overrides)
    return bit


def make_door(
    door_id,
    *,
    owner_world,
    role,
    accepts_classes,
    protocol,
    status="available",
):
    return {
        "schema": DOOR_SCHEMA,
        "door_id": door_id,
        "owner_world": owner_world,
        "role": role,
        "accepts_classes": list(accepts_classes),
        "protocol": protocol,
        "capability_ref": f"capability://{door_id}",
        "status": status,
    }
```

Add the following test cases:

```python
class LoadinsteadRouterTests(unittest.TestCase):
    def test_routes_repository_work_to_single_forge_door_and_alex_witness(self):
        bit = make_bit()
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
            make_door(
                "alex-witness",
                owner_world="ALEX",
                role="witness",
                accepts_classes=["research_accounting"],
                protocol="alex.route-witness/v0",
            ),
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["schema"], ROUTE_PROPOSAL_SCHEMA)
        self.assertEqual(result["profile"], LOADINSTEAD_M0_PROFILE)
        self.assertEqual(result["disposition"], "ROUTED")
        self.assertEqual(result["primary_door_ref"], "forge")
        self.assertEqual(result["candidate_door_refs"], ["forge"])
        self.assertEqual(result["witness_door_refs"], ["alex-witness"])
        self.assertFalse(result["authority_transferred"])
        self.assertEqual(result["admission_status"], "NOT_ATTEMPTED")
        self.assertEqual(result["delivery_envelopes"][0]["authority"], "none")
        self.assertEqual(result["delivery_envelopes"][0]["protocol"], "forge.work-envelope/v0")
        self.assertRegex(result["route_id"], r"^sha256:[0-9a-f]{64}$")

    def test_zero_available_destination_owners_is_unroutable(self):
        bit = make_bit(consequence_class="relationship_crossing", witness_classes=[])
        result = route_bit(bit, [])
        self.assertEqual(result["disposition"], "UNROUTABLE")
        self.assertIsNone(result["primary_door_ref"])
        self.assertEqual(result["candidate_door_refs"], [])
        self.assertEqual(result["delivery_envelopes"], [])

    def test_multiple_available_destination_owners_is_ambiguous_and_never_silently_tiebreaks(self):
        bit = make_bit(witness_classes=[])
        doors = [
            make_door(
                "forge-a",
                owner_world="FORGE-A",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
            make_door(
                "forge-b",
                owner_world="FORGE-B",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["disposition"], "AMBIGUOUS")
        self.assertIsNone(result["primary_door_ref"])
        self.assertEqual(result["candidate_door_refs"], ["forge-a", "forge-b"])
        self.assertEqual(result["delivery_envelopes"], [])

    def test_matching_unavailable_door_is_preserved_as_rejection(self):
        bit = make_bit(witness_classes=[])
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
                status="unavailable",
            )
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["disposition"], "UNROUTABLE")
        self.assertEqual(
            result["rejections"],
            [{"door_id": "forge", "reason_code": "DOOR_UNAVAILABLE"}],
        )

    def test_unavailable_witness_does_not_block_primary_route(self):
        bit = make_bit()
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            ),
            make_door(
                "alex-witness",
                owner_world="ALEX",
                role="witness",
                accepts_classes=["research_accounting"],
                protocol="alex.route-witness/v0",
                status="unavailable",
            ),
        ]
        result = route_bit(bit, doors)
        self.assertEqual(result["disposition"], "ROUTED")
        self.assertEqual(result["primary_door_ref"], "forge")
        self.assertEqual(result["witness_door_refs"], [])
        self.assertIn(
            {"door_id": "alex-witness", "reason_code": "DOOR_UNAVAILABLE"},
            result["rejections"],
        )

    def test_invalid_bit_is_rejected_instead_of_reinterpreted(self):
        bit = make_bit()
        del bit["consequence_class"]
        self.assertIn("BIT_SHAPE_INVALID", validate_route_bit(bit))
        with self.assertRaisesRegex(ValueError, "BIT_SHAPE_INVALID"):
            route_bit(bit, [])

    def test_invalid_door_is_rejected_instead_of_repaired(self):
        door = make_door(
            "forge",
            owner_world="FORGE",
            role="destination",
            accepts_classes=["repository_work"],
            protocol="forge.work-envelope/v0",
        )
        door["role"] = "router-and-owner"
        self.assertIn("DOOR_ROLE_INVALID", validate_door(door))
        with self.assertRaisesRegex(ValueError, "DOOR_ROLE_INVALID"):
            route_bit(make_bit(witness_classes=[]), [door])

    def test_same_inputs_replay_to_same_route_identity(self):
        bit = make_bit()
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            )
        ]
        first = route_bit(copy.deepcopy(bit), copy.deepcopy(doors))
        second = route_bit(copy.deepcopy(bit), copy.deepcopy(doors))
        self.assertEqual(first, second)

    def test_formation_change_changes_route_identity_without_changing_surface_route(self):
        bit = make_bit(witness_classes=[])
        doors = [
            make_door(
                "forge",
                owner_world="FORGE",
                role="destination",
                accepts_classes=["repository_work"],
                protocol="forge.work-envelope/v0",
            )
        ]
        first = route_bit(bit, doors)
        changed = make_bit(
            witness_classes=[],
            formation_ref="ecode://history/bit-001-descendant",
        )
        second = route_bit(changed, doors)
        self.assertEqual(first["primary_door_ref"], second["primary_door_ref"])
        self.assertNotEqual(first["route_id"], second["route_id"])
```

- [ ] **Step 2: Open a draft PR with only docs + failing tests and verify RED in GitHub Actions**

Expected failure: import error for missing `loadout_runtime` package. The failure must be recorded in the PR timeline before production code is added.

---

### Task 2: Green — implement the pure router

**Files:**
- Create: `loadout_runtime/__init__.py`
- Create: `loadout_runtime/loadinstead.py`

**Produces:**

```python
ROUTE_BIT_SCHEMA = "ecode.route-bit/v0"
DOOR_SCHEMA = "loadinstead.door/v0"
ROUTE_PROPOSAL_SCHEMA = "loadinstead.route-proposal/v0"
LOADINSTEAD_M0_PROFILE = "loadout.runtime/loadinstead-door-router-m0"

def validate_route_bit(bit_record: dict) -> list[str]: ...
def validate_door(door_record: dict) -> list[str]: ...
def route_bit(bit_record: dict, doors: list[dict]) -> dict: ...
```

- [ ] **Step 1: Implement strict schemas and validators**

`ROUTE_BIT_KEYS` must be exactly:

```python
{
    "schema",
    "bit_id",
    "occurred_at",
    "source_world",
    "consequence_class",
    "payload_ref",
    "formation_ref",
    "compile_ref",
    "witness_classes",
}
```

`COMPILE_REF_KEYS` must be exactly:

```python
{"compile_id", "compile_digest"}
```

`DOOR_KEYS` must be exactly:

```python
{
    "schema",
    "door_id",
    "owner_world",
    "role",
    "accepts_classes",
    "protocol",
    "capability_ref",
    "status",
}
```

Validation rules:

- exact key set required;
- schema values must match constants;
- string identity/reference/class fields must be non-empty;
- `occurred_at` must parse as offset-aware ISO-8601;
- compile digest must match `^sha256:[0-9a-f]{64}$`;
- `witness_classes` and `accepts_classes` must be lists of unique non-empty strings;
- `role` must be `destination` or `witness`;
- `status` must be `available` or `unavailable`.

Return stable codes in insertion order without duplicates. At minimum use:

```text
BIT_NOT_OBJECT
BIT_SHAPE_INVALID
BIT_SCHEMA_INVALID
BIT_ID_REQUIRED
BIT_OCCURRED_AT_INVALID
BIT_SOURCE_WORLD_REQUIRED
BIT_CONSEQUENCE_CLASS_REQUIRED
BIT_PAYLOAD_REF_REQUIRED
BIT_FORMATION_REF_REQUIRED
BIT_COMPILE_REF_INVALID
BIT_WITNESS_CLASSES_INVALID
DOOR_NOT_OBJECT
DOOR_SHAPE_INVALID
DOOR_SCHEMA_INVALID
DOOR_ID_REQUIRED
DOOR_OWNER_WORLD_REQUIRED
DOOR_ROLE_INVALID
DOOR_ACCEPTS_CLASSES_INVALID
DOOR_PROTOCOL_REQUIRED
DOOR_CAPABILITY_REF_REQUIRED
DOOR_STATUS_INVALID
```

- [ ] **Step 2: Implement deterministic routing**

Implementation order:

1. deep-copy inputs;
2. validate bit and every door;
3. on any validation error, raise `ValueError` with comma-joined stable codes;
4. compute `bit_digest = sha256_json(bit)`;
5. scan doors in input order;
6. for matching unavailable doors, append `{"door_id": ..., "reason_code": "DOOR_UNAVAILABLE"}`;
7. collect available destination candidates matching `consequence_class`;
8. collect available witness doors whose `accepts_classes` intersect `witness_classes`;
9. preserve candidate and witness door order from the registry;
10. choose disposition solely by destination candidate count;
11. create a delivery envelope only for `ROUTED` primary destination;
12. set `authority_transferred = False` and `admission_status = "NOT_ATTEMPTED"` unconditionally;
13. compute `route_id = sha256_json(route_without_route_id)`;
14. return a deep-copied plain dict.

The delivery envelope must be exactly:

```python
{
    "door_id": primary["door_id"],
    "owner_world": primary["owner_world"],
    "protocol": primary["protocol"],
    "payload_ref": bit["payload_ref"],
    "formation_ref": bit["formation_ref"],
    "bit_id": bit["bit_id"],
    "authority": "none",
}
```

Do not add transport calls.

- [ ] **Step 3: Re-export the four constants and three functions from `loadout_runtime/__init__.py`**

Use explicit imports and `__all__`; do not export internal helpers.

- [ ] **Step 4: Run `python -m unittest tests.test_loadinstead_router -v`**

Expected: all LOADINSTEAD tests pass.

- [ ] **Step 5: Run `python -m unittest discover -s tests -v`**

Expected: all existing ALEX and new LOADINSTEAD tests pass.

---

### Task 3: Verify isolation and PR receipt

**Files:**
- No production changes unless verification finds a defect.

- [ ] **Step 1: Compare branch to main**

Required changed surfaces:

```text
docs/superpowers/specs/2026-08-28-loadout-loadinstead-door-router-design.md
docs/superpowers/plans/2026-08-28-loadinstead-door-router-m0.md
tests/test_loadinstead_router.py
loadout_runtime/__init__.py
loadout_runtime/loadinstead.py
```

No file under `alex_runtime/` may change.

- [ ] **Step 2: Confirm GitHub Actions runs `python -m unittest discover -s tests -v` and succeeds on final head**

Record the workflow run ID and final branch head SHA in the PR body.

- [ ] **Step 3: Confirm the PR boundary states the exact non-claims**

The PR body must say:

```text
route != admit
m0 performs no semantic classification
m0 performs no transport or destination write
FORGE is a door family, not the router
ALEX kernel is unchanged
```

- [ ] **Step 4: Leave the PR unmerged**

The user has authorized implementation, not silent landing into `main`. Merge remains a separate owning-world gate.
