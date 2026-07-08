/**
 * @module LinkedInAdapter
 * @description Platform adapter for LinkedIn content tailoring.
 */
import { BasePlatformAdapter } from './BasePlatformAdapter.js';
import { buildLinkedInPrompt } from '../ai/prompts/adaptation.prompts.js';

export class LinkedInAdapter extends BasePlatformAdapter {
  get platform() { return 'linkedin'; }
  get charLimit() { return 3000; }
  get maxHashtags() { return 5; }
  _displayName() { return 'LinkedIn'; }
  _icon() { return 'in'; }
  _color() { return '#0077B5'; }

  _buildPrompt(content, context) {
    return buildLinkedInPrompt(
      content,
      context.audienceContext || {},
      context.performanceHistory || []
    );
  }
}

export default LinkedInAdapter;
