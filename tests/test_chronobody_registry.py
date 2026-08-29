import copy
import unittest

from alex_runtime.chronobody import (
    BodyMode,
    RegistryError,
    parse_registry,
    resolve_body,
)

FAR_SIDE_SHA = "52c678767017c170506ce1895d3a610b6ef115b4"
SECOND_SHA = "1111111111111111111111111111111111111111"


def registry_value():
    return {
        "schema": "alex.chronobody-registry/v0",
        "organs": [
            {
                "organ_id": "far-side-pass",
                "body_time_id": f"far-side-pass@{FAR_SIDE_SHA}",
                "status": "INCUBATING",
                "capabilities": ["far_side_pressure"],
                "source": {
                    "repo": "the-static-collective/ALEX.2",
                    "branch": "feature/far-side-pass-m0",
                    "sha": FAR_SIDE_SHA,
                },
                "runtime": {
                    "contract": "python-json-stdio/v0",
                    "entrypoint": "tools/far_side_lab.py",
                },
                "verification": {
                    "workflow": "crucible-contract",
                    "run_id": 33219406091,
                    "result": "GREEN",
                },
                "authority": "none",
                "parents": [],
            }
        ],
    }


def second_body(*, status="INCUBATING", capability="far_side_pressure"):
    return {
        "organ_id": "far-side-pass-next",
        "body_time_id": f"far-side-pass-next@{SECOND_SHA}",
        "status": status,
        "capabilities": [capability],
        "source": {
            "repo": "the-static-collective/ALEX.2",
            "branch": "feature/far-side-pass-next",
            "sha": SECOND_SHA,
        },
        "runtime": {
            "contract": "python-json-stdio/v0",
            "entrypoint": "tools/far_side_lab.py",
        },
        "verification": {
            "workflow": "crucible-contract",
            "run_id": 1,
            "result": "GREEN",
        },
        "authority": "none",
        "parents": [],
    }


class ChronobodyRegistryTests(unittest.TestCase):
    def assert_registry_error(self, value, code):
        with self.assertRaises(RegistryError) as raised:
            parse_registry(value)
        self.assertEqual(raised.exception.code, code)

    def test_exact_body_time_is_accepted(self):
        entries = parse_registry(registry_value())
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0].body_time_id, f"far-side-pass@{FAR_SIDE_SHA}")
        self.assertEqual(entries[0].status.value, "INCUBATING")
        self.assertEqual(entries[0].capabilities, ("far_side_pressure",))
        self.assertEqual(entries[0].authority, "none")

    def test_branch_without_sha_is_refused(self):
        value = copy.deepcopy(registry_value())
        del value["organs"][0]["source"]["sha"]
        self.assert_registry_error(value, "BODY_SHA_REQUIRED")

    def test_short_sha_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["source"]["sha"] = "52c6787"
        value["organs"][0]["body_time_id"] = "far-side-pass@52c6787"
        self.assert_registry_error(value, "BODY_SHA_INVALID")

    def test_body_time_id_must_match_sha(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["body_time_id"] = "far-side-pass@0000000000000000000000000000000000000000"
        self.assert_registry_error(value, "BODY_TIME_ID_MISMATCH")

    def test_unknown_status_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["status"] = "MAYBE"
        self.assert_registry_error(value, "UNKNOWN_BODY_STATUS")

    def test_authority_must_be_none(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["authority"] = "merge"
        self.assert_registry_error(value, "AUTHORITY_NOT_NONE")

    def test_duplicate_body_time_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"].append(copy.deepcopy(value["organs"][0]))
        self.assert_registry_error(value, "DUPLICATE_BODY_TIME_ID")

    def test_duplicate_capability_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["capabilities"] = ["far_side_pressure", "far_side_pressure"]
        self.assert_registry_error(value, "DUPLICATE_CAPABILITY")

    def test_absolute_entrypoint_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["runtime"]["entrypoint"] = "/tmp/far_side_lab.py"
        self.assert_registry_error(value, "ENTRYPOINT_INVALID")

    def test_parent_traversal_entrypoint_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["runtime"]["entrypoint"] = "../far_side_lab.py"
        self.assert_registry_error(value, "ENTRYPOINT_INVALID")

    def test_non_allowlisted_runtime_contract_is_refused(self):
        value = copy.deepcopy(registry_value())
        value["organs"][0]["runtime"]["contract"] = "shell/v0"
        self.assert_registry_error(value, "RUNTIME_CONTRACT_UNSUPPORTED")


class ChronobodyResolutionTests(unittest.TestCase):
    def setUp(self):
        self.entries = parse_registry(registry_value())

    def test_present_only_does_not_fall_back_to_incubating(self):
        result = resolve_body(self.entries, "far_side_pressure", BodyMode.PRESENT_ONLY)
        self.assertEqual(result.disposition, "UNAVAILABLE")
        self.assertEqual(result.reason_code, "NO_ELIGIBLE_BODY")
        self.assertIsNone(result.entry)

    def test_experimental_routes_one_incubating_body(self):
        result = resolve_body(self.entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
        self.assertEqual(result.disposition, "ROUTED")
        self.assertIsNone(result.reason_code)
        self.assertEqual(result.entry.body_time_id, f"far-side-pass@{FAR_SIDE_SHA}")

    def test_two_eligible_bodies_are_ambiguous_not_latest_wins(self):
        value = registry_value()
        value["organs"].append(second_body())
        entries = parse_registry(value)
        result = resolve_body(entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
        self.assertEqual(result.disposition, "AMBIGUOUS")
        self.assertEqual(result.reason_code, "MULTIPLE_ELIGIBLE_BODIES")
        self.assertIsNone(result.entry)
        self.assertEqual(
            result.candidate_body_time_ids,
            tuple(sorted((f"far-side-pass@{FAR_SIDE_SHA}", f"far-side-pass-next@{SECOND_SHA}"))),
        )

    def test_explicit_organ_disambiguates_without_recency_rule(self):
        value = registry_value()
        value["organs"].append(second_body())
        entries = parse_registry(value)
        result = resolve_body(
            entries,
            "far_side_pressure",
            BodyMode.EXPERIMENTAL,
            organ_id="far-side-pass-next",
        )
        self.assertEqual(result.disposition, "ROUTED")
        self.assertEqual(result.entry.body_time_id, f"far-side-pass-next@{SECOND_SHA}")

    def test_replay_requires_exact_body_time_id(self):
        value = registry_value()
        value["organs"][0]["status"] = "RETIRED"
        entries = parse_registry(value)
        result = resolve_body(entries, "far_side_pressure", BodyMode.REPLAY)
        self.assertEqual(result.disposition, "REFUSED")
        self.assertEqual(result.reason_code, "EXACT_BODY_TIME_REQUIRED")

    def test_retired_body_routes_only_by_exact_replay(self):
        value = registry_value()
        value["organs"][0]["status"] = "RETIRED"
        entries = parse_registry(value)
        result = resolve_body(
            entries,
            "far_side_pressure",
            BodyMode.REPLAY,
            body_time_id=f"far-side-pass@{FAR_SIDE_SHA}",
        )
        self.assertEqual(result.disposition, "ROUTED")
        self.assertEqual(result.entry.status.value, "RETIRED")

    def test_held_body_explicit_request_is_refused(self):
        value = registry_value()
        value["organs"][0]["status"] = "HELD"
        entries = parse_registry(value)
        result = resolve_body(
            entries,
            "far_side_pressure",
            BodyMode.EXPERIMENTAL,
            body_time_id=f"far-side-pass@{FAR_SIDE_SHA}",
        )
        self.assertEqual(result.disposition, "REFUSED")
        self.assertEqual(result.reason_code, "BODY_NOT_EXECUTABLE")

    def test_reconstituted_body_is_experimental_only(self):
        value = registry_value()
        value["organs"][0]["status"] = "RECONSTITUTED"
        entries = parse_registry(value)
        experimental = resolve_body(entries, "far_side_pressure", BodyMode.EXPERIMENTAL)
        present = resolve_body(entries, "far_side_pressure", BodyMode.PRESENT_ONLY)
        self.assertEqual(experimental.disposition, "ROUTED")
        self.assertEqual(present.disposition, "UNAVAILABLE")

    def test_explicit_body_with_wrong_capability_is_refused(self):
        result = resolve_body(
            self.entries,
            "binocular_formation_audit",
            BodyMode.EXPERIMENTAL,
            body_time_id=f"far-side-pass@{FAR_SIDE_SHA}",
        )
        self.assertEqual(result.disposition, "REFUSED")
        self.assertEqual(result.reason_code, "CAPABILITY_MISMATCH")

    def test_explicit_body_in_wrong_mode_is_refused(self):
        result = resolve_body(
            self.entries,
            "far_side_pressure",
            BodyMode.REPLAY,
            body_time_id=f"far-side-pass@{FAR_SIDE_SHA}",
        )
        self.assertEqual(result.disposition, "REFUSED")
        self.assertEqual(result.reason_code, "BODY_MODE_MISMATCH")


if __name__ == "__main__":
    unittest.main()
