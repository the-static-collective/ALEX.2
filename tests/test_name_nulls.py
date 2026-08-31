import copy
import unittest

from alex_runtime.name_nulls import evaluate_name_null_battery


CONTROL_TYPES = [
    "COMMON_NAME",
    "REFERENT_SHUFFLE",
    "DECODER_SWAP",
    "WORLD_CUTOFF",
    "LABEL_BLIND",
    "EDGE_ABLATION",
]


def make_control(control_type: str, index: int) -> dict:
    owners = {
        "COMMON_NAME": "ALEX",
        "REFERENT_SHUFFLE": "ALEX",
        "DECODER_SWAP": "Dogram",
        "WORLD_CUTOFF": "3rdi",
        "LABEL_BLIND": "3rdi",
        "EDGE_ABLATION": "ALEX",
    }
    dimension = {
        "COMMON_NAME": "comparison_subject",
        "REFERENT_SHUFFLE": "referent_assignment",
        "DECODER_SWAP": "decoder_identity",
        "WORLD_CUTOFF": "available_worlds",
        "LABEL_BLIND": "semantic_labels",
        "EDGE_ABLATION": "bridge_edge",
    }[control_type]
    return {
        "control_id": f"control-{index}-{control_type.lower()}",
        "control_type": control_type,
        "changed_dimension": dimension,
        "preserved_invariants": ["target_occurrence", "claim_formulation"],
        "next_discriminator": f"compare favored result after changing {dimension}",
        "executor_owner": owners[control_type],
    }


def make_battery() -> dict:
    return {
        "schema": "alex.name-null-battery/v0",
        "battery_id": "name-nulls-pilot-001",
        "hypothesis_ref": "sha256:" + "a" * 64,
        "target_ref": "sha256:" + "b" * 64,
        "target_world": "B",
        "controls": [make_control(t, i) for i, t in enumerate(CONTROL_TYPES, start=1)],
        "producer": "name-dive@v0",
    }


class NameNullBatteryTests(unittest.TestCase):
    def test_complete_six_control_battery_accepts_without_authority(self):
        result = evaluate_name_null_battery(make_battery())
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["receipt"]["control_types"], CONTROL_TYPES)
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertTrue(result["receipt"]["battery_digest"].startswith("sha256:"))

    def test_missing_control_family_refuses(self):
        battery = make_battery()
        battery["controls"] = battery["controls"][:-1]
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "incomplete_control_family")

    def test_duplicate_control_type_refuses(self):
        battery = make_battery()
        battery["controls"][-1]["control_type"] = "COMMON_NAME"
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "duplicate_control_type")

    def test_control_cannot_change_and_preserve_same_dimension(self):
        battery = make_battery()
        battery["controls"][0]["preserved_invariants"].append("comparison_subject")
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "control_dimension_conflict")

    def test_invalid_hypothesis_or_target_ref_refuses(self):
        battery = make_battery()
        battery["hypothesis_ref"] = "not-a-digest"
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_ref")

    def test_invalid_executor_owner_refuses(self):
        battery = make_battery()
        battery["controls"][0]["executor_owner"] = "favorite-hypothesis"
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_executor_owner")

    def test_key_reorder_does_not_change_battery_identity(self):
        first = evaluate_name_null_battery(make_battery())
        battery = make_battery()
        reordered = dict(reversed(list(battery.items())))
        second = evaluate_name_null_battery(reordered)
        self.assertEqual(first["receipt"]["battery_digest"], second["receipt"]["battery_digest"])

    def test_discriminator_change_changes_battery_identity(self):
        first = evaluate_name_null_battery(make_battery())
        battery = make_battery()
        battery["controls"][0]["next_discriminator"] = "a materially different discriminator"
        second = evaluate_name_null_battery(battery)
        self.assertNotEqual(first["receipt"]["battery_digest"], second["receipt"]["battery_digest"])

    def test_input_authority_cannot_widen_output(self):
        battery = make_battery()
        battery["authority"] = "canon"
        result = evaluate_name_null_battery(battery)
        self.assertEqual(result["authority"], "none")
        self.assertEqual(result["receipt"]["authority"], "none")


if __name__ == "__main__":
    unittest.main()
