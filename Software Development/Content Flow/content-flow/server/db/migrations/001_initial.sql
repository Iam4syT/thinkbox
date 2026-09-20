-- ContentFlow — Initial Schema Migration (fully reconciled with all repositories)
-- 001_initial.sql

-- Source content
CREATE TABLE IF NOT EXISTS content (
    id               TEXT PRIMARY KEY,
    title            TEXT,
    raw_content      TEXT NOT NULL,
    refined_content  TEXT,
    content_type     TEXT DEFAULT 'brain_dump',
    tags             TEXT DEFAULT '[]',
    metadata         TEXT DEFAULT '{}',
    status           TEXT DEFAULT 'draft',
    created_at       DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at       DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- AI-adapted content per platform
CREATE TABLE IF NOT EXISTS adapted_content (
    id               TEXT PRIMARY KEY,
    content_id       TEXT NOT NULL REFERENCES content(id) ON DELETE CASCADE,
    platform         TEXT NOT NULL,
    adapted_text     TEXT NOT NULL,
    metadata         TEXT DEFAULT '{}',
    engagement_score REAL DEFAULT 0,
    status           TEXT DEFAULT 'draft',
    version          INTEGER DEFAULT 1,
    created_at       DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at       DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- User feedback
CREATE TABLE IF NOT EXISTS feedback (
    id                  TEXT PRIMARY KEY,
    adapted_content_id  TEXT NOT NULL REFERENCES adapted_content(id) ON DELETE CASCADE,
    feedback_type       TEXT NOT NULL,
    original_text       TEXT,
    edited_text         TEXT,
    rating              INTEGER,
    comments            TEXT,
    diff_data           TEXT DEFAULT '{}',
    metadata            TEXT DEFAULT '{}',
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Content journeys
CREATE TABLE IF NOT EXISTS journeys (
    id            TEXT PRIMARY KEY,
    title         TEXT NOT NULL,
    description   TEXT,
    platform      TEXT,
    content_ids   TEXT DEFAULT '[]',
    status        TEXT DEFAULT 'planning',
    sequence_data TEXT DEFAULT '{}',
    metadata      TEXT DEFAULT '{}',
    created_at    DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at    DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Post queue
CREATE TABLE IF NOT EXISTS queue (
    id                  TEXT PRIMARY KEY,
    adapted_content_id  TEXT NOT NULL REFERENCES adapted_content(id) ON DELETE CASCADE,
    platform            TEXT NOT NULL,
    scheduled_time      DATETIME,
    priority            INTEGER DEFAULT 0,
    status              TEXT DEFAULT 'pending',
    metadata            TEXT DEFAULT '{}',
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Post performance metrics
CREATE TABLE IF NOT EXISTS post_metrics (
    id                  TEXT PRIMARY KEY,
    adapted_content_id  TEXT NOT NULL REFERENCES adapted_content(id) ON DELETE CASCADE,
    platform            TEXT NOT NULL,
    impressions         INTEGER DEFAULT 0,
    clicks              INTEGER DEFAULT 0,
    likes               INTEGER DEFAULT 0,
    comments            INTEGER DEFAULT 0,
    shares              INTEGER DEFAULT 0,
    saves               INTEGER DEFAULT 0,
    engagement_rate     REAL DEFAULT 0,
    reach               INTEGER DEFAULT 0,
    metadata            TEXT DEFAULT '{}',
    recorded_at         DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- OKR: Objectives
CREATE TABLE IF NOT EXISTS objectives (
    id          TEXT PRIMARY KEY,
    title       TEXT NOT NULL,
    description TEXT,
    target_date DATE,
    status      TEXT DEFAULT 'active',
    progress    REAL DEFAULT 0,
    metadata    TEXT DEFAULT '{}',
    created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- OKR: Key Results
CREATE TABLE IF NOT EXISTS key_results (
    id             TEXT PRIMARY KEY,
    objective_id   TEXT NOT NULL REFERENCES objectives(id) ON DELETE CASCADE,
    title          TEXT NOT NULL,
    metric_type    TEXT NOT NULL,
    current_value  REAL DEFAULT 0,
    target_value   REAL NOT NULL,
    unit           TEXT DEFAULT '',
    status         TEXT DEFAULT 'active',
    metadata       TEXT DEFAULT '{}',
    created_at     DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at     DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Audience profile (learned, per platform)
CREATE TABLE IF NOT EXISTS audience_profile (
    id                  TEXT PRIMARY KEY,
    platform            TEXT NOT NULL UNIQUE,
    profile_data        TEXT DEFAULT '{}',
    engagement_patterns TEXT DEFAULT '{}',
    confidence_score    REAL DEFAULT 0,
    sample_size         INTEGER DEFAULT 0,
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Detected engagement patterns
CREATE TABLE IF NOT EXISTS patterns (
    id              TEXT PRIMARY KEY,
    platform        TEXT,
    pattern_type    TEXT NOT NULL,
    pattern_data    TEXT DEFAULT '{}',
    confidence      REAL DEFAULT 0,
    sample_count    INTEGER DEFAULT 0,
    created_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at      DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Evolution snapshots (weekly quality tracking)
CREATE TABLE IF NOT EXISTS evolution_snapshots (
    id               TEXT PRIMARY KEY,
    snapshot_type    TEXT NOT NULL,
    period_start     DATETIME NOT NULL,
    period_end       DATETIME NOT NULL,
    metrics_data     TEXT DEFAULT '{}',
    insights         TEXT DEFAULT '[]',
    comparison_data  TEXT DEFAULT '{}',
    created_at       DATETIME DEFAULT CURRENT_TIMESTAMP
);
