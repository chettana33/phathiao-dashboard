#!/usr/bin/env python3
"""Build phathiao-dashboard: content/*.md + checkpoint -> docs/index.html"""
import datetime
import os
import re
import html
from pathlib import Path

# Bangkok time — runner (GitHub Actions) เป็น UTC, ใช้ +07 fixed (ไม่พึ่ง tzdata)
BKK = datetime.timezone(datetime.timedelta(hours=7))

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT = ROOT / "docs"

NAV_ITEMS = [
    ("overview", "ภาพรวม"),
    ("workmap", "แผนที่งาน"),
    ("status", "สถานะงาน"),
    ("systemmap", "System Map"),
    ("minimax", "MiniMax Studio"),
    ("characters", "ตัวละคร"),
    ("checkpoint", "Checkpoint"),
    ("memory", "MEMORY"),
    ("roadmap", "ลำดับถัดไป"),
    ("ideas", "กระดานไอเดีย"),
]

STATUS_TAG = {
    "done": ("tag good", "✅ done"),
    "in_progress": ("tag info", "🔵 in_progress"),
    "blocked": ("tag bad", "⛔ blocked"),
    "pending": ("tag muted", "⏳ pending"),
}

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    # รูป: ต้องมาก่อนกฎลิงก์ ไม่งั้น ![alt](src) จะถูกตัดเหลือ <a> (เพิ่ม 7 ต.ค. 69)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" loading="lazy">', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text

def parse_md(text):
    blocks = []
    lines = text.split("\n")
    i = 0
    in_code = False
    code_raw = False  # ```html = HTML ดิบ (ใช้ทำหน้า visual เช่น แผนที่งาน) — 14 ต.ค. 69
    code_buf = []
    in_list = False
    list_buf = []
    in_table = False
    table_buf = []

    def flush_list():
        nonlocal in_list, list_buf
        if in_list:
            items = "".join(f"<li>{inline(l[2:].strip())}</li>" for l in list_buf if l.strip())
            blocks.append(f"<ul>{items}</ul>")
            list_buf = []
            in_list = False

    def flush_table():
        nonlocal in_table, table_buf
        if in_table and len(table_buf) >= 2:
            header = [c.strip() for c in table_buf[0].strip("|").split("|")]
            rows = [[c.strip() for c in r.strip("|").split("|")] for r in table_buf[2:]]
            th = "".join(f"<th>{inline(h)}</th>" for h in header)
            trs = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>"
                for row in rows
            )
            blocks.append(f'<div class="table-wrap"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
        table_buf = []
        in_table = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                if code_raw:
                    # fenced ```html = ปล่อย HTML ดิบ (ไม่ escape) — สำหรับหน้าที่ต้องมีกล่อง/ลูกศร/อนิเมชัน
                    blocks.append("\n".join(code_buf))
                else:
                    blocks.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")
                code_buf = []
                in_code = False
                code_raw = False
            else:
                flush_list(); flush_table()
                in_code = True
                code_raw = stripped[3:].strip().lower() == "html"
            i += 1
            continue

        if in_code:
            code_buf.append(line if code_raw else html.escape(line))
            i += 1
            continue

        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r'^\s*\|?[\s:|-]+\|?\s*$', lines[i+1]):
            flush_list()
            if not in_table:
                in_table = True
            table_buf.append(line)
            i += 1
            continue

        if in_table:
            if stripped.startswith("|"):
                table_buf.append(line)
                i += 1
                continue
            else:
                flush_table()

        if not stripped:
            flush_list(); flush_table()
            i += 1
            continue

        if stripped.startswith("### "):
            flush_list(); flush_table()
            blocks.append(f"<h3>{inline(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            flush_list(); flush_table()
            blocks.append(f"<h2>{inline(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            flush_list(); flush_table()
            blocks.append(f"<h1>{inline(stripped[2:])}</h1>")
        elif stripped.startswith("> "):
            flush_list(); flush_table()
            blocks.append(f'<blockquote>{inline(stripped[2:])}</blockquote>')
        elif stripped == "---":
            flush_list(); flush_table()
            blocks.append("<hr>")
        elif re.match(r'^\s*[-*] ', stripped):
            flush_table()
            if not in_list:
                in_list = True
            list_buf.append(stripped)
        elif re.match(r'^\s*\d+\. ', stripped):
            flush_list(); flush_table()
            blocks.append(f"<p class=\"num\">{inline(re.sub(r'^\s*\d+\. ', '', stripped))}</p>")
        else:
            flush_list(); flush_table()
            blocks.append(f"<p>{inline(stripped)}</p>")
        i += 1

    flush_list(); flush_table()
    if in_code:
        blocks.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")
    return "\n".join(blocks)

def status_chips(body):
    """system-map section: แปลงสถานะในตารางเป็น chips สี (หลัง parse)"""
    for status, (cls, label) in STATUS_TAG.items():
        body = re.sub(
            r"<td>" + status + r"</td>",
            f'<td><span class="{cls}">{label}</span></td>',
            body,
        )
    return body


def build():
    OUT.mkdir(exist_ok=True)
    nav = "".join(
        f'<a href="#{key}" class="nav-link" data-target="{key}">{label}</a>'
        for key, label in NAV_ITEMS
    )

    sections = []
    ts_by_key = {}
    for key, label in NAV_ITEMS:
        src = CONTENT / f"{key}.md"
        if not src.exists():
            continue
        raw = src.read_text(encoding="utf-8")
        # capture last_updated from YAML frontmatter of every section (26 ส.ค. 69), then strip it for clean display
        # 29 ส.ค. 69: badge ใช้เวลา build จริง (อัตโนมัติ) — ไม่ต้องแก้ last_updated ในไฟล์
        if raw.startswith("---"):
            m = re.match(r'^---\n(.*?)\n---\n', raw, re.S)
            if m:
                fm = m.group(1)
                ts_by_key[key] = datetime.datetime.now(BKK).strftime('%Y-%m-%dT%H:%M:%S+07:00')
                if key == "checkpoint":
                    # remove duplicate timestamp from **Status:** line (badge shows it)
                    raw = re.sub(r'(\*\*Status:\*\*[^\n]*?)\s*—\s*อัปเดตล่าสุด[^\n]*', r'\1', raw)
                raw = raw[m.end():]
        body = parse_md(raw)
        if key == "systemmap":
            body = status_chips(body)
        if key in ts_by_key:
            body = f'<div class="tag tag-good">📅 อัปเดตล่าสุด: {ts_by_key[key]}</div>\n' + body
        if key == "ideas":
            body += """
<div class="notes-box">
  <h3>📝 พิมพ์ไอเดีย/โน้ต</h3>
  <input type="text" id="note-name" placeholder="ชื่อคุณ (ไม่บังคับ)" maxlength="100">
  <textarea id="note-text" placeholder="พิมพ์ไอเดียตรงนี้... (สูงสุด 2000 ตัวอักษร)" maxlength="2000" rows="3"></textarea>
  <div class="note-actions">
    <button class="btn" id="note-submit">บันทึกโน้ต</button>
    <span id="note-msg" class="muted"></span>
  </div>
</div>
<div id="notes-list" class="notes-list"><p class="muted">กำลังโหลดโน้ต...</p></div>
"""
        sections.append(f'<section id="{key}" class="section">{body}</section>')

    html_doc = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>พาเที่ยว Dashboard — ภาพรวมธุรกิจ Ichino Tour</title>
<meta name="theme-color" content="#0f172a">
<meta name="description" content="กระดานงาน พี่เจ &amp; พาเที่ยว — แผนที่งาน สถานะ และความคืบหน้า">
<link rel="manifest" href="./manifest.webmanifest">
<link rel="apple-touch-icon" href="./apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="พาเที่ยว">
<script>
  // โหมดสว่าง/มืด + ขนาดตัวอักษร: อ่านค่าที่จำไว้ก่อนวาดหน้า (กันหน้าสว่างวาบ) — เฟส 1, 14 ต.ค. 69
  (function () {{
    try {{
      var t = localStorage.getItem('pd_theme');
      if (t === 'light') document.documentElement.classList.add('light');
      var f = localStorage.getItem('pd_font');
      if (f) document.documentElement.style.fontSize = f + 'px';
    }} catch (e) {{}}
  }})();
</script>
<style>
:root {{
  --bg:#0f172a; --card:#1e293b; --card2:#273449; --line:#334155;
  --text:#e2e8f0; --muted:#94a3b8; --accent:#38bdf8; --good:#4ade80; --warn:#facc15; --bad:#f87171;
  --accent2:#818cf8;
}}
* {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ background:var(--bg); color:var(--text); font-family:'Segoe UI','Noto Sans Thai',Tahoma,sans-serif; line-height:1.6; }}
header {{ position:sticky; top:0; background:rgba(15,23,42,.92); backdrop-filter:blur(8px); border-bottom:1px solid var(--line); padding:12px 20px; z-index:10; }}
.brand {{ display:flex; align-items:center; gap:12px; flex-wrap:wrap; }}
.brand h1 {{ font-size:18px; color:var(--accent); }}
.brand .sub {{ color:var(--muted); font-size:12px; }}
nav {{ display:flex; gap:8px; margin-top:10px; flex-wrap:wrap; }}
.nav-link {{ color:var(--muted); text-decoration:none; font-size:13px; padding:5px 12px; border:1px solid var(--line); border-radius:20px; }}
.nav-link:hover, .nav-link.active {{ color:var(--bg); background:var(--accent); border-color:var(--accent); }}
.brand-row {{ display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; }}
.tools {{ display:flex; gap:6px; align-items:center; }}
.tool-btn {{ border:1px solid var(--line); background:var(--card2); color:var(--text); font-family:inherit;
  font-size:13px; padding:5px 10px; border-radius:9px; cursor:pointer; line-height:1.2; }}
.tool-btn:hover {{ border-color:var(--accent); color:var(--accent); }}
.section {{ animation:secIn .22s ease-out; }}
@keyframes secIn {{ from {{ opacity:0; transform:translateY(6px); }} to {{ opacity:1; transform:none; }} }}
#to-top {{ position:fixed; right:16px; bottom:18px; z-index:20; display:none; width:46px; height:46px;
  border-radius:50%; border:1px solid var(--line); background:var(--card2); color:var(--accent);
  font-size:19px; cursor:pointer; box-shadow:0 8px 20px rgba(0,0,0,.35); }}
#to-top.show {{ display:block; animation:secIn .2s ease-out; }}
@media (prefers-reduced-motion: reduce) {{ .section, #to-top.show {{ animation:none; }} }}
/* โหมดสว่าง */
html.light {{ --bg:#f6f7fb; --card:#ffffff; --card2:#eef2f7; --line:#d7dee8;
  --text:#16202f; --muted:#5b6b80; --accent:#0b74c4; --good:#128a4b; --warn:#a9760a; --bad:#c0392b; --accent2:#4f46e5; }}
html.light body {{ background:var(--bg); color:var(--text); }}
html.light header {{ background:rgba(246,247,251,.92); }}
html.light strong {{ color:#0b1220; }}
html.light .tag.good {{ background:rgba(18,138,75,.12); }}
html.light .tag.info {{ background:rgba(11,116,196,.12); }}
html.light .tag.warn {{ background:rgba(169,118,10,.14); }}
html.light .wm {{ background:linear-gradient(180deg,#ffffff,#f8fafc); }}
html.light .wm-phase {{ background:#f4f7fb; }}
html.light .wm-goal, html.light .wm-card, html.light .wm-step, html.light .wm-tile {{ background:#fff; }}
html.light .wm-tile-name {{ color:#16202f; }}
html.light .wm-progress .wm-bar {{ background:#e6ebf3; }}
html.light .wm-pnum {{ color:#fff; }}
html.light pre {{ background:#eef2f7; }}
html.light .wm-glow {{ opacity:.5; }}
main {{ max-width:1000px; margin:0 auto; padding:24px 16px 80px; }}
.section {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:24px; margin-bottom:24px; }}
h1 {{ font-size:22px; color:var(--accent); margin-bottom:12px; }}
h2 {{ font-size:18px; color:var(--accent); margin:20px 0 10px; padding-bottom:6px; border-bottom:1px solid var(--line); }}
h3 {{ font-size:15px; color:var(--text); margin:14px 0 6px; }}
p {{ margin:6px 0; color:var(--text); }}
img {{ max-width:100%; height:auto; display:block; margin:10px 0; border:1px solid var(--line); border-radius:12px; background:#fff; }}
p.num {{ margin:6px 0 6px 18px; }}
ul {{ margin:6px 0 6px 20px; }}
li {{ margin:3px 0; }}
strong {{ color:#fff; }}
a {{ color:var(--accent); text-decoration:none; }}
a:hover {{ text-decoration:underline; }}
code {{ background:var(--card2); padding:1px 6px; border-radius:5px; font-size:13px; }}
pre {{ background:#0b1220; border:1px solid var(--line); border-radius:10px; padding:14px; overflow-x:auto; margin:10px 0; }}
pre code {{ background:none; padding:0; }}
blockquote {{ border-left:3px solid var(--warn); background:var(--card2); padding:8px 14px; border-radius:0 10px 10px 0; margin:10px 0; color:var(--muted); }}
hr {{ border:0; border-top:1px solid var(--line); margin:16px 0; }}
.table-wrap {{ overflow-x:auto; margin:10px 0; }}
table {{ border-collapse:collapse; width:100%; font-size:13.5px; }}
th {{ background:var(--card2); color:var(--accent); text-align:left; padding:8px 10px; border:1px solid var(--line); white-space:nowrap; }}
td {{ padding:7px 10px; border:1px solid var(--line); vertical-align:top; }}
tr:nth-child(even) td {{ background:rgba(255,255,255,.02); }}
.good {{ color:var(--good); font-weight:700; }}
.warn {{ color:var(--warn); font-weight:700; }}
.bad {{ color:var(--bad); font-weight:700; }}
.tag {{ display:inline-block; font-size:11px; padding:2px 9px; border-radius:12px; margin-right:4px; }}
.tag.good {{ background:rgba(74,222,128,.15); color:var(--good); }}
.tag.warn {{ background:rgba(250,204,21,.15); color:var(--warn); }}
.tag.bad {{ background:rgba(248,113,113,.15); color:var(--bad); }}
.tag.muted {{ background:var(--card2); color:var(--muted); }}
.tag.info {{ background:rgba(56,189,248,.15); color:var(--accent); }}
.btn {{ border:0; border-radius:9px; padding:9px 16px; font-weight:700; cursor:pointer; background:var(--accent); color:#0b1220; font-size:13px; }}
.btn:hover {{ opacity:.9; }}
.muted {{ color:var(--muted); font-size:13px; }}
.notes-box {{ background:var(--card2); border:1px solid var(--line); border-radius:12px; padding:14px; margin:14px 0; }}
.notes-box input, .notes-box textarea {{ width:100%; padding:9px 10px; border:1px solid var(--line); border-radius:8px; font-family:inherit; font-size:14px; background:#0f172a; color:var(--text); margin:4px 0; }}
.note-actions {{ display:flex; align-items:center; gap:12px; margin-top:8px; }}
.notes-list {{ margin-top:14px; }}
.note-card {{ background:var(--card2); border:1px solid var(--line); border-radius:10px; padding:12px 14px; margin:8px 0; }}
.note-card .note-meta {{ color:var(--muted); font-size:11px; margin-top:6px; }}
footer {{ text-align:center; color:var(--muted); font-size:12px; padding:20px; border-top:1px solid var(--line); }}
/* ---- แผนที่งาน: ช่องเลือกงาน (tiles) + รายละเอียดทีละงาน (14 ต.ค. 69) ---- */
.wm-toolbar {{ display:flex; justify-content:space-between; align-items:center; gap:12px; flex-wrap:wrap; margin:6px 0 12px; }}
.wm-toolbar-title {{ font-size:15px; color:var(--muted); }}
.wm-toolbar-title b {{ color:var(--accent); }}
.wm-back {{ border:1px solid var(--line); background:var(--card2); color:var(--accent); font-family:inherit;
  font-size:13px; font-weight:700; padding:8px 14px; border-radius:10px; cursor:pointer; }}
.wm-back:hover {{ background:var(--accent); color:#0b1220; }}
.wm-tools {{ display:flex; gap:8px; align-items:center; flex-wrap:wrap; }}
.wm-search {{ font-family:inherit; font-size:14px; color:var(--text); background:var(--card2);
  border:1px solid var(--line); border-radius:10px; padding:8px 12px; min-width:240px; }}
.wm-search:focus {{ outline:none; border-color:var(--accent); box-shadow:0 0 0 3px rgba(56,189,248,.15); }}
.wm-last {{ font-size:13.5px; color:var(--muted); margin:2px 0 12px; display:flex; align-items:center; gap:8px; flex-wrap:wrap; }}
.wm-last-btn {{ font-family:inherit; font-size:13.5px; cursor:pointer; border:1px dashed var(--line);
  background:transparent; color:var(--accent); border-radius:999px; padding:4px 12px; }}
.wm-last-btn:hover {{ border-style:solid; border-color:var(--accent); }}
.wm-live {{ display:flex; align-items:center; gap:9px; font-size:13px; color:var(--muted);
  background:rgba(15,23,42,.55); border:1px solid var(--line); border-radius:10px; padding:7px 12px; margin:0 0 12px; }}
.wm-live-dot {{ width:9px; height:9px; border-radius:50%; background:#475569; flex:0 0 auto; }}
.wm-live.is-fresh .wm-live-dot {{ background:var(--good); animation:wmLive 2.4s ease-in-out infinite; }}
.wm-live.is-stale .wm-live-dot {{ background:var(--warn); }}
@keyframes wmLive {{ 0%,100% {{ box-shadow:0 0 0 0 rgba(74,222,128,.5); }} 50% {{ box-shadow:0 0 0 6px rgba(74,222,128,0); }} }}
html.light .wm-live {{ background:#f4f7fb; }}
@media (prefers-reduced-motion: reduce) {{ .wm-live.is-fresh .wm-live-dot {{ animation:none; }} }}
.wm-notes {{ margin-top:16px; background:rgba(15,23,42,.55); border:1px solid var(--line); border-radius:14px; padding:14px 16px; }}
.wm-notes-head {{ font-size:14.5px; color:var(--accent); font-weight:700; margin-bottom:9px; }}
.wm-notes-input textarea {{ width:100%; font-family:inherit; font-size:14.5px; color:var(--text); background:var(--card);
  border:1px solid var(--line); border-radius:10px; padding:10px 12px; resize:vertical; }}
.wm-notes-input textarea:focus {{ outline:none; border-color:var(--accent); box-shadow:0 0 0 3px rgba(56,189,248,.15); }}
.wm-notes-actions {{ display:flex; align-items:center; gap:10px; margin-top:8px; flex-wrap:wrap; }}
.wm-note-save {{ border:0; border-radius:9px; padding:8px 16px; font-family:inherit; font-size:13.5px; font-weight:700;
  cursor:pointer; background:var(--accent); color:#0b1220; }}
.wm-note-save:hover {{ opacity:.9; }}
.wm-note-msg {{ font-size:13px; color:var(--muted); }}
.wm-notes-list {{ margin-top:10px; display:flex; flex-direction:column; gap:8px; }}
.wm-note {{ background:var(--card); border:1px solid var(--line); border-left:3px solid var(--accent);
  border-radius:10px; padding:9px 12px; font-size:14px; }}
.wm-note-meta {{ color:var(--muted); font-size:11.5px; margin-top:4px; }}
html.light .wm-notes {{ background:#f4f7fb; }}
html.light .wm-note {{ background:#fff; }}
html.light .wm-notes-input textarea {{ background:#fff; }}
.wm-group-title {{ font-size:13px; color:var(--muted); margin:14px 0 8px; letter-spacing:.4px; }}
.wm-tiles {{ display:grid; grid-template-columns:repeat(auto-fill, minmax(250px, 1fr)); gap:12px; margin-bottom:8px; }}
.wm-tile {{ display:flex; flex-direction:column; gap:5px; text-align:left; cursor:pointer; font-family:inherit;
  background:linear-gradient(180deg, rgba(39,52,73,.9), rgba(30,41,59,.75)); color:var(--text);
  border:1px solid var(--line); border-left:4px solid var(--accent); border-radius:14px;
  padding:13px 15px; transition:transform .18s, box-shadow .18s, border-color .18s; }}
.wm-tile:hover {{ transform:translateY(-3px); box-shadow:0 12px 26px rgba(0,0,0,.32); border-left-color:var(--good); }}
.wm-tile.is-active {{ border-left-color:var(--good); box-shadow:0 0 0 2px rgba(74,222,128,.35); }}
.wm-tile-code {{ font-size:11.5px; letter-spacing:1.2px; color:var(--accent); }}
.wm-tile-name {{ font-size:15.5px; font-weight:700; color:#fff; line-height:1.35; }}
.wm-tile-meta {{ font-size:12.5px; color:var(--text); }}
.wm-tile-next {{ font-size:12.5px; color:var(--muted); border-top:1px dashed var(--line); padding-top:6px; margin-top:2px; }}
.wm-tile.is-empty {{ cursor:default; opacity:.5; border-left-color:#475569; }}
.wm-tile.is-empty:hover {{ transform:none; box-shadow:none; border-left-color:#475569; }}
.wm-detail[hidden] {{ display:none !important; }}
/* สำคัญ: element ที่มี display:grid/flex จาก CSS จะไม่สนใจ attribute hidden ⇒ ต้องสั่ง display:none เอง (14 ต.ค. 69) */
.wm-list[hidden], .wm-group-title[hidden], .wm-tiles[hidden], .wm-tile[hidden] {{ display:none !important; }}
.wm-detail {{ animation:wmIn .32s ease-out; }}
@keyframes wmIn {{ from {{ opacity:0; transform:translateY(10px); }} to {{ opacity:1; transform:none; }} }}
@media (prefers-reduced-motion: reduce) {{ .wm-detail {{ animation:none; }} }}

/* ---- แผนที่งาน (workmap) v2 — การ์ดเรืองแสง + แถบความคืบหน้า + เส้นทางไหล (14 ต.ค. 69) ---- */
.wm {{ position:relative; overflow:hidden; margin:0 0 26px; padding:20px 22px 18px;
  border:1px solid var(--line); border-radius:18px;
  background:linear-gradient(180deg, rgba(39,52,73,.85), rgba(30,41,59,.65)); }}
.wm::before {{ content:""; position:absolute; top:0; left:0; right:0; height:3px;
  background:linear-gradient(90deg,#38bdf8,#818cf8,#4ade80,#38bdf8); background-size:300% 100%;
  animation:wmSlideBg 7s linear infinite; }}
.wm-glow {{ position:absolute; top:-160px; right:-80px; width:360px; height:360px; pointer-events:none;
  background:radial-gradient(circle, rgba(56,189,248,.18), rgba(129,140,248,.10) 45%, transparent 70%);
  animation:wmFloat 9s ease-in-out infinite; }}
.wm-head {{ position:relative; display:flex; justify-content:space-between; align-items:flex-start; gap:16px;
  flex-wrap:wrap; border-bottom:1px solid var(--line); padding-bottom:14px; margin-bottom:16px; }}
.wm-code {{ font-size:12px; letter-spacing:1.2px; color:var(--muted); text-transform:uppercase; }}
.wm-title {{ font-size:23px; margin-top:4px; }}
.wm-sub {{ display:block; font-size:14px; color:var(--muted); margin-top:4px; }}
.wm-right {{ display:flex; flex-direction:column; align-items:flex-end; gap:9px; }}
.wm-status {{ font-size:12.5px; padding:6px 13px; }}
.wm-progress {{ display:flex; align-items:center; gap:9px; }}
.wm-progress .wm-bar {{ display:block; width:170px; height:9px; border-radius:999px; border:1px solid var(--line);
  background:#0b1220; position:relative; overflow:hidden; }}
.wm-progress .wm-bar::after {{ content:""; position:absolute; inset:0; width:var(--p);
  background:linear-gradient(90deg,#38bdf8,#818cf8,#4ade80); background-size:220% 100%;
  border-radius:999px; animation:wmShimmer 3.2s linear infinite; }}
.wm-progress b {{ font-size:13px; color:var(--accent); }}
.wm-goal {{ position:relative; background:var(--card2); border:1px solid var(--line); border-left:5px solid var(--accent);
  border-radius:12px; padding:14px 17px; font-size:16.5px; }}
.wm-goal-label {{ color:var(--accent); font-weight:700; margin-right:6px; }}
.wm-legend {{ display:flex; gap:16px; flex-wrap:wrap; color:var(--muted); font-size:12.5px; margin:15px 0 8px; }}
.wm-legend span {{ display:inline-flex; align-items:center; gap:6px; }}
.wm-dot {{ width:12px; height:12px; border-radius:4px; display:inline-block; }}
.d-done {{ background:var(--good); }}
.d-doing {{ background:var(--accent); }}
.d-wait {{ background:var(--warn); }}
.d-todo {{ background:#475569; }}
.wm-phase {{ position:relative; background:rgba(15,23,42,.55); border:1px solid var(--line); border-radius:14px;
  padding:14px 16px; margin:14px 0; }}
.wm-phase-title {{ display:flex; align-items:center; gap:9px; font-size:15.5px; color:var(--accent);
  font-weight:700; margin-bottom:12px; }}
.wm-pnum {{ display:inline-flex; width:24px; height:24px; align-items:center; justify-content:center; border-radius:50%;
  font-size:13px; color:#0b1220; background:linear-gradient(135deg,#38bdf8,#818cf8); }}
.wm-steps {{ display:flex; align-items:stretch; flex-wrap:wrap; gap:9px; }}
.wm-step {{ flex:1 1 205px; min-width:180px; border:1px solid var(--line); border-left-width:4px; border-radius:12px;
  padding:12px 14px; font-size:15.5px; line-height:1.5; background:var(--card); transition:transform .18s, box-shadow .18s; }}
.wm-step:hover {{ transform:translateY(-3px); box-shadow:0 10px 24px rgba(0,0,0,.28); }}
.wm-step .wm-n {{ display:block; font-size:12.5px; color:var(--muted); margin-bottom:3px; letter-spacing:.5px; }}
.wm-step em {{ display:block; font-size:13px; color:var(--muted); font-style:normal; margin-top:5px; }}
.wm-step.is-done {{ border-left-color:var(--good); background:rgba(74,222,128,.09); }}
.wm-step.is-doing {{ border-left-color:var(--accent); background:rgba(56,189,248,.11); animation:wmPulse 2.4s ease-in-out infinite; }}
.wm-step.is-wait {{ border-left-color:var(--warn); background:rgba(250,204,21,.09); }}
.wm-step.is-todo {{ border-left-color:#475569; }}
.wm-flow {{ flex:0 0 30px; align-self:center; height:2px; border-radius:2px; position:relative;
  background:linear-gradient(90deg, rgba(56,189,248,.15), rgba(56,189,248,.55), rgba(56,189,248,.15)); }}
.wm-flow::after {{ content:""; position:absolute; top:-2px; left:0; width:6px; height:6px; border-radius:50%;
  background:var(--accent); box-shadow:0 0 8px rgba(56,189,248,.9); animation:wmDot 2.6s linear infinite; }}
@keyframes wmPulse {{
  0%,100% {{ box-shadow:0 0 0 0 rgba(56,189,248,0); }}
  50% {{ box-shadow:0 0 0 6px rgba(56,189,248,.18); }}
}}
@keyframes wmSlideBg {{ 0% {{ background-position:0% 50%; }} 100% {{ background-position:300% 50%; }} }}
@keyframes wmShimmer {{ 0% {{ background-position:0% 50%; }} 100% {{ background-position:220% 50%; }} }}
@keyframes wmFloat {{ 0%,100% {{ transform:translate(0,0) scale(1); }} 50% {{ transform:translate(-24px,18px) scale(1.08); }} }}
@keyframes wmDot {{ 0% {{ left:0; opacity:0; }} 12% {{ opacity:1; }} 88% {{ opacity:1; }} 100% {{ left:calc(100% - 6px); opacity:0; }} }}
.wm-now-title {{ font-size:15.5px; color:var(--accent); font-weight:700; margin:18px 0 9px; }}
.wm-now {{ display:flex; gap:12px; flex-wrap:wrap; }}
.wm-card {{ flex:1 1 240px; border:1px solid var(--line); border-top-width:4px; border-radius:14px;
  padding:13px 15px; background:var(--card); transition:transform .18s; }}
.wm-card:hover {{ transform:translateY(-3px); }}
.wm-card h4 {{ font-size:15px; margin-bottom:6px; }}
.wm-card ul {{ margin:0 0 0 18px; font-size:14.5px; }}
.wm-card.is-done {{ border-top-color:var(--good); }}
.wm-card.is-doing {{ border-top-color:var(--accent); }}
.wm-card.is-wait {{ border-top-color:var(--warn); }}
.wm-foot {{ display:flex; justify-content:space-between; gap:10px; flex-wrap:wrap; color:var(--muted);
  font-size:12px; margin-top:15px; padding-top:10px; border-top:1px dashed var(--line); }}
@media (prefers-reduced-motion: reduce) {{
  .wm-wm-glow, .wm-glow, .wm-step.is-doing, .wm-flow::after, .wm::before, .wm-progress .wm-bar::after {{ animation:none; }}
}}
@media (max-width:640px) {{
  .section {{ padding:16px; }}
  main {{ padding:16px 10px 60px; }}
  .wm {{ padding:16px 14px; }}
  .wm-flow {{ display:none; }}
  .wm-step {{ flex:1 1 100%; }}
  .wm-title {{ font-size:19px; }}
  .wm-right {{ align-items:flex-start; }}
  .wm-progress .wm-bar {{ width:130px; }}
}}
</style>
</head>
<body>
<header>
  <div class="brand">
    <div class="brand-row">
      <div>
        <h1>🗺️ พาเที่ยว Dashboard</h1>
        <span class="sub">ภาพรวมธุรกิจ Ichino Tour — กระดานโน้ต พี่เจ &amp; พาเที่ยว</span>
      </div>
      <div class="tools">
        <button class="tool-btn" id="btn-font-minus" title="ตัวอักษรเล็กลง">A−</button>
        <button class="tool-btn" id="btn-font-plus" title="ตัวอักษรใหญ่ขึ้น">A+</button>
        <button class="tool-btn" id="btn-theme" title="สลับโหมดสว่าง/มืด">☀️ สว่าง</button>
      </div>
    </div>
  </div>
  <nav>{nav}</nav>
</header>
<button id="to-top" aria-label="กลับขึ้นบนสุด" title="กลับขึ้นบนสุด">↑</button>
<main>
{''.join(sections)}
</main>
<footer>อัปเดตล่าสุด: {os.environ.get('BUILD_TIME', '')} · แก้ไฟล์ใน content/*.md แล้ว build ใหม่</footer>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/10.7.1/firebase-firestore-compat.js"></script>
<script>
const firebaseConfig = {{
  apiKey: "AIzaSyDznvjBOYJviSVPwj9TESkuZrDANKHxqxA",
  authDomain: "phathiao-dashboard.firebaseapp.com",
  projectId: "phathiao-dashboard",
  storageBucket: "phathiao-dashboard.firebasestorage.app",
  messagingSenderId: "228151129172",
  appId: "1:228151129172:web:6de75a7b39fb76a01ee9c1"
}};
firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

async function loadNotes() {{
  try {{
    const snap = await db.collection('dashboard_notes').orderBy('created', 'desc').limit(50).get();
    const list = document.getElementById('notes-list');
    if (snap.empty) {{
      list.innerHTML = '<p class="muted">ยังไม่มีโน้ต — พิมพ์แรกเลย!</p>';
      return;
    }}
    list.innerHTML = snap.docs.map(d => {{
      const data = d.data();
      const name = data.name ? data.name : 'ไม่ระบุชื่อ';
      const date = data.created && data.created.toDate ? data.created.toDate().toLocaleString('th-TH') : '';
      return '<div class="note-card"><div>' + escapeHtml(data.text) + '</div><div class="note-meta">✍️ ' + escapeHtml(name) + ' · ' + date + '</div></div>';
    }}).join('');
  }} catch (e) {{
    document.getElementById('notes-list').innerHTML = '<p class="muted">โหลดโน้ตไม่ได้: ' + escapeHtml(String(e.message || e)) + '</p>';
  }}
}}

function escapeHtml(s) {{
  return String(s).replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));
}}

document.getElementById('note-submit').addEventListener('click', async () => {{
  const text = document.getElementById('note-text').value.trim();
  const name = document.getElementById('note-name').value.trim();
  const msg = document.getElementById('note-msg');
  if (!text) {{ msg.textContent = 'กรอกข้อความก่อน'; return; }}
  msg.textContent = 'กำลังบันทึก...';
  try {{
    await db.collection('dashboard_notes').add({{
      text: text,
      name: name || 'ไม่ระบุชื่อ',
      created: firebase.firestore.FieldValue.serverTimestamp()
    }});
    document.getElementById('note-text').value = '';
    msg.textContent = '✅ บันทึกแล้ว';
    loadNotes();
  }} catch (e) {{
    msg.textContent = '❌ บันทึกไม่ได้: ' + e.message;
  }}
}});

/* ---------- เฟส 1: นำทางด้วย URL (#งาน) · โหมดสว่าง-มืด · ขนาดตัวอักษร · ปุ่มขึ้นบนสุด · PWA ---------- */
const FONT_STEPS = [15, 16, 17, 18, 20];

function showSection(key, scrollTop) {{
  var el = document.getElementById(key);
  if (!el) {{ key = 'overview'; el = document.getElementById(key); }}
  document.querySelectorAll('.section').forEach(s => s.style.display = 'none');
  if (el) el.style.display = 'block';
  document.querySelectorAll('.nav-link').forEach(x => x.classList.toggle('active', x.dataset.target === key));
  if (scrollTop !== false) window.scrollTo({{ top: 0, behavior: 'smooth' }});
}}

function routeFromHash() {{
  var h = (location.hash || '').replace(/^#/, '');
  var key = h.split('/')[0] || 'overview';
  showSection(key, false);
  // แจ้งให้ส่วนอื่น (เช่น แผนที่งาน) รู้ว่ามีการเปลี่ยนเส้นทาง
  window.dispatchEvent(new CustomEvent('pd:route', {{ detail: {{ hash: h }} }}));
}}

document.querySelectorAll('.nav-link').forEach(a => {{
  a.addEventListener('click', e => {{
    e.preventDefault();
    if (location.hash === '#' + a.dataset.target) {{ routeFromHash(); return; }}
    location.hash = a.dataset.target;   // hashchange จะเรียก routeFromHash เอง
  }});
}});
window.addEventListener('hashchange', routeFromHash);

/* ปุ่มขนาดตัวอักษร + โหมดสว่าง/มืด */
function currentFont() {{
  var v = parseInt(localStorage.getItem('pd_font') || '16', 10);
  return FONT_STEPS.indexOf(v) >= 0 ? v : 16;
}}
function applyFont(px) {{
  document.documentElement.style.fontSize = px + 'px';
  try {{ localStorage.setItem('pd_font', String(px)); }} catch (e) {{}}
}}
document.getElementById('btn-font-plus').addEventListener('click', () => {{
  const i = FONT_STEPS.indexOf(currentFont());
  applyFont(FONT_STEPS[Math.min(i + 1, FONT_STEPS.length - 1)]);
}});
document.getElementById('btn-font-minus').addEventListener('click', () => {{
  const i = FONT_STEPS.indexOf(currentFont());
  applyFont(FONT_STEPS[Math.max(i - 1, 0)]);
}});
const themeBtn = document.getElementById('btn-theme');
function syncThemeBtn() {{
  const light = document.documentElement.classList.contains('light');
  themeBtn.textContent = light ? '🌙 มืด' : '☀️ สว่าง';
  const meta = document.querySelector('meta[name="theme-color"]');
  if (meta) meta.setAttribute('content', light ? '#f6f7fb' : '#0f172a');
}}
themeBtn.addEventListener('click', () => {{
  const light = document.documentElement.classList.toggle('light');
  try {{ localStorage.setItem('pd_theme', light ? 'light' : 'dark'); }} catch (e) {{}}
  syncThemeBtn();
}});
syncThemeBtn();

/* ปุ่มกลับขึ้นบนสุด */
const toTop = document.getElementById('to-top');
window.addEventListener('scroll', () => {{
  toTop.classList.toggle('show', window.scrollY > 480);
}}, {{ passive: true }});
toTop.addEventListener('click', () => window.scrollTo({{ top: 0, behavior: 'smooth' }}));

/* PWA: ติดตั้งเป็นแอปบนมือถือ + เปิดอ่านได้ตอนเน็ตหลุด */
if ('serviceWorker' in navigator && location.protocol.indexOf('http') === 0) {{
  navigator.serviceWorker.register('./sw.js').catch(() => {{}});
}}

(function() {{
  if (!location.hash) {{ location.replace('#overview'); }}
  routeFromHash();
  loadNotes();
  // บอกส่วนอื่นในหน้า (เช่น แผนที่งาน) ว่า Firebase พร้อมแล้ว — กัน ReferenceError ตอนสคริปต์ในเนื้อหารันก่อน
  window.__pdReady = true;
  window.dispatchEvent(new CustomEvent('pd:ready'));
}})();
</script>
</body>
</html>"""
    (OUT / "index.html").write_text(html_doc, encoding="utf-8")
    print(f"Built {OUT / 'index.html'} ({len(html_doc)} bytes)")

if __name__ == "__main__":
    build()
