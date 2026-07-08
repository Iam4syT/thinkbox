/**
 * @module AnalyticsService
 * @description Post performance tracking using AnalyticsRepository methods.
 */
export class AnalyticsService {
  /**
   * @param {Object} analyticsRepo - AnalyticsRepository instance
   * @param {Object} queueRepo - QueueRepository instance
   */
  constructor(analyticsRepo, queueRepo) {
    this.analyticsRepo = analyticsRepo;
    this.queueRepo = queueRepo;
  }

  /**
   * Get overview stats for the dashboard.
   * @returns {Object}
   */
  getOverview() {
    const queue = this.queueRepo.findAll();
    const totalPosts = queue.filter(q => q.status === 'published').length;

    const weekAgo = new Date();
    weekAgo.setDate(weekAgo.getDate() - 7);
    const postsThisWeek = queue.filter(q => {
      if (q.status !== 'published' || !q.updated_at) return false;
      return new Date(q.updated_at) >= weekAgo;
    }).length;

    // Platform distribution
    const platforms = ['linkedin', 'instagram', 'youtube'];
    const platformCounts = {};
    platforms.forEach(p => {
      platformCounts[p] = queue.filter(q => q.platform === p && q.status === 'published').length;
    });
    const topPlatform = Object.entries(platformCounts).sort((a, b) => b[1] - a[1])[0]?.[0] || 'linkedin';

    // Aggregate metrics from each platform
    const now = new Date().toISOString();
    const monthAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();
    let totalEngagement = 0;
    let metricCount = 0;

    for (const p of platforms) {
      try {
        const agg = this.analyticsRepo.getAggregatedMetrics(p, monthAgo, now);
        if (agg.post_count > 0) {
          totalEngagement += agg.avg_engagement_rate * agg.post_count;
          metricCount += agg.post_count;
        }
      } catch (_) { /* noop */ }
    }

    const avgEngagementRate = metricCount > 0 ? parseFloat((totalEngagement / metricCount).toFixed(2)) : 0;

    return { totalPosts, avgEngagementRate, topPlatform, postsThisWeek };
  }

  /**
   * Get engagement trend over N days.
   * @param {number} [days=30]
   * @returns {Object[]} Array of { date, score }
   */
  getEngagementTrend(days = 30) {
    // Build daily slots for the last N days
    const slots = {};
    for (let i = days; i >= 0; i--) {
      const d = new Date();
      d.setDate(d.getDate() - i);
      const key = d.toISOString().split('T')[0];
      slots[key] = [];
    }

    // Use top-performing data across platforms
    const platforms = ['linkedin', 'instagram', 'youtube'];
    for (const platform of platforms) {
      try {
        const top = this.analyticsRepo.getTopPerforming(platform, 50);
        top.forEach(item => {
          const date = (item.recorded_at || item.created_at || '').split('T')[0];
          if (slots[date] !== undefined) {
            slots[date].push(item.engagement_rate || 0);
          }
        });
      } catch (_) { /* noop */ }
    }

    return Object.entries(slots).map(([date, rates]) => ({
      date,
      score: rates.length > 0
        ? parseFloat((rates.reduce((a, b) => a + b, 0) / rates.length).toFixed(2))
        : 0,
    }));
  }

  /**
   * Get per-platform comparison.
   * @returns {Object[]}
   */
  getPlatformComparison() {
    const platforms = ['linkedin', 'instagram', 'youtube'];
    const now = new Date().toISOString();
    const monthAgo = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString();
    const results = [];

    for (const platform of platforms) {
      try {
        const agg = this.analyticsRepo.getAggregatedMetrics(platform, monthAgo, now);
        results.push({
          platform,
          avgEngagement: parseFloat((agg.avg_engagement_rate || 0).toFixed(2)),
          postCount: agg.post_count || 0,
          totalLikes: agg.total_likes || 0,
          totalShares: agg.total_shares || 0,
        });
      } catch (_) {
        results.push({ platform, avgEngagement: 0, postCount: 0, totalLikes: 0, totalShares: 0 });
      }
    }

    return results;
  }

  /**
   * Get recent post performance (top performing across all platforms).
   * @param {number} [limit=10]
   * @returns {Object[]}
   */
  getRecentPerformance(limit = 10) {
    const all = [];
    const platforms = ['linkedin', 'instagram', 'youtube'];
    for (const p of platforms) {
      try {
        const items = this.analyticsRepo.getTopPerforming(p, limit);
        all.push(...items.map(i => ({ ...i, platform: p })));
      } catch (_) { /* noop */ }
    }
    return all
      .sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      .slice(0, limit);
  }

  /**
   * Get evolution snapshots via learning repository.
   * @returns {Object[]}
   */
  getEvolution() {
    return [];
  }
}

export default AnalyticsService;
