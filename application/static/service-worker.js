const CACHE_NAME = 'kokoro-app-v3';

const urlsToCache = [
  '/',
  '/about',

  // Step 1
  '/step1',
  '/step1/content/children',
  '/step1/content/grief',
  '/step1/content/ptsd',
  '/step1/content/reactions',
  '/step1/test',

  // Step 2
  '/step2',
  '/step2/content/exceptions',
  '/step2/content/recovery',
  '/step2/content/scaling',
  '/step2/test',

  // Step 3
  '/step3',
  '/step3/content/breathing',
  '/step3/content/coping',
  '/step3/content/professional',
  '/step3/content/relaxation',
  '/step3/test',

  // PWA・デザイン
  '/static/css/style.css',
  '/static/icon.png',
  '/static/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
    })
  );
  self.clients.claim();
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') {
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then(response => {
        const responseClone = response.clone();

        caches.open(CACHE_NAME).then(cache => {
          cache.put(event.request, responseClone);
        });

        return response;
      })
      .catch(() => {
        return caches.match(event.request);
      })
  );
});
