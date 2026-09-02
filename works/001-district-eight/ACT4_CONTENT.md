# 第八避難区 — ACT 4 CONTENT BIBLE

Status: Exact-copy / relational draft for staging implementation
Current Act 0–1 runtimeには未接続。

# 1. Diary Chronology

All dates below are canonical author dates.

Player scans may obscure some day numerals, but content/order must not change.

## D-01 — 1998-08-10 Monday

Normality weight: very high.

> 午前は部活。暑くてみんなだらだらしてた。帰りに図書館へ寄って、借りてた本を一冊延長した。お母さんが桃を買ってきてたので夜に食べた。

Clues:
- Monday
- club schedule
- library slip exists

Forbidden:
- 水無坂
- 第八
- strange geography

## D-02 — 1998-08-11 Tuesday

> 午後の練習は体育館の点検でなし。由佳と電話して、土曜のお祭りどうするか話した。お母さんに土曜日スーパー付き合ってと言われた。

Clues:
- day after D-01
- club cancellation
- festival is upcoming Saturday
- shopping planned for Saturday

No anomaly.

## D-03 — 1998-08-13 Thursday

> 図書館の本を返してきた。返却日ぎりぎりだった。明日は夕方に市の試験放送があるらしい。土曜はお祭りだけど、混んでたら行かなくてもいいかな。

Clues:
- library due date
- “tomorrow” municipal test
- festival Saturday

No anomaly.

## D-04 — 1998-08-14 Friday

The page begins ordinary.

> 午前は家で宿題。夕方の試験放送、窓を閉めてても聞こえた。晩ごはん前、お母さんに変なことを言ったらしい。

Then:

> 自分ではちゃんと覚えてる。水無坂の家に帰らないと、と思った。玄関の右下に細い傷があって、階段は三段目だけ少し音が違う。台所の窓は流しの左。書いてる今も、そこへ帰らないといけない感じがする。でも私は今、家にいる。

This is the first diary occurrence of 水無坂.

Family event lock:
19:10 verbal statement 「水無坂の家に帰りたい」.

## D-05 — 1998-08-15 Saturday

> お母さんとスーパー。帰り、いつもの交差点で右に曲がりそうになった。水無坂へ行くならそっちだと思ったから。お母さんに言ったら「そんな道ないよ」と笑われた。笑われると、自分が間違ってる気がして少し安心する。

Ordinary:
- shopping memo confirms Saturday
- festival noises / neighborhood context can appear

Anomaly:
nonexistent turn.

## D-06 — 1998-08-17 Monday

> 午後、市の人に昨日からのことを聞かれた。私だけじゃなくて、同じあたりを知ってるっていう人がいるらしい。それを聞いたら安心するはずなのに、逆に怖くなった。

> 時計塔のない公園で遊んだことも思い出す。真ん中に丸い跡だけある。誰と遊んだかも一人だけ名前が出てくる。でも、その名前は書かない。

Character lock:
she hides nonexistent friend identity.

## D-07 — 1998-08-19 Wednesday

> また聞き取り。紙には「第八」と書いてあった。水無坂の話をすると担当の人が何度も同じところを聞く。帰ってから東三丁目のアルバムを見た。写真も部屋も全部知ってるのに、水無坂の家の階段の音まで知ってる。どっちかが嘘って感じがしない。

Important:
staff does not teach her new geography.
Administrative label only.

## D-08 — 1998-08-24 Monday

> 部活の子に久しぶりって言われた。普通に話してる間はいつもの自分だった。帰ると、東三丁目の家も水無坂の家も両方「帰る場所」みたいに思える。

> どっちかだけ本物だと言われると、もう片方の家族を自分で捨てるみたいで嫌だ。

Ethical/emotional center.

## D-09 — 1998-09-07 Monday

> 今日、玄関の傷がどの高さだったか急に分からなくなった。台所の窓も、流しの左だったと思うけど自信がない。前なら目を閉じればすぐ出てきた。

> 忘れた方がいいはずなのに、なくなっていくと焦る。

## D-10 — 1998-09-14 Monday

> 階段の三段目の音が、もう思い出せない。水無坂って字を見ると胸がぎゅっとするのに、家の中は前ほど浮かばない。

> ちょっと安心してる。たぶん。それと同じくらい、誰かの家を勝手に忘れてるみたいで寂しい。

Timeline lock:
mid-September detail loss.

# 2. In-World Ordering References

These references are embedded in SITE-003.

## R-01 Club Summer Schedule

```text
8/10 Mon  午前練習
8/11 Tue  体育館設備点検のため休止
8/12 Wed  自主練
8/17 Mon  午前練習
8/24 Mon  午後練習
```

## R-02 Library Slip

```text
貸出更新: 1998-08-10
返却期限: 1998-08-13
```

## R-03 Neighborhood Festival Flyer

```text
東三丁目 夏祭り
1998-08-15 Saturday
17:00–
```

## R-04 Family Shopping Memo

```text
土曜
夕方 スーパー
結も一緒
```

## R-05 Municipal Notice

```text
1998-08-14 Friday
18:00 防災行政無線 試験放送
```

All are fictional in-world materials.
No external lookup required.

# 3. PZ-006 Presentation

Initial scan order should be deliberately nonchronological.

Recommended initial order:
D-08, D-02, D-10, D-04, D-01, D-06, D-09, D-03, D-05, D-07.

Some visible date numerals can be obscured:
- D-02 day numeral obscured
- D-04 day numeral partially obscured
- D-05 day numeral obscured
- D-06 day numeral partly damaged

Weekday / ordinary references remain.

After solve:
display canonical dates and a simple before/after divider at 1998-08-14 18:00.

Do not animate a supernatural transformation.

# 4. Diary Search Invariant

Before canonical D-04:
occurrences of `水無坂` = **0**.

D-04 onward:
the term may appear naturally.

This is a machine-testable invariant.

# 5. Drawing Provenance

Use fictional child names only in production staging.

## DR-A

ID:
EV-018-A

Date:
1998-08-15

Source:
凪代市立東小学校 / family A

Collection:
parent voluntarily supplied drawing during initial inquiry.

Viewpoint:
park, looking toward slope.

Visible:
- round concrete-looking foundation in park center
- path/slope leaving park
- vending machine on slope
- blue fence higher up

Occluded:
- triangular-roof hall is not visible
- anything beyond the blue fence.

## DR-B

ID:
EV-018-B

Date:
1998-08-15

Source:
凪代市立北小学校 / family B

Viewpoint:
mid-slope, looking downhill.

Visible:
- vending machine near viewpoint
- park below
- circular foundation visible in park
- blue fence edge behind/uphill

Occluded:
- triangular-roof hall is not visible.

## DR-C

ID:
EV-018-C

Date:
1998-08-18

Source:
凪代市立臨海小学校 / family C

Viewpoint:
near hall, looking downhill.

Visible:
- triangular roof at edge/top
- blue fence close to hall
- vending machine farther downhill

Occluded:
- park / circular foundation are hidden below a bend
- lower street connection.

Independence:
- three households
- three schools
- no joint event
- no shared art class
- no shared reference image

# 6. Partial Topology v1

Canonical graph:

```text
PARK
  contains: ROUND_FOUNDATION
  connects_uphill_to: SLOPE

SLOPE
  contains_midway: VENDING_MACHINE
  upper_end_near: BLUE_FENCE

BLUE_FENCE
  beyond: TRIANGULAR_ROOF_HALL
```

Linear projection used by puzzle UI:

```text
Park → Vending machine → Blue fence → Triangular-roof hall
```

with `Round foundation` nested inside Park.

No compass direction.

No real-city coordinate.

No complete boundary.

# 7. EV-020 — 真壁 俊 作文

Date:
1998-08-18.

Source:
fourth household / school record independent of DR-A/B/C and 水城.

Title:
「夏休みに行きたいところ」

Key text:

> ぼくは時計のない公園に行きたいです。時計はないけど、まんなかに時計のあとみたいな丸いところがあります。

> 公園を出ると坂になっていて、途中にジュースの自動販売機があります。

Do not mention:
- blue fence
- triangular hall
- complete route

Function:
corroborates unusual park base + park-to-slope + vending relation.

# 8. EV-019 — Parent Interview Summary

Example rows:

### Household A
Child repeatedly refers to:
- 「水無坂」
- park with circular center mark

### Household B
Child describes:
- slope
- drink vending machine
- blue fence

### Household C
Parent reports child asked:
- whether triangular-roof meeting place had been demolished

Administrative caveat:
terms are summarized by interviewer.
Original wording is not fully preserved.

Therefore EV-019 is supporting evidence only.

# 9. PZ-007 Text Accessibility Descriptions

Do not replace drawings with answer statements.

### DR-A Description
“Park foreground. A circular base is drawn near center. A road rises away from the park. A vending-machine-shaped rectangle is partway up. A blue fence appears higher. What lies beyond the fence is outside the drawing.”

### DR-B Description
“View appears to be from a slope. A vending machine is closest. Below it is a park with a circular center shape. A blue fence edge appears behind/uphill. No building beyond it is visible.”

### DR-C Description
“Foreground includes a triangular roof edge and blue fence. A slope descends away. A vending machine is farther down. The lower end of the slope disappears behind a bend; the park is not visible.”

The player still has to infer topology.

# 10. PZ-007 Solve State

Player places:
- Park
- Vending
- Blue Fence
- Hall

into a relative chain.

Round Foundation is assigned inside Park.

Correct:
```text
Park → Vending → Blue Fence → Hall
```

Incorrect layouts should return neutral relational feedback such as:
“Drawing B and Drawing C cannot both be viewed from the positions implied by this arrangement.”

No gamey “wrong answer” buzzer.

# 11. Partial Map Artifact

After PZ-007:

Title:
`水無坂周辺 — 関係図（暫定）`

Contains only:
- park
- circular foundation
- slope
- vending
- blue fence
- triangular-roof hall

Label:
`方角・縮尺・市内位置 不明`

This prevents premature complete-map reconstruction.

# 12. Act 5 Lead

Archive note:

> 現在の公開地図上では、上記のランドマーク関係に一致する場所を確認できません。地域史料には年代別の市街地図が保存されています。

Link label:
`旧市街地図Collection`

Do not say:
- maps differ by year
- road appears later
- map changed
- archive rewrote itself

# 13. Act 4 Story Conclusion

Confirmed:
- 水城’s 水無坂 memory begins after 8/14
- memory is emotionally/episodically detailed
- unrelated children/families share terminology/features
- independent drawings encode compatible spatial topology
- independent essay repeats unusual park detail
- shared geography can be partially reconstructed

Not confirmed:
- that the place ever physically existed
- why memories align
- audio causality
- physical reality alteration
- record mutation
- containment mechanism

# 14. Emotional Endpoint

Desired player thought:

> 「偽物の記憶」だとしても、
> これだけの人が同じ家や公園を失ったと感じているなら、
> 彼らにとっては本当に“失った場所”なのではないか。

Then:

> その場所は、昔の地図にも本当に無いのか？
