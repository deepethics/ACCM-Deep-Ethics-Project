const SCOPE = new URL(self.registration.scope);
const PREFIX = `accm-deep-ethics-field-navigator:${SCOPE.pathname}:`;
const CACHE = `${PREFIX}v2`;
const SHELL = [
  './', './index.html', './styles.css', './app.js', './pages.json',
  './manifest.webmanifest', './assets/leaf.svg', './assets/john-kuhles.webp',
  './assets/deepethical-art.webp', './assets/truth-and-perspectives.webp',
].map(path => new URL(path, SCOPE).href);
const SHELL_URLS = new Set(SHELL);

self.addEventListener('install', event => {
  event.waitUntil(caches.open(CACHE).then(cache => cache.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', event => {
  event.waitUntil(caches.keys().then(keys => Promise.all(keys
    .filter(key => key.startsWith(PREFIX) && key !== CACHE)
    .map(key => caches.delete(key)))).then(() => self.clients.claim()));
});

self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  const shellUrl = `${url.origin}${url.pathname}`;
  if (event.request.method !== 'GET' || !SHELL_URLS.has(shellUrl)) return;

  event.respondWith((async () => {
    const cache = await caches.open(CACHE);
    let response;
    try {
      response = await fetch(event.request);
    } catch {
      return (await cache.match(shellUrl)) || Response.error();
    }
    if (response.ok && !response.redirected && !url.search) {
      try {
        await cache.put(shellUrl, response.clone());
      } catch {
        // A full or unavailable cache must not discard a successful response.
      }
    }
    return response;
  })());
});
