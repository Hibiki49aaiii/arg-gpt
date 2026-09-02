#!/usr/bin/env python3
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
import sys

ROOT = Path(__file__).parent
DATA = ROOT / "content.json"

errors: list[str] = []

try:
    data = json.loads(DATA.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ACT2 VALIDATION FAILED: cannot load content.json: {exc}")
    sys.exit(1)

def fail(message: str) -> None:
    errors.append(message)

if data.get("act") != 2:
    fail("act must be 2")
if data.get("status") != "staging-unlinked":
    fail("Act 2 staging must remain unlinked before human gate")
if data.get("runtime_connected") is not False:
    fail("Act 2 staging must not be connected to Act 0-1 runtime")
if data.get("municipality") != "凪代市":
    fail("municipality naming lock mismatch")

sequence = data.get("document_sequence", [])
numbers = [item.get("number") for item in sequence]
if numbers != [214, 215, 216]:
    fail(f"document sequence must be exactly 214,215,216; got {numbers}")

by_number = {item.get("number"): item for item in sequence}
if by_number.get(215, {}).get("date") != "1998-08-19":
    fail("防災第215号 must be dated 1998-08-19")
if by_number.get(214, {}).get("reference") != "防災第215号":
    fail("214 must reference 215 as a recovery route")
if by_number.get(216, {}).get("reference") != "防災第215号":
    fail("216 must reference 215 as a recovery route")

artifacts = {item["id"]: item for item in data.get("artifacts", [])}
required_ids = {"EV-006", "EV-007", "EV-008A", "EV-008B", "EV-009", "EV-010", "EV-010B"}
missing = required_ids - artifacts.keys()
if missing:
    fail(f"missing required Act 2 artifacts: {sorted(missing)}")

ev7 = artifacts.get("EV-007", {})
ev7_text = "\n".join(ev7.get("player_copy", []))
for required in (
    "管理区分番号を「08」とする。",
    "関係文書上の呼称を「第八避難区」とする。",
    "第1避難区から第7避難区までの区域変更は行わない。",
    "8月14日以降に受付した照会・相談案件",
):
    if required not in ev7_text:
        fail(f"EV-007 missing required semantic: {required}")

ev9 = artifacts.get("EV-009", {})
columns = ev9.get("columns", [])
if "現住所" not in columns or "管理区分" not in columns:
    fail("EV-009 must separate 現住所 and 管理区分 columns")

yui_rows = [
    row for row in ev9.get("rows", [])
    if len(row) >= 7 and row[1] == "水城 結"
]
if len(yui_rows) != 1:
    fail("EV-009 must contain exactly one visible 水城 結 row")
else:
    row = yui_rows[0]
    if row[2] != "1981-04-27":
        fail("水城 結 DOB mismatch in EV-009")
    if row[3] != "東三丁目12-4":
        fail("水城 結 current address must remain 東三丁目12-4")
    if row[4] != "第八":
        fail("水城 結 management classification must be 第八")

school_notice = "\n".join(artifacts.get("EV-006", {}).get("player_copy", []))
if "第八避難区対象者" not in school_notice:
    fail("school notice must use 第八避難区対象者")
if "第八避難区在住者" in school_notice:
    fail("school notice must not describe targets as 第八避難区在住者")

ledger = artifacts.get("EV-010", {}).get("person", {})
enrollment = artifacts.get("EV-010B", {}).get("person", {})
identity = data.get("puzzle_contracts", {}).get("PZ_004", {}).get("identity_keys", {})

for key, expected in (
    ("name", "水城 結"),
    ("dob", "1981-04-27"),
    ("guardian", "水城 真理子"),
):
    if ledger.get(key) != expected:
        fail(f"EV-010 identity mismatch: {key}")
    if enrollment.get(key) != expected:
        fail(f"EV-010B identity mismatch: {key}")
    if identity.get(key) != expected:
        fail(f"PZ-004 identity contract mismatch: {key}")

if ledger.get("address") != "凪代市東三丁目12-4":
    fail("EV-010 must confirm pre-event East Third address")
if enrollment.get("district") != "東三丁目":
    fail("EV-010B must confirm 1998 East Third district")
if identity.get("address") != "東三丁目12-4":
    fail("PZ-004 identity address mismatch")

seed = data.get("act3_seed", {})
if seed.get("date") != "1998-08-14":
    fail("Act 3 seed must be only the date 1998-08-14")
if seed.get("status") != "公開準備中":
    fail("Act 3 source must remain unrevealed in staging")

# Player-facing staging data must not leak later mechanism terms.
serialized = json.dumps(data, ensure_ascii=False)
for forbidden in (
    "33秒",
    "27秒",
    "共同記憶",
    "記述密度",
    "再構築",
    "現実改変",
    "受信カセット",
):
    if forbidden in serialized:
        fail(f"Act 2 staging leaks later mechanism term: {forbidden}")

# Date ordering invariants.
if not (
    date.fromisoformat("1998-08-14")
    < date.fromisoformat(by_number[215]["date"])
    < date.fromisoformat(by_number[216]["date"])
):
    fail("Act 2 document dates violate incident -> code -> revision ordering")

print(f"Artifacts: {len(artifacts)}")
print(f"Document sequence: {numbers}")
print("Identity keys: name / DOB / address / guardian")
print("Human-gate isolation: enabled")
print("Act 3 mechanism spoiler scan: enabled")

if errors:
    print("\nACT2 VALIDATION FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("ACT2 VALIDATION PASSED")
