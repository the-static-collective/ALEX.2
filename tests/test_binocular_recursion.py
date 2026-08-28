import copy
import json
import unittest
from pathlib import Path

from alex_runtime.binocular_recursion import evaluate_binocular_recursion_case

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "tests" / "fixtures" / "binocular_recursion"


def load_case(name: str = "lawful-residual.json") -> dict:
    return json.loads((SPECIMENS / name).read_text(encoding="utf-8"))


class BinocularRecursionTests(unittest.TestCase):
    def test_lawful_dual_layer_residual_is_accepted(self):
        result = evaluate_binocular_recursion_case(load_case())
        self.assertEqual(result["schema"], "alex.binocular-recursion-result/v0")
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertIsNone(result["reason_code"])
        self.assertEqual(result["terminal"], "RESIDUAL")
        self.assertEqual(result["validated_passes"], 2)
        self.assertIn("UNEXPLAINED_RESIDUAL", result["tension_types"])
        self.assertEqual(result["authority_digest"], "sha256:authority-0")

    def test_evaluator_does_not_mutate_source_case(self):
        case = load_case()
        before = copy.deepcopy(case)
        evaluate_binocular_recursion_case(case)
        self.assertEqual(case, before)


if __name__ == "__main__":
    unittest.main()
