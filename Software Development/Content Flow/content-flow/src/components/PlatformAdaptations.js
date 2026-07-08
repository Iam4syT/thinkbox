/**
 * @module PlatformAdaptations
 * @description Displays platform-tailored content cards with hashtags, scores.
 */
import { $, formatNumber } from '../utils/dom.js';
import * as api from '../services/api.js';

const PLATFORM_CONFIG = {
  linkedin: { label: 'LinkedIn', icon: 'in', color: '#0077B5', charLimit: 3000 },
  instagram: { label: 'Instagram', icon: '📷', color: '#E1306C', charLimit: 2200 },
  youtube: { label: 'YouTube', icon: '▶', color: '#FF0000', charLimit: 5000 },
};

export class PlatformAdaptations {
  constructor() {
    this.container = null;
    this.contentId = null;
    this.adaptations = {};
    this._selectedPlatforms = ['linkedin', 'instagram', 'youtube'];
  }

  mount(mountId) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    if (!this.container) return;
    this._render();
    document.addEventListener('contentflow:refined', e => this._onRefined(e.detail));
  }

  _render() {
    this.container.innerHTML = `
      <div class="glass-card platform-adaptations hidden" id="pa-card">
        <div class="pa-header">
          <div>
            <h3>🎯 Platform Adaptations</h3>
            <p class="text-muted" style="font-size:0.8rem;margin-top:2px;">AI-tailored for each platform's unique audience</p>
          </div>
          <div class="pa-platform-select">
            ${Object.keys(PLATFORM_CONFIG).map(p => `
              <label class="platform-toggle ${this._selectedPlatforms.includes(p) ? 'active' : ''}" data-platform="${p}">
                <input type="checkbox" ${this._selectedPlatforms.includes(p) ? 'checked' : ''} value="${p}" style="display:none;">
                <span class="platform-icon" style="color:${PLATFORM_CONFIG[p].color}">${PLATFORM_CONFIG[p].icon}</span>
                ${PLATFORM_CONFIG[p].label}
              </label>
            `).join('')}
          </div>
        </div>
        <div class="pa-adapt-bar">
          <button id="pa-adapt-btn" class="btn btn--primary btn--glow" disabled>
            ✨ Generate Adaptations
          </button>
          <span id="pa-adapt-status" class="text-muted" style="font-size:0.8rem;"></span>
        </div>
        <div id="pa-cards" class="pa-platform-cards"></div>
      </div>
    `;

    // Platform toggles
    this.container.querySelectorAll('.platform-toggle').forEach(el => {
      el.addEventListener('click', () => {
        const platform = el.dataset.platform;
        const cb = el.querySelector('input[type=checkbox]');
        if (cb.checked) {
          this._selectedPlatforms = this._selectedPlatforms.filter(p => p !== platform);
        } else {
          this._selectedPlatforms.push(platform);
        }
        cb.checked = !cb.checked;
        el.classList.toggle('active', cb.checked);
      });
    });

    document.getElementById('pa-adapt-btn')?.addEventListener('click', () => this._adapt());
  }

  _onRefined({ contentId }) {
    this.contentId = contentId;
    const card = document.getElementById('pa-card');
    if (card) card.classList.remove('hidden');
    const btn = document.getElementById('pa-adapt-btn');
    if (btn) btn.disabled = false;
  }

  async _adapt() {
    if (!this.contentId) return;
    const platforms = this._selectedPlatforms;
    if (!platforms.length) return;

    const btn = document.getElementById('pa-adapt-btn');
    const status = document.getElementById('pa-adapt-status');
    btn.disabled = true;
    btn.textContent = '⏳ Generating...';
    if (status) status.textContent = 'AI is adapting your content for each platform...';

    try {
      const res = await api.adaptContent(this.contentId, platforms);
      const adaptations = res.data || [];
      adaptations.forEach(a => {
        if (!a.error) this.adaptations[a.platform] = a;
      });
      this._renderCards();
      if (status) status.textContent = `✅ ${adaptations.filter(a => !a.error).length} adaptations ready`;
      document.dispatchEvent(new CustomEvent('contentflow:adapted', { detail: { contentId: this.contentId, adaptations } }));
    } catch (err) {
      if (status) status.textContent = '❌ Failed: ' + (err.message || 'Server offline');
    } finally {
      btn.disabled = false;
      btn.textContent = '✨ Generate Adaptations';
    }
  }

  _renderCards() {
    const container = document.getElementById('pa-cards');
    if (!container) return;
    container.innerHTML = '';

    Object.entries(this.adaptations).forEach(([platform, data]) => {
      const cfg = PLATFORM_CONFIG[platform] || {};
      const meta = data.metadata || {};
      const hashtags = meta.hashtags || [];
      const engScore = data.engagement_score || 50;
      const scoreColor = engScore >= 70 ? '#22c55e' : engScore >= 50 ? '#eab308' : '#ef4444';

      const card = document.createElement('div');
      card.className = 'platform-card glass-card';
      card.setAttribute('data-platform', platform);
      card.innerHTML = `
        <div class="platform-card-header">
          <div class="platform-badge" style="background:${cfg.color}20;color:${cfg.color};border:1px solid ${cfg.color}40;">
            <span>${cfg.icon}</span> ${cfg.label}
          </div>
          <div class="platform-scores">
            <div class="score-chip" title="Engagement Score" style="color:${scoreColor}">
              ⚡ ${engScore}
            </div>
            <div class="score-chip" title="Hook Strength">
              🎯 ${meta.hook_strength || 'medium'}
            </div>
          </div>
        </div>

        ${meta.hook ? `<div class="platform-hook">💡 <em>${this._esc(meta.hook)}</em></div>` : ''}

        <div class="platform-content-text">${this._esc(data.adapted_text || '')}</div>

        ${hashtags.length ? `
          <div class="platform-hashtags">
            ${hashtags.slice(0, 10).map(h => `<span class="hashtag">#${h}</span>`).join('')}
            ${hashtags.length > 10 ? `<span class="hashtag hashtag--more">+${hashtags.length - 10}</span>` : ''}
          </div>
        ` : ''}

        <div class="platform-card-actions">
          <button class="btn btn--ghost btn--sm pa-copy-btn" data-id="${data.id}">📋 Copy</button>
          <button class="btn btn--primary btn--sm pa-queue-btn" data-id="${data.id}" data-platform="${platform}">+ Queue</button>
        </div>
      `;

      card.querySelector('.pa-copy-btn')?.addEventListener('click', () => {
        navigator.clipboard.writeText(data.adapted_text || '').then(() => {
          const btn = card.querySelector('.pa-copy-btn');
          btn.textContent = '✅ Copied!';
          setTimeout(() => (btn.textContent = '📋 Copy'), 2000);
        });
      });

      card.querySelector('.pa-queue-btn')?.addEventListener('click', () => {
        this._addToQueue(data.id, platform, card);
      });

      container.appendChild(card);
    });
  }

  async _addToQueue(adaptedContentId, platform, card) {
    const btn = card.querySelector('.pa-queue-btn');
    btn.disabled = true;
    btn.textContent = '⏳ Adding...';
    try {
      await api.addToQueue({ adapted_content_id: adaptedContentId, platform });
      btn.textContent = '✅ Queued!';
      btn.className = 'btn btn--ghost btn--sm';
      document.dispatchEvent(new CustomEvent('contentflow:queue-updated'));
    } catch (err) {
      btn.disabled = false;
      btn.textContent = '❌ Failed';
      setTimeout(() => { btn.textContent = '+ Queue'; btn.disabled = false; }, 2000);
    }
  }

  _esc(str) {
    const d = document.createElement('div');
    d.textContent = str || '';
    return d.innerHTML;
  }
}

export default PlatformAdaptations;
