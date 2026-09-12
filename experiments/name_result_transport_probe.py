from __future__ import annotations

import json

from alex_runtime.name_specimen_gate import (
    SPECIMEN_TYPE_ORDER,
    evaluate_name_six_specimen_gate,
    evaluate_name_specimen_packet,
)

REF_A = "sha256:" + "a" * 64
REF_B = "sha256:" + "b" * 64
REF_C = "sha256:" + "c" * 64
REF_D = "sha256:" + "d" * 64
REF_E = "sha256:" + "e" * 64
REF_F = "sha256:" + "f" * 64


def _packet(specimen_type: str) -> dict:
    record = {
        "schema": "alex.name-specimen-packet/v0",
        "packet_id": f"transport-probe-{specimen_type.lower()}",
        "specimen_type": specimen_type,
        "attestation_ref": REF_A,
        "transform_refs": [REF_B],
        "hypothesis_ref": REF_C,
        "null_battery_ref": REF_D,
        "receipt_refs": [REF_E],
        "producer": "alex-transport-probe@0",
    }
    if specimen_type == "NOMEN_SACRUM":
        record["material_witness_ref"] = REF_F
    return record


def _gate(packet_results: list[dict]) -> dict:
    return {
        "schema": "alex.name-six-specimen-gate/v0",
        "gate_id": "name-result-transport-probe",
        "packet_results": packet_results,
        "producer": "alex-transport-probe@0",
    }


def run_probe() -> dict:
    original_results = [
        evaluate_name_specimen_packet(_packet(specimen_type))
        for specimen_type in SPECIMEN_TYPE_ORDER
    ]
    original_gate = evaluate_name_six_specimen_gate(_gate(original_results))

    serialized = json.dumps(original_results, sort_keys=True, separators=(",", ":"))
    round_trip_results = json.loads(serialized)
    round_trip_gate = evaluate_name_six_specimen_gate(_gate(round_trip_results))

    object_identity_preserved = all(
        before is after
        for before, after in zip(original_results, round_trip_results, strict=True)
    )
    gate_observation_equal = original_gate == round_trip_gate

    return {
        "schema": "alex.experiment.name-result-transport-probe/v0",
        "transport": "json_round_trip",
        "original_gate_disposition": original_gate["disposition"],
        "round_trip_gate_disposition": round_trip_gate["disposition"],
        "gate_observation_equal": gate_observation_equal,
        "object_identity_preserved": object_identity_preserved,
        "finding": (
            "SERIALIZATION_NOT_DETECTABLE_BY_GATE"
            if gate_observation_equal and not object_identity_preserved
            else "OBSERVATION_CHANGED"
        ),
        "interpretation": "measurement_only_no_transport_contract_selected",
        "authority": "none",
    }


if __name__ == "__main__":
    print(json.dumps(run_probe(), sort_keys=True, separators=(",", ":")))
