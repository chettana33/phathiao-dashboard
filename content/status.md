---
title: "สถานะงาน"
type: "dashboard"
last_updated: 2026-08-29T21:45:00+07:00
---

# 📊 สถานะงาน

> อัปเดตอัตโนมัติโดยพาเที่ยวทุกปิดงาน (จาก checkpoint) — timestamp ด้านบน

## การ์ดงาน (Project Cards — PC_INDEX 7 ก.ย. 69)

| การ์ด | งาน | สถานะ |
|---|---|---|
| PC-001 | Master Data (Hotel/Restaurant/Bus) | In Progress — master 855 ใช้จริง เหลือ verify RAW 1,323 |
| PC-002 | Format Migration .md | Done |
| PC-003 | B2B Smile Travel (ติดต่อ) | Pending |
| PC-004 | ทดลอง serena-slim | Done |
| PC-005 | ขยาย Thin MCP 14 repo | Done |
| PC-006 | Meawbin Strategy 2026 (เรียนเทรด 56 คลิป) | In Progress — notes 13/56 |
| PC-007 | Quotation Builder v6 | In Progress — rate UNVERIFIED รอพี่เจ |
| PC-008 | ย้ายบัญชี Google | Pending (รอสั่งเริ่ม) |
| PC-009 | Gochisou TikTok Launch | In Progress — pilot v3 reject รอคลิปใหม่ |
| PC-010 | TikTok Liked Classify 2023-2025 (2,719) | Blocked (รอ data JSON) |
| PC-011 | DSH Tooling & Knowledge Ops (B20/B21/corpus/cloud scheduler) | In Progress — ใหม่ 7 ก.ย. |

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

## งานค้างเรียงตามลำดับ (7 ก.ย. 2569 — รายการเต็มดู section Checkpoint อัตโนมัติ)

1. **A1 Gochisou decision pack** — รอพี่เจ้าสั่ง (PC-009)
2. **Meawbin คลิป 14 Day 03-06** — 13/56 (PC-006)
3. **PC-007 rate UNVERIFIED** — พี่เจตรวจ (Master Data ต่อยอด)
4. **PC-008 ย้ายบัญชี Google** — แผนพร้อม รอสั่งเริ่ม
5. B22 voice-input รอพี่เจสั่ง (PC-011) · คลิปชาบูไอเดีย 3 + Flow Playbook · PC-003 B2B ทักหา
