import copy
import json
import os
import unittest
from pathlib import Path

from alex_runtime.digests import sha256_json
from alex_runtime.research_formation import evaluate_research_formation_run
from alex_runtime.chronobody import parse_registry


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"
STRUCTURAL_FIXTURE = ROOT / "tests" / "fixtures" / "research_formation" / "lawful.json"
FAR_SIDE_ID = "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4"
BINOCULAR_ID = "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e"


def load_entries():
    return parse_registry(json.loads(REGISTRY_PATH.read_text(encoding="utf-8")))


def load_request():
    request = json.loads(STRUCTURAL_FIXTURE.read_text(encoding="utf-8"))
    far_root = os.environ.get("ALEX_FAR_SIDE_BODY_ROOT")
    binocular_root = os.environ.get("ALEX_BINOCULAR_BODY_ROOT")
    if not far_root or not binocular_root:
        raise unittest.SkipTest("exact Chronobody materializations not supplied")

    request["materializations"] = {
        FAR_SIDE_ID: far_root,
        BINOCULAR_ID: binocular_root,
    }
    request["far_side"]["case"] = json.loads(
        (Path(far_root) / "tests" / "fixtures" / "far_side" / "survivor.json").read_text(encoding="utf-8")
    )
    request["binocular"]["case"] = json.loads(
        (
            Path(binocular_root)
            / "tests"
            / "fixtures"
            / "binocular_recursion"
            / "lawful-residual.json"
        ).read_text(encoding="utf-8")
    )
    return request


class ResearchFormationTests(unittest.TestCase):
    def test_two_incubating_body_times_compose_without_promotion(self):
        request = load_request()
        original = copy.deepcopy(request)
        result = evaluate_research_formation_run(request, load_entries())

        self.assertEqual(request, original)
        self.assertEqual(result["schema"], "alex.research-formation-result/v0")
        self.assertEqual(result["run_id"], "formation-001")
        self.assertEqual(result["body_mode"], "EXPERIMENTAL")
        self.assertEqual(result["execution_state"], "COMPLETED")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["authority"], "none")

        far = result["far_side"]
        binocular = result["binocular"]
        bridge = result["bridge"]
        self.assertEqual(far["execution"]["receipt"]["body_time_id"], FAR_SIDE_ID)
        self.assertEqual(far["execution"]["receipt"]["organ_status"], "INCUBATING")
        self.assertEqual(binocular["execution"]["receipt"]["body_time_id"], BINOCULAR_ID)
        self.assertEqual(binocular["execution"]["receipt"]["organ_status"], "INCUBATING")
        self.assertNotEqual(
            far["execution"]["receipt"]["source_sha"],
            binocular["execution"]["receipt"]["source_sha"],
        )
        self.assertEqual(bridge["schema"], "alex.research-formation-bridge/v0")
        self.assertEqual(bridge["kind"], "DISCOVERY_TRIGGER_ONLY")
        self.assertEqual(bridge["from_stage"], "far_side")
        self.assertEqual(bridge["to_stage"], "binocular")
        self.assertEqual(bridge["authority"], "none")
        self.assertEqual(bridge["receipt_ref"], sha256_json(far["execution"]["receipt"]))

        expected_binocular_case = copy.deepcopy(original["binocular"]["case"])
        expected_binocular_case["discovery_trigger_refs"].append(bridge["receipt_ref"])
        self.assertEqual(
            binocular["execution"]["receipt"]["input_digest"],
            sha256_json(expected_binocular_case),
        )
        self.assertNotIn(bridge["receipt_ref"], expected_binocular_case["support_refs"])
        self.assertTrue(
            all(
                bridge["receipt_ref"] not in pass_record["compression"]["claim_support_refs"]
                for pass_record in expected_binocular_case["passes"]
            )
        )
        self.assertEqual(binocular["result"]["disposition"], "ACCEPT")
        self.assertEqual(binocular["result"]["terminal"], "RESIDUAL")

    def test_discovery_trigger_laundering_is_preserved_as_native_binocular_refusal(self):
        baseline = evaluate_research_formation_run(load_request(), load_entries())
        trigger_ref = baseline["bridge"]["receipt_ref"]

        request = load_request()
        request["binocular"]["case"]["passes"][0]["compression"]["claim_support_refs"].append(trigger_ref)
        result = evaluate_research_formation_run(request, load_entries())

        self.assertEqual(result["execution_state"], "COMPLETED")
        self.assertEqual(result["binocular"]["execution"]["execution_state"], "COMPLETED")
        self.assertEqual(result["binocular"]["execution"]["receipt"]["exit_code"], 1)
        self.assertEqual(result["binocular"]["result"]["disposition"], "REFUSE")
        self.assertEqual(
            result["binocular"]["result"]["reason_code"],
            "DISCOVERY_TRIGGER_AS_SUPPORT",
        )

    def test_far_side_body_mismatch_stops_before_binocular(self):
        request = load_request()
        request["materializations"][FAR_SIDE_ID] = request["materializations"][BINOCULAR_ID]
        result = evaluate_research_formation_run(request, load_entries())

        self.assertEqual(result["execution_state"], "REFUSED")
        self.assertIn(result["reason_code"], {"BODY_SHA_MISMATCH", "ENTRYPOINT_MISSING"})
        self.assertIsNone(result["bridge"])
        self.assertIsNone(result["binocular"])

    def test_present_only_never_falls_back_to_incubating_organs(self):
        request = load_request()
        request["body_mode"] = "PRESENT_ONLY"
        result = evaluate_research_formation_run(request, load_entries())

        self.assertEqual(result["execution_state"], "REFUSED")
        self.assertEqual(result["reason_code"], "BODY_MODE_MISMATCH")
        self.assertEqual(result["far_side"]["route"]["disposition"], "REFUSED")
        self.assertIsNone(result["bridge"])
        self.assertIsNone(result["binocular"])

    def test_binocular_materialization_failure_preserves_far_side_and_bridge(self):
        request = load_request()
        request["materializations"][BINOCULAR_ID] = request["materializations"][FAR_SIDE_ID]
        result = evaluate_research_formation_run(request, load_entries())

        self.assertEqual(result["far_side"]["execution"]["execution_state"], "COMPLETED")
        self.assertIsNotNone(result["bridge"])
        self.assertEqual(result["execution_state"], "REFUSED")
        self.assertIn(result["reason_code"], {"BODY_SHA_MISMATCH", "ENTRYPOINT_MISSING"})
        self.assertEqual(result["binocular"]["route"]["disposition"], "ROUTED")
        self.assertEqual(result["binocular"]["execution"]["execution_state"], "REFUSED")


if __name__ == "__main__":
    unittest.main()
