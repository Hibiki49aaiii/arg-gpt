# 第八避難区 — Full Staging Status

Status: **Engineering Readiness Pending Master CI**
Narrative Release Gate: **Issue #8 Human Blind Playtest Round 1**

## Current Position

Story / Timeline / Character Knowledge / Evidence / Puzzle / Site / Media / Domain architectureを固定し、
Act 0〜6の各Stagingを分離実装・個別検証済み。

現時点では、各後続ActはHuman Blind Playtest Issue #8を迂回して現行Trailへ接続していない。

## Act Status

| Act | Runtime / Staging | Core | Machine Gate |
|---|---|---|---|
| Act 0–1 | Vertical Slice | Missing Eight / administrative traces | PASS |
| Act 2 | isolated staging | Document 215 / Two Homes | PASS |
| Act 3 | isolated staging | 33 Seconds / independent receivers | PASS |
| Act 4 | isolated staging | Human Memory / Shared Geography | PASS |
| Act 5 | isolated staging | Records / Reverse Citation / Saegusa | PASS |
| Act 6 | isolated staging | Missing Whole / Seven Became Eight / Endings | PASS |

## Narrative Spine

```text
Act 0–1
第八避難区の痕跡
→
Act 2
地理区ではなく事件後の管理区分
→
Act 3
送信27秒 / 受信60秒 / receiver-only 33秒
→
Act 4
8/14以降に複数人が共有する存在しない生活地理
→
Act 5
後年記録の整合 / 記述と再想起の相関 / 保存から削除への反転
→
Act 6
誰も持っていなかった完全地理をPlayerが初生成
→
同じReality Anchorが1〜7から1〜8へ普通に整合
→
保存範囲を選択
```

## Act 0–1 — Vertical Slice

Core:
- area08 orphan trace
- EV-004 「第八避難区対象者」
- EV-005 「第八避難区 / 旧八号集会所」
- Recovery Route A/B/C
- developer-tool-free player route
- Blind Playtest telemetry/reset tooling

Local:
```bash
python3 -m http.server 8000 --directory works/001-district-eight/implementation/vertical-slice/sites
```

## Act 2

Core:
- 防災第214 → missing 215 → 216
- 防災第215号 = 1998-08-19
- 管理区分08 / 呼称「第八避難区」
- existing address + management classification split
- 水城結 identity verification

Local:
```bash
python3 -m http.server 8100 --directory works/001-district-eight/implementation/act2-staging/site
```

## Act 3

Core:
- Sender 27.000s
- Receiver A/B 60.000s
- receiver-only 33.000s
- independent receiver chains
- alignment before composite revelation
- non-audio equivalent route

Local:
```bash
python3 -m http.server 8200 --directory works/001-district-eight/implementation/act3-staging/site
```

## Act 4

Core:
- 10 diary fragments
- pre-8/14 水無坂 occurrence = 0
- five in-world ordering references
- three independent child-drawing sources
- partial geography only
- text-equivalent topology route

Local:
```bash
python3 -m http.server 8300 --directory works/001-district-eight/implementation/act4-staging/site
```

## Act 5

Core:
- map / phonebook record-side differences
- Kiritani reverse-citation structure
- containment correlation without causal overclaim
- Saegusa preservation → concern → voluntary deletion
- Act 6 player causality remains unrevealed

Local:
```bash
python3 -m http.server 8400 --directory works/001-district-eight/implementation/act5-staging/site
```

## Act 6

Core:
- 6! = 720 candidate assignments
- unique complete geography = exactly one solution
- EV-032 generated synthesis, not a found master map
- SITE-007 State A/B
- SITE-001 /08 State A/B
- both anchors required for PZ-012
- END-A / END-B / END-C mechanically distinct
- no glitch / alert state-change presentation

Local:
```bash
python3 -m http.server 8500 --directory works/001-district-eight/implementation/act6-staging/site
```

## Engineering Readiness

Individual validators:
- Vertical Slice validator
- Act 2 validator
- Act 3 validator
- Act 4 validator
- Act 5 validator
- Act 6 validator

Cross-act:
- `full-readiness/validate_full_story.py`

The master regression workflow must pass all of them in one PR.

## 唯一のNarrative Release Gate

**Issue #8 — Human Blind Playtest Round 1**

Required:
- ARG / 謎解き経験ほぼなし ×2
- 謎解き経験あり / ARG少 ×2
- ARG経験あり ×1

Human Gate confirms what machine validation cannot:
- anomaly discoverability
- curiosity
- bug misclassification
- puzzle-menu feeling
- voluntary continuation
- actual player comprehension

Until Issue #8 passes:
- do not integrate Act 2〜6 into the current public trail
- do not declare Act 0–1 narrative salience frozen
- do not publicly release the complete experience

## Not Yet Production-Hardened

Machine-complete staging does **not** mean public-release complete.

Still separate future work after the Human Gate includes:
- final visual assets
- final recorded audio
- full mobile/browser QA
- real domain/DNS
- production deployment
- indexing/cache policy validation
- final privacy/analytics review
- final public fiction-boundary review
