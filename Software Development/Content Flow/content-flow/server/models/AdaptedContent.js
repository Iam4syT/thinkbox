/**
 * @module AdaptedContent
 * @description Model for platform-adapted content.
 */
import { v4 as uuidv4 } from 'uuid';

export class AdaptedContent {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.content_id = data.content_id;
    this.platform = data.platform;
    this.adapted_text = data.adapted_text;
    this.metadata = data.metadata || {};
    this.engagement_score = data.engagement_score || 0;
    this.status = data.status || 'draft';
    this.version = data.version || 1;
    this.created_at = data.created_at || new Date().toISOString();
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  get charCount() {
    return this.adapted_text ? this.adapted_text.length : 0;
  }

  get hashtags() {
    return this.metadata.hashtags || [];
  }

  validate() {
    const errors = [];
    if (!this.content_id) errors.push('content_id is required');
    if (!this.platform) errors.push('platform is required');
    if (!this.adapted_text) errors.push('adapted_text is required');
    const validPlatforms = ['linkedin', 'instagram', 'youtube'];
    if (!validPlatforms.includes(this.platform)) {
      errors.push(`platform must be one of: ${validPlatforms.join(', ')}`);
    }
    return { valid: errors.length === 0, errors };
  }

  toJSON() {
    return {
      id: this.id, content_id: this.content_id, platform: this.platform,
      adapted_text: this.adapted_text, metadata: this.metadata,
      engagement_score: this.engagement_score, status: this.status,
      version: this.version, created_at: this.created_at, updated_at: this.updated_at,
    };
  }
}

export default AdaptedContent;
