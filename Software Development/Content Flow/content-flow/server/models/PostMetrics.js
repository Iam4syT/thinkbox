/**
 * @module PostMetrics
 * @description Model for post performance metrics.
 */
import { v4 as uuidv4 } from 'uuid';

export class PostMetrics {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.adapted_content_id = data.adapted_content_id;
    this.platform = data.platform;
    this.impressions = data.impressions || 0;
    this.clicks = data.clicks || 0;
    this.likes = data.likes || 0;
    this.comments = data.comments || 0;
    this.shares = data.shares || 0;
    this.saves = data.saves || 0;
    this.engagement_rate = data.engagement_rate || 0;
    this.reach = data.reach || 0;
    this.recorded_at = data.recorded_at || new Date().toISOString();
    this.metadata = data.metadata || {};
  }

  /** Calculate engagement rate from raw metrics */
  calculateEngagementRate() {
    if (this.impressions === 0) return 0;
    const interactions = this.likes + this.comments + this.shares + this.saves + this.clicks;
    this.engagement_rate = parseFloat(((interactions / this.impressions) * 100).toFixed(2));
    return this.engagement_rate;
  }

  get totalInteractions() {
    return this.likes + this.comments + this.shares + this.saves + this.clicks;
  }

  validate() {
    const errors = [];
    if (!this.adapted_content_id) errors.push('adapted_content_id is required');
    if (!this.platform) errors.push('platform is required');
    return { valid: errors.length === 0, errors };
  }

  toJSON() {
    return {
      id: this.id, adapted_content_id: this.adapted_content_id, platform: this.platform,
      impressions: this.impressions, clicks: this.clicks, likes: this.likes,
      comments: this.comments, shares: this.shares, saves: this.saves,
      engagement_rate: this.engagement_rate, reach: this.reach,
      recorded_at: this.recorded_at, metadata: this.metadata,
    };
  }
}

export default PostMetrics;
