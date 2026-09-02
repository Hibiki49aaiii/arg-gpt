# 第八避難区 Vertical Slice

Act 0〜1 の静的プロトタイプ。

## 起動

通常のBlind Playtestでは専用launcherを使用:

```bash
python3 works/001-district-eight/implementation/vertical-slice/serve_playtest.py
```

Default:
- Facilitator: `http://127.0.0.1:8000/meta/playtest.html`
- Tester: `http://127.0.0.1:8000/old-bousai/`

ブラウザを自動起動しない場合:

```bash
python3 works/001-district-eight/implementation/vertical-slice/serve_playtest.py --no-browser
```

## 検証

```bash
python3 works/001-district-eight/implementation/vertical-slice/validate.py
```

外部依存・ビルド工程はありません。

## 実装対象

- SITE-001 旧凪代市防災情報ミラー
- SITE-002 凪代市史料デジタルアーカイブ最小シェル
- VS-001〜VS-008
- PZ-001 Missing Eight
- PZ-002 Deleted File Provenance
- Recovery Route A/B/C

このプロトタイプにはAct 2以降の真相を含めません。

## CI

GitHub Actions `.github/workflows/vertical-slice-validate.yml` で、リンク・Spoiler境界・Recovery Route・Act 1資料整合性を検証します。

## Blind Playtest

- Protocol: `../../PLAYTEST.md`
- Observer Sheet: `../../PLAYTEST_OBSERVER_SHEET.md`
- Tester Feedback: `../../PLAYTEST_FEEDBACK_TEMPLATE.md`
- Operator Runbook: `../../PLAYTEST_OPERATOR_RUNBOOK.md`
- Session tools: `http://127.0.0.1:8000/meta/playtest.html`
- Session export: anonymous Session ID + local JSON download
