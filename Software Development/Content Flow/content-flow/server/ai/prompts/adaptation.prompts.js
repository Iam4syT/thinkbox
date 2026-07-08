/**
 * @module adaptation.prompts
 * @description Prompt builders for the Refined Draft → Platform-Tailored Drafts stage.
 */
import { PromptBuilder } from '../PromptBuilder.js';

/**
 * @param {string} refinedContent
 * @param {Object} [audienceContext={}]
 * @param {Object[]} [performanceHistory=[]]
 * @returns {string}
 */
export function buildLinkedInPrompt(refinedContent, audienceContext = {}, performanceHistory = []) {
  return new PromptBuilder()
    .addRole(
      'You are an expert LinkedIn content strategist with 10+ years of experience building thought leadership and growing professional audiences.'
    )
    .addContext(
      'Adapt the following refined content for LinkedIn. LinkedIn rewards professional insight, data-backed claims, contrarian takes, and authentic storytelling. The audience is professionals, decision-makers, and industry peers.'
    )
    .addContent(refinedContent)
    .addAudienceContext(audienceContext)
    .addPerformanceHistory(performanceHistory)
    .addInstructions([
      'Maximum 3,000 characters (LinkedIn hard limit)',
      'Start with a hook: contrarian statement, surprising data point, or thought-provoking question',
      'Use line breaks every 1-2 sentences for mobile readability (no long paragraphs)',
      'Professional but approachable tone — avoid corporate jargon',
      'End with an engagement question to drive comments',
      'Include 3-5 relevant professional hashtags (no more)',
      'Frame content as thought leadership or professional insight',
      'Suggest a CTA (follow, comment, share, visit link)',
      'Score your prediction of engagement (0-100) and hook strength',
    ])
    .addOutputFormat({
      adapted_text: 'string — the full LinkedIn post text (max 3000 chars)',
      hashtags: 'string[] — 3-5 hashtags without #',
      hook: 'string — the opening hook',
      cta: 'string — call to action',
      engagement_score: 'number 0-100',
      hook_strength: 'weak | medium | strong',
      audience_fit: 'number 0-100',
      character_count: 'number',
    })
    .build();
}

/**
 * @param {string} refinedContent
 * @param {Object} [audienceContext={}]
 * @param {Object[]} [performanceHistory=[]]
 * @returns {string}
 */
export function buildInstagramPrompt(refinedContent, audienceContext = {}, performanceHistory = []) {
  return new PromptBuilder()
    .addRole(
      'You are an expert Instagram content creator specializing in community building, carousel content, and high-engagement captions.'
    )
    .addContext(
      'Adapt the following refined content for Instagram. Instagram is visual-first and story-driven. Captions should feel personal, relatable, and inspire saves and shares. Carousel format (multiple slides) performs best for educational content.'
    )
    .addContent(refinedContent)
    .addAudienceContext(audienceContext)
    .addPerformanceHistory(performanceHistory)
    .addInstructions([
      'Maximum 2,200 characters for the caption',
      'Start with a scroll-stopping first line (visible without expanding)',
      'Use strategic line breaks and white space',
      'Incorporate relevant emojis naturally (not excessively)',
      'If content suits a carousel, provide 5-7 slide titles',
      'Create a strong save/share motivation (value, tips, or inspiration)',
      'End with a CTA: question, poll suggestion, or link-in-bio reference',
      'Include up to 30 hashtags — mix of niche, medium, and broad',
      'Hashtags go at the end after a line break',
    ])
    .addOutputFormat({
      adapted_text: 'string — the full Instagram caption',
      hashtags: 'string[] — up to 30 hashtags without #',
      hook: 'string — first visible line',
      cta: 'string — call to action',
      carousel_slides: 'string[] | null — slide titles if carousel format suits this content',
      engagement_score: 'number 0-100',
      hook_strength: 'weak | medium | strong',
      audience_fit: 'number 0-100',
    })
    .build();
}

/**
 * @param {string} refinedContent
 * @param {Object} [audienceContext={}]
 * @param {Object[]} [performanceHistory=[]]
 * @returns {string}
 */
export function buildYouTubePrompt(refinedContent, audienceContext = {}, performanceHistory = []) {
  return new PromptBuilder()
    .addRole(
      'You are an expert YouTube content strategist specializing in long-form educational and thought leadership content, SEO optimization, and viewer retention.'
    )
    .addContext(
      'Adapt the following refined content for YouTube. Create a complete description with chapters, keywords, and a script outline. YouTube rewards watch-time, SEO keywords, and community engagement.'
    )
    .addContent(refinedContent)
    .addAudienceContext(audienceContext)
    .addPerformanceHistory(performanceHistory)
    .addInstructions([
      'Write a keyword-rich video description (up to 5,000 characters)',
      'First 2-3 sentences must summarize the video (shown before "Show More")',
      'Include timestamps/chapters (e.g. 0:00 Intro, 1:30 Main point)',
      'Create a 5-7 point script outline with timing estimates',
      'Add subscribe CTA, like CTA, and comment question',
      'Include relevant links placeholder section',
      'First 5 seconds hook: the most compelling question or statement to prevent drop-off',
      'Include 5-15 SEO-optimized tags/hashtags',
      'Suggest a video title (under 70 characters)',
    ])
    .addOutputFormat({
      adapted_text: 'string — the full YouTube description',
      video_title: 'string — suggested SEO title',
      hashtags: 'string[] — 5-15 tags without #',
      hook: 'string — the 5-second opening hook',
      cta: 'string — primary call to action',
      chapters: 'Array<{ time: string, title: string }> — timestamp chapters',
      script_outline: 'Array<{ section: string, duration: string, key_points: string[] }>',
      engagement_score: 'number 0-100',
      hook_strength: 'weak | medium | strong',
      audience_fit: 'number 0-100',
    })
    .build();
}
