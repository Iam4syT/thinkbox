/**
 * @module BasePlatformAdapter
 * @description Abstract base class for platform adapters (Template Method pattern).
 */
export class BasePlatformAdapter {
  /** @returns {string} Platform identifier */
  get platform() { throw new Error('BasePlatformAdapter.platform not implemented'); }

  /** @returns {number} Character limit */
  get charLimit() { throw new Error('BasePlatformAdapter.charLimit not implemented'); }

  /** @returns {number} Max hashtags */
  get maxHashtags() { throw new Error('BasePlatformAdapter.maxHashtags not implemented'); }

  /** @returns {Object} Platform configuration for UI */
  get config() {
    return {
      platform: this.platform,
      charLimit: this.charLimit,
      maxHashtags: this.maxHashtags,
      displayName: this._displayName(),
      icon: this._icon(),
      color: this._color(),
    };
  }

  _displayName() { return this.platform; }
  _icon() { return '📝'; }
  _color() { return '#666'; }

  /**
   * Template method — adapt content for this platform.
   * @param {string} refinedContent
   * @param {Object} context - { aiProvider, audienceContext, performanceHistory }
   * @returns {Promise<Object>} Adapted content object
   */
  async adapt(refinedContent, context = {}) {
    const prompt = this._buildPrompt(refinedContent, context);
    const { aiProvider } = context;

    let result;
    try {
      result = await aiProvider.generateJSON(prompt);
    } catch (err) {
      console.error(`[${this.platform}Adapter] AI error:`, err.message);
      result = this._mockResult(refinedContent);
    }

    return this._postProcess(result, refinedContent);
  }

  /**
   * Build the AI prompt — must be implemented by subclasses.
   * @param {string} content
   * @param {Object} context
   * @returns {string}
   */
  _buildPrompt(content, context) {
    throw new Error('BasePlatformAdapter._buildPrompt not implemented');
  }

  /**
   * Post-process the AI result (truncate, sanitize, etc.)
   * @param {Object} result
   * @param {string} original
   * @returns {Object}
   */
  _postProcess(result, original) {
    if (!result || result._mock) {
      return this._mockResult(original);
    }

    // Enforce char limit
    if (result.adapted_text && result.adapted_text.length > this.charLimit) {
      result.adapted_text = result.adapted_text.substring(0, this.charLimit - 3) + '...';
    }

    // Enforce hashtag limit
    if (Array.isArray(result.hashtags) && result.hashtags.length > this.maxHashtags) {
      result.hashtags = result.hashtags.slice(0, this.maxHashtags);
    }

    // Ensure defaults
    result.engagement_score = result.engagement_score ?? 50;
    result.hook_strength = result.hook_strength ?? 'medium';
    result.audience_fit = result.audience_fit ?? 50;

    return result;
  }

  /**
   * Returns a mock result when AI is unavailable.
   * @param {string} content
   * @returns {Object}
   */
  _mockResult(content) {
    const preview = content.substring(0, Math.min(content.length, this.charLimit - 100));
    return {
      adapted_text: `[${this.platform.toUpperCase()} VERSION]\n\n${preview}\n\n[Configure GEMINI_API_KEY to enable AI-powered adaptation]`,
      hashtags: [`${this.platform}`, 'contentflow', 'ai'],
      hook: preview.split('\n')[0] || preview.substring(0, 100),
      cta: 'Follow for more insights!',
      engagement_score: 50,
      hook_strength: 'medium',
      audience_fit: 50,
      journey_coherence: 50,
      _mock: true,
    };
  }
}

export default BasePlatformAdapter;
