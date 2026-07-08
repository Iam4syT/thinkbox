/**
 * @module JourneyPlanner
 * @description AI-powered narrative journey sequencing.
 */
import { buildJourneyGapPrompt } from '../ai/prompts/journey.prompts.js';
import { v4 as uuidv4 } from 'uuid';

export class JourneyPlanner {
  /**
   * @param {import('../ai/AIProvider.js').AIProvider} aiProvider
   * @param {Object} analyticsRepo - AnalyticsRepository instance
   * @param {Object} queueRepo - QueueRepository instance
   */
  constructor(aiProvider, analyticsRepo, queueRepo) {
    this.ai = aiProvider;
    this.analyticsRepo = analyticsRepo;
    this.queueRepo = queueRepo;
  }

  /**
   * Create a new content journey using AnalyticsRepository.
   * @param {Object} data - { title, description, platform }
   * @returns {Object}
   */
  create(data) {
    return this.analyticsRepo.createJourney({
      id: uuidv4(),
      title: data.title,
      description: data.description || null,
      platform: data.platform || null,
      status: 'planning',
    });
  }

  /**
   * Analyze narrative gaps in a journey.
   * @param {string} journeyId
   * @returns {Promise<Object>}
   */
  async analyzeGaps(journeyId) {
    const journey = this.analyticsRepo.getJourneyById(journeyId);
    if (!journey) throw new Error(`Journey not found: ${journeyId}`);

    // Find queue items whose metadata contains this journey_id
    const allQueue = this.queueRepo.findAll();
    const queueItems = allQueue.filter(q => {
      const meta = q.metadata || {};
      return meta.journey_id === journeyId;
    });

    if (queueItems.length === 0) {
      return {
        current_arc: 'No posts yet',
        missing_beats: ['Add posts to this journey first'],
        suggested_order: [],
        bridge_suggestions: [],
        coherence_score: 0,
        analysis: 'This journey has no posts yet. Add adapted content to the queue and assign it to this journey.',
        recommendations: ['Add your first post to start building the narrative'],
      };
    }

    try {
      const prompt = buildJourneyGapPrompt(
        journey.title,
        journey.description,
        queueItems
      );
      const result = await this.ai.generateJSON(prompt);

      if (result._mock) {
        return {
          current_arc: 'Hook → Content',
          missing_beats: ['Proof post', 'CTA post'],
          suggested_order: queueItems.map((_, i) => i + 1),
          bridge_suggestions: [],
          coherence_score: 60,
          analysis: 'Configure GEMINI_API_KEY for AI journey analysis',
          recommendations: ['Add more posts to build a complete narrative'],
        };
      }

      return result;
    } catch (err) {
      console.error('[JourneyPlanner] Error:', err.message);
      throw err;
    }
  }
}

export default JourneyPlanner;
