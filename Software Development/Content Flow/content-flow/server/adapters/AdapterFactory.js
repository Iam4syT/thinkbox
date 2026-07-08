/**
 * @module AdapterFactory
 * @description Factory for creating platform adapter instances.
 */
import { LinkedInAdapter } from './LinkedInAdapter.js';
import { InstagramAdapter } from './InstagramAdapter.js';
import { YouTubeAdapter } from './YouTubeAdapter.js';

export class AdapterFactory {
  /**
   * Create a platform adapter by name.
   * @param {string} platform
   * @returns {import('./BasePlatformAdapter.js').BasePlatformAdapter}
   */
  static create(platform) {
    switch (platform.toLowerCase()) {
      case 'linkedin': return new LinkedInAdapter();
      case 'instagram': return new InstagramAdapter();
      case 'youtube': return new YouTubeAdapter();
      default: throw new Error(`Unknown platform: '${platform}'`);
    }
  }
}

export default AdapterFactory;
