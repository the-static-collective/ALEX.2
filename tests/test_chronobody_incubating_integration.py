import json
import os
import unittest
from pathlib import Path

from alex_runtime.chronobody import BodyMode, execute_body, parse_registry, resolve_body


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "chronobody" / "registry.v0.json"
FAR_SIDE_ID = "far-side-pass@52c678767017c170506ce1895d3a610b6ef115b4"
BINOCULAR_ID = "binocular-recursion@c26620efc3c601eb0686825e1cfcbe1f1951f49e"


def load_entries():
    return parse_registry(json.loads(REGISTRY_PATH.read_text(encoding="utf-8")))


class ChronobodyIncubatingIntegrationTests(unittest.TestCase):
    def test_exact_far_side_body_executes_without_promotion(self):
        root_value = os.environ.get("ALEX_FAR_SIDE_BODY_ROOT")
        if not root_value:
            self.skipTest("ALEX_FAR_SIDE_BODY_ROOT not supplied")

        entries = load_entries()
        route = resolve_body(
            entries,
            "far_side_pressure",
            BodyMode.EXPERIMENTAL,
            body_time_id=FAR_SIDE_ID,
        )
        self.assertEqual(route.disposition, "ROUTED")
        self.assertEqual(route.entry.status.value, "INCUBATING")

        body_root = Path(root_value)
        fixture = json.loads(
            (body_root / "tests" / "fixtures" / "far_side" / "survivor.json").read_text(encoding="utf-8")
        )
        result = execute_body(route.entry, body_root, fixture, BodyMode.EXPERIMENTAL)

        self.assertEqual(result.execution_state, "COMPLETED", result.stderr)
        self.assertEqual(result.receipt["body_time_id"], FAR_SIDE_ID)
        self.assertEqual(result.receipt["organ_status"], "INCUBATING")
        self.assertEqual(result.receipt["authority"], "none")
        self.assertIsInstance(result.output, dict)
        self.assertEqual(result.output["case_id"], "far-side:residual-topology-survivor")
        self.assertEqual(result.output["final_status"], "FAR_SIDE_SURVIVOR")
        self.assertIn("novelty_delta", result.output)
        self.assertIn("receipt_survivors", result.output)
        self.assertNotIn("promotion", result.receipt)

    def test_exact_binocular_body_executes_without_promotion(self):
        root_value = os.environ.get("ALEX_BINOCULAR_BODY_ROOT")
        if not root_value:
            self.skipTest("ALEX_BINOCULAR_BODY_ROOT not supplied")

        entries = load_entries()
        route = resolve_body(
            entries,
            "binocular_formation_audit",
            BodyMode.EXPERIMENTAL,
            body_time_id=BINOCULAR_ID,
        )
        self.assertEqual(route.disposition, "ROUTED")
        self.assertEqual(route.entry.status.value, "INCUBATING")

        body_root = Path(root_value)
        fixture = json.loads(
            (body_root / "tests" / "fixtures" / "binocular_recursion" / "lawful-residual.json").read_text(encoding="utf-8")
        )
        result = execute_body(route.entry, body_root, fixture, BodyMode.EXPERIMENTAL)

        self.assertEqual(result.execution_state, "COMPLETED", result.stderr)
        self.assertEqual(result.receipt["body_time_id"], BINOCULAR_ID)
        self.assertEqual(result.receipt["organ_status"], "INCUBATING")
        self.assertEqual(result.receipt["authority"], "none")
        self.assertEqual(result.output["schema"], "alex.binocular-recursion-result/v0")
        self.assertEqual(result.output["disposition"], "ACCEPT")
        self.assertEqual(result.output["terminal"], "RESIDUAL")
        self.assertNotIn("promotion", result.receipt)


if __name__ == "__main__":
    unittest.main()
