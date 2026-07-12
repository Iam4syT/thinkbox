/**
 * @module OpenAIProvider
 * @description Concrete AI provider using the OpenAI SDK.
 */
import OpenAI from 'openai';
import { AIProvider } from '../AIProvider.js';
import config from '../../config.js';

export class OpenAIProvider extends AIProvider {
  constructor() {
    super();
    this._modelName = config.openaiModel;
    this._client = config.hasValidApiKey
      ? new OpenAI({ apiKey: config.openaiApiKey })
      : null;
  }

  get name() { return 'openai'; }

  /**
   * Generate text from a prompt.
   * @param {string} prompt
   * @returns {Promise<string>}
   */
  async generate(prompt) {
    if (!this._client) {
      return '[AI unavailable: Set OPENAI_API_KEY in your .env file]';
    }
    try {
      const completion = await this._client.chat.completions.create({
        model: this._modelName,
        messages: [{ role: 'user', content: prompt }],
      });
      return completion.choices[0].message.content ?? '';
    } catch (err) {
      console.error('[OpenAIProvider] generate error:', err.message);
      throw err;
    }
  }

  /**
   * Generate a JSON object from a prompt.
   * Uses OpenAI's json_object response format.
   * @param {string} prompt
   * @returns {Promise<Object>}
   */
  async generateJSON(prompt) {
    if (!this._client) {
      return { _mock: true, message: 'AI unavailable: Set OPENAI_API_KEY in .env' };
    }
    try {
      const completion = await this._client.chat.completions.create({
        model: this._modelName,
        response_format: { type: 'json_object' },
        messages: [
          {
            role: 'system',
            content: 'You are a helpful assistant that always responds with valid JSON.',
          },
          { role: 'user', content: prompt },
        ],
      });
      const text = completion.choices[0].message.content ?? '{}';
      return JSON.parse(text);
    } catch (err) {
      console.error('[OpenAIProvider] generateJSON error:', err.message);
      throw err;
    }
  }
}

export default OpenAIProvider;
