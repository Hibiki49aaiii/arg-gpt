# 第八避難区 Vertical Slice

Act 0〜1 の静的プロトタイプ。

## 起動

リポジトリルートから:

```bash
python3 -m http.server 8000 --directory works/001-district-eight/implementation/vertical-slice/sites
```

ブラウザ:

```text
http://localhost:8000/old-bousai/
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
