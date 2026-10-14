# 🗺️ พาเที่ยว Dashboard

กระดานภาพรวมธุรกิจ Ichino Tour — พี่เจ & พาเที่ยว เห็นภาพเดียวกัน

**URL:** https://chettana33.github.io/phathiao-dashboard/

## หน้าต่างๆ

- **ภาพรวม** — โครงสร้าง 4 ชั้น + พันธมิตร + ซัพพลาย (ไฟล์ `content/overview.md`)
- **แผนที่งาน (Work Map)** — หน้ารวมงานทุกการ์ด (เรียงงานที่กำลังทำอยู่ก่อน) → กดช่องงานเพื่อดูขั้นตอน/สถานะ/ก้าวต่อไปในหน้าเดียว
  - ตัวเลข "งานค้าง" ต่อการ์ด **ดึงสดจาก Firestore** (`dashboard_state`) — ดันขึ้นอัตโนมัติทุกครั้งที่ปิดงานด้วย `push_dashboard_state.py` (ขั้น `0h/4` ของ `checkpoint_workflow.py`)
  - มีช่องค้นหา · ป้าย "ดูล่าสุด" · ลิงก์ตรงต่องาน (`#workmap/pc017`) · ปุ่มย้อนกลับของเบราว์เซอร์ใช้ได้
  - **โน้ตต่อการ์ด** — พิมพ์ฝากถึงพาเที่ยวได้ เก็บที่ `card_notes` (อ่าน/เพิ่มได้ · แก้/ลบไม่ได้)
- **ส่วนตัว 🔒** — พื้นที่ต้องล็อกอิน (Google) จำกัดเฉพาะบัญชีพี่เจ · โน้ตส่วนตัวเก็บที่ `private_notes` (คนไม่ล็อกอินอ่านไม่ได้ — rules ปฏิเสธ)
- **สถานะงาน** — สถานะเครื่องมือ + Master Data (ไฟล์ `content/status.md`)
- **Checkpoint** — ดึง `CHECKPOINT_LATEST.md` จาก knowledge-brain อัตโนมัติตอน build (ทุก push + ทุกวัน 00:00 UTC)
- **MEMORY** — ดึง `พี่เจ_MEMORY.md` จาก knowledge-brain อัตโนมัติตอน build (ทุก push + ทุกชั่วโมง) — ห้ามแก้เอง
- **ลำดับถัดไป** — roadmap (ไฟล์ `content/roadmap.md`)
- **กระดานไอเดีย** — ช่องพิมพ์ในเว็บ → เก็บ Firestore (`phathiao-dashboard` project) — เห็นร่วมกันทุกเครื่อง

## ฟีเจอร์ของหน้าเว็บ (เฟส 1-2 · 14 ต.ค. 69)

- **ลื่นไหล**: นำทางด้วย URL (`#งาน`) · เปลี่ยนหน้าแบบมี transition · ปุ่มขึ้นบนสุด · ค้นหา
- **อ่านสบาย**: สลับโหมดสว่าง/มืด + ปรับขนาดตัวอักษร (จำค่าไว้ในเครื่อง)
- **ติดตั้งเป็นแอปได้ (PWA)**: `manifest.webmanifest` + `sw.js` + ไอคอน — เปิดเต็มจอ ใช้ตอนเน็ตหลุดได้
  - service worker เสิร์ฟหน้าเว็บแบบ **network-first** (กันหน้าเก่าค้างหลัง deploy) · ไฟล์นิ่ง (รูป/ไอคอน) cache-first
- **สถานะสด**: อ่านตัวเลขจาก Firestore ไม่ต้องรอ build รายชั่วโมง


## โน้ตจากเว็บ → AI อ่าน

- พี่เจ้าพิมพ์โน้ตในเว็บ → เก็บ Firestore
- **ตอนเริ่มงาน**: AI รัน `python sync_notes.py` ในเครื่อง → ดึงโน้ต → เขียน `content/notes.md` → อ่านได้ (ไม่ต้องรอ schedule)
- `sync_notes.py` อยู่ใน repo — รันเองได้ทุกเมื่อ

## วิธีอัปเดต

1. แก้ไฟล์ใน `content/` → commit + push → GitHub Actions build + deploy อัตโนมัติ
2. หรือรัน `python build.py` ในเครื่อง (สร้าง `docs/index.html` ตรวจก่อน push)
3. โน้ต/ไอเดีย: พิมพ์ในเว็บเลย (ไม่ต้องแก้ไฟล์)

## โครงสร้าง

```text
content/*.md   <- ต้นทาง (แก้ตรงนี้) — checkpoint.md + memory.md ถูก workflow ดึงทับอัตโนมัติ, notes.md ถูก sync_notes.py สร้าง
build.py       <- แปลง .md -> HTML (ไม่ใช้ lib ภายนอก)
sync_notes.py  <- ดึงโน้ตจาก Firestore -> content/notes.md (รันตอนเริ่มงาน)
docs/          <- ผล build (deploy ขึ้น Pages)
firestore.rules + firebase.json <- rules กระดานไอเดีย (deploy: firebase deploy --only firestore:rules)
.github/workflows/deploy.yml <- build + deploy อัตโนมัติ
```

## กฎ

- repo สาธารณะ — **ห้าม** password/token/ราคา margin ภายใน/ข้อมูลลับ
- ทุกไฟล์ใน content ใช้ภาษาไทย, ตาราง + bullet ตาม format กลาง
- `content/checkpoint.md` + `content/memory.md` = ดึงทับอัตโนมัติ — ห้ามแก้เอง (จะโดนทับ)
