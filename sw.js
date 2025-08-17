
// Service Worker for CDN Performance Enhancement
const CACHE_NAME = 'dryalle-v1.1';
const STATIC_CACHE = 'static-v1.1';
const DYNAMIC_CACHE = 'dynamic-v1.1';

const STATIC_ASSETS = [
    '/',
    '/styles.css',
    '/blog-unified.css',
    '/fonts/roboto.woff2',
    '/images/logo.webp',
    '/offline.html'
];

// Install event
self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(STATIC_CACHE)
            .then(cache => cache.addAll(STATIC_ASSETS))
            .then(() => self.skipWaiting())
    );
});

// Activate event
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys()
            .then(keys => {
                return Promise.all(
                    keys.filter(key => key !== STATIC_CACHE && key !== DYNAMIC_CACHE)
                        .map(key => caches.delete(key))
                );
            })
            .then(() => self.clients.claim())
    );
});

// Fetch event with advanced caching strategies
self.addEventListener('fetch', event => {
    const { request } = event;
    const url = new URL(request.url);
    
    // Skip non-GET requests
    if (request.method !== 'GET') return;
    
    // Skip external requests
    if (url.origin !== location.origin) return;
    
    // Handle different types of requests
    if (url.pathname.includes('/blog/')) {
        // Blog pages - Network first, then cache
        event.respondWith(networkFirstStrategy(request));
    } else if (url.pathname.includes('/images/') || url.pathname.includes('.webp')) {
        // Images - Cache first, then network
        event.respondWith(cacheFirstStrategy(request));
    } else if (url.pathname.includes('.css') || url.pathname.includes('.js')) {
        // Static assets - Cache first
        event.respondWith(cacheFirstStrategy(request));
    } else {
        // HTML pages - Network first
        event.respondWith(networkFirstStrategy(request));
    }
});

// Cache first strategy
async function cacheFirstStrategy(request) {
    const cachedResponse = await caches.match(request);
    if (cachedResponse) {
        return cachedResponse;
    }
    
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.status === 200) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        console.log('Network request failed:', error);
        return new Response('Offline', { status: 503 });
    }
}

// Network first strategy
async function networkFirstStrategy(request) {
    try {
        const networkResponse = await fetch(request);
        if (networkResponse.status === 200) {
            const cache = await caches.open(DYNAMIC_CACHE);
            cache.put(request, networkResponse.clone());
        }
        return networkResponse;
    } catch (error) {
        const cachedResponse = await caches.match(request);
        if (cachedResponse) {
            return cachedResponse;
        }
        
        // Return offline page for HTML requests
        if (request.headers.get('accept').includes('text/html')) {
            return caches.match('/offline.html');
        }
        
        return new Response('Offline', { status: 503 });
    }
}
        