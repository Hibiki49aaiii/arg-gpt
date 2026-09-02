# 第八避難区 — Blind Playtest Protocol

Status: Human Gate
Target: Act 0〜1 Vertical Slice

## 1. Purpose

このPlaytestは「謎が解けるか」だけを測らない。

確認する中心命題:

> 作者から説明されていない初見ユーザーが、普通の復元自治体サイトから自発的に違和感を発見し、最終的に「第八避難区は何だったのか？」を調べたいと思うか。

## 2. Testers

最低推奨:
- A: ARG / 謎解き経験ほぼなし × 2
- B: 謎解き経験あり、ARG経験少 × 2
- C: ARG / Web探索経験あり × 1

最低5セッションを1ラウンドとする。

同じテスターを修正版の「初見」として再利用しない。

## 3. Environment

Start:

```bash
python3 works/001-district-eight/implementation/vertical-slice/serve_playtest.py
```

Default URLs:

```text
Facilitator control:
http://127.0.0.1:8000/meta/playtest.html

Tester entry:
http://127.0.0.1:8000/old-bousai/
```

The launcher binds to localhost by default and opens the Facilitator control page.
Do not show the Facilitator page to the tester.

Before every session:
1. Facilitator controlを開く
2. 個人情報を含まないSession IDを設定する（例: PT-A01）
3. 「セッション状態をリセット」
4. Tester entry URLだけをテスターへ渡す
5. Browser cacheは通常状態でよい
6. 前テスターのメモ・検索履歴を見せない

## 4. Exact Facilitator Script

テスターへ伝えるのは以下だけ。

> この復元サイトを自由に見てください。  
> 気になることがあれば調べて構いません。  
> 操作が壊れていると思った場合も、その時点で感じたことを口に出してください。

禁止:
- 「謎解きです」
- 「8に注目してください」
- 「資料を見てください」
- 「ソースを見てください」
- 「第八避難区を探してください」
- ストーリー設定の説明

## 5. Think-Aloud

可能ならテスターへ、
「考えていることをそのまま口に出してよい」
とだけ伝える。

正解／不正解のフィードバックはしない。

Facilitator responses:
- 「なるほど」
- 「そのまま続けてください」
- 「今そう思った理由は何ですか？」

Avoid:
- 「惜しい」
- 「そこ重要」
- 「もう一回見て」
- 表情で正解を示す

## 6. Time Box

Primary observation:
30 minutes.

0–20 min:
No hint.

20–30 min:
完全停止している場合のみ、Observerが「何を見たか整理しても構いません」と言える。
具体的な場所・数字・文書名は示さない。

30 min:
いったん終了。

攻略完走より、自然発見率を優先する。

## 7. What to Observe

Record timestamps for:
- Entry
- First click
- First noticed anomaly
- First mention of "8"
- First visit to area08 missing page
- First administrative document opened
- First explicit recognition of 第八避難区
- First visit to 史料アーカイブ
- Session end

Also record:
- Route A / B / C
- backtracking
- accidental exits to meta page
- confusion interpreted as site bug
- whether tester uses search
- whether tester expects a conventional puzzle answer

## 8. Post-Session Questions

Ask in this order. Do not reorder based on what you want to hear.

### Q1
「今、何が起きていたと思いますか？」

### Q2
「一番気になったものは何でしたか？」

### Q3
「続きがあるなら、次に何を調べたいですか？」

### Q4
「このサイトで意図的に消された、または欠けていると思ったものはありますか？」

### Q5
Only after free responses:
「“第八避難区”という言葉をどう理解しましたか？」

### Q6
「ゲーム／謎解きだと感じたのはいつですか？ それとも感じませんでしたか？」

### Q7
「作り物っぽい、作者に誘導されている、と感じた場所はありましたか？」

## 9. Metrics

### M1 — Evidence Reach
80%+ が明示的なヒントなしで EV-004 または EV-005へ到達。

### M2 — Central Anomaly
60%+ が30分以内に「第八避難区」を主要な異常として認識。

### M3 — Voluntary Continuation
60%+ がQ3で、
- 第八避難区
- 旧八号集会所
- 消えた8番
のいずれかを自発的に調べたいと回答。

### M4 — Puzzle-menu Avoidance
過半数が「次の暗号の答えを探すゲーム」ではなく「何があったか調べる」と表現。

### M5 — Bug Misclassification
「単なるサイト不具合」と結論して離脱するテスターが20%未満。

### M6 — Recovery
Primary routeを逃したテスターのうち、最低1名がRoute BまたはCで自然復帰。

## 10. Gate Decision

### PASS
- M1 / M2達成
- M3 60%以上
- 致命的dead endなし
- Act 2 spoilerなし
- 最終質問が概ね「第八避難区とは何か」に向く

### REVISE
世界観への興味は成立するが、
- 欠番が見つからない
- documentsへ進めない
- bug扱いが多い
- 08が露骨すぎる
- puzzle menu感が強い

場合。

修正はTrail / ordinary content / clue salienceを優先。
Final Truthを追加説明して解決しない。

### FAIL
- 多数が何も異常を認識しない
- 第八区の存在が単なる作者のミスにしか見えない
- 謎の意味よりmechanical password huntingが中心になる
- 明示的説明なしでは進行不能

## 11. Telemetry

Local-only keys:
- `district8-vs-state`
- `district8-vs-events`

Playtest後:
Facilitator control `/meta/playtest.html` で、
1. Session IDを確認
2. 「状態を表示」
3. 「JSONをファイル保存」

Export payload includes:
- anonymous `session_id`
- `exported_at`
- local `state`
- local `events`

The tool does not upload telemetry.
JSON remains browser-local until the facilitator explicitly saves it.

Example Session ID:
`PT-A01`

Do not record:
- real name
- email
- IP
- account ID
- personal browsing history

## 12. Change Discipline

各Blind Playtest round後:
1. Observationsを集計
2. 問題を「発見性 / 理解 /没入 / 操作」に分類
3. 1問題につき最小変更
4. validator実行
5. 新しい初見テスターで再試験

テスターの発言をそのまま仕様変更理由にしない。
複数セッションで再現する問題を優先する。

## 13. Machine Gate

各Blind Playtest roundの開始前に以下がPASSしていること。

```bash
python3 works/001-district-eight/implementation/vertical-slice/validate.py
```

Human observationはこのmachine gateを置き換えず、両方を満たして初めて次Actへ進む。


## 14. Operator Runbook

Operational short-form:
`PLAYTEST_OPERATOR_RUNBOOK.md`

The runbook may simplify setup steps, but this `PLAYTEST.md` remains authoritative for:
- facilitator wording
- tester composition
- 30-minute timing
- M1–M6 metrics
- PASS / REVISE / FAIL decision
