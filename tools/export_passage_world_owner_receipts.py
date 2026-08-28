#!/usr/bin/env python3
"""Export exact LOADOUT/ALEX/LOADIN.STEAD owner receipts for PASSAGE-WORLD-001."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

from alex_runtime.local_support import evaluate_local_support_case
from alex_runtime.passage_formation import bind_passage_formation
from loadout_runtime.loadinstead import route_bit
from skills.loadout.scripts.compile_identity import compile_payload_digest
from skills.loadout.scripts.mortal_actor import bind_mortal_actor_compiles

ROOT = Path(__file__).resolve().parents[1]
INPUT_ROOT = ROOT / "proof_inputs" / "passage-world"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def make_compile() -> dict:
    record = {
        "schema": "loadout.compile/v0",
        "compile_id": "C0",
        "parent_compile_id": None,
        "issued_at": "2026-08-28T13:00:00Z",
        "expires_at": "2026-08-28T14:00:00Z",
        "world_cut_ref": "world-cut:R0",
        "context_pack_ref": "context-pack:R0",
        "compile_trace": {
            "id": "compile-trace:C0",
            "source_world_ref": "world-source:R0",
            "operation": "bounded-selection",
            "preserved_invariants": ["same-payload", "same-destination"],
            "declared_loss": [],
            "producer": "loadout-proof-export@1",
            "freshness": "2026-08-28T13:00:00Z"
        },
        "capability_bindings": [
            {"capability": "3rdi.project", "status": "available"},
            {"capability": "alex.evaluate", "status": "available"}
        ],
        "effect_fence_ref": "effect-fence:EF0",
        "effective_effects": [],
        "owner_evidence_digest": "sha256:" + "a" * 64,
        "egress_policy_ref": "egress-policy:E0"
    }
    record["compile_digest"] = compile_payload_digest(record)
    return record


def child_compile(parent: dict) -> dict:
    child = copy.deepcopy(parent)
    child["compile_id"] = "C1"
    child["parent_compile_id"] = parent["compile_id"]
    child["world_cut_ref"] = "world-cut:ROAD-B1"
    child["context_pack_ref"] = "context-pack:ROAD-B1"
    child["compile_trace"]["id"] = "compile-trace:C1"
    child["compile_digest"] = compile_payload_digest(child)
    return child


def local_support(*, road_id: str, subject_id: str, projection: dict, compile_record: dict) -> dict:
    path_id = f"path:{road_id}"
    case = {
        "case_id": f"local-support:{road_id}",
        "operation_type": "local_support",
        "rule_profile": "alex.runtime/local-support-m0",
        "given": {
            "records": [
                {"id": subject_id, "kind": "evidence"},
                {"id": "claim-token", "kind": "claim"}
            ],
            "evidence_paths": [
                {
                    "id": path_id,
                    "source_id": subject_id,
                    "claim_id": "claim-token",
                    "status": "ATTRIBUTABLE",
                    "basis_ids": [subject_id],
                    "witness_ids": [f"witness:{road_id}"]
                }
            ],
            "relations": [],
            "projection_handoff": projection,
            "evaluation_compile": compile_record
        },
        "attempt": {
            "claim_id": "Q-PASSAGE",
            "expected_projection_digest": projection["projection_digest"],
            "expected_evaluation_compile_id": compile_record["compile_id"],
            "expected_evaluation_compile_digest": compile_record["compile_digest"],
            "relation_proposal": {
                "id": f"proposal:{road_id}",
                "subject_id": subject_id,
                "predicate": "SUPPORTS",
                "object_id": "claim-token",
                "scope": "passage-world-001",
                "basis_ids": [subject_id, path_id]
            },
            "evaluation_id": f"evaluation:{road_id}",
            "execution_step_id": f"step:{road_id}",
            "conclusion_assertion_id": f"conclusion:{road_id}"
        }
    }
    result = evaluate_local_support_case(case)
    if result["local_disposition"] != "local_basis_accept":
        raise RuntimeError(f"local support did not form for {road_id}: {result}")
    return result


def export_receipts(output: Path) -> None:
    c0 = make_compile()
    c1 = child_compile(c0)
    doors = [{
        "schema": "loadinstead.door/v0",
        "door_id": "door:R1",
        "owner_world": "synthetic:R1",
        "role": "destination",
        "accepts_classes": ["passage-token"],
        "protocol": "fixture-only",
        "capability_ref": "capability:synthetic-r1",
        "status": "available"
    }]

    configs = {
        "ROAD-A": {"cut": "ROAD-A", "subject": "evidence-e1", "evaluation_compile": c0, "result_id": "occurrence:token-a"},
        "ROAD-B": {"cut": "ROAD-B1", "subject": "carrier-e2", "evaluation_compile": c1, "result_id": "occurrence:token-b"}
    }

    for road_id, config in configs.items():
        projection = load_json(INPUT_ROOT / road_id / "3rdi.json")
        evaluation_compile = config["evaluation_compile"]
        loadout = bind_mortal_actor_compiles(
            run_id=f"run:{road_id}",
            actor_id=road_id,
            world_cut_ref=projection["cut_id"],
            projection_ref=projection["projection_digest"],
            entry_compile=c0,
            evaluation_compile=evaluation_compile
        )
        support = local_support(
            road_id=road_id,
            subject_id=config["subject"],
            projection=projection,
            compile_record=evaluation_compile
        )
        formation = bind_passage_formation(
            road_id=road_id,
            loadout_binding=loadout,
            projection_handoff=projection,
            local_support_result=support,
            result_occurrence={"id": config["result_id"], "payload_ref": "payload:022100"}
        )
        route = route_bit(
            {
                "schema": "ecode.route-bit/v0",
                "bit_id": f"bit:{road_id}",
                "occurred_at": "2026-08-28T13:30:00Z",
                "source_world": "synthetic:R0",
                "consequence_class": "passage-token",
                "payload_ref": "payload:022100",
                "formation_ref": formation["formation_id"],
                "compile_ref": {
                    "compile_id": evaluation_compile["compile_id"],
                    "compile_digest": evaluation_compile["compile_digest"]
                },
                "witness_classes": []
            },
            doors
        )
        if route["disposition"] != "ROUTED" or route["primary_door_ref"] != "door:R1":
            raise RuntimeError(f"route failed for {road_id}: {route}")

        write_json(output / road_id / "loadout.json", loadout)
        write_json(output / road_id / "alex-formation.json", formation)
        write_json(output / road_id / "loadinstead.json", route)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    export_receipts(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
