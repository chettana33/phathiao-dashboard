---
title: "MiniMax Studio — เครื่องมือ + สถานะงาน (อัปเดต 12 ก.ย. 69)"
type: "note"
tags: ["dashboard", "minimax", "skills", "clip-studio", "gochisou", "ichinotour", "okf"]
status: "active"
created: 2026-09-11T13:20:00+07:00
last_updated: 2026-09-12T22:40:00+07:00
version: "2.0"
owner: "พี่เจ & พาเที่ยว"
source_of_truth: "Obsidian & GitHub"
---
# MiniMax Studio — เครื่องมือ + สถานะงาน

> อัปเดต 12 ก.ย. 69 22:40 (ตัวเลขจากของจริง: gateway `/api/v1/credit/wallet` · tool count จาก MCP ที่ต่อใน DSH · checkpoint ล่าสุด)
> ตัวเลขทุกบรรทัดมาจากการรันจริง — ไม่มีข้อไหนเป็น "คาดว่า"

## 1. ทำเสร็จแล้ว (12 ก.ย. 69)

| งาน | ผลจริง | หลักฐาน |
|---|---|---|
| **MCP MiniMax เข้า DSH** | 58 tools ใช้ในแชตได้ (`mcp__minimax__*`: generate_video/image/audio · ffmpeg · merge_videos · subtitle_format · canvas · media_transcribe) | ยิง `list_capabilities` ได้ manifest จริง · `generate_audio_speech` ได้ไฟล์ mp3 3.64 วิ |
| **MCP Google Workspace เข้า DSH** | 62 tools (`mcp__google-workspace__*`: Drive/Gmail/Calendar/Sheets) | authorize แล้ว · `list_drive_items` คืนไฟล์จริง 3 ไฟล์ |
| **H3 native audio ภาษาไทย** | **ได้จริง** — i2v 4 วิ 768P + `generate_audio:true` + บทไทยใน prompt ≈ **280 เครดิต** → เสียงไทย 100% ตรงบท | `Raw\mm_talking_head\tabi-i2v-thai-audio-test-v1.mp4` + QC 4 ไฟล์ · ปากขยับสอดคล้อง 11/13 เฟรม (kling avatar เดิม ≈67-73%) |
| **Video Editor (clip-studio) ขับอัตโนมัติได้ 100%** | สร้าง host harness แทน host ของแอป (แอปโหลด plugin ไม่มี host SDK → สั่งผ่านแอป timeout ทุกครั้ง) | import → `cut_silences` **1 ช่วง 0.7 วิ** (4.458→3.758) → `import_srt` **2 cue ไทย** (3.658) → diagnostics clean → snapshot + vision QC ผ่าน |
| **CapCut** | ติดตั้ง `9.4.0.4015` + **export draft เข้า CapCut สำเร็จ** (สื่อคัดลอก 1 ไฟล์ · canvas 768×1344 · มี text ไทย 2 อัน) | `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\minimax design项目导入` (draft_info.json) |
| **Skill `phathiao-ingest`** | สูตร QC คลิป (เฟรม → DeepSeek vision → transcribe → checklist → checkpoint) | เข้า skill catalog + mirror Vault/GitHub |
| **ความปลอดภัย/เอกสาร** | แก้ `secret_guard.py` ให้จับ `GOOGLE_OAUTH_CLIENT_SECRET` (เดิมหลุด!) · SOP `clip-studio-harness-sop.md` · lessons #132-138 | commit brain `4d2c00e` |

## 2. ตัวเลขจริง (12 ก.ย. 69)

| รายการ | ค่า |
|---|---|
| เครดิต MiniMax | **≈9,006** (bucket 9,250 + 36 · หมดอายุ 2026-10-10) — บันทึกเก่า "36" = ล้าสมัย |
| ต้นทุนต่อคลิปสั้น | H3 i2v 4 วิ ≈ 280 · 5 วิ ≈ 350 · kling avatar ≈ 650 · 30 วิ ≈ 2,100 |
| Tools ที่ใช้ได้ในแชต | MiniMax 58 · Google Workspace 62 (รวมของเดิม 5 ตัว = ~125) |
| Chroma content-brain | 952 chunks |

## 3. เหลืออะไร

### 3.1 งานผลิต (คิวถัดไป)
| # | งาน | สถานะ |
|---|---|---|
| 1 | **คลิป 4 Gochisou "ภาษาไม่เก่ง จองร้านต้องโทรเท่านั้น"** (กิ่ง A) | บท approve แล้ว (Content Map 9 ก.ย.) · **ยังไม่เริ่มผลิต** — ต้องแก้ VO ให้ใช้คำมาตรฐาน "เรามีทีม Land Operation พร้อมช่วยคุณ" + ทำ SRT ไทยเอง (ASR แอปถอดไทยเป็นจีน ใช้ไม่ได้) |
| 2 | character bible / continuity (Tabi + พาเที่ยว) | ยังไม่ทำ (แผน 11 ก.ย. §4.1-1 — ทำได้ฟรี) |
| 3 | Skill "Phathiao Clip Pipeline" (สูตรประกอบคลิปเต็ม) | ยังไม่ทำ (ส่งมอบแล้วแค่ `phathiao-ingest` = QC) |
| 4 | `voice-clone` → `koc-video` (ทดลองตามลำดับแผน) | ยังไม่แตะ · `koc-video` กินเครดิต |
| 5 | Meawbin คลิป 19 (Day 04-05 Q&A) | ค้างจาก 11 ก.ย. |

### 3.2 งานระบบ
| # | งาน | สถานะ |
|---|---|---|
| 6 | **rotate Google OAuth client secret** | เลื่อนเป็น **13 ก.ย.** (พี่เจสั่ง) — secret หลุดเข้า transcript 12 ก.ย. ต้องหมุน |
| 7 | **linkdigest MCP** (transcript+OCR ลิงก์ TikTok/YT) | เลื่อนเป็น **13 ก.ย.** — ต้องเอา API key (ฟรี 3 digests) จาก linkdigest.dev/app/keys |
| 8 | social-post MCP (YouTube/TikTok/FB) | ยังไม่มีในตลาด — ต้องสร้างเอง |
| 9 | `redfox-community-dsh` · `last30days-skill-cn` | ยังไม่ประเมิน |
| 10 | cold-boot test: ปิดแอป MiniMax แล้วเปิด DSH ใหม่ (reconnect ตั้งไว้ 2 ชม.) | ยังไม่ทดสอบ |

## 4. ข้อจำกัดที่ต้องรู้

- ทุกอย่างในแอป **กินเครดิต** ยกเว้น ffmpeg/ตัดต่อในตัว
- **Video Editor ในแอปสั่งผ่าน API ของแอปไม่ได้** (แอปโหลด plugin แบบไม่มี host) → ใช้ host harness ที่เราสร้าง (SOP: `00_SOP_Master/02_Operations_SOP/clip-studio-harness-sop.md`) · harness ต้องรัน proxy + เบราว์เซอร์ค้างไว้
- **ห้ามทำซับไทยจาก ASR ของแอป** (ถอดไทยออกเป็นตัวจีน) — ทำ SRT เองแล้ว `import_srt`
- ผลจากแอปต้อง QC ต่อด้วย DeepSeek vision + transcribe (`system-rules/gochisou.md` §3)
- Google Workspace MCP = สิทธิ์ **เขียน** (ส่งเมล/แชร์ไฟล์/แก้ Sheet) — ห้ามใช้กับข้อมูลลูกค้า/การเงินโดยไม่สั่ง
- ไฟล์เต็ม: `04_Sales_Marketing/MiniMax_Skills_Plan_2026-09-11.md` + `system-rules/gochisou.md` (Vault)
