#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

ROOT = Path(__file__).parent
SITES = ROOT / "sites"

class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        for key in ("href", "src"):
            value = data.get(key)
            if value:
                self.refs.append((tag, key, value))

def target_for(source: Path, ref: str) -> Path | None:
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc or ref.startswith("#") or ref.startswith("mailto:"):
        return None
    path = unquote(parts.path)
    if not path:
        return None
    if path.startswith("/"):
        target = SITES / path.lstrip("/")
    else:
        target = source.parent / path
    if path.endswith("/"):
        target = target / "index.html"
    return target.resolve()

errors = []
html_files = sorted(SITES.rglob("*.html"))
for page in html_files:
    text = page.read_text(encoding="utf-8")
    if '<html lang="ja"' not in text:
        errors.append(f"{page}: missing lang=ja")
    if "<main" not in text:
        errors.append(f"{page}: missing main landmark")
    parser = LinkParser()
    parser.feed(text)
    for _tag, _key, ref in parser.refs:
        target = target_for(page, ref)
        if target is not None and not target.exists():
            errors.append(f"{page}: broken local reference {ref} -> {target}")

runtime_text = "\n".join(p.read_text(encoding="utf-8") for p in html_files)
for banned in ("久代市", "水城結", "共同記憶", "33秒", "桐谷", "三枝"):
    if banned in runtime_text:
        errors.append(f"runtime contains premature/legacy term: {banned}")

plan = (SITES / "old-bousai/documents/1998-summer-plan/index.html").read_text(encoding="utf-8")
water = (SITES / "old-bousai/documents/water-stations/index.html").read_text(encoding="utf-8")
archive = (SITES / "old-bousai/archive/index.html").read_text(encoding="utf-8")

if "第八避難区対象者は別途指示" not in plan:
    errors.append("plan missing EV-004 clue")
if "第八避難区" not in water or "旧八号集会所" not in water:
    errors.append("water list missing EV-005 clue")
if "1998年8月20日" not in plan or "1998年8月20日" not in water:
    errors.append("Act 1 documents must explicitly post-date the 1998-08-19 code creation")
if "area08.gif" not in archive:
    errors.append("Route B missing orphan area08 reference")

for route in ("A", "B", "C"):
    if f'data-clue-route="{route}"' not in runtime_text:
        errors.append(f"Recovery Route {route} marker missing")

print(f"HTML files: {len(html_files)}")
print("Recovery routes: A / B / C")
print("Act 2+ spoiler scan: enabled")
if errors:
    print("\nVALIDATION FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("VALIDATION PASSED")
