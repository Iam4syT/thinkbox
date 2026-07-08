/**
 * @module suggestion.prompts
 * @description Prompt builders for the AI Suggestion Engine.
 */
import { PromptBuilder } from '../PromptBuilder.js';

/**
 * Build a suggestion prompt for a piece of content.
 * @param {string} content - The refined or adapted content
 * @param {string} [platform='general'] - Target platform
 * @param {Object} [audienceProfile={}] - Learned audience profile
 * @returns {string}
 */
export function buildSuggestionPrompt(content, platform = 'general', audienceProfile = {}) {
  return new PromptBuilder()
    .addRole(
      `You are a senior content strategist and engagement optimization expert specializing in ${platform} content. Your job is to analyze content and provide actionable, prioritized improvement suggestions.`
    )
    .addContext(
      `Analyze the following content intended for ${platform} and provide concrete, actionable suggestions to improve its performance.`
    )
    .addContent(content)
    .addAudienceContext(audienceProfile)
    .addInstructions([
      'Analyze hook strength (first line effectiveness)',
      'Evaluate tone consistency with platform norms',
      'Identify missing engagement triggers (questions, polls, stories)',
      'Assess CTA clarity and effectiveness',
      'Review hashtag strategy if applicable',
      'Check audience alignment with the learned profile',
      'Provide 5-7 concrete, specific suggestions',
      'Prioritize by potential impact (high/medium/low)',
    ])
    .addOutputFormat({
      suggestions: [
        {
          id: 'string — unique suggestion id',
          type: 'hook | tone | engagement | cta | hashtags | audience | structure',
          title: 'string — short title',
          description: 'string — specific, actionable recommendation',
          priority: 'high | medium | low',
          impact: 'string — expected impact if applied',
          example: 'string | null — example of how to apply this suggestion',
        },
      ],
      overall_score: 'number 0-100 — current content quality score',
      top_opportunity: 'string — single most impactful thing to improve',
    })
    .build();
}
