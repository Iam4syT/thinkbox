import { afterAll, beforeAll, describe, expect, it } from 'vitest';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import path from 'node:path';

const directory = mkdtempSync(path.join(tmpdir(), 'content-flow-db-test-'));
process.env.DB_PATH = path.join(directory, 'fixture.db');
let database, closeDatabase, repo;

beforeAll(async () => {
  ({ getDatabase: database, closeDatabase } = await import('../server/db/database.js'));
  const { QueueRepository } = await import('../server/db/repositories/QueueRepository.js');
  repo = new QueueRepository();
});
afterAll(() => { closeDatabase?.(); rmSync(directory, { recursive: true, force: true }); });

describe('Fresh database and due queue', () => {
  it('creates the application schema from the committed migration and can reopen it', () => {
    const db = database();
    expect(db.prepare('SELECT filename FROM _migrations').all()).toEqual([{ filename: '001_initial.sql' }]);
    expect(db.prepare("SELECT name FROM sqlite_master WHERE type='table' AND name='content'").get()).toBeTruthy();
    closeDatabase();
    expect(database().prepare('SELECT COUNT(*) AS n FROM _migrations').get().n).toBe(1);
  });
  it('finds ISO timestamps due today and excludes future, paused and invalid dates', () => {
    const db = database();
    db.prepare('INSERT INTO content (id, raw_content) VALUES (?, ?)').run('content', 'Synthetic test only');
    db.prepare('INSERT INTO adapted_content (id, content_id, platform, adapted_text) VALUES (?, ?, ?, ?)')
      .run('adapted', 'content', 'linkedin', 'Synthetic text');
    const now = Date.now();
    const fixtures = [
      ['due', new Date(now - 1000).toISOString(), 'scheduled'],
      ['offset', new Date(now - 60000).toISOString().replace('Z', '+00:00'), 'scheduled'],
      ['future', new Date(now + 86400000).toISOString(), 'scheduled'],
      ['paused', new Date(now - 1000).toISOString(), 'paused'],
      ['invalid', 'invalid', 'scheduled'],
    ];
    for (const [id, scheduled_time, status] of fixtures) {
      repo.create({ id, adapted_content_id: 'adapted', platform: 'linkedin', scheduled_time, status });
    }
    expect(repo.getDueItems().map(row => row.id).sort()).toEqual(['due', 'offset']);
  });
});
