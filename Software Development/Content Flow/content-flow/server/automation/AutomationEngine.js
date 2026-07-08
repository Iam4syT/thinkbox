/**
 * @module AutomationEngine
 * @description Main automation orchestrator — queue, scheduling, timing, journeys.
 */
export class AutomationEngine {
  /**
   * @param {Object} deps
   * @param {import('./QueueManager.js').QueueManager} deps.queueManager
   * @param {import('./PostScheduler.js').PostScheduler} deps.postScheduler
   * @param {import('./TimingOptimizer.js').TimingOptimizer} deps.timingOptimizer
   * @param {import('./JourneyPlanner.js').JourneyPlanner} deps.journeyPlanner
   */
  constructor({ queueManager, postScheduler, timingOptimizer, journeyPlanner }) {
    this.queueManager = queueManager;
    this.postScheduler = postScheduler;
    this.timingOptimizer = timingOptimizer;
    this.journeyPlanner = journeyPlanner;
  }

  /** Start the automation engine. */
  start() {
    this.postScheduler.start();
    console.log('[AutomationEngine] Started');
  }

  /**
   * Add adapted content to the queue with optional journey assignment.
   * @param {string} adaptedContentId
   * @param {string} platform
   * @param {Object} [opts]
   * @returns {Object} Queue item
   */
  addToQueue(adaptedContentId, platform, opts = {}) {
    return this.queueManager.add(adaptedContentId, platform, opts);
  }

  /**
   * Auto-schedule all unscheduled queue items using AI timing.
   * @param {string} [platform] - Optional platform filter
   * @returns {Promise<Object[]>} Updated queue items
   */
  async autoSchedule(platform) {
    const items = this.queueManager.getUnscheduled()
      .filter(i => !platform || i.platform === platform);

    const results = [];
    const recentTimes = this.queueManager.getScheduled()
      .map(i => i.scheduled_time)
      .filter(Boolean);

    for (const item of items) {
      try {
        const timing = await this.timingOptimizer.getOptimalTime(
          item.platform,
          {},
          recentTimes
        );
        const updated = this.queueManager.schedule(
          item.id,
          timing.optimal_time,
          timing.reasoning
        );
        recentTimes.push(timing.optimal_time);
        results.push({ ...updated, timing });
      } catch (err) {
        console.error(`[AutomationEngine] Failed to schedule ${item.id}:`, err.message);
        results.push({ ...item, error: err.message });
      }
    }

    return results;
  }
}

export default AutomationEngine;
