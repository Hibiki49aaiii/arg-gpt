# 第八避難区 — ACT 5 CONTENT BIBLE

Status: Exact-data / citation draft for staging implementation
Earlier runtimes remain unlinked.

# 1. EV-021 Map Version Contract

## MAP-1997
Label:
`1997 市街地図 保存複写`

Target feature:
absent.

## MAP-1998-07
Label:
`1998年7月 市街地図 印刷複写`

Target feature:
absent.

## MAP-1998-09
Label:
`1998年9月 市街地図 保管原本`

Target feature:
faint line.

## MAP-2001
Label:
`2001 デジタル保存スキャン`

Target feature:
clearer line.

## Fixed Anchors

Normalized staging coordinates:

| Anchor | Meaning | X | Y |
|---|---|---:|---:|
| A | river bend / bridge abutment | 0 | 0 |
| B | old civic hall SW corner | 100 | 0 |
| C | railway underpass center | 40 | 80 |

These are unchanged across all versions.

## Target Feature

Normalized:
- start approximately (57,42)
- endpoint approximately (63,34)

Versions:
- 1997: none
- 1998-07: none
- 1998-09: (57,42)→(62,35), low confidence
- 2001: (57,42)→(63,34), high confidence

Do not label the feature 水無坂 on the maps.

# 2. PZ-008 UI

Player registers each map using A/B/C.

Controls:
- choose anchor A
- choose anchor B
- choose anchor C
- lock transform
- overlay slider
- difference table
- text mode

Success condition:
all three fixed anchors aligned within staging tolerance.

Success output:
- surrounding stable features overlap
- target zone difference becomes visible
- chronological state table unlocks

Neutral copy:

> 固定基準点を合わせると、同一区画の保存状態を比較できます。

Do not say:
“watch the road appear.”

# 3. EV-023 Phonebook

Title:
`1998年度 電話帳索引 — 版差分`

Initial reference copy:
- 水無坂: no entry

Later preserved copy:
- 水無坂: index heading present

Allowed sample entries:
- 水無坂 ○番地 — [氏名非公開]
- 水無坂 ○番地 — [氏名非公開]

No real phone numbers.

Copy:

> 同年度資料として管理されていた複写間で、索引見出しの有無が一致しません。

# 4. EV-022 Photo Anomaly

Title:
`市街地写真 管理番号 P-1842`

Earlier reference:
distant background structure not confirmed.

Later scan:
small roof-like structure visible.

Visible caveat list:
- crop difference
- restoration artifact
- negative mix-up
- labeling error

Status:
Unknown / optional.

# 5. EV-024 Kiritani Note A Structure

Title:
`共同記憶同期に関する予備観察`

Author:
桐谷 宗一

Sections:

1. 対象と定義
2. 接触経路の確認
3. 共通刺激仮説
4. 記録・再想起
   - 4.1 記録分類
   - 4.2 接触群比較
   - 4.3 [欠落]
5. 暫定考察
Appendix A/B

The archive copy is missing 4.3.

# 6. Reverse Citations to 4.3

At least four.

## C-01 — §2.4

> 接触経路を確認できない新規回答者について、4.3区分Dの再測定結果を参照。

Meaning:
new/unexposed respondents were measured.

## C-02 — §5.1

> 記録追加後の再測定では回答一致率が上昇した。4.3表2参照。

Meaning:
record addition precedes a later measurement.

## C-03 — Appendix B

> 記述量区分A–Dと新規再想起率の対応は4.3の集計値による。

Meaning:
description quantity is an explicit variable.

## C-04 — Margin Memo

> D↑ → N(recall)↑ ?
> reverse direction not excluded

Meaning:
directionality concern remains unresolved.

# 7. PZ-009 Solve

The player does not reconstruct missing exact prose.

Required derived statements:

1. 4.3 measured new respondents.
2. records had been added before a later measurement.
3. description quantity was categorized.
4. higher description quantity corresponded to higher new-recall rate.
5. reverse causality was not excluded.

Unlock:
EV-025.

# 8. EV-025 Kiritani Note B

Title:
`記述密度と再想起率 — 追補`

Key paragraph:

> 既知の記述量が多い対象群ほど、後続測定で新規回答者が同一特徴を想起する割合が高かった。

> 本結果は因果を確定しない。ただし、想起の増加を既存回答者間の直接情報伝播のみで説明することは困難である。

Required graph/table:
description-density quartile vs subsequent new-recall rate.

No supernatural terminology.

# 9. EV-026 Suppression Order

Date:
1998-09-03.

Title:
`関連固有語の取扱い及び閲覧制限について`

Actions:
- 水無坂 / 第八避難区 / 旧八号集会所 exact searchable strings removed or hidden
- detailed map access restricted
- affected-person cross-contact reduced
- public explanation standardized

Visible reason:
`混乱拡大防止のため`

Do not write:
“because records create reality.”

# 10. EV-027 Case Trend

Time series buckets:

| Period | New matching-recall reports |
|---|---:|
| 8/14–8/16 | 11 |
| 8/17–8/23 | 18 |
| 8/24–8/30 | 14 |
| 8/31–9/02 | 7 |
| 9/03–9/09 | 4 |
| 9/10–9/16 | 2 |
| 9/17–9/30 | 1 |

Marker:
9/03 containment begins.

Caveat:
collection/reporting conditions also changed.

Do not calculate a causal effect size.

# 11. EV-028 Saegusa 1999

Title:
`個人整理メモ / 1999`

Core:

> 名簿から消したら、その人まで消したことになる。

> 何が起きたか分からないからこそ、少なくとも名前と経緯は残すべきだ。

Function:
establish preservation ethic.

# 12. Saegusa 2001–2005 Context

Ordinary personal archive pages:
- scanner notes
- local history links
- cataloging rules
- document preservation thoughts

This makes him a person, not a puzzle NPC.

# 13. EV-029 Saegusa 2007

Title:
`再整理後の差異 / 2007-02`

Core chronology:

> 昨年から古い複写をまとめ直している。

> 以前の索引にはなかった地名が、保管資料の方に戻っているように見える。

> 自分の整理ミスをまず疑う。

Then:
he compares older screenshots/catalog lists.

He does not jump directly to supernatural causation.

# 14. EV-030 Saegusa 2008 Deletion History

Delete batches:
- 2008-09-03
- 2008-09-07
- 2008-09-12

Deleted:
- precise geographic references
- high-resolution map scans
- exact audio index
- cross-linked name/place index

Retained:
- broad incident chronology
- some personal names
- ethics notes

Evidence of voluntary action:
maintenance notes from same account before deletion.

# 15. PZ-010 Timeline

Cards:
- 1999 preserve names
- 2005 digitize/reorganize
- 2007 recurrence concern
- 2008 delete precise material
- 2009 final memo

Correct order must be established from dated pages.

Story conclusion:
Saegusa’s deletion follows his recurrence concern.

# 16. EV-031 Saegusa 2009

Title:
`最後の整理メモ`

Core line:

> 残せば戻る。消せば彼らが消える。

Additional line allowed:

> 名前まで消す必要があるのか、まだ分からない。

This preserves moral ambiguity.

Forbidden:
- exact safe solution
- explicit END-C instructions
- player blame
- complete mechanism

# 17. Cross-Evidence Flow

Preferred:

```
Partial Map v1
→ EV-021 map overlay
→ record-side anomaly
→ EV-023 phonebook difference
→ EV-024 Kiritani A
→ PZ-009 reverse citations
→ EV-025 density/re-recall
→ EV-026 suppression order
→ EV-027 trend
→ Saegusa archive
→ EV-028 preservation ethic
→ EV-029 recurrence
→ EV-030 self-deletion
→ PZ-010
→ EV-031
→ Act 6
```

EV-022 can be discovered anywhere after EV-021 and is never required.

# 18. Act 5 Exit

Confirmed:
record-side anomalies exist across more than one medium.
record quantity and later new recall are correlated.
suppression coincides with decline.
Saegusa voluntarily reversed from preservation to deletion.

Unconfirmed:
exact mechanism.
whether deleting records caused decline.
whether all records are dangerous.
whether current investigation is changing anything.

Final player-facing question:

> 残すべき記録と、残してはいけない記録は同じなのか？
