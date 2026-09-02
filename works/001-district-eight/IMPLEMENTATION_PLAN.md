# 第八避難区 — Implementation Plan

現段階はストーリー／全体設計フェーズ。本番サイト実装は次工程。

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
1. 旧久代市防災情報ミラー
2. 久代市史料デジタルアーカイブ
3. 久代東中学校 同窓資料室
4. 個人サイト「記録庫・三枝」
5. 地域ラジオ保存会
6. 研究資料ミラー
7. 現行久代市防災ページ

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

## Immediate Next Files

1. TIMELINE.md
2. CHARACTERS.md
3. EVIDENCE_LEDGER.md
4. PUZZLE_LEDGER.md
5. SITE_MAP.md

この5つが揃った時点で、ストーリーから実装仕様へ移行可能。