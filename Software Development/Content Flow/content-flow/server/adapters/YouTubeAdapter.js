/**
 * @module YouTubeAdapter
 * @description Platform adapter for YouTube content tailoring.
 */
import { BasePlatformAdapter } from './BasePlatformAdapter.js';
import { buildYouTubePrompt } from '../ai/prompts/adaptation.prompts.js';

export class YouTubeAdapter extends BasePlatformAdapter {
  get platform() { return 'youtube'; }
  get charLimit() { return 5000; }
  get maxHashtags() { return 15; }
  _displayName() { return 'YouTube'; }
  _icon() { return '▶'; }
  _color() { return '#FF0000'; }

  _buildPrompt(content, context) {
    return buildYouTubePrompt(
      content,
      context.audienceContext || {},
      context.performanceHistory || []
    );
  }
}

export default YouTubeAdapter;
