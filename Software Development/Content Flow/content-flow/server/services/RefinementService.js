/**
 * @module RefinementService
 * @description Brain Dump → Refined Draft service using AI.
 */
import { buildRefinementPrompt } from '../ai/prompts/refinement.prompts.js';

export class RefinementService {
  /** @param {import('../ai/AIProvider.js').AIProvider} aiProvider */
  constructor(aiProvider) {
    this.ai = aiProvider;
  }

  /**
   * Refine a raw brain dump into a polished draft.
   * @param {string} rawContent
   * @param {Object} [audienceContext={}]
   * @returns {Promise<Object>} { refined_text, suggested_title, hook, keywords, tone, content_type, structure_analysis }
   */
  async refine(rawContent, audienceContext = {}) {
    if (!rawContent || rawContent.trim().length === 0) {
      throw new Error('rawContent is required for refinement');
    }

    const prompt = buildRefinementPrompt(rawContent, audienceContext);

    try {
      const result = await this.ai.generateJSON(prompt);

      if (result._mock) {
        return {
          refined_text: rawContent,
          suggested_title: 'Draft Title',
          hook: rawContent.split('\n')[0] || rawContent.substring(0, 100),
          keywords: [],
          tone: 'conversational',
          content_type: 'brain_dump',
          structure_analysis: { hook: '', body_points: [], cta: '', word_count: rawContent.split(/\s+/).length },
          _mock: true,
        };
      }

      return {
        refined_text: result.refined_text || rawContent,
        suggested_title: result.suggested_title || '',
        hook: result.hook || '',
        keywords: Array.isArray(result.keywords) ? result.keywords : [],
        tone: result.tone || 'conversational',
        content_type: result.content_type || 'brain_dump',
        structure_analysis: result.structure_analysis || {},
      };
    } catch (err) {
      console.error('[RefinementService] Error:', err.message);
      throw err;
    }
  }
}

export default RefinementService;
