import inspect
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import tools.crucible as crucible
from tools.crucible_blind import build_case, build_oracle, ruleset_digest

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "tools" / "crucible.py"
FIXTURES = ROOT / "tests" / "fixtures"


class RunnerContractTests(unittest.TestCase):
    def specimen(self) -> dict:
        return {
            "id": "search-absence",
            "title": "temporary search absence specimen",
            "constitutional_laws": ["SEARCH MISS != ABSENCE"],
            "given": {"search_observation": "S1"},
            "attempt": {"promote": "source_absence"},
            "expected": {
                "disposition": "REFUSE",
                "refusal_code": "SEARCH_COVERAGE_INSUFFICIENT",
                "required_receipt_survivors": ["search_observation:S1"],
                "forbidden_promotions": ["source_absence"],
            },
            "version": 1,
        }

    def case_and_oracle(self):
        case = build_case(self.specimen(), nonce="runner-test")
        oracle = build_oracle(self.specimen(), case)
        return case, oracle

    def valid_result(self) -> dict:
        case, _ = self.case_and_oracle()
        return {
            "case_id": case["case_id"],
            "input_digest": case["input_digest"],
            "ruleset_digest": ruleset_digest(case["rule_profile"]),
            "disposition": "REFUSE",
            "reason_code": "SEARCH_COVERAGE_INSUFFICIENT",
            "receipt_survivors": ["search_observation:S1"],
            "derived_assertions": [],
            "execution_trace_summary": {"terminal_state": "FINISHED", "step_count": 1},
        }

    def require_new_runner_api(self):
        self.assertTrue(
            hasattr(crucible, "validate_runtime_result"),
            "runner must validate runtime identity/result shape before ORACLE scoring",
        )
        self.assertEqual(
            list(inspect.signature(crucible.compare_result).parameters),
            ["case", "oracle", "actual"],
        )

    def test_valid_runtime_result_passes_identity_validation_and_oracle_scoring(self):
        self.require_new_runner_api()
        case, oracle = self.case_and_oracle()
        actual = self.valid_result()
        self.assertEqual(crucible.validate_runtime_result(case, actual), [])
        self.assertEqual(crucible.compare_result(case, oracle, actual), [])

    def test_mismatched_input_digest_is_rejected(self):
        self.require_new_runner_api()
        case, _ = self.case_and_oracle()
        actual = self.valid_result()
        actual["input_digest"] = "sha256:" + "0" * 64
        self.assertIn("input_digest mismatch", crucible.validate_runtime_result(case, actual))

    def test_mismatched_ruleset_digest_is_rejected(self):
        self.require_new_runner_api()
        case, _ = self.case_and_oracle()
        actual = self.valid_result()
        actual["ruleset_digest"] = ruleset_digest("stale-profile")
        self.assertIn("ruleset_digest mismatch", crucible.validate_runtime_result(case, actual))

    def test_wrong_case_identity_is_rejected(self):
        self.require_new_runner_api()
        case, _ = self.case_and_oracle()
        actual = self.valid_result()
        actual["case_id"] = "foreign-case"
        self.assertIn("case_id mismatch", crucible.validate_runtime_result(case, actual))

    def test_malformed_execution_summary_is_rejected(self):
        self.require_new_runner_api()
        case, _ = self.case_and_oracle()
        actual = self.valid_result()
        actual["execution_trace_summary"] = {"terminal_state": "REFUSE", "step_count": -1}
        errors = crucible.validate_runtime_result(case, actual)
        joined = " ".join(errors)
        self.assertIn("terminal_state", joined)
        self.assertIn("step_count", joined)

    def test_missing_required_survivor_and_forbidden_output_are_rejected(self):
        self.require_new_runner_api()
        case, oracle = self.case_and_oracle()
        actual = self.valid_result()
        actual["receipt_survivors"] = []
        actual["derived_assertions"] = ["source_absence"]
        errors = crucible.compare_result(case, oracle, actual)
        joined = " ".join(errors)
        self.assertIn("search_observation:S1", joined)
        self.assertIn("source_absence", joined)

    def test_extra_runtime_result_key_is_rejected(self):
        self.require_new_runner_api()
        case, _ = self.case_and_oracle()
        actual = self.valid_result()
        actual["admitted"] = True
        errors = crucible.validate_runtime_result(case, actual)
        self.assertTrue(any("unexpected result key" in error for error in errors), errors)

    def test_duplicate_runtime_result_members_are_rejected(self):
        self.require_new_runner_api()
        case, _ = self.case_and_oracle()
        actual = self.valid_result()
        actual["receipt_survivors"] = ["search_observation:S1", "search_observation:S1"]
        actual["derived_assertions"] = ["candidate:X", "candidate:X"]
        errors = crucible.validate_runtime_result(case, actual)
        joined = " ".join(errors)
        self.assertIn("receipt_survivors must contain unique strings", joined)
        self.assertIn("derived_assertions must contain unique strings", joined)


class ProcessRunnerTests(unittest.TestCase):
    def write_specimen(self, directory: str) -> Path:
        path = Path(directory) / "specimen.json"
        path.write_text(json.dumps(RunnerContractTests().specimen()), encoding="utf-8")
        return path

    def run_adapter(self, adapter_name: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmp:
            fixture = self.write_specimen(tmp)
            return subprocess.run(
                [
                    sys.executable,
                    str(CLI),
                    "--fixture",
                    str(fixture),
                    "--adapter",
                    sys.executable,
                    str(FIXTURES / adapter_name),
                ],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )

    def test_accepts_everything_adapter_exits_one(self):
        result = self.run_adapter("adapter_accepts_everything.py")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL search-absence", result.stdout)

    def test_required_refusal_adapter_exits_zero(self):
        result = self.run_adapter("adapter_refuses_correctly.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS search-absence", result.stdout)

    def test_answer_echo_cheater_cannot_recover_oracle_from_stdin(self):
        result = self.run_adapter("adapter_answer_echo_cheater.py")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("FAIL search-absence", result.stdout)

    def test_id_switch_cheater_is_rejected(self):
        result = self.run_adapter("adapter_id_switch_cheater.py")
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn("case_id mismatch", result.stdout)


class CanonicalFixtureLoadingTests(unittest.TestCase):
    def test_every_canonical_fixture_is_parseable(self):
        specimens = ROOT / "crucible" / "specimens"
        paths = sorted(specimens.glob("*.json"))
        self.assertTrue(paths)
        for path in paths:
            specimen = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(specimen["id"], path.stem)
            self.assertIn("expected", specimen)
            self.assertIn("required_receipt_survivors", specimen["expected"])


class ConformanceBoundaryTests(unittest.TestCase):
    def test_readme_states_contract_is_not_runtime_conformance(self):
        readme = (ROOT / "crucible" / "README.md").read_text(encoding="utf-8")
        sentence = (
            "Passing `crucible-contract` proves the fixture corpus and reference harness are internally consistent. "
            "It does not prove an ALEX runtime conforms. Runtime conformance begins only when a real adapter "
            "executes the applicable fixtures and the harness reports zero constitutional mismatches."
        )
        self.assertIn(sentence, readme)

    def test_ci_workflow_runs_contract_tests(self):
        workflow = (ROOT / ".github" / "workflows" / "crucible.yml").read_text(encoding="utf-8")
        self.assertIn("name: crucible-contract", workflow)
        self.assertIn("python -m unittest discover -s tests -v", workflow)


if __name__ == "__main__":
    unittest.main()
