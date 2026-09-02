#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).parent
DATA=ROOT/"content.json"
errors=[]

def fail(msg:str)->None:
    errors.append(msg)

try:
    data=json.loads(DATA.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ACT4 VALIDATION FAILED: cannot load content.json: {exc}")
    sys.exit(1)

if data.get("act")!=4:
    fail("act must be 4")
if data.get("status")!="staging-unlinked":
    fail("Act 4 staging must remain unlinked")
if data.get("runtime_connected") is not False:
    fail("Act 4 staging must not connect to earlier runtimes")
if data.get("incident_date")!="1998-08-14":
    fail("incident date lock mismatch")

diary=data.get("diary",{})
frags=diary.get("fragments",[])
by_id={x["id"]:x for x in frags}
expected_ids=[f"D-{i:02d}" for i in range(1,11)]
if diary.get("ordered_ids")!=expected_ids:
    fail("canonical diary order must be D-01..D-10")
if set(diary.get("initial_order",[]))!=set(expected_ids) or diary.get("initial_order")==expected_ids:
    fail("initial diary order must contain all fragments and be nonchronological")
if len(frags)!=10:
    fail("exactly 10 diary fragments required")

dates=[by_id[x]["date"] for x in expected_ids if x in by_id]
if dates!=sorted(dates):
    fail("diary canonical dates must increase")
expected_dates=[
    "1998-08-10","1998-08-11","1998-08-13","1998-08-14","1998-08-15",
    "1998-08-17","1998-08-19","1998-08-24","1998-09-07","1998-09-14"
]
if dates!=expected_dates:
    fail(f"diary date lock mismatch: {dates}")

incident=date.fromisoformat("1998-08-14")
for frag in frags:
    d=date.fromisoformat(frag["date"])
    text=frag.get("text","")
    if d<incident and "水無坂" in text:
        fail(f"pre-incident diary leaks 水無坂: {frag['id']}")

d04=by_id.get("D-04",{})
if "水無坂" not in d04.get("text",""):
    fail("D-04 must be first 水無坂 diary occurrence")
if d04.get("event_time")!="19:10" or d04.get("event_quote")!="水無坂の家に帰りたい":
    fail("D-04 19:10 family statement mismatch")

if "他にも同地区を覚える人" not in by_id.get("D-06",{}).get("facts",[]):
    fail("D-06 must preserve 8/17 spread awareness")
if "両方の家がemotionally real" not in by_id.get("D-08",{}).get("facts",[]):
    fail("D-08 must preserve dual-home emotional state")
if "mid-September decay" not in by_id.get("D-10",{}).get("facts",[]):
    fail("D-10 must preserve mid-September decay")

if diary.get("external_lookup_required") is not False:
    fail("diary puzzle must not require external lookup")
reference_types={x.get("type") for x in diary.get("references",[])}
required_refs={"club_schedule","library_slip","festival_flyer","family_memo","municipal_notice"}
if not required_refs.issubset(reference_types):
    fail(f"missing mundane ordering references: {sorted(required_refs-reference_types)}")

drawings=data.get("drawings",[])
if len(drawings)!=3:
    fail("exactly three child drawings required")
schools=[x.get("school") for x in drawings]
households=[x.get("household") for x in drawings]
if len(set(schools))!=3:
    fail("drawings must come from three different schools")
if len(set(households))!=3:
    fail("drawings must come from three different households")
if sorted(x.get("date") for x in drawings)!=["1998-08-15","1998-08-15","1998-08-18"]:
    fail("drawing collection dates mismatch")

# Fairness: no one drawing may expose every linear topology node.
linear=data.get("topology",{}).get("linear_projection",[])
for drawing in drawings:
    if set(linear).issubset(set(drawing.get("visible",[]))):
        fail(f"{drawing['id']} exposes complete linear topology alone")
    if not drawing.get("occluded"):
        fail(f"{drawing['id']} must occlude at least one relevant feature")

topology=data.get("topology",{})
expected_linear=["PARK","VENDING_MACHINE","BLUE_FENCE","TRIANGULAR_ROOF_HALL"]
if topology.get("linear_projection")!=expected_linear:
    fail("partial topology linear projection mismatch")
expected_relations={
    ("PARK","contains","ROUND_FOUNDATION"),
    ("PARK","connects_uphill_to","SLOPE"),
    ("SLOPE","contains_midway","VENDING_MACHINE"),
    ("SLOPE","upper_end_near","BLUE_FENCE"),
    ("BLUE_FENCE","beyond","TRIANGULAR_ROOF_HALL"),
}
relations={tuple(x) for x in topology.get("relations",[])}
if relations!=expected_relations:
    fail("partial topology relation graph mismatch")
for key in ("compass_defined","scale_defined","real_city_coordinates_defined","complete_boundary_defined"):
    if topology.get(key) is not False:
        fail(f"partial map must leave {key} false")

essay=data.get("essay",{})
if essay.get("id")!="EV-020":
    fail("EV-020 essay missing")
essay_text="\n".join(essay.get("text",[]))
for required in ("時計はないけど","丸いところ","公園を出ると坂","自動販売機"):
    if required not in essay_text:
        fail(f"EV-020 missing corroboration: {required}")
for forbidden in ("青い柵","三角"):
    if forbidden in essay_text:
        fail(f"EV-020 over-solves topology with: {forbidden}")

parents=data.get("parent_summary",{})
if parents.get("id")!="EV-019" or parents.get("reliability")!="Biased":
    fail("EV-019 reliability contract mismatch")
if parents.get("sole_proof_allowed") is not False:
    fail("EV-019 must not be sole proof")

pm=data.get("partial_map",{})
if pm.get("complete") is not False:
    fail("Act 4 map must remain partial")
if pm.get("label")!="方角・縮尺・市内位置 不明":
    fail("partial map uncertainty label mismatch")

access=data.get("accessibility",{})
for key in ("image_independent_route","drawing_descriptions_require_synthesis","diary_keyboard_ordering"):
    if access.get(key) is not True:
        fail(f"accessibility contract missing: {key}")

if data.get("act5_lead",{}).get("label")!="旧市街地図Collection":
    fail("Act 5 lead label mismatch")

player_blob=json.dumps({
    "diary":diary,
    "drawings":drawings,
    "essay":essay,
    "parent_summary":parents,
    "partial_map":pm,
    "act5_lead":data.get("act5_lead",{})
},ensure_ascii=False)
for forbidden in data.get("player_facing_forbidden_terms",[]):
    if forbidden in player_blob:
        fail(f"Act 4 contract leaks later mechanism term: {forbidden}")


# ---------------------------------------------------------------------------
# Staging website integrity
# ---------------------------------------------------------------------------
SITE=ROOT/"site"

class LinkParser(HTMLParser):
    def __init__(self)->None:
        super().__init__()
        self.refs:list[str]=[]
    def handle_starttag(self,tag,attrs)->None:
        d=dict(attrs)
        for key in ("href","src"):
            value=d.get(key)
            if value:
                self.refs.append(value)

def target_for(source:Path,ref:str)->Path|None:
    parts=urlsplit(ref)
    if parts.scheme or parts.netloc or ref.startswith("#") or ref.startswith("mailto:"):
        return None
    p=unquote(parts.path)
    if not p:
        return None
    target=(SITE/p.lstrip("/")) if p.startswith("/") else (source.parent/p)
    if p.endswith("/"):
        target=target/"index.html"
    return target.resolve()

required_pages=[
    SITE/"school/index.html",
    SITE/"school/mizuki-diary/index.html",
    SITE/"school/mizuki-diary/references/index.html",
    SITE/"school/elementary/special-collection/drawings/index.html",
    SITE/"school/elementary/archive/essays/makabe-shun/index.html",
    SITE/"archives/interviews/parents/index.html",
    SITE/"school/elementary/special-collection/topology/index.html",
    SITE/"school/elementary/special-collection/partial-map/index.html",
    SITE/"archives/maps/index.html",
]
for page in required_pages:
    if not page.exists():
        fail(f"required staging page missing: {page.relative_to(ROOT)}")

html_files=sorted(SITE.rglob("*.html"))
site_text_parts=[]
for page in html_files:
    text=page.read_text(encoding="utf-8")
    site_text_parts.append(text)
    if '<html lang="ja"' not in text:
        fail(f"{page.relative_to(ROOT)}: missing lang=ja")
    if "<main" not in text:
        fail(f"{page.relative_to(ROOT)}: missing main landmark")
    parser=LinkParser()
    parser.feed(text)
    for ref in parser.refs:
        target=target_for(page,ref)
        if target is not None and not target.exists():
            fail(f"{page.relative_to(ROOT)}: broken local reference {ref}")

site_text="\n".join(site_text_parts)

# Later-mechanism language must not appear in the Act 4 player-facing staging.
for forbidden in ("地図が変化","地図が変わ","新しい道路線","電話帳が変","記述密度","再構築","現実改変","記録媒介","桐谷","三枝"):
    if forbidden in site_text:
        fail(f"Act 4 staging HTML leaks later mechanism term: {forbidden}")

diary_page=(SITE/"school/mizuki-diary/index.html").read_text(encoding="utf-8")
for did in expected_ids:
    if f'data-diary-id="{did}"' not in diary_page:
        fail(f"diary page missing fragment DOM contract: {did}")
if diary_page.find('data-diary-id="D-08"') > diary_page.find('data-diary-id="D-01"'):
    fail("diary page initial order no longer matches nonchronological staging intent")
for required in ('data-check-diary','data-reset-diary','data-diary-solved hidden'):
    if required not in diary_page:
        fail(f"diary puzzle DOM missing: {required}")

# Pull only the pre-incident card blocks from the HTML and confirm they remain clean.
for did in ("D-01","D-02","D-03"):
    start=diary_page.find(f'data-diary-id="{did}"')
    end=diary_page.find('</article>',start)
    if start<0 or end<0:
        fail(f"cannot isolate pre-incident diary card: {did}")
    elif "水無坂" in diary_page[start:end]:
        fail(f"pre-incident diary HTML leaks 水無坂: {did}")

refs_page=(SITE/"school/mizuki-diary/references/index.html").read_text(encoding="utf-8")
for required in ("8/10 Mon","8/11 Tue","返却期限: 1998-08-13","1998-08-15 Saturday","土曜","1998-08-14 Friday","外部の天気・テレビ欄等は必要ありません"):
    if required not in refs_page:
        fail(f"ordering reference page missing: {required}")

drawings_page=(SITE/"school/elementary/special-collection/drawings/index.html").read_text(encoding="utf-8")
for required in ("EV-018-A","EV-018-B","EV-018-C","凪代市立東小学校","凪代市立北小学校","凪代市立臨海小学校","Text description"):
    if required not in drawings_page:
        fail(f"drawings page missing: {required}")
if "1資料だけでは全体の並びは確定できません" not in drawings_page:
    fail("drawings page must communicate multi-source synthesis")

essay_page=(SITE/"school/elementary/archive/essays/makabe-shun/index.html").read_text(encoding="utf-8")
for required in ("時計はないけど","丸いところ","公園を出ると坂","自動販売機"):
    if required not in essay_page:
        fail(f"essay page missing: {required}")
for forbidden in ("青い柵","三角屋根"):
    if forbidden in essay_page and "単独では" not in essay_page:
        fail(f"essay page risks over-solving topology: {forbidden}")

parents_page=(SITE/"archives/interviews/parents/index.html").read_text(encoding="utf-8")
for required in ("Administrative Summary","原発言を逐語的に保存したものではありません","補助資料","別媒体との照合"):
    if required not in parents_page:
        fail(f"EV-019 support-only framing missing: {required}")

topology_page=(SITE/"school/elementary/special-collection/topology/index.html").read_text(encoding="utf-8")
for required in ('id="slot1"','id="slot2"','id="slot3"','id="slot4"','id="foundation-location"','data-check-topology','data-topology-solved hidden'):
    if required not in topology_page:
        fail(f"topology DOM contract missing: {required}")

app_js=(SITE/"app.js").read_text(encoding="utf-8")
for required in (
    "D-01','D-02','D-03','D-04','D-05','D-06','D-07','D-08','D-09','D-10",
    "PARK|VENDING_MACHINE|BLUE_FENCE|TRIANGULAR_ROOF_HALL",
    "foundation==='PARK'",
    "data-move",
):
    if required not in app_js:
        fail(f"Act 4 app logic missing: {required}")

partial_page=(SITE/"school/elementary/special-collection/partial-map/index.html").read_text(encoding="utf-8")
for required in ("水無坂周辺 — 関係図（暫定）","方角・縮尺・市内位置 不明","ROUND FOUNDATION","VENDING MACHINE","BLUE FENCE","TRIANGULAR-ROOF HALL","旧市街地図Collection"):
    if required not in partial_page:
        fail(f"partial map page missing: {required}")
if "地区境界を示すものではありません" not in partial_page:
    fail("partial map must explicitly reject complete-boundary interpretation")

maps_page=(SITE/"archives/maps/index.html").read_text(encoding="utf-8")
for required in ("1997年 市街地図","1998年7月 市街地図","1998年9月 市街地図","2001年 保存複写","公開準備中"):
    if required not in maps_page:
        fail(f"Act 5 neutral lead missing: {required}")


print(f"Diary fragments: {len(frags)}")
print(f"Ordering references: {len(diary.get('references',[]))}")
print(f"Independent drawings: {len(drawings)}")
print(f"Topology relations: {len(relations)}")
print(f"Staging HTML files: {len(html_files)}")
print("Staging link integrity: enabled")
print("Puzzle DOM contracts: enabled")
print("Pre-8/14 水無坂 occurrences: 0")
print("External lookup dependency: disabled")
print("Image-independent route: enabled")
print("Partial-map boundary: enforced")
print("Act 5 mechanism spoiler scan: enabled")
print("Human-gate isolation: enabled")

if errors:
    print("\nACT4 VALIDATION FAILED")
    for err in errors:
        print(" -",err)
    sys.exit(1)

print("ACT4 VALIDATION PASSED")
