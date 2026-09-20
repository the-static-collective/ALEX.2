import unittest
from alex_runtime.relation_nursery import propose_relation, attach_pressure

class NurseryTests(unittest.TestCase):
    def seed(self):
        return propose_relation(proposal_id="fixture:one",
            source_refs=["fixture:egypt","fixture:china"],
            relation_expression="1+2+2+4+1=10", method_ref="fixture:arithmetic",
            author_ref="fixture:researcher")
    def test_pressure_does_not_rewrite_source(self):
        p=self.seed(); result=attach_pressure(p,experiment_ref="fixture:control",
            result="fail",observation_ref="fixture:observed-miss",interpretation="unresolved")
        self.assertEqual(p["disposition"],"proposed")
        self.assertEqual(result["result"],"fail")
        self.assertEqual(result["proposal_ref"],p["proposal_digest"])
    def test_tampered_source_ref_refused(self):
        p=self.seed();p["source_refs"][0]="fixture:replacement"
        with self.assertRaisesRegex(ValueError,"rewritten"):
            attach_pressure(p,experiment_ref="fixture:control",result="pass",
                observation_ref="fixture:witness",interpretation="not_assessed")
    def test_refuse_duplicate_source_and_non_domain_result(self):
        with self.assertRaises(ValueError):
            propose_relation(proposal_id="x",source_refs=["same","same"],
                relation_expression="a=b",method_ref="m",author_ref="human")
        with self.assertRaises(ValueError):
            attach_pressure(self.seed(),experiment_ref="r",result="proof-of-divinity",
                observation_ref="o",interpretation="not_assessed")

if __name__ == "__main__":unittest.main()
