/**
 * @module Journey
 * @description Model for content narrative journeys.
 */
import { v4 as uuidv4 } from 'uuid';

export class Journey {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.title = data.title;
    this.description = data.description || null;
    this.platform = data.platform;
    this.content_ids = data.content_ids || [];
    this.status = data.status || 'planning';
    this.sequence_data = data.sequence_data || {};
    this.metadata = data.metadata || {};
    this.created_at = data.created_at || new Date().toISOString();
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  get postCount() { return this.content_ids.length; }
  get isActive() { return this.status === 'active'; }

  validate() {
    const errors = [];
    if (!this.title) errors.push('title is required');
    if (!this.platform) errors.push('platform is required');
    return { valid: errors.length === 0, errors };
  }

  toJSON() {
    return {
      id: this.id, title: this.title, description: this.description,
      platform: this.platform, content_ids: this.content_ids,
      status: this.status, sequence_data: this.sequence_data,
      metadata: this.metadata, created_at: this.created_at, updated_at: this.updated_at,
    };
  }
}

export default Journey;
