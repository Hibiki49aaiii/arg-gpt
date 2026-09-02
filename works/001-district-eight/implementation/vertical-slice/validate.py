#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys
import ast

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

# Basic HTML / link integrity
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


# Separate real-world/meta content from in-world spoiler checks.
all_html_text = "\n".join(p.read_text(encoding="utf-8") for p in html_files)
inworld_files = [
    p for p in html_files
    if "sites/meta/" not in p.as_posix()
]
inworld_text = "\n".join(p.read_text(encoding="utf-8") for p in inworld_files)

if "久代市" in all_html_text:
    errors.append("runtime contains legacy municipality name: 久代市")

for banned in ("水城結", "共同記憶", "33秒", "桐谷", "三枝"):
    if banned in inworld_text:
        errors.append(f"in-world runtime contains premature Act 2+ term: {banned}")


# Vertical Slice narrative facts
plan = (
    SITES / "old-bousai/documents/1998-summer-plan/index.html"
).read_text(encoding="utf-8")

water = (
    SITES / "old-bousai/documents/water-stations/index.html"
).read_text(encoding="utf-8")

archive = (
    SITES / "old-bousai/archive/index.html"
).read_text(encoding="utf-8")

if "第八避難区対象者は別途指示" not in plan:
    errors.append("plan missing EV-004 clue")

if "第八避難区" not in water or "旧八号集会所" not in water:
    errors.append("water list missing EV-005 clue")

if "1998年8月20日" not in plan or "1998年8月20日" not in water:
    errors.append(
        "Act 1 documents must explicitly post-date the 1998-08-19 code creation"
    )

if "area08.gif" not in archive:
    errors.append("Route B missing orphan area08 reference")


# Recovery Routes
for route in ("A", "B", "C"):
    marker = f'data-clue-route="{route}"'
    if marker not in inworld_text:
        errors.append(f"Recovery Route {route} marker missing")


# Blind-playtest tooling must remain outside in-world navigation.
playtest = SITES / "meta/playtest.html"
if not playtest.exists():
    errors.append("meta playtest tool missing")
else:
    playtest_text = playtest.read_text(encoding="utf-8")
    for required in (
        "district8-vs-state",
        "district8-vs-events",
        "district8-vs-session-id",
        "Session ID",
        "セッション状態をリセット",
        "JSONをファイル保存",
        "new Blob",
        "URL.createObjectURL",
        "session_id:",
        "exported_at:",
        "外部送信はしていません",
        "実名・メールアドレス・アカウント名",
    ):
        if required not in playtest_text:
            errors.append(f"playtest tool missing requirement: {required}")

    for forbidden_network_api in (
        "fetch(",
        "XMLHttpRequest",
        "WebSocket",
        "sendBeacon",
        "EventSource",
    ):
        if forbidden_network_api in playtest_text:
            errors.append(
                f"playtest tool must remain local-only: found {forbidden_network_api}"
            )

    if "localStorage.removeItem(SESSION_KEY)" in playtest_text:
        errors.append(
            "session reset must preserve anonymous Session ID for export continuity"
        )

if "/meta/playtest.html" in inworld_text:
    errors.append(
        "developer playtest tool must not be linked directly from in-world pages"
    )

# One-command Human Gate operator launcher.
launcher = ROOT / "serve_playtest.py"
if not launcher.exists():
    errors.append("playtest launcher missing: serve_playtest.py")
else:
    launcher_text = launcher.read_text(encoding="utf-8")
    try:
        ast.parse(launcher_text)
    except SyntaxError as exc:
        errors.append(f"playtest launcher syntax error: {exc}")

    for required in (
        'default="127.0.0.1"',
        "default=8000",
        "/meta/playtest.html",
        "/old-bousai/",
        "--no-browser",
        "SimpleHTTPRequestHandler",
        "ThreadingTCPServer",
    ):
        if required not in launcher_text:
            errors.append(f"playtest launcher missing requirement: {required}")

    for forbidden_import in (
        "requests",
        "urllib.request",
        "httpx",
        "aiohttp",
    ):
        if f"import {forbidden_import}" in launcher_text or f"from {forbidden_import}" in launcher_text:
            errors.append(
                f"playtest launcher must not upload session data: {forbidden_import}"
            )

operator_runbook = ROOT.parent.parent / "PLAYTEST_OPERATOR_RUNBOOK.md"
if not operator_runbook.exists():
    errors.append("PLAYTEST_OPERATOR_RUNBOOK.md missing")
else:
    runbook_text = operator_runbook.read_text(encoding="utf-8")
    for required in (
        "serve_playtest.py",
        "127.0.0.1:8000/meta/playtest.html",
        "127.0.0.1:8000/old-bousai/",
        "Session ID",
        "PT-A01",
        "JSONをファイル保存",
        "PLAYTEST.md",
        "PLAYTEST_OBSERVER_SHEET.md",
        "30 minutes",
        "real name",
    ):
        if required not in runbook_text:
            errors.append(f"operator runbook missing requirement: {required}")


print(f"HTML files: {len(html_files)}")
print(f"In-world HTML files: {len(inworld_files)}")
print("Recovery routes: A / B / C")
print("Act 2+ in-world spoiler scan: enabled")
print("Blind playtest boundary scan: enabled")
print("Human Gate operator launcher: validated")
print("Anonymous local JSON export: validated")

if errors:
    print("\nVALIDATION FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("VALIDATION PASSED")
