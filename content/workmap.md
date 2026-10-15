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
    <span class="wm-tile-meta">🔵 กำลังทำ · งานค้าง 8</span>
    <span class="wm-tile-next">ถัดไป: แผนที่โปรแกรม affiliate</span>
  </button>

  <button class="wm-tile" data-wm="pc011">
    <span class="wm-tile-code">PC-011</span>
    <span class="wm-tile-name">DSH Tooling / ระบบความรู้</span>
    <span class="wm-tile-meta">🔵 กำลังทำ · งานค้าง 4</span>
    <span class="wm-tile-next">ถัดไป: ตัดสินการจัดกลุ่มโน้ตที่เหลือ</span>
  </button>

  <button class="wm-tile" data-wm="pc006">
    <span class="wm-tile-code">PC-006</span>
    <span class="wm-tile-name">เรียนเทรด Meawbin</span>
    <span class="wm-tile-meta">🔵 กำลังเรียน · งานค้าง 3</span>
    <span class="wm-tile-next">ถัดไป: บท 52 — EP04 ทบทวน Work Shop Grid Forex</span>
  </button>

</div>

<div class="wm-group-title">🟡 รอพี่เจ / รอของ (5)</div>
<div class="wm-tiles wm-list">

  <button class="wm-tile" data-wm="pc012">
    <span class="wm-tile-code">PC-012</span>
    <span class="wm-tile-name">Owner Mail + งานอัตโนมัติในเครื่อง</span>
    <span class="wm-tile-meta">🟡 รอพี่เจ · งานค้าง 5</span>
    <span class="wm-tile-next">ต้องรันคำสั่งแบบ admin 1 ครั้ง</span>
  </button>

  <button class="wm-tile" data-wm="pc015">
    <span class="wm-tile-code">PC-015</span>
    <span class="wm-tile-name">MT5 Trading</span>
    <span class="wm-tile-meta">🟡 รอพี่เจตัดสิน · งานค้าง 5</span>
    <span class="wm-tile-next">รอตัดสินกติกา "ศิลปะ" + ตั้ง SL จริง</span>
  </button>

  <button class="wm-tile" data-wm="pc016">
    <span class="wm-tile-code">PC-016</span>
    <span class="wm-tile-name">ลงราคาค่าโดยสาร 千栄交通 (unbin)</span>
    <span class="wm-tile-meta">🟡 รอต้นสังกัด · งานค้าง 4</span>
    <span class="wm-tile-next">รอบ 便/เดือนถัดไปรอต้นสังกัด</span>
  </button>

  <button class="wm-tile" data-wm="pc003">
    <span class="wm-tile-code">PC-003</span>
    <span class="wm-tile-name">B2B / Smile Travel + หาลูกค้าใหม่</span>
    <span class="wm-tile-meta">🟡 รอพี่เจอนุมัติ · งานค้าง 2</span>
    <span class="wm-tile-next">อนุมัติส่งซ้ำ Next Trip Holiday</span>
  </button>

  <button class="wm-tile" data-wm="pc001">
    <span class="wm-tile-code">PC-001</span>
    <span class="wm-tile-name">Master Data (โรงแรม/ร้านอาหาร/รถ)</span>
    <span class="wm-tile-meta">🟡 รอไฟล์จากพี่เจ · งานค้าง 1</span>
    <span class="wm-tile-next">รอไฟล์ Google Takeout ชุดใหม่</span>
  </button>

</div>

<div class="wm-group-title">⏳ รอคำสั่งเริ่ม (1)</div>
<div class="wm-tiles wm-list">

  <button class="wm-tile" data-wm="pc008">
    <span class="wm-tile-code">PC-008</span>
    <span class="wm-tile-name">ย้ายบัญชี Google</span>
    <span class="wm-tile-meta">⏳ รอคำสั่งเริ่ม · งานค้าง 1</span>
    <span class="wm-tile-next">รอพี่เจสั่ง "เริ่มย้าย" — §4 เปิดค้าง 29 ขั้น</span>
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

<article class="wm wm-detail" id="pc011" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-011 · DSH Tooling / Knowledge Ops</div>
      <h2 class="wm-title">ระบบเครื่องมือ DSH และสมองความรู้ <span class="wm-sub">backlog ระบบความรู้ + งานอัตโนมัติ</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag good wm-status">🔵 งานหลักปิดแล้ว · เหลือข้อใหม่ 4</span>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    เป็นเจ้าของงานระบบ DSH/ความรู้ทั้งหมด (config · corpus · ส่วน 8 · cloud scheduler) ให้ทุกงานค้าง<strong>มีเจ้าของชัด</strong> และระบบความรู้ทำงานอัตโนมัติได้จริง
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>วางราก config + เครื่องมือ</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>B20 backup config DSH<em>กัน config หาย/BOM crash ซ้ำ</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">②</span>B21 dsh-find-plugin verify หลัง restart host</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>สมองความรู้ + เฝ้าระบบคลาวด์</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">③</span>corpus รอบ 3 — เพิ่ม rules/index/BOOT<em>store 689 chunks</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">④</span>cloud scheduler เข้า task_health</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑤</span>re-oauth cloudplatform token (7 ก.ย.)<em>3 jobs ENABLED</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑥</span>re-oauth รอบ 2 (9 ก.ย.)</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑦</span>firebase token watchdog (8 ก.ย.)</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>อัตโนมัติปิดงาน + CI/cloud</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">⑧</span>ส่วน 8 — /work auto-start + review มุมคนนอก</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑨</span>SA + WIF + IAM สำหรับงาน CI</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑩</span>workflow รันเขียวจริง<em>cloud_health · vault_restore_test</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">4</span>ซ่อมเครื่องมือ + probe</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">⑪</span>serena memory fix — param memory_name 4 จุด</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑫</span>serena recipe patch รอบ 2</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑬</span>MiniMax Design study + driver mcp_mm.py</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑭</span>probe MCP ตอนแอปปิด<em>OK 6 · FAIL 0 · DOWN-OK 1</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑮</span>refresh_card_index atomic + ตัวตรวจข้อความถัดไป<em>เทสต์ 13/13</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>ปิดการ์ดรอบหลัก 5 ต.ค. 69 · plugin ceiling เฝ้าอัตโนมัติทุก 30 นาที (เทสต์ 27/27)</li>
        <li>A/B ponytail 2 รอบ — blind เลือกแขน B ทั้งคู่ · canary §ponytail 15/15</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>แก้ข้อความ «จัดกลุ่มโน้ต» ให้ตรงความจริงก่อนขอคำสั่งพี่เจ</li>
        <li>A/B งานอ่าน/สรุป: agy vs subagent DSH</li>
        <li>ต่อช่อง canary ที่ยังไม่ต่อสาย (4 ข้อ)</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>อนุมัติลบโปรแกรม opencode (ค้างจากรายงาน 14 ต.ค. 69)</li>
        <li>.gdoc 3 ไฟล์ลบไม่ได้ — เป็น stub ของ DriveFS (สำรองไม่ได้)</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-011">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-011">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-011"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-011"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-011</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc006" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-006 · Meawbin Strategy 2026</div>
      <h2 class="wm-title">เรียนเทรด Meawbin <span class="wm-sub">เรียน 51/55 บท · พาเที่ยวเป็นเพื่อนร่วมเรียน</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag info wm-status">🔵 กำลังเรียน</span>
      <div class="wm-progress" title="เรียนจบ 51 จาก 55 บท"><span class="wm-bar" style="--p:93%"></span><b>93%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    ถอดบทเรียนจากวิดีโอคอร์สให้ครบ 55 บท — ต่อคลิป: <strong>ถอดเสียง → อ่านภาพ/สไลด์ → สรุป → บันทึก notes/</strong> แล้วกลั่นเป็นสมองกลั่น 2 ชั้น (KNOWLEDGE + TRADING_RULES)
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>ตั้งระบบ + คลิป 1-4</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">1</span>สมองกลั่น 2 ชั้น: KNOWLEDGE master + TRADING_RULES<em>22 ส.ค. 69 v0.2</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">2</span>Framework Meawbin + Basic #1 Rollover</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">3</span>Day 01-04 Grid Trading Mindset ครบ 2 Part</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">4</span>Day 01-05 Q and A</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>Day 02-03 (คลิป 5-12)</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">5</span>Day 02-01 Dynamic Grid Technical and Asset</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">6</span>Day 02-02 TP Zone Merge Split and CF<em>เสียงรกมาก</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">7</span>Day 02-03 DCA and Snow Ball 2 Part</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">8</span>Day 02-04 Q and A 2 Part</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">9</span>Day 03-01 WorkShop Grid S50</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">10</span>Day 03-02 WorkShop Grid USD, TDEX, BTC</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">11</span>Day 03-03 WorkShop Grid Forex</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">12</span>Day 03-04 WorkShop การบ้าน</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>Day 03-05 ถึง 05-01 (คลิป 13-20)</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">13</span>Day 03-05 Q and A<em>Grid = ตัวคำนวณ · FIFO ไม่มีผล</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">14</span>Day 03-06 Work Flow Grid<em>workflow 3 ขั้น + Wheel 7 วัน</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">15</span>Day 04-01 Forex คืออะไร</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">16</span>Day 04-02 ความสามารถในการรับรู้กำไร</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">17</span>Day 04-03 Grid หลุดโซน ทำยังไง<em>DCA เติมเงิน 3 ทาง</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">18</span>Day 04-04 Multi Asset Grid<em>แยกพอร์ต A/B/C + Cash Flow กลาง</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">19</span>Day 04-05 Q and A</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">20</span>Day 05-01 Basic #2<em>เปลี่ยนหมวกเป็น Trader ขั้นต้น</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">4</span>Day 05-02 ขึ้นไป + ตัวหารจริง</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">21</span>Day 05-02 Adaptive Grid<em>Grid ที่ไม่มีโซน · No SL</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">22</span>Day 05-03 Alpha Port</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">23</span>Day 05-04 VIX Index Trade</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">24</span>Day 05-05 Q and A<em>คู่มือตัดสินใจ 19 คำถาม</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">25</span>Day 06-01 Cash and Carry</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">26</span>Day 06-02 Calendar Spread Arbitrage</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">27</span>Day 07-01 Relative Spread Arbitrage (OIL)</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-doing"><span class="wm-n">28</span>คลิป 28-56 ทยอยทำวันละ 1-2 คลิป<em>ถัดไปบท 52 EP04</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">29</span>ยืนยันตัวหารจริง = 55 บท<em>มติพี่เจ 27 ก.ย. 69 · ปิด 6 ต.ค. 69</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">30</span>สรุปตัวหารคลิป = 55 (ทะเบียน D)<em>ปิด 5 ต.ค. 69 · เนื้อหายังเหลือ 4 บท</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>เรียนจบ 51/55 บท (93%) — จบ 4 บทติด 10 ต.ค. 69</li>
        <li>จบบท 47 Special 03 + 48-51 (SP04 · EP01-EP03)</li>
        <li>การ์ดจบบท + ยอดเครดิตยิง Discord ครบทุกบท</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>บทถัดไป: EP04 ทบทวน Work Shop Grid Forex (บท 52)</li>
        <li>ตรวจ §6.4 ของโน้ตบท 48-51 แยก</li>
        <li>หลังเรียนครบ 55 บท: ต้องตอบคำถามค้าง ≥35 ข้อ</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>รอพี่เจสั่ง /เรียนต่อ — ตัวรันหยุดตามคำสั่ง /พอ</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-006">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-006">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-006"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-006"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-006</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc012" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-012 · Owner Mail + งานอัตโนมัติในเครื่อง</div>
      <h2 class="wm-title">เมลพี่เจ + งานอัตโนมัติในเครื่อง <span class="wm-sub">Journal · สำรอง Vault · Discord</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag warn wm-status">🟡 รอคำสั่ง/สิทธิ์พี่เจ</span>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    รวมงานระบบในเครื่องกับระบบเมลพี่เจ (owner mail · Journal · สำรอง Vault · health check · Discord log) ให้<strong>เดินจริงและพิสูจน์ได้จาก log/ไฟล์จริง</strong>
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>ระบบเมลพี่เจ (Owner Mail)</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>owner_mail_loop.py (เฟส 1 สแกนอย่างเดียว) + task ทุก 30 นาที<em>task รันจริง LastTaskResult=0</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>งานอัตโนมัติในเครื่อง (Journal / Vault)</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">②</span>journal_mail.py + task Journal 2 ตัว</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-wait"><span class="wm-n">③</span>vault_backup.py<em>ใช้ Startup vbs แทน · task จริงรอ admin</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">④</span>vault_git_snapshot.py</div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>Discord 2 ทาง + โหมด B ตอบเอง จำบริบทได้ (3-4 ต.ค. 69)</li>
        <li>Gemini Billing รันจริง LastTaskResult=0 (13 ต.ค. 69)</li>
        <li>ด่านแบต + task DriveFS ชี้ wrapper เลือกเวอร์ชันเอง (13 ต.ค. 69)</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>งานที่พาเที่ยวเดินเองได้ตอนนี้ = 0 — ที่เหลือรอพี่เจ 5 เรื่อง (ดูช่อง «รอพี่เจ»)</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>รันเชลล์แบบ admin 1 ครั้ง — เพิ่ม trigger At log on ให้ VaultBackup</li>
        <li>GCP: grant serviceUsageViewer + re-auth token ชั้น repair</li>
        <li>เปิด Balance alert ในหน้าเว็บ DeepSeek</li>
        <li>เมลค้าง 2 เรื่อง (ราคาต่อคน/ลีดไทม์ · ขอสิทธิ์โฟลเดอร์ Drive) + Discord ช่องเดียวเป็นจุดเสี่ยงพัง</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-012">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-012">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-012"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-012"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-012</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc015" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-015 · MT5 Trading</div>
      <h2 class="wm-title">เทรด MT5 + ระบบกติกา <span class="wm-sub">กติกาที่ทดสอบกับข้อมูลจริง</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag warn wm-status">🟡 รอพี่เจเคาะกติกา</span>
      <div class="wm-progress" title="ขั้นตอนใน §4 ทำแล้ว 9 จาก 13"><span class="wm-bar" style="--p:69%"></span><b>69%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    ต่อยอดคอร์สเทรดของพี่เจเป็น <strong>กติกาที่ทดสอบกับข้อมูลจริง</strong> บน MT5 — EA ใช้คำนวณ/ออกแบบโซนเท่านั้น ไม่รันเทรดจริง
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>สำรวจเครื่อง + โบรกแรก</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>สำรวจ MT5 ในเครื่อง — 5 โบรก<em>เลือกโบรกหลักได้แล้ว 1 ตัว</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">②</span>คุยโบรกแรกครบ (บัญชี / โซน / magic)</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>ตรวจข้อมูลจริงจากเทอร์มินัล</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">③</span>ตรวจอินดิเคเตอร์จริง<em>CDC/MACD/RSI 55/43 · buf6</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">④</span>ตรวจความลึกข้อมูลย้อนหลัง<em>WTI M30 99,234 แท่ง</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>ศึกษา + Backtest 4 ระดับ</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">⑤</span>Signal study สี × MACD × RSI<em>~30,000 แท่ง</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑥</span>Rule backtest เข้า + เทียบวิธีออก 6 แบบ</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑦</span>Zone backtest 6 vs 12 เดือน<em>6 เดือนชนะ</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑧</span>แยกตามสภาวะตลาด (ADX/DI)<em>ADX&gt;25 และ −DI&gt;+DI = ห้าม short</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑨</span>เทียบกติกาจบไม้ + แยกน้ำมัน/ทอง<em>L3: BE 1.5 ATR · ล็อก 1.0 ที่ 2.5</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">4</span>กติกาสุดท้าย + เทรดจริง + โบรกที่เหลือ</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑩</span>กติกา "ศิลปะ" ให้ชัด<em>เมื่อไรไม่เข้า / เมื่อไรขยับโซน</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑪</span>เทรดจริง lot เล็ก + เก็บสถิติเทียบ backtest</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑫</span>คุยโบรกที่เหลือ 4</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-wait"><span class="wm-n">⑬</span>ย้าย RULES_DRAFT → rules mt5-trading.md<em>พี่เจสั่ง "คุยกันให้จบก่อน"</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>สำรวจ 5 โบรก + ยืนยันโบรกหลักตัวเดียว</li>
        <li>Backtest 4 ระดับเสร็จ · เลือก L3 + rezone 6 เดือน</li>
        <li>ดัมป์ค่าจริงด้วย PaTeawAll.mq5 (27 ก.ย. 69)</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>ตัดสินกติกา "ศิลปะ" (เมื่อไรไม่เข้า/ขยับโซน)</li>
        <li>เริ่มเทรดจริง lot เล็ก แล้วเทียบสถิติกับ backtest</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>ตั้งเกณฑ์ป้องกันความเสี่ยงในจอ (SL) หรือใช้เส้นตาย D1 แทน — ก่อนเริ่มเทรดจริง</li>
        <li>เลือกโบรกถัดไป (เหลืออีก 4 ราย)</li>
        <li>ขอคำยืนยันที่มา RSI 55/43 — ไม่บล็อกงาน</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-015">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-015">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-015"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-015"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-015</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc016" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-016 · 運賃の入力</div>
      <h2 class="wm-title">กรอกราคาค่าโดยสารลงระบบจอง 千栄交通 <span class="wm-sub">ทำจริงแล้ว 8 便 · ตรวจรับผ่านทุกตัว</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag good wm-status">🟢 รอต้นสังกัดส่งกระดาษ</span>
      <div class="wm-progress" title="ขั้นตอนใน §4 ทำแล้ว 6 จาก 7"><span class="wm-bar" style="--p:86%"></span><b>86%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    กรอกราคาค่าโดยสาร/ตั้งวันเดินรถ/手仕舞い ลงระบบจองออนไลน์ 千栄交通 ให้ <strong>ทำเองได้ครบขั้นตอน</strong> ตามที่พี่เจสอนทีละขั้น (เริ่ม 11 ต.ค. 69)
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>เรียนขั้นตอน + สรุปเป็นกติกา</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>เรียนขั้นตอนจากพี่เจทีละขั้น<em>301 親 → 301 子 → 302 親 → 302 子</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">②</span>สรุปเป็น rules + Skill<em>แยกตาม 便 · rules unbin.md</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>กรอกจริง 8 便 (เดือน 2026年12月)</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">③</span>351 · 352 · 451 · 452</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">④</span>แก้ส่วนเพิ่มค่าโดยสาร + แก้แถวของ 352 + ตัดวัน 12/18 ออกจาก 452</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑤</span>601便 都内→京都・大阪<em>ตัวแม่ + ตัวลูก บันทึกครบ</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑥</span>602便 大阪・京都→都内<em>ตัวแม่ + ตัวลูก บันทึกครบ</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>รอบถัดไป</div>
    <div class="wm-steps">
      <div class="wm-step is-wait"><span class="wm-n">⑦</span>งาน 便 อื่น/เดือนอื่น — รอต้นสังกัดส่งกระดาษ<em>พร้อมทำทันทีเมื่อได้ไฟล์</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>กรอกครบ 8 便 เดือน 2026年12月 · ตรวจ persistence ผ่านทุกตัว</li>
        <li>601/602 บันทึกครบ + 時間更新 (12 ต.ค. 69)</li>
        <li>สรุป rules + Skill แยกตาม 便 ใช้ซ้ำได้</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>เมื่อได้ไฟล์: เสนอชื่อไฟล์ + รอพี่เจเคาะก่อนอ่าน/กรอก</li>
        <li>ทำทีละ 1 便 แล้วแจ้งพี่เจตรวจ — ห้ามล้ำไป 便 ถัดไป</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอต้นสังกัด / รอสอน</h4>
      <ul>
        <li>รอต้นสังกัดส่งกระดาษ 便/เดือนถัดไป — ไม่มีกำหนดแน่นอน</li>
        <li>ยังไม่รู้ขั้นตอนยกเลิก/ลบวันเดินรถ — ห้ามกดจนพี่เจสอน</li>
        <li>ส่วนเพิ่มค่าโดยสารของวัน 金/土/日 + ช่วงปลายเดือน อาจไม่เหมือนรอบก่อน — อ่านหมายเหตุของไฟล์รอบนั้นทุกครั้ง</li>
        <li>ยังไม่ยืนยันว่า 便 เลขชุดใหม่ที่พี่เจให้จะทำเมื่อไร</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-016">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-016">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-016"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-016"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-016</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc003" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-003 · B2B / Smile Travel</div>
      <h2 class="wm-title">B2B Smile Travel + หาลูกค้าใหม่ <span class="wm-sub">ยิง outreach จริง 6 เจ้า</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag warn wm-status">🟡 รอพี่เจอนุมัติส่งซ้ำ</span>
      <div class="wm-progress" title="ขั้นตอนใน §4 ทำแล้ว 3 จาก 4"><span class="wm-bar" style="--p:75%"></span><b>75%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    เปิดช่องทาง B2B ใหม่ต่อจาก B2B Shortlist v1.0 — ส่งข้อความ outreach จริง แล้ว<strong>บันทึกผลไว้ใช้ต่อ</strong>
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>เตรียมช่องทาง + ยิงข้อความ</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>หาช่องทางติดต่อ (เมล/LINE/ฟอร์ม)<em>เคาะช่องทาง = เมล (25 ก.ย. 69)</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">②</span>ส่ง intro + profile kit<em>ยิงจริง 5 ต.ค. 69 · 5/6 ฉบับสำเร็จ</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>นัดคุย + บันทึกผล</div>
    <div class="wm-steps">
      <div class="wm-step is-wait"><span class="wm-n">③</span>ติดตาม/นัดคุย<em>รอเจ้าตอบกลับ</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">④</span>บันทึกผลลง Sales_Marketing<em>tracker 6 แถว + หลักฐาน DSN</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>ยิงเมล B2B จริง 6 เจ้า — 5 ถึงมือ · 1 ตีกลับ (5 ต.ค. 69)</li>
        <li>ปิดงานหาช่องทาง/ส่ง/บันทึกผล ด้วยหลักฐานครบชุด</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>ส่งซ้ำ Next Trip ไปอีเมลใหม่</li>
        <li>กดส่งฉบับติดตาม 10 ฉบับ</li>
        <li>ติดตามผู้รับที่ยังไม่ตอบกลับ (ยิงไป 5 ต.ค. 69)</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>อนุมัติ 1 คลิก — ส่งซ้ำ Next Trip Holiday</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-003">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-003">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-003"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-003"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-003</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc001" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-001 · Master Data</div>
      <h2 class="wm-title">Master Data (โรงแรม / ร้านอาหาร / รถ) <span class="wm-sub">ฐานราคากลางสำหรับใบเสนอราคา</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag warn wm-status">🟡 ใช้จริงแล้ว · เหลือ verify RAW</span>
      <div class="wm-progress" title="§4 ทำแล้ว 5/6 · งานจริง (VERIFY) 855 จาก 1,323 = 65%"><span class="wm-bar" style="--p:83%"></span><b>83%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    สร้างฐานข้อมูลต้นทุน/ราคากลาง 3 กลุ่ม (HOTEL / RESTAURANT / BUS) ให้ใบเสนอราคาและโปรแกรมทัวร์ใช้ได้ — <strong>ห้ามใช้ข้อมูลดิบคำนวณตรง</strong> ต้องผ่าน pipeline RAW → VERIFY → MASTER
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>วางโครงสร้าง + pipeline</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>ตั้งโครงสร้าง 18 tabs + rate 13<em>pipeline RAW→STAGING→VERIFY→MASTER→OUTPUT</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>VERIFY → MASTER</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">②</span>VERIFY 855 รายการ (Hotel/Restaurant)<em>เป้ารวม 1,323 รายการ</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">③</span>เติม supplier บัส — BUS 12 ใน Firestore<em>27 ส.ค. 69</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">④</span>ขึ้น MASTER 3 กลุ่ม → Firestore = 855<em>HOT178 + RES495 + ATTR170 + BUS12</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>ใช้จริง + งานที่เหลือ</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">⑤</span>ใช้คำนวณราคา / ออกใบเสนอราคา<em>builder prod ใช้ Firestore (audit 7 ก.ย. 69)</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-wait"><span class="wm-n">⑥</span>verify RAW 1,323 รายการ<em>รออีเมล supplier / ชื่อ List จากพี่เจ</em></div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>Firestore master_data = 855 VERIFIED</li>
        <li>BUS 12 เติมใน Firestore แล้ว (27 ส.ค. 69)</li>
        <li>builder prod ใช้ Firestore คำนวณราคา/ใบเสนอราคา</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป</h4>
      <ul>
        <li>เมื่อได้ไฟล์ Takeout ชุดใหม่: เทียบชุดเดิม 334 รายการ หา List name ใหม่</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>รอไฟล์ Google Takeout ใหม่จากพี่เจ</li>
        <li>verify RAW 1,323 — รออีเมล supplier / ชื่อ List เดิม</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-001">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-001">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-001"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-001"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-001</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
</article>

<article class="wm wm-detail" id="pc008" hidden>
  <span class="wm-glow" aria-hidden="true"></span>
  <header class="wm-head">
    <div class="wm-headtext">
      <div class="wm-code">PC-008 · Google Account Migration</div>
      <h2 class="wm-title">ย้ายบัญชี Google → chettana33 <span class="wm-sub">แผน 8 ระยะ · ยังไม่ลงมือ</span></h2>
    </div>
    <div class="wm-right">
      <span class="tag warn wm-status">⏳ รอพี่เจสั่ง "เริ่มย้าย"</span>
      <div class="wm-progress" title="ขั้นตอนใน §4 ทำแล้ว 2 จาก 31"><span class="wm-bar" style="--p:6%"></span><b>6%</b></div>
    </div>
  </header>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    ย้ายระบบทั้งหมดจากบัญชีเดิม ไปบัญชีใหม่ <strong>chettana33</strong> อย่างเป็นขั้นตอน — ตอนนี้เป็น "แผนพร้อมรัน" ตามที่พี่เจสั่งให้ทำแผนไว้ก่อน ยังไม่ลงมือ
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">1</span>ระยะ 0-1 · Inventory + GitHub</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">①</span>ระยะ 0 — Inventory: กวาด ref ทั้ง Vault + repo</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">②</span>ยืนยัน gh auth = chettana33<em>ยืนยัน 5 ต.ค. 69</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">③</span>ตรวจ repo ผูก webhook/action กับบัญชี Google<em>ichinotour-ai-studio-app → Firebase/Vercel</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">2</span>ระยะ 2-3 · Vault + Drive/Sheets</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">④</span>ย้าย Vault ไปบัญชีใหม่</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑤</span>bulk replace refs ทุกจุด + serena config + MCP</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑥</span>login chettana33 ใน Drive for Desktop<em>ต้องใช้ drive letter ใหม่</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑦</span>ขอ OAuth token ใหม่ทุก scope<em>credential เดิมหาย</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-done"><span class="wm-n">⑧</span>Google Doc sync<em>ยุบทั้งระบบ 6 ก.ย. 69</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">3</span>ระยะ 4-6 · Gmail / Calendar / Gemini</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑨</span>ตั้ง forward เมล monitor หรือแก้สคริปต์<em>ทดสอบรับเมล์จริง 1-2 วัน</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑩</span>export/import ปฏิทินทัวร์-งาน</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑪</span>login Gemini Browser ด้วยบัญชีใหม่</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title"><span class="wm-pnum">4</span>ระยะ 7 · Cutover</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑫</span>รัน 2 บัญชีคู่กันจนมั่นใจ</div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑬</span>ถอนบัญชีเดิมออกจาก DriveFS<em>เก็บ archive/backup ก่อนลบ</em></div>
      <span class="wm-flow" aria-hidden="true"></span>
      <div class="wm-step is-todo"><span class="wm-n">⑭</span>อัปเดต AGENTS.md §9 + lessons-learned</div>
    </div>
  </div>

  <div class="wm-now-title">ตอนนี้อยู่ตรงไหน</div>
  <div class="wm-now">
    <div class="wm-card is-done">
      <h4>✅ ทำเสร็จแล้ว</h4>
      <ul>
        <li>นับ ref จริง: Vault 100 บรรทัด/38 ไฟล์ · repo 145/45</li>
        <li>gh auth status = chettana33 ✓ (5 ต.ค. 69)</li>
        <li>แผนย้าย 8 ระยะ เขียนครบ</li>
      </ul>
    </div>
    <div class="wm-card is-doing">
      <h4>👉 ก้าวต่อไป (เมื่อพี่เจสั่ง)</h4>
      <ul>
        <li>เริ่มระยะ 0 — กวาด ref ทั้ง Vault + repo ก่อนย้าย</li>
        <li>login chettana33 ใน Drive for Desktop → drive letter ใหม่</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>สั่ง "เริ่มย้าย" — 29 ขั้นที่เปิดอยู่ยังไม่เริ่ม</li>
        <li>ยังไม่แตะโฟลเดอร์ credential/token จนกว่าพี่เจสั่ง</li>
        <li>หมายเหตุตัวเลข: การ์ดเรียกว่า "36 ขั้น" = §4 เปิดค้าง 29 + เกณฑ์ §7 อีก 7 (แถบ % ด้านบนนับเฉพาะ §4)</li>
      </ul>
    </div>
  </div>

  <div class="wm-notes" data-card="PC-008">
    <div class="wm-notes-head">📝 โน้ตของพี่เจ — ฝากถึงพาเที่ยวได้</div>
    <div class="wm-notes-input">
      <textarea class="wm-note-text" rows="2" maxlength="2000" placeholder="พิมพ์โน้ต/สิ่งที่อยากให้ทำกับงานนี้…"></textarea>
      <div class="wm-notes-actions">
        <button class="wm-note-save" data-card="PC-008">บันทึก</button>
        <span class="wm-note-msg" data-card="PC-008"></span>
      </div>
    </div>
    <div class="wm-notes-list" data-card="PC-008"><span class="muted">กำลังโหลดโน้ต…</span></div>
  </div>

  <div class="wm-foot"><span>ที่มา: การ์ด PC-008</span><span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span></div>
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
    if (id) { whenDb(function () { loadCardNotes(id.replace('pc', 'PC-')); }); }
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
    if (cid) { whenDb(function () { loadCardNotes(cid.replace('pc', 'PC-')); }); }
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

  /* รอให้สคริปต์หลัก (ที่ init Firebase) ประกาศว่าพร้อมก่อน — กัน ReferenceError ตอนสคริปต์ในเนื้อหารันก่อน */
  function whenDb(fn) {
    if (window.__pdReady && typeof db !== 'undefined') { fn(); return; }
    window.addEventListener('pd:ready', function () { fn(); }, { once: true });
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
      if (!window.__pdReady) { if (msg) msg.textContent = 'ระบบยังโหลดไม่เสร็จ ลองอีกครั้ง'; return; }
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
  whenDb(loadLive);
})();
</script>
```
