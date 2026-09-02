# 第八避難区 — PUZZLE_LEDGER

Source of Truth:
- STORY_BIBLE.md
- NARRATIVE_GRAPH.md
- EVIDENCE_LEDGER.md

Design Rule:
謎は「次のURLを出すための障害」ではなく、解く過程そのものが事件理解を変えること。

## Difficulty Scale
1 = observation
2 = simple comparison
3 = multi-document reasoning
4 = cross-media synthesis
5 = final synthesis

---

# PZ-001 — Missing Eight

Act: 0
Difficulty: 1

Narrative Reason:
旧自治体サイトの復元が不完全で、asset規則だけ残っている。

Input:
- EV-001 現行避難区一覧
- EV-002 asset index
- EV-003 backup断片

Observed Pattern:
area01〜area07。
一箇所だけ参照番号が飛ぶ。

Required Insight:
「8を推測入力する」のではなく、複数のページ構造から欠番08が本当に存在したと確認する。

Solution:
欠番を示すasset referenceを特定し、失われた資料群へ到達。

Output:
「第八避難区」という探索対象。

Story Reveal:
単なる都市伝説ではなく、旧サイト構造上に痕跡がある。

Next Leads:
EV-004 / EV-005。

Hint 1:
避難区の本文ではなく、ページ同士で共通する規則を見る。

Hint 2:
画像・PDF名の番号を比較する。

Fallback:
EV-003から同じ結論へ到達可能。

Failure Risk:
URL総当たりゲームに見える。

Mitigation:
推測だけではなく明示的な構造証拠を2つ置く。

---

# PZ-002 — Deleted File Provenance

Act: 1
Difficulty: 2

Narrative Reason:
本文から削除された第八区の痕跡が、PDF作成履歴・元ファイル名に残った。

Input:
EV-004 / EV-005。

Observed Pattern:
公開タイトルと内部filenameが一致しない。

Required Insight:
複数PDFの文書プロパティを比較。

Solution:
source filenameの `area08_water` と作成日時を発見。

Output:
「第八区資料が独立ファイルとして存在していた」こと。

Story Reveal:
単なるタイプミスではない。

Next Leads:
旧八号集会所 / 文書番号。

Hint 1:
本文以外にも文書には情報が残る。

Hint 2:
作成者・作成日時・元ファイル名を比較。

Fallback:
ページ上に「文書情報を見る」UIを用意し、OS依存のPDF操作を不要にする。

Accessibility:
metadataはテキストで取得可能にする。

---

# PZ-003 — Document Number Gap

Act: 1–2
Difficulty: 2

Narrative Reason:
行政資料には連番の起案番号があり、削除資料があっても参照番号の整合が残る。

Input:
- EV-004
- EV-006
- EV-008

Observed Pattern:
防災第214号 → 216号。
215号への引用だけ残る。

Required Insight:
欠番文書番号を別資料の引用から逆引きする。

Solution:
215号 = 「臨時管理区分の設定」。

Output:
EV-007へ。

Story Reveal:
第八区は事件前の地理制度ではなく、事件後に設定された可能性。

Next Leads:
1998-08-19。

Hint:
見えない文書を探すのではなく、「引用されている文書」を探す。

Fallback:
議事録の脚注にも215号を記載。

---

# PZ-004 — Two Homes

Act: 2
Difficulty: 3

Narrative Reason:
行政の対象者名簿と学校資料が異なる住所を示す。

Input:
- EV-009
- EV-010
- 学籍番号
- 生年月日
- 旧電話帳

Observed Pattern:
同名人物だけでは同一人物と断定できない。

Required Insight:
氏名ではなく、生年月日・学校・保護者名を組み合わせる。

Solution:
水城結が同一人物でありながら、
- 東三丁目
- 第八避難区
の2住所を同時期に持つことを確定。

Output:
「第八区は普通の住所ではない」という疑問。

Story Reveal:
消された住民ではなく、既存住民へ第八区が重ねられている。

Next Leads:
水城日記。

Hint 1:
同姓同名の可能性を潰す。

Hint 2:
住所より変わりにくい属性を照合。

Fallback:
保護者名一致からも同一人物を確定可能。

---

# PZ-005 — 33 Seconds

Act: 3
Difficulty: 3

Narrative Reason:
複数地点の受信テープが劣化し、それぞれ別部分だけ聞き取りやすい。

Input:
- EV-011
- EV-012
- EV-013
- 時報基準音

Observed Pattern:
送信ログは27秒。
録音は60秒。

Required Insight:
時報／チャイム位置を同期点として複数録音を重ねる。

Solution:
27秒以降の33秒区間を復元。

Output:
「第八避難区」「水無坂」の断片。

Story Reveal:
送信設備に存在しない情報が受信側では一致する。

Next Leads:
1998-08-14問い合わせ / 水城日記。

Hint 1:
音そのものより、同じ瞬間を特定する目印を探す。

Hint 2:
冒頭と末尾のチャイムを基準にする。

Fallback:
波形合わせをGUIで補助。
完全手動編集ソフトを要求しない。

Accessibility:
聴覚だけを必須にしない。
同期済み文字起こし断片と波形位置でも解ける。

Failure Risk:
音声編集スキル依存。

Mitigation:
ゲーム内簡易alignment UIを実装候補。

---

# PZ-006 — Before and After

Act: 4
Difficulty: 2

Narrative Reason:
水城の日記ページが保管時に順不同になった。

Input:
EV-016 / EV-017。

Observed Pattern:
ページ番号の一部欠損。

Required Insight:
- 日付
- 天気
- 夏祭り
- 曜日
- 家族予定
を使って順序を確定。

Solution:
8/14以前と以後を正しい順に並べる。

Output:
事件前には水無坂の記述が一度もないこと。

Story Reveal:
水城が元々第八区住民だった説が弱まる。

Next Leads:
児童画 / 他家庭。

Hint:
異常記述ではなく普通の日常情報を使う。

Accessibility:
ドラッグ操作だけでなく選択式並び替えにも対応。

---

# PZ-007 — The Park Without a Clock

Act: 4
Difficulty: 3

Narrative Reason:
複数児童が描いた絵には、同じ街の部分的な視点だけが残る。

Input:
EV-018 / EV-020。

Observed Pattern:
それぞれ違う絵だが、
- 丸い基礎
- 青柵
- 三角屋根
- 坂
が共通。

Required Insight:
絵を「同じものを描いたコピー」ではなく「同じ場所の別視点」として扱う。

Solution:
ランドマーク間の相対位置を統合。

Output:
部分地図 v1。

Story Reveal:
独立人物が共通の架空空間を内部的に共有している。

Next Leads:
古地図比較。

Hint 1:
物の形より、何が何の隣にあるかを見る。

Hint 2:
各絵を方角の違うカメラとして考える。

Fallback:
作文EV-020に位置関係の言語ヒント。

Accessibility:
画像情報は位置関係テキストでも提供。

---

# PZ-008 — Map That Learns

Act: 4–5
Difficulty: 4

Narrative Reason:
同じ市街地図の保存版が年代ごとに微妙に異なる。

Input:
EV-021。

Observed Pattern:
基準道路・川・公共施設は一致。
一本だけ年代で濃さ／形が変わる線。

Required Insight:
スキャン画像の見た目比較ではなく、固定基準点で重ねる。

Solution:
1997 → 1998-07 → 1998-09 → 2001 の順で水無坂らしい道路が形成されることを確認。

Output:
「地図が過去を記録している」のではなく、「後から地図側が整合している」疑い。

Story Reveal:
現象は人間の記憶だけに閉じていない。

Next Leads:
桐谷研究ノート。

Hint:
変わらない場所を3点選び、それを基準にする。

Fallback:
ゲーム内overlay slider。

Accessibility:
差分座標をテキスト表でも提示。

---

# PZ-009 — Reverse Citation

Act: 5
Difficulty: 3

Narrative Reason:
桐谷研究ノートの危険な章は抜かれているが、他章から引用されている。

Input:
EV-024。

Observed Pattern:
存在しないページ／節への脚注が複数。

Required Insight:
削除箇所そのものではなく、引用文脈を集めて章の主張を再構成。

Solution:
「記述密度」と「再想起率」の相関を導出。

Output:
EV-025。

Story Reveal:
資料を増やすことが現象を弱めるどころか強める。

Next Leads:
削除命令 / 三枝再評価。

Hint:
欠けた文章を当てる必要はない。その文章を引用している箇所を見る。

Fallback:
3つの引用だけでも主要結論へ到達可能。

---

# PZ-010 — Why Did He Delete It?

Act: 5
Difficulty: 3

Narrative Reason:
三枝の個人サイトには、保存を訴える文章と後年の大量削除が同居する。

Input:
EV-028 / EV-029 / EV-030。

Observed Pattern:
思想と行動が矛盾。

Required Insight:
削除日時と三枝がデジタル化した資料の日時を並べる。

Solution:
資料再整理 → 異常再出現 → ページ削除 の順序を確定。

Output:
三枝は圧力で黙らされたのではなく、自発的に消した可能性。

Story Reveal:
内部告発者／英雄像が反転。

Next Leads:
EV-031。

Hint:
「何を消したか」だけでなく「いつ消したか」。

Fallback:
削除履歴と2007メモを相互リンク。

---

# PZ-011 — The Missing Whole

Act: 6
Difficulty: 5

Narrative Reason:
誰も完全な第八区地図を保持していない。
各人物の資料には一部分しかない。

Input:
- EV-005
- EV-016
- EV-018
- EV-020
- EV-021
- EV-023
- 桐谷ノートの距離表

Observed Pattern:
個別資料だけでは閉じた地図にならない。

Required Insight:
複数人物・複数年代・複数媒体を同じ座標系へ統合。

Solution:
水無坂、八号集会所、公園、バス停、住宅街を一意に配置。

Output:
EV-032 完全復元地図。

Immediate State Change:
SITE-007に第8区項目。
SITE-001にdistrict08 archive page。

Story Reveal:
プレイヤーが「失われた完成図を発見した」のではない。
プレイヤーが初めて完全図を作った。

This distinction must be explicit.

Hint 1:
資料ごとに正解地図が隠れているわけではない。

Hint 2:
共通ランドマークを座標の接点として使う。

Recovery:
重要ランドマークには最低2資料からの位置情報。

Accessibility:
マウス操作以外に座標選択UI。
色だけで区別しない。

---

# PZ-012 — Seven Became Eight

Act: 6
Difficulty: 1 observational / 4 interpretive

Narrative Reason:
最終復元後、最初に見た普通のページが静かに変わる。

Input:
EV-001 remembered state + EV-033 / EV-034。

Observed Pattern:
同じURL。
同じUI。
第8避難区だけが自然に追加されている。

Required Insight:
「新しいゲーム画面」ではなく、序盤の現実基準ページを見直す。

Solution:
変更を確認。

Output:
Final Recontextualization。

Story Reveal:
調査は観測ではなく生成だった可能性が確定。

Next:
Ending choice。

Hint:
最初に見たページへ戻る。

No visual glitch:
赤文字・ノイズ・警告演出を使わない。

Horror comes from normality.

---

# Puzzle Dependency Graph

```text
PZ-001 Missing Eight
  ├─ PZ-002 PDF Provenance
  │    └─ PZ-003 Document Number Gap
  │          └─ PZ-004 Two Homes
  │
  └─ alternate recovery ───────────────┐
                                       │
PZ-004 Two Homes                       │
  └─ PZ-006 Diary Order                │
        └─ PZ-007 Children's Map       │
              └─ PZ-008 Map That Learns
                                       │
PZ-003 / date clues                    │
  └─ PZ-005 33 Seconds                 │
              └────────────────────────┤
                                       ▼
                              PZ-009 Reverse Citation
                                       │
                              PZ-010 Why Delete It
                                       │
                              PZ-011 Missing Whole
                                       │
                              PZ-012 Seven Became Eight
                                       │
                                     END
```

## Deadlock Review

Hard dependencies:
- PZ-011 requires discoveries from branches, not every optional artifact.
- Audio PZ-005 cannot be the sole gateway to Act 4.
- PZ-008 and PZ-009 each have alternate leads into Act 5.
- If image puzzles fail, textual evidence can establish the same narrative fact.
- No puzzle requires proprietary desktop software.

## Hint Philosophy

Hint levels:
1. Direction — what category to inspect
2. Method — how to compare
3. Near-solution — precise elements to use
4. Recovery — bypass mechanical work but preserve Story Reveal

Using a hint must not remove the narrative payoff.

## Puzzle Quality Gate

Every major puzzle must answer YES:
- Does solving it reveal story information?
- Could a player explain why this puzzle exists in-world?
- Is brute force unnecessary?
- Is at least one hint available?
- Is required information duplicated across independent media where needed?
- Is the puzzle usable on mobile or does it have a mobile alternative?
- For audio/image tasks, is there an accessibility-equivalent route?
