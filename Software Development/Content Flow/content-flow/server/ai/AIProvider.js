/**
 * @module AIProvider
 * @description Abstract base class for AI providers (Strategy pattern).
 * All concrete AI providers must extend this class.
 */
export class AIProvider {
  /** @returns {string} Unique provider name */
  get name() { throw new Error('AIProvider.name not implemented'); }

  /**
   * Generate text from a prompt.
   * @param {string} prompt
   * @param {Object} [options]
   * @returns {Promise<string>}
   */
  async generate(prompt, options = {}) {
    throw new Error('AIProvider.generate not implemented');
  }

  /**
   * Generate a JSON object from a prompt.
   * @param {string} prompt
   * @param {Object} [options]
   * @returns {Promise<Object>}
   */
  async generateJSON(prompt, options = {}) {
    throw new Error('AIProvider.generateJSON not implemented');
  }
}

export default AIProvider;
