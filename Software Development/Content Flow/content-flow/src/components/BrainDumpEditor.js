/**
 * @module BrainDumpEditor
 * @description Stage 1 UI — brain dump input with AI refinement.
 * Mounts into: #mount-brain-dump
 */
import { $, createElement, debounce, formatNumber } from '../utils/dom.js';
import * as api from '../services/api.js';

export class BrainDumpEditor {
  constructor() {
    this.contentId = null;
    this.container = null;
    this._onInput = debounce(() => this._updateCounts(), 150);
  }

  mount(mountId) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    if (!this.container) return;
    this._render();
    this._bindEvents();
  }

  _render() {
    this.container.innerHTML = `
      <div class="glass-card brain-dump-editor" id="brain-dump-card">
        <div class="brain-dump-header">
          <div>
            <h3 class="brain-dump-title">🧠 Brain Dump</h3>
            <p class="text-muted" style="font-size:0.8rem;margin-top:2px;">Paste your raw ideas — AI will refine them</p>
          </div>
          <div class="brain-dump-counts" id="bd-counts">
            <span class="badge badge--outline" id="bd-word-count">0 words</span>
            <span class="badge badge--outline" id="bd-char-count">0 chars</span>
          </div>
        </div>

        <div class="form-group" style="margin-top:0.75rem;">
          <input type="text" id="bd-title" class="form-input" placeholder="Optional title..." autocomplete="off" />
        </div>

        <div class="form-group">
          <select id="bd-content-type" class="form-select">
            <option value="brain_dump">🧠 Brain Dump</option>
            <option value="article">📝 Article Draft</option>
            <option value="notes">📋 Notes</option>
          </select>
        </div>

        <textarea id="bd-textarea" class="brain-dump-textarea form-input"
          placeholder="Start typing or paste your raw ideas here... No need to be perfect. Let the AI do the heavy lifting."
          rows="10"></textarea>

        <div class="brain-dump-actions">
          <button id="bd-save-btn" class="btn btn--ghost btn--sm">
            💾 Save Draft
          </button>
          <button id="bd-refine-btn" class="btn btn--primary btn--glow" disabled>
            ✨ Refine with AI
          </button>
        </div>

        <div id="bd-status" class="brain-dump-status hidden"></div>
      </div>
    `;
  }

  _bindEvents() {
    const textarea = $('#bd-textarea', this.container);
    const saveBtn = $('#bd-save-btn', this.container);
    const refineBtn = $('#bd-refine-btn', this.container);

    textarea.addEventListener('input', () => {
      this._updateCounts();
      refineBtn.disabled = textarea.value.trim().length < 20;
    });

    saveBtn.addEventListener('click', () => this._save());
    refineBtn.addEventListener('click', () => this._refine());
  }

  _updateCounts() {
    const textarea = $('#bd-textarea', this.container);
    const text = textarea.value;
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    const chars = text.length;
    const wc = $('#bd-word-count', this.container);
    const cc = $('#bd-char-count', this.container);
    if (wc) wc.textContent = `${formatNumber(words)} words`;
    if (cc) cc.textContent = `${formatNumber(chars)} chars`;
  }

  async _save() {
    const textarea = $('#bd-textarea', this.container);
    const titleInput = $('#bd-title', this.container);
    const typeSelect = $('#bd-content-type', this.container);
    const text = textarea.value.trim();

    if (!text) return this._showStatus('Please enter some content first.', 'error');

    this._setLoading('save', true);
    try {
      const res = await api.createContent({
        raw_content: text,
        title: titleInput.value.trim() || null,
        content_type: typeSelect.value,
      });
      this.contentId = res.data.id;
      this._showStatus('✅ Draft saved!', 'success');
      document.dispatchEvent(new CustomEvent('contentflow:saved', { detail: { contentId: this.contentId } }));
    } catch (err) {
      this._showStatus('❌ Save failed: ' + (err.message || 'Server offline'), 'error');
    } finally {
      this._setLoading('save', false);
    }
  }

  async _refine() {
    const textarea = $('#bd-textarea', this.container);
    const titleInput = $('#bd-title', this.container);
    const typeSelect = $('#bd-content-type', this.container);
    const text = textarea.value.trim();

    if (!text) return this._showStatus('Please enter some content first.', 'error');

    // Auto-save first if not saved
    if (!this.contentId) {
      try {
        const res = await api.createContent({
          raw_content: text,
          title: titleInput.value.trim() || null,
          content_type: typeSelect.value,
        });
        this.contentId = res.data.id;
      } catch (err) {
        return this._showStatus('❌ Could not save content: ' + (err.message || 'Server offline'), 'error');
      }
    }

    this._setLoading('refine', true);
    this._showStatus('🤖 AI is thinking...', 'loading');

    try {
      const res = await api.refineContent(this.contentId, {});
      const refinement = res.data?.refinement || res.data;

      document.dispatchEvent(new CustomEvent('contentflow:refined', {
        detail: {
          contentId: this.contentId,
          refinedContent: refinement?.refined_text || refinement?.content?.refined_content,
          metadata: refinement,
        }
      }));
      this._showStatus('✅ Content refined! See the result below.', 'success');
    } catch (err) {
      this._showStatus('❌ Refinement failed: ' + (err.message || 'Server offline'), 'error');
    } finally {
      this._setLoading('refine', false);
    }
  }

  _setLoading(btn, loading) {
    const saveBtn = $('#bd-save-btn', this.container);
    const refineBtn = $('#bd-refine-btn', this.container);
    if (btn === 'save') {
      saveBtn.disabled = loading;
      saveBtn.textContent = loading ? '⏳ Saving...' : '💾 Save Draft';
    } else {
      refineBtn.disabled = loading;
      refineBtn.textContent = loading ? '⏳ Refining...' : '✨ Refine with AI';
    }
  }

  _showStatus(msg, type = 'info') {
    const status = $('#bd-status', this.container);
    if (!status) return;
    status.textContent = msg;
    status.className = `brain-dump-status status--${type}`;
    status.classList.remove('hidden');
    if (type === 'success') setTimeout(() => status.classList.add('hidden'), 4000);
  }

  /** Load existing content into editor */
  loadContent(content) {
    this.contentId = content.id;
    const textarea = $('#bd-textarea', this.container);
    const titleInput = $('#bd-title', this.container);
    if (textarea) textarea.value = content.raw_content || '';
    if (titleInput) titleInput.value = content.title || '';
    this._updateCounts();
    const refineBtn = $('#bd-refine-btn', this.container);
    if (refineBtn) refineBtn.disabled = false;
  }
}

export default BrainDumpEditor;
