from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from alex_runtime.digests import sha256_json

PROJECTION_KINDS = frozenset({"characters", "world", "plot", "materials", "chapters"})
RESEARCH_LIFECYCLES = frozenset({"PROPOSED", "RETIRED"})


def _require_text(**values: str | None) -> None:
    for name, value in values.items():
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name} must be a non-empty string")


def _require_unique_refs(name: str, values: tuple[str, ...]) -> None:
    if not isinstance(values, tuple):
        raise ValueError(f"{name} must be a tuple")
    if any(not isinstance(value, str) or not value.strip() for value in values):
        raise ValueError(f"{name} must contain non-empty strings")
    if len(values) != len(set(values)):
        raise ValueError(f"{name} must contain unique refs")


def record_digest(record: Any) -> str:
    return sha256_json({"record_type": type(record).__name__, **asdict(record)})


@dataclass(frozen=True, slots=True)
class BookRoomIdentity:
    room_id: str
    work_ref: str
    carrier_ref: str
    acquisition_id: str
    object_digest: str
    page_count: int
    created_at: str

    def __post_init__(self) -> None:
        _require_text(room_id=self.room_id, work_ref=self.work_ref, carrier_ref=self.carrier_ref,
                      acquisition_id=self.acquisition_id, object_digest=self.object_digest,
                      created_at=self.created_at)
        if isinstance(self.page_count, bool) or not isinstance(self.page_count, int) or self.page_count < 0:
            raise ValueError("page_count must be a non-negative integer")


@dataclass(frozen=True, slots=True)
class AcquisitionRecord:
    acquisition_id: str
    room_id: str
    work_ref: str
    carrier_ref: str
    object_digest: str
    source_locator: str
    acquired_at: str
    rights_status: str
    egress_policy_ref: str

    def __post_init__(self) -> None:
        _require_text(acquisition_id=self.acquisition_id, room_id=self.room_id, work_ref=self.work_ref,
                      carrier_ref=self.carrier_ref, object_digest=self.object_digest,
                      source_locator=self.source_locator, acquired_at=self.acquired_at,
                      rights_status=self.rights_status, egress_policy_ref=self.egress_policy_ref)


@dataclass(frozen=True, slots=True)
class CanvasRecord:
    canvas_id: str
    room_id: str
    acquisition_id: str
    sequence: int
    printed_label: str | None
    width_pt: float
    height_pt: float
    surface_digest: str
    created_at: str

    def __post_init__(self) -> None:
        _require_text(canvas_id=self.canvas_id, room_id=self.room_id,
                      acquisition_id=self.acquisition_id, surface_digest=self.surface_digest,
                      created_at=self.created_at)
        if isinstance(self.sequence, bool) or not isinstance(self.sequence, int) or self.sequence < 0:
            raise ValueError("sequence must be a non-negative integer")
        if not isinstance(self.width_pt, (int, float)) or self.width_pt <= 0:
            raise ValueError("width_pt must be positive")
        if not isinstance(self.height_pt, (int, float)) or self.height_pt <= 0:
            raise ValueError("height_pt must be positive")
        if self.printed_label is not None and not isinstance(self.printed_label, str):
            raise ValueError("printed_label must be string or null")


@dataclass(frozen=True, slots=True)
class ReadingRecord:
    reading_id: str
    room_id: str
    acquisition_id: str
    canvas_id: str
    parent_reading_id: str | None
    method: str
    producer: str
    producer_version: str
    status: str
    text: str
    created_at: str

    def __post_init__(self) -> None:
        _require_text(reading_id=self.reading_id, room_id=self.room_id,
                      acquisition_id=self.acquisition_id, canvas_id=self.canvas_id,
                      method=self.method, producer=self.producer,
                      producer_version=self.producer_version, status=self.status,
                      created_at=self.created_at)
        if self.parent_reading_id is not None:
            _require_text(parent_reading_id=self.parent_reading_id)
        if not isinstance(self.text, str):
            raise ValueError("text must be a string")


@dataclass(frozen=True, slots=True)
class SourceLocusRecord:
    locus_id: str
    room_id: str
    acquisition_id: str
    canvas_id: str
    reading_id: str
    char_start: int
    char_end: int
    exact_text: str
    bbox_pdf: tuple[float, float, float, float] | None
    surface_digest: str
    created_at: str

    def __post_init__(self) -> None:
        _require_text(locus_id=self.locus_id, room_id=self.room_id,
                      acquisition_id=self.acquisition_id, canvas_id=self.canvas_id,
                      reading_id=self.reading_id, surface_digest=self.surface_digest,
                      created_at=self.created_at)
        if isinstance(self.char_start, bool) or not isinstance(self.char_start, int) or self.char_start < 0:
            raise ValueError("char_start must be a non-negative integer")
        if isinstance(self.char_end, bool) or not isinstance(self.char_end, int) or self.char_end < self.char_start:
            raise ValueError("char_end must be an integer >= char_start")
        if not isinstance(self.exact_text, str):
            raise ValueError("exact_text must be a string")
        if self.bbox_pdf is not None:
            if not isinstance(self.bbox_pdf, tuple) or len(self.bbox_pdf) != 4:
                raise ValueError("bbox_pdf must be a four-number tuple or null")
            if any(not isinstance(value, (int, float)) for value in self.bbox_pdf):
                raise ValueError("bbox_pdf must contain numbers")


@dataclass(frozen=True, slots=True)
class BookModelItem:
    item_id: str
    room_id: str
    kind: str
    label: str
    body: str
    locus_refs: tuple[str, ...]
    book_cut_id: str
    projection_kind: str
    created_at: str
    supersedes_item_id: str | None = None

    def __post_init__(self) -> None:
        _require_text(item_id=self.item_id, room_id=self.room_id, kind=self.kind,
                      label=self.label, body=self.body, book_cut_id=self.book_cut_id,
                      created_at=self.created_at)
        _require_unique_refs("locus_refs", self.locus_refs)
        if not self.locus_refs:
            raise ValueError("locus_refs must not be empty")
        if self.projection_kind not in PROJECTION_KINDS:
            raise ValueError("projection_kind outside Book Room projection grammar")
        if self.supersedes_item_id is not None:
            _require_text(supersedes_item_id=self.supersedes_item_id)


@dataclass(frozen=True, slots=True)
class ResearchAssertion:
    assertion_id: str
    room_id: str
    question_id: str
    text: str
    book_cut_id: str
    basis_refs: tuple[str, ...]
    discovery_refs: tuple[str, ...]
    lifecycle: str
    created_at: str
    supersedes_assertion_id: str | None = None

    def __post_init__(self) -> None:
        _require_text(assertion_id=self.assertion_id, room_id=self.room_id,
                      question_id=self.question_id, text=self.text,
                      book_cut_id=self.book_cut_id, created_at=self.created_at)
        _require_unique_refs("basis_refs", self.basis_refs)
        _require_unique_refs("discovery_refs", self.discovery_refs)
        if self.lifecycle not in RESEARCH_LIFECYCLES:
            raise ValueError("research lifecycle must be PROPOSED or RETIRED")
        if self.supersedes_assertion_id is not None:
            _require_text(supersedes_assertion_id=self.supersedes_assertion_id)


@dataclass(frozen=True, slots=True)
class ResearchPressure:
    pressure_id: str
    room_id: str
    assertion_id: str
    kind: str
    basis_refs: tuple[str, ...]
    note: str
    book_cut_id: str
    created_at: str

    def __post_init__(self) -> None:
        _require_text(pressure_id=self.pressure_id, room_id=self.room_id,
                      assertion_id=self.assertion_id, kind=self.kind,
                      note=self.note, book_cut_id=self.book_cut_id,
                      created_at=self.created_at)
        _require_unique_refs("basis_refs", self.basis_refs)


@dataclass(frozen=True, slots=True)
class BookCut:
    book_cut_id: str
    room_id: str
    acquisition_id: str
    max_sequence: int
    created_at: str

    def __post_init__(self) -> None:
        _require_text(book_cut_id=self.book_cut_id, room_id=self.room_id,
                      acquisition_id=self.acquisition_id, created_at=self.created_at)
        if isinstance(self.max_sequence, bool) or not isinstance(self.max_sequence, int) or self.max_sequence < 0:
            raise ValueError("max_sequence must be a non-negative integer")


@dataclass(frozen=True, slots=True)
class ContextPack:
    pack_id: str
    room_id: str
    question_id: str
    book_cut_id: str
    query: str
    record_refs: tuple[str, ...]
    omitted_refs: tuple[str, ...]
    source_refs: tuple[str, ...]
    residual_fog: tuple[str, ...]
    pack_digest: str

    def __post_init__(self) -> None:
        _require_text(pack_id=self.pack_id, room_id=self.room_id,
                      question_id=self.question_id, book_cut_id=self.book_cut_id,
                      query=self.query, pack_digest=self.pack_digest)
        for name in ("record_refs", "omitted_refs", "source_refs", "residual_fog"):
            _require_unique_refs(name, getattr(self, name))


@dataclass(frozen=True, slots=True)
class DossierReceipt:
    dossier_id: str
    room_id: str
    question_id: str
    book_cut_id: str
    acquisition_id: str
    acquisition_object_digest: str
    required_object_digests: tuple[str, ...]
    book_model_item_ids: tuple[str, ...]
    research_assertion_ids: tuple[str, ...]
    evaluation_receipt_ids: tuple[str, ...]
    source_locus_refs: tuple[str, ...]
    residual_fog: tuple[str, ...]
    created_at: str
    dossier_digest: str

    def __post_init__(self) -> None:
        _require_text(dossier_id=self.dossier_id, room_id=self.room_id,
                      question_id=self.question_id, book_cut_id=self.book_cut_id,
                      acquisition_id=self.acquisition_id,
                      acquisition_object_digest=self.acquisition_object_digest,
                      created_at=self.created_at, dossier_digest=self.dossier_digest)
        for name in ("required_object_digests", "book_model_item_ids",
                     "research_assertion_ids", "evaluation_receipt_ids",
                     "source_locus_refs", "residual_fog"):
            _require_unique_refs(name, getattr(self, name))
