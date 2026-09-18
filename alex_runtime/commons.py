from __future__ import annotations

import base64
import binascii
import hashlib
import re
from typing import Any

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

from .digests import sha256_json

CARD_SCHEMA = "alex.library-card/v0"
CARD_RESULT_SCHEMA = "alex.library-card-result/v0"
CARD_RECEIPT_SCHEMA = "alex.library-card-receipt/v0"
RIGHTS_SCHEMA = "alex.rights-statement/v0"
RIGHTS_RESULT_SCHEMA = "alex.rights-statement-result/v0"
RIGHTS_RECEIPT_SCHEMA = "alex.rights-statement-receipt/v0"
DEPOSIT_SCHEMA = "alex.commons-deposit/v0"
DEPOSIT_RESULT_SCHEMA = "alex.commons-deposit-result/v0"
DEPOSIT_RECEIPT_SCHEMA = "alex.commons-deposit-receipt/v0"
CONTINUITY_SCHEMA = "alex.pseudonym-continuity/v0"
CONTINUITY_RESULT_SCHEMA = "alex.pseudonym-continuity-result/v0"
CONTINUITY_RECEIPT_SCHEMA = "alex.pseudonym-continuity-receipt/v0"

CARD_MODES = frozenset({"NAMED","VERIFIED_NAMED","PERSISTENT_PSEUDONYM","ONE_SHOT_ANONYMOUS"})
CAPABILITIES = frozenset({
    "deposit_source_pointer","deposit_bytes","deposit_reading","deposit_correction",
    "deposit_counterexample","deposit_question_response","deposit_rights_statement",
    "retrieve_own_receipts","append_to_own_deposit","prove_continuity",
})
PERMISSIONS = frozenset({"YES","NO","UNRESOLVED"})
RIGHTS_FIELDS = ("hold","process","quote","publish","identity_disclosure","reply")
TRANSPORT_CLASSES = frozenset({"CLEARNET","ONION_SERVICE","LOCAL","IMPORTED_CORRESPONDENCE","CONNECTOR","OTHER_DECLARED"})
QUARANTINE_STATUSES = frozenset({"INERT","CLEARED_METADATA_ONLY","CLEARED_FOR_PROCESSING","REJECTED"})
INGEST_RESULTS = frozenset({"RECEIVED","REFUSED","HELD","PROCESSED"})
INDEPENDENCE_STATUSES = frozenset({"UNKNOWN","DEPENDENT","PARTIALLY_RESOLVED","INDEPENDENT_ESTABLISHED"})
PRIVACY_REQUESTS = frozenset({"PUBLIC","PRIVATE","RESTRICTED"})
SHA256_REF = re.compile(r"^sha256:[0-9a-f]{64}$")

def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())

def _unique_strings(value: Any, *, allow_empty: bool = True) -> bool:
    return isinstance(value, list) and (allow_empty or bool(value)) and all(_nonempty(x) for x in value) and len(value) == len(set(value))

def _refuse(schema: str, reason: str) -> dict[str, Any]:
    return {"schema":schema,"disposition":"REFUSE","reason":reason,"authority":"none"}

def evaluate_library_card(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(CARD_RESULT_SCHEMA,"not_an_object")
    if record.get("schema") != CARD_SCHEMA:
        return _refuse(CARD_RESULT_SCHEMA,"wrong_schema")
    if not _nonempty(record.get("card_id")) or not _nonempty(record.get("mode")):
        return _refuse(CARD_RESULT_SCHEMA,"missing_required_field")
    if record["mode"] not in CARD_MODES:
        return _refuse(CARD_RESULT_SCHEMA,"invalid_mode")
    if not _unique_strings(record.get("capabilities"), allow_empty=False) or not set(record["capabilities"]).issubset(CAPABILITIES):
        return _refuse(CARD_RESULT_SCHEMA,"invalid_capabilities")
    if record["mode"] == "PERSISTENT_PSEUDONYM" and not _nonempty(record.get("contributor_key_id")):
        return _refuse(CARD_RESULT_SCHEMA,"contributor_key_required")
    receipt = {
        "schema":CARD_RECEIPT_SCHEMA,
        "card_id":record["card_id"],
        "mode":record["mode"],
        "capabilities":list(record["capabilities"]),
        "card_digest":sha256_json(record),
        "authority":"none",
    }
    for optional in ("public_label","contributor_key_id"):
        if _nonempty(record.get(optional)):
            receipt[optional]=record[optional]
    return {"schema":CARD_RESULT_SCHEMA,"disposition":"ACCEPT","reason":None,"receipt":receipt,"authority":"none"}

def evaluate_rights_statement(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(RIGHTS_RESULT_SCHEMA,"not_an_object")
    if record.get("schema") != RIGHTS_SCHEMA:
        return _refuse(RIGHTS_RESULT_SCHEMA,"wrong_schema")
    if not _nonempty(record.get("rights_id")):
        return _refuse(RIGHTS_RESULT_SCHEMA,"missing_required_field")
    for field in RIGHTS_FIELDS:
        if record.get(field) not in PERMISSIONS:
            return _refuse(RIGHTS_RESULT_SCHEMA,f"invalid_{field}_permission")
    receipt={"schema":RIGHTS_RECEIPT_SCHEMA,"rights_id":record["rights_id"],"rights_digest":sha256_json(record),"authority":"none"}
    for field in RIGHTS_FIELDS:
        receipt[field]=record[field]
    return {"schema":RIGHTS_RESULT_SCHEMA,"disposition":"ACCEPT","reason":None,"receipt":receipt,"authority":"none"}

def evaluate_commons_deposit(record: object) -> dict[str, Any]:
    if not isinstance(record, dict):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"not_an_object")
    if record.get("schema") != DEPOSIT_SCHEMA:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"wrong_schema")
    required=("deposit_id","transport_class","contributor_mode","rights_statement_ref","privacy_request","publication_permission","content_digest","quarantine_status","ingest_result","independence_status")
    if any(not _nonempty(record.get(k)) for k in required):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"missing_required_field")
    if record["transport_class"] not in TRANSPORT_CLASSES:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_transport_class")
    if record["contributor_mode"] not in CARD_MODES:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_contributor_mode")
    if record["contributor_mode"] != "ONE_SHOT_ANONYMOUS" and not _nonempty(record.get("card_id")):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"card_id_required")
    if record["contributor_mode"] == "ONE_SHOT_ANONYMOUS" and record.get("card_id") not in (None,"") and not _nonempty(record.get("card_id")):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_card_id")
    if not _unique_strings(record.get("source_locators")):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_source_locators")
    if not _unique_strings(record.get("held_artifact_refs")):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_held_artifact_refs")
    if not _unique_strings(record.get("proposed_relations")):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_proposed_relations")
    if not SHA256_REF.fullmatch(record["rights_statement_ref"]) or not SHA256_REF.fullmatch(record["content_digest"]):
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_digest_ref")
    if record["privacy_request"] not in PRIVACY_REQUESTS:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_privacy_request")
    if record["publication_permission"] not in PERMISSIONS:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_publication_permission")
    if record["quarantine_status"] not in QUARANTINE_STATUSES:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_quarantine_status")
    if record["quarantine_status"] != "INERT":
        return _refuse(DEPOSIT_RESULT_SCHEMA,"arrival_must_be_inert")
    if record["ingest_result"] not in INGEST_RESULTS:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_ingest_result")
    if record["ingest_result"] != "RECEIVED":
        return _refuse(DEPOSIT_RESULT_SCHEMA,"arrival_must_be_received")
    if record["independence_status"] not in INDEPENDENCE_STATUSES:
        return _refuse(DEPOSIT_RESULT_SCHEMA,"invalid_independence_status")
    receipt={
        "schema":DEPOSIT_RECEIPT_SCHEMA,
        "deposit_id":record["deposit_id"],
        "transport_class":record["transport_class"],
        "contributor_mode":record["contributor_mode"],
        "card_id":record.get("card_id"),
        "source_locators":list(record["source_locators"]),
        "held_artifact_refs":list(record["held_artifact_refs"]),
        "proposed_relations":list(record["proposed_relations"]),
        "rights_statement_ref":record["rights_statement_ref"],
        "privacy_request":record["privacy_request"],
        "publication_permission":record["publication_permission"],
        "content_digest":record["content_digest"],
        "quarantine_status":record["quarantine_status"],
        "ingest_result":record["ingest_result"],
        "independence_status":record["independence_status"],
        "deposit_digest":sha256_json(record),
        "authority":"none",
    }
    return {"schema":DEPOSIT_RESULT_SCHEMA,"disposition":"ACCEPT","reason":None,"receipt":receipt,"authority":"none"}

def verify_pseudonym_continuity(proof: object) -> dict[str, Any]:
    if not isinstance(proof, dict):
        return _refuse(CONTINUITY_RESULT_SCHEMA,"not_an_object")
    if proof.get("schema") != CONTINUITY_SCHEMA:
        return _refuse(CONTINUITY_RESULT_SCHEMA,"wrong_schema")
    for field in ("card_id","public_key_b64","message","signature_b64"):
        if not _nonempty(proof.get(field)):
            return _refuse(CONTINUITY_RESULT_SCHEMA,"missing_required_field")
    try:
        public_key_bytes=base64.b64decode(proof["public_key_b64"],validate=True)
        signature=base64.b64decode(proof["signature_b64"],validate=True)
    except (binascii.Error,ValueError):
        return _refuse(CONTINUITY_RESULT_SCHEMA,"invalid_base64")
    if len(public_key_bytes)!=32:
        return _refuse(CONTINUITY_RESULT_SCHEMA,"invalid_public_key")
    expected_prefix=f"alex-continuity:{proof['card_id']}:"
    if not proof["message"].startswith(expected_prefix):
        return _refuse(CONTINUITY_RESULT_SCHEMA,"message_card_mismatch")
    try:
        Ed25519PublicKey.from_public_bytes(public_key_bytes).verify(signature,proof["message"].encode("utf-8"))
    except (InvalidSignature,ValueError):
        return _refuse(CONTINUITY_RESULT_SCHEMA,"signature_verification_failed")
    fingerprint="sha256:"+hashlib.sha256(public_key_bytes).hexdigest()
    receipt={
        "schema":CONTINUITY_RECEIPT_SCHEMA,
        "card_id":proof["card_id"],
        "continuity_status":"VERIFIED_KEY_CONTINUITY",
        "civil_identity_status":"UNKNOWN",
        "key_fingerprint":fingerprint,
        "proof_digest":sha256_json(proof),
        "authority":"none",
    }
    return {"schema":CONTINUITY_RESULT_SCHEMA,"disposition":"ACCEPT","reason":None,"receipt":receipt,"authority":"none"}
