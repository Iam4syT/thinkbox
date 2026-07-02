/**
 * @module QueueRepository
 * @description Repository for the publishing queue.
 * Implements the Repository pattern for the queue table.
 */
import { getDatabase } from '../database.js';

export class QueueRepository {
  /** @returns {import('better-sqlite3').Database} */
  get db() {
    return getDatabase();
  }

  /**
   * Add an item to the queue.
   * @param {Object} data
   * @returns {Object}
   */
  create(data) {
    this.db
      .prepare(`
        INSERT INTO queue (id, adapted_content_id, platform, scheduled_time, priority, status, metadata)
        VALUES (@id, @adapted_content_id, @platform, @scheduled_time, @priority, @status, @metadata)
      `)
      .run({
        id: data.id,
        adapted_content_id: data.adapted_content_id,
        platform: data.platform,
        scheduled_time: data.scheduled_time || null,
        priority: data.priority || 0,
        status: data.status || 'pending',
        metadata: JSON.stringify(data.metadata || {}),
      });

    return this.findById(data.id);
  }

  /**
   * Find a queue item by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  findById(id) {
    const row = this.db.prepare('SELECT * FROM queue WHERE id = ?').get(id);
    return row ? this._deserialize(row) : undefined;
  }

  /**
   * Get all items in the queue with optional filters.
   * @param {Object} [filters]
   * @param {string} [filters.status]
   * @param {string} [filters.platform]
   * @param {number} [filters.limit]
   * @returns {Object[]}
   */
  findAll(filters = {}) {
    let sql = 'SELECT * FROM queue WHERE 1=1';
    const params = [];

    if (filters.status) {
      sql += ' AND status = ?';
      params.push(filters.status);
    }
    if (filters.platform) {
      sql += ' AND platform = ?';
      params.push(filters.platform);
    }

    sql += ' ORDER BY priority DESC, scheduled_time ASC, created_at ASC';

    if (filters.limit) {
      sql += ' LIMIT ?';
      params.push(filters.limit);
    }

    return this.db.prepare(sql).all(...params).map(this._deserialize);
  }

  /**
   * Get items due for publishing (scheduled_time <= now and status = scheduled).
   * @returns {Object[]}
   */
  getDueItems() {
    return this.db
      .prepare(`
        SELECT * FROM queue
        WHERE status = 'scheduled'
          AND scheduled_time <= datetime('now')
        ORDER BY priority DESC, scheduled_time ASC
      `)
      .all()
      .map(this._deserialize);
  }

  /**
   * Update a queue item.
   * @param {string} id
   * @param {Object} data
   * @returns {Object|undefined}
   */
  update(id, data) {
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

    if (fields.length === 0) return this.findById(id);

    fields.push("updated_at = datetime('now')");

    this.db
      .prepare(`UPDATE queue SET ${fields.join(', ')} WHERE id = @id`)
      .run(params);

    return this.findById(id);
  }

  /**
   * Delete a queue item.
   * @param {string} id
   * @returns {boolean}
   */
  delete(id) {
    return this.db.prepare('DELETE FROM queue WHERE id = ?').run(id).changes > 0;
  }

  /**
   * Reorder queue items by updating their priority.
   * @param {Array<{id: string, priority: number}>} items
   */
  reorder(items) {
    const stmt = this.db.prepare("UPDATE queue SET priority = ?, updated_at = datetime('now') WHERE id = ?");
    const tx = this.db.transaction((itemList) => {
      for (const item of itemList) {
        stmt.run(item.priority, item.id);
      }
    });
    tx(items);
  }

  /**
   * Get queue statistics.
   * @returns {Object}
   */
  getStats() {
    const rows = this.db
      .prepare('SELECT status, COUNT(*) as count FROM queue GROUP BY status')
      .all();
    const stats = { pending: 0, scheduled: 0, publishing: 0, published: 0, failed: 0, total: 0 };
    for (const row of rows) {
      stats[row.status] = row.count;
      stats.total += row.count;
    }
    return stats;
  }

  /** @private */
  _deserialize(row) {
    if (!row) return row;
    return {
      ...row,
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }
}

export default new QueueRepository();
