import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from bookroom_pdf_fixture import write_encrypted_pdf, write_text_pdf
from alex_runtime.bookroom.pdf_adapter import PdfIngestError, ingest_pdf
from alex_runtime.bookroom.store import BookRoomStore, RecordConflict, RecordNotFound


class BookRoomPdfAdapterTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.root = Path(self.tempdir.name)
        self.store = BookRoomStore.open(self.root / "store")
        self.addCleanup(self.store.close)

    def ingest(self, path: Path, acquisition_id: str = "A1"):
        return ingest_pdf(
            self.store,
            path,
            room_id="ROOM1",
            work_ref="work:W1",
            carrier_ref="carrier:C1",
            acquisition_id=acquisition_id,
            source_locator=str(path),
            acquired_at="2026-08-27T20:00:00Z",
            rights_status="local-test",
            egress_policy_ref="egress:none",
        )

    def test_ingests_exact_carrier_pages_surfaces_and_text_layer_readings(self):
        pdf = write_text_pdf(
            self.root / "book.pdf",
            ["alpha whale", "beta rope", "gamma sea", ""],
        )
        identity = self.ingest(pdf)

        self.assertEqual(identity.room_id, "ROOM1")
        self.assertEqual(identity.acquisition_id, "A1")
        self.assertEqual(identity.page_count, 4)
        self.assertTrue(identity.object_digest.startswith("sha256:"))
        self.assertEqual(self.store.get_acquisition("A1").object_digest, identity.object_digest)

        canvases = self.store.list_canvases("A1")
        self.assertEqual([canvas.sequence for canvas in canvases], [0, 1, 2, 3])
        for canvas in canvases:
            surface = self.store.get_object(canvas.surface_digest)
            self.assertTrue(surface.startswith(b"\x89PNG\r\n\x1a\n"))

        readings = self.store.list_readings("A1")
        self.assertEqual(len(readings), 4)
        self.assertTrue(all(reading.method == "pdf_text_layer" for reading in readings))
        self.assertIn("alpha whale", readings[0].text)
        self.assertIn("beta rope", readings[1].text)
        self.assertIn("gamma sea", readings[2].text)
        self.assertEqual(readings[3].status, "FOG")
        self.assertFalse(readings[3].text.strip())

    def test_nonexistent_nonpdf_and_encrypted_carriers_are_refused(self):
        with self.assertRaises(PdfIngestError):
            self.ingest(self.root / "missing.pdf", acquisition_id="MISSING")

        junk = self.root / "junk.pdf"
        junk.write_bytes(b"not a pdf")
        with self.assertRaises(PdfIngestError):
            self.ingest(junk, acquisition_id="JUNK")

        encrypted = write_encrypted_pdf(self.root / "encrypted.pdf")
        with self.assertRaises(PdfIngestError):
            self.ingest(encrypted, acquisition_id="ENC")

        for acquisition_id in ("MISSING", "JUNK", "ENC"):
            with self.assertRaises(RecordNotFound):
                self.store.get_acquisition(acquisition_id)

    def test_duplicate_acquisition_id_cannot_be_rebound_to_changed_carrier_bytes(self):
        first = write_text_pdf(self.root / "first.pdf", ["first carrier"])
        second = write_text_pdf(self.root / "second.pdf", ["different carrier"])
        self.ingest(first, acquisition_id="A1")
        with self.assertRaises(RecordConflict):
            self.ingest(second, acquisition_id="A1")


if __name__ == "__main__":
    unittest.main()
