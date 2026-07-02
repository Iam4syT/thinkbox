/**
 * @module FeedbackRepository
 * @description Repository for feedback CRUD and aggregation.
 * Implements the Repository pattern for the feedback table.
 */
import { getDatabase } from '../database.js';

export class FeedbackRepository {
  /** @returns {import('better-sqlite3').Database} */
  get db() {
    return getDatabase();
  }

  /**
   * Create a feedback record.
   * @param {Object} data
   * @param {string} data.id
   * @param {string} data.adapted_content_id
   * @param {string} data.feedback_type
   * @param {string} [data.original_text]
   * @param {string} [data.edited_text]
   * @param {number} [data.rating]
   * @param {string} [data.comments]
   * @param {Object} [data.diff_data]
   * @param {Object} [data.metadata]
   * @returns {Object}
   */
  create(data) {
    const stmt = this.db.prepare(`
      INSERT INTO feedback (id, adapted_content_id, feedback_type, original_text, edited_text, rating, comments, diff_data, metadata)
      VALUES (@id, @adapted_content_id, @feedback_type, @original_text, @edited_text, @rating, @comments, @diff_data, @metadata)
    `);

    stmt.run({
      id: data.id,
      adapted_content_id: data.adapted_content_id,
      feedback_type: data.feedback_type,
      original_text: data.original_text || null,
      edited_text: data.edited_text || null,
      rating: data.rating || null,
      comments: data.comments || null,
      diff_data: JSON.stringify(data.diff_data || {}),
      metadata: JSON.stringify(data.metadata || {}),
    });

    return this.findById(data.id);
  }

  /**
   * Find feedback by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  findById(id) {
    const row = this.db.prepare('SELECT * FROM feedback WHERE id = ?').get(id);
    return row ? this._deserialize(row) : undefined;
  }

  /**
   * Find all feedback for an adapted content piece.
   * @param {string} adaptedContentId
   * @returns {Object[]}
   */
  findByAdaptedContentId(adaptedContentId) {
    return this.db
      .prepare('SELECT * FROM feedback WHERE adapted_content_id = ? ORDER BY created_at DESC')
      .all(adaptedContentId)
      .map(this._deserialize);
  }

  /**
   * Find all feedback of a certain type.
   * @param {string} feedbackType
   * @param {number} [limit=100]
   * @returns {Object[]}
   */
  findByType(feedbackType, limit = 100) {
    return this.db
      .prepare('SELECT * FROM feedback WHERE feedback_type = ? ORDER BY created_at DESC LIMIT ?')
      .all(feedbackType, limit)
      .map(this._deserialize);
  }

  /**
   * Get average rating for a platform.
   * @param {string} platform
   * @returns {{ avgRating: number, count: number }}
   */
  getAverageRatingByPlatform(platform) {
    const row = this.db
      .prepare(`
        SELECT AVG(f.rating) as avg_rating, COUNT(f.id) as count
        FROM feedback f
        JOIN adapted_content ac ON f.adapted_content_id = ac.id
        WHERE ac.platform = ? AND f.rating IS NOT NULL
      `)
      .get(platform);

    return {
      avgRating: row?.avg_rating || 0,
      count: row?.count || 0,
    };
  }

  /**
   * Get recent feedback for learning (edits and preferences).
   * @param {number} [limit=50]
   * @returns {Object[]}
   */
  getRecentLearningFeedback(limit = 50) {
    return this.db
      .prepare(`
        SELECT f.*, ac.platform, ac.adapted_text
        FROM feedback f
        JOIN adapted_content ac ON f.adapted_content_id = ac.id
        WHERE f.feedback_type IN ('edit', 'preference', 'rating')
        ORDER BY f.created_at DESC
        LIMIT ?
      `)
      .all(limit)
      .map(this._deserialize);
  }

  /**
   * Delete feedback by ID.
   * @param {string} id
   * @returns {boolean}
   */
  delete(id) {
    return this.db.prepare('DELETE FROM feedback WHERE id = ?').run(id).changes > 0;
  }

  /** @private */
  _deserialize(row) {
    if (!row) return row;
    return {
      ...row,
      diff_data: JSON.parse(row.diff_data || '{}'),
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }
}

export default new FeedbackRepository();
