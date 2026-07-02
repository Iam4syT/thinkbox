/**
 * ContentFlow — DOM Utility Helpers
 */

/** Query a single element */
export function $(selector, context = document) {
  return context.querySelector(selector);
}

/** Query all elements */
export function $$(selector, context = document) {
  return [...context.querySelectorAll(selector)];
}

/**
 * Create a DOM element with properties and children.
 * @param {string} tag
 * @param {Object} props - attributes, className, style, events (on*)
 * @param {(string|Node)[]} children
 * @returns {HTMLElement}
 */
export function createElement(tag, props = {}, children = []) {
  const el = document.createElement(tag);
  for (const [key, val] of Object.entries(props)) {
    if (key === 'className') {
      el.className = val;
    } else if (key === 'style' && typeof val === 'object') {
      Object.assign(el.style, val);
    } else if (key === 'dataset' && typeof val === 'object') {
      for (const [dk, dv] of Object.entries(val)) el.dataset[dk] = dv;
    } else if (key.startsWith('on') && typeof val === 'function') {
      el.addEventListener(key.slice(2).toLowerCase(), val);
    } else if (key === 'innerHTML') {
      el.innerHTML = val;
    } else {
      el.setAttribute(key, val);
    }
  }
  for (const child of Array.isArray(children) ? children : [children]) {
    if (child == null) continue;
    el.append(typeof child === 'string' ? document.createTextNode(child) : child);
  }
  return el;
}

/** Shorthand event binding */
export function on(el, event, handler, opts) {
  el.addEventListener(event, handler, opts);
  return () => el.removeEventListener(event, handler, opts);
}

/** Show an element */
export function show(el) {
  el.hidden = false;
  el.classList.remove('hidden');
}

/** Hide an element */
export function hide(el) {
  el.hidden = true;
  el.classList.add('hidden');
}

/** Toggle visibility */
export function toggle(el, force) {
  const shouldShow = force !== undefined ? force : el.hidden;
  shouldShow ? show(el) : hide(el);
}

/**
 * Simple animation helper using Web Animations API
 */
export function animate(el, keyframes, options = {}) {
  const defaults = { duration: 400, easing: 'cubic-bezier(0.16, 1, 0.3, 1)', fill: 'forwards' };
  return el.animate(keyframes, { ...defaults, ...options });
}

/** Format a date for display */
export function formatDate(date, opts = {}) {
  const d = date instanceof Date ? date : new Date(date);
  const defaults = { month: 'short', day: 'numeric', year: 'numeric' };
  return d.toLocaleDateString('en-US', { ...defaults, ...opts });
}

/** Format a date as time */
export function formatTime(date) {
  const d = date instanceof Date ? date : new Date(date);
  return d.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
}

/** Format a number with abbreviation (1.2k, 3.4M) */
export function formatNumber(num) {
  if (num >= 1_000_000) return (num / 1_000_000).toFixed(1) + 'M';
  if (num >= 1_000) return (num / 1_000).toFixed(1) + 'k';
  return num.toString();
}

/** Debounce a function */
export function debounce(fn, delay = 300) {
  let timer;
  return function (...args) {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}

/** Throttle a function */
export function throttle(fn, limit = 200) {
  let inThrottle = false;
  return function (...args) {
    if (!inThrottle) {
      fn.apply(this, args);
      inThrottle = true;
      setTimeout(() => (inThrottle = false), limit);
    }
  };
}

/** Generate a unique ID */
export function uid(prefix = 'cf') {
  return `${prefix}-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 7)}`;
}

/** Clamp a value */
export function clamp(val, min, max) {
  return Math.min(Math.max(val, min), max);
}

/** Escape HTML */
export function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

/** Simple HTML template */
export function html(strings, ...values) {
  return strings.reduce((result, str, i) => result + str + (values[i] ?? ''), '');
}

/** Empty an element */
export function empty(el) {
  while (el.firstChild) el.removeChild(el.firstChild);
}
