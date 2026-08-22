# 📊 สถานะงาน

> สถานะอัปเดต: 22 ส.ค. 2569 · แก้ไขตารางนี้เมื่องานเปลี่ยน

## เครื่องมือ

| เครื่องมือ | สถานะ | หมายเหตุ |
|---|---|---|
| เว็บ ichinotour-thailand.com | <span class="tag good">LIVE</span> | v0.1.0 เปิดสาธารณะ — เนื้อหาราคา/เบอร์/LINE ยังต้องตรวจกับเจ้าของ |
| quotation v5.8 (CI) | <span class="tag good">ใช้ได้</span> | Yen→Baht, BUS dropdown 10 แบบ, ลูกค้า B2B, backup ใน browser |
| JLOS Restaurant | <span class="tag good">เสร็จ 100%</span> | TASK-001..012 — เหลือ polish ตามที่พี่เจเลือก |
| JLOS Hotel / Bus / Attraction | <span class="tag warn">ยังไม่เริ่ม</span> | รอ spec + อนุมัติ — หลัง Restaurant polish |
| 台帳 / King BUS ระบบ | <span class="tag good">อัตโนมัติ</span> | monitor_cgman + taicho_auto + taicho_gsheets |
| Master Data | <span class="tag bad">ค้างหนัก</span> | 2,178 entity — VERIFIED แค่ 40 (ดูด้านล่าง) |

## Master Data (PC-001)

| รายการ | จำนวน | สถานะ |
|---|---|---|
| รวม entity | 2,178 | HOTEL 312 · RESTAURANT 1,247 · ATTRACTION 598 · BUS/PARKING 21 |
| VERIFIED | 40 | เฉพาะ HOTEL ชุดแรก |
| RAW (ยังไม่ตรวจ) | 2,138 | **ติดหลักฐานนอกเครื่อง** — ต้องอีเมล supplier / ชื่อ List เดิมจาก Google Takeout |
| Rate History | เริ่มแล้ว | Hotel_Rate_History + Bus_Quote_History — **UNVERIFIED** รอพี่เจตรวจ |

## งานค้างเรียงตามลำดับ

1. **Master Data เสร็จก่อน** (เปิดทางทุกอย่าง) — verify RAW 2,138 + ตรวจ rate + เติม supplier บัส
2. ตรวจเนื้อหาเว็บ (ราคา/เบอร์/LINE) กับพี่เจ
3. Restaurant polish (JLOS) → Hotel → Bus → Attraction
4. B2B outreach — Smile Travel (#40) คิวแรก
