# 第八避難区 — ACT 3 IMPLEMENTATION

Status: Preproduction
Act: 3 — 33 Seconds
Human Gate: Act 0–1 Issue #8 pending

## 1. Purpose

Act 3でプレイヤーの問いを、

> 「8月14日に何があった？」

から、

> 「送信されていない33秒を、なぜ複数地点が同じように受信した？」

へ変える。

ここで初めて、行政の隠蔽だけでは説明できないTechnical Contradictionを確定させる。

ただしMechanismは説明しない。

## 2. Entry Knowledge

Act 2終了時:

- 第八避難区は1998-08-19に管理区分08として設定
- 第1〜7区の地理区域は変更されていない
- 水城結は事件前から東三丁目在住
- 「第八」は人へ付与された分類
- 対象者記録の共通起点は1998-08-14

Player Theory:
「8月14日に行政が隠している事件があり、その関係者を第八区として管理した」

## 3. Act 3 Core Contradiction

### Sender
1998-08-14 18:00:00 start.
1998-08-14 18:00:27 end.

Duration:
**27.000 seconds**

Sender-side records contain:
- normal test broadcast
- no 第八避難区
- no 水無坂
- no second source
- no continuation after 18:00:27

### Receivers
Independent receiver recordings preserve audio until 18:01:00.

Shared surplus interval:

```text
18:00:27.000 → 18:01:00.000
= 33.000 seconds
```

The surplus content is not fully intelligible.

Recoverable composite fragments:
- 「……第八避難区の方は……」
- 「……水無坂……」
- voice gender indeterminate
- final short chime does not match the normal municipal test chime

## 4. Critical Temporal Reversal

The phrase 「第八避難区」 is received on **1998-08-14**.

The administrative label 「第八避難区」 is formally created on **1998-08-19**.

This must be discoverable without an author explaining the implication.

The 8/14 inquiry memo provides independent historical support:
listeners were asking about 「第八」 immediately after the broadcast, before the 8/19 document existed.

This prevents the easy explanation:
「後年の行政資料を知った人がテープを加工しただけ」。

## 5. PZ-005 — 33 Seconds

Difficulty: 3

### Inputs
- EV-011 sender log
- EV-012 Tape A
- EV-013 Tape B
- common timing anchors
- waveform / transcript-fragment UI

### Mechanical Task
Two recordings have:
- different noise
- different dropout
- slight cassette-speed drift
- different intelligibility by segment

Player aligns them using common anchors in the normal 27-second portion.

### Required Insight
The important comparison is not which recording “sounds scarier”.

The player must distinguish:

```text
what transmitter says it sent
vs
what two independent receivers contain
```

### Solution
Once aligned:
- both receiver waveforms continue after sender end
- the continuation is structurally correlated for 33 seconds
- different clear fragments combine into the same impossible vocabulary

### Story Reveal
The 33 seconds are not present in sender-side source/log evidence, yet are independently preserved at receivers.

## 6. Alignment Design

Do not require external DAW/audio editor.

In-world viewer:

```text
Sender Log     |===========================| END
Tape A         |===========================|.................................|
Tape B         |===========================|.................................|
                0                         27                                60
```

Player controls:
- nudge Tape A ± time
- nudge Tape B ± time
- lock anchor
- play 3-second region
- toggle waveform
- toggle transcript fragments
- keyboard controls

The UI may apply small simulated drift correction after two anchors are chosen.

This is not a precision audio-engineering exam.

## 7. Timing Anchors

Use ordinary audio, not puzzle sound effects.

### Anchor 1
Opening test chime / known municipal melody onset.

### Anchor 2
Normal test-message closing chime ending near sender t=27.

Two anchors allow:
- start offset correction
- small cassette-speed drift correction

### Unknown Final Chime
Near the end of the surplus 33 seconds.

Important:
This final short chime is **not** a valid alignment anchor.
It differs from the normal test chime.

It is evidence content, not a tool hint.

## 8. Tape Provenance

### EV-012 — Tape A
Owner:
fictional local resident archive donation.

Original context:
a household cassette recorder was already running during the evening test.

Capture path:
acoustic capture of a nearby outdoor disaster speaker.

Why Mostly Reliable:
- provenance reconstructed from donation notes
- cassette has wear/dropouts
- no continuous custody chain from 1998 to digitization

Strength:
physically local reception.

### EV-013 — Tape B
Owner:
regional FM preservation archive.

Original context:
station maintained an off-air/monitor receiver used to log municipal public-information transmissions.

Capture path:
separate receiver hardware and recorder at another location.

Why Confirmed:
- station archive index
- dated tape box
- contemporaneous logging sheet
- continuous archive custody

Strength:
independent receiver chain.

Do not imply Tape B copied Tape A.

## 9. EV-011 Sender Log

SITE-001 / old municipal archive.

Required fields:

```text
1998-08-14
18:00:00 START
source: TEST_0814
mode: scheduled
18:00:27 END
result: NORMAL
```

Attached source duration:
27 seconds.

No:
- 第八
- 水無坂
- 60 sec entry
- second transmission

## 10. EV-014 — Katase Maintenance Report

Character:
片瀬亮介.

Tone:
technical, defensive, slightly over-explanatory.

Visible claims:
- source audio length 27s
- scheduler triggered normally
- transmitter stop logged at 18:00:27
- no auxiliary input selected
- post-event equipment inspection found no reproducible fault
- external interference source not identified

Narrative role:
supports sender/receiver contradiction.

Reliability:
Biased.

Important:
This document does **not** prove Katase innocent.
It proves only what was and was not recorded by the inspected system.

## 11. EV-015 — Inquiry Memo

SITE-002.

Exact historical anchors:

```text
18:12
「第八ってどこですか」

18:25
同様問い合わせ 3件
```

Purpose:
The vocabulary appears in human response minutes after the broadcast.

This evidence is more important than simply “people were scared”.

## 12. Surplus Audio Content

The 33 seconds should not be a fully decipherable monologue.

Target:
roughly 70–80% ambiguous/noisy,
20–30% recoverable through combining sources.

### Shared Semantic Fragments
Required:
- 第八避難区
- 水無坂

Optional low-confidence fragments:
- 「……方は……」
- 「……そのまま……」
- 「……ください……」

Do not add:
- explanation of what 第八区 is
- entity name
- threat
- player address/name
- prophecy
- overt supernatural statement

## 13. Horror Direction

Horror source:
**bureaucratic normality in the wrong causal order.**

Not:
- demonic voice
- whisper in player's headphones
- reverse speech
- sudden volume spike
- scream
- BGM sting
- glitch overlay

Ideal emotional beat:

1. technical curiosity
2. “there really is extra audio”
3. recognition of 第八避難区
4. realization that the term predates the code by five days
5. 水無坂 appears
6. desire to search who remembered 水無坂

## 14. Red Herring — Secret Broadcast

Intended theory:
片瀬 or a hidden municipal subsystem transmitted a secret second message.

Evidence that supports this theory:
- Katase was on duty
- admin later hides records
- the 33 seconds sound like public-information speech
- the city later adopts the same term

Evidence that weakens it:
- sender log/source only 27s
- separate receiver chains contain the same surplus
- immediate inquiry precedes later administrative documents
- equipment fault cannot be reproduced

Do not kill the Red Herring in Act 3.
It should remain plausible into early Act 4.

## 15. SITE-005 Page Contracts

### A3-S5-001 /
凪代地域ラジオ保存会 home.

Ordinary content:
- local broadcast recordings
- equipment articles
- digitization projects
- unrelated 1990s audio

### A3-S5-002 /1998-08-14/
Collection page.
Introduces Tape A / Tape B without saying “33 seconds anomaly”.

### A3-S5-003 /recordings/a
Tape A provenance + player.

### A3-S5-004 /recordings/b
Tape B provenance + player.

### A3-S5-005 /compare/1998-08-14
PZ-005 alignment UI.

### A3-S5-006 /equipment
receiver / cassette / digitization context.

### A3-S5-007 /interviews/katase
EV-014 / later interview framing.

### A3-S5-008 /digitization-notes
custody / restoration notes.

## 16. Cross-Site Act 3 Inputs

SITE-002:
- EV-015 inquiry memo

SITE-001:
- EV-011 sender log

SITE-005:
- EV-012 / 013 / 014
- PZ-005

Act 3 must require comparison across at least two organizations.

## 17. Recovery Routes

### Route A — 8/14 Inquiry
Act 2 exit → inquiry memo → 18:00 test broadcast → sender log.

### Route B — Sender Log
1998-08-14 search → sender log → preservation note points to independent receiver archive.

### Route C — Radio Archive
anniversary/digitization index → 1998-08-14 collection → compare with municipal sender log.

Audio puzzle recovery:
- waveform alignment
- timing table
- partial transcript
- synchronized marker list

No single inaccessible audio detail may be the sole proof.

## 18. Accessibility Equivalent

A deaf/hard-of-hearing player must be able to reach the same story conclusion.

Provide:
- waveform envelopes
- timestamped transcript fragments
- confidence markers
- duration table
- shared-feature markers
- explicit sender-end marker at 27s

Do not provide a full composite transcript before puzzle completion.

After solving:
show a synchronized composite text with uncertainty retained.

## 19. Act 4 Lead

The key new search term:
**水無坂**

After PZ-005:
searching 水無坂 in controlled archives should lead toward:
- 水城結の日記
- later human-memory records

Do not yet show:
- common child drawings
- map mutation
- research theory
- record-density mechanism

Final Act 3 question:

> 水無坂を、誰が覚えていた？

## 20. Human-Gate Isolation

Until Issue #8 PASS:
- no links from current Act 0–1 Vertical Slice to Act 2/3 staging
- no alteration to current Act 0–1 clue salience

Act 3 staging/preproduction may exist separately.

## 21. Definition of Done

Act 3 preproduction is complete when an implementer can create sender logs, two independent receiver artifacts, the alignment UI, accessibility route, Katase evidence, inquiry memo, and Act 4 lead without inventing timing, provenance, vocabulary, or spoiler boundaries.
