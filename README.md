# 🗺️ พาเที่ยว Dashboard

กระดานภาพรวมธุรกิจ Ichino Tour — พี่เจ & พาเที่ยว เห็นภาพเดียวกัน

**URL:** https://chettana33.github.io/phathiao-dashboard/

## วิธีอัปเดต

1. แก้ไฟล์ใน `content/` (`overview.md` · `status.md` · `roadmap.md` · `ideas.md`)
2. commit + push ไป `main` — GitHub Actions build + deploy อัตโนมัติ
3. เปิด URL อีกครั้ง (หรือ refresh) ดูผล

หรือรัน build ในเครื่องก่อน push:

```bash
python build.py
# สร้าง docs/index.html — ตรวจได้ก่อน push
```

## โครงสร้าง

```text
content/*.md   <- ต้นทาง (แก้ตรงนี้)
build.py       <- แปลง .md -> HTML (ไม่ใช้ lib ภายนอก)
docs/          <- ผล build (deploy ขึ้น Pages)
.github/workflows/deploy.yml <- build + deploy อัตโนมัติ
```

## กฎ

- repo สาธารณะ — **ห้าม** password/token/ราคา margin ภายใน/ข้อมูลลับ
- ทุกไฟล์ใน content ใช้ภาษาไทย, ตาราง + bullet ตาม format กลาง
