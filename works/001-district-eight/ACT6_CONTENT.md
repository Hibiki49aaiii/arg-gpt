# 第八避難区 — ACT 6 CONTENT BIBLE

Status: Exact state / constraint draft
Earlier runtimes remain unlinked.

# 1. PZ-011 Candidate Graph

Candidate slots:

```text
S1 — S2 — S3 — S4 — S6
      |
      S5
```

Edges:
- S1-S2
- S2-S3
- S3-S4
- S4-S6
- S2-S5

Canonical assignment:

| Slot | Landmark |
|---|---|
| S1 | PARK |
| S2 | VENDING_MACHINE |
| S3 | BLUE_FENCE |
| S4 | OLD_EIGHT_MEETING_HALL |
| S5 | BUS_STOP |
| S6 | RESIDENTIAL_CLUSTER |

Nested:
ROUND_FOUNDATION inside PARK.

Named route after synthesis:
`水無坂 = S1-S2-S3-S4-S6`

# 2. Source Constraint Set

## G-01 — EV-018 / EV-020
Linear partial topology:
`PARK → VENDING_MACHINE → BLUE_FENCE → HALL`

Maps to four consecutive slots on main route.

## G-02 — EV-021
The candidate target road is the five-slot main route:
`S1-S2-S3-S4-S6`

Stable transport symbol gives a side spur at S2-S5.

No place name.

## G-03 — EV-005 + EV-018-C
Triangular-roof hall is cross-matched with 旧八号集会所.

Therefore:
HALL = OLD_EIGHT_MEETING_HALL.

## G-04 — Kiritani Distance Table
Graph-link distances:

| Pair | Distance |
|---|---:|
| PARK ↔ BUS_STOP | 2 |
| BUS_STOP ↔ OLD_EIGHT_MEETING_HALL | 3 |
| OLD_EIGHT_MEETING_HALL ↔ RESIDENTIAL_CLUSTER | 1 |
| PARK ↔ RESIDENTIAL_CLUSTER | 4 |

## G-05 — EV-023
Later phonebook preservation places household-style entries under 水無坂.
It supports RESIDENTIAL_CLUSTER on the named main route.

## G-06 — EV-016
Waterless-Slope home memory supports a residential endpoint beyond the public landmarks.

## G-07 — EV-013 / EV-016 / EV-023
Name synthesis:
audio term + diary term + phonebook heading
→ main route name `水無坂`.

# 3. Uniqueness Requirement

Allowed landmark cards:
- PARK
- VENDING_MACHINE
- BLUE_FENCE
- OLD_EIGHT_MEETING_HALL
- BUS_STOP
- RESIDENTIAL_CLUSTER

Allowed slots:
S1–S6.

Constraints G-01 through G-06 must produce exactly one assignment.

CI must enumerate all 6! assignments and assert solution count = 1.

# 4. Evidence Support Minimums

Required support counts:

| Landmark | Minimum independent support groups |
|---|---:|
| PARK | 2 |
| VENDING_MACHINE | 2 |
| BLUE_FENCE | 2 |
| OLD_EIGHT_MEETING_HALL | 2 |
| BUS_STOP | 2 |
| RESIDENTIAL_CLUSTER | 2 |
| 水無坂 route name | 3 |

Support groups should not count multiple pages from one identical source as independent.

# 5. EV-032 Generated Artifact

Title:
`第八避難区 / 水無坂周辺 — 統合復元図`

Metadata:

```text
artifact_type: generated synthesis
source_periods: 1998 / later archive copies / current investigation
complete_source_map_found: false
generated_during_investigation: true
```

Placement provenance:

### S1 PARK
Sources:
EV-018-A/B, EV-020.

### S2 VENDING_MACHINE
Sources:
EV-018-A/B/C, EV-020.

### S3 BLUE_FENCE
Sources:
EV-018-A/B/C, Kiritani normalized sketch.

### S4 OLD_EIGHT_MEETING_HALL
Sources:
EV-018-C, EV-005, Kiritani distance table.

### S5 BUS_STOP
Sources:
EV-021 transport symbol, Kiritani distance table.

### S6 RESIDENTIAL_CLUSTER
Sources:
EV-023, EV-016, Kiritani distance table.

### Route name 水無坂
Sources:
EV-013, EV-016, EV-023.

Required copy:

> この完成図と同一の資料は、現在確認されている1998年資料には存在しません。

> 各資料に分散していた位置関係を統合して作成したものです。

# 6. Runtime State Contract

Initial:
`MAP_INCOMPLETE`

After correct PZ-011:
`MAP_COMPLETE_UNOBSERVED`

Side effect:
reality adapter selects state B.

No player notification.

After visiting either:
- SITE-007 reality anchor
- SITE-001 /08

set:
`REALITY_CHANGE_OBSERVED`

PZ-012 requires checking both for full confirmation but one may trigger hint progression.

After both:
`PZ012_OBSERVED`

Then:
`ENDING_AVAILABLE`

# 7. SITE-007 State A Fixture

Path:
`/bousai-now/areas/`

Title:
`凪代市 防災・避難情報`

Last updated:
`2026-04-01`

Rows:
1–7 only.

Ordinary columns:
- 避難区
- 主な対象地域
- 指定避難拠点

No clue language.

# 8. SITE-007 State B Fixture

Same:
- path
- title
- header
- nav
- CSS
- last updated `2026-04-01`

Adds ordinary row:
`第8避難区`

Use a mundane designated site name in staging:
`水無坂地域センター`

Do not style differently.

Map legend:
1–8.

No “new/restored”.

# 9. SITE-001 /08 State A Fixture

Path:
`/old-bousai/disaster/areas/08/`

Copy aligned with existing Vertical Slice:
`保存ページを確認できません`

Requested path displayed normally.

# 10. SITE-001 /08 State B Fixture

Same old-site visual language.

Title:
`第8避難区｜旧凪代市防災情報`

Period-appropriate update:
`平成15年4月1日`

Content:
- 第8避難区
- 指定集合場所: 旧八号集会所
- ordinary evacuation notes
- no explanation of why page exists

Important:
the old page is too complete/normal for the player’s generated map to be mere discovery.

# 11. PZ-012 Player Copy

No popup.

After map completion, workspace says only:

> 統合復元図を保存しました。

Optional Hint 1:
> ここまでの資料と、最初に基準にしたページを比較してください。

Optional Hint 2:
> 現在の避難区一覧と、旧サイトの08ページをもう一度確認してください。

On observing current state B:
no special message.

On observing old /08 state B:
no special message.

Only after both, synthesis panel may show:

> これらのページは、復元図作成前に保存した基準状態と一致しません。

# 12. Baseline Evidence

Before PZ-011, freeze:
- SITE-007 state A fixture hash
- SITE-001 /08 state A fixture hash

After:
compare B hashes.

Player-facing baseline can be a browser-history/snapshot feature rather than a game HUD.

# 13. Final Recontextualization Copy

Allowed:

> 完全図を「見つけた」資料はない。

> 完全図を作成した後、完全図を前提とするページが現在側・過去側の両方で成立した。

> 記録と再想起の関係を考えると、調査そのものを無関係とは扱えない。

Do not claim a mathematically proven supernatural law.

# 14. Ending Choice Screen

Title:
`保存方針`

Intro:

> 統合復元図は、複数資料を横断して作成した新しい記録です。
> 保存範囲を選択してください。

Choices use action language only.

## A
`完全復元資料を公開状態で保持する`

## B
`復元キーと精密地理を破棄する`

## C
`人物記録を残し、精密地理を非公開化する`

No:
- Good / Bad / True
- recommended badge
- color moral coding

# 15. Ending Persistent States

## END-A
```text
people = full
incident = full
complete_geography = public
exact_audio = available
cross_index = full
site007 = B
site001_08 = B
```

Final implication:
search result count / cross-links increase.

## END-B
```text
people = mostly_redacted
incident = minimal
complete_geography = destroyed
exact_audio = removed
cross_index = removed
site007 = A
site001_08 = A
```

Final implication:
a remembered person/place becomes harder to verify.

## END-C
```text
people = preserved
incident = preserved
complete_geography = suppressed_or_destroyed
exact_audio = removed
cross_index = removed
site007 = A
site001_08 = A
```

Last line:
`忘れないために、思い出してはいけないことがある。`

# 16. Ending Mechanical Distinction

END-B and END-C must not be cosmetically identical.

Difference:
- END-B redacts most person records and reduces incident context
- END-C retains biographies and chronology

Tests must verify this distinction.

# 17. No-Glitch Tokens

Player-facing state-change HTML/CSS must not include:
- glitch
- anomaly alert
- danger
- warning red
- flicker
- scanline
- distortion
- jumpscare
- “new area”

Ordinary municipal/archive language only.
