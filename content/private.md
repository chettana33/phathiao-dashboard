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
        <h4>โน้ตส่วนตัวของพี่เจ</h4>
        <div class="pv-notes">
          <textarea id="pvn-text" rows="2" maxlength="5000" placeholder="พิมพ์เรื่องส่วนตัว/การเงิน/ลูกค้า… (เห็นเฉพาะตอนล็อกอิน)"></textarea>
          <div class="pv-notes-actions">
            <button class="pv-btn pv-btn-sm" id="pvn-save">บันทึก</button>
            <span class="pv-msg" id="pvn-msg"></span>
          </div>
          <div class="pv-notes-list" id="pvn-list"><span class="pv-sub">กำลังโหลด…</span></div>
        </div>
      </div>
      <div class="pv-box">
        <h4>🔒 ข้อมูลที่ถูกกันออกจากหน้า public</h4>
        <p class="pv-sub">บรรทัดที่ระบบกรองออกก่อนขึ้นหน้าเว็บสาธารณะ (เช่น สถานะพอร์ตจริง · ชื่อโบรก · รหัสภายในของคู่ค้า · credential) — ต้นฉบับครบอยู่ใน Vault เสมอ</p>
        <div class="pv-notes-list" id="pvd-list"><span class="pv-sub">กำลังโหลด…</span></div>
      </div>
      <div class="pv-box">
        <h4>สถานะระบบ</h4>
        <ul>
          <li>อ่านข้อมูลส่วนตัวจากฐานข้อมูลได้เฉพาะบัญชีที่อนุญาต</li>
          <li>เนื้อหาไม่ฝังในไฟล์เว็บ ⇒ ค้นหา/แชร์ลิงก์แล้วไม่เห็นข้อมูล</li>
          <li>หน้าเว็บสาธารณะผ่านด่านกรองอัตโนมัติก่อน build ทุกครั้ง</li>
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

    var ALLOW = ['kimonoland.jp1@gmail.com', 'chettana33@gmail.com'];

    firebase.auth().onAuthStateChanged(function (user) {
      var ok = !!user;
      locked.hidden = ok;
      inside.hidden = !ok;
      if (!ok) { return; }
      var email = (user.email || '').toLowerCase();
      if (ALLOW.indexOf(email) === -1) {
        msg.textContent = 'บัญชีนี้ไม่ได้รับอนุญาตสำหรับพื้นที่ส่วนตัว (' + email + ') — กำลังออกจากระบบ';
        firebase.auth().signOut();
        return;
      }
      who.textContent = 'บัญชี: ' + email + ' · ' + (user.displayName || '');
      loadPrivateNotes();
      loadDigest();
    });

    /* บรรทัดที่ถูกกันออกจากหน้า public (collection private_digest · อ่านได้เฉพาะบัญชีที่ล็อกอิน) */
    function loadDigest() {
      var box = document.getElementById('pvd-list');
      if (!box) return;
      box.innerHTML = '<span class="pv-sub">กำลังโหลด…</span>';
      db.collection('private_digest').orderBy('updatedAt', 'desc').limit(1).get().then(function (snap) {
        if (snap.empty) { box.innerHTML = '<span class="pv-sub">ยังไม่มีบรรทัดที่ถูกกันออก</span>'; return; }
        var doc = snap.docs[0].data();
        var data = {};
        try { data = JSON.parse(doc.payload || '{}'); } catch (e) {}
        var items = data.items || [];
        var when = doc.updatedAt && doc.updatedAt.toDate ? doc.updatedAt.toDate().toLocaleString('th-TH') : '';
        if (!items.length) { box.innerHTML = '<span class="pv-sub">ยังไม่มีบรรทัดที่ถูกกันออก</span>'; return; }
        box.innerHTML = '<div class="pv-note-meta">อัปเดต ' + esc(when) + ' · ' + items.length + ' บรรทัด</div>' +
          items.map(function (it) {
            return '<div class="pv-note"><div>' + esc(it.text) + '</div><div class="pv-note-meta">' +
              esc(it.source || '') + ' · บรรทัด ' + esc(String(it.line || '')) + '</div></div>';
          }).join('');
      }).catch(function (e) {
        box.innerHTML = '<span class="pv-sub">โหลดไม่ได้ (ต้องล็อกอินบัญชีพี่เจ): ' + esc(String(e.message || e)) + '</span>';
      });
    }

    function esc(s) {
      return String(s).replace(/[&<>"']/g, function (c) {
        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
      });
    }

    function loadPrivateNotes() {
      var list = document.getElementById('pvn-list');
      if (!list) return;
      list.innerHTML = '<span class="pv-sub">กำลังโหลด…</span>';
      db.collection('private_notes').get().then(function (snap) {
        if (snap.empty) { list.innerHTML = '<span class="pv-sub">ยังไม่มีโน้ตส่วนตัว</span>'; return; }
        var rows = snap.docs.map(function (d) { return d.data(); });
        rows.sort(function (a, b) {
          var ta = a.created && a.created.toDate ? a.created.toDate().getTime() : 0;
          var tb = b.created && b.created.toDate ? b.created.toDate().getTime() : 0;
          return tb - ta;
        });
        list.innerHTML = rows.slice(0, 30).map(function (r) {
          var when = r.created && r.created.toDate ? r.created.toDate().toLocaleString('th-TH') : '';
          return '<div class="pv-note"><div>' + esc(r.text) + '</div><div class="pv-note-meta">' +
            esc(r.email || '') + ' · ' + esc(when) + '</div></div>';
        }).join('');
      }).catch(function (e) {
        list.innerHTML = '<span class="pv-sub">โหลดไม่ได้: ' + esc(String(e.message || e)) + '</span>';
      });
    }

    var saveBtn = document.getElementById('pvn-save');
    if (saveBtn) {
      saveBtn.addEventListener('click', function () {
        var ta = document.getElementById('pvn-text');
        var m = document.getElementById('pvn-msg');
        var user = firebase.auth().currentUser;
        var text = (ta && ta.value || '').trim();
        if (!user) { if (m) m.textContent = 'ต้องล็อกอินก่อน'; return; }
        if (!text) { if (m) m.textContent = 'พิมพ์ข้อความก่อน'; return; }
        if (m) m.textContent = 'กำลังบันทึก…';
        db.collection('private_notes').add({
          text: text,
          email: user.email || '',
          created: firebase.firestore.FieldValue.serverTimestamp()
        }).then(function () {
          if (ta) ta.value = '';
          if (m) m.textContent = '✅ บันทึกแล้ว (เห็นเฉพาะบัญชีพี่เจ)';
          loadPrivateNotes();
        }).catch(function (e) {
          if (m) m.textContent = '❌ บันทึกไม่ได้: ' + String(e.message || e);
        });
      });
    }

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
