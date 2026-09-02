# 第八避難区 — MEDIA_LEDGER

Status: Production Specification
Purpose: Evidenceを実在感のあるartifactへ変換するための制作台帳。

## Media Principles

1. 素材は「ホラー画像」ではなく、その資料を作った人物・組織が実際に作りそうなものにする。
2. 重要Clueを汚れ・ノイズ・低解像度だけに隠さない。
3. 年代、作成者、複写経路、劣化理由を設定する。
4. 同じ情報を複数媒体で完全重複させず、相互補完させる。
5. Act 0〜1では超常現象の直接描写を出さない。
6. Act 6以外で「現実改変」を断定できる素材を出さない。

## Asset Status
- REQUIRED-VS: Vertical Slice必須
- REQUIRED-FULL: 本編必須
- OPTIONAL: 雰囲気強化
- LATE: Act 5〜6のみ

---

# A. Act 0–1 / Vertical Slice Assets

| ID | Asset | Type | Source/Site | Status | Evidence | Production Notes |
|---|---|---|---|---|---|---|
| MED-001 | 現行避難区一覧スクリーン | HTML/CSS | SITE-007 | REQUIRED-VS | EV-001 | 1〜7、完全に普通 |
| MED-002 | 旧防災トップ | HTML/CSS | SITE-001 | REQUIRED-VS | context | 2002〜04自治体Web |
| MED-003 | 旧避難区一覧 | HTML/CSS | SITE-001 | REQUIRED-VS | EV-001 | 01〜07 |
| MED-004 | 共通区アイコン01〜07 | GIF/PNG | SITE-001 | REQUIRED-VS | EV-002 | filename ruleを統一 |
| MED-005 | broken asset reference 08 | HTML/source | SITE-001 | REQUIRED-VS | EV-002 | 総当たり不要の明示痕跡 |
| MED-006 | backup index | TXT/HTML | SITE-001 | REQUIRED-VS | EV-003 | Recovery Route |
| MED-007 | 平成10年夏季防災計画 | PDF | SITE-001 | REQUIRED-VS | EV-004 | 8〜12ページ程度 |
| MED-008 | 給水地点一覧 | PDF | SITE-001 | REQUIRED-VS | EV-005 | 旧八号集会所 |
| MED-009 | PDF metadata panel | UI/text | SITE-001 | REQUIRED-VS | PZ-002 | Mobile対応 |
| MED-010 | 古いサイト更新履歴 | HTML | SITE-001 | REQUIRED-VS | context | 普通の更新を多数入れる |
| MED-011 | 防災課連絡先ページ | HTML | SITE-001 | OPTIONAL | filler | 実在感 |
| MED-012 | 第1〜7区個別ページ | HTML | SITE-001 | REQUIRED-VS | PZ-001 | 同じ規則を学習させる |
| MED-013 | 第8区404ページ | HTML | SITE-001 | REQUIRED-VS | future callback | 普通の404 |
| MED-014 | 文書検索トップ | HTML | SITE-002 | REQUIRED-VS | bridge | document ID検索 |
| MED-015 | 旧八号集会所検索結果0件 | HTML | SITE-002 | REQUIRED-VS | unease | 明確な異常ではない |

## VS Asset Acceptance

MED-001〜015だけで、プレイヤーは以下へ到達できること:

1. 現行制度は7区。
2. 旧サイトにも見える範囲では7区。
3. しかしasset/backup規則に08がある。
4. 古い行政PDFに「第八避難区」が存在。
5. 「単なるfilenameミス」では説明しにくい。
6. 旧八号集会所という具体語を次の探索対象として得る。

禁止:
- 水城結の二重住所をVSで明かす
- 33秒音声をVSで再生する
- 桐谷の研究理論をVSで出す
- 「記録が現実を作る」と示唆しすぎる

---

# B. Act 2 Assets

| ID | Asset | Type | Site | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| MED-016 | 庁内分類コード起案 | scanned document | SITE-002 | REQUIRED-FULL | EV-007 | 1998-08-19明示 |
| MED-017 | 対策会議議事要旨 | PDF | SITE-002 | REQUIRED-FULL | EV-008 | 一部黒塗り |
| MED-018 | 対象者一覧断片 | scan | SITE-002 | REQUIRED-FULL | EV-009 | 水城の二重表記 |
| MED-019 | 1997中学卒業台帳 | scan | SITE-003 | REQUIRED-FULL | EV-010 | 東三丁目 |
| MED-020 | 高校夏季連絡資料 | PDF/scan | SITE-003 | REQUIRED-FULL | EV-006 | 「第八避難区対象」 |
| MED-021 | 旧電話帳人物索引 | scan | SITE-002 | OPTIONAL | corroboration | 同一人物確認 |

---

# C. Act 3 / Audio Assets

| ID | Asset | Type | Site | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| MED-022 | 防災無線送信ログ | scan/log | SITE-001 | REQUIRED-FULL | EV-011 | 27秒 |
| MED-023 | 受信カセットA | audio | SITE-005 | REQUIRED-FULL | EV-012 | 劣化あり |
| MED-024 | 地域FM受信カセットB | audio | SITE-005 | REQUIRED-FULL | EV-013 | 独立source |
| MED-025 | 同期用時報/チャイム | audio | SITE-005 | REQUIRED-FULL | PZ-005 | alignment anchor |
| MED-026 | 波形簡易viewer | UI | SITE-005 | REQUIRED-FULL | PZ-005 | audio editor不要 |
| MED-027 | accessibility transcript fragments | text | SITE-005 | REQUIRED-FULL | PZ-005 | 答えを直書きしない |
| MED-028 | 片瀬保守報告書 | PDF | SITE-005 | REQUIRED-FULL | EV-014 | defensive tone |
| MED-029 | 問い合わせ手書きメモ | image | SITE-002 | REQUIRED-FULL | EV-015 | 18:12 / 18:25 |

Audio production rule:
33秒を単純な怖い声にしない。
大部分は不明瞭な行政放送らしさを維持する。
BGM、逆再生声、悪魔声は禁止。

---

# D. Act 4 / Human Memory Assets

| ID | Asset | Type | Site | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| MED-030 | 水城日記 前半 | 8–12 scans | SITE-003 | REQUIRED-FULL | EV-016 | 日常80%、異常20% |
| MED-031 | 水城日記 後半 | 8–12 scans | SITE-003 | REQUIRED-FULL | EV-017 | 忘却の過程 |
| MED-032 | 日記transcription | text | SITE-003 | REQUIRED-FULL | accessibility | 検索indexは制限 |
| MED-033 | 児童画A | image | SITE-003 | REQUIRED-FULL | EV-018 | 公園 |
| MED-034 | 児童画B | image | SITE-003 | REQUIRED-FULL | EV-018 | 坂 |
| MED-035 | 児童画C | image | SITE-003 | REQUIRED-FULL | EV-018 | 集会所 |
| MED-036 | 真壁俊作文 | scan/text | SITE-003 | REQUIRED-FULL | EV-020 | 公園中央基礎 |
| MED-037 | 保護者聞き取り要約 | PDF | SITE-002 | OPTIONAL | EV-019 | 独立家庭 |

Watercolor/child drawing rule:
絵自体を露骨にホラー化しない。
普通の児童画として成立させる。

---

# E. Act 4–5 / Reality Consistency Assets

| ID | Asset | Type | Site | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| MED-038 | 1997地図 | image | SITE-002 | REQUIRED-FULL | EV-021 | baseline |
| MED-039 | 1998-07地図 | image | SITE-002 | REQUIRED-FULL | EV-021 | baseline |
| MED-040 | 1998-09地図 | image | SITE-002 | REQUIRED-FULL | EV-021 | faint line |
| MED-041 | 2001 scan地図 | image | SITE-002 | REQUIRED-FULL | EV-021 | clearer line |
| MED-042 | overlay viewer | UI | SITE-002 | REQUIRED-FULL | PZ-008 | fixed reference points |
| MED-043 | 市街地写真negative view | image | SITE-002 | OPTIONAL | EV-022 | unreliable clue |
| MED-044 | 市街地写真later scan | image | SITE-002 | OPTIONAL | EV-022 | building difference |
| MED-045 | 電話帳初版複写 | image | SITE-002 | REQUIRED-FULL | EV-023 | no 水無坂 |
| MED-046 | 電話帳保管版 | image | SITE-002 | REQUIRED-FULL | EV-023 | 水無坂 |

---

# F. Act 5 / Research + Saegusa Assets

| ID | Asset | Type | Site | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| MED-047 | 桐谷研究ノートA | PDF | SITE-006 | REQUIRED-FULL | EV-024 | early hypothesis |
| MED-048 | 引用索引 | HTML/PDF | SITE-006 | REQUIRED-FULL | PZ-009 | missing chapter clues |
| MED-049 | 桐谷ノートB | PDF | SITE-006 | REQUIRED-FULL | EV-025 | density correlation |
| MED-050 | 固有語削除命令 | scan | SITE-002/006 | REQUIRED-FULL | EV-026 | containment |
| MED-051 | 症例推移グラフ | chart | SITE-006 | REQUIRED-FULL | EV-027 | correlation only |
| MED-052 | 三枝1999 page | HTML snapshot | SITE-004 | REQUIRED-FULL | EV-028 | preservation ethic |
| MED-053 | 三枝2007 page | HTML snapshot | SITE-004 | REQUIRED-FULL | EV-029 | recurrence |
| MED-054 | 三枝2008 deleted index | HTML snapshot | SITE-004 | REQUIRED-FULL | EV-030 | reversal |
| MED-055 | 三枝2009 final memo | scan/text | SITE-004 | REQUIRED-FULL | EV-031 | moral key |

---

# G. Act 6 / Final State Assets

| ID | Asset | Type | Site | Status | Evidence | Notes |
|---|---|---|---|---|---|---|
| MED-056 | player map workspace | interactive UI | shared | LATE | EV-032 | multi-source synthesis |
| MED-057 | final reconstructed map | image/data | shared | LATE | EV-032 | generated, not found |
| MED-058 | SITE-007 state A snapshot | HTML fixture | SITE-007 | REQUIRED-FULL | EV-001 | 7区 |
| MED-059 | SITE-007 state B | HTML | SITE-007 | LATE | EV-033 | 8区 |
| MED-060 | SITE-001 /08 state B | HTML | SITE-001 | LATE | EV-034 | old-looking normal page |
| MED-061 | END-A final index | HTML | shared | LATE | ending | full restore |
| MED-062 | END-B degraded index | HTML | shared | LATE | ending | removal |
| MED-063 | END-C incomplete archive | HTML | shared | LATE | ending | people preserved |

Critical:
MED-058のAct 0 stateは実装開始時にfixtureとして保存し、Act 6との差分をテスト可能にする。

---

# H. Ordinary / Non-Clue Content

没入のため、各サイトはClueだけで構成しない。

Required ordinary content examples:

SITE-001:
- 台風時避難案内
- 防災訓練
- 消火器案内
- 過去の更新履歴
- 第1〜7区の普通情報

SITE-002:
- 市史写真
- 広報紙
- unrelated meeting records
- map collections

SITE-003:
- 学校沿革
- 部活写真
- 行事記録
- 卒業年度一覧

SITE-004:
- 三枝の文書保存論
- scanner tips
- local history links

SITE-005:
- 地域番組録音
- equipment articles

SITE-006:
- 桐谷の通常研究業績
- unrelated memory papers

Target:
各Core Siteで、プレイヤーが見る範囲の30〜60%は直接的な主要Clueではない文脈情報にする。
ただし無意味なページ水増しはしない。

---

# I. Accessibility Contract

Image:
- OCR相当の全文転記ではなく、必要に応じaccessible transcriptionを提供
- puzzle answerをaltだけに隠さない
- 色だけを差分根拠にしない

Audio:
- waveform
- partial transcript
- timing information
を組み合わせて同じ推論が可能。

Interactive map:
- keyboard操作
- coordinate/list input
- screen-reader compatible landmark table

PDF:
- browser内metadata viewerを持たせる
- OSやAdobe Acrobat固有操作を要求しない

---

# J. Spoiler Boundaries

## SB-0
Act 0で許可:
- 08欠番

禁止:
- 人名
- 1998-08-14の異常放送
- 記録媒介

## SB-1
Act 1で許可:
- 第八避難区という語
- 旧八号集会所
- 対象者という曖昧語

禁止:
- 二重住所の確定
- 行政コード新設日
- 共同記憶理論

## SB-2+
後続ActはPUZZLE_LEDGER / EVIDENCE_LEDGERに従う。

Build/testでは、各assetにminimum_actをmetadataとして持たせる案を推奨。
