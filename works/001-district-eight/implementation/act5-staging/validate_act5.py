#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
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
    print(f"ACT5 VALIDATION FAILED: cannot load content.json: {exc}")
    sys.exit(1)

if data.get("act")!=5:
    fail("act must be 5")
if data.get("status")!="staging-unlinked":
    fail("Act 5 staging must remain unlinked")
if data.get("runtime_connected") is not False:
    fail("Act 5 staging must not connect to earlier runtimes")

maps=data.get("maps",{})
anchors=maps.get("anchors",[])
if [(x.get("id"),x.get("x"),x.get("y")) for x in anchors] != [("A",0,0),("B",100,0),("C",40,80)]:
    fail("map fixed-anchor contract mismatch")
if maps.get("fixed_anchor_alignment_required") is not True:
    fail("PZ-008 must require fixed-anchor alignment")
if maps.get("text_coordinate_route") is not True:
    fail("PZ-008 must have text coordinate route")
if maps.get("target_label_exposed") is not False:
    fail("map target line must not be labeled 水無坂")

versions=maps.get("versions",[])
expected=[
    ("MAP-1997","1997","absent"),
    ("MAP-1998-07","1998-07","absent"),
    ("MAP-1998-09","1998-09","faint"),
    ("MAP-2001","2001","clear"),
]
got=[(x.get("id"),x.get("date"),x.get("target_feature")) for x in versions]
if got!=expected:
    fail(f"map chronology mismatch: {got}")
if versions[2].get("line")!=[[57,42],[62,35]]:
    fail("1998-09 target line coordinates mismatch")
if versions[3].get("line")!=[[57,42],[63,34]]:
    fail("2001 target line coordinates mismatch")
if versions[2].get("confidence")!="low" or versions[3].get("confidence")!="high":
    fail("map confidence progression mismatch")

phone=data.get("phonebook",{})
if phone.get("id")!="EV-023":
    fail("EV-023 phonebook contract missing")
if phone.get("initial_copy",{}).get("waterless_slope_heading") is not False:
    fail("1998 initial phonebook copy must not contain 水無坂")
if phone.get("later_preserved_copy",{}).get("waterless_slope_heading") is not True:
    fail("later preserved phonebook must contain 水無坂 heading")
if phone.get("real_phone_numbers") is not False:
    fail("real phone numbers must never be used")

photo=data.get("photo",{})
if photo.get("id")!="EV-022" or photo.get("required") is not False or photo.get("reliability")!="Unknown":
    fail("EV-022 must remain optional Unknown evidence")
if len(photo.get("ordinary_explanations",[]))<3:
    fail("EV-022 must expose ordinary alternative explanations")

k=data.get("kiritani",{})
note_a=k.get("note_a",{})
if note_a.get("id")!="EV-024" or note_a.get("missing_section")!="4.3":
    fail("Kiritani Note A missing-section contract mismatch")
if note_a.get("early_model")!="human_information_spread":
    fail("Kiritani early model must remain human information spread")

citations=k.get("reverse_citations",[])
if len(citations)<4:
    fail("PZ-009 requires at least four reverse citations")
sources={x.get("source") for x in citations}
if len(sources)!=len(citations):
    fail("reverse citations must come from distinct locations")
citation_blob="\n".join(x.get("claim","") for x in citations)
for required in ("新規回答者","記録追加後","記述量区分","reverse direction"):
    if required not in citation_blob:
        fail(f"reverse citation graph missing semantic: {required}")

note_b=k.get("note_b",{})
if note_b.get("id")!="EV-025":
    fail("EV-025 missing")
if note_b.get("temporal_direction")!="records_increase_before_later_new_recall":
    fail("EV-025 must preserve record->later-new-recall temporal direction")
if note_b.get("causality_proven") is not False:
    fail("EV-025 must not claim causality proven")
if note_b.get("direct_human_spread_sufficient") is not False:
    fail("EV-025 must challenge direct-human-spread sufficiency")

contain=data.get("containment",{})
order=contain.get("order",{})
if order.get("id")!="EV-026" or order.get("date")!="1998-09-03":
    fail("EV-026 containment start must remain 1998-09-03")
trend=contain.get("trend",{})
if trend.get("id")!="EV-027" or trend.get("correlation_only") is not True:
    fail("EV-027 must remain correlation-only")
buckets=trend.get("buckets",[])
if len(buckets)!=7:
    fail("EV-027 requires seven reporting buckets")
if buckets[4][0]!="1998-09-03/1998-09-09":
    fail("EV-027 must visibly bracket 9/3 containment")
if not all(buckets[i][1]>=buckets[i+1][1] for i in range(3,len(buckets)-1)):
    fail("post-8/31 report counts must not rise in canonical trend")
if len(trend.get("confounders",[]))<4:
    fail("EV-027 must list confounders")

s=data.get("saegusa",{})
chron=s.get("chronology",[])
years=[x.get("year") for x in chron]
if years!=[1999,2005,2007,2008,2009]:
    fail(f"Saegusa chronology mismatch: {years}")
actions=[x.get("action") for x in chron]
if actions!=["preserve","digitize_reorganize","recurrence_concern","voluntary_delete","final_memo"]:
    fail("Saegusa action sequence mismatch")
if s.get("voluntary_deletion") is not True:
    fail("Saegusa deletion must be voluntary")
if chron[-1].get("claim")!="残せば戻る。消せば彼らが消える。":
    fail("EV-031 final memo line mismatch")

boundary=data.get("act6_boundary",{})
for key in ("complete_map_created","player_causality_revealed","current_municipal_area8_revealed","ending_choice_revealed"):
    if boundary.get(key) is not False:
        fail(f"Act 6 boundary violated: {key}")

player_blob=json.dumps({
    "maps":maps,
    "phonebook":phone,
    "photo":photo,
    "kiritani":k,
    "containment":contain,
    "saegusa":s
},ensure_ascii=False)
for forbidden in data.get("player_facing_forbidden_terms",[]):
    if forbidden in player_blob:
        fail(f"Act 5 contract leaks Act 6 term: {forbidden}")


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
    SITE/"archives/index.html",
    SITE/"archives/maps/index.html",
    SITE/"archives/maps/compare/index.html",
    SITE/"archives/phonebook/index.html",
    SITE/"archives/photos/p1842/index.html",
    SITE/"research/index.html",
    SITE/"research/kiritani/note-a/index.html",
    SITE/"research/kiritani/reverse-citation/index.html",
    SITE/"research/kiritani/note-b/index.html",
    SITE/"research/containment/index.html",
    SITE/"saegusa/index.html",
    SITE/"saegusa/timeline/index.html",
    SITE/"saegusa/final/index.html",
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

# Act 6 must remain unrevealed in player-facing Act 5 pages.
for forbidden in (
    "プレイヤーが第八区を作る",
    "完全地図を作ると現実が変わる",
    "現在の防災ページに第8避難区が追加",
    "調査が再発原因",
    "END-A","END-B","END-C"
):
    if forbidden in site_text:
        fail(f"Act 5 staging HTML leaks Act 6 term: {forbidden}")

maps_page=(SITE/"archives/maps/index.html").read_text(encoding="utf-8")
for required in ("MAP-1997","MAP-1998-07","MAP-1998-09","MAP-2001","1997 市街地図 保存複写","1998年7月 市街地図 印刷複写","1998年9月 市街地図 保管原本","2001 デジタル保存スキャン"):
    if required not in maps_page:
        fail(f"map collection page missing: {required}")
if "水無坂" in maps_page:
    fail("EV-021 map collection must not label the target feature 水無坂")

compare_page=(SITE/"archives/maps/compare/index.html").read_text(encoding="utf-8")
for required in ('id="anchor-a"','id="anchor-b"','id="anchor-c"','data-lock-map','data-map-solved hidden',"Text-only route","(57,42) → (62,35)","(57,42) → (63,34)"):
    if required not in compare_page:
        fail(f"PZ-008 compare DOM/content missing: {required}")
if "水無坂" in compare_page:
    fail("PZ-008 compare page must not label target line 水無坂")

phone_page=(SITE/"archives/phonebook/index.html").read_text(encoding="utf-8")
for required in ("1998年 初期参照複写","後年 保管版","水無坂","なし","あり","実在の電話番号・個人情報は使用していません"):
    if required not in phone_page:
        fail(f"EV-023 phonebook page missing: {required}")

photo_page=(SITE/"archives/photos/p1842/index.html").read_text(encoding="utf-8")
for required in ("Reliability: Unknown / Optional","scan crop difference","restoration artifact","negative mix-up","labeling error","本編進行にも必須ではありません"):
    if required not in photo_page:
        fail(f"EV-022 optional/Unknown framing missing: {required}")

research_index=(SITE/"research/index.html").read_text(encoding="utf-8")
if 'href="/research/containment/"' in research_index:
    fail("research index must not bypass Reverse Citation directly to containment")
if 'href="/saegusa/"' in research_index:
    fail("research index must not bypass Kiritani route directly to Saegusa")

note_a_page=(SITE/"research/kiritani/note-a/index.html").read_text(encoding="utf-8")
for required in ("4.3 [欠落]","共有刺激または情報伝播","4.3参照箇所"):
    if required not in note_a_page:
        fail(f"EV-024 Note A missing: {required}")
if 'href="/research/containment/"' in note_a_page:
    fail("Note A must not bypass PZ-009 to containment")

reverse_page=(SITE/"research/kiritani/reverse-citation/index.html").read_text(encoding="utf-8")
for cid in ("C-01","C-02","C-03","C-04"):
    if cid not in reverse_page:
        fail(f"PZ-009 page missing citation: {cid}")
for required in ("新規回答者","記録追加後","記述量区分A–D","reverse direction not excluded",'data-synthesize-citations','data-citation-solved hidden'):
    if required not in reverse_page:
        fail(f"PZ-009 DOM/semantic missing: {required}")
if 'href="/research/kiritani/note-b/"' not in reverse_page:
    fail("PZ-009 solved state must unlock EV-025")

note_b_page=(SITE/"research/kiritani/note-b/index.html").read_text(encoding="utf-8")
for required in ("後続測定で新規回答者","記録が追加された後の新規回答者","因果を確定しない","直接情報伝播のみで説明することは困難"):
    if required not in note_b_page:
        fail(f"EV-025 temporal-direction wording missing: {required}")
if 'href="/research/containment/"' not in note_b_page:
    fail("EV-025 must lead to containment evidence")

contain_page=(SITE/"research/containment/index.html").read_text(encoding="utf-8")
for required in ("1998-09-03","Correlation only","因果効果を証明するものではありません","8/14–8/16","9/17–9/30","Confounders"):
    if required not in contain_page:
        fail(f"containment page missing: {required}")
if 'href="/saegusa/"' not in contain_page:
    fail("containment page must lead to Saegusa route")

saegusa_page=(SITE/"saegusa/timeline/index.html").read_text(encoding="utf-8")
for sid in ("S-1999","S-2005","S-2007","S-2008","S-2009"):
    if f'data-saegusa-id="{sid}"' not in saegusa_page:
        fail(f"PZ-010 timeline missing: {sid}")
for required in ('data-check-saegusa','data-saegusa-solved hidden',"外部takedown記録なし","2008-09-03 / 09-07 / 09-12"):
    if required not in saegusa_page:
        fail(f"PZ-010 DOM/evidence missing: {required}")
if saegusa_page.find('data-saegusa-id="S-2008"') > saegusa_page.find('data-saegusa-id="S-1999"'):
    fail("Saegusa initial staging order should remain nonchronological")

app_js=(SITE/"app.js").read_text(encoding="utf-8")
for required in (
    "a==='river'&&b==='civic'&&c==='railway'",
    "checked.length===4",
    "S-1999','S-2005','S-2007','S-2008','S-2009"
):
    if required not in app_js:
        fail(f"Act 5 puzzle logic missing: {required}")

final_page=(SITE/"saegusa/final/index.html").read_text(encoding="utf-8")
for required in ("残せば戻る。消せば彼らが消える。","名前まで消す必要があるのか、まだ分からない","安全な保存方法や現象の完全な説明を残していません","残すべき記録と、残してはいけない記録は同じなのか"):
    if required not in final_page:
        fail(f"EV-031 ambiguity missing: {required}")


print(f"Map versions: {len(versions)}")
print(f"Fixed anchors: {len(anchors)}")
print(f"Reverse citations: {len(citations)}")
print(f"Trend buckets: {len(buckets)}")
print(f"Saegusa chronology nodes: {len(chron)}")
print(f"Staging HTML files: {len(html_files)}")
print("Staging link integrity: enabled")
print("Puzzle DOM contracts: enabled")
print("Text-coordinate map route: enabled")
print("EV-022 optional/Unknown: enforced")
print("EV-027 correlation-only: enforced")
print("Act 6 spoiler boundary: enforced")
print("Human-gate isolation: enabled")

if errors:
    print("\nACT5 VALIDATION FAILED")
    for err in errors:
        print(" -",err)
    sys.exit(1)

print("ACT5 VALIDATION PASSED")
