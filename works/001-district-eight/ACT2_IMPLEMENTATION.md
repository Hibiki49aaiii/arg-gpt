# 第八避難区 — ACT 2 IMPLEMENTATION

Status: Preproduction
Act: 2 — The Missing People
Human Gate: Act 0–1 #8 pending

## 1. Purpose

Act 2でプレイヤーの問いを、

> 「消された第八避難区はどこにあった？」

から、

> 「そもそも“第八避難区”は場所だったのか？」

へ変える。

このActでは超常現象を確定させない。

## 2. Entry Knowledge

Act 1終了時、プレイヤーは以下を知る。

- 現行避難区は1〜7
- 旧Webにarea08痕跡
- 防災第214号の8/20追補に「第八避難区対象者」
- 防災第216号の8/20改訂に「第八避難区 / 旧八号集会所」
- 旧八号集会所は公開史料検索で0件

まだ知らない:
- 第八区がいつ作られたか
- 誰が対象だったか
- 8/14に何が起きたか

## 3. Core Trail

```text
防災第214号
    ↓
防災第216号
    ↓
連番「215」がない
    ↓
史料アーカイブを文書番号検索
    ↓
防災第215号
「臨時管理区分の設定について」
1998-08-19
    ↓
第八避難区 = 管理区分08
    ↓
対象者一覧断片
    ↓
水城 結
現住所: 東三丁目
管理区分: 第八
    ↓
学校史資料
    ↓
1997中学卒業台帳:
水城 結 / 東三丁目
    ↓
同一人物照合
    ↓
「第八区の住民」ではなく
「既存住民に第八区を付与している」
    ↓
8月14日という共通起点
    ↓
ACT 3
```

## 4. Revelation

### R2-A
第八避難区という行政名称は1998-08-19に作られた。

これは1998-08-20のAct 1資料より1日前。

### R2-B
防災第215号は、第1〜7区の区域を変更しないまま「管理区分08」を設定している。

### R2-C
第八区対象者には既存住所がある。

### R2-D
水城結は事件以前から東三丁目に居住している。

したがって、

> 「昔から第八区に住んでいた人々が消された」

というAct 1仮説は成立しにくくなる。

## 5. Intended Player Theory

Act 2終了時の最有力仮説:

> 8月14日に何らかの事件があり、市は関係者を秘密裏に隔離・管理するため「第八避難区」というコードを作った。

これは**Partly True**。

True:
- 事件後にコードを作った
- 人を分類した
- 観察拠点を使った
- 情報を制限した

Misleading:
- 人体実験が事件原因
- 市が事件を起こした
- 第八区が秘密施設そのもの

## 6. PZ-003 — Document Number Gap

### Inputs
- 防災第214号
- 防災第216号
- 史料アーカイブ「防災関係文書目録」

### Observation
214 → 216。

### Required Insight
「第八区」という語ではなく、欠けた文書番号215を検索する。

### Search Result
```text
防災第215号
臨時管理区分の設定について
作成日: 1998年8月19日
主管: 防災課
公開状態: 一部公開
```

### Story Reveal
第八区の正式な行政コードは事件後に作られた。

### Recovery
- 214号の追補欄に「215号に基づく」と参照
- 216号改訂履歴に「215号適用」と参照

どちらか片方からでも到達可能。

## 7. EV-007 / 防災第215号

### Exact semantic requirements

必須:
- 1998-08-19
- 「臨時管理区分08」
- 「呼称: 第八避難区」
- 「既存第1〜7避難区の区域変更は行わない」
- 「8月14日以降に受付した照会・相談案件」
- 一部黒塗り

書かない:
- 共同記憶
- 放送33秒
- 水無坂の仕組み
- 記録媒介
- 超常現象

### Why partial redaction matters
文書がすべて説明するとMysteryが死ぬ。

黒塗り対象例:
- 対象条件
- 人数
- 具体的な聞き取り内容
- 外部研究者名

## 8. EV-008 / 対策会議議事要旨

Two dates:

### 1998-08-17
- 「8月14日発生の照会事案」
- 複数地区から類似問い合わせ
- 個別聞き取り開始
- 教育・保健部門へ共有

### 1998-08-19
- 対象者情報の混在防止
- 管理区分08採用
- 面談場所として旧市民体育館を使用
- 外部専門家の選定

Player-facing interpretation:
秘密隔離計画に見える。

Truth:
相談・観察拠点。

## 9. EV-009 / 対象者一覧断片

Columns:

| 氏名 | 現住所 | 管理区分 | 面談場所 | 備考 |
|---|---|---|---|---|
| 水城 結 | 東三丁目12-4 | 第八 | 旧市民体育館 | 保護者同伴 |

Important:
「住所」欄を第八へ書き換えない。

Act 1の別artifactで住所横に「第八」と追記された痕跡があるため、
Act 2で正式列構造を見せて再解釈させる。

## 10. PZ-004 — Two Homes

### Problem
「水城 結」が同姓同名の別人かもしれない。

### Sources
1. 対象者一覧
2. 1997年度中学校卒業台帳
3. 1998年度高校在籍資料
4. 保護者名
5. 生年月日

### Identity Keys
- 氏名: 水城 結
- DOB: 1981-04-27
- Guardian: 水城 真理子
- Address: 東三丁目12-4
- School progression consistent

### Solve
同一人物であることを複数属性で確定。

### Reveal
水城結は第八区から東三丁目へ移ったのではない。
第八区コードが付与される前から東三丁目に住んでいる。

## 11. SITE-002 Page Contracts

### A2-S2-001 防災関係文書目録
Show mundane records 210〜219。
215はtitleのみ閲覧可能。

### A2-S2-002 /documents/215
EV-007 scan/transcription。

### A2-S2-003 /meetings/1998-08-17
EV-008 first meeting.

### A2-S2-004 /meetings/1998-08-19
EV-008 code decision.

### A2-S2-005 /restricted/subjects-fragment
EV-009。

Discover via document attachment reference, not global nav.

## 12. SITE-003 — 凪代市学校史資料室

Act 2 introduces SITE-003.

### A2-S3-001 /
地域学校史archive home.

Ordinary content:
- 学校沿革
- 卒業年度一覧
- 行事写真
- 部活動記録

### A2-S3-002 /junior-high/graduates/1997
Graduation ledger.

### A2-S3-003 /junior-high/graduates/1997/yui-mizuki
EV-010 detail.

### A2-S3-004 /high-school/1998/summer-notice
EV-006。

Critical phrase:
「第八避難区対象者」

Again:
対象者, not 在住者.

## 13. Recovery Routes

### Route A — Document Numbers
214/216 → 215。

### Route B — Revision Reference
Act 1 plan metadata → 「215号適用」。

### Route C — School Notice
学校資料の「第八避難区対象」 → archiveで第八区を再検索 → 215 metadata。

PZ-004 identity confirmation:
- DOB route
- Guardian route
どちらでも同一人物へ到達可能。

## 14. Horror Beat

Act 2の恐怖はIdentity Unease。

Strong moment:
水城の「住所」を探しているのに、
資料ごとに

```text
現住所: 東三丁目
管理区分: 第八
```

と並ぶ。

No:
- ghost photo
- moving text
- glitch
- threatening message

## 15. Act 3 Lead

Act 2後半で「8月14日」を繰り返す。

Allowed:
- 「8月14日発生の照会事案」
- 「8月14日以降の対象者」
- 8/14の問い合わせ件数が別紙扱い

Do not reveal yet:
- 防災無線
- 18:00
- 27秒
- 33秒
- 受信録音

Final Act 2 question:

> 8月14日に、何があった？

This becomes Act 3 entry.

## 16. Human-Gate Isolation

Until Issue #8 PASS:
- Do not link these pages from current vertical-slice runtime.
- Do not modify current clue salience.
- Do not change Act 1 archive zero-result behavior.

Allowed:
- author exact content
- create staging assets
- machine validate staging

## 17. Definition of Done

Act 2 preproduction is complete when another implementer can build all pages/artifacts without inventing:
- dates
- document numbers
- identity keys
- wording distinction between 対象 / 在住
- intended player theory
- Act 3 spoiler boundary
