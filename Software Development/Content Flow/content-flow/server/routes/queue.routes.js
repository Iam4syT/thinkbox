/**
 * @module queue.routes
 * @description Queue management and scheduling routes.
 */
import { Router } from 'express';

const router = Router();

/** GET /api/queue — Get all queue items */
router.get('/queue', (req, res, next) => {
  try {
    const { platform, status } = req.query;
    const items = req.queueRepo.findAll({ platform, status });
    // Enrich with adapted content preview
    const enriched = items.map(item => {
      try {
        const ac = req.analyticsRepo.getAdaptedContentById(item.adapted_content_id);
        return { ...item, preview: ac ? ac.adapted_text.substring(0, 120) + '...' : '', metadata_content: ac?.metadata };
      } catch (_) { return item; }
    });
    res.json({ data: enriched, stats: req.queueRepo.getStats() });
  } catch (err) { next(err); }
});

/** POST /api/queue — Add to queue */
router.post('/queue', (req, res, next) => {
  try {
    const { adapted_content_id, platform, journey_id, priority } = req.body;
    if (!adapted_content_id || !platform) {
      return res.status(400).json({ error: 'adapted_content_id and platform are required' });
    }
    const item = req.services.automationEngine.addToQueue(adapted_content_id, platform, { journey_id });
    res.status(201).json({ data: item });
  } catch (err) { next(err); }
});

/** PUT /api/queue/reorder — Reorder queue */
router.put('/queue/reorder', (req, res, next) => {
  try {
    const { order } = req.body;
    if (!Array.isArray(order)) return res.status(400).json({ error: 'order array is required' });
    const items = order.map((id, idx) => ({ id, priority: order.length - idx }));
    req.queueRepo.reorder(items);
    res.json({ data: { reordered: true } });
  } catch (err) { next(err); }
});

/** POST /api/queue/auto-schedule — AI auto-schedule all pending items */
router.post('/queue/auto-schedule', async (req, res, next) => {
  try {
    const { platform } = req.body;
    const results = await req.services.automationEngine.autoSchedule(platform);
    res.json({ data: results });
  } catch (err) { next(err); }
});

/** GET /api/queue/:id — Get single queue item */
router.get('/queue/:id', (req, res, next) => {
  try {
    const item = req.queueRepo.findById(req.params.id);
    if (!item) return res.status(404).json({ error: 'Queue item not found' });
    res.json({ data: item });
  } catch (err) { next(err); }
});

/** PUT /api/queue/:id — Update queue item */
router.put('/queue/:id', (req, res, next) => {
  try {
    const item = req.queueRepo.findById(req.params.id);
    if (!item) return res.status(404).json({ error: 'Queue item not found' });
    const updated = req.queueRepo.update(req.params.id, req.body);
    res.json({ data: updated });
  } catch (err) { next(err); }
});

/** DELETE /api/queue/:id — Remove from queue */
router.delete('/queue/:id', (req, res, next) => {
  try {
    const deleted = req.queueRepo.delete(req.params.id);
    if (!deleted) return res.status(404).json({ error: 'Queue item not found' });
    res.json({ data: { deleted: true } });
  } catch (err) { next(err); }
});

/** POST /api/queue/:id/pause — Pause a scheduled post */
router.post('/queue/:id/pause', (req, res, next) => {
  try {
    const updated = req.queueRepo.update(req.params.id, { status: 'paused' });
    if (!updated) return res.status(404).json({ error: 'Queue item not found' });
    res.json({ data: updated });
  } catch (err) { next(err); }
});

/** POST /api/queue/:id/resume — Resume a paused post */
router.post('/queue/:id/resume', (req, res, next) => {
  try {
    const updated = req.queueRepo.update(req.params.id, { status: 'pending' });
    if (!updated) return res.status(404).json({ error: 'Queue item not found' });
    res.json({ data: updated });
  } catch (err) { next(err); }
});

/** POST /api/queue/:id/schedule — Schedule a specific post */
router.post('/queue/:id/schedule', (req, res, next) => {
  try {
    const { scheduled_time } = req.body;
    if (!scheduled_time) return res.status(400).json({ error: 'scheduled_time is required' });
    const updated = req.queueRepo.update(req.params.id, { scheduled_time, status: 'scheduled' });
    if (!updated) return res.status(404).json({ error: 'Queue item not found' });
    res.json({ data: updated });
  } catch (err) { next(err); }
});

export default router;
