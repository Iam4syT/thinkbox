/**
 * @module QueueManager
 * @description Manages the content posting queue using QueueRepository.
 */
import { v4 as uuidv4 } from 'uuid';

export class QueueManager {
  /** @param {Object} queueRepo - QueueRepository instance */
  constructor(queueRepo) {
    this.repo = queueRepo;
  }

  /**
   * Add an item to the queue.
   * @param {string} adaptedContentId
   * @param {string} platform
   * @param {Object} [opts]
   * @returns {Object}
   */
  add(adaptedContentId, platform, opts = {}) {
    const all = this.repo.findAll({ platform });
    const maxPriority = all.reduce((m, i) => Math.max(m, i.priority || 0), 0);
    return this.repo.create({
      id: uuidv4(),
      adapted_content_id: adaptedContentId,
      platform,
      status: 'pending',
      priority: maxPriority + 1,
      metadata: opts.journey_id ? { journey_id: opts.journey_id } : {},
    });
  }

  /**
   * Reorder queue items by priority.
   * @param {string[]} orderedIds - IDs in desired order (highest priority first)
   */
  reorder(orderedIds) {
    const items = orderedIds.map((id, idx) => ({
      id,
      priority: orderedIds.length - idx,
    }));
    this.repo.reorder(items);
  }

  /**
   * Schedule a queue item.
   * @param {string} id
   * @param {string} scheduledTime - ISO datetime
   * @param {string} [reason]
   */
  schedule(id, scheduledTime, reason = '') {
    return this.repo.update(id, {
      status: 'scheduled',
      scheduled_time: scheduledTime,
      metadata: { timing_reason: reason },
    });
  }

  /** @param {string} id */
  pause(id) { return this.repo.update(id, { status: 'paused' }); }

  /** @param {string} id */
  resume(id) { return this.repo.update(id, { status: 'pending' }); }

  /** @param {string} id */
  remove(id) { return this.repo.delete(id); }

  /** @param {string} id */
  markPosted(id) {
    return this.repo.update(id, { status: 'published' });
  }

  /**
   * Get all queue items.
   * @param {string} [platform]
   * @returns {Object[]}
   */
  getAll(platform) {
    return this.repo.findAll(platform ? { platform } : {});
  }

  /** @param {string} id */
  getById(id) { return this.repo.findById(id); }

  /** @returns {Object[]} */
  getUnscheduled() {
    return this.repo.findAll({ status: 'pending' }).filter(i => !i.scheduled_time);
  }

  /** @returns {Object[]} */
  getScheduled() {
    return this.repo.getDueItems ? this.repo.getDueItems() : this.repo.findAll({ status: 'scheduled' });
  }
}

export default QueueManager;
