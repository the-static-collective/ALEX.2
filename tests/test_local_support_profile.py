from __future__ import annotations

import copy
import unittest

from alex_runtime.handshake import compile_payload_digest
from alex_runtime.local_support import LOCAL_SUPPORT_PROFILE, evaluate_local_support_case


def make_compile() -> dict:
    record = {
        "schema": "loadout.compile/v0",
        "compile_id": "C0",
        "parent_compile_id": None,
        "issued_at": "2026-08-27T13:00:00Z",
        "expires_at": "2026-08-27T14:00:00Z",
        "world_cut_ref": "world-cut:room-before-merge",
        "context_pack_ref": "context-pack:room-a0",
        "compile_trace": {
            "id": "compile-trace:C0",
            "source_world_ref": "world-source:MA0",
            "operation": "bounded-selection",
            "preserved_invariants": ["mortal-aperture"],
            "declared_loss": [],
            "producer": "local-support-test@1",
            "freshness": "2026-08-27T13:00:00Z",
        },
        "capability_bindings": [{"capability": "alex.evaluate", "status": "available"}],
        "effect_fence_ref": "effect-fence:EF0",
        "effective_effects": [],
        "owner_evidence_digest": "sha256:" + "a" * 64,
        "egress_policy_ref": "egress-policy:E0",
    }
    record["compile_digest"] = compile_payload_digest(record)
    return record


def make_projection(*visible: str, cut_id: str = "A0", observer: str = "A", digest: str = "sha256:projection-a0") -> dict:
    return {
        "schema": "mortal_actor.3rdi-handoff/v0",
        "projection_digest": digest,
        "field_id": "four-witnesses-one-room",
        "cut_id": cut_id,
        "observer": observer,
        "visible_occurrence_ids": list(visible),
        "visible_causal_edge_ids": [],
        "visible_relevance_edge_ids": [],
        "contact_ids": [],
        "attention_event_ids": [],
        "decoder_application_ids": [],
        "stance_ids": [],
    }


def make_case(*, claim_id: str, source_id: str, object_id: str, path_id: str | None, projection: dict) -> dict:
    compile_record = make_compile()
    records = [
        {"id": source_id, "kind": "evidence"},
        {"id": object_id, "kind": "claim"},
    ]
    evidence_paths = []
    proposal_basis = [source_id]
    if path_id is not None:
        evidence_paths.append({
            "id": path_id,
            "source_id": source_id,
            "claim_id": object_id,
            "status": "ATTRIBUTABLE",
            "basis_ids": [source_id],
            "witness_ids": [f"witness:{claim_id}"],
        })
        proposal_basis.append(path_id)
    return {
        "operation_type": "local_support",
        "rule_profile": LOCAL_SUPPORT_PROFILE,
        "given": {
            "records": records,
            "evidence_paths": evidence_paths,
            "relations": [],
            "projection_handoff": copy.deepcopy(projection),
            "evaluation_compile": compile_record,
        },
        "attempt": {
            "claim_id": claim_id,
            "expected_projection_digest": projection["projection_digest"],
            "expected_evaluation_compile_id": compile_record["compile_id"],
            "expected_evaluation_compile_digest": compile_record["compile_digest"],
            "relation_proposal": {
                "id": f"RP-{claim_id}",
                "subject_id": source_id,
                "predicate": "SUPPORTS",
                "object_id": object_id,
                "scope": f"candidate_claim:{object_id}",
                "basis_ids": proposal_basis,
            },
            "evaluation_id": f"EV-{claim_id}",
            "execution_step_id": f"STEP-{claim_id}",
            "conclusion_assertion_id": f"AS-{claim_id}",
        },
        "input_digest": "sha256:" + "b" * 64,
    }


def all_keys(value):
    if isinstance(value, dict):
        for key, child in value.items():
            yield key
            yield from all_keys(child)
    elif isinstance(value, list):
        for child in value:
            yield from all_keys(child)


class LocalSupportProfileTests(unittest.TestCase):
    def test_global_path_outside_projection_is_not_actor_support(self):
        case = make_case(
            claim_id="Q1", source_id="red-note-placed", object_id="claim-red-note-was-present",
            path_id="EP-Q1", projection=make_projection("mirror-scratch"),
        )
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "basis_outside_projection")
        self.assertEqual(result["missing_local_basis_ids"], ["red-note-placed"])
        self.assertIsNone(result["derivation"])

    def test_same_support_path_accepts_when_locally_visible(self):
        projection = make_projection("red-note-placed", cut_id="R0", observer="R", digest="sha256:projection-r0")
        case = make_case(
            claim_id="Q1", source_id="red-note-placed", object_id="claim-red-note-was-present",
            path_id="EP-Q1", projection=projection,
        )
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "local_basis_accept")
        self.assertEqual(result["derivation"]["evaluation"]["disposition"], "ACCEPT")
        self.assertEqual(result["claim_id"], "Q1")
        self.assertEqual(result["cut_id"], "R0")
        self.assertEqual(result["projection_digest"], "sha256:projection-r0")
        self.assertEqual(result["compile_id"], "C0")

    def test_locally_acceptable_case_contains_no_global_answer(self):
        projection = make_projection("lamp-flicker", cut_id="N0", observer="N", digest="sha256:projection-n0")
        case = make_case(
            claim_id="Q2", source_id="lamp-flicker", object_id="claim-door-is-unlocked",
            path_id="EP-Q2", projection=projection,
        )
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "local_basis_accept")
        self.assertNotIn("truth", set(all_keys(result)))
        self.assertNotIn("global_truth", str(case))

    def test_missing_attributable_path_remains_unresolved(self):
        projection = make_projection("mirror-scratch")
        case = make_case(
            claim_id="Q3", source_id="mirror-scratch", object_id="claim-red-note-author",
            path_id=None, projection=projection,
        )
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "local_basis_unresolved")
        self.assertEqual(result["reason_code"], "NO_ATTRIBUTABLE_SUPPORT_PATH")

    def test_projection_and_compile_mismatch_block_semantic_derivation(self):
        case = make_case(
            claim_id="Q1", source_id="red-note-placed", object_id="claim-red-note-was-present",
            path_id="EP-Q1", projection=make_projection("red-note-placed"),
        )
        bad_projection = copy.deepcopy(case)
        bad_projection["attempt"]["expected_projection_digest"] = "sha256:foreign"
        result = evaluate_local_support_case(bad_projection)
        self.assertEqual(result["local_disposition"], "projection_mismatch")
        self.assertIsNone(result["derivation"])

        bad_compile = copy.deepcopy(case)
        bad_compile["attempt"]["expected_evaluation_compile_id"] = "FOREIGN"
        result = evaluate_local_support_case(bad_compile)
        self.assertEqual(result["local_disposition"], "compile_mismatch")
        self.assertIsNone(result["derivation"])

    def test_claim_identity_is_never_inferred(self):
        case = make_case(
            claim_id="Q1", source_id="red-note-placed", object_id="claim-red-note-was-present",
            path_id="EP-Q1", projection=make_projection("red-note-placed"),
        )
        case["attempt"]["claim_id"] = ""
        result = evaluate_local_support_case(case)
        self.assertEqual(result["local_disposition"], "local_basis_unresolved")
        self.assertEqual(result["reason_code"], "CLAIM_ID_REQUIRED")

    def test_a0_a1_supportability_changes_without_rewriting_a0(self):
        a0 = make_case(
            claim_id="Q5", source_id="red-note-placed", object_id="claim-a-can-now-identify-note",
            path_id="EP-Q5", projection=make_projection("mirror-scratch", cut_id="A0", observer="A", digest="sha256:a0"),
        )
        a1 = make_case(
            claim_id="Q5", source_id="red-note-placed", object_id="claim-a-can-now-identify-note",
            path_id="EP-Q5", projection=make_projection("mirror-scratch", "red-note-placed", cut_id="A1", observer="A", digest="sha256:a1"),
        )
        self.assertEqual(evaluate_local_support_case(a0)["local_disposition"], "basis_outside_projection")
        self.assertEqual(evaluate_local_support_case(a1)["local_disposition"], "local_basis_accept")
        self.assertEqual(evaluate_local_support_case(a0)["local_disposition"], "basis_outside_projection")

    def test_result_contains_no_authority_or_consequence_semantics(self):
        case = make_case(
            claim_id="Q1", source_id="red-note-placed", object_id="claim-red-note-was-present",
            path_id="EP-Q1", projection=make_projection("red-note-placed"),
        )
        result = evaluate_local_support_case(case)
        forbidden = {"authority", "canon", "admitted", "publication", "execute", "side_effect", "truth", "global_truth"}
        self.assertTrue(forbidden.isdisjoint(set(all_keys(result))))


if __name__ == "__main__":
    unittest.main()
