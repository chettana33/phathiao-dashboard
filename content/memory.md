---
title: "พี่เจ_MEMORY — บันทึกทบทวนระบบ (กันลืม)"
type: "note"
tags: ["memory", "recap", "พี่เจ", "okf"]
status: "active"
created: 2026-08-22T13:02:00+07:00
last_updated: 2026-09-06T14:50:00+07:00
version: "1.5"
owner: "พี่เจ & พาเที่ยว"
source_of_truth: "Obsidian & GitHub"
---
# 🧠 พี่เจ_MEMORY — ทบทวนว่าระบบเราทำอะไรไปแล้วบ้าง

> 🔗 **ดัชนีกล่องรับข้อมูล: [[99_Inbox/00_Inbox_INDEX]]** — รายการไฟล์ใน 99_Inbox ทั้งหมด + สถานะ (11 ต.ค. 69)

โน้ตนี้เขียนไว้ให้พี่เจอ่านกันลืม — อัปเดตเมื่อระบบเปลี่ยน ไม่ใช่บันทึกรายวัน

## ระบบของเรา

| ระบบ | บทบาท | มาตรฐาน/รายละเอียด |
|---|---|---|
| Obsidian Vault (`H:\My Drive\พาเที่ยว\Obsidian-Vault`) | สมองที่ 2 ให้ AI ทุกค่าย — เก็บความรู้, SOP, checkpoint | LLM Wiki / OKF + timestamp ทุกไฟล์ |
| GitHub (`chettana33`) | Source of Truth — โปรเจกต์ 18 ตัว (อ่านจาก projects.json) | commit/push ผ่าน checkpoint script กลาง |
| Google Drive (`H:\My Drive`) | ข้อมูลดิบ: Excel, Docs, Sheets, ภาพ | แผนที่ 33 โฟลเดอร์ใน MASTER_INDEX_DRIVE |
| DSH (DeepSeek Harness) | Execution — รันงาน AI | ใช้ Serena slim + Thin MCP |
| Discord (#ai-activity-log) | Audit log กลางทุกค่าย | START / PROGRESS / ALERT / BLOCKED / DONE |

## เครื่องมือผลิตคอนเทนต์ — MiniMax Design (เพิ่ม 11 ก.ย. 69 · พี่เจ approve)

> รายละเอียดเต็ม: `04_Sales_Marketing/MiniMax_Skills_Plan_2026-09-11.md` · https://chettana33.github.io/phathiao-dashboard/#minimax

| เรื่อง | สรุป |
|---|---|
| บัญชี + แผน | Chettana Suparatarpa · Media Plan Starter · เติม $10.5 (11 ก.ย. 69) · H3 30 วิ ≈ 2,100 เครดิต |
| Skills ที่จะใช้ | `koc-video` (talking head/POV) · `voice-clone` · `education-studio` (คลิปยาว YouTube) · `paper-collage-explainer-generator` · `brand-promo-video-generator` · `music-3.0` + `lyrics_generation` (BGM ประจำช่อง) · `clip-export` (CapCut) |
| Plugin ในตัวแอป | **Video Editor** (ตัด/ลบเงียบ/ซับอัตโนมัติ — ทดสอบคืน 11 ก.ย.) · Director Stage (3D storyboard) · ComfyUI (เก็บไว้) |
| Connector | แอปยังไม่มี Connector API (404) — ที่ควรดึง: MCP ต่อแอป MiniMax · `linkdigest-mcp` · `redfox-community-dsh` · `last30days-skill-cn` · `riffkit/skill` · MCP โพสต์ YouTube/TikTok/FB (ยังไม่มี ต้องสร้างเอง) |
| แผนช่องทาง | โครงเดียว 3 ตัด: TikTok 20-35 วิ · YouTube Shorts (มีซับ) · YouTube ยาว 60-180 วิ · Facebook 60-120 วิ · ichinotour B2B hero 15-45 วิ |
| ฝั่งพาเที่ยว (V4.1) | เพิ่ม MCP ต่อแอป MiniMax เข้า DSH · Google Workspace MCP เข้า DSH · `linkdigest` MCP · Skill "Phathiao Ingest" |

## งาน Automation ที่มีแล้ว

| ระบบ                                 | ทำอะไร                                                                                                                                   | ตำแหน่ง/หมายเหตุ                                                                                     |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| สคริปต์กลาง `checkpoint_workflow.py` | pull โปรเจกต์, ทับ `CHECKPOINT_LATEST.md`, commit+push, Discord START/DONE, `--convert` Quick Capture จากมือถือ (sync Google Docs ยุบแล้ว 6 ก.ย. 69 — lessons #95) | `D:\GitHub\phathiao-knowledge-brain\tools\` — ใช้ตัวเดียว ห้ามสร้างซ้ำ                               |
| `monitor_cgman.py`                   | จับเมล `⟨อีเมล⟩` (จ–ศ ~18:00–19:00 JST) → โหลดใบขอรถ King BUS `MMDD_千栄交通㈱_貸切バス手配依頼書.xlsx` + LINE แจ้ง                               | `C:\Users\chett\.config\opencode\gmail-monitor\`                                                     |
| `taicho_gsheets.py`                  | อ่านใบขอรถ (ทุก tab) → diff vs 台帳 Google Sheets → apply หลังพี่เจอนุมัติ → สร้าง PDF 台帳                                                  | `D:\GitHub\senei-kotsu-invoice\tools\` — `diff` / `apply` / `pdf`                               |
| `taicho_auto.py`                     | ตรวจใบใหม่ vs 台帳 อัตโนมัติ → diff → apply เอง → LINE สรุป (dedupe 1 ครั้ง/ไฟล์)                                                          | `D:\GitHub\senei-kotsu-invoice\tools\` — `--dry-run` พรีวิว; state ใน `taicho_auto_state.json`  |
| `daily-news-line-bot`                | LINE bot: ข่าวรายวัน + พยากรณ์อากาศ (กทม. 5 เขต / โตเกียว/โอซาก้า/ฮอกไกโด) + สแกนราคาทัวร์ญี่ปุ่น 6 เจ้า                                 | repo `D:\GitHub\daily-news-line-bot` — Python + LINE API + GitHub Actions                            |
| `MASTER_INDEX_DRIVE`                 | regenerate แผนที่ Drive อัตโนมัติทุกปิดงาน (โฟลเดอร์ใหม่ขึ้นเอง; เติมคำอธิบายที่ `tools/index_descriptions.json`)                        | 0 token — อยู่ในสคริปต์กลาง                                                                          |
| Apps Script                          | งานอัตโนมัติบน Google Workspace (Docs/Sheets/Drive/Gmail) เมื่อพี่เจขอ                                                                 | เก็บใน repo `KIMONO-Land-Operation-Workspace`                                                        |
| Master data pipeline scripts         | verify RAW / extract rates / extract bus / apply ลง MASTER (ใช้กับ PC-001)                                                               | `C:\Users\chett\.Deepseek\` — `verify_round*.py`, `extract_rates.py`, `extract_bus.py`, `apply_*.py` |
| `build_sales_kit.py`                 | สร้าง PDF Sales Kit (PyMuPDF, ฟอนต์ Tahoma รองรับไทย)                                                                                    | ดู `04_Sales_Marketing/Sales_Kit_Thailand_Rep.md`                                                    |
| `tour_price_tracker.py`              | เก็บประวัติราคาทัวร์ญี่ปุ่น 8 เจ้า รายวัน + เทรนด์ขึ้น/ลง + โปรเด็ด (ต่อจาก scraper)                                                       | repo `daily-news-line-bot` — GH Actions รันหลัง scraper (จ-ศ), history commit กลับ `data/tour_price_history.json` (เก็บ 30 รอบ) |

## DSH Tooling — สายพาน AI ops จบในเครื่องเดียว (เพิ่ม 26 ส.ค. 2569)

| ระบบ | ทำอะไร | ตำแหน่ง/หมายเหตุ |
|---|---|---|
| ModLens vision | อ่านภาพใน session DSH เอง (OCR + layout + semantics) — ใบขอรถ King BUS, สไลด์คอร์ส Meawbin, กราฟ MT5 ไม่ต้องส่ง Gemini Browser | plugin `@liustack/⟨อีเมล⟩` (profile web); engine gemini-api, model `gemini-3.6-flash`; config `~/.modlens/config.json`; tool `modlens_read_image`; ทดสอบภาพจริงผ่าน 3/3 (26 ส.ค. 69) |
| Agent presets (6 ตัว) | บทบาท AI สำเร็จรูป: standard-zh / minimal-zh / researcher / writer / reviewer / architect — เลือกตอนเปิด session ใหม่ | `~/.dsh/.agent-presets/<ชื่อ>/` (source `~/.dsh/awesome-dsh-presets/presets/`); รายละเอียด: `00_SOP_Master/01_AI_Protocols/dsh-agent-presets.md` |
| architect preset | ออกแบบ decision-complete ก่อนเขียนโค้ด — dev implement ได้ไม่ต้องเดา design | ทดสอบผ่าน 25 ส.ค. 69 (PC-007 P3 design) |
| reviewer preset | รีวิวโค้ดก่อน commit/push — หลักฐานจริง + severity Critical/Major/Minor/Nit, ข้อไม่แน่ใจแยกชัด | ทดสอบผ่าน 26 ส.ค. 69 — รีวิว checkpoint_workflow.py (889 บรรทัด) เจอ 6 Major + 7 Minor + 7 Nit |
| repeat-tool-reminder | กัน agent วนเรียก tool ซ้ำ (spin detection) — เตือน advisory thresholds [3,5,8], ไม่บล็อก | mount ครบ 6 presets 26 ส.ค. 69; DSH base มีอยู่แล้ว (`dsh-base/cordis.patch.yml`) |
| MCP Playwright (browser automation) | ควบคุมเบราว์เซอร์จริงใน session — navigate / click / type / screenshot / รัน JS / login flow; ใช้ QA Ichinotour, สแกนราคาทัวร์, ตรวจเว็บ | `@playwright/mcp` 0.0.79 → `~/.dsh/mcp/playwright-mcp/`; register `profiles/web/cordis.patch.yml` (`mcp-playwright`, headless); ทดสอบผ่าน 26 ส.ค. 69 (24 tools); ห้ามคุม Chrome ตัวหลัก + ปุ่มสำคัญต้องพี่เจอนุมัติ — ดู `00_SOP_Master/01_AI_Protocols/dsh-browser-automation.md` |
| Cursor integration | Cursor = IDE/หน้าต่างดู diff + review + แก้ด้วยมือ (Hobby ฟรี); ตัวหลักยังเป็น DSH; Gemini ใช้ผ่าน API ตรง (ModLens) — Cursor เปลี่ยนโมเดลเป็น Gemini ไม่ได้จริง | `.cursorrules` + `.cursor/mcp.json` (playwright) ใน `ichinotour-quotation` push `358a1bd`; ดู `00_SOP_Master/01_AI_Protocols/dsh-cursor-integration.md` |
| Vault Semantic Search (RAG) | ค้นความรู้ใน Vault แบบ semantic — ถาม "กติกา/งานค้างเรื่อง X" → ได้ไฟล์ที่ตรงสุด (embedding gemini-embedding-001) — ลด token อ่านไฟล์ทั้งโฟลเดอร์ | MCP server `~/.dsh/mcp/vault-search/` + register `mcp-vault-search`; index 99 ไฟล์ (reindex 6 ก.ย. 69 lessons #88); tool `mcp__vault__vault_search`; ดู `00_SOP_Master/01_AI_Protocols/dsh-vault-search.md` |
| lessons-learned #21-24 | กับดัก DSH: pnpm/npm-cache EPERM (sandbox), validator presets พังบน Windows, gemini model เปลี่ยน, งานค้างต้องมี marker ใน summary | `00_SOP_Master/01_AI_Protocols/lessons-learned.md` |

**งานค้าง DSH tooling (6 ก.ย. 69):** portfolio-analyst preset = draft v0.1 สร้างแล้ว (รอ wiring สคริปต์โบรก read-only 4 ตัว) · dsh-routed-subagent (Master Data verify) · voice-input plugin = เก็บ source ไม่ mount (BOM แก้แล้ว 6 ก.ย. — รอ Test หลัง restart ครั้งหน้า) · MCP กู้ทั้งหมดรอ restart (playwright/vault-search/firebase recipe พร้อม) · ✅ เสร็จก่อนหน้า: repeat-tool-reminder mount 6 presets (26 ส.ค.), ModLens 3/3, browser automation MCP

## หลักการที่ตกลงกันแล้ว

- Format กลางของ Vault: tables + nested bullets + wikilinks; tree เฉพาะ static ใน code block; ห้าม branch symbols — ดู `00_SOP_Master/01_AI_Protocols/note-format-standard.md`
- AI ใหม่ต้องอ่าน `AGENTS_3LAYER.md` → `AGENTS.md` ก่อนทำงาน
- Checkpoint กลางไฟล์เดียว: `03_AI_Checkpoints/CHECKPOINT_LATEST.md` — สคริปต์ทับทุกปิดงาน, คงไว้แค่ `## Pending Tasks`

## การ์ดงาน (Project Card)

- แต่ละงานใหญ่มี 1 การ์ด ตอบครบ: ต้นทาง / เชื่อมโยง / สถานะ / ขั้นตอน / ผลลัพธ์ / หน้าตาตอนเสร็จ / เกณฑ์เสร็จ / ทำไมเป็นแบบนี้
- Template: `00_SOP_Master/01_AI_Protocols/project-card-template.md`
- ดัชนีการ์ด: [[03_AI_Checkpoints/PC_INDEX|PC_INDEX]] — PC-001..PC-011 (PC-011 = DSH Tooling & Knowledge Ops เพิ่ม 7 ก.ย. 69 — เจ้าของ B20/B21/corpus/cloud scheduler); PC-001 master 855 ใช้จริง · PC-006 Meawbin 25/56 · PC-009 Gochisou pilot v3 reject รอคลิปใหม่ · PC-010 รอ data JSON

## งานใหญ่ที่ค้าง

- ปรับ .md ทั้ง vault+repo เป็น format ใหม่ (เริ่มโปรเอกสารหลัก)
- Master data: verify RAW 1,323, เติม supplier บัส, rate 13
- B2B Smile Travel (PC-003)
- ~~ทดลอง slim~~ / ~~ขยาย Thin MCP 14 repo~~ — PC-004 Done (slim ใช้อยู่) + PC-005 Done (เลข "14/15 repo" = projects.json ยุค 22 ส.ค. — ปัจจุบัน 18)

## กำหนดการ

- HAI — 26 ธ.ค.
- ma-meow — ม.ค.
