/**
 * @module okr.routes
 * @description OKR objectives and key results routes.
 */
import { Router } from 'express';

const router = Router();

/** GET /api/okr/objectives — List all objectives with progress */
router.get('/okr/objectives', (req, res, next) => {
  try {
    const objectives = req.services.okrEngine.getObjectives();
    res.json({ data: objectives });
  } catch (err) { next(err); }
});

/** POST /api/okr/objectives — Create objective */
router.post('/okr/objectives', (req, res, next) => {
  try {
    const { title, description, target_date } = req.body;
    if (!title) return res.status(400).json({ error: 'title is required' });
    const objective = req.services.okrEngine.createObjective({ title, description, target_date });
    res.status(201).json({ data: objective });
  } catch (err) { next(err); }
});

/** PUT /api/okr/objectives/:id — Update objective */
router.put('/okr/objectives/:id', (req, res, next) => {
  try {
    const updated = req.services.okrEngine.updateObjective(req.params.id, req.body);
    if (!updated) return res.status(404).json({ error: 'Objective not found' });
    res.json({ data: updated });
  } catch (err) { next(err); }
});

/** DELETE /api/okr/objectives/:id — Delete objective */
router.delete('/okr/objectives/:id', (req, res, next) => {
  try {
    const deleted = req.services.okrEngine.deleteObjective(req.params.id);
    if (!deleted) return res.status(404).json({ error: 'Objective not found' });
    res.json({ data: { deleted: true } });
  } catch (err) { next(err); }
});

/** GET /api/okr/objectives/:id/key-results — List KRs for objective */
router.get('/okr/objectives/:id/key-results', (req, res, next) => {
  try {
    const krs = req.okrRepo.getKeyResultsByObjectiveId(req.params.id);
    res.json({ data: krs });
  } catch (err) { next(err); }
});

/** POST /api/okr/objectives/:id/key-results — Add KR */
router.post('/okr/objectives/:id/key-results', (req, res, next) => {
  try {
    const { title, metric_type, target_value, unit, current_value } = req.body;
    if (!title || !metric_type || target_value === undefined) {
      return res.status(400).json({ error: 'title, metric_type, and target_value are required' });
    }
    const kr = req.services.okrEngine.addKeyResult(req.params.id, {
      title, metric_type, target_value: parseFloat(target_value),
      unit: unit || '', current_value: current_value ? parseFloat(current_value) : 0,
    });
    res.status(201).json({ data: kr });
  } catch (err) { next(err); }
});

/** PUT /api/okr/objectives/:objectiveId/key-results/:krId — Update KR progress */
router.put('/okr/objectives/:objectiveId/key-results/:krId', (req, res, next) => {
  try {
    const { current_value, status } = req.body;
    const updateData = {};
    if (current_value !== undefined) updateData.current_value = parseFloat(current_value);
    if (status) updateData.status = status;
    const updated = req.okrRepo.updateKeyResult(req.params.krId, updateData);
    req.okrRepo.recalculateProgress(req.params.objectiveId);
    res.json({ data: updated });
  } catch (err) { next(err); }
});

/** GET /api/okr/recommendations — AI recommendations */
router.get('/okr/recommendations', (req, res, next) => {
  try {
    const recommendations = req.services.okrEngine.getRecommendations();
    res.json({ data: recommendations });
  } catch (err) { next(err); }
});

export default router;
