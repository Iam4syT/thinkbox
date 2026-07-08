/**
 * @module PromptBuilder
 * @description Builder pattern for composing rich, context-aware AI prompts.
 * Chain methods to add context, then call build() to get the final prompt string.
 */
export class PromptBuilder {
  constructor() {
    this._parts = [];
  }

  /** @param {string} role - e.g. "You are an expert LinkedIn content strategist" */
  addRole(role) {
    this._parts.push(`## ROLE\n${role}`);
    return this;
  }

  /** @param {string} ctx - Contextual information about the task */
  addContext(ctx) {
    this._parts.push(`## CONTEXT\n${ctx}`);
    return this;
  }

  /** @param {string} content - The content to process */
  addContent(content) {
    this._parts.push(`## CONTENT\n${content}`);
    return this;
  }

  /** @param {string[]} instructions - Array of instruction strings */
  addInstructions(instructions) {
    const list = Array.isArray(instructions)
      ? instructions.map((i, n) => `${n + 1}. ${i}`).join('\n')
      : instructions;
    this._parts.push(`## INSTRUCTIONS\n${list}`);
    return this;
  }

  /** @param {Object} format - JSON schema description or format string */
  addOutputFormat(format) {
    const fmt = typeof format === 'object' ? JSON.stringify(format, null, 2) : format;
    this._parts.push(`## OUTPUT FORMAT\nRespond ONLY with valid JSON matching this schema:\n${fmt}`);
    return this;
  }

  /** @param {Object} profile - Audience profile object */
  addAudienceContext(profile) {
    if (!profile || Object.keys(profile).length === 0) return this;
    this._parts.push(`## AUDIENCE CONTEXT\n${JSON.stringify(profile, null, 2)}`);
    return this;
  }

  /** @param {Object[]} history - Recent performance history */
  addPerformanceHistory(history) {
    if (!history || history.length === 0) return this;
    this._parts.push(`## PERFORMANCE HISTORY\n${JSON.stringify(history, null, 2)}`);
    return this;
  }

  /** @param {Object[]} okrs - Active OKRs */
  addOKRContext(okrs) {
    if (!okrs || okrs.length === 0) return this;
    this._parts.push(`## OKR ALIGNMENT\nAlign this content with these objectives:\n${JSON.stringify(okrs, null, 2)}`);
    return this;
  }

  /** @param {string} extra - Any additional context */
  addExtra(extra) {
    this._parts.push(extra);
    return this;
  }

  /** @returns {string} The composed prompt */
  build() {
    return this._parts.join('\n\n---\n\n');
  }

  /** Reset for reuse */
  reset() {
    this._parts = [];
    return this;
  }
}

export default PromptBuilder;
