const DJANGO_BASE_URL = 'https://osome.iu.edu/tools/services-portal-api';
const ENDPOINT = '/api/tools/log-usage';

let _toolName = null;
let _tracked = false;

function init(toolName, options = {}) {
  _toolName = toolName;
  const { trackOnInit = true } = options;
  if (trackOnInit) track();
}

async function track(page = null) {
  const pageVisited = page || _toolName;

  if (!pageVisited) {
    console.warn('[UsageTracker] No tool name provided.');
    return;
  }

  if (_tracked && !page) return;

  try {
    const response = await fetch(`${DJANGO_BASE_URL}${ENDPOINT}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ page_visited: pageVisited })
    });

    if (!response.ok) {
      console.warn('[UsageTracker] Response:', response.status);
      return;
    }

    _tracked = true;
    const result = await response.json();
    console.debug('[UsageTracker] Tracked:', pageVisited, '| record_id:', result.record_id);

  } catch (err) {
    console.warn('[UsageTracker] Failed silently:', err.message);
  }
}

const UsageTracker = { init, track };
export default UsageTracker;