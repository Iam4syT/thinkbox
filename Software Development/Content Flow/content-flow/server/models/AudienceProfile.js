/**
 * @module AudienceProfile
 * @description Model for per-platform audience profiles.
 */
export class AudienceProfile {
  constructor(data) {
    this.id = data.id;
    this.platform = data.platform;
    this.profile_data = data.profile_data || {
      demographics: {},
      interests: [],
      preferredTone: 'professional',
      peakEngagementTimes: [],
      contentPreferences: {},
    };
    this.engagement_patterns = data.engagement_patterns || {
      topPerformingFormats: [],
      avgEngagementRate: 0,
      bestHookStyles: [],
      preferredContentLength: 'medium',
    };
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  get tone() { return this.profile_data.preferredTone || 'professional'; }
  get interests() { return this.profile_data.interests || []; }
  get peakTimes() { return this.profile_data.peakEngagementTimes || []; }

  toJSON() {
    return {
      id: this.id, platform: this.platform,
      profile_data: this.profile_data,
      engagement_patterns: this.engagement_patterns,
      updated_at: this.updated_at,
    };
  }
}

export default AudienceProfile;
