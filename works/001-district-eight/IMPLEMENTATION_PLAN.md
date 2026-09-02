# 第八避難区 — Implementation Plan

Production Specification固定済み。Act 0〜6 Stagingは分離実装・個別machine validation済み。現在はEngineering Readiness横断検証とHuman Blind Playtest Gateを管理する段階。

## P0 — Story Lock

Deliverables:
- Final Truth
- Theme
- Real Timeline
- Character Knowledge Matrix
- Revelation Ladder
- Ending logic

Exit Criteria:
- 最終真相に矛盾がない
- 主要人物の行動動機が成立
- Act 0〜6の情報開示順が確定
- END-A/B/CがThemeに接続

## P1 — Evidence Architecture

Deliverables:
- EVIDENCE_LEDGER.md
- TIMELINE.md
- CHARACTERS.md

Tasks:
- EV台帳
- Reliability
- Supports / Contradicts
- Player discovery act
- Character ownership
- Creation date / modification history

Exit Criteria:
Final Truthの主要命題すべてに、公開前から複数の根拠が存在する。

## P2 — Puzzle Architecture

Deliverables:
- PUZZLE_LEDGER.md

各Puzzleで管理する項目:
- Narrative Reason
- Input
- Insight
- Solution
- Reveal
- Next Lead
- Hint 1 / Hint 2
- Recovery Route
- Accessibility Alternative

Difficulty Curve:
- Act 0: Very Easy
- Act 1: Easy
- Act 2: Easy-Medium
- Act 3: Medium
- Act 4: Medium
- Act 5: Medium-Hard
- Act 6: Hard

暗号技術の難しさより、情報を結び付ける難しさを主軸にする。

## P3 — Media / Site Architecture

Deliverables:
- SITE_MAP.md
- MEDIA_LEDGER.md
- DOMAIN_PLAN.md

Proposed properties:
1. 旧凪代市防災情報ミラー
2. 凪代市史料デジタルアーカイブ
3. 凪代市学校史資料室
4. 個人サイト「記録庫・三枝」
5. 地域ラジオ保存会
6. 研究資料ミラー
7. 現行凪代市防災ページ

Design requirement:
全サイトを同じUIキットで作らない。年代・所有者・用途ごとに別の情報設計と外観を持たせる。

## P4 — Vertical Slice

Act 0〜1だけ先に実装。

Required:
- Trailhead
- area08発見
- 最初のPDF
- 最初の外部サイト遷移
- 1 puzzle
- 1 false theory
- 1 horror beat

Test Goal:
完全初見プレイヤーが説明なしで「何かおかしい」→「調べたい」→「第八避難区があったらしい」まで到達する。

## P5 — Full Narrative Implementation

Act 2〜6を実装。

Systems:
- Static content
- Evidence assets
- Audio / Video
- Optional local progress
- Conditional page reveal
- Ending selection

サーバー側アカウントは必須にしない。

## P6 — Consistency QA

Timeline checks:
- 年齢
- 曜日
- 学校年度
- 文書作成日
- 研究開始時期
- 事故前後

Character Knowledge:
その時点で知り得ない情報を人物が発言していないか。

Artifact Authenticity:
- 年代に合わないWeb表現
- 不自然なファイル形式
- 当時存在しない用語
- 不自然な行政文書形式

Mystery Fairness:
最終真相を示すEvidenceが後出しだけになっていないか。

## P7 — Blind Playtest

Tester A: ARG経験なし — Trailhead / UX
Tester B: 謎解き経験者 — Puzzle fairness
Tester C: ARG / Mystery経験者 — 真相の予測可能性と納得度

Metrics:
- Act到達時間
- 停滞点
- 誤仮説
- Hint使用回数
- Abandon point
- Ending選択
- 最終真相理解率

## P8 — Production Hardening

- Mobile QA
- Link Rot fallback
- Accessibility
- SEO / discoverability
- Cache behavior
- Asset backup
- Analytics
- Fiction disclaimer
- Exit / safety page
- robots / indexing policy
- spoiler management

## Production / Implementation Status

### Architecture / Specification
- [x] TIMELINE.md
- [x] CHARACTERS.md
- [x] EVIDENCE_LEDGER.md
- [x] PUZZLE_LEDGER.md
- [x] SITE_MAP.md
- [x] MEDIA_LEDGER.md
- [x] DOMAIN_PLAN.md
- [x] VERTICAL_SLICE.md
- [x] Naming Lock: 凪代市

### Staging Implementation
- [x] Act 0〜1 Vertical Slice
- [x] Act 2 Staging
- [x] Act 3 Staging
- [x] Act 4 Staging
- [x] Act 5 Staging
- [x] Act 6 Staging

### Machine Validation
- [x] Vertical Slice validator
- [x] Act 2 validator
- [x] Act 3 validator
- [x] Act 4 validator
- [x] Act 5 validator
- [x] Act 6 validator
- [x] Full-Staging Engineering Readiness master gate

### Human / Release Gates
- [ ] **Issue #8 Human Blind Playtest Round 1**
- [ ] Public runtime integration
- [ ] Production Hardening
- [ ] Public release

## Engineering Readiness

Full status:
`FULL_STAGING_STATUS.md`

The master gate must verify all Act validators plus cross-act chronology, naming, spoiler boundaries, generated-vs-found semantics, and isolation.

## Human Blind Playtest

**Issue #8 is the required Human Blind Playtest gate.**

Until it passes:
- Act 2〜6 staging must remain unlinked from the current public trail.
- Act 0〜1 narrative salience is not considered frozen.
- public release remains blocked.

Machine PASS does not substitute for human discovery / comprehension testing.
