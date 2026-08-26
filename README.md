# 🗺️ พาเที่ยว Dashboard

กระดานภาพรวมธุรกิจ Ichino Tour — พี่เจ & พาเที่ยว เห็นภาพเดียวกัน

**URL:** https://chettana33.github.io/phathiao-dashboard/

## หน้าต่างๆ

- **ภาพรวม** — โครงสร้าง 4 ชั้น + พันธมิตร + ซัพพลาย (ไฟล์ `content/overview.md`)
- **สถานะงาน** — สถานะเครื่องมือ + Master Data (ไฟล์ `content/status.md`)
- **Checkpoint** — ดึง `CHECKPOINT_LATEST.md` จาก knowledge-brain อัตโนมัติตอน build (ทุก push + ทุกวัน 00:00 UTC)
- **MEMORY** — ดึง `พี่เจ_MEMORY.md` จาก knowledge-brain อัตโนมัติตอน build (ทุก push + ทุกชั่วโมง) — ห้ามแก้เอง
- **ลำดับถัดไป** — roadmap (ไฟล์ `content/roadmap.md`)
- **กระดานไอเดีย** — ช่องพิมพ์ในเว็บ → เก็บ Firestore (`phathiao-dashboard` project) — เห็นร่วมกันทุกเครื่อง

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
