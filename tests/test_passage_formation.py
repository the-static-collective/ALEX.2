from __future__ import annotations

import copy
import unittest

from alex_runtime.passage_formation import bind_passage_formation


def bundle(
    *,
    road_id: str,
    projection_hex: str,
    compile_id: str,
    compile_hex: str,
    contact_ids: list[str],
    decoder_ids: list[str],
    input_ids: list[str],
    result_id: str,
) -> dict:
    projection_digest = "sha256:" + projection_hex * 64
    compile_digest = "sha256:" + compile_hex * 64
    loadout = {
        "schema": "mortal_actor.loadout-binding/v0",
        "run_id": f"run:{road_id}",
        "actor_id": road_id,
        "world_cut_ref": f"cut:{road_id}",
        "projection_ref": projection_digest,
        "entry_compile_id": "C0",
        "entry_compile_digest": "sha256:" + "a" * 64,
        "evaluation_compile_id": compile_id,
        "evaluation_compile_digest": compile_digest,
        "recompile_relation": "same" if compile_id == "C0" else "child",
        "effect_fence_ref": "effect-fence:EF0",
        "authority_expanded": False,
        "side_effect_executed": False,
    }
    projection = {
        "schema": "mortal_actor.3rdi-handoff/v0",
        "projection_digest": projection_digest,
        "field_id": "passage-world-001",
        "cut_id": road_id,
        "observer": road_id.lower(),
        "visible_occurrence_ids": ["token-formation-point"],
        "visible_causal_edge_ids": [],
        "visible_relevance_edge_ids": [],
        "contact_ids": list(contact_ids),
        "attention_event_ids": [f"attention:{road_id}"],
        "decoder_application_ids": list(decoder_ids),
        "stance_ids": [f"stance:{road_id}"] if decoder_ids else [],
    }
    local_support = {
        "profile": "alex.runtime/local-support-m0",
        "rule_id": "LOCAL-SUPPORT-001",
        "rule_version": 1,
        "claim_id": "Q-PASSAGE",
        "cut_id": road_id,
        "observer": road_id.lower(),
        "projection_digest": projection_digest,
        "compile_id": compile_id,
        "compile_digest": compile_digest,
        "local_disposition": "local_basis_accept",
        "reason_code": None,
        "required_local_basis_ids": ["token-formation-point"],
        "missing_local_basis_ids": [],
        "receipt_survivors": [f"projection:{projection_digest}", f"compile:{compile_id}"],
        "derivation": {
            "proposal": {"id": f"proposal:{road_id}"},
            "evaluation": {
                "evaluation_id": f"evaluation:{road_id}",
                "ruleset_digest": "sha256:" + "d" * 64,
                "input_ids": list(input_ids),
                "disposition": "ACCEPT",
                "reason_code": None,
                "conclusion_assertion_id": f"conclusion:{road_id}",
            },
            "conclusion_assertion": {
                "id": f"conclusion:{road_id}",
                "predicate": "SUPPORTS",
            },
        },
    }
    return {
        "road_id": road_id,
        "loadout_binding": loadout,
        "projection_handoff": projection,
        "local_support_result": local_support,
        "result_occurrence": {"id": result_id, "payload_ref": "payload:022100"},
    }


def road_a() -> dict:
    return bundle(
        road_id="ROAD-A",
        projection_hex="1",
        compile_id="C0",
        compile_hex="2",
        contact_ids=["contact-e1-road-a"],
        decoder_ids=[],
        input_ids=["evidence-e1", "path:P1"],
        result_id="occurrence:token-a",
    )


def road_b() -> dict:
    return bundle(
        road_id="ROAD-B1",
        projection_hex="3",
        compile_id="C1",
        compile_hex="4",
        contact_ids=["contact-e2-road-b"],
        decoder_ids=["decoder-road-b1"],
        input_ids=["carrier-e2", "path:P2"],
        result_id="occurrence:token-b",
    )


class PassageFormationTests(unittest.TestCase):
    def test_same_payload_different_lawful_formation_bases_remain_distinct(self) -> None:
        a = bind_passage_formation(**road_a())
        b = bind_passage_formation(**road_b())
        self.assertEqual(a["schema"], "passage_world.alex-formation/v0")
        self.assertEqual(a["payload_ref"], b["payload_ref"])
        self.assertNotEqual(a["formation_basis_digest"], b["formation_basis_digest"])
        self.assertFalse(a["authority_transferred"])
        self.assertFalse(b["authority_transferred"])
        self.assertEqual(a["admission_status"], "NOT_ATTEMPTED")

    def test_result_occurrence_id_noise_changes_exact_identity_not_substantive_basis(self) -> None:
        original = road_a()
        changed = copy.deepcopy(original)
        changed["result_occurrence"]["id"] = "occurrence:renamed-wrapper"
        a = bind_passage_formation(**original)
        b = bind_passage_formation(**changed)
        self.assertEqual(a["formation_basis_digest"], b["formation_basis_digest"])
        self.assertNotEqual(a["formation_id"], b["formation_id"])

    def test_set_like_list_order_does_not_mint_formation_history(self) -> None:
        original = road_b()
        changed = copy.deepcopy(original)
        changed["projection_handoff"]["contact_ids"].reverse()
        changed["projection_handoff"]["decoder_application_ids"].reverse()
        changed["local_support_result"]["derivation"]["evaluation"]["input_ids"].reverse()
        self.assertEqual(
            bind_passage_formation(**original)["formation_basis_digest"],
            bind_passage_formation(**changed)["formation_basis_digest"],
        )

    def test_cross_binding_failures_are_refused_with_stable_codes(self) -> None:
        cases = []
        invalid = road_a(); invalid["loadout_binding"]["schema"] = "bad"; cases.append((invalid, "LOADOUT_BINDING_INVALID"))
        invalid = road_a(); invalid["projection_handoff"]["schema"] = "bad"; cases.append((invalid, "PROJECTION_HANDOFF_INVALID"))
        invalid = road_a(); invalid["local_support_result"]["profile"] = "bad"; cases.append((invalid, "LOCAL_SUPPORT_RESULT_INVALID"))
        invalid = road_a(); invalid["loadout_binding"]["projection_ref"] = "sha256:" + "9" * 64; cases.append((invalid, "PROJECTION_BINDING_MISMATCH"))
        invalid = road_a(); invalid["local_support_result"]["compile_id"] = "FOREIGN"; cases.append((invalid, "COMPILE_BINDING_MISMATCH"))
        invalid = road_a(); invalid["local_support_result"]["cut_id"] = "FOREIGN"; cases.append((invalid, "CUT_BINDING_MISMATCH"))
        invalid = road_a(); invalid["result_occurrence"] = {"id": "", "payload_ref": "payload:022100"}; cases.append((invalid, "RESULT_OCCURRENCE_INVALID"))
        invalid = road_a(); invalid["local_support_result"]["local_disposition"] = "local_basis_unresolved"; cases.append((invalid, "LOCAL_SUPPORT_NOT_FORMED"))
        for payload, code in cases:
            with self.subTest(code=code):
                with self.assertRaisesRegex(ValueError, code):
                    bind_passage_formation(**payload)

    def test_substantive_mutations_change_basis_digest(self) -> None:
        original = road_b()
        baseline = bind_passage_formation(**original)["formation_basis_digest"]
        mutations = []
        changed = copy.deepcopy(original); changed["projection_handoff"]["decoder_application_ids"] = ["decoder:other"]; mutations.append(changed)
        changed = copy.deepcopy(original); changed["local_support_result"]["derivation"]["evaluation"]["input_ids"] = ["different-basis"]; mutations.append(changed)
        for changed in mutations:
            self.assertNotEqual(baseline, bind_passage_formation(**changed)["formation_basis_digest"])

    def test_receipt_does_not_claim_route_destination_truth_or_passage_verdict(self) -> None:
        receipt = bind_passage_formation(**road_a())
        encoded = repr(receipt).lower()
        for forbidden in ("global_truth", "passage_verdict", "same_passage", "destination", "route_id", "canon"):
            self.assertNotIn(forbidden, encoded)


if __name__ == "__main__":
    unittest.main()
