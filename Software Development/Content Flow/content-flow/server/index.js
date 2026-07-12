/**
 * @module server/index.js
 * @description ContentFlow Express API server — entry point.
 * Initializes all services, wires dependencies, and mounts routes.
 */
import express from 'express';
import cors from 'cors';
import config from './config.js';
import { getDatabase } from './db/database.js';

// ─── Repositories ──────────────────────────────────────────────
import contentRepo from './db/repositories/ContentRepository.js';
import analyticsRepo from './db/repositories/AnalyticsRepository.js';
import feedbackRepo from './db/repositories/FeedbackRepository.js';
import learningRepo from './db/repositories/LearningRepository.js';
import queueRepo from './db/repositories/QueueRepository.js';
import okrRepo from './db/repositories/OKRRepository.js';

// ─── AI Layer ──────────────────────────────────────────────────
import { AIProviderFactory } from './ai/AIProviderFactory.js';

// ─── Platform Adapters ─────────────────────────────────────────
import { PlatformRegistry } from './adapters/PlatformRegistry.js';

// ─── Services ─────────────────────────────────────────────────
import { RefinementService } from './services/RefinementService.js';
import { SuggestionEngine } from './services/SuggestionEngine.js';
import { EngagementScorer } from './services/EngagementScorer.js';
import { ContentPipeline } from './services/ContentPipeline.js';

// ─── Automation ────────────────────────────────────────────────
import { QueueManager } from './automation/QueueManager.js';
import { TimingOptimizer } from './automation/TimingOptimizer.js';
import { JourneyPlanner } from './automation/JourneyPlanner.js';
import { PostScheduler } from './automation/PostScheduler.js';
import { AutomationEngine } from './automation/AutomationEngine.js';

// ─── Analytics ─────────────────────────────────────────────────
import { AnalyticsService } from './analytics/AnalyticsService.js';
import { OKREngine } from './analytics/OKREngine.js';

// ─── Routes ────────────────────────────────────────────────────
import contentRoutes from './routes/content.routes.js';
import queueRoutes from './routes/queue.routes.js';
import analyticsRoutes from './routes/analytics.routes.js';
import okrRoutes from './routes/okr.routes.js';
import journeyRoutes from './routes/journey.routes.js';

// ═══════════════════════════════════════════════════════════════
// INITIALIZATION
// ═══════════════════════════════════════════════════════════════

const app = express();

// Initialise DB (runs migrations)
const db = getDatabase();
console.log('[ContentFlow] Database initialized');

// AI Provider
const aiProvider = AIProviderFactory.create('openai');
if (!config.hasValidApiKey) {
  console.warn('[ContentFlow] ⚠️  No OPENAI_API_KEY set — AI features will return mock responses');
} else {
  console.log(`[ContentFlow] ✅ OpenAI connected (model: ${config.openaiModel})`);
}

// Platform Registry (auto-registers LinkedIn, Instagram, YouTube)
const platformRegistry = new PlatformRegistry();

// Services
const refinementService = new RefinementService(aiProvider);
const suggestionEngine = new SuggestionEngine(aiProvider);
const engagementScorer = new EngagementScorer(aiProvider);

const contentPipeline = new ContentPipeline({
  aiProvider,
  platformRegistry,
  refinementService,
  suggestionEngine,
  engagementScorer,
  contentRepo,
  analyticsRepo,
  learningRepo,
});

// Automation
const queueManager = new QueueManager(queueRepo);
const timingOptimizer = new TimingOptimizer(aiProvider);
const journeyPlanner = new JourneyPlanner(aiProvider, analyticsRepo, queueRepo);
const postScheduler = new PostScheduler(queueManager);

const automationEngine = new AutomationEngine({
  queueManager,
  postScheduler,
  timingOptimizer,
  journeyPlanner,
});

// Analytics
const analyticsService = new AnalyticsService(analyticsRepo, queueRepo);
const okrEngine = new OKREngine(okrRepo, queueRepo, analyticsRepo);

// ═══════════════════════════════════════════════════════════════
// MIDDLEWARE
// ═══════════════════════════════════════════════════════════════

app.use(cors(config.cors));
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true }));

// Attach services and repos to every request
app.use((req, _res, next) => {
  req.db = db;
  req.contentRepo = contentRepo;
  req.analyticsRepo = analyticsRepo;
  req.feedbackRepo = feedbackRepo;
  req.learningRepo = learningRepo;
  req.queueRepo = queueRepo;
  req.okrRepo = okrRepo;
  req.services = {
    contentPipeline,
    automationEngine,
    analyticsService,
    okrEngine,
    journeyPlanner,
    engagementScorer,
  };
  next();
});

// Request logger (dev only)
if (config.isDev) {
  app.use((req, _res, next) => {
    console.log(`[API] ${req.method} ${req.path}`);
    next();
  });
}

// ═══════════════════════════════════════════════════════════════
// ROUTES
// ═══════════════════════════════════════════════════════════════

app.use('/api', contentRoutes);
app.use('/api', queueRoutes);
app.use('/api', analyticsRoutes);
app.use('/api', okrRoutes);
app.use('/api', journeyRoutes);

// ─── Utility endpoints ─────────────────────────────────────────

/** GET / — Landing page */
app.get('/', (_req, res) => {
  res.send(`<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ContentFlow API</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:'Segoe UI',system-ui,sans-serif;background:#0f0f13;color:#e2e8f0;min-height:100vh;padding:2rem}
    header{text-align:center;padding:3rem 1rem 2rem}
    header h1{font-size:2.4rem;font-weight:700;background:linear-gradient(135deg,#6ee7b7,#3b82f6);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
    header p{color:#94a3b8;margin-top:.5rem;font-size:1rem}
    .badge{display:inline-flex;align-items:center;gap:.4rem;background:#1e293b;border:1px solid #334155;border-radius:999px;padding:.3rem .9rem;font-size:.8rem;color:#6ee7b7;margin-top:1rem}
    .badge span{width:8px;height:8px;border-radius:50%;background:#6ee7b7;animation:pulse 1.5s infinite}
    @keyframes pulse{0%,100%{opacity:1}50%{opacity:.3}}
    .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1.2rem;max-width:1100px;margin:0 auto 3rem}
    .card{background:#1a1a24;border:1px solid #2d2d3d;border-radius:12px;padding:1.4rem;transition:border-color .2s,transform .2s}
    .card:hover{border-color:#3b82f6;transform:translateY(-2px)}
    .card h2{font-size:.85rem;font-weight:600;text-transform:uppercase;letter-spacing:.08em;color:#64748b;margin-bottom:1rem}
    .route{display:flex;align-items:center;gap:.6rem;padding:.45rem 0;border-bottom:1px solid #1e293b;font-size:.85rem}
    .route:last-child{border-bottom:none}
    .method{font-size:.7rem;font-weight:700;padding:.2rem .5rem;border-radius:4px;min-width:46px;text-align:center;letter-spacing:.04em}
    .GET{background:#0f3a2a;color:#6ee7b7}.POST{background:#1a2a4a;color:#60a5fa}
    .PUT{background:#2a2a10;color:#facc15}.DELETE{background:#3a1010;color:#f87171}
    .path{color:#cbd5e1;font-family:'Courier New',monospace}
    .ai-tag{font-size:.65rem;background:#2d1b4e;color:#a78bfa;border-radius:4px;padding:.1rem .4rem;margin-left:auto;white-space:nowrap}
    footer{text-align:center;color:#475569;font-size:.8rem;padding:1rem}
  </style>
</head>
<body>
<header>
  <h1>⚡ ContentFlow API</h1>
  <p>AI-Powered Cross-Platform Content Repurposing Engine</p>
  <div class="badge"><span></span> OpenAI connected &nbsp;·&nbsp; model: ${config.openaiModel} &nbsp;·&nbsp; port ${config.port}</div>
</header>
<div class="grid">

  <div class="card">
    <h2>🔧 Utility</h2>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/health</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/platforms</span></div>
  </div>

  <div class="card">
    <h2>📝 Content</h2>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/content</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/content</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/content/:id</span></div>
    <div class="route"><span class="method PUT">PUT</span><span class="path">/api/content/:id</span></div>
    <div class="route"><span class="method DELETE">DELETE</span><span class="path">/api/content/:id</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/content/:id/refine</span><span class="ai-tag">✦ AI</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/content/:id/adapt</span><span class="ai-tag">✦ AI</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/content/:id/adaptations</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/content/:id/suggestions</span><span class="ai-tag">✦ AI</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/content/:id/feedback</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/content/:id/feedback</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/content/:id/score</span><span class="ai-tag">✦ AI</span></div>
  </div>

  <div class="card">
    <h2>📊 Analytics</h2>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/analytics/overview</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/analytics/engagement-trend</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/analytics/platform-comparison</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/analytics/recent-performance</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/analytics/evolution</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/analytics/audience</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/analytics/metrics</span></div>
  </div>

  <div class="card">
    <h2>📅 Queue</h2>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/queue</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/queue</span></div>
    <div class="route"><span class="method PUT">PUT</span><span class="path">/api/queue/reorder</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/queue/auto-schedule</span><span class="ai-tag">✦ AI</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/queue/:id</span></div>
    <div class="route"><span class="method PUT">PUT</span><span class="path">/api/queue/:id</span></div>
    <div class="route"><span class="method DELETE">DELETE</span><span class="path">/api/queue/:id</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/queue/:id/pause</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/queue/:id/resume</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/queue/:id/schedule</span></div>
  </div>

  <div class="card">
    <h2>🗺️ Journeys</h2>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/journeys</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/journeys</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/journeys/:id</span></div>
    <div class="route"><span class="method DELETE">DELETE</span><span class="path">/api/journeys/:id</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/journeys/:id/analyze-gaps</span><span class="ai-tag">✦ AI</span></div>
  </div>

  <div class="card">
    <h2>🎯 OKRs</h2>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/okr/objectives</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/okr/objectives</span></div>
    <div class="route"><span class="method PUT">PUT</span><span class="path">/api/okr/objectives/:id</span></div>
    <div class="route"><span class="method DELETE">DELETE</span><span class="path">/api/okr/objectives/:id</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/okr/objectives/:id/key-results</span></div>
    <div class="route"><span class="method POST">POST</span><span class="path">/api/okr/objectives/:id/key-results</span></div>
    <div class="route"><span class="method PUT">PUT</span><span class="path">/api/okr/objectives/:objectiveId/key-results/:krId</span></div>
    <div class="route"><span class="method GET">GET</span><span class="path">/api/okr/recommendations</span></div>
  </div>

</div>
<footer>ContentFlow v1.0.0 &nbsp;·&nbsp; <a href="/api/health" style="color:#3b82f6">health check</a></footer>
</body>
</html>`);
});

/** GET /api/health */
app.get('/api/health', (_req, res) => {
  res.json({
    status: 'ok',
    version: '1.0.0',
    ai: config.hasValidApiKey ? 'connected' : 'mock mode',
    platforms: platformRegistry.list(),
    timestamp: new Date().toISOString(),
  });
});

/** GET /api/platforms */
app.get('/api/platforms', (_req, res) => {
  res.json({ data: platformRegistry.listConfigs() });
});

// ─── 404 handler ──────────────────────────────────────────────
app.use((_req, res) => {
  res.status(404).json({ error: 'Route not found' });
});

// ─── Global error handler ─────────────────────────────────────
app.use((err, _req, res, _next) => {
  console.error('[ContentFlow Error]', err.message);
  if (config.isDev) console.error(err.stack);
  res.status(err.status || 500).json({
    error: err.message || 'Internal server error',
    ...(config.isDev && { stack: err.stack }),
  });
});

// ═══════════════════════════════════════════════════════════════
// START
// ═══════════════════════════════════════════════════════════════

app.listen(config.port, () => {
  console.log(`\n🚀 ContentFlow API running at http://localhost:${config.port}`);
  console.log(`   Health: http://localhost:${config.port}/api/health`);
  console.log(`   Platforms: http://localhost:${config.port}/api/platforms\n`);
  automationEngine.start();
});

export default app;
