/**
 * @module Objective
 * @description Model for OKR objectives and key results.
 */
import { v4 as uuidv4 } from 'uuid';

export class Objective {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.title = data.title;
    this.description = data.description || null;
    this.target_date = data.target_date || null;
    this.status = data.status || 'active';
    this.progress = data.progress || 0;
    this.metadata = data.metadata || {};
    this.key_results = (data.key_results || []).map((kr) => new KeyResult(kr));
    this.created_at = data.created_at || new Date().toISOString();
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  get isComplete() { return this.progress >= 1; }
  get progressPercent() { return Math.round(this.progress * 100); }

  validate() {
    const errors = [];
    if (!this.title) errors.push('title is required');
    return { valid: errors.length === 0, errors };
  }

  toJSON() {
    return {
      id: this.id, title: this.title, description: this.description,
      target_date: this.target_date, status: this.status, progress: this.progress,
      metadata: this.metadata, key_results: this.key_results.map((kr) => kr.toJSON()),
      created_at: this.created_at, updated_at: this.updated_at,
    };
  }
}

export class KeyResult {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.objective_id = data.objective_id;
    this.title = data.title;
    this.metric_type = data.metric_type;
    this.current_value = data.current_value || 0;
    this.target_value = data.target_value;
    this.unit = data.unit || '';
    this.status = data.status || 'active';
    this.metadata = data.metadata || {};
    this.created_at = data.created_at || new Date().toISOString();
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  get progress() {
    return this.target_value > 0 ? Math.min(this.current_value / this.target_value, 1) : 0;
  }

  get progressPercent() { return Math.round(this.progress * 100); }

  toJSON() {
    return {
      id: this.id, objective_id: this.objective_id, title: this.title,
      metric_type: this.metric_type, current_value: this.current_value,
      target_value: this.target_value, unit: this.unit, status: this.status,
      metadata: this.metadata, created_at: this.created_at, updated_at: this.updated_at,
    };
  }
}

export default Objective;
