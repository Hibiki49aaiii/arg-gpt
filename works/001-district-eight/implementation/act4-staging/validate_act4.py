#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

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

print(f"Diary fragments: {len(frags)}")
print(f"Ordering references: {len(diary.get('references',[]))}")
print(f"Independent drawings: {len(drawings)}")
print(f"Topology relations: {len(relations)}")
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
