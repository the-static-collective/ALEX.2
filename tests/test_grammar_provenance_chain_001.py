import unittest

from research.grammar_provenance_chain_001 import witness_reading_at_cut


G0 = {
    "schema": "alex.hinge-grammar/v0",
    "grammar_ref": "grammar:g0",
    "carrier": "text",
    "source_ref": "carrier:fixed-001",
    "available_from": "2026-09-18T10:00:00Z",
    "rules": [{"selector": "sign:hinge", "relation": "reading:mechanical-joint"}],
}

G1 = {
    "schema": "alex.hinge-grammar/v0",
    "grammar_ref": "grammar:g1",
    "carrier": "text",
    "source_ref": "carrier:fixed-001",
    "available_from": "2026-09-18T11:00:00Z",
    "rules": [{"selector": "sign:hinge", "relation": "reading:constitutive-relation"}],
}


class GrammarProvenanceChain001Tests(unittest.TestCase):
    def test_historical_reading_uses_grammar_available_at_cut(self):
        r = witness_reading_at_cut(
            G0, "sign:hinge", "2026-09-18T10:30:00Z", "2026-09-18T10:30:00Z"
        )
        self.assertEqual(r["relation"], "reading:mechanical-joint")
        self.assertEqual(r["binding_mode"], "historical_reading")
        self.assertTrue(r["available_at_subject_cut"])

    def test_later_grammar_may_reread_old_carrier_without_backdating_it(self):
        r = witness_reading_at_cut(
            G1, "sign:hinge", "2026-09-18T10:30:00Z", "2026-09-18T11:30:00Z"
        )
        self.assertEqual(r["relation"], "reading:constitutive-relation")
        self.assertEqual(r["binding_mode"], "retrospective_rereading")
        self.assertFalse(r["available_at_subject_cut"])
        self.assertEqual(r["grammar_available_from"], "2026-09-18T11:00:00Z")
        self.assertEqual(r["authority"], "none")
        self.assertEqual(r["meaning_verdict"], "none")

    def test_later_grammar_cannot_be_applied_before_it_exists(self):
        r = witness_reading_at_cut(
            G1, "sign:hinge", "2026-09-18T10:30:00Z", "2026-09-18T10:30:00Z"
        )
        self.assertEqual(r["disposition"], "REFUSE")
        self.assertEqual(r["reason"], "grammar_not_yet_available")

    def test_current_rereading_does_not_mutate_historical_receipt(self):
        historical = witness_reading_at_cut(
            G0, "sign:hinge", "2026-09-18T10:30:00Z", "2026-09-18T10:30:00Z"
        )
        before = dict(historical)
        rereading = witness_reading_at_cut(
            G1, "sign:hinge", "2026-09-18T10:30:00Z", "2026-09-18T11:30:00Z"
        )
        self.assertEqual(historical, before)
        self.assertNotEqual(historical["relation"], rereading["relation"])
        self.assertEqual(historical["binding_mode"], "historical_reading")
        self.assertEqual(rereading["binding_mode"], "retrospective_rereading")


if __name__ == "__main__":
    unittest.main()
