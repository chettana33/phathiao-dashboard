---
title: "System Map"
type: "dashboard"
---

# 🗺️ System Map

> อัปเดตโดยพาเที่ยวทุกปิดงาน (manual + schema §9 การ์ด PC) — เห็นทั้งระบบ: **กี่ส่วน / เสร็จกี่ส่วน / สาขา-เวอร์ชัน**
> สถานะ: done (เขียว) · in_progress (ฟ้า) · blocked (แดง) · pending (เทา) · %progress + เจ้าของ ต่อส่วน
> **เป้าหมาย:** ขยายให้ทุกการ์ด PC / ทุกงาน ครอบคลุม vector DB (chroma content brain) — ค่อย ๆ ทำทีละระบบ (6 ก.ย. 69)

## Local Embedding (chroma content brain)

**ภาพรวม:** vector search งานพาเที่ยว — corpus = Gochisou + PC + checkpoint + lessons + ความรูทั้งระบบ (AGENTS/SOP/locator/indexes/memories) · store local `vec_test` · เสร็จ **6/8 ส่วน** · default = **local bge-m3** (6 ก.ย. 69 พี่เจเลือก)

### ส่วน

| # | ส่วน | %progress | สถานะ | เจ้าของ | หมายเหตุ |
|---|---|---|---|---|---|
| 1 | corpus collect (`vec_collect.py`) | 100% | done | พาเที่ยว | 27 แหล่ง 314 docs (Gochisou + PC + checkpoint + lessons + raw manifest) |
| 2 | store + query (`patheaw_work`) | 100% | done | พาเที่ยว | **local bge-m3 dim 1024** — สลับ default 6 ก.ย. (พี่เจเลือก) |
| 3 | meter (`embed_meter.py`) | 100% | done | พาเที่ยว | log ทุก Gemini embed call — หลัง local = API call เหลือ 0 (build/search) |
| 4 | pilot local MiniLM (`patheaw_local`) | 100% | done | พาเที่ยว | dim 384 · 311 docs 39.3s · eval 20/28 (71%) — ตัวสำรอง |
| 5 | pilot local bge-m3 (`patheaw_bge`) | 100% | done | พาเที่ยว | dim 1024 · 312 docs 180s · eval 20/28 (71%) |
| 6 | ตัดสินใจ default model | 100% | done | พี่เจ | **เลือก local bge-m3** (6 ก.ย.) — คุณภาพไทย/ญี่ปุ่นสูงสุด ฟรี/ไร้ 429 |
| 7 | ขยาย corpus ครอบทั้งระบบ | 80% | in_progress | พาเที่ยว | รอบ 1 เสร็จ 6 ก.ย.: 314 → 506 docs — AGENTS/3LAYER/locator/indexes/memories/SOP/workflow_tree + secret gate (0 รั่ว) — eval ระบบผ่าน |
| 8 | auto-load ใน `/work` | 10% | in_progress | พาเที่ยว | hint layer: คืน src/section ไม่ใช่ snippet — design พร้อม |

### สาขา / เวอร์ชัน

| ต้นทาง (ราก) | แตกเป็น / เวอร์ชัน | จำนวน | สถานะแต่ละตัว |
|---|---|---|---|
| embedding engine | local bge-m3 (default) · API gemini (fallback) · MiniLM (สำรอง) | 3 | default · legacy `VEC_ENGINE=api` · collection แยก |
| collection | patheaw_work · patheaw_local · patheaw_bge | 3 | prod (bge-m3) · ทดสอบ MiniLM · ทดสอบ bge-m3 (pilot) |
| key modlens (Gemini) | yukikameda51 · kimonoland · chettana33 | 3 | index 0 ฟรี · ฟรี · billing (ท้าย) — เหลือใช้เฉพาะ fallback |

## Gochisou TikTok — ระบบงาน 5 สาย (PC-009)

**ภาพรวม:** แบ่งตาม**สายงานธุรกิจ (workstream)** ไม่ใช่แค่ระบบผลิต — 3 หน้า (Front: สร้าง→โพสต์→ขาย) + 2 หลัง (Back: ข้อมูล→เงิน) = วงจร **Customer-to-Cash** · คลิปแรกยัง 0 (pilot v3 reject 6 ก.ย. — เสียง TTS เพี้ยน lessons #107) · โครงสร้างนี้จะ reuse กับ Ichinotour (lessons #108)

### ส่วน (สายงาน)

| # | สายงาน | %progress | สถานะ | เจ้าของ | หมายเหตุ |
|---|---|---|---|---|---|
| 1 | **Content Production** — คิด/สร้างจริง/วางแผนต่อยอด | 45% | in_progress | พาเที่ยว + พี่เจ | idea/script/ภาพ/VO/QC — pilot v3 reject ต้องทำคลิปใหม่ (ดูส่วนย่อยข้างล่าง) |
| 2 | **Publishing + Growth** — ลงโพสต์จริง TikTok + feedback | 15% | in_progress | พี่เจ | ช่อง @gochisou_booking setup done (2 ก.ย.) — คลิปแรก 0, batch queue design พร้อม (PC-009 §4) |
| 3 | **Sales + Booking** — ลูกค้าทัก → จองจริง → ปิดงาน | 35% | in_progress | พาเที่ยว | Landing + form (email field 5 ก.ย.) + LINE poll cloud (gochisou-monitor) + Firestore quotations done — จองจริง 0 รอคลิป |
| 4 | **CRM + Data** — บันทึกข้อมูลลูกค้า/lead | 20% | in_progress | พาเที่ยว | quotations มี source=gochisou + email; lead hygiene = งานค้าง B7; นิยาม Lead ตายตัว = A2 7 ก.ย. |
| 5 | **Finance + Admin** — เอกสารบัญชี/การเงิน | 5% | pending | พี่เจ | KPI ต้นทุน/กำไร (M3) รอตัวเลข (A4); ยังไม่มีเอกสารบัญชีลูกค้า |

### ส่วนย่อย — สาย 1 Content Production

| # | ส่วน | %progress | สถานะ | เจ้าของ | หมายเหตุ |
|---|---|---|---|---|---|
| 1 | Idea prompt (`idea_engine.md`) | 100% | done | พาเที่ยว | 1 แบบ ครอบ persona + ฤดูกาล — ใช้เช้า |
| 2 | Script prompt Gemini (`gemini_ideas.py`) | 100% | done | พาเที่ยว | BASE + extra ต่อวัน + chroma context กันซ้ำ (B17 6 ก.ย.) |
| 3 | Script พาเที่ยว (P1-4 persona) | 60% | in_progress | พี่เจ | draft `scripts_4persona.md` — รอคัดกับพี่เจ |
| 4 | Style guide + QC checklist | 100% | done | พาเที่ยว | constrain ทุก prompt (ห้ามโม้/CTA ใช้ได้ 6 ก.ย.) |
| 5 | Omni/Flow ภาพ prompt | 40% | in_progress | พี่เจ | ต่อคลิป — ภาพ "ดู AI" ต้องผสมภาพจริง/stock |
| 6 | pilot คลิปใหม่ | 10% | in_progress | พาเที่ยว + พี่เจ | pilot v3 reject 6 ก.ย. (เสียง "ตั๋ว/ยากินิกิ" เพี้ยน) — QC เสียงต้อง transcribe เทียบบท (lessons #107) |
| 7 | Batch approval + posting queue | 10% | pending | พาเที่ยว | design พร้อม (PC-009 §4) — หลังคลิปแรก |
| 8 | validation gate 2 สัปดาห์ | 0% | pending | พาเที่ยว | ตั้งวัน review หลังคลิปแรก + 14 วัน |

### สาขา / เวอร์ชัน

| ต้นทาง (ราก) | แตกเป็น / เวอร์ชัน | จำนวน | สถานะแต่ละตัว |
|---|---|---|---|
| prompt ต่อ persona | บริษัททัวร์ · ไกด์ · FIT/ครอบครัว · กรุ๊ป 40+ | 4 | ครบ 4 (P1-4 + G1-4 ใน scripts_combined) |
| persona × ฤดูกาล × ประเภท | 4 persona × 4 ฤดู × 3 ประเภท (ความรู้/เคส/อยากกิน) | 48 มุม | ใช้ไอเดียได้ไม่ซ้ำ |
| script ที่เคยทำ | Batch1 5 · P1-4 · G1-4 · scripts_485 | 13+ | ใช้กันซ้ำ (chroma ชี้) |
| เสียง VO | charon (default) · algenib · fenrir | 3 | ฟรี Gemini TTS — วนได้; **ต้อง transcribe ตรวจคำทับศัพท์ทุกครั้ง** (#107) |
| CTA ท้าย | "ช่วยจองให้ได้" · "ช่วยเช็คและจองร้าน" · "อยู่ญี่ปุ่น จัดการแทน" | 3 | ใช้ได้ทั้งหมด (พี่เจ 6 ก.ย.) |
| สายงาน (workstream) | 5 สาย: Content/Publishing/Sales/CRM/Finance | 5 | 3 หน้า + 2 หลัง — reuse กับ Ichinotour ได้ |
