/**
 * @module refinement.prompts
 * @description Prompt builders for the Brain Dump → Refined Draft stage.
 */
import { PromptBuilder } from '../PromptBuilder.js';

/**
 * Build a refinement prompt for Gemini.
 * @param {string} rawContent - The raw brain dump text
 * @param {Object} [audienceContext={}] - Learned audience profile
 * @returns {string} The composed prompt
 */
export function buildRefinementPrompt(rawContent, audienceContext = {}) {
  return new PromptBuilder()
    .addRole(
      'You are an expert content strategist and editor. Your job is to transform raw, unstructured brain dumps into polished, well-structured written pieces that capture the creator\'s authentic voice while maximizing clarity and engagement.'
    )
    .addContext(
      'The creator has written a raw brain dump — stream of consciousness, rough ideas, unstructured notes. Transform it into a publication-ready piece.'
    )
    .addContent(rawContent)
    .addAudienceContext(audienceContext)
    .addInstructions([
      'Preserve the creator\'s authentic voice and core message — do not fabricate ideas',
      'Add a compelling hook (attention-grabbing first sentence)',
      'Impose clear structure: hook → context → body (2-4 key points) → conclusion/CTA',
      'Fix grammar, tighten prose, remove redundancy',
      'Extract 5-8 SEO/discoverability keywords from the content',
      'Identify the primary tone (professional/conversational/inspirational/educational/provocative)',
      'Detect the content type (thought-leadership/how-to/story/data-insight/opinion)',
      'Suggest a compelling title',
      'Keep the refined text between 200-800 words unless the original warrants more',
    ])
    .addOutputFormat({
      refined_text: 'string — the polished, structured draft',
      suggested_title: 'string — compelling title',
      hook: 'string — the opening hook sentence',
      keywords: 'string[] — 5-8 SEO keywords',
      tone: 'string — detected tone',
      content_type: 'string — content category',
      structure_analysis: {
        hook: 'string',
        body_points: 'string[]',
        cta: 'string',
        word_count: 'number',
      },
    })
    .build();
}
