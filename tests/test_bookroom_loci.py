import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from alex_runtime.bookroom.loci import InvalidLocus, LocusMismatch, create_text_locus, resolve_quote
from alex_runtime.bookroom.records import AcquisitionRecord, CanvasRecord, ReadingRecord, SourceLocusRecord
from alex_runtime.bookroom.store import BookRoomStore, ReferenceMismatch


class BookRoomLocusTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.store = BookRoomStore.open(Path(self.tempdir.name))
        self.addCleanup(self.store.close)

        carrier_digest = self.store.put_object(b"carrier")
        self.store.append_acquisition(
            AcquisitionRecord(
                acquisition_id="A1",
                room_id="ROOM1",
                work_ref="work:W1",
                carrier_ref="carrier:C1",
                object_digest=carrier_digest,
                source_locator="fixture.pdf",
                acquired_at="2026-08-27T20:00:00Z",
                rights_status="local-test",
                egress_policy_ref="egress:none",
            )
        )
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
        self.store.append_reading(
            ReadingRecord(
                reading_id="R1",
                room_id="ROOM1",
                acquisition_id="A1",
                canvas_id="P1",
                parent_reading_id=None,
                method="pdf_text_layer",
                producer="fixture",
                producer_version="1",
                status="OBSERVED",
                text="alpha hello omega",
                created_at="2026-08-27T20:02:00Z",
            )
        )

    def test_quote_resolves_to_exact_reading_slice_and_page_surface(self):
        locus = create_text_locus(
            self.store,
            locus_id="L1",
            reading_id="R1",
            char_start=6,
            char_end=11,
            created_at="2026-08-27T20:10:00Z",
        )
        quote = resolve_quote(self.store, "L1")
        self.assertEqual(locus.exact_text, "hello")
        self.assertEqual(quote["exact_text"], self.store.get_reading("R1").text[6:11])
        self.assertEqual(quote["surface_digest"], self.store.get_canvas("P1").surface_digest)
        self.assertEqual(quote["acquisition_id"], "A1")
        self.assertEqual(quote["canvas_sequence"], 0)

    def test_out_of_range_and_mismatched_exact_text_are_refused(self):
        with self.assertRaises(InvalidLocus):
            create_text_locus(
                self.store,
                locus_id="L-bad-range",
                reading_id="R1",
                char_start=6,
                char_end=999,
                created_at="2026-08-27T20:10:00Z",
            )

        with self.assertRaises(LocusMismatch):
            create_text_locus(
                self.store,
                locus_id="L-bad-text",
                reading_id="R1",
                char_start=6,
                char_end=11,
                exact_text="world",
                created_at="2026-08-27T20:10:00Z",
            )

    def test_cross_acquisition_locus_and_missing_surface_identity_are_refused(self):
        digest = self.store.put_object(b"second carrier")
        self.store.append_acquisition(
            AcquisitionRecord(
                acquisition_id="A2",
                room_id="ROOM1",
                work_ref="work:W1",
                carrier_ref="carrier:C2",
                object_digest=digest,
                source_locator="fixture-2.pdf",
                acquired_at="2026-08-27T20:20:00Z",
                rights_status="local-test",
                egress_policy_ref="egress:none",
            )
        )
        with self.assertRaises(ReferenceMismatch):
            self.store.append_source_locus(
                SourceLocusRecord(
                    locus_id="L-cross",
                    room_id="ROOM1",
                    acquisition_id="A2",
                    canvas_id="P1",
                    reading_id="R1",
                    char_start=0,
                    char_end=5,
                    exact_text="alpha",
                    bbox_pdf=None,
                    surface_digest=self.store.get_canvas("P1").surface_digest,
                    created_at="2026-08-27T20:21:00Z",
                )
            )

        with self.assertRaises(ValueError):
            SourceLocusRecord(
                locus_id="L-no-surface",
                room_id="ROOM1",
                acquisition_id="A1",
                canvas_id="P1",
                reading_id="R1",
                char_start=0,
                char_end=5,
                exact_text="alpha",
                bbox_pdf=None,
                surface_digest="",
                created_at="2026-08-27T20:21:00Z",
            )


if __name__ == "__main__":
    unittest.main()
