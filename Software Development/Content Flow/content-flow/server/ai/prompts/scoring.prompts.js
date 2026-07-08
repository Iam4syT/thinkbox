/**
 * @module scoring.prompts
 * @description Prompt builders for AI engagement scoring.
 */
import { PromptBuilder } from '../PromptBuilder.js';

/**
 * Build a scoring prompt to predict engagement for content.
 * @param {string} content - The adapted content to score
 * @param {string} platform - Target platform
 * @param {Object} [audienceProfile={}]
 * @param {Object[]} [history=[]] - Past performance data
 * @returns {string}
 */
export function buildScoringPrompt(content, platform, audienceProfile = {}, history = []) {
  return new PromptBuilder()
    .addRole(
      `You are an AI engagement prediction expert with deep expertise in ${platform} algorithm mechanics, audience psychology, and content performance analytics.`
    )
    .addContext(
      `Predict the engagement performance of the following ${platform} content. Base your prediction on platform best practices, content quality signals, and the provided audience context.`
    )
    .addContent(content)
    .addAudienceContext(audienceProfile)
    .addPerformanceHistory(history)
    .addInstructions([
      'Score overall engagement potential (0-100)',
      'Assess hook strength based on first-line psychology',
      'Evaluate audience fit against the learned profile',
      'Rate journey coherence (how well this fits in a content sequence)',
      'Rate OKR alignment (how much this serves growth objectives)',
      'Provide brief reasoning for each score',
    ])
    .addOutputFormat({
      engagement_score: 'number 0-100',
      hook_strength: 'weak | medium | strong',
      audience_fit: 'number 0-100',
      journey_coherence: 'number 0-100',
      okr_alignment: 'number 0-100',
      reasoning: {
        engagement: 'string',
        hook: 'string',
        audience: 'string',
        overall: 'string',
      },
    })
    .build();
}
