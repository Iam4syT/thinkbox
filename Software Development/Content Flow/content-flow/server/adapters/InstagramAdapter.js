/**
 * @module InstagramAdapter
 * @description Platform adapter for Instagram content tailoring.
 */
import { BasePlatformAdapter } from './BasePlatformAdapter.js';
import { buildInstagramPrompt } from '../ai/prompts/adaptation.prompts.js';

export class InstagramAdapter extends BasePlatformAdapter {
  get platform() { return 'instagram'; }
  get charLimit() { return 2200; }
  get maxHashtags() { return 30; }
  _displayName() { return 'Instagram'; }
  _icon() { return '📷'; }
  _color() { return '#E1306C'; }

  _buildPrompt(content, context) {
    return buildInstagramPrompt(
      content,
      context.audienceContext || {},
      context.performanceHistory || []
    );
  }
}

export default InstagramAdapter;
