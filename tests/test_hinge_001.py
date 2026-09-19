import copy
import unittest

from research.hinge_001 import witness_grammar_delta


BASE_PRE = {
    "schema": "alex.hinge-grammar/v0",
    "grammar_ref": "grammar:before",
    "carrier": "text",
    "source_ref": "whole-return:crossing-001",
    "rules": [
        {"selector": "sign:hinge", "relation": "reading:mechanical-joint"},
        {"selector": "sign:wire", "relation": "reading:carrier"},
    ],
}

BASE_POST = {
    "schema": "alex.hinge-grammar/v0",
    "grammar_ref": "grammar:after",
    "carrier": "text",
    "source_ref": "whole-return:crossing-001",
    "rules": [
        {"selector": "sign:hinge", "relation": "reading:constitutive-relation"},
        {"selector": "sign:wire", "relation": "reading:carrier"},
        {"selector": "sign:crossing", "relation": "reading:relation-site"},
    ],
}


class Hinge001Tests(unittest.TestCase):
    def test_retargeted_selector_is_witnessed_without_authority(self):
        r = witness_grammar_delta(
            copy.deepcopy(BASE_PRE),
            "encounter:shaker-code-and-creed",
            copy.deepcopy(BASE_POST),
            ["sign:hinge", "sign:wire"],
        )
        self.assertEqual(r["disposition"], "ACCEPT")
        self.assertTrue(r["grammar_changed"])
        self.assertTrue(r["constitutive_candidate"])
        self.assertEqual(
            r["retargeted_rules"],
            [{
                "selector": "sign:hinge",
                "before": "reading:mechanical-joint",
                "after": "reading:constitutive-relation",
            }],
        )
        self.assertEqual(r["authority"], "none")
        self.assertEqual(r["meaning_verdict"], "none")
        self.assertEqual(r["causal_status"], "not_established")

    def test_added_selector_can_change_later_resolution(self):
        r = witness_grammar_delta(
            BASE_PRE,
            "encounter:shaker-code-and-creed",
            BASE_POST,
            ["sign:crossing"],
        )
        self.assertEqual(
            r["probe_results"],
            [{
                "selector": "sign:crossing",
                "before": None,
                "after": "reading:relation-site",
                "changed": True,
            }],
        )
        self.assertTrue(r["constitutive_candidate"])

    def test_rule_reordering_is_not_a_grammar_delta(self):
        post = copy.deepcopy(BASE_PRE)
        post["grammar_ref"] = "grammar:new-address-same-rules"
        post["rules"] = list(reversed(post["rules"]))
        r = witness_grammar_delta(
            BASE_PRE,
            "encounter:no-op",
            post,
            ["sign:hinge", "sign:wire"],
        )
        self.assertFalse(r["grammar_changed"])
        self.assertFalse(r["constitutive_candidate"])
        self.assertEqual(r["retargeted_rules"], [])

    def test_grammar_ref_change_alone_does_not_create_semantic_change(self):
        post = copy.deepcopy(BASE_PRE)
        post["grammar_ref"] = "grammar:new-ref-only"
        r = witness_grammar_delta(BASE_PRE, "encounter:no-op", post, ["sign:hinge"])
        self.assertFalse(r["grammar_changed"])
        self.assertFalse(r["probe_results"][0]["changed"])

    def test_carrier_change_is_outside_this_specimen(self):
        post = copy.deepcopy(BASE_POST)
        post["carrier"] = "image"
        r = witness_grammar_delta(BASE_PRE, "encounter:x", post, ["sign:hinge"])
        self.assertEqual(r["disposition"], "REFUSE")
        self.assertEqual(r["reason"], "carrier_changed")

    def test_duplicate_selector_is_refused(self):
        pre = copy.deepcopy(BASE_PRE)
        pre["rules"].append({"selector": "sign:hinge", "relation": "reading:duplicate"})
        r = witness_grammar_delta(pre, "encounter:x", BASE_POST, ["sign:hinge"])
        self.assertEqual(r["disposition"], "REFUSE")
        self.assertEqual(r["reason"], "invalid_grammar_snapshot")

    def test_duplicate_probe_is_refused(self):
        r = witness_grammar_delta(
            BASE_PRE,
            "encounter:x",
            BASE_POST,
            ["sign:hinge", "sign:hinge"],
        )
        self.assertEqual(r["disposition"], "REFUSE")
        self.assertEqual(r["reason"], "duplicate_probe")


if __name__ == "__main__":
    unittest.main()
