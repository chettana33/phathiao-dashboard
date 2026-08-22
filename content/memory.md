---
title: "พี่เจ_MEMORY — บันทึกทบทวนระบบ (กันลืม)"
type: "note"
tags: ["memory", "recap", "พี่เจ", "okf"]
status: "active"
created: 2026-08-22T13:02:00+07:00
last_updated: 2026-08-22T14:30:00+07:00
version: "1.0"
owner: "พี่เจ & พาเที่ยว"
source_of_truth: "Obsidian & GitHub"
---
# 🧠 พี่เจ_MEMORY — ทบทวนว่าระบบเราทำอะไรไปแล้วบ้าง

โน้ตนี้เขียนไว้ให้พี่เจอ่านกันลืม — อัปเดตเมื่อระบบเปลี่ยน ไม่ใช่บันทึกรายวัน

## ระบบของเรา

| ระบบ | บทบาท | มาตรฐาน/รายละเอียด |
|---|---|---|
| Obsidian Vault (`H:\My Drive\พาเที่ยว\Obsidian-Vault`) | สมองที่ 2 ให้ AI ทุกค่าย — เก็บความรู้, SOP, checkpoint | LLM Wiki / OKF + timestamp ทุกไฟล์ |
| GitHub (`chettana33`) | Source of Truth — โปรเจกต์ 15 ตัว | commit/push ผ่าน checkpoint script กลาง |
| Google Drive (`H:\My Drive`) | ข้อมูลดิบ: Excel, Docs, Sheets, ภาพ | แผนที่ 33 โฟลเดอร์ใน MASTER_INDEX_DRIVE |
| DSH (DeepSeek Harness) | Execution — รันงาน AI | ใช้ Serena slim + Thin MCP |
| Discord (#ai-activity-log) | Audit log กลางทุกค่าย | START / PROGRESS / ALERT / BLOCKED / DONE |

## งาน Automation ที่มีแล้ว

| ระบบ                                 | ทำอะไร                                                                                                                                   | ตำแหน่ง/หมายเหตุ                                                                                     |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| สคริปต์กลาง `checkpoint_workflow.py` | pull โปรเจกต์, ทับ `CHECKPOINT_LATEST.md`, commit+push, Discord START/DONE, sync Google Docs 6 ฉบับ, `--convert` Quick Capture จากมือถือ | `D:\GitHub\phathiao-knowledge-brain\tools\` — ใช้ตัวเดียว ห้ามสร้างซ้ำ                               |
| `monitor_cgman.py`                   | จับเมล `rsv@cgman.jp` (จ–ศ ~18:00–19:00 JST) → โหลดใบขอรถ King BUS `MMDD_千栄交通㈱_貸切バス手配依頼書.xlsx` + LINE แจ้ง                               | `C:\Users\chett\.config\opencode\gmail-monitor\`                                                     |
| `taicho_gsheets.py`                  | อ่านใบขอรถ (ทุก tab) → diff vs 台帳 Google Sheets → apply หลังพี่เจอนุมัติ → สร้าง PDF 台帳                                                  | `D:\GitHub\phathiao-knowledge-brain\tools\` — `diff` / `apply` / `pdf`                               |
| `taicho_auto.py`                     | ตรวจใบใหม่ vs 台帳 อัตโนมัติ → diff → apply เอง → LINE สรุป (dedupe 1 ครั้ง/ไฟล์)                                                          | `D:\GitHub\phathiao-knowledge-brain\tools\` — `--dry-run` พรีวิว; state ใน `taicho_auto_state.json`  |
| `daily-news-line-bot`                | LINE bot: ข่าวรายวัน + พยากรณ์อากาศ (กทม. 5 เขต / โตเกียว/โอซาก้า/ฮอกไกโด) + สแกนราคาทัวร์ญี่ปุ่น 6 เจ้า                                 | repo `D:\GitHub\daily-news-line-bot` — Python + LINE API + GitHub Actions                            |
| `MASTER_INDEX_DRIVE`                 | regenerate แผนที่ Drive อัตโนมัติทุกปิดงาน (โฟลเดอร์ใหม่ขึ้นเอง; เติมคำอธิบายที่ `tools/index_descriptions.json`)                        | 0 token — อยู่ในสคริปต์กลาง                                                                          |
| Apps Script                          | งานอัตโนมัติบน Google Workspace (Docs/Sheets/Drive/Gmail) เมื่อพี่เจ้าขอ                                                                 | เก็บใน repo `KIMONO-Land-Operation-Workspace`                                                        |
| Master data pipeline scripts         | verify RAW / extract rates / extract bus / apply ลง MASTER (ใช้กับ PC-001)                                                               | `C:\Users\chett\.Deepseek\` — `verify_round*.py`, `extract_rates.py`, `extract_bus.py`, `apply_*.py` |
| `build_sales_kit.py`                 | สร้าง PDF Sales Kit (PyMuPDF, ฟอนต์ Tahoma รองรับไทย)                                                                                    | ดู `04_Sales_Marketing/Sales_Kit_Thailand_Rep.md`                                                    |

## หลักการที่ตกลงกันแล้ว

- Format กลางของ Vault: tables + nested bullets + wikilinks; tree เฉพาะ static ใน code block; ห้าม branch symbols — ดู `00_SOP_Master/01_AI_Protocols/note-format-standard.md`
- AI ใหม่ต้องอ่าน `AGENTS_3LAYER.md` → `AGENTS.md` ก่อนทำงาน
- Checkpoint กลางไฟล์เดียว: `03_AI_Checkpoints/CHECKPOINT_LATEST.md` — สคริปต์ทับทุกปิดงาน, คงไว้แค่ `## Pending Tasks`

## การ์ดงาน (Project Card)

- แต่ละงานใหญ่มี 1 การ์ด ตอบครบ: ต้นทาง / เชื่อมโยง / สถานะ / ขั้นตอน / ผลลัพธ์ / หน้าตาตอนเสร็จ / เกณฑ์เสร็จ / ทำไมเป็นแบบนี้
- Template: `00_SOP_Master/01_AI_Protocols/project-card-template.md`
- ดัชนีการ์ด: [[03_AI_Checkpoints/PC_INDEX|PC_INDEX]] — PC-001..PC-005

## งานใหญ่ที่ค้าง

- ปรับ .md ทั้ง vault+repo เป็น format ใหม่ (เริ่มโปรเอกสารหลัก)
- Master data: verify RAW 1,323, เติม supplier บัส, rate 13
- B2B Smile Travel, ทดลอง slim, ขยาย Thin MCP 14 repo

## กำหนดการ

- HAI — 26 ธ.ค.
- ma-meow — ม.ค.
