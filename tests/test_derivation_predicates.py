import unittest

from alex_runtime.predicates import predicate_minting_class, semantic_predicate_allowed


class PredicateMintingTests(unittest.TestCase):
    def test_mechanical_relation_is_not_semantic(self):
        self.assertEqual(predicate_minting_class("derived_from"), "MECHANICAL_WITNESSED")
        self.assertFalse(semantic_predicate_allowed("alex.runtime/derivation-m0", "derived_from"))

    def test_supports_is_the_only_m0_semantic_predicate(self):
        self.assertEqual(predicate_minting_class("SUPPORTS"), "SEMANTIC_EVALUATED")
        self.assertTrue(semantic_predicate_allowed("alex.runtime/derivation-m0", "SUPPORTS"))
        self.assertFalse(semantic_predicate_allowed("alex.runtime/derivation-m0", "RESEMBLES"))

    def test_unknown_predicate_is_not_silently_classified(self):
        self.assertIsNone(predicate_minting_class("MAGICALLY_AUTHORIZES"))


if __name__ == "__main__":
    unittest.main()
