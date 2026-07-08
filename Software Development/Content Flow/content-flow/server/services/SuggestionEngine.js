/**
 * @module SuggestionEngine
 * @description AI-powered suggestion engine using Chain of Responsibility pattern.
 */
import { buildSuggestionPrompt } from '../ai/prompts/suggestion.prompts.js';

export class SuggestionEngine {
  /** @param {import('../ai/AIProvider.js').AIProvider} aiProvider */
  constructor(aiProvider) {
    this.ai = aiProvider;
  }

  /**
   * Generate content improvement suggestions.
   * @param {string} content - Refined or adapted content
   * @param {string} [platform='general']
   * @param {Object} [audienceProfile={}]
   * @returns {Promise<Object>} { suggestions, overall_score, top_opportunity }
   */
  async analyze(content, platform = 'general', audienceProfile = {}) {
    if (!content || content.trim().length === 0) {
      return { suggestions: [], overall_score: 0, top_opportunity: 'Add some content first' };
    }

    const prompt = buildSuggestionPrompt(content, platform, audienceProfile);

    try {
      const result = await this.ai.generateJSON(prompt);

      if (result._mock) {
        return {
          suggestions: [
            { id: 'mock-1', type: 'hook', title: 'Strengthen your hook', description: 'Configure GEMINI_API_KEY for real AI suggestions', priority: 'high', impact: 'High engagement boost', example: null },
          ],
          overall_score: 50,
          top_opportunity: 'Configure AI to get personalized suggestions',
        };
      }

      return {
        suggestions: Array.isArray(result.suggestions) ? result.suggestions : [],
        overall_score: result.overall_score ?? 50,
        top_opportunity: result.top_opportunity || '',
      };
    } catch (err) {
      console.error('[SuggestionEngine] Error:', err.message);
      return { suggestions: [], overall_score: 50, top_opportunity: '' };
    }
  }
}

export default SuggestionEngine;
