/**
 * @module Content
 * @description Content domain model with validation and factory methods.
 */
import { v4 as uuidv4 } from 'uuid';

export class Content {
  /**
   * @param {Object} data
   * @param {string} [data.id]
   * @param {string} [data.title]
   * @param {string} data.raw_content
   * @param {string} [data.refined_content]
   * @param {string} [data.content_type]
   * @param {string[]} [data.tags]
   * @param {Object} [data.metadata]
   * @param {string} [data.status]
   * @param {string} [data.created_at]
   * @param {string} [data.updated_at]
   */
  constructor(data) {
    this.id = data.id || uuidv4();
    this.title = data.title || null;
    this.raw_content = data.raw_content;
    this.refined_content = data.refined_content || null;
    this.content_type = data.content_type || 'brain_dump';
    this.tags = data.tags || [];
    this.metadata = data.metadata || {};
    this.status = data.status || 'draft';
    this.created_at = data.created_at || new Date().toISOString();
    this.updated_at = data.updated_at || new Date().toISOString();
  }

  /** @returns {boolean} Whether the content has been refined */
  get isRefined() {
    return this.refined_content !== null && this.refined_content.length > 0;
  }

  /** @returns {string} The best available content (refined or raw) */
  get bestContent() {
    return this.isRefined ? this.refined_content : this.raw_content;
  }

  /** @returns {number} Word count of the best content */
  get wordCount() {
    return this.bestContent.split(/\s+/).filter(Boolean).length;
  }

  /**
   * Validate the content model.
   * @returns {{ valid: boolean, errors: string[] }}
   */
  validate() {
    const errors = [];
    if (!this.raw_content || this.raw_content.trim().length === 0) {
      errors.push('raw_content is required');
    }
    if (this.raw_content && this.raw_content.length > 50_000) {
      errors.push('raw_content exceeds maximum length of 50,000 characters');
    }
    const validTypes = ['brain_dump', 'article', 'notes'];
    if (!validTypes.includes(this.content_type)) {
      errors.push(`content_type must be one of: ${validTypes.join(', ')}`);
    }
    const validStatuses = ['draft', 'refined', 'published', 'archived'];
    if (!validStatuses.includes(this.status)) {
      errors.push(`status must be one of: ${validStatuses.join(', ')}`);
    }
    return { valid: errors.length === 0, errors };
  }

  /** Convert to a plain object for persistence. */
  toJSON() {
    return {
      id: this.id,
      title: this.title,
      raw_content: this.raw_content,
      refined_content: this.refined_content,
      content_type: this.content_type,
      tags: this.tags,
      metadata: this.metadata,
      status: this.status,
      created_at: this.created_at,
      updated_at: this.updated_at,
    };
  }

  /**
   * Factory: create a Content from a brain dump string.
   * @param {string} rawText
   * @param {string} [title]
   * @returns {Content}
   */
  static fromBrainDump(rawText, title) {
    return new Content({
      raw_content: rawText,
      title: title || null,
      content_type: 'brain_dump',
    });
  }
}

export default Content;
