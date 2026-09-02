#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import date
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).parent
DATA = ROOT / "content.json"
SITE = ROOT / "site"

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


# ---------------------------------------------------------------------------
# Machine-readable narrative contract
# ---------------------------------------------------------------------------
try:
    data = json.loads(DATA.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ACT3 VALIDATION FAILED: cannot load content.json: {exc}")
    sys.exit(1)

if data.get("act") != 3:
    fail("act must be 3")
if data.get("status") != "staging-unlinked":
    fail("Act 3 staging must remain unlinked")
if data.get("runtime_connected") is not False:
    fail("Act 3 staging must not be connected to current runtimes")

incident = data.get("incident", {})
sender = incident.get("sender", {})
recv = incident.get("receiver_window", {})

if sender.get("duration_seconds") != 27:
    fail("sender duration must be 27 seconds")
if recv.get("duration_seconds") != 60:
    fail("receiver window must be 60 seconds")
if recv.get("surplus_seconds") != 33:
    fail("surplus duration must be 33 seconds")
if recv.get("duration_seconds") - sender.get("duration_seconds") != recv.get("surplus_seconds"):
    fail("60 - 27 must equal 33")

if sender.get("start") != "18:00:00.000" or sender.get("end") != "18:00:27.000":
    fail("sender absolute timing mismatch")
if recv.get("surplus_start") != "18:00:27.000" or recv.get("surplus_end") != "18:01:00.000":
    fail("receiver surplus interval mismatch")

chron = data.get("chronology", {})
if date.fromisoformat(chron.get("phrase_received")) >= date.fromisoformat(chron.get("formal_code_created")):
    fail("第八避難区 phrase must predate formal code creation")
if chron.get("first_inquiry") != "1998-08-14T18:12:00":
    fail("first inquiry must remain 18:12")
if chron.get("similar_inquiries") != "1998-08-14T18:25:00":
    fail("similar inquiries must remain 18:25")

evidence = {x["id"]: x for x in data.get("evidence", [])}
required = {"EV-011", "EV-012", "EV-013", "EV-014", "EV-015"}
missing = required - evidence.keys()
if missing:
    fail(f"missing Act 3 evidence: {sorted(missing)}")

ev11 = evidence.get("EV-011", {})
joined11 = "\n".join(ev11.get("required_facts", []))
for required_fact in (
    "18:00:00 START TEST_0814 SCHEDULED",
    "18:00:27 END TEST_0814 NORMAL",
    "Recorded duration: 00:27.000",
    "Aux input: OFF",
    "Manual override: NONE",
):
    if required_fact not in joined11:
        fail(f"EV-011 missing: {required_fact}")
for forbidden in ("第八避難区", "水無坂"):
    if forbidden in joined11:
        fail(f"sender log must not contain {forbidden}")

a = evidence.get("EV-012", {})
b = evidence.get("EV-013", {})
if a.get("provenance", {}).get("capture_path") == b.get("provenance", {}).get("capture_path"):
    fail("Tape A and B capture paths must be independent")
if a.get("provenance", {}).get("owner") == b.get("provenance", {}).get("owner"):
    fail("Tape A and B owners must be independent")

for tape in (a, b):
    raw = " ".join(tape.get("pre_alignment_display_fragments", []))
    for solved in ("第八避難区", "水無坂"):
        if solved in raw:
            fail(f"{tape.get('label')} pre-alignment display exposes solved term: {solved}")

ev15 = evidence.get("EV-015", {})
entries = {x.get("time"): x.get("text") for x in ev15.get("entries", [])}
if entries.get("18:12") != "第八ってどこですか":
    fail("EV-015 18:12 inquiry mismatch")
if entries.get("18:25") != "同様問い合わせ 3件":
    fail("EV-015 18:25 inquiry mismatch")

segments = data.get("surplus_segments", [])
if not segments:
    fail("surplus segment map missing")
else:
    previous = 27.0
    for seg in segments:
        start = float(seg["start"])
        end = float(seg["end"])
        if abs(start - previous) > 0.0001:
            fail(f"segment gap/overlap before {start}")
        if end <= start:
            fail(f"invalid segment {start}-{end}")
        previous = end
    if abs(previous - 60.0) > 0.0001:
        fail("surplus segments must end exactly at 60.000")

composites = [x.get("composite", "") for x in segments]
if not any("第八避難区" in x for x in composites):
    fail("composite must recover 第八避難区")
if not any("水無坂" in x for x in composites):
    fail("composite must recover 水無坂")
if not any(x.get("role") == "shared_short_chime" for x in segments):
    fail("final shared short chime segment missing")

alignment = data.get("alignment", {})
anchors = alignment.get("anchors", [])
if len(anchors) < 2:
    fail("at least two normal-source alignment anchors required")
if not all(x.get("within_sender_window") for x in anchors):
    fail("alignment anchors must be within normal sender window")
if alignment.get("final_chime_is_anchor") is not False:
    fail("unknown final chime must not be used as alignment anchor")
if alignment.get("external_audio_editor_required") is not False:
    fail("external audio editor must not be required")

access = data.get("accessibility", {})
if access.get("equivalent_route") is not True:
    fail("non-audio equivalent route required")
if access.get("full_composite_before_solve") is not False:
    fail("full composite must remain hidden before solve")
required_access = {
    "waveform_envelopes",
    "timestamped_transcript_fragments",
    "confidence_markers",
    "duration_table",
    "shared_feature_markers",
    "sender_end_marker",
}
missing_access = required_access - set(access.get("components", []))
if missing_access:
    fail(f"missing accessibility components: {sorted(missing_access)}")

if data.get("act4_lead", {}).get("search_term") != "水無坂":
    fail("Act 4 lead must be 水無坂")

player_blob = json.dumps({
    "evidence": data.get("evidence", []),
    "segments": data.get("surplus_segments", []),
    "lead": data.get("act4_lead", {}),
}, ensure_ascii=False)
for forbidden in data.get("player_facing_forbidden_terms", []):
    if forbidden in player_blob:
        fail(f"Act 3 player-facing contract leaks later term: {forbidden}")


# ---------------------------------------------------------------------------
# Staging website integrity
# ---------------------------------------------------------------------------
class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.refs: list[str] = []

    def handle_starttag(self, tag, attrs) -> None:
        data = dict(attrs)
        for key in ("href", "src"):
            value = data.get(key)
            if value:
                self.refs.append(value)


def target_for(source: Path, ref: str) -> Path | None:
    parts = urlsplit(ref)
    if parts.scheme or parts.netloc or ref.startswith("#") or ref.startswith("mailto:"):
        return None
    path = unquote(parts.path)
    if not path:
        return None
    target = SITE / path.lstrip("/") if path.startswith("/") else source.parent / path
    if path.endswith("/"):
        target = target / "index.html"
    return target.resolve()


required_pages = [
    SITE / "radio/index.html",
    SITE / "radio/1998-08-14/index.html",
    SITE / "radio/recordings/a/index.html",
    SITE / "radio/recordings/b/index.html",
    SITE / "radio/compare/1998-08-14/index.html",
    SITE / "radio/equipment/index.html",
    SITE / "radio/digitization-notes/index.html",
    SITE / "radio/interviews/katase/index.html",
    SITE / "old-bousai/sender-log/index.html",
    SITE / "archives/inquiry/1998-08-14/index.html",
]

for page in required_pages:
    if not page.exists():
        fail(f"required staging page missing: {page.relative_to(ROOT)}")

html_files = sorted(SITE.rglob("*.html"))
site_text_parts: list[str] = []

for page in html_files:
    text = page.read_text(encoding="utf-8")
    site_text_parts.append(text)

    if '<html lang="ja"' not in text:
        fail(f"{page.relative_to(ROOT)}: missing lang=ja")
    if "<main" not in text:
        fail(f"{page.relative_to(ROOT)}: missing main landmark")

    parser = LinkParser()
    parser.feed(text)
    for ref in parser.refs:
        target = target_for(page, ref)
        if target is not None and not target.exists():
            fail(f"{page.relative_to(ROOT)}: broken local reference {ref}")

site_text = "\n".join(site_text_parts)

# Later mechanism must not appear anywhere in Act 3 staging HTML.
for forbidden in ("共同記憶", "記述密度", "再構築", "現実改変", "記録媒介", "桐谷", "三枝"):
    if forbidden in site_text:
        fail(f"Act 3 staging HTML leaks later mechanism term: {forbidden}")

# Individual receiver pages must preserve the comparison payoff.
tape_a_page = (SITE / "radio/recordings/a/index.html").read_text(encoding="utf-8")
tape_b_page = (SITE / "radio/recordings/b/index.html").read_text(encoding="utf-8")
for page_name, text in (("Tape A", tape_a_page), ("Tape B", tape_b_page)):
    for solved in ("第八避難区", "水無坂"):
        if solved in text:
            fail(f"{page_name} page exposes solved term before comparison: {solved}")

sender_page = (SITE / "old-bousai/sender-log/index.html").read_text(encoding="utf-8")
for required_fact in ("18:00:00", "18:00:27", "00:27.000", "Aux input: OFF", "Manual override: NONE"):
    if required_fact not in sender_page:
        fail(f"sender page missing: {required_fact}")
for forbidden in ("第八避難区", "水無坂"):
    if forbidden in sender_page:
        fail(f"sender page contains receiver-only term: {forbidden}")

inquiry_page = (SITE / "archives/inquiry/1998-08-14/index.html").read_text(encoding="utf-8")
for required_fact in ("18:12", "第八ってどこですか", "18:25", "同様問い合わせ 3件"):
    if required_fact not in inquiry_page:
        fail(f"inquiry page missing: {required_fact}")

katase_page = (SITE / "radio/interviews/katase/index.html").read_text(encoding="utf-8")
for required_fact in ("27秒", "18時00分27秒", "補助入力", "手動送出操作", "異常動作を再現できなかった", "発生源を特定できない"):
    if required_fact not in katase_page:
        fail(f"Katase report missing: {required_fact}")
if "原因を確定するものではありません" not in katase_page:
    fail("Katase page must explicitly avoid exoneration")

compare_page = (SITE / "radio/compare/1998-08-14/index.html").read_text(encoding="utf-8")
for required_fact in (
    "27.000秒",
    "60.000秒",
    "33.000秒",
    'id="anchor-1"',
    'id="anchor-2"',
    'id="apply-alignment"',
    'id="solved-table" hidden',
    "第八避難区の方は",
    "水無坂",
    "通常試験放送のチャイムと一致しない",
):
    if required_fact not in compare_page:
        fail(f"compare page missing: {required_fact}")

# Non-audio evidence must exist directly in the comparison UI.
for required_fact in ("Duration Comparison", "sender end", "Transcript断片"):
    if required_fact not in compare_page:
        fail(f"compare accessibility route missing: {required_fact}")

app_js = (SITE / "app.js").read_text(encoding="utf-8")
if "first==='opening'&&second==='closing'" not in app_js:
    fail("alignment UI must accept normal opening+closing anchors")
if "first==='closing'&&second==='opening'" not in app_js:
    fail("alignment UI must accept reversed normal anchor selection")
if "unknown-final" not in app_js and "unknown-final" not in compare_page:
    fail("unknown final chime option missing")
if "district8-act3-aligned" not in app_js:
    fail("staging alignment state key missing")

print(f"Evidence: {len(evidence)}")
print("Sender: 27.000s")
print("Receiver window: 60.000s")
print("Surplus: 33.000s")
print(f"Surplus segments: {len(segments)}")
print(f"Staging HTML files: {len(html_files)}")
print("Independent receiver chains: A / B")
print("Pre-solve transcript leakage: blocked")
print("Accessibility equivalent route: enabled")
print("Act 4+ mechanism spoiler scan: enabled")
print("Staging link integrity: enabled")
print("Human-gate isolation: enabled")

if errors:
    print("\nACT3 VALIDATION FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("ACT3 VALIDATION PASSED")
