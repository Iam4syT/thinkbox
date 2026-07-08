/**
 * @module AnalyticsDashboard
 * @description Analytics view with charts, engagement trends, platform comparison.
 */
import { $, formatNumber } from '../utils/dom.js';
import { LineChart, BarChart, CircularProgress } from '../utils/charts.js';
import * as api from '../services/api.js';

export class AnalyticsDashboard {
  constructor() {
    this.container = null;
    this.charts = {};
    this._initialized = false;
  }

  mount(mountId) {
    this.container = typeof mountId === 'string' ? document.getElementById(mountId) : mountId;
    if (!this.container) return;
    this._render();
    this.refresh();
  }

  async refresh() {
    try {
      const [overviewRes, trendRes, platformRes] = await Promise.all([
        api.getAnalyticsOverview(),
        api.getEngagementTrend(30),
        api.getPlatformComparison(),
      ]);
      this._renderOverview(overviewRes.data || {});
      this._renderTrend(trendRes.data || []);
      this._renderPlatformComparison(platformRes.data || []);
    } catch (err) {
      console.error('[AnalyticsDashboard] refresh failed:', err.message);
    }
  }

  _render() {
    this.container.innerHTML = `
      <div class="analytics-dashboard">
        <!-- Overview KPI cards -->
        <div class="analytics-kpis" id="analytics-kpis">
          ${['total-posts', 'avg-engagement', 'top-platform', 'posts-week'].map(id => `
            <div class="kpi-card glass-card" id="kpi-${id}">
              <div class="kpi-skeleton"></div>
            </div>
          `).join('')}
        </div>

        <!-- Engagement Trend -->
        <div class="glass-card analytics-section">
          <h4 class="section-title">📈 Engagement Trend (30 Days)</h4>
          <div style="position:relative;height:220px;">
            <canvas id="engagement-chart"></canvas>
          </div>
        </div>

        <!-- Platform Comparison -->
        <div class="glass-card analytics-section">
          <h4 class="section-title">🏆 Platform Performance</h4>
          <div style="position:relative;height:220px;">
            <canvas id="platform-chart"></canvas>
          </div>
        </div>
      </div>
    `;

    // Init charts after DOM ready
    setTimeout(() => {
      const engCanvas = document.getElementById('engagement-chart');
      if (engCanvas) this.charts.engagement = new LineChart(engCanvas, { height: 220 });

      const platCanvas = document.getElementById('platform-chart');
      if (platCanvas) this.charts.platform = new BarChart(platCanvas, { height: 220 });
    }, 50);
  }

  _renderOverview(data) {
    const kpis = [
      {
        id: 'kpi-total-posts',
        icon: '📝',
        label: 'Total Posts',
        value: formatNumber(data.totalPosts || 0),
        sub: 'all time',
        color: '#7c3aed',
      },
      {
        id: 'kpi-avg-engagement',
        icon: '⚡',
        label: 'Avg Engagement',
        value: `${data.avgEngagementRate || 0}%`,
        sub: 'last 30 days',
        color: '#06b6d4',
      },
      {
        id: 'kpi-top-platform',
        icon: '🏆',
        label: 'Top Platform',
        value: data.topPlatform || '—',
        sub: 'by engagement',
        color: '#22c55e',
      },
      {
        id: 'kpi-posts-week',
        icon: '📅',
        label: 'This Week',
        value: formatNumber(data.postsThisWeek || 0),
        sub: 'posts published',
        color: '#eab308',
      },
    ];

    kpis.forEach(kpi => {
      const el = document.getElementById(kpi.id);
      if (!el) return;
      el.innerHTML = `
        <div class="kpi-icon" style="color:${kpi.color};">${kpi.icon}</div>
        <div class="kpi-value" style="color:${kpi.color};">${kpi.value}</div>
        <div class="kpi-label">${kpi.label}</div>
        <div class="kpi-sub">${kpi.sub}</div>
      `;
    });
  }

  _renderTrend(trendData) {
    if (!this.charts.engagement || !trendData.length) return;
    const labels = trendData.map(d => d.date.slice(5)); // MM-DD
    const values = trendData.map(d => d.score);
    this.charts.engagement.setData(labels, [{ label: 'Engagement', data: values, color: '#7c3aed' }]);
  }

  _renderPlatformComparison(platformData) {
    if (!this.charts.platform || !platformData.length) return;
    const labels = platformData.map(d => d.platform.charAt(0).toUpperCase() + d.platform.slice(1));
    const values = platformData.map(d => d.avgEngagement);
    const colors = platformData.map(d => {
      const cfg = { linkedin: '#0077B5', instagram: '#E1306C', youtube: '#FF0000' };
      return cfg[d.platform] || '#7c3aed';
    });
    this.charts.platform.setData(labels, values, colors);
  }
}

export default AnalyticsDashboard;
