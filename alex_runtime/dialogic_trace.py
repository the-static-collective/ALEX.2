from __future__ import annotations

import re
from typing import Any

from .digests import sha256_json

QUESTION_SCHEMA = "alex.source-question/v0"
QUESTION_RESULT_SCHEMA = "alex.source-question-result/v0"
QUESTION_RECEIPT_SCHEMA = "alex.source-question-receipt/v0"
RESPONSE_SCHEMA = "alex.source-response/v0"
RESPONSE_RESULT_SCHEMA = "alex.source-response-result/v0"
RESPONSE_RECEIPT_SCHEMA = "alex.source-response-receipt/v0"
MODEL_DELTA_SCHEMA = "alex.model-delta/v0"
MODEL_DELTA_RESULT_SCHEMA = "alex.model-delta-result/v0"
MODEL_DELTA_RECEIPT_SCHEMA = "alex.model-delta-receipt/v0"

IDENTITY_STATUSES = frozenset({"VERIFIED_NAMED","NAMED","PERSISTENT_PSEUDONYM","ONE_SHOT_ANONYMOUS","UNKNOWN"})
LEADING_RISKS = frozenset({"LOW","MEDIUM","HIGH","UNASSESSED"})
QUESTION_STATUSES = frozenset({"DRAFT","SENT","ANSWERED","DECLINED","UNANSWERED","UNDELIVERABLE","WITHDRAWN"})
VISIBILITIES = frozenset({"PUBLIC","PRIVATE","RESTRICTED"})
PERMISSIONS = frozenset({"YES","NO","UNRESOLVED"})
RESPONSE_CLASSES = frozenset({
    "CLARIFIES_CURRENT_POSITION","CLARIFIES_CURRENT_INTENT","DISPUTES_OUR_READING",
    "CONFIRMS_OUR_READING","CORRECTS_FACTUAL_CLAIM","SUPPLIES_SOURCE",
    "SUPPLIES_COUNTEREXAMPLE","OPENS_DISCRIMINATOR","REFUSES_QUESTION",
    "CLAIMS_HISTORICAL_INTENT","CLAIMS_AUTHORSHIP","CLAIMS_PROVENANCE",
})
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")

def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def _refuse(schema: str, reason: str) -> dict[str, Any]:
    return {"schema": schema, "disposition": "REFUSE", "reason": reason, "authority": "none"}

def _unique_string_list(value: Any) -> bool:
    return isinstance(value, list) and all(_nonempty_string(x) for x in value) and len(value) == len(set(value))

def evaluate_source_question(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(QUESTION_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != QUESTION_SCHEMA:
        return _refuse(QUESTION_RESULT_SCHEMA, "wrong_schema")
    required = ("question_id","target_ref","target_identity_status","exact_question","leading_risk","channel","visibility","publication_permission","status")
    if any(not _nonempty_string(record.get(k)) for k in required):
        return _refuse(QUESTION_RESULT_SCHEMA, "missing_required_field")
    if not _unique_string_list(record.get("derived_from_claim_ids")):
        return _refuse(QUESTION_RESULT_SCHEMA, "invalid_derived_from_claim_ids")
    if record["target_identity_status"] not in IDENTITY_STATUSES:
        return _refuse(QUESTION_RESULT_SCHEMA, "invalid_identity_status")
    if record["leading_risk"] not in LEADING_RISKS:
        return _refuse(QUESTION_RESULT_SCHEMA, "invalid_leading_risk")
    if record["visibility"] not in VISIBILITIES:
        return _refuse(QUESTION_RESULT_SCHEMA, "invalid_visibility")
    if record["publication_permission"] not in PERMISSIONS:
        return _refuse(QUESTION_RESULT_SCHEMA, "invalid_publication_permission")
    if record["status"] not in QUESTION_STATUSES:
        return _refuse(QUESTION_RESULT_SCHEMA, "invalid_question_status")
    receipt = {k: record[k] for k in required}
    receipt["derived_from_claim_ids"] = list(record["derived_from_claim_ids"])
    receipt["question_digest"] = sha256_json(record)
    receipt["authority"] = "none"
    receipt["schema"] = QUESTION_RECEIPT_SCHEMA
    return {"schema": QUESTION_RESULT_SCHEMA, "disposition": "ACCEPT", "reason": None, "receipt": receipt, "authority": "none"}

def evaluate_source_response(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(RESPONSE_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != RESPONSE_SCHEMA:
        return _refuse(RESPONSE_RESULT_SCHEMA, "wrong_schema")
    required = ("response_id","question_id","responder_claimed_identity","responder_identity_status","channel","visibility","quotation_permission","publication_permission","response_class","response_reading","carrier_ref")
    if any(not _nonempty_string(record.get(k)) for k in required):
        return _refuse(RESPONSE_RESULT_SCHEMA, "missing_required_field")
    if record["responder_identity_status"] not in IDENTITY_STATUSES:
        return _refuse(RESPONSE_RESULT_SCHEMA, "invalid_identity_status")
    if record["visibility"] not in VISIBILITIES:
        return _refuse(RESPONSE_RESULT_SCHEMA, "invalid_visibility")
    if record["quotation_permission"] not in PERMISSIONS or record["publication_permission"] not in PERMISSIONS:
        return _refuse(RESPONSE_RESULT_SCHEMA, "invalid_permission")
    if record["response_class"] not in RESPONSE_CLASSES:
        return _refuse(RESPONSE_RESULT_SCHEMA, "invalid_response_class")
    if not SHA256_REF.fullmatch(record["carrier_ref"]):
        return _refuse(RESPONSE_RESULT_SCHEMA, "invalid_carrier_ref")
    receipt = {k: record[k] for k in required}
    receipt["response_digest"] = sha256_json(record)
    receipt["authority"] = "none"
    receipt["schema"] = RESPONSE_RECEIPT_SCHEMA
    return {"schema": RESPONSE_RESULT_SCHEMA, "disposition": "ACCEPT", "reason": None, "receipt": receipt, "authority": "none"}

def evaluate_model_delta(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(MODEL_DELTA_RESULT_SCHEMA, "not_an_object")
    if record.get("schema") != MODEL_DELTA_SCHEMA:
        return _refuse(MODEL_DELTA_RESULT_SCHEMA, "wrong_schema")
    if not _nonempty_string(record.get("delta_id")):
        return _refuse(MODEL_DELTA_RESULT_SCHEMA, "missing_required_field")
    refs = ("pre_response_model_ref","response_ref","post_response_model_ref")
    if any(not _nonempty_string(record.get(k)) for k in refs):
        return _refuse(MODEL_DELTA_RESULT_SCHEMA, "missing_required_field")
    if any(not SHA256_REF.fullmatch(record[k]) for k in refs):
        return _refuse(MODEL_DELTA_RESULT_SCHEMA, "invalid_ref")
    list_fields = (
        "changed_claims","unchanged_claims","killed_claims","new_questions",
        "new_source_paths","response_dependent_claims","independently_retested_claims",
        "residual_disagreement",
    )
    for field in list_fields:
        if not _unique_string_list(record.get(field)):
            return _refuse(MODEL_DELTA_RESULT_SCHEMA, f"invalid_{field}")
    if set(record["response_dependent_claims"]) & set(record["independently_retested_claims"]):
        return _refuse(MODEL_DELTA_RESULT_SCHEMA, "retest_status_conflict")
    receipt = {"schema": MODEL_DELTA_RECEIPT_SCHEMA, "delta_id": record["delta_id"]}
    for k in refs + list_fields:
        receipt[k] = list(record[k]) if isinstance(record[k], list) else record[k]
    receipt["delta_digest"] = sha256_json(record)
    receipt["authority"] = "none"
    return {"schema": MODEL_DELTA_RESULT_SCHEMA, "disposition": "ACCEPT", "reason": None, "receipt": receipt, "authority": "none"}
