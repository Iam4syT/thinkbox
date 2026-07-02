/**
 * @module AnalyticsRepository
 * @description Repository for post metrics, adapted content queries, and analytics aggregation.
 */
import { getDatabase } from '../database.js';

export class AnalyticsRepository {
  /** @returns {import('better-sqlite3').Database} */
  get db() {
    return getDatabase();
  }

  // ─── Adapted Content ──────────────────────────────────────

  /**
   * Create an adapted content record.
   * @param {Object} data
   * @returns {Object}
   */
  createAdaptedContent(data) {
    this.db
      .prepare(`
        INSERT INTO adapted_content (id, content_id, platform, adapted_text, metadata, engagement_score, status, version)
        VALUES (@id, @content_id, @platform, @adapted_text, @metadata, @engagement_score, @status, @version)
      `)
      .run({
        id: data.id,
        content_id: data.content_id,
        platform: data.platform,
        adapted_text: data.adapted_text,
        metadata: JSON.stringify(data.metadata || {}),
        engagement_score: data.engagement_score || 0,
        status: data.status || 'draft',
        version: data.version || 1,
      });

    return this.getAdaptedContentById(data.id);
  }

  /**
   * Get adapted content by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getAdaptedContentById(id) {
    const row = this.db.prepare('SELECT * FROM adapted_content WHERE id = ?').get(id);
    return row ? this._deserializeAdapted(row) : undefined;
  }

  /**
   * Get all adaptations for a content piece.
   * @param {string} contentId
   * @returns {Object[]}
   */
  getAdaptationsByContentId(contentId) {
    return this.db
      .prepare('SELECT * FROM adapted_content WHERE content_id = ? ORDER BY created_at DESC')
      .all(contentId)
      .map(this._deserializeAdapted);
  }

  /**
   * Get adaptations by platform.
   * @param {string} platform
   * @param {number} [limit=50]
   * @returns {Object[]}
   */
  getAdaptationsByPlatform(platform, limit = 50) {
    return this.db
      .prepare('SELECT * FROM adapted_content WHERE platform = ? ORDER BY created_at DESC LIMIT ?')
      .all(platform, limit)
      .map(this._deserializeAdapted);
  }

  /**
   * Update adapted content.
   * @param {string} id
   * @param {Object} data
   * @returns {Object|undefined}
   */
  updateAdaptedContent(id, data) {
    const fields = [];
    const params = { id };

    for (const [key, value] of Object.entries(data)) {
      if (key === 'metadata') {
        fields.push('metadata = @metadata');
        params.metadata = JSON.stringify(value);
      } else {
        fields.push(`${key} = @${key}`);
        params[key] = value;
      }
    }

    if (fields.length === 0) return this.getAdaptedContentById(id);

    fields.push("updated_at = datetime('now')");

    this.db
      .prepare(`UPDATE adapted_content SET ${fields.join(', ')} WHERE id = @id`)
      .run(params);

    return this.getAdaptedContentById(id);
  }

  // ─── Post Metrics ─────────────────────────────────────────

  /**
   * Record metrics for a post.
   * @param {Object} data
   * @returns {Object}
   */
  recordMetrics(data) {
    this.db
      .prepare(`
        INSERT INTO post_metrics (id, adapted_content_id, platform, impressions, clicks, likes, comments, shares, saves, engagement_rate, reach, metadata)
        VALUES (@id, @adapted_content_id, @platform, @impressions, @clicks, @likes, @comments, @shares, @saves, @engagement_rate, @reach, @metadata)
      `)
      .run({
        id: data.id,
        adapted_content_id: data.adapted_content_id,
        platform: data.platform,
        impressions: data.impressions || 0,
        clicks: data.clicks || 0,
        likes: data.likes || 0,
        comments: data.comments || 0,
        shares: data.shares || 0,
        saves: data.saves || 0,
        engagement_rate: data.engagement_rate || 0,
        reach: data.reach || 0,
        metadata: JSON.stringify(data.metadata || {}),
      });

    return this.getMetricsById(data.id);
  }

  /**
   * Get metrics by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getMetricsById(id) {
    const row = this.db.prepare('SELECT * FROM post_metrics WHERE id = ?').get(id);
    return row ? this._deserializeMetrics(row) : undefined;
  }

  /**
   * Get all metrics for an adapted content piece.
   * @param {string} adaptedContentId
   * @returns {Object[]}
   */
  getMetricsByAdaptedContentId(adaptedContentId) {
    return this.db
      .prepare('SELECT * FROM post_metrics WHERE adapted_content_id = ? ORDER BY recorded_at DESC')
      .all(adaptedContentId)
      .map(this._deserializeMetrics);
  }

  /**
   * Get aggregated metrics for a platform within a date range.
   * @param {string} platform
   * @param {string} startDate - ISO date string
   * @param {string} endDate - ISO date string
   * @returns {Object}
   */
  getAggregatedMetrics(platform, startDate, endDate) {
    const row = this.db
      .prepare(`
        SELECT
          COUNT(*) as post_count,
          COALESCE(SUM(impressions), 0) as total_impressions,
          COALESCE(SUM(clicks), 0) as total_clicks,
          COALESCE(SUM(likes), 0) as total_likes,
          COALESCE(SUM(comments), 0) as total_comments,
          COALESCE(SUM(shares), 0) as total_shares,
          COALESCE(SUM(saves), 0) as total_saves,
          COALESCE(AVG(engagement_rate), 0) as avg_engagement_rate,
          COALESCE(SUM(reach), 0) as total_reach
        FROM post_metrics
        WHERE platform = ?
          AND recorded_at BETWEEN ? AND ?
      `)
      .get(platform, startDate, endDate);

    return row || {};
  }

  /**
   * Get top-performing adapted content by engagement.
   * @param {string} [platform]
   * @param {number} [limit=10]
   * @returns {Object[]}
   */
  getTopPerforming(platform, limit = 10) {
    let sql = `
      SELECT ac.*, pm.impressions, pm.likes, pm.comments, pm.shares, pm.engagement_rate
      FROM adapted_content ac
      JOIN post_metrics pm ON ac.id = pm.adapted_content_id
    `;
    const params = [];

    if (platform) {
      sql += ' WHERE ac.platform = ?';
      params.push(platform);
    }

    sql += ' ORDER BY pm.engagement_rate DESC LIMIT ?';
    params.push(limit);

    return this.db.prepare(sql).all(...params).map(this._deserializeAdapted);
  }

  // ─── Journeys ─────────────────────────────────────────────

  /**
   * Create a journey.
   * @param {Object} data
   * @returns {Object}
   */
  createJourney(data) {
    this.db
      .prepare(`
        INSERT INTO journeys (id, title, description, platform, content_ids, status, sequence_data, metadata)
        VALUES (@id, @title, @description, @platform, @content_ids, @status, @sequence_data, @metadata)
      `)
      .run({
        id: data.id,
        title: data.title,
        description: data.description || null,
        platform: data.platform,
        content_ids: JSON.stringify(data.content_ids || []),
        status: data.status || 'planning',
        sequence_data: JSON.stringify(data.sequence_data || {}),
        metadata: JSON.stringify(data.metadata || {}),
      });

    return this.getJourneyById(data.id);
  }

  /**
   * Get journey by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getJourneyById(id) {
    const row = this.db.prepare('SELECT * FROM journeys WHERE id = ?').get(id);
    return row ? this._deserializeJourney(row) : undefined;
  }

  /**
   * Get all journeys.
   * @param {string} [platform]
   * @returns {Object[]}
   */
  getJourneys(platform) {
    let sql = 'SELECT * FROM journeys';
    const params = [];

    if (platform) {
      sql += ' WHERE platform = ?';
      params.push(platform);
    }

    sql += ' ORDER BY created_at DESC';
    return this.db.prepare(sql).all(...params).map(this._deserializeJourney);
  }

  /**
   * Update a journey.
   * @param {string} id
   * @param {Object} data
   * @returns {Object|undefined}
   */
  updateJourney(id, data) {
    const fields = [];
    const params = { id };

    for (const [key, value] of Object.entries(data)) {
      if (['content_ids', 'sequence_data', 'metadata'].includes(key)) {
        fields.push(`${key} = @${key}`);
        params[key] = JSON.stringify(value);
      } else {
        fields.push(`${key} = @${key}`);
        params[key] = value;
      }
    }

    if (fields.length === 0) return this.getJourneyById(id);

    fields.push("updated_at = datetime('now')");

    this.db
      .prepare(`UPDATE journeys SET ${fields.join(', ')} WHERE id = @id`)
      .run(params);

    return this.getJourneyById(id);
  }

  // ─── Private Helpers ──────────────────────────────────────

  /** @private */
  _deserializeAdapted(row) {
    if (!row) return row;
    return {
      ...row,
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }

  /** @private */
  _deserializeMetrics(row) {
    if (!row) return row;
    return {
      ...row,
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }

  /** @private */
  _deserializeJourney(row) {
    if (!row) return row;
    return {
      ...row,
      content_ids: JSON.parse(row.content_ids || '[]'),
      sequence_data: JSON.parse(row.sequence_data || '{}'),
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }
}

export default new AnalyticsRepository();
