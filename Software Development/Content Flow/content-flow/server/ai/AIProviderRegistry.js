/**
 * @module AIProviderRegistry
 * @description Singleton registry of AI provider instances (Registry pattern).
 */
export class AIProviderRegistry {
  constructor() {
    /** @type {Map<string, import('./AIProvider.js').AIProvider>} */
    this._providers = new Map();
    this._default = null;
  }

  /**
   * Register a provider instance.
   * @param {import('./AIProvider.js').AIProvider} provider
   * @param {boolean} [isDefault=false]
   */
  register(provider, isDefault = false) {
    this._providers.set(provider.name, provider);
    if (isDefault || !this._default) this._default = provider.name;
  }

  /**
   * Get a provider by name.
   * @param {string} name
   * @returns {import('./AIProvider.js').AIProvider}
   */
  get(name) {
    const p = this._providers.get(name);
    if (!p) throw new Error(`AI provider '${name}' not registered`);
    return p;
  }

  /** @returns {import('./AIProvider.js').AIProvider} */
  getDefault() {
    return this.get(this._default);
  }

  /** @returns {string[]} */
  list() {
    return [...this._providers.keys()];
  }
}

// Singleton instance
export const aiProviderRegistry = new AIProviderRegistry();
export default aiProviderRegistry;
