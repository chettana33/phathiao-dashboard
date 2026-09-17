---
title: "MiniMax Studio — เครื่องมือ + สถานะงาน (อัปเดต 17 ก.ย. 69)"
type: "note"
tags: ["dashboard", "minimax", "skills", "clip-studio", "gochisou", "ichinotour", "okf"]
status: "active"
created: 2026-09-11T13:20:00+07:00
last_updated: 2026-09-17T22:35:00+07:00
version: "3.0"
owner: "พี่เจ & พาเที่ยว"
source_of_truth: "Obsidian & GitHub"
---
# MiniMax Studio — เครื่องมือ + สถานะงาน

> อัปเดต 17 ก.ย. 69 (ตัวเลขจากของจริง: gateway `/api/v1/credit/wallet` · `list_capabilities` · `get_model_concurrency` · นับการใช้ tool จาก session log DSH 163 ไฟล์)
> ตัวเลขทุกบรรทัดมาจากการรันจริง — ไม่มีข้อไหนเป็น "คาดว่า"

## 1. ตัวเลขจริง (17 ก.ย. 69)

| รายการ | ค่า |
|---|---|
| เครดิตคงเหลือ | **3,820** (plan Media Plan Starter · เติมเป็นรอบรายเดือน) |
| ราคาที่วัดได้ | 768P = **70 เครดิต/วิ** → 5วิ 350 · 10วิ 700 · 15วิ 1,050 |
| 2K (≈×2.4) | 15วิ ≈ **1,680** · 10วิ ≈ 1,120 · 5วิ ≈ 560 |
| ความยาวสูงสุดของ H3 | **4–15 วิ** (เกิน 15 ไม่ได้ — งานพูดยาวต้องใช้ kling avatar) |
| คิวขนาน (concurrency) | MiniMax-H3 = **5 slots** (ว่าง 5/5) · H3-Max = 5 · H3-Max-Turbo = ไม่จำกัด |
| โมเดลที่มี | MiniMax H3 · MiniMax H3 Max · MiniMax H3 Max Turbo (Max ไม่มี 2K และไม่มี `generate_audio`) |
| งบ Gochisou (มติพี่เจ 17 ก.ย. 69) | **1,000 บาท/เดือน** |

## 2. งบต่อคลิป — ตีกรอบให้ H3 ไม่เกินเครดิต

**หน่วยมาตรฐาน 1 คลิป = "hook test 768P 5วิ (350) + final 2K 15วิ (1,680)" = 2,030 เครดิต**

| แผน | องค์ประกอบ | ใช้ | เหลือจาก 3,820 |
|---|---|---|---|
| **แนะนำ** | แนวA: hook 350 + final 2K 1,680 · แนวB: hook 350 + final 768P 1,050 | **3,430** | 390 |
| ปล่อยของ 2 ตัว 2K | แนวA hook 350 + 2K 1,680 · แนวB 2K 1,680 (ข้าม hook B) | 3,710 | 110 |
| ครบ 3 แนว ไม่ 2K | 3 × (hook 350 + final 768P 1,050) | 4,200 | ❌ เกิน |
| 3 แนว 768P ล้วน | 3 × 1,050 | 3,150 | 670 |

- กฎเหล็ก: **ห้ามเจน 2K ก่อนเทสต์ hook 5 วิ** (playbook §2) · เช็คยอดก่อนเจนทุกครั้ง
- **คอขวดจริงไม่ใช่เครดิต** — ถ้าแพ็ก Starter ≈ ฿300/10,000 เครดิต (บันทึก 9 ก.ย. 69: $8.4) งบ ฿1,000/เดือน ≈ **~3 หมื่นเครดิต** = ~19 คลิป 2K/เดือน ⇒ ผลิตไม่ทันอยู่แล้ว · ที่จำกัดคือ "ก้อนที่มีตอนนี้" (3,820) ไม่ใช่งบรายเดือน (ต้องยืนยันราคาแพ็กจริง)

## 3. Tool ทั้ง 58 — สถานะการใช้จริง (นับจาก session log 163 ไฟล์)

- **ใช้จริงแล้ว 16** · **ไม่เคยแตะ 35** · **อ้างถึงแต่ไม่มีบันทึกการเรียก 7**

### 3.1 ใช้จริงแล้ว 16

`generate_video` 95 · `generate_audio_speech` 76 · `generate_image` 30 · `memory` 12 · `analyse_media` 8 · `list_capabilities` 8 · `image_search` 8 · `canvas_list_nodes` 7 · `plugin_agent_invoke` 6 · `canvas_get_node` 4 · `voice_prepare` 4 · `media_transcribe` 4 · `plugin_agent_describe` 3 · `plugin_agent_open_editor` 3 · `get_model_concurrency` 2 · `search_knowledge` 2

### 3.2 ไม่เคยแตะเลย 35

**วิดีโอ/ภาพ:** `image_remove_background` · `batch_lip_sync` · `merge_videos` · `read`
**เสียง:** `audio_analyze_music` · `audio_meta` · `audio_separate` · `generate_audio_music` · `lyrics_generation` · `music_cover`
**วางแผน/แคนวาส:** `plan_write` · `plan_get_stage_status` · `plan_get_stage_detail` · `plan_get_work_items` · `plan_update_stage_state` · `plan_replan` · `plan_patch_stage` · `canvas_write_node` · `canvas_read_text` · `canvas_grep_text` · `canvas_apply_text_edits` · `canvas_group_nodes` · `canvas_ungroup_node`
**คลัง/อ้างอิง:** `asset_center_search` · `asset_center_use_entity` · `web_media` · `select_image_recipe`
**ComfyUI 8:** `list_comfyui_template` · `list_comfyui_workflow` · `get_comfyui_workflow` · `edit_comfyui_workflow` · `run_comfyui_workflow` · `save_comfyui_workflow` · `get_comfyui_run_status` · `open_comfyui`
**อื่น ๆ:** `report_outcome`

### 3.3 อ้างถึงแต่ไม่มีบันทึกการเรียก 7 (ไม่ยืนยัน)

`ffmpeg` · `subtitle_format` · `preview_and_collect_feedback` · `canvas_group_recent_outputs` · `add_comfyui_workflow` · `save_comfyui_run_as_workflow` · (นับจาก mention สูงกว่า baseline แต่ parse record ไม่ได้)

## 4. ทดสอบสด 17 ก.ย. 69 — เฉพาะตัวที่ไม่กินเครดิตเจน

| tool | ผล | หมายเหตุ |
|---|---|---|
| `audio_analyze_music` | ✅ ผ่าน | หลังแก้ runtime: BPM 143.6 · beat_times 5 จุด · impact 11 จุด · `mv_summary` แนะนำตัดถี่ + จำนวนช็อต ≈ 5 ⇒ **ใช้ทำ卡点ตามจังหวะได้** |
| `audio_meta` | ✅ ผ่าน | duration 2.554 วิ · mp3 · bitrate 135,267 |
| `web_media` (inspect) | ✅ ผ่าน | อ่าน metadata คลิปต้นแบบจาก URL ได้ |
| `get_model_concurrency` | ✅ ผ่าน | H3 available 5/5 |
| `asset_center_search` | ✅ เรียกได้ | ผลลัพธ์ **ว่าง** — ยังไม่มีตัวละคร/สไตล์ที่บันทึกไว้ในคลัง |
| `image_remove_background` | ⚠️ ต้อง copy ไฟล์เข้าโฟลเดอร์แอปก่อน | `Path traversal detected` เมื่อส่ง path นอกโฟลเดอร์แอป |
| `select_image_recipe` | ❌ | `Knowledge directory not found` — ต้องติดตั้ง knowledge pack |
| `search_knowledge` | ❌ | `Requested knowledge resource root is unavailable` (ตัวเดียวกัน) |
| `list_comfyui_template` | ❌ | schema พังในตัวแอป (`workflows[0].inputs Required`) = bug ของ build |

### 4.1 แก้ runtime ของแอปแล้ว (17 ก.ย. 69)

- อาการเดิม: `python runtime unavailable: executable not found at C:\Users\chett\.hub-dev\runtimes\python\python.exe`
- สาเหตุจริง: แพ็กเกจ `librosa/numpy` ที่แอปเตรียมไว้ compile มาสำหรับ **cp312** แต่ junction ชี้ python 3.14 ⇒ `ImportError: No module named 'numpy._core._multiarray_umath'`
- แก้: ติดตั้ง python 3.12 (uv) + junction `~\.hub-dev\runtimes\python` → `cpython-3.12-windows-x86_64-none` ⇒ `audio_analyze_music` ใช้ได้ทันที

## 5. ComfyUI — ตอบคำถาม "ถ้ามี backend จะควบคุมได้ไหม"

- **ควบคุมได้ในทางเทคนิค** (มี 8 tools: list/get/edit/run/save/status/open + add/save-run-as)
- **แต่ยังใช้ไม่ได้ 2 ชั้น:** ① ไม่มี backend ในเครื่อง (17 ก.ย. 69: ไม่มีโฟลเดอร์ ComfyUI · port 8188/8189/8000 ปิด) ② `list_comfyui_template` พังที่ schema ภายในแอปเอง
- ถ้าจะใช้จริง = ติดตั้ง ComfyUI (python + torch + โมเดล หลาย GB) หรือชี้ไป backend ที่รันที่อื่น ⇒ **ยังไม่คุ้มกับงานปัจจุบัน** (H3 2K พอสำหรับ 15 วิ)

## 6. งานผลิต (คิวถัดไป)

- เป้า: **"คลิปว้าว" 1 ตัวที่ 2K 15 วิ** (แนว A UGC เซลฟี่ในร้าน) + 1 ตัวทดลอง 768P (แนว B)
- ลำดับที่ใช้: `audio_analyze_music` (จังหวะ/จุดพีก) → `image_search` (ภาพจริงอ้างอิง) → hook 5 วิ 768P → พี่เจดู → final 2K
- QC gate ก่อนส่ง: 3 วิแรกหยุดนิ้ว · มีจุดพีก · ไม่มี AI tell · เทียบคลิปต้นแบบ · ไม่ว้าว = ห้ามส่ง

## 7. ข้อจำกัดที่ต้องรู้

- tool ในแอปใช้ได้เมื่อ **MiniMax Design เปิดอยู่** (gateway `127.0.0.1:8001`)
- path ของไฟล์ที่ป้อน tool (image/video) ต้องอยู่ใน**โฟลเดอร์แอป** (ไม่งั้น `Path traversal detected`)
- `batch_lip_sync` + `voice_prepare clone` = `Internal server error` (ฝั่งเซิร์ฟเวอร์ 12 ก.ย. 69) — อย่าเสียเวลาลองซ้ำ
- เสียงไทยใช้ได้กับ **H3 `generate_audio: true` (i2v) เท่านั้น** — Max/Turbo ไม่มีสวิตช์นี้
- งานตัดต่อ/ซับ: ใช้ `ffmpeg` + `subtitle_format` + `merge_videos` (ฟรี ไม่กินเครดิตเจน)
