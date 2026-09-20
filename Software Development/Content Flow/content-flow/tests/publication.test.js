import { describe, it, expect } from 'vitest';
import { QueueManager } from '../server/automation/QueueManager.js';
import { PostScheduler } from '../server/automation/PostScheduler.js';

describe('Publication evidence boundary', () => {
  const setup = () => {
    let item = { id: 'fixture', status: 'scheduled', metadata: {}, scheduled_time: '2020-01-01T00:00:00Z' };
    const repo = { findById: () => item, update: (id, values) => (item = { ...item, ...values }), findAll: () => [item] };
    return { manager: new QueueManager(repo), get: () => item };
  };
  it('never marks simulated scheduling as published', () => {
    const { manager, get } = setup();
    new PostScheduler(manager)._publishPost(get());
    expect(get().status).toBe('ready_for_review');
    expect(get().metadata.external_publication_verified).toBe(false);
  });
  it('requires a verified receipt for publication state', () => {
    const { manager } = setup();
    expect(() => manager.markPosted('fixture')).toThrow();
    expect(() => manager.markPosted('fixture', {verified: true, url: 'javascript:void(0)', published_at: 'bad'})).toThrow();
    expect(manager.markPosted('fixture', {verified:true,url:'https://example.com/post/1',published_at:'2026-09-13T12:00:00Z'}).status).toBe('published');
  });
});
