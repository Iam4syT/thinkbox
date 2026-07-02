/**
 * @module OKRRepository
 * @description Repository for Objectives and Key Results.
 * Implements the Repository pattern for the objectives and key_results tables.
 */
import { getDatabase } from '../database.js';

export class OKRRepository {
  /** @returns {import('better-sqlite3').Database} */
  get db() {
    return getDatabase();
  }

  // ─── Objectives ───────────────────────────────────────────

  /**
   * Create an objective.
   * @param {Object} data
   * @returns {Object}
   */
  createObjective(data) {
    this.db
      .prepare(`
        INSERT INTO objectives (id, title, description, target_date, status, progress, metadata)
        VALUES (@id, @title, @description, @target_date, @status, @progress, @metadata)
      `)
      .run({
        id: data.id,
        title: data.title,
        description: data.description || null,
        target_date: data.target_date || null,
        status: data.status || 'active',
        progress: data.progress || 0,
        metadata: JSON.stringify(data.metadata || {}),
      });

    return this.getObjectiveById(data.id);
  }

  /**
   * Get an objective by ID, including its key results.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getObjectiveById(id) {
    const row = this.db.prepare('SELECT * FROM objectives WHERE id = ?').get(id);
    if (!row) return undefined;

    const objective = this._deserializeObjective(row);
    objective.key_results = this.getKeyResultsByObjectiveId(id);
    return objective;
  }

  /**
   * Get all objectives with their key results.
   * @param {string} [status]
   * @returns {Object[]}
   */
  getAllObjectives(status) {
    let sql = 'SELECT * FROM objectives';
    const params = [];

    if (status) {
      sql += ' WHERE status = ?';
      params.push(status);
    }

    sql += ' ORDER BY created_at DESC';

    const objectives = this.db.prepare(sql).all(...params).map(this._deserializeObjective);

    for (const obj of objectives) {
      obj.key_results = this.getKeyResultsByObjectiveId(obj.id);
    }

    return objectives;
  }

  /**
   * Update an objective.
   * @param {string} id
   * @param {Object} data
   * @returns {Object|undefined}
   */
  updateObjective(id, data) {
    const fields = [];
    const params = { id };

    for (const [key, value] of Object.entries(data)) {
      if (key === 'metadata') {
        fields.push('metadata = @metadata');
        params.metadata = JSON.stringify(value);
      } else if (key !== 'key_results') {
        fields.push(`${key} = @${key}`);
        params[key] = value;
      }
    }

    if (fields.length === 0) return this.getObjectiveById(id);

    fields.push("updated_at = datetime('now')");

    this.db
      .prepare(`UPDATE objectives SET ${fields.join(', ')} WHERE id = @id`)
      .run(params);

    return this.getObjectiveById(id);
  }

  /**
   * Delete an objective and its key results.
   * @param {string} id
   * @returns {boolean}
   */
  deleteObjective(id) {
    return this.db.prepare('DELETE FROM objectives WHERE id = ?').run(id).changes > 0;
  }

  /**
   * Recalculate objective progress from its key results.
   * @param {string} objectiveId
   * @returns {Object|undefined}
   */
  recalculateProgress(objectiveId) {
    const keyResults = this.getKeyResultsByObjectiveId(objectiveId);
    if (keyResults.length === 0) return this.getObjectiveById(objectiveId);

    const totalProgress = keyResults.reduce((sum, kr) => {
      const krProgress = kr.target_value > 0 ? Math.min(kr.current_value / kr.target_value, 1) : 0;
      return sum + krProgress;
    }, 0);

    const avgProgress = totalProgress / keyResults.length;

    this.db
      .prepare("UPDATE objectives SET progress = ?, updated_at = datetime('now') WHERE id = ?")
      .run(avgProgress, objectiveId);

    return this.getObjectiveById(objectiveId);
  }

  // ─── Key Results ──────────────────────────────────────────

  /**
   * Create a key result.
   * @param {Object} data
   * @returns {Object}
   */
  createKeyResult(data) {
    this.db
      .prepare(`
        INSERT INTO key_results (id, objective_id, title, metric_type, current_value, target_value, unit, status, metadata)
        VALUES (@id, @objective_id, @title, @metric_type, @current_value, @target_value, @unit, @status, @metadata)
      `)
      .run({
        id: data.id,
        objective_id: data.objective_id,
        title: data.title,
        metric_type: data.metric_type,
        current_value: data.current_value || 0,
        target_value: data.target_value,
        unit: data.unit || '',
        status: data.status || 'active',
        metadata: JSON.stringify(data.metadata || {}),
      });

    return this.getKeyResultById(data.id);
  }

  /**
   * Get a key result by ID.
   * @param {string} id
   * @returns {Object|undefined}
   */
  getKeyResultById(id) {
    const row = this.db.prepare('SELECT * FROM key_results WHERE id = ?').get(id);
    return row ? this._deserializeKeyResult(row) : undefined;
  }

  /**
   * Get all key results for an objective.
   * @param {string} objectiveId
   * @returns {Object[]}
   */
  getKeyResultsByObjectiveId(objectiveId) {
    return this.db
      .prepare('SELECT * FROM key_results WHERE objective_id = ? ORDER BY created_at ASC')
      .all(objectiveId)
      .map(this._deserializeKeyResult);
  }

  /**
   * Update a key result.
   * @param {string} id
   * @param {Object} data
   * @returns {Object|undefined}
   */
  updateKeyResult(id, data) {
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

    if (fields.length === 0) return this.getKeyResultById(id);

    fields.push("updated_at = datetime('now')");

    this.db
      .prepare(`UPDATE key_results SET ${fields.join(', ')} WHERE id = @id`)
      .run(params);

    return this.getKeyResultById(id);
  }

  /**
   * Delete a key result.
   * @param {string} id
   * @returns {boolean}
   */
  deleteKeyResult(id) {
    return this.db.prepare('DELETE FROM key_results WHERE id = ?').run(id).changes > 0;
  }

  // ─── Private Helpers ──────────────────────────────────────

  /** @private */
  _deserializeObjective(row) {
    if (!row) return row;
    return {
      ...row,
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }

  /** @private */
  _deserializeKeyResult(row) {
    if (!row) return row;
    return {
      ...row,
      metadata: JSON.parse(row.metadata || '{}'),
    };
  }
}

export default new OKRRepository();
