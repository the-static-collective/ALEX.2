import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.crucible_blind import build_case, ruleset_digest
from tools.run_derivation_profile import _prepare_metamorphic_case

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "crucible" / "profiles" / "alex.runtime.derivation-m0.json"
SCHEMA = ROOT / "crucible" / "schema" / "conformance-profile.schema.json"
RUNNER = ROOT / "tools" / "run_derivation_profile.py"
SPECIMENS = ROOT / "crucible" / "specimens"


class DerivationProfileManifestTests(unittest.TestCase):
    def test_profile_schema_and_manifest_pin_gate_two_scope(self):
        self.assertTrue(SCHEMA.exists(), "conformance profile schema must exist")
        self.assertTrue(PROFILE.exists(), "derivation m0 profile must exist")

        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        self.assertEqual(schema["$schema"], "https://json-schema.org/draft/2020-12/schema")
        self.assertFalse(schema["additionalProperties"])

        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        self.assertEqual(profile["id"], "alex.runtime/derivation-m0")
        self.assertEqual(profile["operation_types"], ["relation_derivation"])
        self.assertEqual(profile["rule_profile"], "alex.runtime/derivation-m0")
        self.assertEqual(
            profile["fixture_families"],
            [
                {
                    "id": "RELATION-DERIVATION-001",
                    "version": 1,
                    "fixtures": [
                        "relation-derivation-001-attention-negative",
                        "relation-derivation-001-evidence-positive",
                    ],
                }
            ],
        )
        self.assertEqual(
            profile["runtime_adapter"],
            {"path": "tools/derivation_adapter.py", "version": 1},
        )
        self.assertEqual(
            profile["excluded_profiles"],
            ["alex.runtime/one-book-m1", "alex.runtime/formation-trace-m2"],
        )
        self.assertNotIn("ruleset_digest", profile)


class DerivationProfileExecutionTests(unittest.TestCase):
    def test_metamorphic_siblings_are_fresh_across_builds(self):
        specimen = json.loads(
            (SPECIMENS / "relation-derivation-001-evidence-positive.json").read_text(encoding="utf-8")
        )
        case = build_case(
            specimen,
            nonce="parent-nonce",
            operation_type="relation_derivation",
            rule_profile="alex.runtime/derivation-m0",
        )

        first = _prepare_metamorphic_case(case, specimen["id"])
        second = _prepare_metamorphic_case(case, specimen["id"])

        self.assertNotEqual(first["case_id"], second["case_id"])
        self.assertNotEqual(first["nonce"], second["nonce"])
        self.assertNotEqual(first["input_digest"], second["input_digest"])
        first_distractors = {r["id"] for r in first["given"]["relations"] if r["predicate"] == "derived_from"}
        second_distractors = {r["id"] for r in second["given"]["relations"] if r["predicate"] == "derived_from"}
        self.assertTrue(first_distractors.isdisjoint(second_distractors))

    def test_original_and_metamorphic_profile_passes_four_cases(self):
        result = subprocess.run(
            [sys.executable, str(RUNNER)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        lines = [line for line in result.stdout.splitlines() if line.strip()]
        self.assertTrue(lines, result.stdout + result.stderr)
        summary = json.loads(lines[-1])
        self.assertEqual(summary["profile"], "alex.runtime/derivation-m0")
        self.assertEqual(summary["ruleset_digest"], ruleset_digest("alex.runtime/derivation-m0"))
        self.assertEqual(summary["runtime_adapter"], "tools/derivation_adapter.py@1")
        self.assertEqual(summary["families"], {"RELATION-DERIVATION-001": 4})
        self.assertEqual(summary["passed"], 4)
        self.assertEqual(summary["failed"], 0)


if __name__ == "__main__":
    unittest.main()
