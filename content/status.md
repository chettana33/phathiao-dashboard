---
title: "สถานะงาน"
type: "dashboard"
last_updated: 2026-08-29T21:45:00+07:00
---

# 📊 สถานะงาน

> อัปเดตอัตโนมัติโดยพาเที่ยวทุกปิดงาน (จาก checkpoint) — timestamp ด้านบน

## เครื่องมือ

| เครื่องมือ | สถานะ | หมายเหตุ |
|---|---|---|
| เว็บ ichinotour-thailand.com | <span class="tag good">LIVE</span> | Firestore rules แก้แล้ว (quotations create ผ่าน) — เนื้อหาตรวจกับพี่เจ |
| quotation v6 builder | <span class="tag good">ใช้ได้</span> | เรทเยน-บาท **อัตโนมัติจาก gist** (0.2066) — rate UNVERIFIED รอพี่เจตรวจ |
| Gochisou landing (งานนอก) | <span class="tag good">LIVE</span> | Pages — ฟอร์ม→Firestore→LINE ครบวงจร (ทดสอบผ่าน) — รอ domain Vercel |
| 台帳 / King BUS ระบบ | <span class="tag good">อัตโนมัติ</span> | master ถูกไฟล์ + token ใหม่ + PDF→LINE (การบ้าน: PDF สวย + ส่งไฟล์จริง) |
| daily-news LINE/เมล | <span class="tag good">อัตโนมัติ</span> | ย้าย Task Scheduler เครื่อง (07:00) — เช็ครอบแรก 30 ส.ค. |
| Backup Vault | <span class="tag good">อัตโนมัติ</span> | zip→Drive ทุก 18:30 (เก็บ 14) |
| Master Data | <span class="tag bad">ค้าง</span> | verify RAW 1,323 ค้าง — rate รอพี่เจ |

## Master Data (PC-001)

| รายการ | จำนวน | สถานะ |
|---|---|---|
| รวม entity | 2,178 | HOTEL 312 · RESTAURANT 1,247 · ATTRACTION 598 · BUS/PARKING 21 |
| VERIFIED | 855 | master_data ใน Firestore (HOTEL/RES/ATTR/BUS) |
| RAW (ยังไม่ตรวจ) | 1,323 | **ติดหลักฐานนอกเครื่อง** — อีเมล supplier / ชื่อ List เดิม |
| Rate History | เริ่มแล้ว | **UNVERIFIED** รอพี่เจตรวจ |

## ระบบครบวงจร (สายพาน AI ops)

| ระบบ | บทบาท | สถานะ |
|---|---|---|
| DSH (DeepSeek) | execution หลัก — agents, checkpoint, Discord, GitHub | ✅ ใช้งาน |
| ModLens vision | อ่านภาพใน session (Gemini bridge) | ✅ ใช้ได้ (quota ฟื้น) |
| Playwright browser | ควบคุม browser จริง | ✅ |
| MCP client | serena + playwright + vault + (firebase MCP config พร้อม — รอ restart) | ✅ |
| สคริปต์กลาง | checkpoint/commit/push/Discord | ✅ |
| Task Scheduler | daily-news 07:00 · taicho 16:00 · backup 18:30 · yen 08:00 · Gochisou LINE 15 นาที | ✅ 5 งาน |
| Google Workspace MCP | **รอ official** — third-party ไม่ใช้ (supply chain) | ⏳ |

> รายละเอียด: `00_SOP_Master/01_AI_Protocols/` ใน Vault

## งานค้างเรียงตามลำดับ (29 ส.ค. 2569)

1. **PC-007 rate UNVERIFIED** — พี่เจตรวจ (Master Data ต่อยอด)
2. **PC-008 ย้ายบัญชี Google** kimonoland→chettana33 — แผนพร้อม รอสั่งเริ่ม
3. **taicho PDF การบ้าน** — PDF สวยเหมือนจริง + ส่งไฟล์ PDF จริงเข้า LINE (หาวิธีฟรี)
4. **PC-003 B2B Smile Travel** (#40) — ทักหา
5. Google Doc sync (client_secret หาย) · PC-001 verify RAW 1,323 · taicho→senei-kotsu-invoice · PC-006 Meawbin · portfolio-analyst · voice-input · Workspace MCP รอ official · Gochisou domain/ภาพ/TikTok
