#!/usr/bin/env python3
"""Sync dashboard notes from Firestore -> content/notes.md (for AI to read via git).

Firestore rules allow public read, so no auth needed. Writes file only when content changes
so git only commits when there is something new.
"""
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / "content" / "notes.md"

FIREBASE_URL = (
    "https://firestore.googleapis.com/v1/projects/phathiao-dashboard/"
    "databases/(default)/documents/dashboard_notes"
)

def fetch_notes():
    url = FIREBASE_URL + "?orderBy=created%20desc&pageSize=50"
    req = urllib.request.Request(url, headers={"User-Agent": "phathiao-dashboard-sync"})
    r = urllib.request.urlopen(req, timeout=30)
    d = json.loads(r.read().decode("utf-8"))
    notes = []
    for doc in d.get("documents", []):
        f = doc.get("fields", {})
        text = f.get("text", {}).get("stringValue", "")
        name = f.get("name", {}).get("stringValue", "ไม่ระบุชื่อ")
        created = f.get("created", {}).get("timestampValue", "")[:10]
        notes.append({"text": text, "name": name, "date": created})
    return notes

def render(notes):
    lines = [
        "# 📝 โน้ตจากเว็บ (อัตโนมัติ)",
        "",
        "> ไฟล์นี้สร้างอัตโนมัติจาก `sync_notes.py` — โน้ตที่พี่เจ้าพิมพ์ในเว็บ dashboard",
        "> ห้ามแก้เอง — จะโดนทับทุก 30 นาที. อัปเดตล่าสุด: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "",
    ]
    if not notes:
        lines.append("_ยังไม่มีโน้ต_")
    for n in notes:
        lines.append(f"- **{n['date']}** · {n['name']}: {n['text']}")
    return "\n".join(lines) + "\n"

def main():
    try:
        notes = fetch_notes()
    except Exception as e:
        print("FETCH FAIL:", e)
        raise SystemExit(1)

    new_content = render(notes)
    changed = True
    if OUT.exists():
        old = OUT.read_text(encoding="utf-8")
        changed = old != new_content
    if changed:
        OUT.write_text(new_content, encoding="utf-8")
        print(f"WROTE {OUT} ({len(notes)} notes)")
    else:
        print("NO CHANGE")

if __name__ == "__main__":
    main()
