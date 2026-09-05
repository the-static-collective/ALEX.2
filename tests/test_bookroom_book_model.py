import unittest
from dataclasses import replace
from pathlib import Path
from tempfile import TemporaryDirectory

from alex_runtime.bookroom.book_model import (
    MissingSourceLocus,
    SourceJurisdictionMismatch,
    book_item_source_chain,
    propose_book_item,
)
from alex_runtime.bookroom.loci import create_text_locus
from alex_runtime.bookroom.records import (
    AcquisitionRecord,
    BookModelItem,
    CanvasRecord,
    ReadingRecord,
)
from alex_runtime.bookroom.store import BookRoomStore, RecordNotFound


class BookRoomBookModelTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.store = BookRoomStore.open(Path(self.tempdir.name))
        self.addCleanup(self.store.close)
        self._add_source("ROOM1", "A1", "P1", "R1", "alpha captain whale", "L1", 6, 13)
        self._add_source("ROOM2", "A2", "P2", "R2", "beta foreign rope", "L2", 5, 12)

    def _add_source(
        self,
        room_id: str,
        acquisition_id: str,
        canvas_id: str,
        reading_id: str,
        text: str,
        locus_id: str,
        start: int,
        end: int,
    ) -> None:
        carrier_digest = self.store.put_object(f"carrier:{acquisition_id}".encode())
        self.store.append_acquisition(
            AcquisitionRecord(
                acquisition_id=acquisition_id,
                room_id=room_id,
                work_ref=f"work:{room_id}",
                carrier_ref=f"carrier:{acquisition_id}",
                object_digest=carrier_digest,
                source_locator=f"{acquisition_id}.pdf",
                acquired_at="2026-08-27T20:00:00Z",
                rights_status="local-test",
                egress_policy_ref="egress:none",
            )
        )
        surface_digest = self.store.put_object(f"surface:{canvas_id}".encode())
        self.store.append_canvas(
            CanvasRecord(
                canvas_id=canvas_id,
                room_id=room_id,
                acquisition_id=acquisition_id,
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
                reading_id=reading_id,
                room_id=room_id,
                acquisition_id=acquisition_id,
                canvas_id=canvas_id,
                parent_reading_id=None,
                method="pdf_text_layer",
                producer="fixture",
                producer_version="1",
                status="OBSERVED",
                text=text,
                created_at="2026-08-27T20:02:00Z",
            )
        )
        create_text_locus(
            self.store,
            locus_id=locus_id,
            reading_id=reading_id,
            char_start=start,
            char_end=end,
            created_at="2026-08-27T20:03:00Z",
        )

    def item(self, *, item_id="B1", kind="source_claim", projection_kind="materials", locus_refs=("L1",), supersedes=None):
        return BookModelItem(
            item_id=item_id,
            room_id="ROOM1",
            kind=kind,
            label=f"{kind} card",
            body=f"source-local {kind}",
            locus_refs=locus_refs,
            book_cut_id="CUT-END",
            projection_kind=projection_kind,
            created_at="2026-08-27T20:10:00Z",
            supersedes_item_id=supersedes,
        )

    def test_source_local_kinds_are_attributable_to_exact_loci(self):
        cases = [
            ("entity", "characters"),
            ("world", "world"),
            ("thread", "plot"),
            ("material", "materials"),
            ("section", "chapters"),
            ("source_claim", "materials"),
        ]
        for index, (kind, projection_kind) in enumerate(cases):
            item = self.item(item_id=f"B{index}", kind=kind, projection_kind=projection_kind)
            self.assertEqual(propose_book_item(self.store, item), item)
            chain = book_item_source_chain(self.store, item.item_id)
            self.assertEqual(chain["item"].item_id, item.item_id)
            self.assertEqual(chain["loci"][0].locus_id, "L1")
            self.assertEqual(chain["acquisition_ids"], ("A1",))

    def test_missing_research_or_projection_refs_cannot_impersonate_source_loci(self):
        for bad_ref in ("NOPE", "H1", "novelist/materials/generated.md"):
            with self.subTest(bad_ref=bad_ref):
                with self.assertRaises(MissingSourceLocus):
                    propose_book_item(self.store, replace(self.item(), locus_refs=(bad_ref,)))

        with self.assertRaises(RecordNotFound):
            self.store.get_book_item("B1")

    def test_cross_room_locus_is_refused(self):
        with self.assertRaises(SourceJurisdictionMismatch):
            propose_book_item(self.store, replace(self.item(), locus_refs=("L2",)))

    def test_correction_appends_descendant_without_rewriting_parent(self):
        original = self.item(item_id="B1")
        corrected = replace(
            self.item(item_id="B2"),
            body="corrected source-local claim",
            supersedes_item_id="B1",
            created_at="2026-08-27T20:11:00Z",
        )
        propose_book_item(self.store, original)
        propose_book_item(self.store, corrected)

        self.assertEqual(self.store.get_book_item("B1").body, original.body)
        self.assertEqual(self.store.get_book_item("B2").supersedes_item_id, "B1")
        self.assertEqual([item.item_id for item in self.store.list_book_items("ROOM1")], ["B1", "B2"])


if __name__ == "__main__":
    unittest.main()
