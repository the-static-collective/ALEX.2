from __future__ import annotations

import hashlib
import json
import os
import sqlite3
import tempfile
from dataclasses import asdict
from pathlib import Path
from typing import TypeVar

from .records import AcquisitionRecord, CanvasRecord, ReadingRecord, SourceLocusRecord


class BookRoomStoreError(RuntimeError):
    pass


class RecordConflict(BookRoomStoreError):
    pass


class RecordNotFound(BookRoomStoreError):
    pass


class ReferenceMismatch(BookRoomStoreError):
    pass


T = TypeVar("T")


def _canonical_record_json(record: object) -> str:
    return json.dumps(asdict(record), sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _decode(record_type: type[T], payload: str) -> T:
    data = json.loads(payload)
    if record_type is SourceLocusRecord and data.get("bbox_pdf") is not None:
        data["bbox_pdf"] = tuple(data["bbox_pdf"])
    return record_type(**data)


class BookRoomStore:
    def __init__(self, root: Path, connection: sqlite3.Connection):
        self.root = root
        self.connection = connection
        self.objects_root = root / "objects" / "sha256"

    @classmethod
    def open(cls, root: Path) -> "BookRoomStore":
        root = Path(root)
        root.mkdir(parents=True, exist_ok=True)
        objects_root = root / "objects" / "sha256"
        objects_root.mkdir(parents=True, exist_ok=True)
        connection = sqlite3.connect(root / "bookroom.sqlite3")
        connection.execute("PRAGMA foreign_keys = ON")
        schema = Path(__file__).with_name("schema.sql").read_text(encoding="utf-8")
        connection.executescript(schema)
        connection.commit()
        return cls(root, connection)

    def close(self) -> None:
        self.connection.close()

    @staticmethod
    def _digest_bytes(data: bytes) -> str:
        return "sha256:" + hashlib.sha256(data).hexdigest()

    def object_path(self, digest: str) -> Path:
        if not isinstance(digest, str) or not digest.startswith("sha256:"):
            raise ValueError("digest must use sha256:<hex>")
        hex_digest = digest.removeprefix("sha256:")
        if len(hex_digest) != 64 or any(ch not in "0123456789abcdef" for ch in hex_digest):
            raise ValueError("digest must contain 64 lowercase hex characters")
        return self.objects_root / hex_digest

    def put_object(self, data: bytes) -> str:
        if not isinstance(data, bytes):
            raise TypeError("CAS objects must be bytes")
        digest = self._digest_bytes(data)
        target = self.object_path(digest)
        if target.exists():
            return digest

        fd, temp_name = tempfile.mkstemp(prefix=".cas-", dir=self.objects_root)
        temp_path = Path(temp_name)
        try:
            with os.fdopen(fd, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            if target.exists():
                temp_path.unlink(missing_ok=True)
            else:
                os.replace(temp_path, target)
        finally:
            temp_path.unlink(missing_ok=True)
        return digest

    def get_object(self, digest: str) -> bytes:
        path = self.object_path(digest)
        if not path.exists():
            raise RecordNotFound(f"CAS object not found: {digest}")
        data = path.read_bytes()
        if self._digest_bytes(data) != digest:
            raise BookRoomStoreError(f"CAS digest mismatch: {digest}")
        return data

    def _append_record(
        self,
        *,
        table: str,
        id_column: str,
        record_id: str,
        record: object,
        columns: dict[str, object],
    ) -> bool:
        payload = _canonical_record_json(record)
        existing = self.connection.execute(
            f"SELECT record_json FROM {table} WHERE {id_column} = ?", (record_id,)
        ).fetchone()
        if existing is not None:
            if existing[0] != payload:
                raise RecordConflict(f"{table}:{record_id} already exists with different payload")
            return False

        all_columns = {id_column: record_id, **columns, "record_json": payload}
        names = ", ".join(all_columns)
        placeholders = ", ".join("?" for _ in all_columns)
        self.connection.execute(
            f"INSERT INTO {table} ({names}) VALUES ({placeholders})",
            tuple(all_columns.values()),
        )
        self.connection.commit()
        return True

    def _get_record(self, table: str, id_column: str, record_id: str, record_type: type[T]) -> T:
        row = self.connection.execute(
            f"SELECT record_json FROM {table} WHERE {id_column} = ?", (record_id,)
        ).fetchone()
        if row is None:
            raise RecordNotFound(f"{table}:{record_id} not found")
        return _decode(record_type, row[0])

    def append_acquisition(self, record: AcquisitionRecord) -> AcquisitionRecord:
        self.get_object(record.object_digest)
        self._append_record(
            table="acquisitions",
            id_column="acquisition_id",
            record_id=record.acquisition_id,
            record=record,
            columns={
                "room_id": record.room_id,
                "carrier_ref": record.carrier_ref,
                "object_digest": record.object_digest,
                "source_locator": record.source_locator,
                "acquired_at": record.acquired_at,
                "rights_status": record.rights_status,
                "egress_policy_ref": record.egress_policy_ref,
            },
        )
        return record

    def get_acquisition(self, acquisition_id: str) -> AcquisitionRecord:
        return self._get_record("acquisitions", "acquisition_id", acquisition_id, AcquisitionRecord)

    def append_canvas(self, record: CanvasRecord) -> CanvasRecord:
        acquisition = self.get_acquisition(record.acquisition_id)
        if acquisition.room_id != record.room_id:
            raise ReferenceMismatch("canvas room does not match acquisition room")
        self.get_object(record.surface_digest)
        self._append_record(
            table="canvases",
            id_column="canvas_id",
            record_id=record.canvas_id,
            record=record,
            columns={
                "acquisition_id": record.acquisition_id,
                "sequence": record.sequence,
                "printed_label": record.printed_label,
                "width_pt": record.width_pt,
                "height_pt": record.height_pt,
                "surface_digest": record.surface_digest,
            },
        )
        return record

    def get_canvas(self, canvas_id: str) -> CanvasRecord:
        return self._get_record("canvases", "canvas_id", canvas_id, CanvasRecord)

    def list_canvases(self, acquisition_id: str) -> list[CanvasRecord]:
        self.get_acquisition(acquisition_id)
        rows = self.connection.execute(
            "SELECT record_json FROM canvases WHERE acquisition_id = ? ORDER BY sequence, canvas_id",
            (acquisition_id,),
        ).fetchall()
        return [_decode(CanvasRecord, row[0]) for row in rows]

    def append_reading(self, record: ReadingRecord) -> ReadingRecord:
        canvas = self.get_canvas(record.canvas_id)
        if canvas.room_id != record.room_id or canvas.acquisition_id != record.acquisition_id:
            raise ReferenceMismatch("reading does not belong to the declared canvas/acquisition")
        if record.parent_reading_id is not None:
            parent = self.get_reading(record.parent_reading_id)
            if parent.canvas_id != record.canvas_id or parent.acquisition_id != record.acquisition_id:
                raise ReferenceMismatch("reading parent belongs to another source occurrence")
        inserted = self._append_record(
            table="readings",
            id_column="reading_id",
            record_id=record.reading_id,
            record=record,
            columns={
                "canvas_id": record.canvas_id,
                "parent_reading_id": record.parent_reading_id,
                "method": record.method,
                "producer": record.producer,
                "producer_version": record.producer_version,
                "status": record.status,
                "text": record.text,
            },
        )
        if inserted:
            self.connection.execute(
                "INSERT INTO reading_fts (reading_id, text) VALUES (?, ?)",
                (record.reading_id, record.text),
            )
            self.connection.commit()
        return record

    def get_reading(self, reading_id: str) -> ReadingRecord:
        return self._get_record("readings", "reading_id", reading_id, ReadingRecord)

    def list_readings(self, acquisition_id: str) -> list[ReadingRecord]:
        self.get_acquisition(acquisition_id)
        rows = self.connection.execute(
            """
            SELECT r.record_json
            FROM readings AS r
            JOIN canvases AS c ON c.canvas_id = r.canvas_id
            WHERE c.acquisition_id = ?
            ORDER BY c.sequence, r.reading_id
            """,
            (acquisition_id,),
        ).fetchall()
        return [_decode(ReadingRecord, row[0]) for row in rows]

    def search_readings(self, query: str) -> list[ReadingRecord]:
        rows = self.connection.execute(
            "SELECT reading_id FROM reading_fts WHERE reading_fts MATCH ? ORDER BY rank, reading_id",
            (query,),
        ).fetchall()
        return [self.get_reading(row[0]) for row in rows]

    def append_source_locus(self, record: SourceLocusRecord) -> SourceLocusRecord:
        acquisition = self.get_acquisition(record.acquisition_id)
        canvas = self.get_canvas(record.canvas_id)
        reading = self.get_reading(record.reading_id)
        if not (
            acquisition.room_id == record.room_id
            and canvas.room_id == record.room_id
            and reading.room_id == record.room_id
            and canvas.acquisition_id == record.acquisition_id
            and reading.acquisition_id == record.acquisition_id
            and reading.canvas_id == record.canvas_id
        ):
            raise ReferenceMismatch("source locus crosses room/acquisition/canvas ancestry")
        if record.surface_digest != canvas.surface_digest:
            raise ReferenceMismatch("source locus surface does not match canvas surface")
        if record.char_end > len(reading.text) or reading.text[record.char_start:record.char_end] != record.exact_text:
            raise ReferenceMismatch("source locus text does not match reading span")
        self._append_record(
            table="source_loci",
            id_column="locus_id",
            record_id=record.locus_id,
            record=record,
            columns={
                "acquisition_id": record.acquisition_id,
                "canvas_id": record.canvas_id,
                "reading_id": record.reading_id,
                "char_start": record.char_start,
                "char_end": record.char_end,
                "exact_text": record.exact_text,
                "surface_digest": record.surface_digest,
            },
        )
        return record

    def get_source_locus(self, locus_id: str) -> SourceLocusRecord:
        return self._get_record("source_loci", "locus_id", locus_id, SourceLocusRecord)
