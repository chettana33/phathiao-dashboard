/* sw.js — service worker ของพาเที่ยว Dashboard (เฟส 1 + แก้ 14 ต.ค. 69)
   บทเรียนสำคัญ (14 ต.ค. 69): รอบแรก cache index.html ไว้แล้วเสิร์ฟแบบ cache-first
   ⇒ ผู้ใช้เห็นหน้าเก่าค้างหลัง deploy ใหม่ (เจอจริงตอนทดสอบโน้ตต่อการ์ด)
   กติกาปัจจุบัน: หน้าเว็บ = network-first + cache:'no-store' · ไฟล์นิ่ง (รูป/ไอคอน/manifest) = cache-first
   เปลี่ยน CACHE เวอร์ชันทุกครั้งที่แก้หน้าเว็บ เพื่อล้างของเก่า */
const CACHE = 'phathiao-dashboard-v2';
const SHELL = [
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

  const url = new URL(req.url);
  if (url.origin !== location.origin) return;          // ปล่อยผ่าน (Firebase/อื่น ๆ)

  // 1) หน้าเว็บ (HTML) = เอาของใหม่เสมอ · ถ้าเน็ตหลุดค่อยใช้ของที่ cache ไว้
  const isHtml = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  if (isHtml) {
    e.respondWith(
      fetch(req, { cache: 'no-store' })
        .then((res) => {
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put('./index.html', copy)).catch(() => undefined);
          return res;
        })
        .catch(() => caches.match('./index.html'))
    );
    return;
  }

  // 2) ไฟล์นิ่ง = cache-first (เร็ว) แล้วค่อยอัปเดตเบื้องหลัง
  e.respondWith(
    caches.match(req).then((hit) => {
      const net = fetch(req).then((res) => {
        const copy = res.clone();
        caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => undefined);
        return res;
      }).catch(() => hit);
      return hit || net;
    })
  );
});
