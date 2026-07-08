/**
 * @module EngagementScorer
 * @description Predicts engagement score for adapted content using AI.
 */
import { buildScoringPrompt } from '../ai/prompts/scoring.prompts.js';

export class EngagementScorer {
  /** @param {import('../ai/AIProvider.js').AIProvider} aiProvider */
  constructor(aiProvider) {
    this.ai = aiProvider;
  }

  /**
   * Score content for a given platform.
   * @param {string} content
   * @param {string} platform
   * @param {Object} [audienceProfile={}]
   * @param {Object[]} [history=[]]
   * @returns {Promise<Object>} Scoring result
   */
  async score(content, platform, audienceProfile = {}, history = []) {
    const prompt = buildScoringPrompt(content, platform, audienceProfile, history);
    try {
      const result = await this.ai.generateJSON(prompt);
      if (result._mock) {
        return { engagement_score: 50, hook_strength: 'medium', audience_fit: 50, journey_coherence: 50, okr_alignment: 50, reasoning: { overall: 'AI not configured' } };
      }
      return result;
    } catch (err) {
      console.error('[EngagementScorer] Error:', err.message);
      return { engagement_score: 50, hook_strength: 'medium', audience_fit: 50, journey_coherence: 50, okr_alignment: 50 };
    }
  }
}

export default EngagementScorer;
