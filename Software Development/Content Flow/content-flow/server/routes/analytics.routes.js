/**
 * @module analytics.routes
 * @description Analytics dashboard, metrics, evolution, and audience routes.
 */
import { Router } from 'express';
import { v4 as uuidv4 } from 'uuid';

const router = Router();

/** GET /api/analytics/overview — Dashboard stats */
router.get('/analytics/overview', (req, res, next) => {
  try {
    const overview = req.services.analyticsService.getOverview();
    res.json({ data: overview });
  } catch (err) { next(err); }
});

/** GET /api/analytics/engagement-trend — Trend data for charting */
router.get('/analytics/engagement-trend', (req, res, next) => {
  try {
    const days = parseInt(req.query.days) || 30;
    const trend = req.services.analyticsService.getEngagementTrend(days);
    res.json({ data: trend });
  } catch (err) { next(err); }
});

/** GET /api/analytics/platform-comparison — Per-platform stats */
router.get('/analytics/platform-comparison', (req, res, next) => {
  try {
    const comparison = req.services.analyticsService.getPlatformComparison();
    res.json({ data: comparison });
  } catch (err) { next(err); }
});

/** GET /api/analytics/recent-performance — Recent posts with metrics */
router.get('/analytics/recent-performance', (req, res, next) => {
  try {
    const limit = parseInt(req.query.limit) || 10;
    const recent = req.services.analyticsService.getRecentPerformance(limit);
    res.json({ data: recent });
  } catch (err) { next(err); }
});

/** GET /api/analytics/evolution — Evolution snapshots */
router.get('/analytics/evolution', (req, res, next) => {
  try {
    const snapshots = req.learningRepo.getSnapshotsByType('weekly', 12);
    res.json({ data: snapshots });
  } catch (err) { next(err); }
});

/** GET /api/analytics/audience — Audience profile for a platform */
router.get('/analytics/audience', (req, res, next) => {
  try {
    const { platform = 'linkedin' } = req.query;
    const profile = req.learningRepo.getAudienceProfile(platform);
    res.json({ data: profile });
  } catch (err) { next(err); }
});

/** POST /api/analytics/metrics — Log post performance metrics */
router.post('/analytics/metrics', (req, res, next) => {
  try {
    const { adapted_content_id, platform, impressions, clicks, likes, comments, shares, saves, reach } = req.body;
    if (!adapted_content_id || !platform) {
      return res.status(400).json({ error: 'adapted_content_id and platform are required' });
    }

    const likesN = likes || 0;
    const commentsN = comments || 0;
    const sharesN = shares || 0;
    const savesN = saves || 0;
    const reachN = reach || impressions || 1;
    const engagement_rate = parseFloat(((likesN + commentsN + sharesN + savesN) / reachN * 100).toFixed(2));

    const record = req.analyticsRepo.recordMetrics({
      id: uuidv4(),
      adapted_content_id,
      platform,
      impressions: impressions || 0,
      clicks: clicks || 0,
      likes: likesN,
      comments: commentsN,
      shares: sharesN,
      saves: savesN,
      engagement_rate,
      reach: reachN,
    });

    res.status(201).json({ data: record });
  } catch (err) { next(err); }
});

export default router;
