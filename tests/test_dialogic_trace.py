import copy
import unittest

from alex_runtime.dialogic_trace import evaluate_source_question, evaluate_source_response, evaluate_model_delta

BASE_QUESTION = {
    "schema":"alex.source-question/v0","question_id":"q-001","target_ref":"person:reachable-source",
    "target_identity_status":"VERIFIED_NAMED","derived_from_claim_ids":["claim:model-001"],
    "exact_question":"Are you changing the operator, the object type, or adding a transformation?",
    "leading_risk":"LOW","channel":"EMAIL","visibility":"PRIVATE","publication_permission":"NO","status":"SENT",
}
BASE_RESPONSE = {
    "schema":"alex.source-response/v0","response_id":"r-001","question_id":"q-001",
    "responder_claimed_identity":"person:reachable-source","responder_identity_status":"VERIFIED_NAMED",
    "channel":"EMAIL","visibility":"PRIVATE","quotation_permission":"NO","publication_permission":"NO",
    "response_class":"CLARIFIES_CURRENT_POSITION",
    "response_reading":"I mean an additional transformation, not ordinary multiplication.",
    "carrier_ref":"sha256:"+"a"*64,
}
BASE_DELTA = {
    "schema":"alex.model-delta/v0","delta_id":"delta-001",
    "pre_response_model_ref":"sha256:"+"1"*64,"response_ref":"sha256:"+"2"*64,
    "post_response_model_ref":"sha256:"+"3"*64,"changed_claims":["claim:operator-semantics"],
    "unchanged_claims":["claim:public-artifact-wording"],"killed_claims":[],
    "new_questions":["question:what-transformation"],"new_source_paths":[],
    "response_dependent_claims":["claim:creator-current-position"],
    "independently_retested_claims":[],"residual_disagreement":[],
}
class SourceQuestionTests(unittest.TestCase):
    def test_accepts_bounded_question_and_freezes_authority(self):
        r=evaluate_source_question(copy.deepcopy(BASE_QUESTION)); self.assertEqual(r["disposition"],"ACCEPT")
        self.assertEqual(r["receipt"]["authority"],"none"); self.assertEqual(r["receipt"]["exact_question"],BASE_QUESTION["exact_question"])
    def test_silence_is_not_a_response_status(self):
        x=copy.deepcopy(BASE_QUESTION); x["status"]="REJECTED_BY_SILENCE"
        r=evaluate_source_question(x); self.assertEqual(r["disposition"],"REFUSE"); self.assertEqual(r["reason"],"invalid_question_status")
class SourceResponseTests(unittest.TestCase):
    def test_private_response_accepts_without_publication_promotion(self):
        r=evaluate_source_response(copy.deepcopy(BASE_RESPONSE)); self.assertEqual(r["disposition"],"ACCEPT")
        self.assertEqual(r["receipt"]["publication_permission"],"NO"); self.assertEqual(r["receipt"]["authority"],"none")
    def test_response_requires_exact_question_parent(self):
        x=copy.deepcopy(BASE_RESPONSE); x["question_id"]=""
        self.assertEqual(evaluate_source_response(x)["reason"],"missing_required_field")
class ModelDeltaTests(unittest.TestCase):
    def test_response_dependent_claim_is_not_auto_retested(self):
        r=evaluate_model_delta(copy.deepcopy(BASE_DELTA)); self.assertEqual(r["disposition"],"ACCEPT")
        self.assertEqual(r["receipt"]["response_dependent_claims"],["claim:creator-current-position"])
        self.assertEqual(r["receipt"]["independently_retested_claims"],[])
    def test_same_claim_cannot_be_response_only_and_retested(self):
        x=copy.deepcopy(BASE_DELTA); x["independently_retested_claims"]=["claim:creator-current-position"]
        r=evaluate_model_delta(x); self.assertEqual(r["reason"],"retest_status_conflict")
if __name__=="__main__": unittest.main()
