/**
 * @module ContentLibrary
 * @description Browse, filter, and manage all saved content pieces.
 */
import { formatDate } from '../utils/dom.js';
import * as api from '../services/api.js';

const STATUS_BADGES = {
  draft: { label: 'Draft', color: '#6b6890' },
  refined: { label: 'Refined', color: '#7c3aed' },
  published: { label: 'Published', color: '#22c55e' },
  archived: { label: 'Archived', color: '#374151' },
};

export class ContentLibrary {
  constructor() {
    this.container = null;
    this.items = [];
    this._onSelect = null;
  }

  mount(mountId, { onSelect } = {}) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    this._onSelect = onSelect;
    if (!this.container) return;
    this._render();
    this.refresh();
    document.addEventListener('contentflow:saved', () => this.refresh());
    document.addEventListener('contentflow:refined', () => this.refresh());
  }

  async refresh() {
    try {
      const res = await api.getContent();
      this.items = res.data || [];
      this._renderList();
    } catch (err) {
      console.error('[ContentLibrary] refresh failed:', err.message);
    }
  }

  _render() {
    this.container.innerHTML = `
      <div class="glass-card content-library">
        <div class="library-header">
          <h3>📚 Content Library</h3>
          <span id="lib-count" class="badge badge--outline">0</span>
        </div>
        <div id="lib-list" class="library-list">
          <div class="queue-empty">Loading...</div>
        </div>
      </div>
    `;
  }

  _renderList() {
    const el = document.getElementById('lib-list');
    const countEl = document.getElementById('lib-count');
    if (!el) return;
    if (countEl) countEl.textContent = this.items.length;

    if (!this.items.length) {
      el.innerHTML = `<div class="queue-empty"><p>No content yet.</p><p class="text-muted" style="font-size:0.8rem;">Start by writing a brain dump above.</p></div>`;
      return;
    }

    el.innerHTML = '';
    this.items.forEach(item => {
      const statusCfg = STATUS_BADGES[item.status] || STATUS_BADGES.draft;
      const preview = (item.refined_content || item.raw_content || '').substring(0, 100);

      const row = document.createElement('div');
      row.className = 'library-item';
      row.innerHTML = `
        <div class="library-item-body">
          <div class="library-item-title">${this._esc(item.title || 'Untitled')}</div>
          <div class="library-item-preview text-muted">${this._esc(preview)}${preview.length >= 100 ? '...' : ''}</div>
          <div class="library-item-meta">
            <span class="badge" style="color:${statusCfg.color};border-color:${statusCfg.color}40;">${statusCfg.label}</span>
            <span class="text-muted" style="font-size:0.7rem;">${formatDate(item.updated_at || item.created_at)}</span>
          </div>
        </div>
        <div class="library-item-actions">
          <button class="btn btn--ghost btn--xs lib-load-btn" data-id="${item.id}" title="Load into editor">✏️</button>
          <button class="btn btn--ghost btn--xs lib-delete-btn" data-id="${item.id}" title="Delete" style="color:#ef4444;">✕</button>
        </div>
      `;

      row.querySelector('.lib-load-btn')?.addEventListener('click', () => {
        if (this._onSelect) this._onSelect(item);
        document.dispatchEvent(new CustomEvent('contentflow:load-content', { detail: item }));
      });

      row.querySelector('.lib-delete-btn')?.addEventListener('click', () => this._delete(item.id));
      el.appendChild(row);
    });
  }

  async _delete(id) {
    if (!confirm('Delete this content and all its adaptations?')) return;
    try {
      await api.deleteContent(id);
      this.refresh();
    } catch (err) {
      console.error('[ContentLibrary] delete failed:', err.message);
    }
  }

  _esc(str) {
    const d = document.createElement('div');
    d.textContent = str || '';
    return d.innerHTML;
  }
}

export default ContentLibrary;
