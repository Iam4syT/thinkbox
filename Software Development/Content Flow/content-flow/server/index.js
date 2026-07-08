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
const aiProvider = AIProviderFactory.create('gemini');
if (!config.hasValidApiKey) {
  console.warn('[ContentFlow] ⚠️  No GEMINI_API_KEY set — AI features will return mock responses');
} else {
  console.log(`[ContentFlow] ✅ Gemini AI connected (model: ${config.geminiModel})`);
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
