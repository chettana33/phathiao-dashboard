---
title: "แผนที่งาน — ดูแล้วรู้ทันทีว่าทำอะไรอยู่ และทำยังไง"
type: "dashboard"
---

# 🧭 แผนที่งาน (Work Map)

> เปิดดูเมื่อไหร่ก็รู้ทันที: งานนี้ทำอะไรอยู่ · ถึงขั้นไหน · ก้าวต่อไปคืออะไร · อะไรต้องรอพี่เจ
> อัปเดตโดยพาเที่ยวทุกครั้งที่ปิดงานรอบ · แก้ที่ `content/workmap.md` แล้ว build ใหม่

```html
<article class="wm">
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

  <div class="wm-foot">
    <span>ที่มา: การ์ด PC-017</span>
    <span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span>
  </div>
</article>

<article class="wm">
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
      <div class="wm-step is-doing"><span class="wm-n">50%</span>ปลายทาง «กดต่อ» (ลิงก์ไบโอ + GA4)<em>รอ Measurement ID จากพี่เจ (ยังว่าง = ยังไม่เก็บข้อมูล)</em></div>
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
        <li>ปักหมุดคอมเมนต์ CTA บน IG ใบ 2/3 (หลังโพสต์ 15–16 ต.ค. 18:00) — ทำได้ในแอปมือถือเท่านั้น</li>
        <li>เตรียมคลิปถัดไปตามแผน 3 เดือน (รอเครดิตเจน)</li>
      </ul>
    </div>
    <div class="wm-card is-wait">
      <h4>🙋 รอพี่เจ</h4>
      <ul>
        <li>ชื่อโปรไฟล์ IG (@gochisou_booking) — ยังว่าง</li>
        <li>GA4 Measurement ID (ส่งมาแล้วโค้ดเริ่มเก็บข้อมูลทันที)</li>
        <li>งบเครดิตสำหรับคลิปว้าว 3 แนว</li>
      </ul>
    </div>
  </div>

  <div class="wm-foot">
    <span>ที่มา: การ์ด PC-009</span>
    <span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด</span>
  </div>
</article>
```
