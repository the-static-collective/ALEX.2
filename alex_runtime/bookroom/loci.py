from __future__ import annotations

from .records import SourceLocusRecord
from .store import BookRoomStore, ReferenceMismatch


class InvalidLocus(ValueError):
    pass


class LocusMismatch(ValueError):
    pass


def create_text_locus(
    store: BookRoomStore,
    *,
    locus_id: str,
    reading_id: str,
    char_start: int,
    char_end: int,
    created_at: str,
    exact_text: str | None = None,
    bbox_pdf: tuple[float, float, float, float] | None = None,
) -> SourceLocusRecord:
    reading = store.get_reading(reading_id)
    if (
        isinstance(char_start, bool)
        or isinstance(char_end, bool)
        or not isinstance(char_start, int)
        or not isinstance(char_end, int)
        or char_start < 0
        or char_end <= char_start
        or char_end > len(reading.text)
    ):
        raise InvalidLocus("locus span must be a non-empty slice inside the reading")

    observed = reading.text[char_start:char_end]
    if exact_text is not None and exact_text != observed:
        raise LocusMismatch("declared exact text does not match reading span")

    canvas = store.get_canvas(reading.canvas_id)
    acquisition = store.get_acquisition(reading.acquisition_id)
    if canvas.acquisition_id != acquisition.acquisition_id or canvas.room_id != reading.room_id:
        raise ReferenceMismatch("reading ancestry does not resolve to one canvas/acquisition")

    locus = SourceLocusRecord(
        locus_id=locus_id,
        room_id=reading.room_id,
        acquisition_id=acquisition.acquisition_id,
        canvas_id=canvas.canvas_id,
        reading_id=reading.reading_id,
        char_start=char_start,
        char_end=char_end,
        exact_text=observed,
        bbox_pdf=bbox_pdf,
        surface_digest=canvas.surface_digest,
        created_at=created_at,
    )
    return store.append_source_locus(locus)


def resolve_quote(store: BookRoomStore, locus_id: str) -> dict:
    locus = store.get_source_locus(locus_id)
    reading = store.get_reading(locus.reading_id)
    canvas = store.get_canvas(locus.canvas_id)
    acquisition = store.get_acquisition(locus.acquisition_id)

    observed = reading.text[locus.char_start:locus.char_end]
    if observed != locus.exact_text:
        raise LocusMismatch("stored locus no longer matches its reading span")
    if canvas.surface_digest != locus.surface_digest:
        raise LocusMismatch("stored locus no longer matches its page surface")
    if not (
        reading.canvas_id == canvas.canvas_id
        and reading.acquisition_id == acquisition.acquisition_id
        and canvas.acquisition_id == acquisition.acquisition_id
    ):
        raise ReferenceMismatch("stored locus ancestry is inconsistent")

    return {
        "locus_id": locus.locus_id,
        "room_id": locus.room_id,
        "acquisition_id": acquisition.acquisition_id,
        "canvas_id": canvas.canvas_id,
        "canvas_sequence": canvas.sequence,
        "printed_label": canvas.printed_label,
        "reading_id": reading.reading_id,
        "char_start": locus.char_start,
        "char_end": locus.char_end,
        "exact_text": locus.exact_text,
        "bbox_pdf": locus.bbox_pdf,
        "surface_digest": locus.surface_digest,
    }
