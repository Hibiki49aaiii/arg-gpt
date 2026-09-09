from __future__ import annotations

from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import mm
from reportlab.lib.colors import black, HexColor
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist" / "assets" / "vs"
INDEX = ROOT / "dist" / "index.html"
OUT.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
W, H = A4


def pdf_header(c, title: str, page: int, total: int) -> None:
    c.setFont("HeiseiKakuGo-W5", 10)
    c.drawString(18 * mm, H - 16 * mm, "凪代市 総務部 防災課")
    c.setFont("HeiseiMin-W3", 9)
    c.drawRightString(W - 18 * mm, H - 16 * mm, f"{title}  {page}/{total}")
    c.line(18 * mm, H - 19 * mm, W - 18 * mm, H - 19 * mm)


def pdf_footer(c) -> None:
    c.setFont("HeiseiMin-W3", 8)
    c.setFillColor(HexColor("#555555"))
    c.drawCentredString(W / 2, 11 * mm, "平成10年度 庁内配布資料 / 公開保存複写")
    c.setFillColor(black)


def wrapped(c, text: str, x: float, y: float, width_chars: int = 38, leading: float = 6.5 * mm, size: int = 10) -> float:
    c.setFont("HeiseiMin-W3", size)
    lines: list[str] = []
    for para in text.split("\n"):
        if not para:
            lines.append("")
            continue
        while len(para) > width_chars:
            lines.append(para[:width_chars])
            para = para[width_chars:]
        lines.append(para)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def generate_zone_icons() -> None:
    for n in range(1, 8):
        img = Image.new("RGB", (96, 72), (238, 234, 220))
        d = ImageDraw.Draw(img)
        d.rectangle((2, 2, 93, 69), outline=(80, 96, 90), width=2)
        d.rectangle((8, 8, 87, 63), fill=(218, 222, 209), outline=(130, 140, 132))
        d.ellipse((15, 15, 55, 55), outline=(57, 93, 96), width=4)
        d.text((24, 22), f"{n:02d}", fill=(125, 62, 48))
        d.line((60, 22, 80, 22), fill=(87, 103, 96), width=2)
        d.line((60, 32, 78, 32), fill=(87, 103, 96), width=2)
        d.line((60, 42, 82, 42), fill=(87, 103, 96), width=2)
        img.save(OUT / f"area_{n:02d}.png", optimize=True)

    # MED-005: area_08.png is deliberately absent. The backup index keeps the missing reference.
    missing = OUT / "area_08.png"
    if missing.exists():
        missing.unlink()


def generate_disaster_plan() -> None:
    path = OUT / "h10_summer_disaster_plan.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle("平成10年夏季防災計画")
    c.setAuthor("凪代市 総務部 防災課")
    c.setSubject("平成10年度 夏季防災体制・避難所運用計画")
    c.setKeywords("凪代市, 防災, 平成10年, 避難区, 公開保存")
    sections = [
        ("表紙", ["平成10年 夏季防災計画", "凪代市 総務部 防災課", "平成10年7月 改訂"]),
        ("1. 目的", ["本計画は、台風・集中豪雨・河川増水等の夏季災害に際し、避難所の開設、情報伝達、給水及び巡回体制を定めるものとする。", "通常の行政区域とは別に、防災運用上の地区番号を使用する。"]),
        ("2. 警戒体制", ["気象台発表、河川水位、道路冠水及び停電情報を総合し、警戒班・連絡班・施設班を段階的に配置する。", "夜間は防災無線と地区連絡員を併用する。"]),
        ("3. 避難所開設", ["地区01 中央、02 西浜、03 東三丁目、04 南川、05 北丘、06 駅前、07 水門について、指定施設を順次開設する。", "収容人数は当日点検の結果により増減する。"]),
        ("4. 給水・物資", ["給水車は市役所、西浜小学校、南川小学校を優先する。", "臨時給水地点については別紙『給水地点一覧』を参照する。"]),
        ("5. 交通・迂回", ["冠水時は河川沿い道路を閉鎖し、旧県道側へ迂回する。", "バス事業者には臨時停留所の設置を依頼する場合がある。"]),
        ("6. 臨時管理区分", ["災害記録整理の都合上、既存の地区01〜07に変更を加えず、複数地区にまたがる報告を一時的な管理区分へ束ねることがある。", "区分08『第八避難区』は、必要時のみ防災課長決裁により使用する。行政区域を新設するものではない。"]),
        ("7. 連絡記録", ["無線放送、電話受付、現地巡回の時刻は原則として分単位で記録する。", "録音媒体を使用した場合、保管番号を記録簿に転記する。"]),
        ("8. 更新履歴", ["平成10年7月03日 初版", "平成10年7月21日 給水地点追記", "平成10年8月05日 避難所収容人数更新", "平成10年8月19日 臨時管理区分に関する注記追加"]),
        ("付記", ["本資料は庁内運用資料を公開保存用に複写したものである。現行の避難情報として使用しないこと。"]),
    ]
    total = len(sections)
    for i, (title, paras) in enumerate(sections, 1):
        pdf_header(c, "平成10年夏季防災計画", i, total)
        y = H - 35 * mm
        if i == 1:
            c.setFont("HeiseiKakuGo-W5", 22)
            c.drawCentredString(W / 2, y, paras[0]); y -= 18 * mm
            c.setFont("HeiseiMin-W3", 14)
            c.drawCentredString(W / 2, y, paras[1]); y -= 10 * mm
            c.drawCentredString(W / 2, y, paras[2]); y -= 22 * mm
            c.rect(35 * mm, y - 35 * mm, W - 70 * mm, 35 * mm)
            c.setFont("HeiseiMin-W3", 10)
            c.drawCentredString(W / 2, y - 14 * mm, "公開保存複写")
            c.drawCentredString(W / 2, y - 23 * mm, "原本の押印・個人連絡先は省略")
        else:
            c.setFont("HeiseiKakuGo-W5", 16)
            c.drawString(20 * mm, y, title); y -= 12 * mm
            for p in paras:
                y = wrapped(c, p, 24 * mm, y, 37, 7 * mm, 10)
                y -= 4 * mm
            if i == 7:
                y -= 3 * mm
                c.setStrokeColor(HexColor("#666666"))
                c.rect(24 * mm, y - 30 * mm, W - 48 * mm, 30 * mm)
                c.setFont("HeiseiKakuGo-W5", 10)
                c.drawString(28 * mm, y - 8 * mm, "運用コード")
                c.drawString(72 * mm, y - 8 * mm, "08")
                c.drawString(28 * mm, y - 17 * mm, "呼称")
                c.drawString(72 * mm, y - 17 * mm, "第八避難区")
                c.drawString(28 * mm, y - 26 * mm, "備考")
                c.setFont("HeiseiMin-W3", 9)
                c.drawString(72 * mm, y - 26 * mm, "臨時・記録整理用 / 常設行政区ではない")
                c.setStrokeColor(black)
        pdf_footer(c)
        c.showPage()
    c.save()


def generate_water_points() -> None:
    path = OUT / "h10_water_points.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle("給水地点一覧")
    c.setAuthor("凪代市 総務部 防災課")
    c.setSubject("平成10年夏季 給水地点一覧")
    c.setKeywords("凪代市, 給水, 旧八号集会所, 平成10年")
    rows = [
        ("01", "市役所南側駐車場", "常設", "大型車可"),
        ("02", "西浜小学校 正門脇", "常設", "消火栓併用"),
        ("03", "東三丁目公民館", "常設", "夜間鍵管理"),
        ("04", "南川小学校 体育館側", "常設", "発電機あり"),
        ("05", "北丘集会所", "臨時", "小型車のみ"),
        ("06", "駅前防災倉庫", "臨時", "混雑時閉鎖"),
        ("07", "水門公園北口", "臨時", "河川増水時停止"),
        ("08", "旧八号集会所", "予備", "使用時は防災課へ連絡"),
    ]
    total = 3
    for page in range(1, 4):
        pdf_header(c, "給水地点一覧", page, total)
        y = H - 34 * mm
        if page == 1:
            c.setFont("HeiseiKakuGo-W5", 18)
            c.drawString(20 * mm, y, "平成10年夏季 給水地点一覧"); y -= 14 * mm
            c.setFont("HeiseiMin-W3", 10)
            c.drawString(20 * mm, y, "配布先：災害対策本部・給水班・地区連絡員"); y -= 10 * mm
            widths = [18, 70, 25, 55]
            x = 20 * mm
            c.setFont("HeiseiKakuGo-W5", 9)
            for h, w in zip(["番号", "地点", "区分", "備考"], widths):
                c.rect(x, y - 8 * mm, w * mm, 8 * mm)
                c.drawCentredString(x + w * mm / 2, y - 5.5 * mm, h)
                x += w * mm
            y -= 8 * mm
            c.setFont("HeiseiMin-W3", 8.5)
            for r in rows:
                x = 20 * mm
                for val, w in zip(r, widths):
                    c.rect(x, y - 8 * mm, w * mm, 8 * mm)
                    c.drawString(x + 2 * mm, y - 5.5 * mm, val)
                    x += w * mm
                y -= 8 * mm
            y -= 10 * mm
            c.setFont("HeiseiMin-W3", 9)
            c.drawString(20 * mm, y, "※ 08は通常の地区別一覧には掲載しない予備地点。")
            y -= 6 * mm
            c.drawString(20 * mm, y, "※ 旧八号集会所の鍵は施設班保管。")
        elif page == 2:
            c.setFont("HeiseiKakuGo-W5", 15)
            c.drawString(20 * mm, y, "給水車運行メモ"); y -= 12 * mm
            for t in ["午前便 06:30 市役所出発", "昼便 12:00 西浜経由", "夕方便 17:00 南川経由", "臨時便：現地連絡員の要請により追加"]:
                y = wrapped(c, t, 24 * mm, y, 36, 8 * mm, 10)
            y -= 8 * mm
            c.setFont("HeiseiMin-W3", 9)
            c.drawString(24 * mm, y, "旧八号集会所は道路状況確認後に進入すること。")
        else:
            c.setFont("HeiseiKakuGo-W5", 15)
            c.drawString(20 * mm, y, "改訂記録"); y -= 12 * mm
            for t in ["1998-07-18 初版", "1998-08-02 北丘を追加", "1998-08-13 旧八号集会所を予備地点として追記", "1998-08-20 配布先表記を更新"]:
                y = wrapped(c, t, 24 * mm, y, 36, 8 * mm, 10)
        pdf_footer(c)
        c.showPage()
    c.save()


def generate_text_assets() -> None:
    (OUT / "backup-index.txt").write_text("""# 凪代市旧防災サイト バックアップ索引
# mirror snapshot: 2004-03-18
# charset: Shift_JIS (converted for preservation)

[areas]
area_01.png  OK
area_02.png  OK
area_03.png  OK
area_04.png  OK
area_05.png  OK
area_06.png  OK
area_07.png  OK
area_08.png  MISSING

[pages]
/disaster/areas/01/index.html  SAVED
/disaster/areas/02/index.html  SAVED
/disaster/areas/03/index.html  SAVED
/disaster/areas/04/index.html  SAVED
/disaster/areas/05/index.html  SAVED
/disaster/areas/06/index.html  SAVED
/disaster/areas/07/index.html  SAVED
/disaster/areas/08/index.html  TARGET MISSING

[documents]
h10_summer_disaster_plan.pdf  SAVED
h10_water_points.pdf          SAVED

note:
08 is retained in the historical file list because the original index
contained the filename. The corresponding image/page was not present
in the preservation source.
""", encoding="utf-8")

    (OUT / "pdf-metadata.html").write_text("""<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>PDF保存情報 | 凪代市アーカイブ</title>
<style>body{max-width:760px;margin:24px auto;padding:0 16px;background:#ddd8cc;color:#25302e;font:15px/1.7 "Yu Gothic",Meiryo,sans-serif}main{background:#f6f1e6;border:1px solid #aaa293;padding:24px}h1{font:24px serif;border-bottom:3px double #8e887d;padding-bottom:10px}table{width:100%;border-collapse:collapse}th,td{border:1px solid #b8b0a1;padding:9px;text-align:left;vertical-align:top}th{width:30%;background:#e7e0d2}a{color:#2a5e64}.warn{border-left:4px solid #8c3d2f;padding:10px 14px;background:#eee2d8}</style></head><body><main><h1>保存PDF メタデータ</h1><p>旧防災サイトから保存されたPDFの書誌情報です。PDF閲覧ソフト固有の操作は必要ありません。</p><table><tr><th>ファイル</th><td><a href="h10_summer_disaster_plan.pdf">h10_summer_disaster_plan.pdf</a></td></tr><tr><th>Title</th><td>平成10年夏季防災計画</td></tr><tr><th>Author</th><td>凪代市 総務部 防災課</td></tr><tr><th>Pages</th><td>10</td></tr><tr><th>保存注記</th><td>庁内配布資料の公開保存複写</td></tr></table><br><table><tr><th>ファイル</th><td><a href="h10_water_points.pdf">h10_water_points.pdf</a></td></tr><tr><th>Title</th><td>給水地点一覧</td></tr><tr><th>Author</th><td>凪代市 総務部 防災課</td></tr><tr><th>Pages</th><td>3</td></tr><tr><th>索引語</th><td>給水 / 旧八号集会所 / 平成10年</td></tr></table><p class="warn">これはフィクション作品内の架空資料です。現実の災害情報として使用しないでください。</p></main></body></html>""", encoding="utf-8")

    (OUT / "update-history.html").write_text("""<!doctype html><html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>更新履歴 | 旧・凪代市防災情報</title><style>body{margin:0;background:#d8d4c8;color:#222;font:14px/1.65 Arial,"MS PGothic",sans-serif}.box{width:min(760px,calc(100% - 24px));margin:18px auto;background:#f7f3e8;border:1px solid #8d8a82;padding:16px}h1{font-size:20px;margin:0 0 12px;border-bottom:2px solid #375d61}.date{font-family:monospace;color:#704034}.row{padding:7px 0;border-bottom:1px dotted #aaa}.small{font-size:12px;color:#666}</style></head><body><div class="box"><h1>旧・凪代市 防災情報　更新履歴</h1><div class="row"><span class="date">2004-03-18</span> 保存用リンク切れを確認。旧資料は現状のまま保存。</div><div class="row"><span class="date">2003-09-12</span> 台風時の避難所案内を更新。</div><div class="row"><span class="date">2002-06-04</span> 地区06 駅前防災倉庫の案内を修正。</div><div class="row"><span class="date">2001-11-19</span> 防災訓練写真を追加。</div><div class="row"><span class="date">2000-08-29</span> 給水地点一覧をPDF化。</div><div class="row"><span class="date">1999-07-10</span> 夏季防災計画の保存版を掲載。</div><div class="row"><span class="date">1998-08-20</span> 臨時資料索引を更新。</div><div class="row"><span class="date">1998-08-13</span> 給水地点一覧を更新。</div><div class="row"><span class="date">1998-07-21</span> 避難所収容人数を更新。</div><div class="row"><span class="date">1998-07-03</span> 夏季防災ページを公開。</div><p class="small">保存コピー。リンク先が存在しない項目も原構造を保持しています。</p></div></body></html>""", encoding="utf-8")


def patch_index() -> None:
    html = INDEX.read_text(encoding="utf-8")

    old = '<div class="note"><span class="label">閲覧方法</span><p>入口から自由に読み始められます。手がかりを得たら、同じ語句や資料番号を別の保存先でも照合してください。</p></div>'
    new = '<div class="note"><span class="label">旧サイト保存資料</span><p>通常更新の履歴も保存されています。異常だけでなく、普通の更新が長く続いたことも確認できます。</p><div class="actions"><a class="btn secondary" href="assets/vs/update-history.html" target="_blank" rel="noopener">旧サイト更新履歴</a></div></div>' + old
    if old not in html:
        raise RuntimeError("home insertion anchor not found")
    html = html.replace(old, new, 1)

    old = '<div class="notice"><span class="label">照合メモ</span><p>地区 08 だけが、一覧から個別ページへ正常に遷移しません。これは一時的な通信エラーではなく、保存構造上の欠落として扱われています。</p></div>'
    new = old + '<div class="note"><span class="label">保存画像の命名規則</span><p>保存元には area_01.png から area_07.png まで同じ形式の画像があります。08だけ実体がありません。</p><div class="actions"><a class="btn secondary" href="assets/vs/area_01.png" target="_blank" rel="noopener">area_01.png を確認</a><a class="btn secondary" href="assets/vs/backup-index.txt" target="_blank" rel="noopener">backup index</a></div></div>'
    if old not in html:
        raise RuntimeError("areas insertion anchor not found")
    html = html.replace(old, new, 1)

    old = '<div class="notice"><p>欠落は単独の 404 ではありません。文書保存庫にある資料番号の前後関係を確認してください。</p></div><div class="actions">'
    new = '<div class="notice"><p>欠落は単独の 404 ではありません。旧行政PDFにも同じ語が残っています。PDF本体と保存メタデータを照合できます。</p></div><div class="actions"><a class="btn" href="assets/vs/h10_summer_disaster_plan.pdf" target="_blank" rel="noopener">平成10年夏季防災計画</a><a class="btn secondary" href="assets/vs/h10_water_points.pdf" target="_blank" rel="noopener">給水地点一覧</a><a class="btn secondary" href="assets/vs/pdf-metadata.html" target="_blank" rel="noopener">PDF保存情報</a>'
    if old not in html:
        raise RuntimeError("archive insertion anchor not found")
    html = html.replace(old, new, 1)

    INDEX.write_text(html, encoding="utf-8")


def main() -> None:
    generate_zone_icons()
    generate_disaster_plan()
    generate_water_points()
    generate_text_assets()
    patch_index()
    expected = [*(f"area_{n:02d}.png" for n in range(1, 8)), "backup-index.txt", "h10_summer_disaster_plan.pdf", "h10_water_points.pdf", "pdf-metadata.html", "update-history.html"]
    missing = [name for name in expected if not (OUT / name).is_file()]
    if missing:
        raise RuntimeError(f"missing generated assets: {missing}")
    if (OUT / "area_08.png").exists():
        raise RuntimeError("area_08.png must remain absent")
    print(f"generated {len(expected)} VS assets in {OUT}")


if __name__ == "__main__":
    main()
