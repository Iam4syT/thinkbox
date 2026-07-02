/**
 * @module Feedback
 * @description Model for user feedback on adapted content.
 */
import { v4 as uuidv4 } from 'uuid';

export class Feedback {
  constructor(data) {
    this.id = data.id || uuidv4();
    this.adapted_content_id = data.adapted_content_id;
    this.feedback_type = data.feedback_type;
    this.original_text = data.original_text || null;
    this.edited_text = data.edited_text || null;
    this.rating = data.rating || null;
    this.comments = data.comments || null;
    this.diff_data = data.diff_data || {};
    this.metadata = data.metadata || {};
    this.created_at = data.created_at || new Date().toISOString();
  }

  validate() {
    const errors = [];
    if (!this.adapted_content_id) errors.push('adapted_content_id is required');
    const validTypes = ['rating', 'edit', 'preference', 'rejection'];
    if (!validTypes.includes(this.feedback_type)) {
      errors.push(`feedback_type must be one of: ${validTypes.join(', ')}`);
    }
    if (this.feedback_type === 'rating' && (this.rating == null || this.rating < 1 || this.rating > 5)) {
      errors.push('rating must be between 1 and 5');
    }
    if (this.feedback_type === 'edit' && !this.edited_text) {
      errors.push('edited_text is required for edit feedback');
    }
    return { valid: errors.length === 0, errors };
  }

  toJSON() {
    return {
      id: this.id, adapted_content_id: this.adapted_content_id,
      feedback_type: this.feedback_type, original_text: this.original_text,
      edited_text: this.edited_text, rating: this.rating, comments: this.comments,
      diff_data: this.diff_data, metadata: this.metadata, created_at: this.created_at,
    };
  }
}

export default Feedback;
