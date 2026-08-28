import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from alex_runtime.bookroom.book_model import propose_book_item
from alex_runtime.bookroom.loci import create_text_locus
from alex_runtime.bookroom.records import (
    AcquisitionRecord,
    BookModelItem,
    CanvasRecord,
    ReadingRecord,
    ResearchAssertion,
    ResearchPressure,
)
from alex_runtime.bookroom.research_model import (
    append_assertion,
    append_counterpressure,
    evaluate_support,
    retire_assertion,
)
from alex_runtime.bookroom.store import BookRoomStore


class BookRoomResearchModelTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = TemporaryDirectory()
        self.addCleanup(self.tempdir.cleanup)
        self.store = BookRoomStore.open(Path(self.tempdir.name))
        self.addCleanup(self.store.close)

        carrier_digest = self.store.put_object(b"research carrier")
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
        for sequence, (canvas_id, reading_id, text) in enumerate(
            (("P1", "R1", "captain commands the ship"), ("P2", "R2", "crew resists the command"))
        ):
            surface_digest = self.store.put_object(f"surface:{canvas_id}".encode())
            self.store.append_canvas(
                CanvasRecord(
                    canvas_id=canvas_id,
                    room_id="ROOM1",
                    acquisition_id="A1",
                    sequence=sequence,
                    printed_label=str(sequence + 1),
                    width_pt=612.0,
                    height_pt=792.0,
                    surface_digest=surface_digest,
                    created_at="2026-08-27T20:01:00Z",
                )
            )
            self.store.append_reading(
                ReadingRecord(
                    reading_id=reading_id,
                    room_id="ROOM1",
                    acquisition_id="A1",
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
        create_text_locus(self.store, locus_id="L1", reading_id="R1", char_start=0, char_end=7, created_at="2026-08-27T20:03:00Z")
        create_text_locus(self.store, locus_id="L2", reading_id="R2", char_start=0, char_end=4, created_at="2026-08-27T20:03:00Z")
        propose_book_item(
            self.store,
            BookModelItem(
                item_id="B1",
                room_id="ROOM1",
                kind="source_claim",
                label="Captain source claim",
                body="The source presents a captain-command relation.",
                locus_refs=("L1",),
                book_cut_id="CUT-END",
                projection_kind="materials",
                created_at="2026-08-27T20:04:00Z",
            ),
        )

    def assertion(self, assertion_id="H1", lifecycle="PROPOSED"):
        return ResearchAssertion(
            assertion_id=assertion_id,
            room_id="ROOM1",
            question_id="Q1",
            text="The captain is framed as a sovereignty figure.",
            book_cut_id="CUT-END",
            basis_refs=("B1",),
            discovery_refs=("query:sovereignty",),
            lifecycle=lifecycle,
            created_at="2026-08-27T20:10:00Z",
        )

    def test_counterevidence_is_pressure_not_a_contradicts_predicate(self):
        assertion = append_assertion(self.store, self.assertion())
        pressure = append_counterpressure(
            self.store,
            ResearchPressure(
                pressure_id="PRES1",
                room_id="ROOM1",
                assertion_id=assertion.assertion_id,
                kind="COUNTEREVIDENCE",
                basis_refs=("L2",),
                note="The crew resists the command.",
                book_cut_id="CUT-END",
                created_at="2026-08-27T20:11:00Z",
            ),
        )

        self.assertEqual(self.store.get_research_assertion("H1").lifecycle, "PROPOSED")
        self.assertEqual(pressure.kind, "COUNTEREVIDENCE")
        self.assertEqual([item.item_id for item in self.store.list_book_items("ROOM1")], ["B1"])
        self.assertEqual(self.store.list_relation_proposals("H1"), [])
        self.assertNotIn("CONTRADICTS", json.dumps(pressure.__dict__ if hasattr(pressure, "__dict__") else {"kind": pressure.kind}))

    def test_gate2_support_is_persisted_without_changing_research_lifecycle(self):
        append_assertion(self.store, self.assertion())
        result = evaluate_support(
            self.store,
            assertion_id="H1",
            evidence_locus_id="L1",
            witness_refs=("page-surface:P1",),
            case_id="CASE1",
            evidence_path_id="EP1",
            proposal_id="RP1",
            evaluation_id="EV1",
            execution_step_id="STEP1",
            conclusion_assertion_id="SUPPORT1",
        )

        self.assertEqual(result["evaluation"]["disposition"], "ACCEPT")
        self.assertEqual(result["conclusion_assertion"]["predicate"], "SUPPORTS")
        self.assertEqual(self.store.get_research_assertion("H1").lifecycle, "PROPOSED")
        self.assertEqual(self.store.get_relation_proposal("RP1")["predicate"], "SUPPORTS")
        self.assertEqual(self.store.get_relation_evaluation("EV1")["disposition"], "ACCEPT")
        self.assertNotIn("admitted", result)
        self.assertNotIn("authority", result)

    def test_retirement_appends_a_research_descendant(self):
        append_assertion(self.store, self.assertion())
        retired = retire_assertion(
            self.store,
            "H1",
            retired_assertion_id="H1-RET",
            created_at="2026-08-27T20:12:00Z",
        )

        self.assertEqual(self.store.get_research_assertion("H1").lifecycle, "PROPOSED")
        self.assertEqual(retired.lifecycle, "RETIRED")
        self.assertEqual(retired.supersedes_assertion_id, "H1")
        self.assertEqual([row.assertion_id for row in self.store.list_research_assertions("ROOM1")], ["H1", "H1-RET"])

    def test_insufficient_support_preserves_proposal_and_explicit_fog(self):
        append_assertion(self.store, self.assertion(assertion_id="H2"))
        append_counterpressure(
            self.store,
            ResearchPressure(
                pressure_id="FOG1",
                room_id="ROOM1",
                assertion_id="H2",
                kind="FOG",
                basis_refs=("L1",),
                note="No independent witness has been admitted for this support path.",
                book_cut_id="CUT-END",
                created_at="2026-08-27T20:13:00Z",
            ),
        )
        result = evaluate_support(
            self.store,
            assertion_id="H2",
            evidence_locus_id="L1",
            witness_refs=(),
            case_id="CASE2",
            evidence_path_id="EP2",
            proposal_id="RP2",
            evaluation_id="EV2",
            execution_step_id="STEP2",
            conclusion_assertion_id="SUPPORT2",
        )

        self.assertEqual(result["evaluation"]["disposition"], "INSUFFICIENT_TO_TEST")
        self.assertEqual(result["evaluation"]["reason_code"], "NO_ATTRIBUTABLE_SUPPORT_PATH")
        self.assertIsNone(result["conclusion_assertion"])
        self.assertEqual(self.store.get_research_assertion("H2").lifecycle, "PROPOSED")
        self.assertEqual([p.kind for p in self.store.list_research_pressures("H2")], ["FOG"])


if __name__ == "__main__":
    unittest.main()
