import unittest
from dataclasses import FrozenInstanceError, fields

from alex_runtime.bookroom.records import (
    AcquisitionRecord,
    BookCut,
    BookModelItem,
    BookRoomIdentity,
    CanvasRecord,
    ContextPack,
    DossierReceipt,
    ReadingRecord,
    ResearchAssertion,
    ResearchPressure,
    SourceLocusRecord,
    record_digest,
)


class BookRoomRecordTests(unittest.TestCase):
    def test_book_and_research_records_are_distinct_and_frozen(self):
        book = BookModelItem(
            item_id="B1",
            room_id="ROOM1",
            kind="source_claim",
            label="Captain claim",
            body="The source names Ahab as captain.",
            locus_refs=("L1",),
            book_cut_id="CUT-END",
            projection_kind="materials",
            created_at="2026-08-27T20:00:00Z",
        )
        research = ResearchAssertion(
            assertion_id="H1",
            room_id="ROOM1",
            question_id="Q1",
            text="Ahab functions as a sovereignty figure.",
            book_cut_id="CUT-END",
            basis_refs=("B1",),
            discovery_refs=(),
            lifecycle="PROPOSED",
            created_at="2026-08-27T20:01:00Z",
        )

        self.assertNotEqual(type(book), type(research))
        self.assertNotEqual(record_digest(book), record_digest(research))
        with self.assertRaises(FrozenInstanceError):
            book.body = "rewritten"

    def test_empty_occurrence_ids_are_rejected(self):
        with self.assertRaises(ValueError):
            BookRoomIdentity(
                room_id="",
                work_ref="work:W1",
                carrier_ref="carrier:C1",
                acquisition_id="A1",
                object_digest="sha256:abc",
                page_count=1,
                created_at="2026-08-27T20:00:00Z",
            )

        with self.assertRaises(ValueError):
            ReadingRecord(
                reading_id="",
                room_id="ROOM1",
                acquisition_id="A1",
                canvas_id="P1",
                parent_reading_id=None,
                method="pdf_text_layer",
                producer="fixture",
                producer_version="1",
                status="OBSERVED",
                text="hello",
                created_at="2026-08-27T20:00:00Z",
            )

    def test_duplicate_reference_tuples_are_rejected(self):
        with self.assertRaises(ValueError):
            BookModelItem(
                item_id="B1",
                room_id="ROOM1",
                kind="source_claim",
                label="claim",
                body="body",
                locus_refs=("L1", "L1"),
                book_cut_id="CUT1",
                projection_kind="materials",
                created_at="2026-08-27T20:00:00Z",
            )

        with self.assertRaises(ValueError):
            ResearchAssertion(
                assertion_id="H1",
                room_id="ROOM1",
                question_id="Q1",
                text="claim",
                book_cut_id="CUT1",
                basis_refs=("B1", "B1"),
                discovery_refs=(),
                lifecycle="PROPOSED",
                created_at="2026-08-27T20:00:00Z",
            )

    def test_projection_kind_is_closed_and_explicit(self):
        allowed = {"characters", "world", "plot", "materials", "chapters"}
        for projection_kind in allowed:
            item = BookModelItem(
                item_id=f"B-{projection_kind}",
                room_id="ROOM1",
                kind="source_claim",
                label="claim",
                body="body",
                locus_refs=("L1",),
                book_cut_id="CUT1",
                projection_kind=projection_kind,
                created_at="2026-08-27T20:00:00Z",
            )
            self.assertEqual(item.projection_kind, projection_kind)

        with self.assertRaises(ValueError):
            BookModelItem(
                item_id="B-bad",
                room_id="ROOM1",
                kind="source_claim",
                label="claim",
                body="body",
                locus_refs=("L1",),
                book_cut_id="CUT1",
                projection_kind="truth",
                created_at="2026-08-27T20:00:00Z",
            )

    def test_research_lifecycle_is_not_evaluator_disposition(self):
        for lifecycle in ("PROPOSED", "RETIRED"):
            assertion = ResearchAssertion(
                assertion_id=f"H-{lifecycle}",
                room_id="ROOM1",
                question_id="Q1",
                text="claim",
                book_cut_id="CUT1",
                basis_refs=("B1",),
                discovery_refs=(),
                lifecycle=lifecycle,
                created_at="2026-08-27T20:00:00Z",
            )
            self.assertEqual(assertion.lifecycle, lifecycle)

        for forbidden in ("ACCEPT", "REFUSE", "SUPPORTED", "ADMITTED"):
            with self.assertRaises(ValueError):
                ResearchAssertion(
                    assertion_id=f"H-{forbidden}",
                    room_id="ROOM1",
                    question_id="Q1",
                    text="claim",
                    book_cut_id="CUT1",
                    basis_refs=("B1",),
                    discovery_refs=(),
                    lifecycle=forbidden,
                    created_at="2026-08-27T20:00:00Z",
                )

    def test_source_locus_requires_surface_identity_and_valid_span(self):
        locus = SourceLocusRecord(
            locus_id="L1",
            room_id="ROOM1",
            acquisition_id="A1",
            canvas_id="P1",
            reading_id="R1",
            char_start=0,
            char_end=5,
            exact_text="hello",
            bbox_pdf=None,
            surface_digest="sha256:surface",
            created_at="2026-08-27T20:00:00Z",
        )
        self.assertEqual(locus.surface_digest, "sha256:surface")

        with self.assertRaises(ValueError):
            SourceLocusRecord(
                locus_id="L2",
                room_id="ROOM1",
                acquisition_id="A1",
                canvas_id="P1",
                reading_id="R1",
                char_start=5,
                char_end=4,
                exact_text="",
                bbox_pdf=None,
                surface_digest="sha256:surface",
                created_at="2026-08-27T20:00:00Z",
            )

    def test_public_record_types_do_not_expose_authority_or_truth_fields(self):
        forbidden = {"truth", "authority", "admitted", "canon"}
        record_types = (
            BookRoomIdentity,
            AcquisitionRecord,
            CanvasRecord,
            ReadingRecord,
            SourceLocusRecord,
            BookModelItem,
            ResearchAssertion,
            ResearchPressure,
            BookCut,
            ContextPack,
            DossierReceipt,
        )
        for record_type in record_types:
            names = {field.name for field in fields(record_type)}
            self.assertTrue(forbidden.isdisjoint(names), record_type.__name__)


if __name__ == "__main__":
    unittest.main()
