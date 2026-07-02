/**
 * @module QueueItem
 * @description Model for publishing queue items.
 */
import { v4 as uuidv4 } from 'uuid';

export class QueueItem {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.adapted_content_id = data.adapted_content_id;
    this.platform = data.platform;
    this.scheduled_time = data.scheduled_time || null;
    this.priority = data.priority || 0;
    this.status = data.status || 'pending';
    this.retry_count = data.retry_count || 0;
    this.error_message = data.error_message || null;
    this.metadata = data.metadata || {};
    this.created_at = data.created_at || new Date().toISOString();
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  get isScheduled() { return this.status === 'scheduled' && this.scheduled_time !== null; }
  get isDue() {
    if (!this.isScheduled) return false;
    return new Date(this.scheduled_time) <= new Date();
  }

  validate() {
    const errors = [];
    if (!this.adapted_content_id) errors.push('adapted_content_id is required');
    if (!this.platform) errors.push('platform is required');
    return { valid: errors.length === 0, errors };
  }

  toJSON() {
    return {
      id: this.id, adapted_content_id: this.adapted_content_id,
      platform: this.platform, scheduled_time: this.scheduled_time,
      priority: this.priority, status: this.status, retry_count: this.retry_count,
      error_message: this.error_message, metadata: this.metadata,
      created_at: this.created_at, updated_at: this.updated_at,
    };
  }
}

export default QueueItem;
