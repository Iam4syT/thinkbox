/**
 * @module LearningRepository
 * @description Repository for audience profiles, patterns, and evolution snapshots.
 * Supports the learning engine's data persistence needs.
 */
import { getDatabase } from '../database.js';
import { v4 as uuidv4 } from 'uuid';

export class LearningRepository {
  /** @returns {import('better-sqlite3').Database} */
  get db() {
    return getDatabase();
  }

  // ─── Audience Profiles ────────────────────────────────────

  /**
   * Get or create an audience profile for a platform.
   * @param {string} platform
   * @returns {Object}
   */
  getAudienceProfile(platform) {
    let row = this.db
      .prepare('SELECT * FROM audience_profile WHERE platform = ?')
      .get(platform);

    if (!row) {
      this.db
        .prepare('INSERT INTO audience_profile (id, platform) VALUES (?, ?)')
        .run(uuidv4(), platform);
      row = this.db
        .prepare('SELECT * FROM audience_profile WHERE platform = ?')
        .get(platform);
    }

    return this._deserializeProfile(row);
  }

  /**
   * Update audience profile data.
   * @param {string} platform
   * @param {Object} profileData
   * @param {Object} [engagementPatterns]
   * @returns {Object}
   */
  updateAudienceProfile(platform, profileData, engagementPatterns) {
    const params = { platform };
    const sets = ["updated_at = datetime('now')"];

    if (profileData !== undefined) {
      sets.push('profile_data = @profile_data');
      params.profile_data = JSON.stringify(profileData);
    }
    if (engagementPatterns !== undefined) {
      sets.push('engagement_patterns = @engagement_patterns');
      params.engagement_patterns = JSON.stringify(engagementPatterns);
    }

    this.db
      .prepare(`UPDATE audience_profile SET ${sets.join(', ')} WHERE platform = @platform`)
      .run(params);

    return this.getAudienceProfile(platform);
  }

  /**
   * Get all audience profiles.
   * @returns {Object[]}
   */
  getAllAudienceProfiles() {
    return this.db
      .prepare('SELECT * FROM audience_profile')
      .all()
      .map(this._deserializeProfile);
  }

  // ─── Patterns ─────────────────────────────────────────────

  /**
   * Upsert a detected pattern.
   * @param {Object} data
   * @returns {Object}
   */
  upsertPattern(data) {
    const existing = this.db
      .prepare('SELECT * FROM patterns WHERE platform = ? AND pattern_type = ?')
      .get(data.platform, data.pattern_type);

    if (existing) {
      this.db
        .prepare(`
          UPDATE patterns
          SET pattern_data = ?, confidence = ?, sample_count = ?, updated_at = datetime('now')
          WHERE id = ?
        `)
        .run(
          JSON.stringify(data.pattern_data || {}),
          data.confidence || 0,
          data.sample_count || 0,
          existing.id
        );
      return this.getPatternById(existing.id);
    }

    this.db
      .prepare(`
        INSERT INTO patterns (id, platform, pattern_type, pattern_data, confidence, sample_count)
        VALUES (?, ?, ?, ?, ?, ?)
      `)
      .run(
        data.id,
        data.platform,
        data.pattern_type,
        JSON.stringify(data.pattern_data || {}),
        data.confidence || 0,
        data.sample_count || 0
      );

    return this.getPatternById(data.id);
  }

  /**
   * Get a pattern by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getPatternById(id) {
    const row = this.db.prepare('SELECT * FROM patterns WHERE id = ?').get(id);
    return row ? this._deserializePattern(row) : undefined;
  }

  /**
   * Get patterns for a platform.
   * @param {string} platform
   * @param {string} [patternType]
   * @returns {Object[]}
   */
  getPatternsByPlatform(platform, patternType) {
    let sql = 'SELECT * FROM patterns WHERE platform = ?';
    const params = [platform];

    if (patternType) {
      sql += ' AND pattern_type = ?';
      params.push(patternType);
    }

    sql += ' ORDER BY confidence DESC';
    return this.db.prepare(sql).all(...params).map(this._deserializePattern);
  }

  // ─── Evolution Snapshots ──────────────────────────────────

  /**
   * Create an evolution snapshot.
   * @param {Object} data
   * @returns {Object}
   */
  createSnapshot(data) {
    this.db
      .prepare(`
        INSERT INTO evolution_snapshots (id, snapshot_type, period_start, period_end, metrics_data, insights, comparison_data)
        VALUES (?, ?, ?, ?, ?, ?, ?)
      `)
      .run(
        data.id,
        data.snapshot_type,
        data.period_start,
        data.period_end,
        JSON.stringify(data.metrics_data || {}),
        JSON.stringify(data.insights || []),
        JSON.stringify(data.comparison_data || {})
      );

    return this.getSnapshotById(data.id);
  }

  /**
   * Get a snapshot by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getSnapshotById(id) {
    const row = this.db
      .prepare('SELECT * FROM evolution_snapshots WHERE id = ?')
      .get(id);
    return row ? this._deserializeSnapshot(row) : undefined;
  }

  /**
   * Get snapshots by type, ordered by period.
   * @param {string} snapshotType
   * @param {number} [limit=10]
   * @returns {Object[]}
   */
  getSnapshotsByType(snapshotType, limit = 10) {
    return this.db
      .prepare(
        'SELECT * FROM evolution_snapshots WHERE snapshot_type = ? ORDER BY period_end DESC LIMIT ?'
      )
      .all(snapshotType, limit)
      .map(this._deserializeSnapshot);
  }

  /**
   * Get the latest snapshot of a given type.
   * @param {string} snapshotType
   * @returns {Object|undefined}
   */
  getLatestSnapshot(snapshotType) {
    const row = this.db
      .prepare(
        'SELECT * FROM evolution_snapshots WHERE snapshot_type = ? ORDER BY period_end DESC LIMIT 1'
      )
      .get(snapshotType);
    return row ? this._deserializeSnapshot(row) : undefined;
  }

  // ─── Private Helpers ──────────────────────────────────────

  /** @private */
  _deserializeProfile(row) {
    if (!row) return row;
    return {
      ...row,
      profile_data: JSON.parse(row.profile_data || '{}'),
      engagement_patterns: JSON.parse(row.engagement_patterns || '{}'),
    };
  }

  /** @private */
  _deserializePattern(row) {
    if (!row) return row;
    return {
      ...row,
      pattern_data: JSON.parse(row.pattern_data || '{}'),
    };
  }

  /** @private */
  _deserializeSnapshot(row) {
    if (!row) return row;
    return {
      ...row,
      metrics_data: JSON.parse(row.metrics_data || '{}'),
      insights: JSON.parse(row.insights || '[]'),
      comparison_data: JSON.parse(row.comparison_data || '{}'),
    };
  }
}

export default new LearningRepository();
