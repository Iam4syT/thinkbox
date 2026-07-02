/**
 * @module config
 * @description Central configuration loader for ContentFlow.
 * Reads environment variables from .env via dotenv and exports
 * a frozen configuration object with sensible defaults.
 */
import dotenv from 'dotenv';
import { fileURLToPath } from 'url';
import path from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

dotenv.config({ path: path.join(ROOT_DIR, '.env') });

/**
 * @typedef {Object} AppConfig
 * @property {number} port - HTTP server port
 * @property {string} nodeEnv - Current environment (development | production | test)
 * @property {string} dbPath - Path to the SQLite database file
 * @property {string} geminiApiKey - Google Gemini API key
 * @property {string} geminiModel - Gemini model identifier
 * @property {string} rootDir - Absolute path to project root
 * @property {Object} cors - CORS configuration
 * @property {Object} rateLimit - Rate limiting configuration
 * @property {Object} contentDefaults - Default content settings
 */
const config = Object.freeze({
  port: parseInt(process.env.PORT, 10) || 3001,
  nodeEnv: process.env.NODE_ENV || 'development',
  dbPath: path.resolve(ROOT_DIR, process.env.DB_PATH || './data/contentflow.db'),
  geminiApiKey: process.env.GEMINI_API_KEY || '',
  geminiModel: process.env.GEMINI_MODEL || 'gemini-2.0-flash',
  rootDir: ROOT_DIR,

  cors: {
    origin: process.env.CORS_ORIGIN || '*',
    credentials: true,
  },

  rateLimit: {
    windowMs: parseInt(process.env.RATE_LIMIT_WINDOW_MS, 10) || 60_000,
    maxRequests: parseInt(process.env.RATE_LIMIT_MAX, 10) || 100,
  },

  contentDefaults: {
    maxBrainDumpLength: 50_000,
    maxAdaptedContentLength: 10_000,
    supportedPlatforms: ['linkedin', 'instagram', 'youtube'],
  },

  /** @returns {boolean} Whether a valid Gemini API key is configured */
  get hasValidApiKey() {
    return (
      this.geminiApiKey.length > 0 &&
      this.geminiApiKey !== 'your_gemini_api_key_here'
    );
  },

  /** @returns {boolean} Whether the app is running in development mode */
  get isDev() {
    return this.nodeEnv === 'development';
  },
});

export default config;
