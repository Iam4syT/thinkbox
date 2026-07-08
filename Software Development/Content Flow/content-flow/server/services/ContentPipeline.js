/**
 * @module ContentPipeline
 * @description Orchestrates the full 4-stage content pipeline.
 */
import { v4 as uuidv4 } from 'uuid';

export class ContentPipeline {
  /**
   * @param {Object} deps
   * @param {import('../ai/AIProvider.js').AIProvider} deps.aiProvider
   * @param {import('../adapters/PlatformRegistry.js').PlatformRegistry} deps.platformRegistry
   * @param {import('./RefinementService.js').RefinementService} deps.refinementService
   * @param {import('./SuggestionEngine.js').SuggestionEngine} deps.suggestionEngine
   * @param {import('./EngagementScorer.js').EngagementScorer} deps.engagementScorer
   * @param {Object} deps.contentRepo
   * @param {Object} deps.analyticsRepo
   * @param {Object} deps.learningRepo
   */
  constructor(deps) {
    this.ai = deps.aiProvider;
    this.platformRegistry = deps.platformRegistry;
    this.refinementService = deps.refinementService;
    this.suggestionEngine = deps.suggestionEngine;
    this.engagementScorer = deps.engagementScorer;
    this.contentRepo = deps.contentRepo;
    this.analyticsRepo = deps.analyticsRepo;
    this.learningRepo = deps.learningRepo;
  }

  /**
   * Stage 1: Refine a brain dump into a polished draft.
   * @param {string} contentId
   * @returns {Promise<Object>} { content, refinement }
   */
  async refine(contentId) {
    const content = this.contentRepo.findById(contentId);
    if (!content) throw new Error(`Content not found: ${contentId}`);

    // Get audience context
    let audienceContext = {};
    try {
      const profile = this.learningRepo.getAudienceProfile('general');
      if (profile && profile.profile_data) audienceContext = profile.profile_data;
    } catch (_) { /* no profile yet */ }

    const result = await this.refinementService.refine(content.raw_content, audienceContext);

    // Merge refinement into existing metadata
    const existingMeta = content.metadata || {};
    const updated = this.contentRepo.update(contentId, {
      refined_content: result.refined_text,
      metadata: {
        ...existingMeta,
        suggested_title: result.suggested_title,
        hook: result.hook,
        keywords: result.keywords,
        tone: result.tone,
        content_type: result.content_type,
        structure_analysis: result.structure_analysis,
      },
      status: 'refined',
    });

    return { content: updated, refinement: result };
  }

  /**
   * Stage 2: Adapt refined content for selected platforms.
   * @param {string} contentId
   * @param {string[]} platforms
   * @returns {Promise<Object[]>} Array of adapted content records
   */
  async adapt(contentId, platforms) {
    const content = this.contentRepo.findById(contentId);
    if (!content) throw new Error(`Content not found: ${contentId}`);
    if (!content.refined_content) throw new Error('Content must be refined before adapting');

    const adaptations = [];

    for (const platform of platforms) {
      try {
        const adapter = this.platformRegistry.get(platform);

        let audienceContext = {};
        try {
          const profile = this.learningRepo.getAudienceProfile(platform);
          if (profile && profile.profile_data) audienceContext = profile.profile_data;
        } catch (_) { /* no profile yet */ }

        const adapted = await adapter.adapt(content.refined_content, {
          aiProvider: this.ai,
          audienceContext,
        });

        const record = this.analyticsRepo.createAdaptedContent({
          id: uuidv4(),
          content_id: contentId,
          platform,
          adapted_text: adapted.adapted_text,
          metadata: {
            hashtags: adapted.hashtags || [],
            hook: adapted.hook,
            cta: adapted.cta,
            hook_strength: adapted.hook_strength,
            audience_fit: adapted.audience_fit,
            journey_coherence: adapted.journey_coherence || 50,
            carousel_slides: adapted.carousel_slides || null,
            chapters: adapted.chapters || null,
            script_outline: adapted.script_outline || null,
          },
          engagement_score: adapted.engagement_score || 50,
          status: 'draft',
        });

        adaptations.push(record);
      } catch (err) {
        console.error(`[ContentPipeline] adapt error for ${platform}:`, err.message);
        adaptations.push({ platform, error: err.message });
      }
    }

    this.contentRepo.update(contentId, { status: 'refined' });
    return adaptations;
  }

  /**
   * Get AI suggestions for content.
   * @param {string} contentId
   * @param {string} [platform='general']
   * @returns {Promise<Object>}
   */
  async suggest(contentId, platform = 'general') {
    const content = this.contentRepo.findById(contentId);
    if (!content) throw new Error(`Content not found: ${contentId}`);

    const text = content.refined_content || content.raw_content;
    let audienceProfile = {};
    try {
      const profile = this.learningRepo.getAudienceProfile(platform);
      if (profile && profile.profile_data) audienceProfile = profile.profile_data;
    } catch (_) { /* noop */ }

    return this.suggestionEngine.analyze(text, platform, audienceProfile);
  }
}

export default ContentPipeline;
