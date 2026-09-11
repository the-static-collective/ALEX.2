from __future__ import annotations

from .records import BookModelItem
from .store import BookRoomStore, RecordNotFound


class BookModelError(RuntimeError):
    pass


class MissingSourceLocus(BookModelError):
    pass


class SourceJurisdictionMismatch(BookModelError):
    pass


def _resolve_loci(store: BookRoomStore, item: BookModelItem):
    loci = []
    for locus_ref in item.locus_refs:
        try:
            locus = store.get_source_locus(locus_ref)
        except RecordNotFound as exc:
            raise MissingSourceLocus(f"{item.item_id} requires source locus {locus_ref}") from exc
        loci.append(locus)

    if not loci:
        raise MissingSourceLocus(f"{item.item_id} has no attributable source loci")
    if any(locus.room_id != item.room_id for locus in loci):
        raise SourceJurisdictionMismatch(f"{item.item_id} crosses Book Room jurisdiction")
    acquisition_ids = {locus.acquisition_id for locus in loci}
    if len(acquisition_ids) != 1:
        raise SourceJurisdictionMismatch(f"{item.item_id} crosses carrier/acquisition jurisdiction")
    return tuple(loci)


def propose_book_item(store: BookRoomStore, item: BookModelItem) -> BookModelItem:
    _resolve_loci(store, item)
    if item.supersedes_item_id is not None:
        try:
            parent = store.get_book_item(item.supersedes_item_id)
        except RecordNotFound as exc:
            raise MissingSourceLocus(
                f"{item.item_id} names missing superseded Book Model item {item.supersedes_item_id}"
            ) from exc
        if parent.room_id != item.room_id:
            raise SourceJurisdictionMismatch("Book Model correction crosses room jurisdiction")
    return store.append_book_item(item)


def book_item_source_chain(store: BookRoomStore, item_id: str) -> dict:
    item = store.get_book_item(item_id)
    loci = _resolve_loci(store, item)
    return {
        "item": item,
        "loci": loci,
        "acquisition_ids": tuple(dict.fromkeys(locus.acquisition_id for locus in loci)),
    }
