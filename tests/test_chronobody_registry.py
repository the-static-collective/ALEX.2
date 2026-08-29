import copy
import unittest

from alex_runtime.chronobody import RegistryError, parse_registry

FAR_SIDE_SHA = "52c678767017c170506ce1895d3a610b6ef115b4"


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


if __name__ == "__main__":
    unittest.main()
