# 第八避難区 — ACT 3 CONTENT BIBLE

Status: Exact-copy / timing draft for staging implementation
Act 0–1 runtimeには未接続。

# 1. Fixed Incident Clock

Date:
**1998-08-14 Friday**

Canonical timeline:

| Absolute Time | Sender | Receiver A | Receiver B |
|---|---|---|---|
| 18:00:00.000 | START | normal test begins | normal test begins |
| 18:00:27.000 | END / NORMAL | audio continues | audio continues |
| 18:00:27–18:01:00 | no transmission logged | surplus content | surplus content |
| 18:01:00.000 | — | relevant 60s window ends | relevant 60s window ends |
| 18:12 | — | first inquiry logged | — |
| 18:25 | — | 3 similar inquiries totalled | — |

Arithmetic invariant:

```text
60 - 27 = 33 seconds
```

# 2. EV-011 — 防災無線送信ログ

Header:

```text
凪代市 防災行政無線
自動送出記録
1998年8月14日
```

Visible rows:

```text
17:59:58  SYSTEM READY
18:00:00  START   TEST_0814   SCHEDULED
18:00:27  END     TEST_0814   NORMAL
18:00:27  SYSTEM  STANDBY
```

Source information:

```text
Source ID: TEST_0814
Recorded duration: 00:27.000
Aux input: OFF
Manual override: NONE
```

Do not include any row after 18:00:27 implying another transmission.

# 3. Normal 27-Second Source

The exact spoken copy can be finalized during audio production, but semantics are locked.

Must be mundane.

Example structure:

```text
[chime]
「こちらは凪代市です。
防災無線の試験放送です。
これは試験放送です。
ご協力ありがとうございました。」
[normal closing chime]
```

Target duration:
27.000s including chimes.

No:
- 第八
- 水無坂
- unusual instructions

# 4. EV-012 — Tape A Provenance Copy

Title:
`市内受信録音 A / 1998-08-14 18:00`

Archive note:

> 1998年8月14日夕方に市内東部で録音されたカセットテープの一部です。寄贈者宅で録音機が作動中だった際、屋外の防災放送が入ったものとされています。

> 原テープは複数回の再生による摩耗があり、28〜41秒付近にドロップアウトと速度揺れがあります。

Provenance:
- donor family archive
- label handwritten 「8/14 夕方」
- donated 2011
- digitized 2024

Reliability note:
exact recorder clock was not synchronized to municipal time.

Important:
The published comparison UI uses the known test chime to normalize its relevant 60-second window.

# 5. EV-013 — Tape B Provenance Copy

Title:
`地域FM監視録音 B / 1998-08-14 18:00`

Archive note:

> 当時の地域FM局が、自治体からの公共情報を確認する目的で運用していたモニター受信機の記録です。

> テープケース、局内記録簿、保存番号が一致しており、1998年以降同局資料室で保管されていました。

Provenance:
- separate receiver location
- station equipment
- archive identifier
- continuous custody
- digitized independently from Tape A

Reliability:
Confirmed.

Do not say:
“this proves paranormal activity”.

# 6. Receiver 60-Second Timeline

This is a **content map**, not a literal final waveform.

## 00.000–27.000
Normal test broadcast.

Tape A:
more environmental noise.

Tape B:
cleaner speech, light receiver hiss.

Both match the semantic content of TEST_0814.

## 27.000–30.800
Sender has ended.

Receiver recordings:
low-level noise continues.
A faint structured signal becomes visible in both waveforms after alignment.

No clear words yet.

## 30.800–36.400
Shared voice-like segment.

Tape A clarity:
medium.

Tape B clarity:
poor at first, then medium.

Composite recoverable:
「……第八避難区の方は……」

Do not expose entire phrase on either unsolved single-tape transcript.

Suggested split:
- Tape A clearly exposes 「……第八……の方は……」
- Tape B clearly exposes 「……避難区……」

## 36.400–43.900
Mostly unintelligible shared speech/noise.

Possible low-confidence fragment:
「……そのまま……」

This fragment is optional and must never be required.

## 43.900–49.200
Second semantic region.

Suggested split:
- Tape A: 「……みな……ざか……」 with dropout
- Tape B: 「……水無…坂……」 with different dropout / clearer consonant boundaries

Before alignment, neither displayed transcript may present the complete place name as confirmed text.

After alignment/comparison:
confidence sufficient for 「水無坂」.

## 49.200–57.800
Unintelligible voice-like continuation.

No additional major proper noun.

## 57.800–59.150
Short chime.

Properties:
- same timing/shape across receivers after alignment
- different from normal municipal test chime
- not present in sender source

## 59.150–60.000
noise tail / end of relevant comparison window.

# 7. Transcript Display Rules

## Before alignment
Tape A transcript:
- normal 0–27s text
- sparse fragments
- no complete 「第八避難区」
- no complete 「水無坂」

Tape B transcript:
same principle, different gaps.

## After first anchor
show improved time correspondence but no composite answer.

## After two-anchor alignment
unlock composite fragment table.

Example:

| Time | A | B | Composite |
|---|---|---|---|
| 31.4–35.8 | 第八…の方は | …避難区… | 第八避難区の方は… |
| 44.4–48.1 | みな…ざか | 水無坂 | 水無坂 |
| 58.0–59.1 | [短いチャイム] | [短いチャイム] | shared non-source chime |

Uncertainty must remain visible.

# 8. PZ-005 UI Copy

Title:
`1998-08-14 受信記録 比較`

Neutral instruction:

> 2つの記録は録音機器と保存状態が異なるため、そのままでは時間軸が一致しません。共通する音を基準に位置を合わせることができます。

Do not say:
- “find the hidden 33 seconds”
- “solve the mystery”
- “paranormal”

Controls:
- 再生 / 停止
- ±0.1 sec nudge
- anchor A
- anchor B
- region replay
- waveform/text mode

Success-state copy:

> 2記録の時間軸を補正しました。

Then show sender-end marker and composite comparison.

# 9. EV-014 — 片瀬保守報告書

Header:

```text
設備保守確認報告
1998年8月15日
担当: 片瀬 亮介
```

Body semantics:

> 8月14日18時00分の定時試験放送について、送出装置の自動記録を確認した。

> 使用音源 TEST_0814 の記録長は27秒であり、18時00分27秒に正常終了している。

> 補助入力は選択されておらず、手動送出操作の記録もない。

> 送信機、制御装置、時刻制御について翌15日に再試験を実施したが、異常動作を再現できなかった。

> 複数地点から申告された追加音声については、当設備の送出記録から発生源を特定できない。

> 外来混信を含め確認を継続する。

Tone note:
片瀬は自分の責任を否定したい。
過度に断定的な「絶対に送っていない」は避ける。

# 10. EV-015 — 8/14問い合わせメモ

Header:

```text
8月14日 市民問い合わせ
防災課 内線メモ
```

Rows:

```text
18:12
試験放送について
「第八ってどこですか」
担当: 片瀬
→ 通常試験放送のみと回答

18:25
同様問い合わせ 3件
「第八」「避難区」についての確認
→ 内容確認中
```

Do not add 水無坂 to the memo unless later story review explicitly requires it.

Reason:
第八 vocabulary gets immediate corroboration.
水無坂 remains the audio-derived Act 4 lead.

# 11. SITE-005 Home Ordinary Content

To avoid “audio puzzle website” feeling:

Visible collections:
- 1996 商店街夏祭り録音
- 1997 港まつり中継
- 1998 台風7号関連放送
- 1998-08-14 市内受信記録
- 2001 市制記念番組
- cassette preservation guide
- receiver history article

At least half the visible index should not concern 第八避難区.

# 12. Equipment Page

Explain only what player needs:

- Tape A = acoustic outdoor-speaker capture
- Tape B = receiver monitor recording
- analog cassette can drift slightly
- digitization can align known common sounds
- waveform similarity is useful even when words are unclear

Do not turn this into an RF engineering course.

# 13. Digitization Note

Author:
高瀬章子.

Tone:
archivist, not investigator.

Copy concept:

> AとBは由来の異なるテープですが、通常試験放送部分のチャイムと読み上げ位置が一致するため、同時刻の記録として比較可能と判断しました。

> 劣化の大きい区間については、内容を推測して補完せず、聞き取れない部分をそのまま残しています。

This protects puzzle fairness:
the archive is not inventing missing speech.

# 14. Act 3 Discovery Order

Preferred:

```text
8/14 reference
→ EV-015 inquiry memo
→ 18:00 test broadcast
→ EV-011 sender log
→ SITE-005 1998-08-14 collection
→ Tape A / B provenance
→ PZ-005 alignment
→ 33-second surplus
→ 第八避難区 predates 8/19
→ 水無坂
→ search 水無坂
→ Act 4
```

Alternate:
radio archive can be found before sender log, but sender/receiver contradiction must be established before Act 3 is considered solved.

# 15. Story Conclusion at Act 3

Confirmed:
- sender ends at 27s
- receivers contain common content to 60s
- surplus = 33s
- 第八 vocabulary existed by 8/14
- 水無坂 is present in the receiver-side surplus

Not confirmed:
- why it happened
- whether transmission was supernatural
- whether Katase caused it
- whether the city knew beforehand
- whether 水無坂 was a real place
- whether the audio caused the later memories

# 16. Exit

Player-facing search target:
`水無坂`

Desired final thought:

> 「第八避難区」が後から作られたなら、
> 8月14日の声は何を知っていた？
> そして水無坂を覚えていた人は誰だ？

The next Act should answer the second question before the first.
