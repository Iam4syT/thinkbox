/**
 * @module journey.prompts
 * @description Prompt builders for journey planning and narrative sequencing.
 */
import { PromptBuilder } from '../PromptBuilder.js';

/**
 * Build a journey gap analysis prompt.
 * @param {string} journeyTitle
 * @param {string} journeyDescription
 * @param {Object[]} posts - Array of queue items with adapted_text and platform
 * @returns {string}
 */
export function buildJourneyGapPrompt(journeyTitle, journeyDescription, posts) {
  return new PromptBuilder()
    .addRole(
      'You are a content journey architect specializing in narrative sequencing and audience retention. You analyze content series to identify gaps, improve flow, and maximize audience engagement over time.'
    )
    .addContext(
      `Journey: "${journeyTitle}"\nDescription: ${journeyDescription || 'Not provided'}\n\nAnalyze the following content series and identify narrative gaps, suggested ordering improvements, and missing content beats.`
    )
    .addContent(JSON.stringify(posts.map((p, i) => ({
      position: i + 1,
      platform: p.platform,
      preview: (p.adapted_text || '').substring(0, 200) + '...',
    })), null, 2))
    .addInstructions([
      'Identify the current narrative arc (hook/problem/solution/proof/cta)',
      'Detect which narrative beats are missing',
      'Suggest ideal ordering for maximum audience journey impact',
      'Suggest 1-2 "bridge" post ideas that could connect gaps',
      'Assess overall journey coherence (0-100)',
    ])
    .addOutputFormat({
      current_arc: 'string — detected narrative arc',
      missing_beats: 'string[] — missing elements in the narrative',
      suggested_order: 'number[] — array of current positions in suggested order',
      bridge_suggestions: 'Array<{ title: string, description: string, platform: string }>',
      coherence_score: 'number 0-100',
      analysis: 'string — detailed narrative analysis',
      recommendations: 'string[] — top 3 actionable recommendations',
    })
    .build();
}
