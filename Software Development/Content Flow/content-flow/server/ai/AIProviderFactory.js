/**
 * @module AIProviderFactory
 * @description Factory for creating and registering AI providers.
 */
import { GeminiProvider } from './providers/GeminiProvider.js';
import { aiProviderRegistry } from './AIProviderRegistry.js';

export class AIProviderFactory {
  /**
   * Create a provider by name, register it, and return it.
   * @param {string} name - 'gemini' | 'openai' | 'claude'
   * @returns {import('./AIProvider.js').AIProvider}
   */
  static create(name = 'gemini') {
    let provider;
    switch (name) {
      case 'gemini':
        provider = new GeminiProvider();
        break;
      default:
        throw new Error(`Unknown AI provider: '${name}'`);
    }
    aiProviderRegistry.register(provider, name === 'gemini');
    return provider;
  }
}

export default AIProviderFactory;
