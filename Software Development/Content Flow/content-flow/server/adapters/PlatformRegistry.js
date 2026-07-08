/**
 * @module PlatformRegistry
 * @description Registry of all registered platform adapters.
 * Self-registers Phase 1 platforms on construction.
 */
import { AdapterFactory } from './AdapterFactory.js';

export class PlatformRegistry {
  constructor() {
    /** @type {Map<string, import('./BasePlatformAdapter.js').BasePlatformAdapter>} */
    this._adapters = new Map();
    this._autoRegister();
  }

  _autoRegister() {
    for (const platform of ['linkedin', 'instagram', 'youtube']) {
      this.register(AdapterFactory.create(platform));
    }
  }

  /**
   * @param {import('./BasePlatformAdapter.js').BasePlatformAdapter} adapter
   */
  register(adapter) {
    this._adapters.set(adapter.platform, adapter);
  }

  /**
   * @param {string} platform
   * @returns {import('./BasePlatformAdapter.js').BasePlatformAdapter}
   */
  get(platform) {
    const a = this._adapters.get(platform.toLowerCase());
    if (!a) throw new Error(`Platform '${platform}' not registered`);
    return a;
  }

  /** @returns {string[]} */
  list() { return [...this._adapters.keys()]; }

  /** @returns {Object[]} Platform configs for the UI */
  listConfigs() { return [...this._adapters.values()].map(a => a.config); }
}

export default PlatformRegistry;
