/**
 * @module journey.routes
 * @description Content journey management routes.
 */
import { Router } from 'express';

const router = Router();

/** GET /api/journeys — List all journeys */
router.get('/journeys', (req, res, next) => {
  try {
    const journeys = req.analyticsRepo.getJourneys(req.query.platform);
    res.json({ data: journeys });
  } catch (err) { next(err); }
});

/** POST /api/journeys — Create journey */
router.post('/journeys', (req, res, next) => {
  try {
    const { title, description, platform } = req.body;
    if (!title) return res.status(400).json({ error: 'title is required' });
    const journey = req.services.journeyPlanner.create({ title, description, platform });
    res.status(201).json({ data: journey });
  } catch (err) { next(err); }
});

/** GET /api/journeys/:id — Get journey with queue items */
router.get('/journeys/:id', (req, res, next) => {
  try {
    const journey = req.analyticsRepo.getJourneyById(req.params.id);
    if (!journey) return res.status(404).json({ error: 'Journey not found' });
    // Get queue items for this journey
    const queueItems = req.queueRepo.findAll().filter(q => q.metadata?.journey_id === req.params.id);
    res.json({ data: { ...journey, queue_items: queueItems } });
  } catch (err) { next(err); }
});

/** DELETE /api/journeys/:id — Delete journey */
router.delete('/journeys/:id', (req, res, next) => {
  try {
    const journey = req.analyticsRepo.getJourneyById(req.params.id);
    if (!journey) return res.status(404).json({ error: 'Journey not found' });
    // Use db directly to delete
    req.db.prepare('DELETE FROM journeys WHERE id = ?').run(req.params.id);
    res.json({ data: { deleted: true } });
  } catch (err) { next(err); }
});

/** POST /api/journeys/:id/analyze-gaps — AI gap analysis */
router.post('/journeys/:id/analyze-gaps', async (req, res, next) => {
  try {
    const analysis = await req.services.journeyPlanner.analyzeGaps(req.params.id);
    res.json({ data: analysis });
  } catch (err) { next(err); }
});

export default router;
