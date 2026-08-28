from __future__ import annotations

import copy
import unittest

from alex_runtime.handshake import compile_payload_digest
from alex_runtime.local_support import evaluate_local_support_case


def make_compile() -> dict:
    record = {
        "schema": "loadout.compile/v0",
        "compile_id": "C0",
        "parent_compile_id": None,
        "issued_at": "2026-08-28T13:00:00Z",
        "expires_at": "2026-08-28T14:00:00Z",
        "world_cut_ref": "world-cut:R0",
        "context_pack_ref": "context-pack:R0",
        "compile_trace": {"id": "compile-trace:C0"},
        "capability_bindings": [],
        "effect_fence_ref": "effect-fence:EF0",
        "effective_effects": [],
        "owner_evidence_digest": "sha256:" + "a" * 64,
        "egress_policy_ref": "egress-policy:E0",
    }
    record["compile_digest"] = compile_payload_digest(record)
    return record


def make_case(*, visible: list[str] | None = None) -> dict:
    compile_record = make_compile()
    projection_digest = "sha256:" + "b" * 64
    return {
        "case_id": "local-support-fixture",
        "operation_type": "local_support",
        "rule_profile": "alex.runtime/local-support-m0",
        "given": {
            "records": [
                {"id": "evidence-e1", "kind": "evidence"},
                {"id": "claim-token", "kind": "claim"},
            ],
            "evidence_paths": [
                {
                    "id": "path:P1",
                    "source_id": "evidence-e1",
                    "claim_id": "claim-token",
                    "status": "ATTRIBUTABLE",
                    "basis_ids": ["evidence-e1"],
                    "witness_ids": ["witness:fixture"],
                }
            ],
            "relations": [],
            "projection_handoff": {
                "schema": "mortal_actor.3rdi-handoff/v0",
                "projection_digest": projection_digest,
                "field_id": "passage-world-001",
                "cut_id": "ROAD-A",
                "observer": "road-a",
                "visible_occurrence_ids": list(visible or []),
            },
            "evaluation_compile": compile_record,
        },
        "attempt": {
            "claim_id": "Q-PASSAGE",
            "expected_projection_digest": projection_digest,
            "expected_evaluation_compile_id": "C0",
            "expected_evaluation_compile_digest": compile_record["compile_digest"],
            "relation_proposal": {
                "id": "proposal:P1",
                "subject_id": "evidence-e1",
                "predicate": "SUPPORTS",
                "object_id": "claim-token",
                "scope": "passage-world-test",
                "basis_ids": ["evidence-e1", "path:P1"],
            },
            "evaluation_id": "evaluation:E1",
            "execution_step_id": "step:S1",
            "conclusion_assertion_id": "conclusion:C1",
        },
    }


class LocalSupportProfileTests(unittest.TestCase):
    def test_basis_outside_projection_stops_before_semantic_derivation(self) -> None:
        result = evaluate_local_support_case(make_case(visible=[]))
        self.assertEqual(result["local_disposition"], "basis_outside_projection")
        self.assertEqual(result["missing_local_basis_ids"], ["evidence-e1"])
        self.assertIsNone(result["derivation"])

    def test_visible_attributable_basis_delegates_to_existing_support_kernel(self) -> None:
        result = evaluate_local_support_case(make_case(visible=["evidence-e1"]))
        self.assertEqual(result["profile"], "alex.runtime/local-support-m0")
        self.assertEqual(result["rule_id"], "LOCAL-SUPPORT-001")
        self.assertEqual(result["claim_id"], "Q-PASSAGE")
        self.assertEqual(result["cut_id"], "ROAD-A")
        self.assertEqual(result["local_disposition"], "local_basis_accept")
        self.assertEqual(result["derivation"]["evaluation"]["disposition"], "ACCEPT")
        self.assertEqual(result["derivation"]["conclusion_assertion"]["predicate"], "SUPPORTS")

    def test_projection_and_compile_mismatch_stop_before_derivation(self) -> None:
        projection = make_case(visible=["evidence-e1"])
        projection["attempt"]["expected_projection_digest"] = "sha256:" + "0" * 64
        result = evaluate_local_support_case(projection)
        self.assertEqual(result["local_disposition"], "projection_mismatch")
        self.assertIsNone(result["derivation"])

        compile_case = make_case(visible=["evidence-e1"])
        compile_case["attempt"]["expected_evaluation_compile_id"] = "FOREIGN"
        result = evaluate_local_support_case(compile_case)
        self.assertEqual(result["local_disposition"], "compile_mismatch")
        self.assertIsNone(result["derivation"])

    def test_missing_attributable_path_remains_unresolved_not_support(self) -> None:
        case = make_case(visible=["evidence-e1"])
        case["given"]["evidence_paths"] = []
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "local_basis_unresolved")
        self.assertEqual(result["reason_code"], "NO_ATTRIBUTABLE_SUPPORT_PATH")

    def test_claim_identity_is_explicit_and_truth_or_authority_never_appear(self) -> None:
        case = make_case(visible=["evidence-e1"])
        case["attempt"]["claim_id"] = ""
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "local_basis_unresolved")
        self.assertEqual(result["reason_code"], "CLAIM_ID_REQUIRED")

        result = evaluate_local_support_case(make_case(visible=["evidence-e1"]))
        encoded = repr(result).lower()
        for forbidden in ("global_truth", "authority", "canon", "publication", "side_effect"):
            self.assertNotIn(forbidden, encoded)

    def test_router_or_relevance_names_cannot_mint_support_without_path(self) -> None:
        case = make_case(visible=["evidence-e1"])
        case["given"]["evidence_paths"] = []
        case["given"]["evaluation_compile"]["capability_bindings"] = [
            {"capability": "source.red-note", "status": "available"}
        ]
        case["given"]["evaluation_compile"]["compile_digest"] = compile_payload_digest(
            case["given"]["evaluation_compile"]
        )
        case["attempt"]["expected_evaluation_compile_digest"] = case["given"]["evaluation_compile"]["compile_digest"]
        case["given"]["projection_handoff"]["visible_relevance_edge_ids"] = ["relevance:red-note"]
        result = evaluate_local_support_case(case)
        self.assertNotEqual(result["local_disposition"], "local_basis_accept")


if __name__ == "__main__":
    unittest.main()
