/**
 * @module main.js
 * @description ContentFlow frontend entry point — mounts all components, handles routing.
 */
import { BrainDumpEditor } from './components/BrainDumpEditor.js';
import { RefinedDraftView } from './components/RefinedDraftView.js';
import { PlatformAdaptations } from './components/PlatformAdaptations.js';
import { QueueView } from './components/QueueView.js';
import { AnalyticsDashboard } from './components/AnalyticsDashboard.js';
import { OKRView } from './components/OKRView.js';
import { ContentLibrary } from './components/ContentLibrary.js';

// ─── Router ──────────────────────────────────────────────────────────
const VIEWS = {
  dashboard: { title: 'Dashboard', icon: '📊' },
  create:    { title: 'Create Content', icon: '🧠' },
  queue:     { title: 'Content Queue', icon: '📤' },
  analytics: { title: 'Analytics', icon: '📈' },
  okr:       { title: 'OKR Tracker', icon: '🎯' },
  settings:  { title: 'Settings', icon: '⚙️' },
};

class Router {
  constructor() {
    this._current = null;
    this._handlers = {};
    window.addEventListener('hashchange', () => this._navigate());
    window.addEventListener('popstate', () => this._navigate());
  }

  on(view, fn) { this._handlers[view] = fn; return this; }

  navigate(view) {
    window.location.hash = view;
  }

  _navigate() {
    const hash = window.location.hash.slice(1) || 'dashboard';
    const view = Object.keys(VIEWS).includes(hash) ? hash : 'dashboard';

    if (this._current === view) return;
    this._current = view;

    // Update active nav
    document.querySelectorAll('.nav-item').forEach(el => {
      el.classList.toggle('active', el.dataset.view === view);
    });

    // Show/hide views
    document.querySelectorAll('.view').forEach(el => {
      el.classList.toggle('view--active', el.dataset.view === view);
    });

    // Update title
    const titleEl = document.getElementById('view-title');
    if (titleEl) {
      const cfg = VIEWS[view];
      titleEl.textContent = `${cfg.icon} ${cfg.title}`;
    }

    // Run view handler
    if (this._handlers[view]) this._handlers[view]();
  }

  start() {
    this._navigate();
  }
}

// ─── Toast Notifications ─────────────────────────────────────────────
function toast(message, type = 'info', duration = 4000) {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const el = document.createElement('div');
  el.className = `toast toast--${type}`;
  el.innerHTML = `<span>${message}</span><button class="toast-close">✕</button>`;
  container.appendChild(el);

  const close = () => {
    el.classList.add('toast--exit');
    setTimeout(() => el.remove(), 300);
  };

  el.querySelector('.toast-close').addEventListener('click', close);
  setTimeout(close, duration);

  // Animate in
  requestAnimationFrame(() => el.classList.add('toast--in'));
}

// ─── Component Initialization ─────────────────────────────────────────
const router = new Router();

// Create
const brainDump = new BrainDumpEditor();
const refinedDraft = new RefinedDraftView();
const platformAdaptations = new PlatformAdaptations();

// Queue
const queueView = new QueueView();

// Analytics
const analyticsDashboard = new AnalyticsDashboard();

// OKR
const okrView = new OKRView();

// Content Library (sidebar of create view)
const contentLibrary = new ContentLibrary();

// ─── Mount Components ─────────────────────────────────────────────────
function mountAll() {
  // Dashboard
  analyticsDashboard.mount('mount-analytics-dashboard');

  // Create view
  brainDump.mount('mount-brain-dump');
  refinedDraft.mount('mount-refined-draft');
  platformAdaptations.mount('mount-adaptation-preview');

  // Queue view
  queueView.mount('mount-queue-manager');

  // Analytics view — second instance
  const analyticsFullEl = document.getElementById('mount-analytics-full');
  if (analyticsFullEl) {
    const analyticsFull = new AnalyticsDashboard();
    analyticsFull.mount('mount-analytics-full');
  }

  // OKR view
  okrView.mount('mount-okr-tracker');

  // Content Library in sidebar of create
  const libMount = document.getElementById('mount-suggestion-panel');
  if (libMount) {
    contentLibrary.mount('mount-suggestion-panel', {
      onSelect: (content) => {
        brainDump.loadContent(content);
        router.navigate('create');
        toast(`✅ Loaded: "${content.title || 'Untitled'}"`, 'success');
      }
    });
  }
}

// ─── Navigation ──────────────────────────────────────────────────────
document.querySelectorAll('.nav-item[data-view]').forEach(el => {
  el.addEventListener('click', (e) => {
    e.preventDefault();
    router.navigate(el.dataset.view);
  });
});

document.getElementById('btn-new-content')?.addEventListener('click', () => {
  router.navigate('create');
});

document.getElementById('sidebar-toggle')?.addEventListener('click', () => {
  document.getElementById('sidebar')?.classList.toggle('sidebar--collapsed');
});

// Theme toggle
document.getElementById('theme-select')?.addEventListener('change', (e) => {
  document.documentElement.setAttribute('data-theme', e.target.value);
  localStorage.setItem('cf-theme', e.target.value);
});

// Restore saved theme
const savedTheme = localStorage.getItem('cf-theme');
if (savedTheme) {
  document.documentElement.setAttribute('data-theme', savedTheme);
  const sel = document.getElementById('theme-select');
  if (sel) sel.value = savedTheme;
}

// ─── Global Event Listeners ──────────────────────────────────────────
document.addEventListener('contentflow:saved', (e) => {
  toast('💾 Draft saved!', 'success');
});

document.addEventListener('contentflow:queue-updated', () => {
  toast('📋 Queue updated!', 'success');
});

document.addEventListener('contentflow:load-content', (e) => {
  router.navigate('create');
});

// ─── Route Handlers ───────────────────────────────────────────────────
router
  .on('dashboard', () => analyticsDashboard.refresh())
  .on('queue', () => queueView.refresh())
  .on('analytics', () => {})
  .on('okr', () => okrView.refresh())
  .on('create', () => {})
  .on('settings', () => {});

// ─── Health Check ─────────────────────────────────────────────────────
async function checkHealth() {
  try {
    const res = await fetch('/api/health');
    if (res.ok) {
      const data = await res.json();
      const aiStatus = document.getElementById('ai-status');
      if (aiStatus) {
        aiStatus.textContent = data.ai === 'connected' ? '🟢 AI Connected' : '🟡 AI Mock Mode';
        aiStatus.title = data.ai;
      }
    }
  } catch (_) {
    toast('⚠️ Cannot reach ContentFlow API. Start the server with: npm run dev', 'error', 8000);
  }
}

// ─── Bootstrap ────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  mountAll();
  router.start();
  checkHealth();
});
