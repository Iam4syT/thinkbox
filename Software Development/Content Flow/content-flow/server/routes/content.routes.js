/**
 * @module content.routes
 * @description Content CRUD, refinement, adaptation, suggestions, and feedback routes.
 */
import { Router } from 'express';
import { v4 as uuidv4 } from 'uuid';

const router = Router();

// ─── Content CRUD ────────────────────────────────────────────

/** POST /api/content — Save a brain dump */
router.post('/content', (req, res, next) => {
  try {
    const { raw_content, title, content_type } = req.body;
    if (!raw_content || raw_content.trim().length === 0) {
      return res.status(400).json({ error: 'raw_content is required' });
    }
    const record = req.contentRepo.create({
      id: uuidv4(),
      raw_content,
      title: title || null,
      content_type: content_type || 'brain_dump',
      status: 'draft',
    });
    res.status(201).json({ data: record });
  } catch (err) { next(err); }
});

/** GET /api/content — List all content */
router.get('/content', (req, res, next) => {
  try {
    const { status, content_type, limit, offset } = req.query;
    const items = req.contentRepo.findAll({
      status, content_type,
      limit: limit ? parseInt(limit) : undefined,
      offset: offset ? parseInt(offset) : undefined,
    });
    res.json({ data: items, count: items.length });
  } catch (err) { next(err); }
});

/** GET /api/content/:id — Get single content */
router.get('/content/:id', (req, res, next) => {
  try {
    const content = req.contentRepo.findById(req.params.id);
    if (!content) return res.status(404).json({ error: 'Content not found' });
    res.json({ data: content });
  } catch (err) { next(err); }
});

/** PUT /api/content/:id — Update content */
router.put('/content/:id', (req, res, next) => {
  try {
    const content = req.contentRepo.findById(req.params.id);
    if (!content) return res.status(404).json({ error: 'Content not found' });
    const updated = req.contentRepo.update(req.params.id, req.body);
    res.json({ data: updated });
  } catch (err) { next(err); }
});

/** DELETE /api/content/:id — Delete content */
router.delete('/content/:id', (req, res, next) => {
  try {
    const deleted = req.contentRepo.delete(req.params.id);
    if (!deleted) return res.status(404).json({ error: 'Content not found' });
    res.json({ data: { deleted: true } });
  } catch (err) { next(err); }
});

// ─── AI Pipeline ─────────────────────────────────────────────

/** POST /api/content/:id/refine — AI refine brain dump */
router.post('/content/:id/refine', async (req, res, next) => {
  try {
    const result = await req.services.contentPipeline.refine(req.params.id);
    res.json({ data: result });
  } catch (err) { next(err); }
});

/** POST /api/content/:id/adapt — AI adapt for platforms */
router.post('/content/:id/adapt', async (req, res, next) => {
  try {
    const { platforms } = req.body;
    if (!Array.isArray(platforms) || platforms.length === 0) {
      return res.status(400).json({ error: 'platforms array is required' });
    }
    const adaptations = await req.services.contentPipeline.adapt(req.params.id, platforms);
    res.json({ data: adaptations });
  } catch (err) { next(err); }
});

/** GET /api/content/:id/adaptations — Get all adaptations */
router.get('/content/:id/adaptations', (req, res, next) => {
  try {
    const adaptations = req.analyticsRepo.getAdaptationsByContentId(req.params.id);
    res.json({ data: adaptations });
  } catch (err) { next(err); }
});

/** POST /api/content/:id/suggestions — Get AI suggestions */
router.post('/content/:id/suggestions', async (req, res, next) => {
  try {
    const { platform } = req.body;
    const result = await req.services.contentPipeline.suggest(req.params.id, platform);
    res.json({ data: result });
  } catch (err) { next(err); }
});

/** POST /api/content/:id/feedback — Submit feedback */
router.post('/content/:id/feedback', (req, res, next) => {
  try {
    const { adapted_content_id, feedback_type, rating, original_text, edited_text, comments } = req.body;
    if (!adapted_content_id || !feedback_type) {
      return res.status(400).json({ error: 'adapted_content_id and feedback_type are required' });
    }
    const record = req.feedbackRepo.create({
      id: uuidv4(),
      adapted_content_id,
      feedback_type,
      rating: rating || null,
      original_text: original_text || null,
      edited_text: edited_text || null,
      comments: comments || null,
    });

    // Update adapted content status
    try {
      if (feedback_type === 'approve') {
        req.analyticsRepo.updateAdaptedContent(adapted_content_id, { status: 'approved' });
      } else if (feedback_type === 'reject') {
        req.analyticsRepo.updateAdaptedContent(adapted_content_id, { status: 'rejected' });
      }
    } catch (_) { /* noop */ }

    res.status(201).json({ data: record });
  } catch (err) { next(err); }
});

/** GET /api/content/:id/feedback — Get feedback history */
router.get('/content/:id/feedback', (req, res, next) => {
  try {
    // Find adaptations for this content, then get feedback for each
    const adaptations = req.analyticsRepo.getAdaptationsByContentId(req.params.id);
    const feedback = adaptations.flatMap(a =>
      req.feedbackRepo.findByAdaptedContentId(a.id)
    );
    res.json({ data: feedback });
  } catch (err) { next(err); }
});

/** POST /api/content/:id/score — Get engagement score */
router.post('/content/:id/score', async (req, res, next) => {
  try {
    const { platform = 'linkedin' } = req.body;
    const content = req.contentRepo.findById(req.params.id);
    if (!content) return res.status(404).json({ error: 'Content not found' });
    const text = content.refined_content || content.raw_content;
    const score = await req.services.engagementScorer.score(text, platform);
    res.json({ data: score });
  } catch (err) { next(err); }
});

export default router;
