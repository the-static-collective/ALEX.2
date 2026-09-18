import base64
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from alex_runtime.commons import (
    evaluate_library_card,
    evaluate_rights_statement,
    evaluate_commons_deposit,
    verify_pseudonym_continuity,
)

BASE_CARD={
 "schema":"alex.library-card/v0","card_id":"card:pseudo:001","mode":"PERSISTENT_PSEUDONYM",
 "public_label":"reader-7","contributor_key_id":"ed25519:reader-7",
 "capabilities":["deposit_source_pointer","deposit_counterexample","retrieve_own_receipts","prove_continuity"],
 "authority":"canon",
}
BASE_RIGHTS={
 "schema":"alex.rights-statement/v0","rights_id":"rights-001",
 "hold":"YES","process":"YES","quote":"NO","publish":"NO","identity_disclosure":"NO","reply":"YES",
}
BASE_DEPOSIT={
 "schema":"alex.commons-deposit/v0","deposit_id":"deposit-001","transport_class":"LOCAL",
 "contributor_mode":"ONE_SHOT_ANONYMOUS","card_id":None,
 "source_locators":["https://example.invalid/source"],"held_artifact_refs":[],"proposed_relations":["contextualizes"],
 "rights_statement_ref":"sha256:"+"b"*64,"privacy_request":"PRIVATE","publication_permission":"NO",
 "content_digest":"sha256:"+"c"*64,"quarantine_status":"INERT","ingest_result":"RECEIVED","independence_status":"UNKNOWN",
}

class LibraryCardTests(unittest.TestCase):
 def test_accepts_pseudonymous_card_without_civil_identity(self):
  r=evaluate_library_card(copy.deepcopy(BASE_CARD)); self.assertEqual(r["disposition"],"ACCEPT")
  self.assertEqual(r["receipt"]["mode"],"PERSISTENT_PSEUDONYM"); self.assertEqual(r["receipt"]["authority"],"none")
  self.assertNotIn("civil_identity",r["receipt"])
 def test_one_shot_anonymous_does_not_require_key(self):
  x=copy.deepcopy(BASE_CARD); x["card_id"]="card:anon:001"; x["mode"]="ONE_SHOT_ANONYMOUS"; x.pop("contributor_key_id")
  self.assertEqual(evaluate_library_card(x)["disposition"],"ACCEPT")
 def test_duplicate_capability_refuses(self):
  x=copy.deepcopy(BASE_CARD); x["capabilities"].append("deposit_counterexample")
  self.assertEqual(evaluate_library_card(x)["reason"],"invalid_capabilities")

class RightsTests(unittest.TestCase):
 def test_permissions_remain_separate(self):
  r=evaluate_rights_statement(copy.deepcopy(BASE_RIGHTS)); self.assertEqual(r["disposition"],"ACCEPT")
  self.assertEqual(r["receipt"]["publish"],"NO"); self.assertEqual(r["receipt"]["process"],"YES")

class DepositTests(unittest.TestCase):
 def test_anonymous_local_deposit_is_not_promoted(self):
  r=evaluate_commons_deposit(copy.deepcopy(BASE_DEPOSIT)); self.assertEqual(r["disposition"],"ACCEPT")
  self.assertEqual(r["receipt"]["authority"],"none"); self.assertEqual(r["receipt"]["independence_status"],"UNKNOWN")
 def test_tor_transport_does_not_change_authority(self):
  x=copy.deepcopy(BASE_DEPOSIT); x["transport_class"]="ONION_SERVICE"; r=evaluate_commons_deposit(x)
  self.assertEqual(r["receipt"]["transport_class"],"ONION_SERVICE"); self.assertEqual(r["receipt"]["authority"],"none")
 def test_arrival_cannot_claim_cleared_quarantine(self):
  x=copy.deepcopy(BASE_DEPOSIT); x["quarantine_status"]="CLEARED_FOR_PROCESSING"
  r=evaluate_commons_deposit(x); self.assertEqual(r["reason"],"arrival_must_be_inert")
 def test_arrival_cannot_claim_processed_state(self):
  x=copy.deepcopy(BASE_DEPOSIT); x["ingest_result"]="PROCESSED"
  r=evaluate_commons_deposit(x); self.assertEqual(r["reason"],"arrival_must_be_received")

class PseudonymContinuityTests(unittest.TestCase):
 def _bytes(self,key):
  return key.public_key().public_bytes(encoding=serialization.Encoding.Raw,format=serialization.PublicFormat.Raw)
 def test_valid_signature_establishes_key_continuity_not_civil_identity(self):
  k=Ed25519PrivateKey.generate(); message=b"alex-continuity:card:pseudo:001:deposit-002"
  proof={"schema":"alex.pseudonym-continuity/v0","card_id":"card:pseudo:001",
   "public_key_b64":base64.b64encode(self._bytes(k)).decode("ascii"),"message":message.decode("ascii"),
   "signature_b64":base64.b64encode(k.sign(message)).decode("ascii")}
  r=verify_pseudonym_continuity(proof); self.assertEqual(r["disposition"],"ACCEPT")
  self.assertEqual(r["receipt"]["continuity_status"],"VERIFIED_KEY_CONTINUITY")
  self.assertEqual(r["receipt"]["civil_identity_status"],"UNKNOWN"); self.assertEqual(r["receipt"]["authority"],"none")
 def test_bad_signature_refuses(self):
  k=Ed25519PrivateKey.generate(); other=Ed25519PrivateKey.generate(); message=b"alex-continuity:card:pseudo:001:deposit-002"
  proof={"schema":"alex.pseudonym-continuity/v0","card_id":"card:pseudo:001",
   "public_key_b64":base64.b64encode(self._bytes(k)).decode("ascii"),"message":message.decode("ascii"),
   "signature_b64":base64.b64encode(other.sign(message)).decode("ascii")}
  r=verify_pseudonym_continuity(proof); self.assertEqual(r["reason"],"signature_verification_failed")

class RunnerTests(unittest.TestCase):
 def test_local_runner_has_no_network_listener_and_accepts_deposit(self):
  runner=Path("tools/run_commons_intake.py").read_text(encoding="utf-8")
  for forbidden in ["socket.","http.server","Flask","FastAPI","uvicorn","listen("]:
   self.assertNotIn(forbidden,runner)
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/"deposit.json"; p.write_text(json.dumps(BASE_DEPOSIT),encoding="utf-8")
   cp=subprocess.run([sys.executable,"tools/run_commons_intake.py",str(p)],capture_output=True,text=True,check=False)
   self.assertEqual(cp.returncode,0,cp.stderr); payload=json.loads(cp.stdout)
   self.assertEqual(payload["disposition"],"ACCEPT"); self.assertEqual(payload["receipt"]["authority"],"none")

if __name__=="__main__": unittest.main()
