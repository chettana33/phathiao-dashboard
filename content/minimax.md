---
title: "MiniMax Design — Skills / Plugins / Connectors (แผนใช้กับงานเรา)"
type: "note"
tags: ["dashboard", "minimax", "skills", "connector", "gochisou", "ichinotour", "okf"]
status: "active"
created: 2026-09-11T13:20:00+07:00
last_updated: 2026-09-11T13:20:00+07:00
version: "1.0"
owner: "พี่เจ & พาเที่ยว"
source_of_truth: "Obsidian & GitHub"
---
# MiniMax Design — Skills / Plugins / Connectors

> ตรวจของจริง 11 ก.ย. 69 (ไม่เดา): `/api/skills` แอป · `/api/skills/market` · manifest ของ plugin ในตัวแอป · capability manifest · ทดสอบ REST connector 8 เส้นทาง
> **สถานะ: พี่เจ approve 11 ก.ย. 69** — แผนช่องทาง 3 ตัด ✅ · แผนฝั่งพาเที่ยว (V4.1) ✅ · KOC-video + Video Editor = ทดสอบคืนนี้

## 1. บัญชี + เครดิต (จริง)

| รายการ | ค่า |
|---|---|
| บัญชีแอป | Chettana Suparatarpa · userID `553409288619683847` · group_id `2097222684311036351` |
| แผน | Media Plan Starter (มีอยู่แล้ว) |
| เครดิต | 36 (ก่อนเติม) · bucket หมดอายุ 2026-10-10 06:59 |
| เติม | $10.5 (11 ก.ย. 69) — ยังไม่ใช้ |

## 2. Skills (ติดตั้ง 20 · ตลาด 20)

**ตัวที่เลือกใช้กับงานเรา (พี่เจ approve แล้ว)**

| Skill | ใช้ทำอะไร | สถานะ |
|---|---|---|
| `koc-video` | talking head / POV / testimonial / product seeding | ทดสอบคืนนี้ |
| `voice-clone` | เสียงประจำตัว (ชาย/หญิง) consent-based — แก้ปัญหาเสียงไม่ตรงตัวละคร | คิวถัดไป |
| `education-studio` | คลิปยาว YouTube: ทัวร์ 1 เมือง / วิธีจอง / วัฒนธรรม | คิวถัดไป |
| `paper-collage-explainer-generator` | คลิปอธิบาย (ค่าใช้จ่าย/ขั้นตอนจอง) ต้นทุนต่ำ | คิวถัดไป |
| `brand-promo-video-generator` / `brand-ad` | Hero film 15-45 วิ ให้ ichinotour B2B | คิวถัดไป |
| `character-scene-storyboard` (ตลาด) | design sheet ตัวละครคงที่ก่อนทำซีรีส์ | คิวถัดไป |
| `music-3.0` + `lyrics_generation` | BGM ประจำช่อง (ธีมเดียวทุกคลิป = แบรนด์จำได้) | คิวถัดไป |
| `clip-export` (ตลาด) | ส่งเข้า CapCut/剪映 draft | คิวถัดไป |
| `fpv-tour-video-generator` (featured) | คลิปทัวร์ FPV — คู่แข่งไทยแทบไม่มี | เก็บไว้ |
| `fashion-scene-video-planner` / `sitcom-story-video` (featured) | เอา "วินัยล็อกสเปก" + "bible ตัวละคร/ฉาก" มาใช้เป็นแม่แบบซีรีส์ | เก็บไว้ |

## 3. Plugins ในตัวแอป (bundled) — ที่ยังไม่เคยใช้

| Plugin | ทำอะไร | แผน |
|---|---|---|
| Video Editor (`clip-studio` v0.10.2) | ตัดอัตโนมัติ · ลบช่วงเงียบ · ซับอัตโนมัติ · timeline/transition/สี · export เข้า CapCut | ทดสอบคืนนี้ (ฟรี) |
| Director Stage (3D v0.24.8) | หุ่น 3D + กล้อง + path → storyboard/blocking ก่อนเจน | เก็บไว้ |
| ComfyUI (v0.2.4) | node editor ในแอป + backend จัดการให้ | ยังไม่ต้อง (ต้องโหลดโมเดลเอง) |

## 4. Connectors — ตรวจแล้ว

- ❌ แอปยังไม่มี Connector API เราเรียกได้ (`/api/connectors`, `/api/mcp`, `/api/integrations` = 404 ทั้งหมด) · config มีแค่ช่อง `customMcpVault`
- ✅ Connector ที่ทำงานจริง = MCP ฝั่งเรา: DSH 5 ตัว (chroma · vault-search · playwright · google-workspace · firebase) + opencode 2 บัญชี Google Workspace (kimonoland + info@)
- 🎯 ควรดึงเพิ่ม (พี่เจ approve)
  1. MCP ต่อแอป MiniMax ตรง (เจนภาพ/วิดีโอ/เพลง/ตัดต่อจากในแชต)
  2. `linkdigest-mcp` — ลิงก์ TikTok/YouTube → transcript + timecode + OCR (deconstruct คู่แข่ง + QC)
  3. `redfox-community-dsh` — 100+ skill ข้อมูลโซเชียล + 40 MCP tool
  4. `last30days-skill-cn` — สแกนเทรนด์ 8 แพลตฟอร์ม 30 วัน
  5. `riffkit/skill` — riff คลิปที่ชนะเป็นสูตรของเรา
  6. MCP โพสต์ YouTube/TikTok/FB — ยังไม่มีในตลาด ต้องสร้างเอง

## 5. แผนช่องทาง ichinotour — โครงเดียว 3 ตัด (approve)

| ช่อง | รูปแบบ | เครื่องมือ |
|---|---|---|
| TikTok | 20-35 วิ แนวตั้ง | H3 i2v + kling avatar + Video Editor (ซับ) |
| YouTube Shorts | เหมือน TikTok + ซับ/ชื่อเรื่องค้นหาได้ | เพิ่ม `music-video-subtitle-generator` + `clip-export` |
| YouTube ยาว | 60-180 วิ (1 เมือง / 1 ร้าน / วิธีจอง) | `education-studio` + `mg-voiceover-animation-generator` |
| Facebook | 60-120 วิ + ข้อความยาว | asset ชุดเดียวกับ YouTube ตัดต่างกัน |
| ichinotour B2B | Hero 15-45 วิ | `brand-promo-video-generator` |

## 6. ฝั่งพาเที่ยว (V4.1) — ที่ควรมีเพิ่ม (approve)

| เพิ่ม | ทำไม |
|---|---|
| MCP ต่อแอป MiniMax เข้า DSH | วันนี้เรียกผ่าน `mm_run.py` เท่านั้น — ต่อ MCP แล้วใช้ tool แอปในแชตได้เลย |
| Google Workspace MCP เข้า DSH | binary มีแล้ว (`workspace-mcp.exe`) — Sheets/Drive ในแชต |
| `linkdigest` MCP | QC/วิจัยคู่แข่งด้วย transcript + OCR |
| Skill "Phathiao Ingest" (เขียนเองด้วย `skill-creator`) | รวมสูตร คลิป → ffmpeg → `read_image_deepseek` → QC → checkpoint |

## 7. ข้อจำกัด (ต้องรู้ก่อนใช้)

- ทุกอย่างในแอปกินเครดิต ยกเว้น ffmpeg/ตัดต่อในตัว · H3 30 วิ ≈ 2,100 เครดิต
- Skill ของแอปบังคับหยุดยืนยันกับผู้ใช้หลายจุด (ไม่ใช่ auto 100%)
- ผลจากแอปต้อง QC ต่อด้วย DeepSeek vision + transcribe (`system-rules/gochisou.md` §3)
- ไฟล์เต็ม: `04_Sales_Marketing/MiniMax_Skills_Plan_2026-09-11.md` (Vault)
