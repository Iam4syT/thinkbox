/**
 * @module RefinedDraftView
 * @description Shows the AI-refined draft with metadata. Mounts into #mount-refined-draft.
 */
import { $, createElement } from '../utils/dom.js';

export class RefinedDraftView {
  constructor() {
    this.container = null;
    this.contentId = null;
  }

  mount(mountId) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    if (!this.container) return;
    this._render();
    document.addEventListener('contentflow:refined', e => this._onRefined(e.detail));
  }

  _render() {
    this.container.innerHTML = `
      <div class="glass-card refined-draft-view hidden" id="refined-draft-card">
        <div class="refined-draft-header">
          <div>
            <h3>✍️ Refined Draft</h3>
            <p class="text-muted" style="font-size:0.8rem;margin-top:2px;">AI-polished version of your content</p>
          </div>
          <button id="rd-re-refine-btn" class="btn btn--ghost btn--sm">🔄 Re-Refine</button>
        </div>

        <div id="rd-metadata" class="refined-meta" style="display:flex;gap:0.5rem;flex-wrap:wrap;margin-bottom:1rem;"></div>

        <div id="rd-content" class="refined-content-body"></div>

        <div class="refined-draft-footer">
          <span id="rd-word-count" class="text-muted" style="font-size:0.8rem;"></span>
        </div>
      </div>
    `;

    document.getElementById('rd-re-refine-btn')?.addEventListener('click', () => {
      document.dispatchEvent(new CustomEvent('contentflow:request-rerefine', { detail: { contentId: this.contentId } }));
    });
  }

  _onRefined({ contentId, refinedContent, metadata }) {
    this.contentId = contentId;
    const card = document.getElementById('refined-draft-card');
    if (!card) return;
    card.classList.remove('hidden');

    // Metadata row
    const metaEl = document.getElementById('rd-metadata');
    if (metaEl && metadata) {
      const items = [];
      if (metadata.tone) items.push(`<span class="badge badge--info">🎯 ${metadata.tone}</span>`);
      if (metadata.content_type) items.push(`<span class="badge badge--outline">📄 ${metadata.content_type}</span>`);
      if (Array.isArray(metadata.keywords)) {
        metadata.keywords.slice(0, 5).forEach(k => {
          items.push(`<span class="badge badge--outline" style="font-size:0.7rem;">${k}</span>`);
        });
      }
      metaEl.innerHTML = items.join('');
    }

    // Content
    const contentEl = document.getElementById('rd-content');
    if (contentEl && refinedContent) {
      contentEl.innerHTML = `<p style="white-space:pre-wrap;line-height:1.7;">${this._escapeHtml(refinedContent)}</p>`;
      const words = refinedContent.trim().split(/\s+/).length;
      const wc = document.getElementById('rd-word-count');
      if (wc) wc.textContent = `${words} words`;
    }

    card.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }

  _escapeHtml(str) {
    const d = document.createElement('div');
    d.textContent = str;
    return d.innerHTML;
  }
}

export default RefinedDraftView;
