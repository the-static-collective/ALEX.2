import importlib
import importlib.util
import unittest


class NameResultTransportProbeTests(unittest.TestCase):
    def test_json_round_trip_is_observationally_indistinguishable_to_family_gate(self):
        spec = importlib.util.find_spec("experiments.name_result_transport_probe")
        self.assertIsNotNone(spec, "transport probe module must exist")

        module = importlib.import_module("experiments.name_result_transport_probe")
        result = module.run_probe()

        self.assertEqual(result["schema"], "alex.experiment.name-result-transport-probe/v0")
        self.assertEqual(result["original_gate_disposition"], "DIVE_READY")
        self.assertEqual(result["round_trip_gate_disposition"], "DIVE_READY")
        self.assertTrue(result["gate_observation_equal"])
        self.assertFalse(result["object_identity_preserved"])
        self.assertEqual(result["finding"], "SERIALIZATION_NOT_DETECTABLE_BY_GATE")
        self.assertEqual(result["authority"], "none")


if __name__ == "__main__":
    unittest.main()
