import { afterAll, beforeAll, expect, it } from 'vitest';
import { spawn } from 'node:child_process';
import { mkdtempSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { createServer } from 'node:net';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const directory = mkdtempSync(path.join(tmpdir(), 'content-flow-api-test-'));
let child, base, output = '';
const request = async (route, method = 'GET', body) => {
  const response = await fetch(base + route, {
    method, headers: { 'Content-Type': 'application/json' },
    ...(body === undefined ? {} : { body: JSON.stringify(body) }),
  });
  return { status: response.status, body: await response.json() };
};

beforeAll(async () => {
  const probe = createServer();
  await new Promise((resolve, reject) => { probe.once('error', reject); probe.listen(0, '127.0.0.1', resolve); });
  const port = probe.address().port;
  await new Promise(resolve => probe.close(resolve));
  base = `http://127.0.0.1:${port}/api`;
  child = spawn(process.execPath, ['server/index.js'], {
    cwd: fileURLToPath(new URL('../', import.meta.url)),
    env: { ...process.env, PORT: String(port), DB_PATH: path.join(directory, 'fixture.db'), OPENAI_API_KEY: '', GEMINI_API_KEY: '' },
    stdio: ['ignore', 'pipe', 'pipe'],
  });
  child.stdout.on('data', data => { output += data; });
  child.stderr.on('data', data => { output += data; });
  for (let attempt = 0; attempt < 100; attempt++) {
    if (child.exitCode !== null) throw new Error(output);
    try { if ((await request('/health')).status === 200) return; } catch { /* Startup may still be running. */ }
    await new Promise(resolve => setTimeout(resolve, 100));
  }
  throw new Error(`Server failed to start: ${output}`);
}, 15000);

afterAll(async () => {
  if (child && child.exitCode === null) {
    await new Promise(resolve => { child.once('exit', resolve); child.kill('SIGTERM'); });
  }
  rmSync(directory, { recursive: true, force: true });
});

it('runs the local draft-to-queue workflow without claiming publication or a live AI connection', async () => {
  const health = await request('/health');
  expect(health.body.ai).toMatch(/mock/i);
  expect((await request('/content', 'POST', { raw_content: 123 })).status).toBe(400);
  const created = await request('/content', 'POST', { title: 'Local fixture', raw_content: 'I tested a synthetic workplace data policy and recorded its limits.' });
  expect(created.status).toBe(201);
  const id = created.body.data.id;
  expect((await request(`/content/${id}/refine`, 'POST', {})).status).toBe(200);
  const adapted = await request(`/content/${id}/adapt`, 'POST', { platforms: ['linkedin'] });
  expect(adapted.status).toBe(200);
  expect(adapted.body.data.length).toBe(1);
  const queued = await request('/queue', 'POST', { adapted_content_id: adapted.body.data[0].id, platform: 'linkedin' });
  expect(queued.status).toBe(201);
  const queueId = queued.body.data.id;
  expect((await request(`/queue/${queueId}`, 'PUT', { status: 'published' })).status).toBe(400);
  expect((await request(`/queue/${queueId}`, 'PUT', { unknown_sql_column: 'bad' })).status).toBe(400);
  expect((await request(`/queue/${queueId}/schedule`, 'POST', { scheduled_time: 'invalid' })).status).toBe(400);
  const scheduled = await request(`/queue/${queueId}/schedule`, 'POST', { scheduled_time: new Date(Date.now() + 86400000).toISOString() });
  expect(scheduled.body.data.status).toBe('scheduled');
  expect((await request(`/content/${id}`, 'PUT', { unknown_sql_column: 'bad' })).status).toBe(400);
  expect((await request(`/queue/${queueId}`, 'DELETE')).status).toBe(200);
  expect((await request(`/content/${id}`, 'DELETE')).status).toBe(200);
}, 15000);
