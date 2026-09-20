/**
 * @module PostScheduler
 * @description Scheduler for preparing posts for manual publication. No platform publisher is implemented.
 */
import cron from 'node-cron';

export class PostScheduler {
  /**
   * @param {import('./QueueManager.js').QueueManager} queueManager
   */
  constructor(queueManager) {
    this.queueManager = queueManager;
    this._jobs = new Map(); // queueItemId → cron task
    this._started = false;
  }

  /**
   * Start the scheduler — loads all scheduled items and sets up cron jobs.
   */
  start() {
    if (this._started) return;
    this._started = true;
    console.log('[PostScheduler] Starting...');

    // Check for due posts every minute
    this._mainJob = cron.schedule('* * * * *', () => this._processDuePosts());
    console.log('[PostScheduler] Running — checks every minute');
  }

  /**
   * Stop the scheduler.
   */
  stop() {
    if (this._mainJob) { this._mainJob.stop(); this._mainJob.destroy?.(); this._mainJob = null; }
    this._jobs.forEach(j => { j.stop(); j.destroy?.(); });
    this._jobs.clear();
    this._started = false;
  }

  /**
   * Process any posts that are past their scheduled time.
   */
  _processDuePosts() {
    try {
      const scheduled = this.queueManager.getScheduled();
      const now = new Date();

      for (const item of scheduled) {
        if (!item.scheduled_time) continue;
        const scheduledAt = new Date(item.scheduled_time);
        if (scheduledAt <= now) {
          this._publishPost(item);
        }
      }
    } catch (err) {
      console.error('[PostScheduler] Error processing due posts:', err.message);
    }
  }

  /**
   * Mark due content ready for manual review. No publisher is called.
   * @param {Object} queueItem
   */
  _publishPost(queueItem) {
    try {
      this.queueManager.markReadyForReview(queueItem.id);
      console.log(`[PostScheduler] Post ${queueItem.id} ready for manual review; nothing published`);
    } catch (err) {
      console.error(`[PostScheduler] Failed to prepare ${queueItem.id}:`, err.message);
    }
  }
}

export default PostScheduler;
