PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS acquisitions (
    acquisition_id TEXT PRIMARY KEY,
    room_id TEXT NOT NULL,
    carrier_ref TEXT NOT NULL,
    object_digest TEXT NOT NULL,
    source_locator TEXT NOT NULL,
    acquired_at TEXT NOT NULL,
    rights_status TEXT NOT NULL,
    egress_policy_ref TEXT NOT NULL,
    record_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS canvases (
    canvas_id TEXT PRIMARY KEY,
    acquisition_id TEXT NOT NULL,
    sequence INTEGER NOT NULL,
    printed_label TEXT,
    width_pt REAL NOT NULL,
    height_pt REAL NOT NULL,
    surface_digest TEXT NOT NULL,
    record_json TEXT NOT NULL,
    FOREIGN KEY(acquisition_id) REFERENCES acquisitions(acquisition_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS canvases_acquisition_sequence
ON canvases(acquisition_id, sequence);

CREATE TABLE IF NOT EXISTS readings (
    reading_id TEXT PRIMARY KEY,
    canvas_id TEXT NOT NULL,
    parent_reading_id TEXT,
    method TEXT NOT NULL,
    producer TEXT NOT NULL,
    producer_version TEXT NOT NULL,
    status TEXT NOT NULL,
    text TEXT NOT NULL,
    record_json TEXT NOT NULL,
    FOREIGN KEY(canvas_id) REFERENCES canvases(canvas_id),
    FOREIGN KEY(parent_reading_id) REFERENCES readings(reading_id)
);

CREATE VIRTUAL TABLE IF NOT EXISTS reading_fts USING fts5(
    reading_id UNINDEXED,
    text
);

CREATE TABLE IF NOT EXISTS source_loci (
    locus_id TEXT PRIMARY KEY,
    acquisition_id TEXT NOT NULL,
    canvas_id TEXT NOT NULL,
    reading_id TEXT NOT NULL,
    char_start INTEGER NOT NULL,
    char_end INTEGER NOT NULL,
    exact_text TEXT NOT NULL,
    surface_digest TEXT NOT NULL,
    record_json TEXT NOT NULL,
    FOREIGN KEY(acquisition_id) REFERENCES acquisitions(acquisition_id),
    FOREIGN KEY(canvas_id) REFERENCES canvases(canvas_id),
    FOREIGN KEY(reading_id) REFERENCES readings(reading_id)
);

CREATE TABLE IF NOT EXISTS book_items (
    item_id TEXT PRIMARY KEY,
    room_id TEXT NOT NULL,
    kind TEXT NOT NULL,
    book_cut_id TEXT NOT NULL,
    record_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS research_assertions (
    assertion_id TEXT PRIMARY KEY,
    room_id TEXT NOT NULL,
    question_id TEXT NOT NULL,
    book_cut_id TEXT NOT NULL,
    lifecycle TEXT NOT NULL,
    record_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS research_pressures (
    pressure_id TEXT PRIMARY KEY,
    assertion_id TEXT NOT NULL,
    kind TEXT NOT NULL,
    record_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS book_cuts (
    book_cut_id TEXT PRIMARY KEY,
    room_id TEXT NOT NULL,
    acquisition_id TEXT NOT NULL,
    max_sequence INTEGER NOT NULL,
    record_json TEXT NOT NULL
);
