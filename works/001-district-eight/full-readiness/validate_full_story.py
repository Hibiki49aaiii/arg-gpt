#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
errors: list[str] = []

def fail(msg: str) -> None:
    errors.append(msg)

def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"cannot load {path.relative_to(REPO)}: {exc}")
        return {}

acts = {}
for n in range(2, 7):
    p = ROOT / f"implementation/act{n}-staging/content.json"
    if not p.exists():
        fail(f"missing Act {n} content contract")
        acts[n] = {}
    else:
        acts[n] = load_json(p)

# ---------------------------------------------------------------------------
# Required staging / validator presence
# ---------------------------------------------------------------------------
required_paths = [
    ROOT / "implementation/vertical-slice/README.md",
    ROOT / "implementation/vertical-slice/validate.py",
]
for n in range(2, 7):
    required_paths.extend([
        ROOT / f"implementation/act{n}-staging/README.md",
        ROOT / f"implementation/act{n}-staging/content.json",
        ROOT / f"implementation/act{n}-staging/validate_act{n}.py",
    ])
for p in required_paths:
    if not p.exists():
        fail(f"required readiness artifact missing: {p.relative_to(REPO)}")

# ---------------------------------------------------------------------------
# Isolation / naming lock
# ---------------------------------------------------------------------------
for n in range(2, 7):
    if acts[n].get("status") != "staging-unlinked":
        fail(f"Act {n} must remain staging-unlinked")
    if acts[n].get("runtime_connected") is not False:
        fail(f"Act {n} runtime_connected must remain false")

if acts[2].get("municipality") != "凪代市":
    fail("Act 2 municipality naming lock mismatch")

# Scan current player-facing/production source, excluding validators because
# validators intentionally contain retired-name sentinels.
scan_ext = {".md", ".html", ".js", ".json", ".css"}
legacy_terms = ("久代市", "久代東中学校", "kushiro-east-alumni")
legacy_hits: list[str] = []
for p in ROOT.rglob("*"):
    if not p.is_file() or p.suffix not in scan_ext:
        continue
    if p.name.startswith("validate") or "full-readiness" in p.as_posix():
        continue
    text = p.read_text(encoding="utf-8")
    for term in legacy_terms:
        if term in text:
            legacy_hits.append(f"{p.relative_to(REPO)}: {term}")
if legacy_hits:
    for hit in legacy_hits:
        fail(f"legacy naming remains: {hit}")

# ---------------------------------------------------------------------------
# Cross-act chronology
# ---------------------------------------------------------------------------
act2 = acts[2]
seq = {x.get("number"): x for x in act2.get("document_sequence", [])}
code_date = seq.get(215, {}).get("date")
act3_seed = act2.get("act3_seed", {}).get("date")
if code_date != "1998-08-19":
    fail("Act 2 formal code date must remain 1998-08-19")
if act3_seed != "1998-08-14":
    fail("Act 2 → Act 3 seed must remain 1998-08-14")
if code_date and act3_seed and not date.fromisoformat(act3_seed) < date.fromisoformat(code_date):
    fail("incident/seed must precede formal code creation")

act3 = acts[3]
incident_date = act3.get("incident", {}).get("date")
chron = act3.get("chronology", {})
if incident_date != act3_seed:
    fail("Act 2 seed date and Act 3 incident date diverge")
if chron.get("phrase_received") != "1998-08-14":
    fail("Act 3 phrase-received date mismatch")
if chron.get("formal_code_created") != code_date:
    fail("Act 3 formal-code date diverges from Act 2 document 215")
if not date.fromisoformat(chron["phrase_received"]) < date.fromisoformat(chron["formal_code_created"]):
    fail("Act 3 phrase must predate management-code creation")

sender = act3.get("incident", {}).get("sender", {})
receiver = act3.get("incident", {}).get("receiver_window", {})
if sender.get("duration_seconds") != 27 or receiver.get("duration_seconds") != 60 or receiver.get("surplus_seconds") != 33:
    fail("Act 3 27/60/33 timing invariant changed")

# ---------------------------------------------------------------------------
# Act 3 → Act 4 memory onset
# ---------------------------------------------------------------------------
act4 = acts[4]
if act3.get("act4_lead", {}).get("search_term") != "水無坂":
    fail("Act 3 → Act 4 lead must remain 水無坂")
if act4.get("incident_date") != incident_date:
    fail("Act 4 incident date diverges from Act 3")

frags = act4.get("diary", {}).get("fragments", [])
pre = [x for x in frags if x.get("date", "") < "1998-08-14"]
if any("水無坂" in x.get("text", "") for x in pre):
    fail("Act 4 pre-8/14 diary contains 水無坂")
d04 = next((x for x in frags if x.get("id") == "D-04"), {})
if d04.get("date") != "1998-08-14" or "水無坂" not in d04.get("text", ""):
    fail("Act 4 D-04 must be the 8/14 onset")
if act4.get("partial_map", {}).get("complete") is not False:
    fail("Act 4 map must remain partial before Act 6")

# ---------------------------------------------------------------------------
# Act 4 → Act 5 → Act 6 spoiler boundary
# ---------------------------------------------------------------------------
if act4.get("act5_lead", {}).get("label") != "旧市街地図Collection":
    fail("Act 4 → Act 5 lead mismatch")

act5 = acts[5]
boundary = act5.get("act6_boundary", {})
for key in (
    "complete_map_created",
    "player_causality_revealed",
    "current_municipal_area8_revealed",
    "ending_choice_revealed",
):
    if boundary.get(key) is not False:
        fail(f"Act 5 leaks Act 6 boundary: {key}")

containment = act5.get("containment", {})
if containment.get("order", {}).get("date") != "1998-09-03":
    fail("Act 5 containment order date must remain 1998-09-03")
if containment.get("trend", {}).get("correlation_only") is not True:
    fail("Act 5 containment trend must remain correlation-only")

# ---------------------------------------------------------------------------
# Act 6 generated-vs-found / gate
# ---------------------------------------------------------------------------
act6 = acts[6]
artifact = act6.get("generated_artifact", {})
if artifact.get("id") != "EV-032":
    fail("Act 6 generated artifact must remain EV-032")
if artifact.get("artifact_type") != "generated synthesis":
    fail("Act 6 map must remain a generated synthesis")
if artifact.get("complete_source_map_found") is not False:
    fail("Act 6 must not contain a found complete source map")
if artifact.get("generated_during_investigation") is not True:
    fail("Act 6 map must be generated during current investigation")
if act6.get("constraints", {}).get("solution_count_required") != 1:
    fail("Act 6 constraint system must require exactly one solution")
if act6.get("human_gate", {}).get("issue") != 8:
    fail("Human Gate must remain Issue #8")
if act6.get("human_gate", {}).get("required_before_runtime_integration") is not True:
    fail("Human Gate #8 must remain required before runtime integration")

# ---------------------------------------------------------------------------
# Documentation readiness
# ---------------------------------------------------------------------------
status_doc = ROOT / "FULL_STAGING_STATUS.md"
if not status_doc.exists():
    fail("FULL_STAGING_STATUS.md missing")
else:
    status_text = status_doc.read_text(encoding="utf-8")
    for required in (
        "Act 0–1",
        "Act 2",
        "Act 3",
        "Act 4",
        "Act 5",
        "Act 6",
        "Issue #8",
        "Human Blind Playtest",
        "唯一のNarrative Release Gate",
    ):
        if required not in status_text:
            fail(f"FULL_STAGING_STATUS.md missing status marker: {required}")

readme = (REPO / "README.md").read_text(encoding="utf-8")
if "FULL_STAGING_STATUS.md" not in readme:
    fail("README does not link FULL_STAGING_STATUS.md")

plan = (ROOT / "IMPLEMENTATION_PLAN.md").read_text(encoding="utf-8")
for required in (
    "Act 0〜6 Staging",
    "Human Blind Playtest",
    "Issue #8",
    "Engineering Readiness",
):
    if required not in plan:
        fail(f"IMPLEMENTATION_PLAN status is stale: missing {required}")

print("Acts loaded: 2 / 3 / 4 / 5 / 6")
print(f"Required readiness artifacts: {len(required_paths)}")
print("Legacy production-name scan: clean")
print("Cross-act chronology: 8/14 → 8/19 enforced")
print("Act 3 timing: 27 / 60 / 33 enforced")
print("Act 4 pre-incident 水無坂: 0")
print("Act 5 → Act 6 spoiler boundary: enforced")
print("Act 6 generated-vs-found invariant: enforced")
print("Human Gate: Issue #8")
print("Engineering readiness documentation: synchronized")

if errors:
    print("\nFULL READINESS VALIDATION FAILED")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("FULL READINESS VALIDATION PASSED")
