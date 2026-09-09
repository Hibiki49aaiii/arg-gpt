from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VS = ROOT / "dist" / "assets" / "vs"
AREAS = VS / "areas"
INDEX = ROOT / "dist" / "index.html"

DATA = [
    ("01", "中央地区", "中央小学校 / 中央公民館", "市役所周辺の通常防災区。"),
    ("02", "西浜地区", "西浜小学校 / 西浜集会所", "海岸側の通常防災区。"),
    ("03", "東三丁目", "東三丁目公民館", "住宅地を中心とする通常防災区。"),
    ("04", "南川地区", "南川小学校", "河川南側の通常防災区。"),
    ("05", "北丘地区", "北丘集会所", "丘陵部の通常防災区。"),
    ("06", "駅前地区", "駅前防災倉庫", "駅周辺の通常防災区。"),
    ("07", "水門地区", "水門公園", "水門周辺の通常防災区。"),
]

STYLE = """body{margin:0;background:#d7d3c8;color:#222;font:14px/1.7 Arial,'MS PGothic',sans-serif}main{width:min(760px,calc(100% - 24px));margin:16px auto;background:#f7f4e9;border:1px solid #8c8981}header{padding:10px 14px;background:#315e63;color:#fff}header h1{margin:0;font-size:20px}nav{padding:7px 14px;background:#e4dfd3;border-bottom:1px solid #aaa}.content{padding:18px}.area{display:grid;grid-template-columns:110px 1fr;gap:18px;align-items:start}.area img{width:96px;height:72px;border:1px solid #888;background:#eee}.box{margin:16px 0;padding:12px;border:1px solid #aaa;background:#eeeadf}table{width:100%;border-collapse:collapse}th,td{padding:8px;border:1px solid #aaa;text-align:left}th{width:30%;background:#e2ddd1}footer{padding:9px 14px;border-top:1px solid #aaa;color:#666;font-size:12px}a{color:#234f55}@media(max-width:520px){.area{grid-template-columns:1fr}.area img{margin:auto}}"""


def area_html(code: str, name: str, shelter: str, summary: str) -> str:
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>地区{code} {name} | 旧・凪代市防災情報</title><style>{STYLE}</style></head><body><main><header><h1>旧・凪代市 防災情報</h1><div>地区別ページ / 保存コピー</div></header><nav><a href="../../../../index.html#areas">地域一覧へ戻る</a> ｜ <a href="../../update-history.html">更新履歴</a></nav><div class="content"><div class="area"><img src="../../area_{code}.png" alt="地区{code}保存アイコン"><div><h2>地区 {code} — {name}</h2><p>{summary}</p></div></div><table><tr><th>地区番号</th><td>{code}</td></tr><tr><th>地区名</th><td>{name}</td></tr><tr><th>主な避難所</th><td>{shelter}</td></tr><tr><th>保存状態</th><td>個別ページ・地区画像とも保存済み</td></tr></table><div class="box">このページは01〜07で共通のレイアウト・命名規則を使用しています。</div></div><footer>これはフィクション作品内の架空自治体ページです。現実の災害情報として使用しないでください。</footer></main></body></html>'''


def contact_html() -> str:
    return f'''<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>防災課連絡先 | 旧・凪代市防災情報</title><style>{STYLE}</style></head><body><main><header><h1>凪代市 総務部 防災課</h1><div>旧サイト保存ページ</div></header><nav><a href="../../index.html#home">保存サイトへ戻る</a></nav><div class="content"><h2>お問い合わせ</h2><p>保存元サイトに掲載されていた連絡先欄を、フィクション境界のため非実在情報へ置き換えています。</p><table><tr><th>所在地</th><td>凪代市役所庁舎内（架空）</td></tr><tr><th>電話</th><td>000-000-0000（非通話・架空表記）</td></tr><tr><th>電子メール</th><td>bousai@nagi-shiro.example.invalid</td></tr><tr><th>担当</th><td>防災計画・避難所管理・資料保存</td></tr></table><div class="box">現実の緊急連絡先ではありません。緊急時には実在する自治体・消防・警察等の公式情報を利用してください。</div></div><footer>これはフィクション作品です。</footer></main></body></html>'''


def patch_index() -> None:
    html = INDEX.read_text(encoding="utf-8")
    if 'assets/vs/areas/01/index.html' not in html:
        anchor = '<a class="btn secondary" href="assets/vs/backup-index.txt" target="_blank" rel="noopener">backup index</a>'
        replacement = anchor + '<a class="btn secondary" href="assets/vs/areas/01/index.html" target="_blank" rel="noopener">地区01 保存ページ</a><a class="btn secondary" href="assets/vs/contact.html" target="_blank" rel="noopener">旧・防災課連絡先</a>'
        if anchor not in html:
            raise RuntimeError("area page insertion anchor not found")
        html = html.replace(anchor, replacement, 1)
        INDEX.write_text(html, encoding="utf-8")


def patch_backup_index() -> None:
    path = VS / "backup-index.txt"
    text = path.read_text(encoding="utf-8")
    marker = "[preservation-local]"
    if marker not in text:
        text += "\n[preservation-local]\n"
        for code, *_ in DATA:
            text += f"areas/{code}/index.html  SAVED\n"
        text += "areas/08/index.html  MISSING\n"
        path.write_text(text, encoding="utf-8")


def main() -> None:
    AREAS.mkdir(parents=True, exist_ok=True)
    for code, name, shelter, summary in DATA:
        d = AREAS / code
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(area_html(code, name, shelter, summary), encoding="utf-8")

    # MED-013: 08 remains a real missing path, not a fake 200 page.
    eight = AREAS / "08"
    if eight.exists():
        raise RuntimeError("areas/08 must remain absent")

    (VS / "contact.html").write_text(contact_html(), encoding="utf-8")
    patch_backup_index()
    patch_index()

    expected = [AREAS / code / "index.html" for code, *_ in DATA]
    assert all(p.is_file() for p in expected)
    assert not (AREAS / "08" / "index.html").exists()
    print("generated 7 ordinary area pages + fictional contact page")


if __name__ == "__main__":
    main()
