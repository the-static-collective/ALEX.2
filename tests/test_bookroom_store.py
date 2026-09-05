import unittest
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from alex_runtime.bookroom.records import AcquisitionRecord, CanvasRecord, ReadingRecord
from alex_runtime.bookroom.store import BookRoomStore, RecordConflict


class BookRoomStoreTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.store = BookRoomStore.open(Path(self.tempdir.name))
        self.addCleanup(self.store.close)

    def acquisition(self, acquisition_id: str, digest: str) -> AcquisitionRecord:
        return AcquisitionRecord(
            acquisition_id=acquisition_id,
            room_id="ROOM1",
            work_ref="work:W1",
            carrier_ref="carrier:C1",
            object_digest=digest,
            source_locator="fixture.pdf",
            acquired_at="2026-08-27T20:00:00Z",
            rights_status="local-test",
            egress_policy_ref="egress:none",
        )

    def test_equal_bytes_deduplicate_without_collapsing_acquisition_occurrences(self):
        d1 = self.store.put_object(b"same bytes")
        d2 = self.store.put_object(b"same bytes")
        self.assertEqual(d1, d2)

        a1 = self.store.append_acquisition(self.acquisition("A1", d1))
        a2 = self.store.append_acquisition(self.acquisition("A2", d2))
        self.assertEqual(a1.object_digest, a2.object_digest)
        self.assertNotEqual(a1.acquisition_id, a2.acquisition_id)

    def test_exact_occurrence_replay_is_idempotent_but_changed_payload_conflicts(self):
        digest = self.store.put_object(b"carrier")
        acquisition = self.acquisition("A1", digest)
        self.assertEqual(self.store.append_acquisition(acquisition), acquisition)
        self.assertEqual(self.store.append_acquisition(acquisition), acquisition)

        with self.assertRaises(RecordConflict):
            self.store.append_acquisition(replace(acquisition, carrier_ref="carrier:C2"))

    def test_reading_corrections_append_and_fts_search_returns_the_descendant(self):
        carrier_digest = self.store.put_object(b"carrier")
        self.store.append_acquisition(self.acquisition("A1", carrier_digest))
        surface_digest = self.store.put_object(b"page surface")
        self.store.append_canvas(
            CanvasRecord(
                canvas_id="P1",
                room_id="ROOM1",
                acquisition_id="A1",
                sequence=0,
                printed_label="1",
                width_pt=612.0,
                height_pt=792.0,
                surface_digest=surface_digest,
                created_at="2026-08-27T20:01:00Z",
            )
        )
        first = ReadingRecord(
            reading_id="R1",
            room_id="ROOM1",
            acquisition_id="A1",
            canvas_id="P1",
            parent_reading_id=None,
            method="pdf_text_layer",
            producer="fixture",
            producer_version="1",
            status="OBSERVED",
            text="the pale whale",
            created_at="2026-08-27T20:02:00Z",
        )
        corrected = ReadingRecord(
            reading_id="R2",
            room_id="ROOM1",
            acquisition_id="A1",
            canvas_id="P1",
            parent_reading_id="R1",
            method="human_correction",
            producer="human:test",
            producer_version="1",
            status="OBSERVED",
            text="the white whale",
            created_at="2026-08-27T20:03:00Z",
        )
        self.store.append_reading(first)
        self.store.append_reading(corrected)

        self.assertEqual(self.store.get_reading("R2").parent_reading_id, "R1")
        hits = self.store.search_readings('"white whale"')
        self.assertEqual([hit.reading_id for hit in hits], ["R2"])


if __name__ == "__main__":
    unittest.main()
