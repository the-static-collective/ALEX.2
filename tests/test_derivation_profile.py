import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.crucible_blind import ruleset_digest

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "crucible" / "profiles" / "alex.runtime.derivation-m0.json"
SCHEMA = ROOT / "crucible" / "schema" / "conformance-profile.schema.json"
RUNNER = ROOT / "tools" / "run_derivation_profile.py"


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
