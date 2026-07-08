/**
 * @module QueueView
 * @description Drag-and-drop post queue with scheduling and status management.
 */
import { $, formatDate, formatTime } from '../utils/dom.js';
import * as api from '../services/api.js';

const STATUS_CONFIG = {
  pending: { label: 'Pending', color: '#6b6890', icon: '⏳' },
  scheduled: { label: 'Scheduled', color: '#7c3aed', icon: '📅' },
  published: { label: 'Published', color: '#22c55e', icon: '✅' },
  failed: { label: 'Failed', color: '#ef4444', icon: '❌' },
  paused: { label: 'Paused', color: '#eab308', icon: '⏸' },
};

const PLATFORM_CONFIG = {
  linkedin: { label: 'LinkedIn', icon: 'in', color: '#0077B5' },
  instagram: { label: 'Instagram', icon: '📷', color: '#E1306C' },
  youtube: { label: 'YouTube', icon: '▶', color: '#FF0000' },
};

export class QueueView {
  constructor() {
    this.container = null;
    this.items = [];
    this.stats = {};
    this._filter = 'all';
  }

  mount(mountId) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    if (!this.container) return;
    this._render();
    this.refresh();
    document.addEventListener('contentflow:queue-updated', () => this.refresh());
  }

  async refresh() {
    try {
      const res = await api.getQueue();
      this.items = res.data || [];
      this.stats = res.stats || {};
      this._renderList();
      this._renderStats();
    } catch (err) {
      console.error('[QueueView] refresh failed:', err.message);
    }
  }

  _render() {
    this.container.innerHTML = `
      <div class="glass-card queue-view" id="queue-card">
        <div class="queue-header">
          <div>
            <h3>📋 Content Queue</h3>
            <p class="text-muted" style="font-size:0.8rem;margin-top:2px;">Manage and schedule your posts</p>
          </div>
          <div class="queue-header-actions">
            <button id="q-auto-schedule-btn" class="btn btn--primary btn--sm btn--glow">
              ⚡ Auto-Schedule All
            </button>
            <button id="q-refresh-btn" class="btn btn--ghost btn--sm">🔄</button>
          </div>
        </div>

        <!-- Stats row -->
        <div id="q-stats" class="queue-stats-row"></div>

        <!-- Filters -->
        <div class="queue-filters">
          ${['all', 'pending', 'scheduled', 'published'].map(f => `
            <button class="filter-tab ${f === this._filter ? 'active' : ''}" data-filter="${f}">
              ${f.charAt(0).toUpperCase() + f.slice(1)}
            </button>
          `).join('')}
        </div>

        <!-- Queue list -->
        <div id="q-list" class="queue-list">
          <div class="queue-empty">Loading...</div>
        </div>
      </div>
    `;

    this.container.querySelectorAll('.filter-tab').forEach(btn => {
      btn.addEventListener('click', () => {
        this._filter = btn.dataset.filter;
        this.container.querySelectorAll('.filter-tab').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this._renderList();
      });
    });

    document.getElementById('q-auto-schedule-btn')?.addEventListener('click', () => this._autoSchedule());
    document.getElementById('q-refresh-btn')?.addEventListener('click', () => this.refresh());
  }

  _renderStats() {
    const el = document.getElementById('q-stats');
    if (!el) return;
    const s = this.stats;
    el.innerHTML = `
      <div class="stat-chip"><span>${s.pending || 0}</span> Pending</div>
      <div class="stat-chip" style="color:#7c3aed;"><span>${s.scheduled || 0}</span> Scheduled</div>
      <div class="stat-chip" style="color:#22c55e;"><span>${s.published || 0}</span> Published</div>
      <div class="stat-chip"><span>${s.total || 0}</span> Total</div>
    `;
  }

  _renderList() {
    const el = document.getElementById('q-list');
    if (!el) return;

    let items = this.items;
    if (this._filter !== 'all') {
      items = items.filter(i => i.status === this._filter);
    }

    if (!items.length) {
      el.innerHTML = `
        <div class="queue-empty">
          <div style="font-size:2.5rem;margin-bottom:0.5rem;">📭</div>
          <p>No posts in queue${this._filter !== 'all' ? ` with status "${this._filter}"` : ''}.</p>
          <p class="text-muted" style="font-size:0.8rem;">Create content and add adaptations to your queue.</p>
        </div>
      `;
      return;
    }

    el.innerHTML = '';
    items.forEach(item => {
      const status = STATUS_CONFIG[item.status] || STATUS_CONFIG.pending;
      const platform = PLATFORM_CONFIG[item.platform] || {};
      const card = document.createElement('div');
      card.className = `queue-item queue-item--${item.status}`;
      card.dataset.id = item.id;

      card.innerHTML = `
        <div class="queue-item-drag">⠿</div>
        <div class="queue-item-platform" style="color:${platform.color};" title="${platform.label}">
          ${platform.icon || '📝'}
        </div>
        <div class="queue-item-body">
          <div class="queue-item-preview">${this._esc(item.preview || '(No preview)')}</div>
          ${item.scheduled_time ? `<div class="queue-item-time">📅 ${formatDate(item.scheduled_time)} ${formatTime(item.scheduled_time)}</div>` : ''}
        </div>
        <div class="queue-item-status">
          <span class="status-badge" style="color:${status.color};">${status.icon} ${status.label}</span>
        </div>
        <div class="queue-item-actions">
          ${item.status === 'pending' ? `
            <button class="btn btn--ghost btn--xs q-schedule-btn" data-id="${item.id}" title="Set time">📅</button>
          ` : ''}
          ${item.status === 'scheduled' ? `
            <button class="btn btn--ghost btn--xs q-pause-btn" data-id="${item.id}" title="Pause">⏸</button>
          ` : ''}
          ${item.status === 'paused' ? `
            <button class="btn btn--ghost btn--xs q-resume-btn" data-id="${item.id}" title="Resume">▶</button>
          ` : ''}
          <button class="btn btn--ghost btn--xs q-delete-btn" data-id="${item.id}" title="Remove" style="color:#ef4444;">✕</button>
        </div>
      `;

      card.querySelector('.q-delete-btn')?.addEventListener('click', () => this._deleteItem(item.id));
      card.querySelector('.q-pause-btn')?.addEventListener('click', () => this._pauseItem(item.id));
      card.querySelector('.q-resume-btn')?.addEventListener('click', () => this._resumeItem(item.id));
      card.querySelector('.q-schedule-btn')?.addEventListener('click', () => this._showScheduler(item.id));

      el.appendChild(card);
    });
  }

  async _autoSchedule() {
    const btn = document.getElementById('q-auto-schedule-btn');
    btn.disabled = true;
    btn.textContent = '⏳ Scheduling...';
    try {
      await api.autoSchedule({});
      await this.refresh();
    } catch (err) {
      console.error('[QueueView] auto-schedule failed:', err.message);
    } finally {
      btn.disabled = false;
      btn.textContent = '⚡ Auto-Schedule All';
    }
  }

  async _deleteItem(id) {
    if (!confirm('Remove this post from the queue?')) return;
    try {
      await api.deleteQueueItem(id);
      this.refresh();
    } catch (err) {
      console.error('[QueueView] delete failed:', err.message);
    }
  }

  async _pauseItem(id) {
    try {
      await api.pauseQueueItem(id);
      this.refresh();
    } catch (err) {
      console.error('[QueueView] pause failed:', err.message);
    }
  }

  async _resumeItem(id) {
    try {
      await api.resumeQueueItem(id);
      this.refresh();
    } catch (err) {
      console.error('[QueueView] resume failed:', err.message);
    }
  }

  _showScheduler(id) {
    const time = prompt('Enter scheduling time (YYYY-MM-DD HH:MM):');
    if (!time) return;
    const isoTime = new Date(time).toISOString();
    api.scheduleQueueItem(id, { scheduled_time: isoTime })
      .then(() => this.refresh())
      .catch(err => console.error('[QueueView] schedule failed:', err.message));
  }

  _esc(str) {
    const d = document.createElement('div');
    d.textContent = str || '';
    return d.innerHTML;
  }
}

export default QueueView;
