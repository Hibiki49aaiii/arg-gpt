# arg-gpt

複数のオリジナルARG（Alternate Reality Game）を継続的に企画・設計・実装するための制作リポジトリ。

## Vision

単なる暗号問題集やホラーLPではなく、プレイヤーが「自分でインターネット上の事件を調査している」と感じられる作品を作る。

各作品では以下を重視する。

- Horror: 説明されない異常が徐々に日常へ侵入する
- Mystery: 最初の仮説が後の証拠で再解釈される
- Investigation: Web、資料、映像、音声、検索を横断する
- Puzzle: 謎そのものが世界観・人物・事件の情報を開示する
- Immersion: UIではなくWeb上の「実在感」を設計する
- Fairness: 理不尽な総当たりを避け、複数の回復導線を持つ
- Recontextualization: 終盤で序盤の資料の意味が変わる

## Repository Structure

```text
arg-gpt/
├─ README.md
├─ docs/
│  └─ ARG_FRAMEWORK.md
└─ works/
   ├─ 001-district-eight/
   │  ├─ STORY_BIBLE.md
   │  ├─ NARRATIVE_GRAPH.md
   │  ├─ TIMELINE.md
   │  ├─ CHARACTERS.md
   │  ├─ EVIDENCE_LEDGER.md
   │  ├─ PUZZLE_LEDGER.md
   │  ├─ SITE_MAP.md
   │  ├─ MEDIA_LEDGER.md
   │  ├─ DOMAIN_PLAN.md
   │  ├─ VERTICAL_SLICE.md
   │  ├─ IMPLEMENTATION_PLAN.md
   │  └─ FULL_STAGING_STATUS.md
   └─ 002-...
```

## Source of Truth

作品ごとに以下を必ず分離する。

1. **Truth**
   - 制作者だけが知る最終真相
2. **Player-Facing Facts**
   - プレイヤーが各Act時点で観測できる事実
3. **Character Knowledge**
   - 各登場人物が知っていること／誤解していること
4. **Timeline**
   - 実際に起きた出来事の時系列
5. **Evidence Graph**
   - どの証拠がどの真相を支持・反証するか
6. **Puzzle Graph**
   - どの謎から何が開示されるか
7. **Release Graph**
   - どのサイト・媒体・ページで情報を出すか

この分離を崩さない。物語中の嘘と、制作資料上の矛盾を混同しない。

## Work 001

### 第八避難区（working title）

> ある自治体の古い防災サイトから、行政上は存在しない「第八避難区」の記録が見つかる。  
> プレイヤーは消された地区を復元するため調査を始めるが、やがて「消された」のではなく、「忘れさせなければならなかった」ことを知る。

詳細:
- `works/001-district-eight/STORY_BIBLE.md`
- `works/001-district-eight/NARRATIVE_GRAPH.md`
- `works/001-district-eight/TIMELINE.md`
- `works/001-district-eight/CHARACTERS.md`
- `works/001-district-eight/EVIDENCE_LEDGER.md`
- `works/001-district-eight/PUZZLE_LEDGER.md`
- `works/001-district-eight/SITE_MAP.md`
- `works/001-district-eight/MEDIA_LEDGER.md`
- `works/001-district-eight/DOMAIN_PLAN.md`
- `works/001-district-eight/VERTICAL_SLICE.md`
- `works/001-district-eight/IMPLEMENTATION_PLAN.md`
- `works/001-district-eight/FULL_STAGING_STATUS.md`

### Implementation Status

- Act 0–1 Vertical Slice: implemented / machine-validated
- Act 2–6: isolated staging implemented / machine-validated
- Full cross-act Engineering Readiness Gate: **PASS**
- Human Blind Playtest: Issue #8 pending
- Public runtime integration: blocked until Human Gate passes

See:
- `works/001-district-eight/FULL_STAGING_STATUS.md`

## Production Principles

### 1. Puzzle follows story

謎を解く理由を物語内に持たせる。

悪い例:
- 関係のないシーザー暗号を置く

良い例:
- 防災無線の欠損音声を復元すると、行政が削除した地区名が聞こえる

### 2. Every clue changes understanding

主要Clueは最低1つを行う。

- 新情報を開示する
- 既存情報を否定する
- 登場人物への評価を変える
- Timelineを更新する
- 次の探索対象を示す

### 3. No single fragile trail

必須進行には原則2本以上の発見経路を用意する。

### 4. Horror through implication

グリッチ、赤文字、ジャンプスケアを主役にしない。

怖さの中心は、

- 記録同士がわずかに食い違う
- 誰も説明しない
- 後から過去のページの意味が変わる
- プレイヤーの行動が事件を進行させていたと分かる

ことに置く。

### 5. Fiction safety

実在人物・現役企業・実在の災害被害者を誤認させる設計は避ける。
公開作品にはフィクション表記と安全な退出導線を持たせる。

## Development Process

各作品は原則以下の順で進める。

1. Central Mystery
2. Final Truth
3. Theme
4. Real Timeline
5. Character Knowledge
6. Acts / Revelations
7. Evidence Graph
8. Puzzle Graph
9. Site / Media Architecture
10. Recovery Paths
11. Ending
12. Implementation
13. Internal Consistency Review
14. Blind Playtest
15. Release
