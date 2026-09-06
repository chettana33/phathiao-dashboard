---
title: "System Map"
type: "dashboard"
---

# 🗺️ System Map

> อัปเดตโดยพาเที่ยวทุกปิดงาน (manual + schema §9 การ์ด PC) — เห็นทั้งระบบ: **กี่ส่วน / เสร็จกี่ส่วน / สาขา-เวอร์ชัน**
> สถานะ: done (เขียว) · in_progress (ฟ้า) · blocked (แดง) · pending (เทา)

## Local Embedding (chroma content brain)

**ภาพรวม:** vector search งานพาเที่ยว — corpus Gochisou/PC/checkpoint/lessons · store local `vec_test` · เสร็จ **5/8 ส่วน**

### ส่วน

| # | ส่วน | สถานะ | หมายเหตุ |
|---|---|---|---|
| 1 | corpus collect (`vec_collect.py`) | done | 27 แหล่ง 311 docs (Gochisou + PC + checkpoint + lessons + raw manifest) |
| 2 | store + query API (`patheaw_work`) | done | gemini-embedding-001 dim 3072 — prod ปัจจุบัน |
| 3 | meter (`embed_meter.py`) | done | log ทุก embed call รายวัน (6 ก.ย.) — 39 search/2 build ไร้ error |
| 4 | pilot local MiniLM (`patheaw_local`) | done | dim 384 · 311 docs 39.3s · eval 20/28 (71%) |
| 5 | pilot local bge-m3 (`patheaw_bge`) | done | dim 1024 · 312 docs 180s · eval 20/28 (71%) |
| 6 | ตัดสินใจ default model | blocked | รอพี่เจ: API 75% vs local 71% (ห่าง 1 ข้อ, local ฟรี/ไร้ 429) |
| 7 | ขยาย corpus ครอบทั้งระบบ | pending | AGENTS/3LAYER/locator/SOP — whitelist + secret gate ก่อน |
| 8 | auto-load ใน `/work` | pending | hint layer: คืน src/section ไม่ใช่ snippet |

### สาขา / เวอร์ชัน

| ต้นทาง (ราก) | แตกเป็น / เวอร์ชัน | จำนวน | สถานะแต่ละตัว |
|---|---|---|---|
| embedding model | API gemini-embedding-001 · MiniLM multilingual · bge-m3 | 3 | prod (API) · pilot done · pilot done |
| collection | patheaw_work · patheaw_local · patheaw_bge | 3 | ใช้งาน · ทดสอบ · ทดสอบ |
| key modlens (Gemini) | yukikameda51 · kimonoland · chettana33 | 3 | index 0 ฟรี · ฟรี · billing (ท้าย) |

## Gochisou TikTok — Prompt / ระบบผลิต (PC-009)

**ภาพรวม:** คลิปแรกยังไม่ผ่าน QC · prompt แตกตาม persona × ฤดูกาล × ประเภท — เสร็จ **4/8 ส่วน**

### ส่วน

| # | ส่วน | สถานะ | หมายเหตุ |
|---|---|---|---|
| 1 | Idea prompt (`idea_engine.md`) | done | 1 แบบ ครอบ persona + ฤดูกาล — ใช้เช้า |
| 2 | Script prompt Gemini (`gemini_ideas.py`) | done | BASE + extra ต่อวัน + chroma context กันซ้ำ (B17 6 ก.ย.) |
| 3 | Script พาเที่ยว (P1-4 persona) | in_progress | draft `scripts_4persona.md` — รอคัดกับพี่เจ |
| 4 | Style guide + QC checklist | done | ใช้ constrain ทุก prompt (ห้ามโม้/CTA 3 แบบใช้ได้ 6 ก.ย.) |
| 5 | Omni/Flow ภาพ prompt | in_progress | ต่อคลิป — ภาพ "ดู AI" ยังต้องแก้ (ภาพจริง/stock ผสม) |
| 6 | pilot คลิปใหม่ | in_progress | รอ Decision 1-2 (billing + บท VO) → ประกอบ → QC |
| 7 | Batch approval + posting queue | pending | design พร้อม (PC-009 §4) — หลังคลิปแรก |
| 8 | validation gate 2 สัปดาห์ | pending | ตั้งวัน review หลังคลิปแรก + 14 วัน |

### สาขา / เวอร์ชัน

| ต้นทาง (ราก) | แตกเป็น / เวอร์ชัน | จำนวน | สถานะแต่ละตัว |
|---|---|---|---|
| prompt ต่อ persona | บริษัททัวร์ · ไกด์ · FIT/ครอบครัว · กรุ๊ป 40+ | 4 | ครบ 4 (P1-4 + G1-4 ใน scripts_combined) |
| persona × ฤดูกาล × ประเภท | 4 persona × 4 ฤดู × 3 ประเภท (ความรู้/เคส/อยากกิน) | 48 มุม | ใช้ไอเดียได้ไม่ซ้ำ |
| script ที่เคยทำ | Batch1 5 · P1-4 · G1-4 · scripts_485 | 13+ | ใช้กันซ้ำ (chroma ชี้) |
| เสียง VO | charon (default) · algenib · fenrir | 3 | ฟรี Gemini TTS — วนได้ |
| CTA ท้าย | "ช่วยจองให้ได้" · "ช่วยเช็คและจองร้าน" · "อยู่ญี่ปุ่น จัดการแทน" | 3 | ใช้ได้ทั้งหมด (พี่เจ 6 ก.ย.) |
