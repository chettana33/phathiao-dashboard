#!/usr/bin/env python3
"""Build phathiao-dashboard: content/*.md -> docs/index.html"""
import os
import re
import html
from pathlib import Path

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
OUT = ROOT / "docs"

NAV_ITEMS = [
    ("overview", "ภาพรวม"),
    ("status", "สถานะงาน"),
    ("roadmap", "ลำดับถัดไป"),
    ("ideas", "กระดานไอเดีย"),
]

def inline(text):
    """Convert inline markdown: bold, italic, links, code."""
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'`(.+?)`', r'<code>\1</code>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)
    return text

def parse_md(text):
    """Parse markdown to HTML blocks. Supports headings, tables, lists, code, blockquote, hr."""
    blocks = []
    lines = text.split("\n")
    i = 0
    in_code = False
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
                blocks.append("<pre><code>" + "\n".join(code_buf) + "</code></pre>")
                code_buf = []
                in_code = False
            else:
                flush_list(); flush_table()
                in_code = True
            i += 1
            continue

        if in_code:
            code_buf.append(html.escape(line))
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

def build():
    OUT.mkdir(exist_ok=True)
    nav = "".join(
        f'<a href="#{key}" class="nav-link" data-target="{key}">{label}</a>'
        for key, label in NAV_ITEMS
    )

    sections = []
    for key, label in NAV_ITEMS:
        src = CONTENT / f"{key}.md"
        if not src.exists():
            continue
        body = parse_md(src.read_text(encoding="utf-8"))
        sections.append(f'<section id="{key}" class="section">{body}</section>')

    html_doc = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>พาเที่ยว Dashboard — ภาพรวมธุรกิจ Ichino Tour</title>
<style>
:root {{
  --bg:#0f172a; --card:#1e293b; --card2:#273449; --line:#334155;
  --text:#e2e8f0; --muted:#94a3b8; --accent:#38bdf8; --good:#4ade80; --warn:#facc15; --bad:#f87171;
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
main {{ max-width:1000px; margin:0 auto; padding:24px 16px 80px; }}
.section {{ background:var(--card); border:1px solid var(--line); border-radius:16px; padding:24px; margin-bottom:24px; }}
h1 {{ font-size:22px; color:var(--accent); margin-bottom:12px; }}
h2 {{ font-size:18px; color:var(--accent); margin:20px 0 10px; padding-bottom:6px; border-bottom:1px solid var(--line); }}
h3 {{ font-size:15px; color:var(--text); margin:14px 0 6px; }}
p {{ margin:6px 0; color:var(--text); }}
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
footer {{ text-align:center; color:var(--muted); font-size:12px; padding:20px; border-top:1px solid var(--line); }}
@media (max-width:640px) {{
  .section {{ padding:16px; }}
  main {{ padding:16px 10px 60px; }}
}}
</style>
</head>
<body>
<header>
  <div class="brand">
    <h1>🗺️ พาเที่ยว Dashboard</h1>
    <span class="sub">ภาพรวมธุรกิจ Ichino Tour — กระดานโน้ต พี่เจ &amp; พาเที่ยว</span>
  </div>
  <nav>{nav}</nav>
</header>
<main>
{''.join(sections)}
</main>
<footer>อัปเดตล่าสุด: {os.environ.get('BUILD_TIME', '')} · แก้ไฟล์ใน content/*.md แล้ว build ใหม่</footer>
<script>
document.querySelectorAll('.nav-link').forEach(a => {{
  a.addEventListener('click', e => {{
    e.preventDefault();
    document.querySelectorAll('.section').forEach(s => s.style.display = 'none');
    document.getElementById(a.dataset.target).style.display = 'block';
    document.querySelectorAll('.nav-link').forEach(x => x.classList.remove('active'));
    a.classList.add('active');
  }});
}});
(function() {{
  const first = document.querySelector('.section');
  if (first) first.style.display = 'block';
}})();
</script>
</body>
</html>"""
    (OUT / "index.html").write_text(html_doc, encoding="utf-8")
    print(f"Built {OUT / 'index.html'} ({len(html_doc)} bytes)")

if __name__ == "__main__":
    build()
