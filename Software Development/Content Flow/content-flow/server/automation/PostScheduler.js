/**
 * @module PostScheduler
 * @description Cron-based scheduler for automated post publishing.
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
    if (this._mainJob) this._mainJob.stop();
    this._jobs.forEach(j => j.stop());
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
   * Simulate publishing a post (Phase 4 will call real APIs).
   * @param {Object} queueItem
   */
  _publishPost(queueItem) {
    try {
      console.log(`[PostScheduler] Publishing post ${queueItem.id} to ${queueItem.platform}`);
      this.queueManager.markPosted(queueItem.id);
      console.log(`[PostScheduler] ✅ Post ${queueItem.id} marked as posted`);
    } catch (err) {
      console.error(`[PostScheduler] Failed to publish ${queueItem.id}:`, err.message);
    }
  }
}

export default PostScheduler;
