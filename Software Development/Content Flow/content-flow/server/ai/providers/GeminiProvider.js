/**
 * @module GeminiProvider
 * @description Concrete AI provider using Google Gemini SDK.
 */
import { GoogleGenerativeAI } from '@google/generative-ai';
import { AIProvider } from '../AIProvider.js';
import config from '../../config.js';

export class GeminiProvider extends AIProvider {
  constructor() {
    super();
    this._modelName = config.geminiModel;
    this._client = config.hasValidApiKey
      ? new GoogleGenerativeAI(config.geminiApiKey)
      : null;
  }

  get name() { return 'gemini'; }

  /** @returns {import('@google/generative-ai').GenerativeModel|null} */
  _getModel() {
    if (!this._client) return null;
    return this._client.getGenerativeModel({ model: this._modelName });
  }

  /**
   * Generate text from a prompt.
   * @param {string} prompt
   * @returns {Promise<string>}
   */
  async generate(prompt) {
    const model = this._getModel();
    if (!model) {
      return '[AI unavailable: Set GEMINI_API_KEY in your .env file]';
    }
    try {
      const result = await model.generateContent(prompt);
      return result.response.text();
    } catch (err) {
      console.error('[GeminiProvider] generate error:', err.message);
      throw err;
    }
  }

  /**
   * Generate a JSON object from a prompt.
   * Asks Gemini to respond in JSON mode.
   * @param {string} prompt
   * @returns {Promise<Object>}
   */
  async generateJSON(prompt) {
    const model = this._getModel();
    if (!model) {
      return { _mock: true, message: 'AI unavailable: Set GEMINI_API_KEY in .env' };
    }
    try {
      const jsonModel = this._client.getGenerativeModel({
        model: this._modelName,
        generationConfig: { responseMimeType: 'application/json' },
      });
      const result = await jsonModel.generateContent(prompt);
      const text = result.response.text();
      return JSON.parse(text);
    } catch (err) {
      console.error('[GeminiProvider] generateJSON error:', err.message);
      // Attempt to extract JSON from raw text fallback
      try {
        const raw = err.response?.text ? err.response.text() : null;
        if (raw) {
          const match = raw.match(/\{[\s\S]*\}/);
          if (match) return JSON.parse(match[0]);
        }
      } catch (_) { /* noop */ }
      throw err;
    }
  }
}

export default GeminiProvider;
