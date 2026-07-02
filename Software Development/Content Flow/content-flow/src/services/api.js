/**
 * ContentFlow — Frontend API Client
 * All backend endpoint methods with error handling.
 */

const BASE_URL = '/api';

class ApiError extends Error {
  constructor(message, status, data) {
    super(message);
    this.name = 'ApiError';
    this.status = status;
    this.data = data;
  }
}

async function request(path, options = {}) {
  const { method = 'GET', body, params, headers: extraHeaders = {} } = options;

  let url = `${BASE_URL}${path}`;
  if (params) {
    const qs = new URLSearchParams(params).toString();
    url += `?${qs}`;
  }

  const headers = {
    'Content-Type': 'application/json',
    ...extraHeaders,
  };

  const config = { method, headers };
  if (body && method !== 'GET') {
    config.body = JSON.stringify(body);
  }

  try {
    const res = await fetch(url, config);
    const data = res.headers.get('content-type')?.includes('json')
      ? await res.json()
      : await res.text();

    if (!res.ok) {
      throw new ApiError(data?.message || 'Request failed', res.status, data);
    }
    return data;
  } catch (err) {
    if (err instanceof ApiError) throw err;
    throw new ApiError(err.message || 'Network error', 0, null);
  }
}

// ─── Content CRUD ───

export function createContent(payload) {
  return request('/content', { method: 'POST', body: payload });
}

export function getContent(id) {
  return request(`/content/${id}`);
}

export function listContent(params) {
  return request('/content', { params });
}

export function updateContent(id, payload) {
  return request(`/content/${id}`, { method: 'PUT', body: payload });
}

export function deleteContent(id) {
  return request(`/content/${id}`, { method: 'DELETE' });
}

export function refineContent(id, payload) {
  return request(`/content/${id}/refine`, { method: 'POST', body: payload });
}

// ─── Adapt Pipeline ───

export function adaptContent(id, platforms) {
  return request(`/content/${id}/adapt`, { method: 'POST', body: { platforms } });
}

export function getAdaptations(id) {
  return request(`/content/${id}/adaptations`);
}

// ─── Suggestions & Scoring ───

export function getSuggestions(contentId) {
  return request(`/content/${contentId}/suggestions`);
}

export function applySuggestion(contentId, suggestionId) {
  return request(`/content/${contentId}/suggestions/${suggestionId}/apply`, { method: 'POST' });
}

export function getEngagementScore(contentId, platform) {
  return request(`/content/${contentId}/score`, { params: { platform } });
}

// ─── Feedback ───

export function submitFeedback(contentId, feedback) {
  return request(`/content/${contentId}/feedback`, { method: 'POST', body: feedback });
}

export function getFeedbackHistory(contentId) {
  return request(`/content/${contentId}/feedback`);
}

// ─── Queue Management ───

export function getQueue(params) {
  return request('/queue', { params });
}

export function addToQueue(payload) {
  return request('/queue', { method: 'POST', body: payload });
}

export function updateQueueItem(id, payload) {
  return request(`/queue/${id}`, { method: 'PUT', body: payload });
}

export function deleteQueueItem(id) {
  return request(`/queue/${id}`, { method: 'DELETE' });
}

export function reorderQueue(orderedIds) {
  return request('/queue/reorder', { method: 'POST', body: { order: orderedIds } });
}

export function autoSchedule() {
  return request('/queue/auto-schedule', { method: 'POST' });
}

export function pauseQueueItem(id) {
  return request(`/queue/${id}/pause`, { method: 'POST' });
}

export function resumeQueueItem(id) {
  return request(`/queue/${id}/resume`, { method: 'POST' });
}

// ─── Scheduling ───

export function getSchedule(params) {
  return request('/schedule', { params });
}

export function schedulePost(payload) {
  return request('/schedule', { method: 'POST', body: payload });
}

export function updateSchedule(id, payload) {
  return request(`/schedule/${id}`, { method: 'PUT', body: payload });
}

export function deleteSchedule(id) {
  return request(`/schedule/${id}`, { method: 'DELETE' });
}

// ─── Analytics ───

export function getAnalyticsOverview(params) {
  return request('/analytics/overview', { params });
}

export function getEngagementTrend(params) {
  return request('/analytics/engagement-trend', { params });
}

export function getPlatformComparison(params) {
  return request('/analytics/platform-comparison', { params });
}

export function getRecentPerformance(params) {
  return request('/analytics/recent-performance', { params });
}

export function getEvolutionMetrics(params) {
  return request('/analytics/evolution', { params });
}

export function getAudienceInsights(platform) {
  return request('/analytics/audience', { params: { platform } });
}

// ─── OKR ───

export function getObjectives() {
  return request('/okr/objectives');
}

export function createObjective(payload) {
  return request('/okr/objectives', { method: 'POST', body: payload });
}

export function updateObjective(id, payload) {
  return request(`/okr/objectives/${id}`, { method: 'PUT', body: payload });
}

export function deleteObjective(id) {
  return request(`/okr/objectives/${id}`, { method: 'DELETE' });
}

export function getKeyResults(objectiveId) {
  return request(`/okr/objectives/${objectiveId}/key-results`);
}

export function updateKeyResult(objectiveId, krId, payload) {
  return request(`/okr/objectives/${objectiveId}/key-results/${krId}`, { method: 'PUT', body: payload });
}

export function getOKRRecommendations() {
  return request('/okr/recommendations');
}

// ─── Journeys ───

export function getJourneys() {
  return request('/journeys');
}

export function getJourney(id) {
  return request(`/journeys/${id}`);
}

export function analyzeJourneyGaps(id) {
  return request(`/journeys/${id}/analyze-gaps`, { method: 'POST' });
}

// ─── Export ───

export function exportContent(contentId, format) {
  return request(`/content/${contentId}/export`, { params: { format } });
}

// ─── SSE: Pipeline Progress ───

export function connectPipelineSSE(contentId, onMessage) {
  const url = `${BASE_URL}/content/${contentId}/pipeline/stream`;
  const eventSource = new EventSource(url);

  eventSource.onmessage = (event) => {
    try {
      const data = JSON.parse(event.data);
      onMessage(data);
    } catch {
      onMessage({ raw: event.data });
    }
  };

  eventSource.onerror = () => {
    eventSource.close();
  };

  return eventSource;
}
