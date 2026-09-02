# 第八避難区 — VERTICAL_SLICE

Status: Ready-for-Implementation Specification
Scope: Act 0 → Act 1 only

## 1. Vertical Slice Goal

初見プレイヤーが、説明なしで以下の認知変化を経験すること。

```text
古い自治体サイトだ
↓
少し欠番がある
↓
8という痕跡が複数ある
↓
古い行政資料に「第八避難区」と明記されている
↓
単なるサイト制作ミスではない
↓
第八避難区とは何だったのか調べたい
```

Slice終了時点で明かしてよい真相はここまで。

Do not reveal:
- 水城結の二重住所
- 33秒放送の詳細
- 共同記憶
- 記録媒介
- 三枝の最終判断
- player reconstruction hazard

---

# 2. Target Experience

Estimated playtime:
20–40 minutes first-time.

Primary emotion curve:
```text
Normality
→ Curiosity
→ Pattern recognition satisfaction
→ Doubt
→ Administrative unease
→ Voluntary investigation
```

Horror intensity:
1/6 to 2/6 only.

No:
- jumpscare
- screen takeover
- red warning text
- sudden loud audio
- “you are being watched”
- supernatural entity reveal

---

# 3. Entry

## Entry URL
SITE-001 root.

## Player-facing premise
A restored mirror of an old municipal disaster-information website.

Suggested restoration notice:

「旧凪代市防災情報ページの保存データを閲覧用に復元しています。リンク切れ、画像欠落、文字化け等は元データ由来のものを含みます。」

Important:
Do not say:
- ARG
- mystery
- investigate
- hidden clue
inside the in-world Trailhead.

The project meta/safety page remains separately reachable.

---

# 4. Page Contract

## VS-001 — SITE-001 Home

Purpose:
Establish normality and provenance.

Visible:
- old municipal heading
- disaster information
- update history
- archive restoration note
- links to evacuation districts
- documents

Ordinary content:
- typhoon guidance
- fire drill notice
- emergency bag list
- weather-related archived notice

Clue:
none required.

Exit:
VS-002 / VS-004.

Success:
player believes this is a coherent old-site archive.

---

## VS-002 — Evacuation District Index

URL concept:
`/disaster/areas/`

Visible:
- 第1避難区
- 第2避難区
- ...
- 第7避難区

Each has:
- area icon
- district name
- meeting point
- link

Clue layer:
shared filename/asset pattern.

Example conceptual pattern:
```text
img/area01.gif
img/area02.gif
...
img/area07.gif
```

Do not show:
`area08.gif` plainly in the page UI.

Subtle path:
source manifest / broken prefetch / backup listing can reveal 08.

Exit:
VS-003 / VS-004.

---

## VS-003 — District Detail 01–07

Purpose:
teach the site grammar.

Each page should share:
- title
- navigation
- icon pattern
- document naming pattern

At least 3 pages should contain normal internal references.

Reason:
player must learn a real pattern before noticing the missing value.

Do not make all seven pages identical filler.

---

## VS-004 — Archive / Backup Index

Purpose:
Recovery Route and first reliable anomaly.

Visible:
old backup entries.

Pattern:
```text
area01/
area02/
area03/
...
area07/
[missing entry / orphan reference]
```

Clue:
an orphan path, checksum entry, or manifest record implies `area08`.

Preferred:
two independent weak traces rather than one giant obvious clue.

Example:
- image reference ID 08
- archived path record with missing target

Output:
found_area08 = true.

This state should not visibly show a quest completion notice.

---

## VS-005 — /areas/08 Missing Page

Early state:
normal archive 404.

Text:
「指定された保存ページは復元データに含まれていません。」

No scary language.

Purpose:
confirms that 08 is intentionally interesting but not immediately available.

Navigation:
return to archive / documents.

---

## VS-006 — Document Library

Purpose:
Move player from URL anomaly to administrative evidence.

Visible:
several mundane documents.

Required documents:
- summer disaster plan
- water station list

Other filler:
- fire extinguisher inspection
- evacuation drill schedule
- shelter equipment inventory

Search:
document title / ID / year.

---

## VS-007 — 1998 Summer Disaster Plan

Evidence:
EV-004 / MED-007.

Surface:
8–12 page realistic PDF.

Important clue:
a low-key footnote/reference to:
「第八避難区対象者は別途指示」

Critical wording:
対象者.

At this stage the player likely reads it as:
people living in an 8th district.

Do not explain the wording.

Metadata:
source filename can support PZ-002.

---

## VS-008 — Water Station List

Evidence:
EV-005 / MED-008.

Visible row:
```text
第八避難区    旧八号集会所
```

This is the Vertical Slice reveal.

Why it works:
A single stray “08” could be a technical artifact.
Two administrative documents using the same district is harder to dismiss.

Output:
identified_eighth_district = true.

Next lead:
「旧八号集会所」

Search result on SITE-002:
0 direct exact-match result at first.

End emotion:
“I need to know what this was.”

---

# 5. Puzzles Included

## PZ-001 Missing Eight
Required.

Difficulty:
Very Easy / Easy.

Expected solve:
5–12 minutes.

Recovery:
backup index.

## PZ-002 Deleted File Provenance
Optional-but-rewarding in slice.

Expected:
players who inspect document details confirm `area08` as a distinct source file.

Should not block completion.

---

# 6. Recovery Routes

## Route A — Asset Pattern
Area pages → asset naming → 08 trace → archive.

## Route B — Backup Index
Update history / archive page → orphan backup reference → 08 trace.

## Route C — Document-first
Player ignores 08 clue and browses documents → finds EV-004 or EV-005 directly.

Important:
Route C prevents a player who does not inspect HTML/source-like details from stalling.

Core Slice completion requires:
EV-004 + EV-005, not PZ-001 mechanical completion.

---

# 7. Narrative State

Minimal states:

```text
visited_area_index
found_area08
opened_plan_pdf
opened_water_list
identified_eighth_district
```

Rules:
- order-independent where possible
- opening EV-004/005 directly still works
- state does not alter document content during Act 0–1
- no late-game reality-change behavior in slice

---

# 8. Analytics Events

Privacy-minimal anonymous events:

```text
vs_entry
area_index_viewed
district_page_viewed
archive_index_viewed
area08_trace_seen
missing08_page_opened
document_library_viewed
plan_pdf_opened
water_list_opened
eighth_district_confirmed
vs_exit
```

Properties:
- route
- device class
- elapsed bucket
- hint/recovery route if any

Do not capture:
- typed unrelated search contents unless necessary
- personal identifiers

---

# 9. Accessibility

## Keyboard
Every link and document viewer accessible by keyboard.

## Mobile
No puzzle requires:
- view-source browser feature
- desktop-only devtools
- external PDF editor

Any “metadata” clue appears through an in-world document-information UI.

## Images
Clue does not depend solely on tiny unreadable pixels.

## PDF
Provide semantic accessible text layer where compatible with puzzle fairness.

## Cognitive
At least 2 paths to key conclusion.

---

# 10. Visual Direction

## SITE-001
Old, ordinary, bureaucratic.

Palette:
not defined here; implementation should derive period-appropriate neutral municipal aesthetic.

Avoid:
- pure black horror site
- blood red accent
- glitch typography
- scanline overlay

## PDF
Should look like actual internal/public administrative material:
- consistent numbering
- dates
- department
- headers/footers
- revision marks where appropriate

But:
do not copy a real municipality template exactly.

---

# 11. Content Authenticity Checklist

Before implementation sign-off:

- 1998 terminology plausible
- PDF creation metadata aligns with archive history
- document IDs consistent
- no references to technologies unavailable in 1998 source documents
- restored website layer may be 2002–2004, but underlying documents remain 1998
- address/place names internally consistent
- 第八区 code origin is not accidentally dated before 1998-08-19 in documents that imply formal code creation

Important nuance:
EV-004/EV-005 may contain later annotations or post-incident revisions.
If a document is dated before 1998-08-19, it must not present the formal administrative code as already established unless the artifact’s revision history explicitly explains it.

---

# 12. Critical Timeline Fix for Slice

The existing concept says:
- Incident: 1998-08-14
- Administrative code created: 1998-08-19

Therefore:
Any Act 1 administrative document showing “第八避難区” must be one of:

A. created/revised on or after 1998-08-19, or
B. an earlier base document with an explicit post-8/19 revision/addendum.

Recommended:
- Summer Disaster Plan base: 1998-07
- revised appendix: 1998-08-20
- Water Station List revision: 1998-08-20

This prevents a direct contradiction with T0-04.

---

# 13. Slice Ending

Do not display:
“ACT 1 COMPLETE”.

Instead, after EV-005:
the ordinary document library offers a search field or linked term:
「旧八号集会所」

Exact search:
0 results.

Partial/fuzzy routes:
lead to the next phase once Act 2 is implemented.

For the Vertical Slice standalone build:
show ordinary archive text such as:
「該当する公開資料はありません。」

This creates unresolved tension.

---

# 14. Blind Playtest Tasks

Do not tell testers what to find.

Prompt:
「この復元サイトを自由に見てください。気になることがあれば調べて構いません。」

Observe:
- first anomaly noticed
- whether 08 is recognized
- whether player believes it is a bug
- whether documents are opened
- whether “第八避難区” is independently identified
- whether player wants to continue

---

# 15. Acceptance Criteria

## AC-VS-001
80%+ of testers reach EV-004 or EV-005 without explicit puzzle instructions.

## AC-VS-002
60%+ identify “第八避難区” as the central anomaly within 30 minutes.

## AC-VS-003
No tester needs browser devtools.

## AC-VS-004
At least one recovery route is naturally used by testers who miss the primary 08 trail.

## AC-VS-005
No Act 2+ core truth is correctly stated solely from slice because of an accidental spoiler.

## AC-VS-006
Mobile tester can complete the slice.

## AC-VS-007
Keyboard-only route reaches the same narrative endpoint.

## AC-VS-008
The final player question is approximately:
「第八避難区は何だったのか？」
not:
「この暗号の次の答えは何？」

---

# 16. Implementation Order

1. Freeze naming decision
2. Build SITE-001 shell
3. Build ordinary district pages 01–07
4. Build archive/backup index
5. Build normal 08 missing state
6. Produce MED-007 disaster-plan PDF
7. Produce MED-008 water-list PDF
8. Build document viewer / metadata UI
9. Build SITE-002 minimal document-search shell
10. Add state + analytics
11. Accessibility pass
12. automated link/state tests
13. blind playtest
14. revise before Act 2 implementation

---

# 17. Definition of Done

Vertical Slice is done when a player can start from a normal-looking archived disaster website and, through their own investigation, arrive at convincing evidence that an erased “第八避難区” existed in administrative records—while still having no reliable explanation for what it actually was.
