#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

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

print(f"Map versions: {len(versions)}")
print(f"Fixed anchors: {len(anchors)}")
print(f"Reverse citations: {len(citations)}")
print(f"Trend buckets: {len(buckets)}")
print(f"Saegusa chronology nodes: {len(chron)}")
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
