/**
 * @module timing.prompts
 * @description Prompt builders for optimal post timing AI.
 */
import { PromptBuilder } from '../PromptBuilder.js';

/**
 * Build a timing optimization prompt.
 * @param {string} platform
 * @param {Object} [audienceProfile={}]
 * @param {string[]} [recentPostTimes=[]] - ISO datetime strings of recent posts
 * @returns {string}
 */
export function buildTimingPrompt(platform, audienceProfile = {}, recentPostTimes = []) {
  const now = new Date().toISOString();
  return new PromptBuilder()
    .addRole(
      `You are an expert social media timing strategist. You determine the optimal time to post on ${platform} to maximize reach and engagement.`
    )
    .addContext(
      `Current time: ${now}. Determine the best time to schedule the next post on ${platform} based on platform best practices, audience activity patterns, and post spacing.`
    )
    .addAudienceContext(audienceProfile)
    .addExtra(
      recentPostTimes.length > 0
        ? `## RECENT POST TIMES\n${recentPostTimes.join('\n')}`
        : '## RECENT POST TIMES\nNo previous posts yet.'
    )
    .addInstructions([
      'Consider platform-specific peak engagement windows',
      'LinkedIn: Tue-Thu 8-10am and 12pm are peak times',
      'Instagram: Mon-Fri 11am-1pm, 7-9pm are peak times',
      'YouTube: Fri-Sun 12pm-4pm are peak times',
      'Avoid posting too close to recent posts (minimum 2 hours gap)',
      'Consider time zones — default to GMT if unknown',
      'Return an ISO 8601 datetime string for the optimal time',
      'Provide 2 alternative times',
    ])
    .addOutputFormat({
      optimal_time: 'string — ISO 8601 datetime',
      reasoning: 'string — why this time was chosen',
      confidence: 'number 0-1',
      alternative_times: 'string[] — 2 alternative ISO 8601 datetimes',
    })
    .build();
}
