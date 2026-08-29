import copy
import json
import unittest
from pathlib import Path

from alex_runtime.binocular_recursion import evaluate_binocular_recursion_case

ROOT = Path(__file__).resolve().parents[1]
SPECIMENS = ROOT / "tests" / "fixtures" / "binocular_recursion"


def load_case(name: str = "lawful-residual.json") -> dict:
    return json.loads((SPECIMENS / name).read_text(encoding="utf-8"))


def stable_pass(template: dict, index: int, proposal: str, tension_type: str = "STABLE_MATCH") -> dict:
    pass_ = copy.deepcopy(template)
    pass_["pass_index"] = index
    pass_["compression"]["proposal_digest"] = proposal
    pass_["tensions"] = [{
        "type": tension_type,
        "left_refs": [proposal],
        "right_refs": ["c1"],
        "receipt_refs": [f"receipt:t{index}"],
    }]
    return pass_


def make_fixed_case() -> dict:
    case = load_case()
    template = copy.deepcopy(case["passes"][0])
    first = stable_pass(template, 0, "sha256:fixed-proposal")
    second = stable_pass(template, 1, "sha256:fixed-proposal")
    second["pre_field_digest"] = first["post_field_digest"]
    case["passes"] = [first, second]
    case["terminal"] = "FIXED"
    case["pass_limit"] = 4
    return case


def make_cycle_case() -> dict:
    case = load_case()
    template = copy.deepcopy(case["passes"][0])
    first = stable_pass(template, 0, "sha256:cycle-a")
    middle = stable_pass(template, 1, "sha256:cycle-b")
    last = stable_pass(template, 2, "sha256:cycle-a")
    middle["pre_field_digest"] = first["post_field_digest"]
    last["pre_field_digest"] = middle["post_field_digest"]
    case["passes"] = [first, middle, last]
    case["terminal"] = "CYCLE"
    case["pass_limit"] = 4
    return case


def make_divergent_case() -> dict:
    case = load_case()
    template = copy.deepcopy(case["passes"][0])
    first = stable_pass(template, 0, "sha256:div-a")
    middle = stable_pass(template, 1, "sha256:div-b", "BRANCH_DEPENDENCE")
    last = stable_pass(template, 2, "sha256:div-c", "UNEXPLAINED_RESIDUAL")
    middle["pre_field_digest"] = first["post_field_digest"]
    last["pre_field_digest"] = middle["post_field_digest"]
    case["passes"] = [first, middle, last]
    case["terminal"] = "DIVERGENT"
    case["pass_limit"] = 3
    return case


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

    def test_discovery_trigger_cannot_be_claim_support(self):
        case = load_case()
        case["passes"][0]["compression"]["claim_support_refs"].append("trigger:prompt-001")
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "DISCOVERY_TRIGGER_AS_SUPPORT"))

    def test_expansion_cannot_consume_undeclared_premise(self):
        case = load_case()
        case["passes"][0]["expansion"]["branches"][0]["used_premise_refs"] = ["p999"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "UNDECLARED_PREMISE_INJECTION"))

    def test_branch_local_introduced_premise_is_locally_legal(self):
        case = load_case()
        branch = case["passes"][0]["expansion"]["branches"][0]
        branch["used_premise_refs"] = ["local:p3"]
        branch["introduced_premise_refs"] = ["local:p3"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual(result["disposition"], "ACCEPT")

    def test_compression_cannot_erase_live_consequence(self):
        case = load_case()
        case["passes"][1]["compression"]["reexpanded_live_consequence_refs"] = ["c1"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "COMPRESSION_ERASED_LIVE_CONSEQUENCE"))

    def test_explicitly_withdrawn_consequence_may_leave_reexpansion_surface(self):
        case = load_case()
        case["passes"][1]["compression"]["reexpanded_live_consequence_refs"] = ["c1"]
        case["passes"][1]["update"] = {"kind": "EVIDENCE_ADDED", "receipt_refs": ["receipt:withdraw-c2"], "admit_premise_refs": [], "withdraw_premise_refs": [], "withdraw_consequence_refs": ["c2"], "authority_digest": "sha256:authority-0"}
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual(result["disposition"], "ACCEPT")

    def test_missing_compression_is_one_eye_collapse(self):
        case = load_case()
        del case["passes"][0]["compression"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "ONE_EYE_COLLAPSE"))

    def test_material_trajectory_must_preserve_ordered_path(self):
        case = load_case()
        case["passes"][0]["trajectory"] = []
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TRAJECTORY_NOT_PRESERVED"))

    def test_material_trajectory_repetitions_survive_validation(self):
        case = load_case()
        evaluate_binocular_recursion_case(case)
        self.assertEqual(case["passes"][0]["trajectory"], ["A", "B", "A"])

    def test_broken_pass_ancestry_is_refused(self):
        case = load_case()
        case["passes"][1]["pre_field_digest"] = "sha256:unrelated-field"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "BROKEN_PASS_ANCESTRY"))

    def test_field_change_without_update_receipt_is_refused(self):
        case = load_case()
        case["passes"][0]["post_field_digest"] = "sha256:field-1"
        case["passes"][1]["pre_field_digest"] = "sha256:field-1"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "UNATTRIBUTED_UPDATE"))

    def test_authority_may_not_change_inside_update(self):
        case = load_case()
        case["passes"][0]["update"]["authority_digest"] = "sha256:authority-changed"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("REFUSE", "AUTHORITY_CHANGED"))

    def test_pass_limit_must_be_positive_integer(self):
        case = load_case()
        case["pass_limit"] = 0
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "INVALID_PASS_LIMIT"))

    def test_unknown_tension_type_is_insufficient(self):
        case = load_case()
        case["passes"][0]["tensions"][0]["type"] = "MYSTERY"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "UNKNOWN_TENSION_TYPE"))

    def test_unknown_branch_status_is_insufficient(self):
        case = load_case()
        case["passes"][0]["expansion"]["branches"][0]["status"] = "MYSTERY"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "UNKNOWN_BRANCH_STATUS"))

    def test_unknown_update_kind_is_insufficient(self):
        case = load_case()
        case["passes"][0]["update"]["kind"] = "MYSTERY"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "UNKNOWN_UPDATE_KIND"))

    def test_malformed_branch_envelope_is_insufficient(self):
        case = load_case()
        del case["passes"][0]["expansion"]["branches"][0]["used_premise_refs"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "MALFORMED_PASS"))

    def test_fixed_requires_last_two_equal_states_under_same_profiles(self):
        result = evaluate_binocular_recursion_case(make_fixed_case())
        self.assertEqual((result["disposition"], result["terminal"]), ("ACCEPT", "FIXED"))

    def test_fixed_fails_when_compression_profile_changes(self):
        case = make_fixed_case()
        case["passes"][-1]["compression"]["profile_digest"] = "sha256:compress-v2"
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_cycle_requires_repeated_state_with_distinct_intervening_state(self):
        result = evaluate_binocular_recursion_case(make_cycle_case())
        self.assertEqual((result["disposition"], result["terminal"]), ("ACCEPT", "CYCLE"))

    def test_cycle_fails_without_repeated_state(self):
        case = make_cycle_case()
        case["passes"][2]["compression"]["proposal_digest"] = "sha256:cycle-c"
        case["passes"][2]["tensions"][0]["left_refs"] = ["sha256:cycle-c"]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_residual_requires_final_nonstable_tension(self):
        case = load_case()
        case["passes"][-1]["tensions"] = [{"type": "STABLE_MATCH", "left_refs": ["sha256:proposal-1"], "right_refs": ["c1", "c2"], "receipt_refs": ["receipt:stable"]}]
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_divergent_requires_reaching_declared_bound(self):
        case = make_divergent_case()
        case["pass_limit"] = 4
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))

    def test_divergent_rejects_repeated_state(self):
        case = make_divergent_case()
        case["passes"][2]["compression"] = copy.deepcopy(case["passes"][0]["compression"])
        case["passes"][2]["expansion"] = copy.deepcopy(case["passes"][0]["expansion"])
        case["passes"][2]["tensions"] = copy.deepcopy(case["passes"][0]["tensions"])
        result = evaluate_binocular_recursion_case(case)
        self.assertEqual((result["disposition"], result["reason_code"]), ("INSUFFICIENT_TO_TEST", "TERMINAL_NOT_DEMONSTRATED"))


if __name__ == "__main__":
    unittest.main()
