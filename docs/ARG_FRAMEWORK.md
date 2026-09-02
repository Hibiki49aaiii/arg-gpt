# ARG Design Framework

この文書は、arg-gpt内の全作品に共通する設計フレームワーク。

## 1. Core Definition

各作品は最初に以下を1文ずつ固定する。

- Central Mystery: プレイヤーが最初に解こうとする謎
- Final Truth: 制作者だけが知る本当の出来事
- Player Role: なぜプレイヤーが調査に参加するのか
- Danger: 調査によって何が悪化するのか
- Theme: 作品が最終的に扱う人間的テーマ
- Final Recontextualization: 終盤で何の意味が反転するか

## 2. Four Truth Layers

### T0 — Objective Truth
実際に起きたこと。絶対にブレさせない。

### T1 — Institutional Version
行政、企業、研究者、組織が公式に残した説明。

### T2 — Character Belief
登場人物が信じている説明。誤解を含んでよい。

### T3 — Player Theory
プレイヤーが各Actで自然に到達する想定仮説。

良いミステリーは T3 が Actごとに変化し、最終的に T0 へ近づく。

## 3. Revelation Ladder

- R1: 違和感が偶然ではない
- R2: 誰かが意図的に隠している
- R3: 隠蔽には正当化できる理由があった可能性
- R4: プレイヤー自身の調査が事件の一部だった

## 4. Evidence Model

各証拠にIDを付与し、Title / Medium / Source / Visible Fact / Hidden Meaning / Supports / Contradicts / Unlocks / Reliability / Act を管理する。

Reliability:
- Confirmed
- Mostly Reliable
- Biased
- Manipulated
- Fabricated
- Unknown

## 5. Puzzle Model

各Puzzleは Narrative Reason / Input / Observed Pattern / Required Insight / Solution / Output / Story Reveal / Next Leads / Fallback Hint / Failure Risk / Difficulty を持つ。

必須条件:
- Puzzleの答えだけで終わらない
- 解答後にStory Revealがある
- 解けない場合のRecovery Pathがある
- 無関係な暗号を置かない

## 6. Trail Architecture

- Trailhead: 最初の入口
- Spine: クリアに必要な主経路
- Branch: 世界観を厚くする任意経路
- Red Herring: 後から合理的に否定できる誤誘導
- Dead End: 必須情報を置かない
- Recovery Route: 主経路を見失った時の復帰経路

## 7. Character Knowledge Matrix

各登場人物について Knows / Believes / Hides / Lies About / Learns At を管理する。

## 8. Timeline

3種類を分離する。
- Real Timeline: 実際に起きた順
- Archive Timeline: 資料が作成された順
- Player Discovery Timeline: プレイヤーが知る順

## 9. Horror Design

優先順位:
1. Logical Unease
2. Social Unease
3. Temporal Unease
4. Identity Unease
5. Direct Threat
6. Shock

最初からShockへ行かない。

## 10. Immersion Rules

- ゲームUIを過剰に出さない
- Fictional artifactは目的に合う見た目にする
- 古い自治体ページは古いWebとして作る
- 研究資料は研究資料として作る
- SNS人物は投稿履歴と口調を一貫させる
- すべての媒体を同一デザインにしない

## 11. Searchability

- 固有語を用意する
- 表記揺れを管理する
- SEO依存だけを必須進行にしない
- サイト内にも救済導線を持つ
- 外部プラットフォーム停止時のFallbackを用意する

## 12. Ending Design

- プレイヤーは真相を知るだけか、選択するか
- 選択が世界へ影響するか
- どの選択も完全正解にしないか
- 序盤を読み返したくなる再文脈化があるか

## 13. Quality Gates

### Story Gate
- Truthに矛盾がない
- Character Knowledgeが整合する
- Motiveが成立する

### Mystery Gate
- 重要な真相に事前証拠がある
- 後出し設定だけで解決しない
- Red Herringがフェア

### Puzzle Gate
- 解法が一意または許容可能
- 物語上の理由がある
- 総当たり不要
- ヒント導線がある

### ARG Gate
- Trailheadが機能する
- 必須外部サイト死亡時も詰まない
- スマホでも進められる
- Blind Playtestで完走可能

## 14. Required Files Per Work

最低限:
- STORY_BIBLE.md
- NARRATIVE_GRAPH.md
- IMPLEMENTATION_PLAN.md

本格制作開始後:
- TIMELINE.md
- CHARACTERS.md
- EVIDENCE_LEDGER.md
- PUZZLE_LEDGER.md
- SITE_MAP.md
- RELEASE_PLAN.md
- PLAYTEST.md