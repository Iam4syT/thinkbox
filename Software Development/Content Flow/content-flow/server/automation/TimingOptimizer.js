/**
 * @module TimingOptimizer
 * @description Determines optimal posting times using AI.
 */
import { buildTimingPrompt } from '../ai/prompts/timing.prompts.js';

// Platform defaults when AI is not available
const PLATFORM_DEFAULTS = {
  linkedin: { hour: 9, minute: 0, daysAhead: 1 },   // 9am next weekday
  instagram: { hour: 12, minute: 0, daysAhead: 1 },  // noon next day
  youtube: { hour: 14, minute: 0, daysAhead: 2 },    // 2pm in 2 days
};

export class TimingOptimizer {
  /** @param {import('../ai/AIProvider.js').AIProvider} aiProvider */
  constructor(aiProvider) {
    this.ai = aiProvider;
  }

  /**
   * Get optimal posting time for a platform.
   * @param {string} platform
   * @param {Object} [audienceProfile={}]
   * @param {string[]} [recentPostTimes=[]]
   * @returns {Promise<{ optimal_time: string, reasoning: string, confidence: number }>}
   */
  async getOptimalTime(platform, audienceProfile = {}, recentPostTimes = []) {
    try {
      const prompt = buildTimingPrompt(platform, audienceProfile, recentPostTimes);
      const result = await this.ai.generateJSON(prompt);

      if (result._mock || !result.optimal_time) {
        return this._fallback(platform);
      }

      return {
        optimal_time: result.optimal_time,
        reasoning: result.reasoning || 'AI-recommended time',
        confidence: result.confidence || 0.7,
        alternative_times: result.alternative_times || [],
      };
    } catch (err) {
      console.error('[TimingOptimizer] Error:', err.message);
      return this._fallback(platform);
    }
  }

  /**
   * Fallback timing based on platform best practices.
   * @param {string} platform
   * @returns {Object}
   */
  _fallback(platform) {
    const defaults = PLATFORM_DEFAULTS[platform] || { hour: 10, minute: 0, daysAhead: 1 };
    const date = new Date();
    date.setDate(date.getDate() + defaults.daysAhead);
    date.setHours(defaults.hour, defaults.minute, 0, 0);

    // Skip weekends for LinkedIn
    if (platform === 'linkedin') {
      while (date.getDay() === 0 || date.getDay() === 6) {
        date.setDate(date.getDate() + 1);
      }
    }

    return {
      optimal_time: date.toISOString(),
      reasoning: `Default ${platform} peak posting window`,
      confidence: 0.5,
      alternative_times: [],
    };
  }
}

export default TimingOptimizer;
