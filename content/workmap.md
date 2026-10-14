---
title: "แผนที่งาน — ดูแล้วรู้ทันทีว่าทำอะไรอยู่ และทำยังไง"
type: "dashboard"
---

# 🧭 แผนที่งาน (Work Map)

> หน้านี้ทำไว้ให้พี่เจ **เปิดดูเมื่อไหร่ก็รู้ทันที** ว่างานนั้นทำอะไรอยู่ ถึงขั้นไหน และก้าวต่อไปคืออะไร
> อัปเดตโดยพาเที่ยวทุกครั้งที่ปิดงานรอบ · แก้ที่ `content/workmap.md` แล้ว build ใหม่

```html
<div class="wm">

  <div class="wm-head">
    <div>
      <div class="wm-code">PC-017</div>
      <h2 class="wm-title">Affiliate Marketing <span class="wm-sub">การตลาดแบบพันธมิตร — เราทำ affiliate เอง (รับค่าคอมจากแบรนด์)</span></h2>
    </div>
    <span class="tag info wm-status">🔵 กำลังทำ · ช่วงศึกษา</span>
  </div>

  <div class="wm-goal">
    <span class="wm-goal-label">🎯 เป้าหมาย</span>
    หา <strong>สินค้าที่มีเทรนด์/ขายดี</strong> → ทำ <strong>คลิป</strong> → โพสต์ผ่านช่องทางของเรา → รับ <strong>ค่าคอมมิชชัน</strong>
  </div>

  <div class="wm-legend">
    <span><i class="wm-dot d-done"></i>เสร็จแล้ว</span>
    <span><i class="wm-dot d-doing"></i>กำลังทำ / ทำต่อ</span>
    <span><i class="wm-dot d-wait"></i>รอพี่เจ</span>
    <span><i class="wm-dot d-todo"></i>ยังไม่เริ่ม</span>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title">ระยะ 1 · หาคำตอบให้ครบก่อนลงมือ</div>
    <div class="wm-steps">
      <div class="wm-step is-done"><span class="wm-n">①</span>ล็อกโจทย์: เราทำ affiliate เอง</div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-doing"><span class="wm-n">②</span>แผนที่โปรแกรม affiliate (ญี่ปุ่น + ไทย)<em>ชื่อโปรแกรม · เกณฑ์สมัคร · ค่าคอม</em></div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-todo"><span class="wm-n">③</span>เลือกสายสินค้าที่เข้ากับเรา 3 อันดับ</div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-todo"><span class="wm-n">④</span>โมเดลรายได้ + เงื่อนไขจ่ายจริง</div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-todo"><span class="wm-n">⑤</span>ด่านกฎหมาย/ภาษี + เปิดเผยว่าเป็นลิงก์โฆษณา</div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-todo"><span class="wm-n">⑥</span>ประเมินความเสี่ยง (บัญชีถูกระงับ · เงินค้าง)</div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-todo"><span class="wm-n">⑧</span>ใบตัดสิน: ทำ/ไม่ทำ + เริ่มที่ไหน</div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title">ระยะ 2 · หาสินค้า (งานของพาเที่ยว)</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑨</span>หาสินค้าที่มีเทรนด์/ขายดี<em>ส่งลิสต์สั้น 3–5 ชิ้น</em></div>
      <span class="wm-arrow">➜</span>
      <div class="wm-step is-wait"><span class="wm-n">⑩</span>พี่เจเลือกสินค้า<em>ด่านก่อนผลิตทุกครั้ง</em></div>
    </div>
  </div>

  <div class="wm-phase">
    <div class="wm-phase-title">ระยะ 3 · ทำคลิปและวัดผล</div>
    <div class="wm-steps">
      <div class="wm-step is-todo"><span class="wm-n">⑦</span>ทดลองเล็ก 1 ช่องทาง<em>1 สินค้า × 1 คลิป × 2–4 สัปดาห์</em></div>
      <span class="wm-arrow">➜</span>
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
    <span>ที่มา: การ์ด PC-017 · อัปเดต 14 ต.ค. 69</span>
    <span>งานค้างทั้งหมดอยู่ใน «งานค้าง» ของการ์ด · หน้านี้อัปเดตทุกครั้งที่ปิดงานรอบ</span>
  </div>

</div>
```
