import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

from tools.crucible_blind import ruleset_digest

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "crucible" / "profiles" / "alex.runtime.loadout-handshake-m0.json"
RUNNER = ROOT / "tools" / "run_loadout_handshake_profile.py"
ADAPTER = ROOT / "tools" / "loadout_handshake_adapter.py"
SPECIMENS = ROOT / "crucible" / "specimens"
FIXTURE_IDS = [
    "loadout-handshake-valid",
    "loadout-handshake-stale-compile",
    "loadout-handshake-owner-drift",
    "loadout-handshake-permission-drift",
    "loadout-handshake-capability-gap",
]


class LoadoutHandshakeProfileManifestTests(unittest.TestCase):
    def test_gate_three_profile_pins_five_fixture_family(self):
        self.assertTrue(PROFILE.exists(), "Gate-3 profile must exist")
        self.assertTrue(ADAPTER.exists(), "real CASE-only handshake adapter must exist")
        self.assertTrue(RUNNER.exists(), "Gate-3 profile runner must exist")
        for fixture_id in FIXTURE_IDS:
            self.assertTrue((SPECIMENS / f"{fixture_id}.json").exists(), fixture_id)

        profile = json.loads(PROFILE.read_text(encoding="utf-8"))
        self.assertEqual(profile["id"], "alex.runtime/loadout-handshake-m0")
        self.assertEqual(profile["operation_types"], ["loadout_handshake"])
        self.assertEqual(profile["rule_profile"], "alex.runtime/loadout-handshake-m0")
        self.assertEqual(
            profile["fixture_families"],
            [{"id": "LOADOUT-HANDSHAKE-001", "version": 1, "fixtures": FIXTURE_IDS}],
        )
        self.assertEqual(profile["runtime_adapter"], {"path": "tools/loadout_handshake_adapter.py", "version": 1})
        self.assertEqual(
            profile["excluded_profiles"],
            ["alex.runtime/one-book-m1", "alex.runtime/formation-trace-m2"],
        )


class LoadoutHandshakeProfileExecutionTests(unittest.TestCase):
    def test_original_and_fresh_metamorphic_profile_passes_ten_cases(self):
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
        self.assertEqual(summary["profile"], "alex.runtime/loadout-handshake-m0")
        self.assertEqual(summary["ruleset_digest"], ruleset_digest("alex.runtime/loadout-handshake-m0"))
        self.assertEqual(summary["runtime_adapter"], "tools/loadout_handshake_adapter.py@1")
        self.assertEqual(summary["families"], {"LOADOUT-HANDSHAKE-001": 10})
        self.assertEqual(summary["passed"], 10)
        self.assertEqual(summary["failed"], 0)

    def test_metamorphic_handshake_surfaces_are_fresh_across_builds(self):
        spec = importlib.util.spec_from_file_location("loadout_profile_runner", RUNNER)
        self.assertIsNotNone(spec)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        specimen = json.loads((SPECIMENS / "loadout-handshake-valid.json").read_text(encoding="utf-8"))
        first = module.build_metamorphic_case(specimen)
        second = module.build_metamorphic_case(specimen)
        self.assertNotEqual(first["case_id"], second["case_id"])
        self.assertNotEqual(first["nonce"], second["nonce"])
        self.assertNotEqual(first["input_digest"], second["input_digest"])
        self.assertNotEqual(first["given"]["compile"]["compile_id"], second["given"]["compile"]["compile_id"])
        self.assertNotEqual(first["given"]["compile"]["compile_digest"], second["given"]["compile"]["compile_digest"])


if __name__ == "__main__":
    unittest.main()
