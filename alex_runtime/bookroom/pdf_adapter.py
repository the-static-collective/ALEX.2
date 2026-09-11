from __future__ import annotations

from io import BytesIO
from pathlib import Path

import pypdfium2 as pdfium

from .records import AcquisitionRecord, BookRoomIdentity, CanvasRecord, ReadingRecord
from .store import BookRoomStore

PDFIUM_VERSION = "5.13.0"


class PdfIngestError(RuntimeError):
    pass


def _render_png_bytes(page) -> bytes:
    bitmap = page.render(scale=96 / 72, rotation=0)
    try:
        image = bitmap.to_pil()
        if image.mode not in {"RGB", "RGBA"}:
            image = image.convert("RGB")
        buffer = BytesIO()
        image.save(buffer, format="PNG", compress_level=9, optimize=False)
        return buffer.getvalue()
    finally:
        close = getattr(bitmap, "close", None)
        if callable(close):
            close()


def ingest_pdf(
    store: BookRoomStore,
    pdf_path: Path,
    *,
    room_id: str,
    work_ref: str,
    carrier_ref: str,
    acquisition_id: str,
    source_locator: str,
    acquired_at: str,
    rights_status: str,
    egress_policy_ref: str,
) -> BookRoomIdentity:
    path = Path(pdf_path)
    if not path.is_file():
        raise PdfIngestError(f"PDF path is not a readable file: {path}")

    raw_bytes = path.read_bytes()
    object_digest = store.put_object(raw_bytes)
    cas_path = store.object_path(object_digest)

    try:
        document = pdfium.PdfDocument(str(cas_path))
    except Exception as exc:
        raise PdfIngestError(f"PDF cannot be opened without additional credentials: {path}") from exc

    try:
        page_count = len(document)
        acquisition = AcquisitionRecord(
            acquisition_id=acquisition_id,
            room_id=room_id,
            work_ref=work_ref,
            carrier_ref=carrier_ref,
            object_digest=object_digest,
            source_locator=source_locator,
            acquired_at=acquired_at,
            rights_status=rights_status,
            egress_policy_ref=egress_policy_ref,
        )
        store.append_acquisition(acquisition)

        for index in range(page_count):
            page = document[index]
            try:
                width_pt, height_pt = page.get_size()
                surface_digest = store.put_object(_render_png_bytes(page))
                canvas_id = f"{acquisition_id}:canvas:{index:06d}"
                store.append_canvas(
                    CanvasRecord(
                        canvas_id=canvas_id,
                        room_id=room_id,
                        acquisition_id=acquisition_id,
                        sequence=index,
                        printed_label=None,
                        width_pt=float(width_pt),
                        height_pt=float(height_pt),
                        surface_digest=surface_digest,
                        created_at=acquired_at,
                    )
                )

                textpage = page.get_textpage()
                try:
                    text = textpage.get_text_bounded().replace("\r\n", "\n")
                finally:
                    close_textpage = getattr(textpage, "close", None)
                    if callable(close_textpage):
                        close_textpage()

                reading_id = f"{acquisition_id}:reading:{index:06d}:pdf_text_layer"
                store.append_reading(
                    ReadingRecord(
                        reading_id=reading_id,
                        room_id=room_id,
                        acquisition_id=acquisition_id,
                        canvas_id=canvas_id,
                        parent_reading_id=None,
                        method="pdf_text_layer",
                        producer="pypdfium2",
                        producer_version=PDFIUM_VERSION,
                        status="OBSERVED" if text.strip() else "FOG",
                        text=text,
                        created_at=acquired_at,
                    )
                )
            finally:
                close_page = getattr(page, "close", None)
                if callable(close_page):
                    close_page()

        return BookRoomIdentity(
            room_id=room_id,
            work_ref=work_ref,
            carrier_ref=carrier_ref,
            acquisition_id=acquisition_id,
            object_digest=object_digest,
            page_count=page_count,
            created_at=acquired_at,
        )
    finally:
        close_document = getattr(document, "close", None)
        if callable(close_document):
            close_document()
