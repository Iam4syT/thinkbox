/**
 * @module OKRView
 * @description OKR objectives and key results tracker with progress bars.
 */
import * as api from '../services/api.js';

export class OKRView {
  constructor() {
    this.container = null;
    this.objectives = [];
  }

  mount(mountId) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    if (!this.container) return;
    this._render();
    this.refresh();
  }

  async refresh() {
    try {
      const res = await api.getObjectives();
      this.objectives = res.data || [];
      this._renderObjectives();
    } catch (err) {
      console.error('[OKRView] refresh failed:', err.message);
    }
  }

  _render() {
    this.container.innerHTML = `
      <div class="glass-card okr-view">
        <div class="okr-header">
          <div>
            <h3>🎯 Objectives & Key Results</h3>
            <p class="text-muted" style="font-size:0.8rem;margin-top:2px;">Track your content strategy goals</p>
          </div>
          <button id="okr-add-btn" class="btn btn--primary btn--sm btn--glow">+ New Objective</button>
        </div>
        <div id="okr-list" class="okr-list">
          <div class="queue-empty">Loading...</div>
        </div>
      </div>

      <!-- Add Objective Modal -->
      <div id="okr-modal" class="modal-overlay hidden">
        <div class="modal-card glass-card">
          <h4>Create Objective</h4>
          <div class="form-group" style="margin-top:1rem;">
            <label class="form-label">Objective Title *</label>
            <input type="text" id="okr-title" class="form-input" placeholder="e.g. Grow LinkedIn following to 10k" />
          </div>
          <div class="form-group">
            <label class="form-label">Description</label>
            <textarea id="okr-desc" class="form-input" rows="2" placeholder="What does success look like?"></textarea>
          </div>
          <div class="form-group">
            <label class="form-label">Target Date</label>
            <input type="date" id="okr-date" class="form-input" />
          </div>
          <div class="modal-actions">
            <button id="okr-cancel-btn" class="btn btn--ghost">Cancel</button>
            <button id="okr-save-btn" class="btn btn--primary">Create Objective</button>
          </div>
        </div>
      </div>
    `;

    document.getElementById('okr-add-btn')?.addEventListener('click', () => {
      document.getElementById('okr-modal')?.classList.remove('hidden');
    });
    document.getElementById('okr-cancel-btn')?.addEventListener('click', () => {
      document.getElementById('okr-modal')?.classList.add('hidden');
    });
    document.getElementById('okr-save-btn')?.addEventListener('click', () => this._createObjective());
  }

  _renderObjectives() {
    const el = document.getElementById('okr-list');
    if (!el) return;

    if (!this.objectives.length) {
      el.innerHTML = `
        <div class="queue-empty">
          <div style="font-size:2.5rem;margin-bottom:0.5rem;">🎯</div>
          <p>No objectives yet.</p>
          <p class="text-muted" style="font-size:0.8rem;">Create your first OKR to start tracking your content strategy.</p>
        </div>
      `;
      return;
    }

    el.innerHTML = '';
    this.objectives.forEach(obj => {
      const progress = obj.progress || 0;
      const progressColor = progress >= 70 ? '#22c55e' : progress >= 40 ? '#eab308' : '#7c3aed';
      const krs = obj.key_results || [];

      const card = document.createElement('div');
      card.className = 'okr-card';
      card.innerHTML = `
        <div class="okr-card-header">
          <div class="okr-card-title">
            <span class="okr-icon">🎯</span>
            <span>${this._esc(obj.title)}</span>
          </div>
          <div class="okr-progress-label" style="color:${progressColor};">
            ${progress.toFixed(0)}%
          </div>
        </div>

        ${obj.description ? `<p class="okr-description">${this._esc(obj.description)}</p>` : ''}

        <div class="progress-bar-container">
          <div class="progress-bar" style="width:${progress}%;background:${progressColor};"></div>
        </div>

        ${obj.target_date ? `<p class="text-muted" style="font-size:0.75rem;margin-top:0.25rem;">Target: ${obj.target_date}</p>` : ''}

        <div class="kr-list" id="kr-list-${obj.id}">
          ${krs.map(kr => this._renderKR(kr, obj.id)).join('')}
        </div>

        <div class="okr-actions">
          <button class="btn btn--ghost btn--xs okr-add-kr-btn" data-id="${obj.id}">+ Add Key Result</button>
          <button class="btn btn--ghost btn--xs okr-delete-btn" data-id="${obj.id}" style="color:#ef4444;">Delete</button>
        </div>
      `;

      card.querySelector('.okr-add-kr-btn')?.addEventListener('click', () => this._showAddKR(obj.id));
      card.querySelector('.okr-delete-btn')?.addEventListener('click', () => this._deleteObjective(obj.id));

      el.appendChild(card);
    });
  }

  _renderKR(kr, objectiveId) {
    const pct = kr.target_value > 0 ? Math.min(100, (kr.current_value / kr.target_value) * 100) : 0;
    const color = pct >= 70 ? '#22c55e' : pct >= 40 ? '#eab308' : '#7c3aed';
    return `
      <div class="kr-item">
        <div class="kr-header">
          <span class="kr-title">${this._esc(kr.title)}</span>
          <span class="kr-value" style="color:${color};">${kr.current_value}/${kr.target_value} ${kr.unit || ''}</span>
        </div>
        <div class="progress-bar-container" style="height:4px;">
          <div class="progress-bar" style="width:${pct}%;background:${color};"></div>
        </div>
      </div>
    `;
  }

  async _createObjective() {
    const title = document.getElementById('okr-title')?.value.trim();
    const desc = document.getElementById('okr-desc')?.value.trim();
    const date = document.getElementById('okr-date')?.value;

    if (!title) return;
    try {
      await api.createObjective({ title, description: desc, target_date: date });
      document.getElementById('okr-modal')?.classList.add('hidden');
      document.getElementById('okr-title').value = '';
      document.getElementById('okr-desc').value = '';
      this.refresh();
    } catch (err) {
      console.error('[OKRView] create objective failed:', err.message);
    }
  }

  async _deleteObjective(id) {
    if (!confirm('Delete this objective and all its key results?')) return;
    try {
      await api.deleteObjective(id);
      this.refresh();
    } catch (err) {
      console.error('[OKRView] delete failed:', err.message);
    }
  }

  _showAddKR(objectiveId) {
    const title = prompt('Key Result title:');
    if (!title) return;
    const metric = prompt('Metric type (e.g. posts_per_week, engagement_rate, followers):');
    if (!metric) return;
    const target = parseFloat(prompt('Target value:') || '0');
    const unit = prompt('Unit (e.g. posts, %, followers) — optional:') || '';
    api.addKeyResult(objectiveId, { title, metric_type: metric, target_value: target, unit })
      .then(() => this.refresh())
      .catch(err => console.error('[OKRView] add KR failed:', err.message));
  }

  _esc(str) {
    const d = document.createElement('div');
    d.textContent = str || '';
    return d.innerHTML;
  }
}

export default OKRView;
