/* ─────────────────────────────────────────────────────────
   BigQuery Release Notes — main.js
──────────────────────────────────────────────────────────── */

const TWEET_MAX = 280;
let allEntries = [];
let activeFilter = 'all';

/* ── DOM refs ─────────────────────────────────────────────── */
const refreshBtn      = document.getElementById('refresh-btn');
const statusBar       = document.getElementById('status-bar');
const statusDot       = document.getElementById('status-dot');
const statusText      = document.getElementById('status-text');
const entriesContainer= document.getElementById('entries-container');
const filterBar       = document.getElementById('filter-bar');
const modalOverlay    = document.getElementById('modal-overlay');
const tweetTextarea   = document.getElementById('tweet-textarea');
const charCount       = document.getElementById('char-count');
const tweetBtn        = document.getElementById('tweet-btn');
const modalCloseBtn   = document.getElementById('modal-close');
const cancelBtn       = document.getElementById('cancel-btn');

/* ── Utility ──────────────────────────────────────────────── */
function setStatus(state, message) {
  statusBar.className = state;   // 'loading' | 'error' | ''
  statusText.textContent = message;
}

function formatDate(isoStr) {
  if (!isoStr) return '';
  const d = new Date(isoStr);
  return d.toLocaleDateString('en-GB', { day:'numeric', month:'short', year:'numeric' });
}

function getCategoryClass(cat) {
  const map = {
    'feature': 'feature',
    'change':  'change',
    'changed': 'changed',
    'deprecated': 'deprecated',
    'fixed': 'fixed',
    'breaking': 'breaking',
    'security': 'security',
  };
  return map[cat.toLowerCase()] || 'default';
}

function buildTweetText(entry) {
  const title   = entry.title || '';
  const link    = entry.link  || '';
  const cats    = (entry.categories || []).join(' · ');
  const snippet = entry.plain_text
    ? entry.plain_text.substring(0, 160).trim() + (entry.plain_text.length > 160 ? '…' : '')
    : '';

  let text = `📦 BigQuery Release Notes — ${title}\n`;
  if (cats) text += `${cats}\n`;
  text += `\n${snippet}\n\n🔗 ${link}\n\n#BigQuery #GoogleCloud #GCP`;
  return text.substring(0, TWEET_MAX);
}

/* ── Render entries ───────────────────────────────────────── */
function renderEntries(entries) {
  entriesContainer.innerHTML = '';

  if (!entries.length) {
    entriesContainer.innerHTML = `
      <div class="state-box">
        <div class="state-icon">🔍</div>
        <strong>No entries match this filter</strong>
        <p>Try selecting a different category above.</p>
      </div>`;
    return;
  }

  entries.forEach((entry, idx) => {
    const card = document.createElement('div');
    card.className = 'entry-card';
    card.style.animationDelay = `${idx * 40}ms`;

    const categoryTagsHTML = (entry.categories || [])
      .map(c => `<span class="category-tag ${getCategoryClass(c)}">${c}</span>`)
      .join('');

    card.innerHTML = `
      <div class="card-header" role="button" aria-expanded="false" tabindex="0">
        <div class="card-header-left">
          <div class="date-badge">${entry.title || 'Unknown date'}</div>
          <div>
            <div class="card-title">BigQuery Update</div>
            <div class="card-meta">${categoryTagsHTML}</div>
          </div>
        </div>
        <svg class="chevron" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <polyline points="6 9 12 15 18 9"/>
        </svg>
      </div>
      <div class="card-body">
        <div class="card-body-inner">
          <div class="release-content">${entry.content_html || '<p>No content available.</p>'}</div>
          <div class="card-footer">
            <a href="${entry.link}" target="_blank" rel="noopener" class="action-btn">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/>
                <polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/>
              </svg>
              View on Docs
            </a>
            <button class="action-btn tweet-btn" data-idx="${idx}">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-4.714-6.231-5.401 6.231H2.744l7.73-8.835L1.254 2.25H8.08l4.253 5.622zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
              </svg>
              Tweet this
            </button>
          </div>
        </div>
      </div>`;

    /* Toggle expand */
    const header = card.querySelector('.card-header');
    const toggle = () => {
      const isOpen = card.classList.toggle('expanded');
      header.setAttribute('aria-expanded', isOpen);
    };
    header.addEventListener('click', toggle);
    header.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle(); } });

    /* Tweet button */
    card.querySelector('.tweet-btn').addEventListener('click', e => {
      e.stopPropagation();
      openTweetModal(entry);
    });

    entriesContainer.appendChild(card);
  });
}

/* ── Filter chips ─────────────────────────────────────────── */
function buildFilterChips(entries) {
  const cats = new Set();
  entries.forEach(e => (e.categories || []).forEach(c => cats.add(c)));

  filterBar.innerHTML = '';
  const allChip = document.createElement('button');
  allChip.className = 'filter-chip active';
  allChip.textContent = 'All';
  allChip.dataset.filter = 'all';
  filterBar.appendChild(allChip);

  [...cats].forEach(cat => {
    const chip = document.createElement('button');
    chip.className = 'filter-chip';
    chip.textContent = cat;
    chip.dataset.filter = cat.toLowerCase();
    filterBar.appendChild(chip);
  });

  filterBar.addEventListener('click', e => {
    const chip = e.target.closest('.filter-chip');
    if (!chip) return;
    activeFilter = chip.dataset.filter;
    filterBar.querySelectorAll('.filter-chip').forEach(c => c.classList.remove('active'));
    chip.classList.add('active');
    applyFilter();
  });
}

function applyFilter() {
  if (activeFilter === 'all') {
    renderEntries(allEntries);
    return;
  }
  const filtered = allEntries.filter(e =>
    (e.categories || []).some(c => c.toLowerCase() === activeFilter)
  );
  renderEntries(filtered);
}

/* ── Fetch releases ───────────────────────────────────────── */
async function fetchReleases() {
  refreshBtn.classList.add('loading');
  refreshBtn.disabled = true;
  setStatus('loading', 'Fetching latest release notes…');
  entriesContainer.innerHTML = `
    <div class="state-box">
      <div class="state-icon" style="animation: spin 1s linear infinite; display:inline-block;">⟳</div>
      <p>Loading BigQuery release notes…</p>
    </div>`;

  try {
    const res  = await fetch('/api/releases');
    const json = await res.json();

    if (!json.ok) throw new Error(json.error || 'Unknown error');

    allEntries = json.data.entries || [];
    buildFilterChips(allEntries);
    applyFilter();
    setStatus('', `✓ ${allEntries.length} entries loaded · Last updated ${json.data.fetched_at}`);
  } catch (err) {
    setStatus('error', `Error: ${err.message}`);
    entriesContainer.innerHTML = `
      <div class="state-box">
        <div class="state-icon">⚠️</div>
        <strong>Failed to load release notes</strong>
        <p>${err.message}</p>
      </div>`;
  } finally {
    refreshBtn.classList.remove('loading');
    refreshBtn.disabled = false;
  }
}

/* ── Tweet modal ──────────────────────────────────────────── */
function openTweetModal(entry) {
  tweetTextarea.value = buildTweetText(entry);
  updateCharCount();
  modalOverlay.classList.add('visible');
  tweetTextarea.focus();
}

function closeTweetModal() {
  modalOverlay.classList.remove('visible');
}

function updateCharCount() {
  const len = tweetTextarea.value.length;
  const remaining = TWEET_MAX - len;
  charCount.textContent = `${len} / ${TWEET_MAX}`;
  charCount.className = remaining < 0 ? 'over' : remaining < 30 ? 'warning' : '';
  tweetBtn.disabled = len === 0 || remaining < 0;
}

tweetTextarea.addEventListener('input', updateCharCount);

tweetBtn.addEventListener('click', () => {
  const text = encodeURIComponent(tweetTextarea.value);
  window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank', 'noopener,noreferrer,width=600,height=500');
  closeTweetModal();
});

modalCloseBtn.addEventListener('click', closeTweetModal);
cancelBtn.addEventListener('click', closeTweetModal);
modalOverlay.addEventListener('click', e => { if (e.target === modalOverlay) closeTweetModal(); });
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeTweetModal(); });

/* ── Init ─────────────────────────────────────────────────── */
refreshBtn.addEventListener('click', fetchReleases);
fetchReleases();
