# 第八避難区 — ACT 6 IMPLEMENTATION

Status: Preproduction
Act: 6 — The Missing Whole / Seven Became Eight / Endings
Human Gate: Act 0–1 Issue #8 pending

## 1. Purpose

Act 6で最後に反転させるものは「真犯人」ではない。

プレイヤーがここまでしてきた行為そのものを再定義する。

Before:
> 欠けた資料を探し、過去の真相を復元している。

After PZ-011 / PZ-012:
> 誰も持っていなかった完全な地理を、プレイヤー自身が初めて生成した。
> その生成後に、現在と過去の基準ページが“最初からそうだった”形へ整合した。

## 2. Entry Knowledge

Act 5終了時:

- shared nonexistent geography exists in memory
- later records increasingly contain compatible geography
- higher description density correlates with later new recall
- suppression coincides with decline
- Saegusa reversed from preservation to deletion
- exact mechanism remains unknown

The player now has enough partial spatial constraints to combine all sources.

## 3. PZ-011 — The Missing Whole

Difficulty: 5

### Design Principle

There is no hidden complete map file.

No:
- secret 1998 master map
- complete Saegusa scan
- complete Kiritani diagram
- one final PDF with all answers

The complete map is a generated artifact whose individual placements store provenance.

## 4. Candidate Geography Graph

EV-021’s registered target road provides a normalized topology with six candidate slots.

```text
S1 — S2 — S3 — S4 — S6
      |
      S5
```

Interpretation only after solve:
- S1 Park
- S2 Vending machine
- S3 Blue fence
- S4 Old Eighth Meeting Hall
- S5 Bus stop
- S6 Residential cluster

Named road:
the S1→S2→S3→S4→S6 route becomes the reconstructed `水無坂`.

Important:
the name is applied by synthesis from independent evidence.
EV-021 itself never labels the road.

## 5. Fixed Placements from Act 4

PZ-007 already establishes:

```text
Park → Vending → Blue Fence → Hall
```

Within PZ-011 candidate graph, this maps onto:

```text
S1 → S2 → S3 → S4
```

Round Foundation is nested in Park/S1.

This uses:
- EV-018 drawings
- EV-020 essay
- Partial Map v1

## 6. Hall Identity

EV-018 only establishes a triangular-roof hall.

EV-005 establishes:
`旧八号集会所`

Act 6 cross-match:
- EV-005 facility description / roof form
- EV-018-C triangular-roof structure
- Kiritani distance-table reference to 「旧集会所」

Result:
S4 = `旧八号集会所`.

No earlier Act needs to state this identity explicitly.

## 7. Kiritani Distance Table

This previously named-but-unfixed input is now canonical.

Table unit:
graph-link distance, derived from interview sketch normalization.
Not meters.

```text
公園 ↔ 停留所          = 2 links
停留所 ↔ 旧集会所      = 3 links
旧集会所 ↔ 住宅群      = 1 link
公園 ↔ 住宅群          = 4 links
```

Given candidate graph:
- S5 uniquely satisfies Bus Stop
- S6 uniquely satisfies Residential cluster

The validator must enumerate permutations and prove uniqueness.

## 8. Additional Placement Support

### Park / S1
Supports:
- EV-018-A/B
- EV-020
- EV-016 memory reference

### Vending / S2
Supports:
- EV-018-A/B/C
- EV-020

### Blue Fence / S3
Supports:
- EV-018-A/B/C
- Kiritani normalized sketch notes

### Old Eighth Meeting Hall / S4
Supports:
- EV-018-C
- EV-005
- Kiritani distance table

### Bus Stop / S5
Supports:
- EV-021 stable transport symbol near target road
- Kiritani distance table

### Residential Cluster / S6
Supports:
- EV-023 later phonebook heading/addresses
- Kiritani distance table
- EV-016 home-memory material

### Waterless Slope Route
Supports:
- EV-013 audio term
- EV-016 diary
- EV-021 target road geometry
- EV-023 phonebook heading

Every major landmark must retain 2+ routes in machine data.

## 9. EV-032 — Generated Map Artifact

On solve, create a structured artifact:

```text
第八避難区 / 水無坂周辺 — 統合復元図
status: player-generated synthesis
source count: N
created during current investigation
```

Each placement contains:
- slot
- landmark
- source IDs
- relation basis
- confidence

Critical player-facing copy:

> この完成図と同一の資料は、現在確認されている1998年資料には存在しません。

> 各資料に分散していた位置関係を統合して作成したものです。

Do not say “found”.

## 10. PZ-011 Recovery

Every major landmark has 2+ sources.

Hints:
1. “資料ごとに完成図があるわけではない。”
2. “同じランドマークを複数資料の接点として使う。”
3. “距離表は絶対座標ではなく候補Slotの除外に使う。”

Accessibility:
- candidate-slot dropdowns
- keyboard
- relation table
- evidence provenance table
- no color-only distinction

## 11. State Machine

```text
MAP_INCOMPLETE
  |
  | PZ-011 solved
  v
MAP_COMPLETE_UNOBSERVED
  |
  | reality adapter selects state B
  | no popup / no notification
  v
REALITY_B_ACTIVE
  |
  | player revisits reality anchors
  v
PZ012_OBSERVED
  |
  v
ENDING_AVAILABLE
```

The state change occurs after PZ-011.
The player is not told where to look until a subtle “最初のページを確認する” hint is requested.

## 12. SITE-007 Reality Fixture

SITE-007 is not currently implemented in the existing Vertical Slice.
Act 6 staging therefore creates frozen fixture states.

### State A — Baseline
Same modern municipal UI.

Shows:
- 第1〜第7避難区
- 防災map
- shelter search

Update date:
use one ordinary fixed date shared with State B, e.g. `2026-04-01`.

### State B — After PZ-011
Same pathname.
Same header.
Same CSS.
Same update date.
Same ordinary language.

Difference:
- 第8避難区 row exists
- map legend includes 8
- 第8 page resolves normally

No:
- “new”
- “restored”
- warning
- animation
- glitch
- red text
- current timestamp

## 13. SITE-001 /08 Fixture

Use the same old-site visual system as the Vertical Slice.

### State A
`/old-bousai/disaster/areas/08/`
ordinary “保存ページを確認できません” state.

### State B
same path resolves as a normal 2003-era district page.

Old timestamp:
ordinary period-appropriate date.
Do not use current date or “復元成功”.

This supports EV-034.

## 14. PZ-012 — Seven Became Eight

Difficulty:
1 observational / 4 interpretive.

Mechanical action:
revisit a page the player already used as baseline.

Correct observation:
- baseline had 7
- now same reality anchor has 8
- old /08 also resolves

Required interpretation:
the new map was not merely describing an already-complete hidden map.

Combined with EV-025/029:
the investigation’s act of assembling a complete representation is itself implicated.

Final Story Reveal:
`調査 = 再構築` is now a supported explanation.

Do not present a supernatural narrator confirming it.
The evidence state change is the confirmation.

## 15. No-Glitch Contract

Forbidden in Act 6 state change:
- glitch CSS
- flicker
- chromatic aberration
- scanline effect
- red warning
- “ANOMALY DETECTED”
- jumpscare audio
- automatic scroll
- modal alert

Horror source:
normality.

## 16. Ending Gate

Endings are unavailable until:
- PZ-011 solved
- PZ-012 change observed

Do not allow choosing before the player understands the reconstruction hazard.

## 17. END-A — REMEMBER

Player action:
publish/retain the complete reconstruction package.

Persistent:
- generated complete map retained
- precise geography searchable
- SITE-007 remains State B
- SITE-001 /08 remains State B
- full cross-index retained
- exact high-quality evidence may remain available

Implication:
search/result coverage continues increasing.

Cost:
preserves maximum evidence and people/place detail, but maximizes recurrence risk.

No label:
“bad ending”.

## 18. END-B — FORGET

Player action:
destroy reconstruction key and precise linked package.

Persistent:
- complete map unavailable
- precise geography suppressed
- /08 returns State A/missing
- SITE-007 returns State A/7
- names become mostly redacted in the reconstructed package
- exact audio unavailable

Implication:
containment strongest, but documentary identity is damaged.

Cost:
reduces risk at the price of erasing people/context.

No label:
“good ending”.

## 19. END-C — INCOMPLETE

Player action:
preserve people/incident history while suppressing precise geography and high-risk cross-links.

Persistent:
- biographies/person records remain
- incident chronology remains
- precise geography hidden
- complete map destroyed/not published
- exact high-quality audio unavailable
- cross-linked name/place index unavailable
- SITE-007 settles to State A/7
- SITE-001 /08 settles to missing
- no normalization of 第八区

Last line:
`忘れないために、思い出してはいけないことがある。`

Cost:
accepts incomplete truth as a containment boundary.

No label:
“true ending” / “correct ending”.

## 20. Ending Choice UX

Present actions, not moral labels.

Example buttons:
- `完全復元資料を公開状態で保持する`
- `復元キーと精密地理を破棄する`
- `人物記録を残し、精密地理を非公開化する`

Before action, show a state matrix of what each preserves/removes.

No confirmation wording that hints one is recommended.

## 21. Ending Persistence Matrix

| State | END-A | END-B | END-C |
|---|---|---|---|
| People biographies | Full | Mostly redacted | Preserved |
| Incident chronology | Full | Minimal | Preserved |
| Complete geography | Public | Destroyed | Suppressed/destroyed |
| Exact audio | Available | Removed | Removed |
| Cross index | Full | Removed | Removed |
| SITE-007 | B / 8 | A / 7 | A / 7 |
| SITE-001 /08 | B / exists | A / missing | A / missing |

All three must be mechanically distinct.

## 22. Human Gate Isolation

Act 6 staging remains isolated while Issue #8 is open.

Do not mutate the existing Act 0–1 Vertical Slice files during staging.
Use fixtures / state adapters.

Runtime integration is a separate future gate.

## 23. Definition of Done

Act 6 preproduction is complete when:
- PZ-011 constraint system has exactly one solution
- generated artifact provenance is defined
- State A/B fixtures have strict structural-diff rules
- PZ-012 recheck is defined
- ending gate and persistence matrix are defined
- no ending is authorially privileged
- staging can be implemented without inventing causality or state semantics.
