---
title: "System Map"
type: "dashboard"
---

# 🗺️ System Map

> อัปเดตล่าสุด **26 ก.ย. 69 (รอบ 45)** — เขียนจาก §9 System Map ของการ์ดจริง 14 ใบ (ครบทุกใบแล้ว)
> สถานะ: done (เขียว) · in_progress (ฟ้า) · blocked (แดง) · pending (เทา)
> กติกา: ตัวเลข/สถานะในหน้านี้ต้องมีที่มาจากการ์ดหรือคำสั่งที่รันได้จริง — ห้ามเขียนงานค้างไว้ที่นี่ (งานค้างอยู่ที่ §10 ของการ์ด)

## ระบบงานทั้งหมด — 14 การ์ด

| การ์ด | ระบบ | %เสร็จ | สถานะ | เจ้าของ | หลักฐานล่าสุด |
|---|---|---|---|---|---|
| PC-001 | Master Data (HOTEL/RESTAURANT/ATTRACTION/BUS) | 93 | in_progress | พาเที่ยว | Firestore `master_data` 855 (`HOT178·RES495·ATTR170·BUS12`) · VERIFY ยัง 855/1,323 |
| PC-002 | Format Migration (กติกา format กลาง) | 100 | done | พาเที่ยว | sync repo `ab468b4` (22 ส.ค. 69) |
| PC-003 | B2B Outreach (Smile Travel / เอเจนซี่) | 67 | in_progress | พี่เจ + พาเที่ยว | แม่แบบเมลฉบับ 1 อนุมัติ 25 ก.ย. 69 · pilot 3 ร้านแรกฟรี |
| PC-004 | Serena Slim (MCP token) | 100 | done | พาเที่ยว | 13 tools ≈ 2,968 tok (ลด ~76.5% จาก serena เต็ม) |
| PC-005 | Thin MCP / ทะเบียน repo | 100 | done | พาเที่ยว | `tools/projects.json` activate 15/15 ผ่าน |
| PC-006 | Meawbin Strategy 2026 | 92 | in_progress | พาเที่ยว | เรียนจบ 27/56 · KNOWLEDGE v2.9 / RULES v2.8 · notes 27 ไฟล์ |
| PC-007 | Quotation Builder v6 | 81 | in_progress | พาเที่ยว + พี่เจ | merge `f7e37fd` (P4 แผนที่/time v1-v9) · print ยังพัก (พี่เจ: "แย่มาก ยิ่งแก้ยิ่งผิด") |
| PC-008 | Google Account Migration | 13 | pending | พี่เจ + พาเที่ยว | แผน 8 ระยะครบ · ยังไม่เริ่มระยะ 0 (inventory) |
| PC-009 | Gochisou TikTok Launch | 75 | in_progress | พาเที่ยว + พี่เจ | 4 คลิปโพสต์ · วิวสะสม 822 · FB 356 · **ทัก LINE 0** · `/phoy/` = 200 |
| PC-010 | TikTok Liked Classify | 14 | pending | พี่เจ + พาเที่ยว | สคริปต์พร้อม · รอไฟล์ export จากพี่เจ |
| PC-011 | DSH Tooling / Knowledge Ops | 100 | done | พาเที่ยว | corpus 2,673 docs · MCP 2 entry ผ่าน handshake (38 tools) |
| PC-012 | Owner Mail + Local Automation | 59 | in_progress | พาเที่ยว | task `PaTeaw-OwnerMailIngest` / `JournalIngest` = all OK · สำรอง Vault ทำงาน 2 ทาง |
| PC-013 | Knowledge / Checkpoint / Dashboard | 71 | in_progress | พาเที่ยว | `--summary` รันจริง · canary ผ่าน · eval 10/10 (N/A 1) |
| PC-014 | Creator Knowledge Clips | 57 | in_progress | พี่เจ + พาเที่ยว | กลั่นแล้ว 10 คลิป (ชุด 1-2) · คลัง prompt H3 222 entry |

**สรุปภาพรวม:** done 4 · in_progress 9 · pending 2 · blocked 0 (จาก 14 การ์ด — blocked ระดับส่วนอยู่ใน PC-007 print และ PC-012 Task logon)

## Local Embedding (chroma content brain)

**ภาพรวม:** vector search งานพาเที่ยว — **ครบ 8/8 ส่วน** · store local `vec_test` · model default **local bge-m3 (dim 1024)**

| # | ส่วน | สถานะ | หลักฐาน |
|---|---|---|---|
| 1 | corpus collect (`vec_collect.py`) | done | **2,673 docs · 174 src** (26 ก.ย. 69) — เพิ่ม glob ต่อโฟลเดอร์ `04_Sales_Marketing` · `03_AI_Checkpoints` · `03_Reference_Indexes` · `04_Profiles_and_Governance` · `01_AI_Protocols` |
| 2 | store + query (`patheaw_work`) | done | local bge-m3 dim 1024 · collection แยก `patheaw_local` / `patheaw_bge` สำหรับทดสอบ |
| 3 | meter (`embed_meter.py`) | done | หลังเปลี่ยนเป็น local = API call 0 (build/search) |
| 4 | watcher อัตโนมัติ | done | task `PaTeaw-ChromaWatcher` = Ready · รอบทุก 30 นาที |
| 5 | ครอบการ์ด PC | done | **14/14 ใบ** (`pc_001`…`pc_014`) |
| 6 | ครอบ serena memory | done | **12/12** (`mem_*` + `gochisou_memory`) |
| 7 | ครอบ rules + SOP | done | `system-rules/*` ทุกระบบ · `02_Operations_SOP/*` · indexes · governance |
| 8 | auto-load ใน `/work` | done | chunk มี `section` → คืน `{src, section}` ให้เปิดไฟล์จริงจาก hint |

**สาขา / เวอร์ชัน**

| ต้นทาง (ราก) | แตกเป็น / เวอร์ชัน | จำนวน | สถานะแต่ละตัว |
|---|---|---|---|
| embedding engine | local bge-m3 (default) · API gemini (fallback) · MiniLM (สำรอง) | 3 | default · legacy `VEC_ENGINE=api` · collection แยก |
| collection | `patheaw_work` · `patheaw_local` · `patheaw_bge` | 3 | prod · ทดสอบ · ทดสอบ |
| วิธีเก็บเข้าคลัง | whitelist ชื่อไฟล์ (เดิม) · glob ต่อโฟลเดอร์ (26 ก.ย. 69) | 2 | เลิกใช้ · ใช้จริง |

## หมายเหตุการดูแลหน้านี้

- ตัวเลขที่ต้องรีเฟรชทุกครั้งที่ปิดรอบ: corpus docs/src · สถานะการ์ด · ตัวเลข KPI ของ PC-009
- หน้านี้สะท้อน **§9 System Map ของการ์ด** — ถ้าการ์ดเปลี่ยน หน้าต้องเปลี่ยนตาม (ไม่เขียนมือแยกจากหลักฐาน)
- ห้ามใส่รายการงานค้างในหน้านี้ (งานค้างอยู่ที่ `03_AI_Checkpoints/PC-XXX.md` §10)
