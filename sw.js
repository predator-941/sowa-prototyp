// Minimalny service worker: pozwala zainstalować grę jak aplikację. Niczego nie zapisuje w pamięci podręcznej,
// więc każda nowa wersja z Netlify od razu działa.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", () => {});
