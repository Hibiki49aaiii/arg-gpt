# 第八避難区 — SITE_MAP

Status: Production Specification
Domain names in this document are placeholders only.
Do not deploy the literal placeholder hostnames.

## 0. Naming / Fiction Boundary

Current municipality name:
「久代市」は制作上の仮称。

Public release requirement:
- 実在自治体と誤認されにくい名称を最終確認する
- 全サイト群に統一されたFiction boundaryを用意する
- ただし各in-worldページの没入を壊す位置に大きなゲームUIは置かない
- Legal / safety pageから明確にフィクション作品だと確認可能にする

Placeholder base:
`*.district8.example.invalid`

---

# 1. Global Site Graph

```text
External Trailhead
        |
        v
SITE-001 旧防災情報ミラー
  |         |            \
  |         |             \--> SITE-005 地域ラジオ保存会
  |         |
  |         +--> SITE-002 市史料アーカイブ
  |                    |          \
  |                    |           \--> SITE-006 研究資料ミラー
  |                    |
  |                    +--> SITE-003 学校同窓資料室
  |
  +--> SITE-004 三枝個人サイト
                 |
                 +--> SITE-006
                 |
                 +--> SITE-005

All evidence branches
        |
        v
PZ-011 complete map
        |
        +--> SITE-007 現行防災ページ changes
        |
        +--> SITE-001 district08 page appears
        |
        v
Ending Layer
```

---

# 2. SITE-001 — 旧久代市防災情報ミラー

## Role
Primary Trailhead / Act 0–1 / Act 6 callback.

## Placeholder Host
`old-bousai.district8.example.invalid`

## Owner Persona
2026年の匿名アーカイブ復元者。

## Surface Design
2002〜2004年頃の自治体サイトを復元したような構成。

Key visual rules:
- 固定幅レイアウト寄り
- テーブルベース風だが実装はsemantic HTML
- 小さなGIF風アイコン
- 過度なCRT/glitchなし
- 「怖いサイト」ではなく「古い普通のサイト」

## Pages

### S1-001 /
復元ミラー説明。
更新履歴。
「一部リンク切れがあります」。

Clues:
- backup date
- source archive name

### S1-002 /disaster/
防災情報トップ。

### S1-003 /disaster/areas/
避難区一覧 01〜07。

Primary Evidence:
EV-001。

### S1-004 /disaster/areas/01 ... 07
各区の普通のページ。
PZ-001用の共通asset規則。

### S1-005 /documents/1998-summer-plan
EV-004。

### S1-006 /documents/water-stations
EV-005。

### S1-007 /archive/index
asset / backup index。
EV-002 / EV-003。

### S1-008 /disaster/areas/08
Act 0–5:
404 / missing archive response.

Act 6:
普通の古い自治体ページとして出現。
EV-034。

## Exit Routes
- 文書番号 → SITE-002
- 旧八号集会所 → SITE-002
- 1998-08-14 → SITE-005
- 水城結 → SITE-003

## Recovery
PZ-001に失敗しても、
- backup index
- PDF metadata
からAct 1へ進める。

---

# 3. SITE-002 — 久代市史料デジタルアーカイブ

## Role
Administrative / historical evidence.
Acts 1–5。

## Placeholder Host
`archives.district8.example.invalid`

## Owner Persona
郷土資料デジタル化事業。

## Design
2010年代後半の公共アーカイブ風。
SITE-001より新しい。
検索UI、資料ID、サムネイル、PDF viewer。

## Information Architecture

### S2-001 /
Search / categories。

### S2-002 /collections/disaster-1998
平成10年度防災資料群。

Contains:
- EV-007
- EV-008
- EV-009
- EV-015

### S2-003 /maps/
年代別地図。

Contains:
EV-021。

### S2-004 /photographs/
市街地写真。

Contains:
EV-022。

### S2-005 /directories/
電話帳・住所索引。

Contains:
EV-023。

### S2-006 /council/
議事録／会議要旨。

Puzzle:
PZ-003 document number gap。

## Search Behavior
Searchable fields:
- title
- document ID
- date
- department
- keyword

Important:
「第八避難区」で最初から全重要資料が出ない。

Reason:
1998年の抑制処理でkeyword indexが欠落。

Player must use:
- document ID
- dates
- person names
- old facility names

## Horror Beat
Act 4–5で同じ資料IDのthumbnailとPDF本体に微差がある。
演出は1回だけ。
Final truthはこれに依存しない。

---

# 4. SITE-003 — 久代東中学校 同窓資料室

## Role
Humanize the event.
Acts 2–4。

## Placeholder Host
`kushiro-east-alumni.district8.example.invalid`

## Owner Persona
卒業生有志の非公式資料室。

## Design
個人運営の学校同窓サイト。
2008〜2013年頃のブログ/CMS感。

## Pages

### S3-001 /
学校史 / 卒業年度リンク。

### S3-002 /1998/
1998年度関連。

### S3-003 /students/yui-mizuki
公開上は個人情報配慮で完全プロフィールにはしない。
卒業アルバム断片へ繋ぐ。

Evidence:
EV-010。

### S3-004 /documents/summer-notice
EV-006。

### S3-005 /special-collection/drawings
EV-018。

### S3-006 /archive/essays
EV-020。

### S3-007 /mizuki-diary/
水城家から寄贈された日記という設定。

Evidence:
EV-016 / EV-017。

Puzzle:
PZ-006 diary ordering。

## Emotional Function
ここは恐怖サイトにしない。
水城の生活、
友人、
部活、
普通の夏休みを十分見せる。

目的:
「Evidenceとしての少女」ではなく人間として感じさせる。

---

# 5. SITE-004 — 個人サイト「記録庫・三枝」

## Role
Whistleblower route / moral core.
Acts 1–6。

## Placeholder Host
`saegusa-log.district8.example.invalid`

## Owner
三枝冬一。

## Historical Layers
同一サイトの複数保存時点を持たせる。

- 2001 snapshot
- 2005 snapshot
- 2007 snapshot
- 2008 deletion phase
- 2009 final state

## Design
初期個人ホームページ。
手打ちHTML感。
テキスト中心。

No horror styling.

## Pages

### S4-001 /
「個人的な記録保存」。

### S4-002 /missing/
欠番資料。

### S4-003 /memo/1999
EV-028。

### S4-004 /memo/2007
EV-029。

### S4-005 /deleted/
2008年のリンク切れ一覧。
EV-030。

### S4-006 /last/
直接リンクなし。
PZ-010後に見つかる。
EV-031。

## Critical UX
プレイヤーに「三枝は正義の内部告発者」という愛着を持たせてから、
自発的削除の事実を見せる。

---

# 6. SITE-005 — 久代地域ラジオ保存会

## Role
Independent technical evidence.
Act 3。

## Placeholder Host
`radio-archive.district8.example.invalid`

## Owner Persona
地域放送・録音保存の趣味団体。

## Design
2020年代の小規模文化アーカイブ。
音声プレイヤー中心。

## Pages

### S5-001 /
保存会概要。

### S5-002 /1998-08-14
当日の受信録音。

Contains:
EV-012 / EV-013。

### S5-003 /equipment
当時の録音機器・受信方式。

Purpose:
Audio provenance。

### S5-004 /interviews/katase
片瀬の後年インタビュー。
EV-014補助。

### S5-005 /digitization-notes
高瀬章子のデジタル化記録。

## Puzzle
PZ-005 33 Seconds。

## Recovery
Audio failure時:
- 波形
- transcript fragments
- duration data
で主要推論可能。

---

# 7. SITE-006 — 共同記憶研究資料ミラー

## Role
Scientific model / Act 5。

## Placeholder Host
`memory-study.district8.example.invalid`

## Owner Persona
閉鎖研究室資料のミラー。

## Design
大学研究室の静的資料ページ風。
PDF index。

## Pages

### S6-001 /
研究室概要。

### S6-002 /kiritani/
桐谷宗一 bibliography。

### S6-003 /notes/a
EV-024。

### S6-004 /notes/index
引用・ページ索引。

PZ-009。

### S6-005 /notes/density
EV-025。
直接ナビには出さないが、謎が解ければ到達可能。

### S6-006 /containment/
EV-026 / EV-027。

## Narrative Rule
ここを「答え合わせサイト」にしない。

桐谷資料だけでは、
- なぜ33秒が発生したか
- 第八区の完全地理
- 三枝の最終判断
- プレイヤーによる再構築
は説明できない。

---

# 8. SITE-007 — 現行久代市防災ページ

## Role
Reality Anchor / final horror.

## Placeholder Host
`bousai-now.district8.example.invalid`

## Act 0 State
Completely normal modern municipal page.

Shows:
- 第1〜第7避難区
- 防災マップ
- 避難所検索

Do not:
- place clues everywhere
- use horror copy
- hint that this is special

## Act 6 State
After PZ-011 complete map:
- 第8避難区が普通の項目として追加
- map legend includes 8
- no warning
- no animation
- no glitch

EV-033。

## Strong Horror Detail
プレイヤーが第8項目を開くと、
「最終更新: 2026年○月○日」
ではなく、他地区と同じ通常更新日。

意味:
システム上「今追加された」のではなく、
最初からそうだったように整合している。

---

# 9. Ending Layer

This does not need a separate visibly game-like domain.

## END-A REMEMBER
Action:
完全資料を公開状態にする。

Persistent states:
- SITE-001 /08 exists
- SITE-007 area08 exists
- 三枝資料 full index appears

Last implication:
検索結果件数が増えている。

## END-B FORGET
Action:
reconstruction keyを破棄。

Persistent states:
- /08 returns missing
- map incomplete
- names mostly redacted

Last implication:
水城の日記ページから固有地名が一つ減る。

## END-C INCOMPLETE
Action:
人物の記録を保存し、地理再構成情報だけ非公開化。

Persistent states:
- biography / incident archive remains
- exact audio unavailable
- map stays incomplete
- 第8区 itself does not normalize

Last line:
「忘れないために、思い出してはいけないことがある。」

---

# 10. Cross-Site Lead Matrix

| From | Clue | To | Required? | Recovery |
|---|---|---|---|---|
| SITE-001 | document ID | SITE-002 | Yes | backup index |
| SITE-001 | 水城結 | SITE-003 | Yes | SITE-002対象者一覧 |
| SITE-001 | 8/14 | SITE-005 | Yes | 三枝memo |
| SITE-002 | 三枝名 | SITE-004 | No early / Yes late | SITE-006 citation |
| SITE-003 | 33秒日付 | SITE-005 | No | SITE-001 |
| SITE-004 | 桐谷引用 | SITE-006 | Yes | SITE-002 council |
| SITE-005 | 研究協力者 | SITE-006 | Recovery | SITE-004 |
| SITE-006 | 地図記述 | SITE-002 | Yes | SITE-003 drawings |
| all | landmarks | PZ-011 | Yes | duplicated evidence |
| PZ-011 | state change | SITE-007 | Yes | direct final prompt |

---

# 11. Page Count Budget

| Site | Core Pages | Optional Pages | Total Target |
|---|---:|---:|---:|
| SITE-001 | 8 | 5 | 13 |
| SITE-002 | 6 | 8 | 14 |
| SITE-003 | 7 | 5 | 12 |
| SITE-004 | 6 | 4 | 10 |
| SITE-005 | 5 | 3 | 8 |
| SITE-006 | 6 | 3 | 9 |
| SITE-007 | 3 | 2 | 5 |
| Ending/shared | 2 | 1 | 3 |
| Total | 43 | 31 | 74 max |

MVP/full release target:
40〜55 meaningful pages。
Optional flavor pagesは必要に応じ削る。

---

# 12. Technical Packaging Proposal

Repository future structure:

```text
works/001-district-eight/
├─ design/
├─ content/
│  ├─ evidence/
│  ├─ characters/
│  └─ copy/
├─ sites/
│  ├─ old-bousai/
│  ├─ archives/
│  ├─ alumni/
│  ├─ saegusa/
│  ├─ radio/
│  ├─ research/
│  └─ bousai-now/
├─ shared/
│  ├─ narrative-state/
│  ├─ analytics/
│  └─ accessibility/
└─ tests/
   ├─ trail/
   ├─ links/
   └─ narrative/
```

Implementation preference:
各サイトの見た目は異なるが、
内部では共通のcontent schemaとstate adapterを使えるようにする。

Do not share:
- visible global navbar
- common game HUD
- same design tokens across all in-world properties

May share internally:
- build tooling
- asset pipeline
- analytics wrapper
- conditional narrative state
- accessibility primitives
- test helpers

---

# 13. State Architecture

Player state should be minimal.

Potential local state:
```text
found_area08
identified_yui
heard_broadcast
ordered_diary
mapped_landmarks
understood_record_hazard
completed_map
ending
```

Avoid:
visible XP / quest progress.

State effects should appear in-world:
- pages become resolvable
- archive version changes
- index gains item
- wording subtly changes

---

# 14. Link-Rot / Platform Safety

Core story must be hosted on properties controlled by the project.

External real platforms:
optional only.

Do not make mandatory:
- X posts
- YouTube account availability
- Google search ranking
- third-party URL shortener
- public paste service

If social media is later added:
mirror essential content in controlled archive.

---

# 15. Production Gate Before Coding

Before implementation starts, verify:

- Municipality name / place names do not create unacceptable real-world confusion
- Every page has owner + era + purpose
- Every required lead has a recovery route
- Every site has at least 50% ordinary/non-clue content or contextual content where appropriate, so it feels like a site rather than a puzzle menu
- SITE-007 Act 0 screenshot/state is frozen for later comparison
- No final-state page accidentally ships discoverable without gating if that would spoil progression
