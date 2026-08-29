import copy
import unittest

from alex_runtime.name_attestation import evaluate_name_attestation


BASE_ATTESTATION = {
    "schema": "alex.name-attestation/v0",
    "attestation_id": "matt-1-21-iesous",
    "source_world": "B",
    "artifact_id": "na28-matthew",
    "locus": "Matthew 1:21",
    "language": "grc",
    "script": "Greek",
    "raw_form": "Ἰησοῦς",
    "reading_status": "editorial_transcription",
    "referent": "Jesus of Nazareth",
    "referent_confidence": "high",
}


class NameAttestationTests(unittest.TestCase):
    def test_accepts_bounded_attestation_and_freezes_authority(self):
        record = copy.deepcopy(BASE_ATTESTATION)
        record["authority"] = "canon"
        result = evaluate_name_attestation(record)
        self.assertEqual(result["disposition"], "ACCEPT")
        self.assertEqual(result["schema"], "alex.name-attestation-result/v0")
        self.assertEqual(result["receipt"]["raw_form"], "Ἰησοῦς")
        self.assertEqual(result["receipt"]["source_world"], "B")
        self.assertEqual(result["receipt"]["authority"], "none")
        self.assertTrue(result["receipt"]["attestation_digest"].startswith("sha256:"))

    def test_unicode_change_changes_attestation_identity(self):
        first = evaluate_name_attestation(copy.deepcopy(BASE_ATTESTATION))
        second_record = copy.deepcopy(BASE_ATTESTATION)
        second_record["raw_form"] = "ΙΗΣΟΥΣ"
        second = evaluate_name_attestation(second_record)
        self.assertNotEqual(
            first["receipt"]["attestation_digest"],
            second["receipt"]["attestation_digest"],
        )

    def test_source_world_is_part_of_attestation_identity(self):
        first = evaluate_name_attestation(copy.deepcopy(BASE_ATTESTATION))
        second_record = copy.deepcopy(BASE_ATTESTATION)
        second_record["source_world"] = "D"
        second = evaluate_name_attestation(second_record)
        self.assertNotEqual(
            first["receipt"]["attestation_digest"],
            second["receipt"]["attestation_digest"],
        )

    def test_rejects_invalid_source_world(self):
        record = copy.deepcopy(BASE_ATTESTATION)
        record["source_world"] = "Z"
        result = evaluate_name_attestation(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "invalid_source_world")
        self.assertEqual(result["authority"], "none")

    def test_rejects_blank_required_field(self):
        record = copy.deepcopy(BASE_ATTESTATION)
        record["raw_form"] = ""
        result = evaluate_name_attestation(record)
        self.assertEqual(result["disposition"], "REFUSE")
        self.assertEqual(result["reason"], "missing_required_field")


if __name__ == "__main__":
    unittest.main()
