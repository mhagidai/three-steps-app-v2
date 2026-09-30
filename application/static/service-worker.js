const CACHE_NAME = 'kokoro-app-v1';

const urlsToCache = [
  '/',
  '/static/css/style.css',
  '/static/icon.png',
  '/static/manifest.json'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(urlsToCache))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    fetch(event.request)
      .then(response => {
        const responseClone = response.clone();

        caches.open(CACHE_NAME)
          .then(cache => {
            cache.put(event.request, responseClone);
          });

        return response;
      })
      .catch(() => caches.match(event.request))
  );
});
