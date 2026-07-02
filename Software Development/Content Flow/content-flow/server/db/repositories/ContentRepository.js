/**
 * @module ContentRepository
 * @description Repository for content CRUD operations.
 * Implements the Repository pattern for the content table.
 */
import { getDatabase } from '../database.js';

export class ContentRepository {
  /** @returns {import('better-sqlite3').Database} */
  get db() {
    return getDatabase();
  }

  /**
   * Create a new content record.
   * @param {Object} data
   * @param {string} data.id
   * @param {string} [data.title]
   * @param {string} data.raw_content
   * @param {string} [data.refined_content]
   * @param {string} [data.content_type]
   * @param {string[]} [data.tags]
   * @param {Object} [data.metadata]
   * @returns {Object} The created content row
   */
  create(data) {
    const stmt = this.db.prepare(`
      INSERT INTO content (id, title, raw_content, refined_content, content_type, tags, metadata, status)
      VALUES (@id, @title, @raw_content, @refined_content, @content_type, @tags, @metadata, @status)
    `);

    stmt.run({
      id: data.id,
      title: data.title || null,
      raw_content: data.raw_content,
      refined_content: data.refined_content || null,
      content_type: data.content_type || 'brain_dump',
      tags: JSON.stringify(data.tags || []),
      metadata: JSON.stringify(data.metadata || {}),
      status: data.status || 'draft',
    });

    return this.findById(data.id);
  }

  /**
   * Find content by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  findById(id) {
    const row = this.db.prepare('SELECT * FROM content WHERE id = ?').get(id);
    return row ? this._deserialize(row) : undefined;
  }

  /**
   * List all content with optional filters.
   * @param {Object} [filters]
   * @param {string} [filters.status]
   * @param {string} [filters.content_type]
   * @param {number} [filters.limit]
   * @param {number} [filters.offset]
   * @returns {Object[]}
   */
  findAll(filters = {}) {
    let sql = 'SELECT * FROM content WHERE 1=1';
    const params = [];

    if (filters.status) {
      sql += ' AND status = ?';
      params.push(filters.status);
    }
    if (filters.content_type) {
      sql += ' AND content_type = ?';
      params.push(filters.content_type);
    }

    sql += ' ORDER BY updated_at DESC';

    if (filters.limit) {
      sql += ' LIMIT ?';
      params.push(filters.limit);
    }
    if (filters.offset) {
      sql += ' OFFSET ?';
      params.push(filters.offset);
    }

    return this.db.prepare(sql).all(...params).map(this._deserialize);
  }

  /**
   * Update a content record.
   * @param {string} id
   * @param {Object} data - Fields to update
   * @returns {Object|undefined} The updated row
   */
  update(id, data) {
    const fields = [];
    const params = {};

    for (const [key, value] of Object.entries(data)) {
      if (['tags', 'metadata'].includes(key)) {
        fields.push(`${key} = @${key}`);
        params[key] = JSON.stringify(value);
      } else {
        fields.push(`${key} = @${key}`);
        params[key] = value;
      }
    }

    if (fields.length === 0) return this.findById(id);

    fields.push("updated_at = datetime('now')");
    params.id = id;

    this.db.prepare(`UPDATE content SET ${fields.join(', ')} WHERE id = @id`).run(params);
    return this.findById(id);
  }

  /**
   * Delete content by ID. Cascades to adapted_content and feedback.
   * @param {string} id
   * @returns {boolean} True if a row was deleted
   */
  delete(id) {
    const result = this.db.prepare('DELETE FROM content WHERE id = ?').run(id);
    return result.changes > 0;
  }

  /**
   * Count content by status.
   * @returns {Object} { draft: n, refined: n, published: n, archived: n }
   */
  countByStatus() {
    const rows = this.db
      .prepare('SELECT status, COUNT(*) as count FROM content GROUP BY status')
      .all();
    const counts = { draft: 0, refined: 0, published: 0, archived: 0 };
    for (const row of rows) {
      counts[row.status] = row.count;
    }
    return counts;
  }

  /**
   * Search content by title or raw_content.
   * @param {string} query
   * @returns {Object[]}
   */
  search(query) {
    const sql = `
      SELECT * FROM content
      WHERE title LIKE ? OR raw_content LIKE ? OR refined_content LIKE ?
      ORDER BY updated_at DESC
      LIMIT 50
    `;
    const pattern = `%${query}%`;
    return this.db.prepare(sql).all(pattern, pattern, pattern).map(this._deserialize);
  }

  /**
   * Deserialize JSON fields from a database row.
   * @param {Object} row
   * @returns {Object}
   * @private
   */
  _deserialize(row) {
    if (!row) return row;
    return {
      ...row,
      tags: JSON.parse(row.tags || '[]'),
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }
}

export default new ContentRepository();
