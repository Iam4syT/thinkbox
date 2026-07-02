/**
 * @module database
 * @description SQLite database connection manager using better-sqlite3.
 * Implements the Singleton pattern to ensure a single DB connection.
 * Automatically runs migrations on first initialization.
 */
import Database from 'better-sqlite3';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import config from '../config.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

/** @type {Database.Database|null} */
let instance = null;

/**
 * Returns the singleton SQLite database instance.
 * Creates the database file and runs migrations on first call.
 * @returns {Database.Database} The better-sqlite3 database instance
 */
export function getDatabase() {
  if (instance) return instance;

  // Ensure the data directory exists
  const dbDir = path.dirname(config.dbPath);
  if (!fs.existsSync(dbDir)) {
    fs.mkdirSync(dbDir, { recursive: true });
  }

  instance = new Database(config.dbPath);

  // Enable WAL mode for better concurrent read performance
  instance.pragma('journal_mode = WAL');
  instance.pragma('foreign_keys = ON');
  instance.pragma('busy_timeout = 5000');

  // Run migrations
  runMigrations(instance);

  return instance;
}

/**
 * Runs all pending SQL migrations in order.
 * Tracks applied migrations in a _migrations meta-table.
 * @param {Database.Database} db - The database instance
 */
function runMigrations(db) {
  // Create migrations tracking table
  db.exec(`
    CREATE TABLE IF NOT EXISTS _migrations (
      id          INTEGER PRIMARY KEY AUTOINCREMENT,
      filename    TEXT NOT NULL UNIQUE,
      applied_at  TEXT DEFAULT (datetime('now'))
    );
  `);

  const migrationsDir = path.join(__dirname, 'migrations');
  if (!fs.existsSync(migrationsDir)) return;

  // Read and sort migration files
  const files = fs
    .readdirSync(migrationsDir)
    .filter((f) => f.endsWith('.sql'))
    .sort();

  const applied = new Set(
    db
      .prepare('SELECT filename FROM _migrations')
      .all()
      .map((row) => row.filename)
  );

  for (const file of files) {
    if (applied.has(file)) continue;

    const sql = fs.readFileSync(path.join(migrationsDir, file), 'utf-8');

    const runMigration = db.transaction(() => {
      db.exec(sql);
      db.prepare('INSERT INTO _migrations (filename) VALUES (?)').run(file);
    });

    runMigration();
    console.log(`[DB] Applied migration: ${file}`);
  }
}

/**
 * Closes the database connection and resets the singleton.
 * Useful for graceful shutdown and testing.
 */
export function closeDatabase() {
  if (instance) {
    instance.close();
    instance = null;
  }
}

export default { getDatabase, closeDatabase };
