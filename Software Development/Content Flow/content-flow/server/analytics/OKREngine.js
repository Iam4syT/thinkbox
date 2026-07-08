/**
 * @module OKREngine
 * @description Objective and Key Result tracking engine.
 * Uses OKRRepository, QueueRepository, and AnalyticsRepository.
 */
import { v4 as uuidv4 } from 'uuid';

export class OKREngine {
  /**
   * @param {Object} okrRepo - OKRRepository instance
   * @param {Object} queueRepo - QueueRepository instance
   * @param {Object} analyticsRepo - AnalyticsRepository instance
   */
  constructor(okrRepo, queueRepo, analyticsRepo) {
    this.okrRepo = okrRepo;
    this.queueRepo = queueRepo;
    this.analyticsRepo = analyticsRepo;
  }

  /**
   * Create a new objective.
   * @param {Object} data - { title, description, target_date }
   * @returns {Object}
   */
  createObjective(data) {
    return this.okrRepo.createObjective({
      id: uuidv4(),
      title: data.title,
      description: data.description || null,
      target_date: data.target_date || null,
      status: 'active',
      progress: 0,
    });
  }

  /**
   * Get all objectives with their key results and computed progress.
   * @returns {Object[]}
   */
  getObjectives() {
    const objectives = this.okrRepo.getAllObjectives();
    return objectives.map(obj => {
      const progress = this._calcProgress(obj.key_results || []);
      return { ...obj, progress };
    });
  }

  /**
   * Update an objective.
   * @param {string} id
   * @param {Object} data
   */
  updateObjective(id, data) {
    return this.okrRepo.updateObjective(id, data);
  }

  /**
   * Delete an objective and cascade key results.
   * @param {string} id
   */
  deleteObjective(id) {
    return this.okrRepo.deleteObjective(id);
  }

  /**
   * Add a key result to an objective.
   * @param {string} objectiveId
   * @param {Object} data
   * @returns {Object}
   */
  addKeyResult(objectiveId, data) {
    return this.okrRepo.createKeyResult({
      id: uuidv4(),
      objective_id: objectiveId,
      title: data.title,
      metric_type: data.metric_type,
      target_value: data.target_value,
      current_value: data.current_value || 0,
      unit: data.unit || '',
      status: 'active',
    });
  }

  /**
   * Update key result progress.
   * @param {string} objectiveId
   * @param {string} krId
   * @param {number} currentValue
   */
  updateKeyResult(objectiveId, krId, currentValue) {
    const updated = this.okrRepo.updateKeyResult(krId, { current_value: currentValue });
    this.okrRepo.recalculateProgress(objectiveId);
    return updated;
  }

  /**
   * Calculate overall progress of an objective (average of all KR %).
   * @param {Object[]} keyResults
   * @returns {number} 0-100
   */
  _calcProgress(keyResults) {
    if (!keyResults || keyResults.length === 0) return 0;
    const total = keyResults.reduce((sum, kr) => {
      const pct = kr.target_value > 0 ? Math.min(100, (kr.current_value / kr.target_value) * 100) : 0;
      return sum + pct;
    }, 0);
    return parseFloat((total / keyResults.length).toFixed(1));
  }

  /**
   * Get simple rule-based recommendations.
   * @returns {Object[]}
   */
  getRecommendations() {
    const objectives = this.getObjectives();
    const recommendations = [];

    for (const obj of objectives) {
      if (obj.progress < 25 && obj.status === 'active') {
        recommendations.push({
          objective: obj.title,
          recommendation: `You're at ${obj.progress}% — increase posting frequency to accelerate progress.`,
          priority: 'high',
        });
      } else if (obj.progress >= 75) {
        recommendations.push({
          objective: obj.title,
          recommendation: `Great progress at ${obj.progress}%! Maintain consistency to hit your target.`,
          priority: 'low',
        });
      } else if (obj.progress >= 25) {
        recommendations.push({
          objective: obj.title,
          recommendation: `On track at ${obj.progress}%. Keep posting consistently to reach your goal.`,
          priority: 'medium',
        });
      }
    }

    if (recommendations.length === 0) {
      recommendations.push({
        objective: 'Getting Started',
        recommendation: 'Set objectives with measurable key results to track your content strategy progress.',
        priority: 'medium',
      });
    }

    return recommendations;
  }
}

export default OKREngine;
