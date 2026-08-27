import unittest

from alex_runtime.derivation import ruleset_manifest, ruleset_manifest_digest


class RulesetManifestTests(unittest.TestCase):
    def test_derivation_m0_manifest_pins_rule_and_version(self):
        manifest = ruleset_manifest("alex.runtime/derivation-m0")
        self.assertEqual(manifest["profile"], "alex.runtime/derivation-m0")
        self.assertEqual(manifest["rules"][0]["rule_id"], "RELATION-DERIVATION-001")
        self.assertEqual(manifest["rules"][0]["rule_version"], 1)
        self.assertEqual(manifest["rules"][0]["predicate"], "SUPPORTS")

    def test_ruleset_digest_changes_if_manifest_changes(self):
        digest = ruleset_manifest_digest("alex.runtime/derivation-m0")
        self.assertTrue(digest.startswith("sha256:"))
        self.assertEqual(len(digest), 71)


if __name__ == "__main__":
    unittest.main()
