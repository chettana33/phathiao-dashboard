---
title: "ส่วนตัว 🔒 — พื้นที่ที่ต้องล็อกอิน"
type: "dashboard"
---

# 🔒 พื้นที่ส่วนตัว (ต้องล็อกอิน)

> หน้านี้มีไว้เก็บเรื่องที่ **ไม่ควรอยู่ในเว็บสาธารณะ** (การเงิน · ข้อมูลลูกค้า · ราคาทุน/กำไร)
> กติกา: เนื้อหาจริงจะไม่ถูกฝังในไฟล์เว็บ — ดึงจากฐานข้อมูลเฉพาะเมื่อ **ล็อกอินด้วยบัญชีพี่เจ** เท่านั้น

```html
<div class="pv-wrap">

  <div class="pv-card" id="pv-locked">
    <div class="pv-icon">🔐</div>
    <h2 class="pv-title">ยังไม่ได้เข้าสู่ระบบ</h2>
    <p class="pv-sub">เข้าใช้ด้วยบัญชี Google ของพี่เจ เพื่อเปิดพื้นที่ส่วนตัว</p>
    <button class="pv-btn" id="pv-login">เข้าสู่ระบบด้วย Google</button>
    <div class="pv-msg" id="pv-msg"></div>
    <div class="pv-help" id="pv-help" hidden>
      <b>ยังเปิดระบบล็อกอินไม่ได้ — ต้องทำที่คอนโซล 2 คลิก (พี่เจเท่านั้น):</b>
      <ol>
        <li>เปิด <a href="https://console.firebase.google.com/project/phathiao-dashboard/authentication" target="_blank" rel="noopener">Firebase → Authentication</a> แล้วกด <b>Get started</b></li>
        <li>แท็บ <b>Sign-in method</b> → กด <b>Google</b> → Enable → Save<br>
            และเช็ค <b>Settings → Authorized domains</b> ว่ามี <code>chettana33.github.io</code></li>
      </ol>
      <p class="pv-sub">เสร็จแล้วกลับมากดปุ่มนี้อีกครั้ง — ระบบจะเข้าได้ทันที (ไม่ต้องแก้โค้ดอะไรเพิ่ม)</p>
    </div>
  </div>

  <div class="pv-card pv-ok" id="pv-in" hidden>
    <div class="pv-icon">✅</div>
    <h2 class="pv-title">เข้าสู่ระบบแล้ว</h2>
    <p class="pv-sub" id="pv-who">-</p>
    <div class="pv-grid">
      <div class="pv-box">
        <h4>จะมีอะไรในนี้ (กำลังทำต่อ)</h4>
        <ul>
          <li>สรุปการเงิน/รายรับรายจ่ายที่ไม่ขึ้นหน้าสาธารณะ</li>
          <li>รายชื่อ/โน้ตลูกค้าและซัพพลายเออร์</li>
          <li>ราคาทุน–กำไร และใบเสนอราคาฉบับจริง</li>
        </ul>
      </div>
      <div class="pv-box">
        <h4>สถานะระบบ</h4>
        <ul>
          <li>อ่านข้อมูลส่วนตัวจากฐานข้อมูลได้เฉพาะบัญชีที่อนุญาต</li>
          <li>เนื้อหาไม่ฝังในไฟล์เว็บ ⇒ ค้นหา/แชร์ลิงก์แล้วไม่เห็นข้อมูล</li>
        </ul>
      </div>
    </div>
    <button class="pv-btn pv-btn-ghost" id="pv-logout">ออกจากระบบ</button>
  </div>

</div>

<script>
(function () {
  function whenReady(fn) {
    if (window.__pdReady) { fn(); return; }
    window.addEventListener('pd:ready', function () { fn(); }, { once: true });
  }

  whenReady(function () {
    var btnIn = document.getElementById('pv-login');
    var btnOut = document.getElementById('pv-logout');
    var msg = document.getElementById('pv-msg');
    var help = document.getElementById('pv-help');
    var locked = document.getElementById('pv-locked');
    var inside = document.getElementById('pv-in');
    var who = document.getElementById('pv-who');

    function friendly(code, raw) {
      if (code === 'auth/configuration-not-found') {
        help.hidden = false;
        return 'ระบบล็อกอินของโปรเจกต์ยังไม่ถูกเปิดใช้งาน';
      }
      if (code === 'auth/unauthorized-domain') {
        help.hidden = false;
        return 'โดเมนนี้ยังไม่ได้รับอนุญาต — ต้องเพิ่ม chettana33.github.io ใน Authorized domains';
      }
      if (code === 'auth/popup-blocked') { return 'เบราว์เซอร์บล็อกหน้าต่างล็อกอิน — ลองกดอีกครั้ง หรืออนุญาตป๊อปอัป'; }
      if (code === 'auth/popup-closed-by-user' || code === 'auth/cancelled-popup-request') { return 'ปิดหน้าต่างล็อกอินก่อนเสร็จ — ลองอีกครั้ง'; }
      return 'เข้าใช้ไม่สำเร็จ: ' + (code || raw || 'ไม่ทราบสาเหตุ');
    }

    firebase.auth().onAuthStateChanged(function (user) {
      var ok = !!user;
      locked.hidden = ok;
      inside.hidden = !ok;
      if (ok) { who.textContent = 'บัญชี: ' + (user.email || '') + ' · ' + (user.displayName || ''); }
    });

    btnIn.addEventListener('click', function () {
      msg.textContent = 'กำลังเปิดหน้าต่างล็อกอิน…';
      var provider = new firebase.auth.GoogleAuthProvider();
      provider.setCustomParameters({ prompt: 'select_account' });
      firebase.auth().signInWithPopup(provider)
        .then(function () { msg.textContent = ''; })
        .catch(function (e) {
          var code = (e && e.code) || '';
          msg.textContent = friendly(code, e && e.message);
        });
    });

    btnOut.addEventListener('click', function () { firebase.auth().signOut(); });
  });
})();
</script>
```
