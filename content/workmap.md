---
title: "แผนที่งาน — เลือกงานที่อยากดู แล้วเห็นขั้นตอนทันที"
type: "dashboard"
---

# 🧭 แผนที่งาน (Work Map)

> เปิดมาเห็น **ทุกงานในจอเดียว** → กดช่องงานที่อยากดู → รายละเอียดเปิดในหน้านี้ ไม่ต้องเปลี่ยนหน้า
> เรียง **งานที่กำลังทำอยู่ก่อน** แล้วต่อด้วยงานที่รอพี่เจ/รอของ · ตัวเลขงานค้างจาก checkpoint รอบล่าสุด · อัปเดตโดยพาเที่ยวทุกครั้งที่ปิดงาน

```html
<div class="wm-toolbar">
  <div class="wm-toolbar-title">งานทั้งหมด <b>10</b> การ์ด · เรียงงานที่กำลังทำอยู่ก่อน</div>
  <div class="wm-tools">
    <input class="wm-search" id="wm-search" type="search" placeholder="ค้นหางาน… (เช่น affiliate · รอพี่เจ)" aria-label="ค้นหางาน">
    <button class="wm-back" id="wm-back" hidden>← กลับไปดูงานทั้งหมด</button>
  </div>
</div>
<div class="wm-live" id="wm-live"><span class="wm-live-dot"></span><span class="wm-live-text">กำลังตรวจข้อมูลสด…</span></div>
<div class="wm-last" id="wm-last" hidden></div>

<div class="wm-group-title">🔵 กำลังทำอยู่ (4)</div>
<div class="wm-tiles wm-list" id="wm-list">

  <button class="wm-tile" data-wm="pc009">
    <span class="wm-tile-code">PC-009</span>
    <span class="wm-tile-name">ช่อง Gochisou — ทำคลิปและวัดผล</span>
    <span class="wm-tile-meta">🔵 กำลังทำ · งานค้าง 25</span>
    <span class="wm-tile-next">ถัดไป: ปักหมุดคอมเมนต์ IG ใบ 2/3</span>
  </button>

  <button class="wm-tile" data-wm="pc017">
    <span class="wm-tile-code">PC-017</span>
    <span class="wm-tile-name">Affiliate Marketing — ทำ affiliate เอง</span>
    <span class="wm-tile-meta">🔵 กำลังทำ · งานค้าง 11</span>
    <span class="wm-tile-next">ถัดไป: แผนที่โปรแกรม affiliate</span>
  </button>

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-011</span>
    <span class="wm-tile-name">DSH Tooling / ระบบความรู้</span>
    <span class="wm-tile-meta">🔵 กำลังทำ · งานค้าง 4</span>
    <span class="wm-tile-next">ยังไม่มีหน้ารายละเอียด — กำลังทำ</span>
  </button>

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-006</span>
    <span class="wm-tile-name">เรียนเทรด Meawbin</span>
    <span class="wm-tile-meta">🔵 กำลังเรียน · งานค้าง 3</span>
    <span class="wm-tile-next">ยังไม่มีหน้ารายละเอียด — กำลังทำ</span>
  </button>

</div>

<div class="wm-group-title">🟡 รอพี่เจ / รอของ (5)</div>
<div class="wm-tiles wm-list">

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-012</span>
    <span class="wm-tile-name">Owner Mail + งานอัตโนมัติในเครื่อง</span>
    <span class="wm-tile-meta">🟡 รอพี่เจ · งานค้าง 5</span>
    <span class="wm-tile-next">ต้องรันคำสั่งแบบ admin 1 ครั้ง</span>
  </button>

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-015</span>
    <span class="wm-tile-name">MT5 Trading</span>
    <span class="wm-tile-meta">🟡 รอพี่เจตัดสิน · งานค้าง 5</span>
    <span class="wm-tile-next">รอตัดสินกติกา "ศิลปะ" + ตั้ง SL จริง</span>
  </button>

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-016</span>
    <span class="wm-tile-name">ลงราคาค่าโดยสาร 千栄交通 (unbin)</span>
    <span class="wm-tile-meta">🟡 รอต้นสังกัด · งานค้าง 4</span>
    <span class="wm-tile-next">รอบ 便/เดือนถัดไปรอต้นสังกัด</span>
  </button>

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-003</span>
    <span class="wm-tile-name">B2B / Smile Travel + หาลูกค้าใหม่</span>
    <span class="wm-tile-meta">🟡 รอพี่เจอนุมัติ · งานค้าง 2</span>
    <span class="wm-tile-next">อนุมัติส่งซ้ำ Next Trip Holiday</span>
  </button>

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-001</span>
    <span class="wm-tile-name">Master Data (โรงแรม/ร้านอาหาร/รถ)</span>
    <span class="wm-tile-meta">🟡 รอไฟล์จากพี่เจ · งานค้าง 1</span>
    <span class="wm-tile-next">รอไฟล์ Google Takeout ชุดใหม่</span>
  </button>

</div>

<div class="wm-group-title">⏳ รอคำสั่งเริ่ม (1)</div>
<div class="wm-tiles wm-list">

  <button class="wm-tile is-empty" disabled>
    <span class="wm-tile-code">PC-008</span>
    <span class="wm-tile-name">ย้ายบัญชี Google</span>
    <span class="wm-tile-meta">⏳ รอคำสั่งเริ่ม · งานค้าง 1</span>
    <span class="wm-tile-next">รอพี่เจสั่ง "เริ่มย้าย" (แผน 36 ขั้นพร้อม)</span>
  </button>

</div>

<article class="wm wm-detail" id="pc009" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-009 · Gochisou Content</div>
      <h2 class="wm-title">ช่อง Gochisou — ทำคลิปและวัดผล <span class="wm-sub">TikTok · Facebook Page · Instagram</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag info wm-status">🔵 กำลังทำ</span>
      <div class="wm-progress" title="ความคืบหน้ารวม 8 ส่วน"><span class="wm-bar" style="--p:78%"></span><b>78%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    ให้คนดูคลิปแล้ว <strong>ทัก LINE / จองร้าน</strong> ผ่านช่องของเรา — วัดด้วย KPI รายสัปดาห์ (วิว · ทัก LINE · ใบเสนอราคา)
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>ฐานรากของช่อง (เสร็จครบแล้ว)</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">ด่านตรวจ</span>QC ภาพ+เสียงอัตโนมัติ<em>บังคับก่อนโพสต์ทุกคลิป</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">LINE</span>LINE OA @gochisou + ริชเมนู<em>เปิดใช้แล้ว 13 ก.ย. 69</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">ของแจก</span>โพยร้านดัง + หน้า /phoy/<em>ใช้งานได้แล้ว</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">ช่องทาง</span>Facebook Page + Instagram<em>โพสต์ Reels ได้แล้ว</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>ผลิตคลิปและโพสต์</div>
    <div class="wm-steps">
      <div class="wm-step is-doing"><span class="wm-n">80%</span>ระบบผลิตคลิป (MiniMax H3 → ตัดต่อ → เสียง → CTA)<em>คลิป 1–6 ปิดครบ · ล็อกวิธีผลิตแล้ว</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-wait"><span class="wm-n">30%</span>คลิปว้าว 3 แนว (UGC / หนังสั้นหักมุม / one-take)<em>รอพี่เจเติมเครดิต — อนุมัติแนวแล้ว</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>ปลายทางและวัดผล</div>
    <div class="wm-steps">
      <div class="wm-step is-doing"><span class="wm-n">50%</span>ปลายทาง «กดต่อ» (ลิงก์ไบโอ + GA4)<em>รอ Measurement ID (ยังว่าง = ยังไม่เก็บข้อมูล)</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-doing"><span class="wm-n">60%</span>แผน 3 เดือน + KPI รายสัปดาห์<em>เริ่มใช้แล้ว · ตัวเลขยังไม่ถึงเป้า ⇒ HOLD</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>ฐานรากช่องครบ 4 ส่วน (ด่าน QC · LINE OA · ของแจก · FB+IG)</li>
        <li>คลิป Batch1 ชุดแรกผลิตและโพสต์ครบ 3 ช่อง</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>ปักหมุดคอมเมนต์ CTA บน IG ใบ 2/3 (หลังโพสต์ 15–16 ต.ค. 18:00) — ทำได้ในแอปมือถือ</li>
        <li>เตรียมคลิปถัดไปตามแผน 3 เดือน (รอเครดิตเจน)</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>ชื่อโปรไฟล์ IG (@gochisou_booking) — ยังว่าง</li>
        <li>GA4 Measurement ID</li>
        <li>งบเครดิตสำหรับคลิปว้าว 3 แนว</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-009">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-009">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-009"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-009"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-009</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc017" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-017 · Affiliate Marketing</div>
      <h2 class="wm-title">การตลาดแบบพันธมิตร <span class="wm-sub">เราทำ affiliate เอง — รับค่าคอมจากแบรนด์อื่น</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag info wm-status">🔵 กำลังทำ · ช่วงศึกษา</span>
      <div class="wm-progress" title="ความคืบหน้ารวม"><span class="wm-bar" style="--p:15%"></span><b>15%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    หา <strong>สินค้าที่มีเทรนด์/ขายดี</strong> → ทำ <strong>คลิป</strong> → โพสต์ผ่านช่องทางของเรา → รับ <strong>ค่าคอมมิชชัน</strong>
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>หาคำตอบให้ครบก่อนลงมือ</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>ล็อกโจทย์: เราทำ affiliate เอง</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-doing"><span class="wm-n">②</span>แผนที่โปรแกรม affiliate (ญี่ปุ่น + ไทย)<em>ชื่อโปรแกรม · เกณฑ์สมัคร · ค่าคอม</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">③</span>เลือกสายสินค้าที่เข้ากับเรา 3 อันดับ</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">④</span>โมเดลรายได้ + เงื่อนไขจ่ายจริง</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑤</span>ด่านกฎหมาย/ภาษี + เปิดเผยว่าเป็นลิงก์โฆษณา</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑥</span>ประเมินความเสี่ยง (บัญชีถูกระงับ · เงินค้าง)</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑧</span>ใบตัดสิน: ทำ/ไม่ทำ + เริ่มที่ไหน</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>หาสินค้า (งานของพาเที่ยว)</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑨</span>หาสินค้าที่มีเทรนด์/ขายดี<em>ส่งลิสต์สั้น 3–5 ชิ้น</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-wait"><span class="wm-n">⑩</span>พี่เจเลือกสินค้า<em>ด่านก่อนผลิตทุกครั้ง</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>ทำคลิปและวัดผล</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑦</span>ทดลองเล็ก 1 ช่องทาง<em>1 สินค้า × 1 คลิป × 2–4 สัปดาห์</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑪</span>ผลิตคลิป → โพสต์ → เก็บลิงก์ติดตาม → วัดค่าคอมจริง</div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>เปิดการ์ดงาน + ตั้งกติกากันพลาด (ห้าม AI สมัคร/ผูกบัญชีเอง)</li>
        <li>พี่เจตัดสินแล้ว: ทำ affiliate เอง</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>ทำ «แผนที่โปรแกรม affiliate» ให้เสร็จ — พาเที่ยวทำเอง ไม่ต้องรอพี่เจ</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>ยังไม่มีอะไรต้องรอตอนนี้ — จะรอตอน ⑩ เลือกสินค้า</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-017">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-017">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-017"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-017"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-017</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<script>
(function () {
  var tiles = Array.prototype.slice.call(document.querySelectorAll('.wm-tiles .wm-tile'));
  var clickable = tiles.filter(function (t) { return t.dataset.wm; });
  var panels = Array.prototype.slice.call(document.querySelectorAll('.wm-detail'));
  var back = document.getElementById('wm-back');
  var search = document.getElementById('wm-search');
  var lastChip = document.getElementById('wm-last');

  function setChrome(id) {
    document.querySelectorAll('.wm-list, .wm-group-title').forEach(function (el) { el.hidden = !!id; });
    panels.forEach(function (p) { p.hidden = (p.id !== id); });
    tiles.forEach(function (t) { t.classList.toggle('is-active', t.dataset.wm === id); });
    back.hidden = !id;
    if (lastChip) lastChip.hidden = !!id;
    if (id) { document.getElementById(id).scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  }

  function remember(id) {
    try { localStorage.setItem('pd_last_card', id); } catch (e) {}
  }

  function openCard(id, pushHash) {
    setChrome(id);
    renderLast();
    if (id) { loadCardNotes(id.replace('pc', 'PC-')); }
    if (id) {
      remember(id);
      if (pushHash && location.hash !== '#workmap/' + id) { location.hash = 'workmap/' + id; }
    } else if (pushHash && location.hash !== '#workmap') {
      location.hash = 'workmap';
    }
  }

  function hashCard() {
    var parts = (location.hash || '').replace(/^#/, '').split('/');
    return parts[0] === 'workmap' ? (parts[1] || '') : null;
  }

  clickable.forEach(function (t) {
    t.addEventListener('click', function () { openCard(t.dataset.wm, true); });
  });
  if (back) { back.addEventListener('click', function () { openCard(null, true); }); }

  // เปิด/ปิดตาม URL (กด refresh แล้วอยู่หน้าเดิม · ปุ่มย้อนกลับของมือถือใช้ได้)
  window.addEventListener('hashchange', function () {
    var id = hashCard();
    if (id === null) { return; }
    setChrome(id || null);
  });
  window.addEventListener('pd:route', function (e) {
    var h = (e.detail && e.detail.hash) || location.hash.replace(/^#/, '');
    if (h.indexOf('workmap') !== 0) { return; }
    var cid = h.split('/')[1] || null;
    setChrome(cid);
    if (cid) { loadCardNotes(cid.replace('pc', 'PC-')); }
  });

  // ค้นหางาน
  if (search) {
    search.addEventListener('input', function () {
      var q = (search.value || '').trim().toLowerCase();
      document.querySelectorAll('.wm-tiles').forEach(function (grid) {
        var visible = 0;
        grid.querySelectorAll('.wm-tile').forEach(function (t) {
          var ok = !q || (t.textContent || '').toLowerCase().indexOf(q) >= 0;
          t.hidden = !ok;
          if (ok) visible++;
        });
        var title = grid.previousElementSibling;
        if (title && title.classList.contains('wm-group-title')) { title.hidden = (visible === 0); }
      });
    });
  }

  // ป้าย "ดูล่าสุด"
  function renderLast() {
    if (!lastChip) return;
    var id = '';
    try { id = localStorage.getItem('pd_last_card') || ''; } catch (e) {}
    var tile = id ? document.querySelector('.wm-tile[data-wm="' + id + '"]') : null;
    if (!tile) { lastChip.hidden = true; return; }
    var name = tile.querySelector('.wm-tile-name');
    lastChip.hidden = false;
    lastChip.innerHTML = '🕘 ดูครั้งล่าสุด: ';
    var b = document.createElement('button');
    b.className = 'wm-last-btn';
    b.textContent = name ? name.textContent : id;
    b.addEventListener('click', function () { openCard(id, true); });
    lastChip.appendChild(b);
  }

  /* ---------- เฟส 2: โน้ตต่อการ์ด (Firestore) ---------- */
  function notesListFor(card) { return document.querySelector('.wm-notes-list[data-card="' + card + '"]'); }

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  function loadCardNotes(card) {
    var box = notesListFor(card);
    if (!box) return;
    box.innerHTML = '<span class="muted">กำลังโหลดโน้ต…</span>';
    try {
      db.collection('card_notes').where('card', '==', card).get()
        .then(function (snap) {
          if (snap.empty) { box.innerHTML = '<span class="muted">ยังไม่มีโน้ตของงานนี้</span>'; return; }
          var rows = snap.docs.map(function (d) { return d.data(); });
          rows.sort(function (a, b) {
            var ta = a.created && a.created.toDate ? a.created.toDate().getTime() : 0;
            var tb = b.created && b.created.toDate ? b.created.toDate().getTime() : 0;
            return tb - ta;
          });
          box.innerHTML = rows.slice(0, 20).map(function (r) {
            var when = r.created && r.created.toDate ? r.created.toDate().toLocaleString('th-TH') : '';
            return '<div class="wm-note"><div>' + esc(r.text) + '</div><div class="wm-note-meta">✍️ ' +
              esc(r.name || 'พี่เจ') + ' · ' + esc(when) + '</div></div>';
          }).join('');
        })
        .catch(function (e) {
          box.innerHTML = '<span class="muted">โหลดโน้ตไม่ได้: ' + esc(String(e.message || e)) + '</span>';
        });
    } catch (e) {
      box.innerHTML = '<span class="muted">ต่อฐานข้อมูลไม่ได้: ' + esc(String(e.message || e)) + '</span>';
    }
  }

  Array.prototype.slice.call(document.querySelectorAll('.wm-note-save')).forEach(function (btn) {
    btn.addEventListener('click', function () {
      var card = btn.dataset.card;
      var ta = document.querySelector('.wm-notes[data-card="' + card + '"] .wm-note-text');
      var msg = document.querySelector('.wm-note-msg[data-card="' + card + '"]');
      var text = (ta && ta.value || '').trim();
      if (!text) { if (msg) msg.textContent = 'พิมพ์ข้อความก่อน'; return; }
      if (msg) msg.textContent = 'กำลังบันทึก…';
      db.collection('card_notes').add({
        card: card,
        text: text,
        name: 'พี่เจ',
        created: firebase.firestore.FieldValue.serverTimestamp()
      }).then(function () {
        if (ta) ta.value = '';
        if (msg) msg.textContent = '✅ บันทึกแล้ว';
        loadCardNotes(card);
      }).catch(function (e) {
        if (msg) msg.textContent = '❌ บันทึกไม่ได้: ' + String(e.message || e);
      });
    });
  });

  /* ---------- เฟส 2: สถานะสดจาก Firestore (dashboard_state) ---------- */
  function renderLive(doc) {
    var live = document.getElementById('wm-live');
    if (!live) return;
    var text = live.querySelector('.wm-live-text');
    if (!doc) {
      live.classList.add('is-stale');
      if (text) text.textContent = 'ยังไม่ได้ดันสถานะสด (ใช้ตัวเลขจากไฟล์ล่าสุด)';
      return;
    }
    var data = {};
    try { data = JSON.parse(doc.payload || '{}'); } catch (e) {}
    var when = doc.updatedAt && doc.updatedAt.toDate ? doc.updatedAt.toDate().toLocaleString('th-TH') : '';
    (data.cards || []).forEach(function (c) {
      var codeEl = Array.prototype.slice.call(document.querySelectorAll('.wm-tile-code'))
        .filter(function (el) { return el.textContent.trim() === c.code; })[0];
      if (!codeEl) return;
      var tile = codeEl.closest('.wm-tile');
      var meta = tile && tile.querySelector('.wm-tile-meta');
      if (meta) { meta.textContent = meta.textContent.replace(/งานค้าง\s*\d+/, 'งานค้าง ' + c.pending); }
    });
    live.classList.remove('is-stale');
    live.classList.add('is-fresh');
    if (text) {
      text.textContent = 'ข้อมูลสด · อัปเดต ' + when + ' · งานค้างรวม ' + (data.pendingTotal || 0) +
        ' · checkpoint ' + (data.checkpointDate || '-');
    }
  }

  function loadLive() {
    try {
      db.collection('dashboard_state').orderBy('updatedAt', 'desc').limit(1).get()
        .then(function (snap) { renderLive(snap.empty ? null : snap.docs[0].data()); })
        .catch(function () { renderLive(null); });
    } catch (e) { renderLive(null); }
  }

  var initial = hashCard();
  if (initial) { openCard(initial, false); } else { renderLast(); }
  loadLive();
})();
</script>
```
