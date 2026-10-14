/* sw.js — service worker ของพาเที่ยว Dashboard (เฟส 1, 14 ต.ค. 69)
   เป้าหมาย: เปิดหน้าได้เร็ว + เปิดอ่านได้ตอนเน็ตหลุด (app shell cache)
   กติกา: เปลี่ยน CACHE เวอร์ชันเมื่อแก้หน้าเว็บ เพื่อล้างของเก่า */
const CACHE = 'phathiao-dashboard-v1';
const SHELL = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icon-192.png',
  './icon-512.png',
  './apple-touch-icon.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(CACHE)
      .then((c) => c.addAll(SHELL).catch(() => undefined))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;

  // หน้าเว็บ: เอาของใหม่ก่อน (network-first) แล้วค่อยถอยไปของที่ cache ไว้
  if (req.mode === 'navigate') {
    e.respondWith(
      fetch(req)
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put('./index.html', copy)).catch(() => undefined);
          return res;
        })
        .catch(() => caches.match('./index.html'))
    );
    return;
  }

  // ไฟล์นิ่งในเว็บเรา: cache-first
  const url = new URL(req.url);
  if (url.origin === location.origin) {
    e.respondWith(
      caches.match(req).then((hit) => hit || fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => undefined);
        return res;
      }).catch(() => hit))
    );
  }
});
