from __future__ import annotations

import json
import random
import tempfile
from pathlib import Path

import fitz
from PIL import Image, ImageEnhance, ImageFilter, ImageOps
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle, PageBreak

ROOT = Path(__file__).resolve().parents[4]
STAGING = ROOT / "works" / "001-district-eight" / "implementation" / "act2-staging"
SITE = STAGING / "site"
MEDIA = SITE / "media"
MEDIA.mkdir(parents=True, exist_ok=True)

pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))

INK = colors.HexColor("#252525")
MUTED = colors.HexColor("#666666")
LINE = colors.HexColor("#8f8f8a")
PAPER = colors.HexColor("#f6f3e9")


def header(c: canvas.Canvas, title: str, ref: str = "") -> float:
    w, h = c._pagesize
    c.setFillColor(INK)
    c.setFont("HeiseiKakuGo-W5", 10)
    c.drawString(18 * mm, h - 15 * mm, "凪代市 史料保存複写")
    if ref:
        c.setFont("HeiseiMin-W3", 8)
        c.drawRightString(w - 18 * mm, h - 15 * mm, ref)
    c.setStrokeColor(LINE)
    c.line(18 * mm, h - 18 * mm, w - 18 * mm, h - 18 * mm)
    c.setFont("HeiseiKakuGo-W5", 16)
    c.drawString(20 * mm, h - 30 * mm, title)
    return h - 42 * mm


def footer(c: canvas.Canvas, text: str = "公開保存複写 / 原本の個人連絡先等は省略") -> None:
    w, _ = c._pagesize
    c.setFont("HeiseiMin-W3", 7.5)
    c.setFillColor(MUTED)
    c.drawCentredString(w / 2, 10 * mm, text)
    c.setFillColor(INK)


def draw_lines(c: canvas.Canvas, lines: list[str], x: float, y: float, size: float = 10, leading: float = 6.5 * mm) -> float:
    c.setFont("HeiseiMin-W3", size)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y


def scan_from_pdf(pdf_path: Path, png_path: Path, page: int = 0, rotate: float = -0.25, seed: int = 0) -> None:
    doc = fitz.open(pdf_path)
    pix = doc[page].get_pixmap(matrix=fitz.Matrix(1.8, 1.8), alpha=False)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    img = ImageOps.grayscale(img)
    img = ImageEnhance.Contrast(img).enhance(0.93)
    img = ImageEnhance.Brightness(img).enhance(1.03)
    img = img.filter(ImageFilter.GaussianBlur(radius=0.18))

    # Mild deterministic copier texture; never obscures semantic text.
    rng = random.Random(seed)
    px = img.load()
    w, h = img.size
    for _ in range(max(100, (w * h) // 18000)):
        x = rng.randrange(w)
        y = rng.randrange(h)
        value = rng.choice([205, 220, 235])
        px[x, y] = value

    img = img.convert("RGB")
    if rotate:
        img = img.rotate(rotate, expand=True, fillcolor=(239, 237, 230))
    img.save(png_path, optimize=True)
    doc.close()


def make_med016() -> None:
    out = MEDIA / "med-016-bousai-215-scan.png"
    with tempfile.TemporaryDirectory() as td:
        pdf = Path(td) / "215.pdf"
        c = canvas.Canvas(str(pdf), pagesize=A4)
        w, h = A4
        y = header(c, "臨時管理区分の設定について", "防災第215号 / 平成10年8月19日")
        c.setFont("HeiseiMin-W3", 10)
        c.drawString(20 * mm, y, "凪代市 防災課")
        y -= 10 * mm
        y = draw_lines(c, [
            "8月14日以降に受付した照会・相談案件について、関係各課での記録混在を防止し、",
            "連絡・面談・経過確認を統一して取り扱うため、下記のとおり臨時管理区分を設定する。",
        ], 20 * mm, y, 9.5, 6 * mm)
        y -= 5 * mm
        items = [
            "1. 管理区分番号を「08」とする。",
            "2. 関係文書上の呼称を「第八避難区」とする。",
            "3. 本区分の設定に伴う、第1避難区から第7避難区までの区域変更は行わない。",
            "4. 対象者の判定基準については別紙Aによる。",
            "5. 面談・連絡記録については、防災課、保健担当、教育委員会で管理番号を共通使用する。",
        ]
        y = draw_lines(c, items, 25 * mm, y, 9.5, 9 * mm)
        c.setFillColor(colors.black)
        c.rect(25 * mm, y - 3 * mm, 115 * mm, 7 * mm, stroke=0, fill=1)
        c.setFillColor(INK)
        c.setFont("HeiseiMin-W3", 8)
        c.drawString(143 * mm, y - 1 * mm, "6. 一部非公開")
        y -= 18 * mm
        c.setStrokeColor(LINE)
        c.line(20 * mm, y, w - 20 * mm, y)
        y -= 7 * mm
        y = draw_lines(c, [
            "施行: 平成10年8月19日 15:00",
            "添付: 別紙A（非公開） / 別紙B 対象者管理表",
        ], 20 * mm, y, 9, 6 * mm)
        c.setStrokeColor(colors.HexColor("#8c3d2f"))
        c.setLineWidth(1.2)
        c.rect(w - 52 * mm, 22 * mm, 30 * mm, 16 * mm)
        c.setFont("HeiseiKakuGo-W5", 9)
        c.setFillColor(colors.HexColor("#8c3d2f"))
        c.drawCentredString(w - 37 * mm, 28 * mm, "一部公開")
        c.setFillColor(INK)
        footer(c)
        c.save()
        scan_from_pdf(pdf, out, rotate=-0.22, seed=16)


def make_med017() -> None:
    path = MEDIA / "med-017-meeting-minutes.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle("防災関連照会事案 臨時打合せ要旨")
    c.setAuthor("凪代市")

    y = header(c, "防災関連照会事案 臨時打合せ要旨", "平成10年8月17日")
    y = draw_lines(c, ["出席: 防災課 / 保健担当 / 教育委員会 / 設備保守担当"], 20 * mm, y, 9.5, 7 * mm)
    y -= 3 * mm
    y = draw_lines(c, [
        "1. 8月14日以降、市内複数地区から類似する照会が寄せられている。",
        "2. 問い合わせ内容の詳細は別紙集計による。",
        "3. 関係世帯について個別聞き取りを実施する。",
        "4. 学齢者を含む世帯について教育委員会と情報を共有する。",
        "5. 次回会議までに記録様式を統一する。",
    ], 24 * mm, y, 9.5, 9 * mm)
    y -= 4 * mm
    c.setFont("HeiseiMin-W3", 8.5)
    c.drawString(24 * mm, y, "別紙集計:")
    c.setFillColor(colors.black)
    c.rect(48 * mm, y - 2 * mm, 72 * mm, 6 * mm, stroke=0, fill=1)
    c.setFillColor(INK)
    footer(c)
    c.showPage()

    y = header(c, "防災関連照会事案 臨時打合せ要旨（第2回）", "平成10年8月19日")
    y = draw_lines(c, [
        "1. 対象者記録の重複・表記不一致が生じている。",
        "2. 防災第215号により管理区分08を設定する。",
        "3. 面談場所として旧市民体育館会議室を使用する。",
        "4. 学齢者については学校経由の連絡を併用する。",
        "5. 外部専門家への協力依頼を検討する。",
        "6. 8月14日以前の関連照会について再確認する。",
    ], 24 * mm, y, 9.5, 9 * mm)
    y -= 5 * mm
    c.setFont("HeiseiMin-W3", 8.5)
    c.drawString(24 * mm, y, "外部協力候補:")
    c.setFillColor(colors.black)
    c.rect(55 * mm, y - 2 * mm, 64 * mm, 6 * mm, stroke=0, fill=1)
    c.setFillColor(INK)
    footer(c)
    c.save()


def make_med018() -> None:
    out = MEDIA / "med-018-subjects-fragment-scan.png"
    with tempfile.TemporaryDirectory() as td:
        pdf = Path(td) / "subjects.pdf"
        c = canvas.Canvas(str(pdf), pagesize=landscape(A4))
        w, h = landscape(A4)
        y = header(c, "防災第215号 別紙B　対象者管理表（抜粋）", "公開可能部分")
        c.setFont("HeiseiMin-W3", 8.5)
        c.drawString(18 * mm, y, "非公開欄は原資料の公開制限に従い置換。住所と管理区分は別列のまま保存。")
        y -= 10 * mm
        cols = [18, 34, 31, 48, 26, 42, 35]
        labels = ["管理No.", "氏名", "生年月日", "現住所", "管理区分", "面談場所", "備考"]
        rows = [
            ["08-011", "［一部非公開］", "—", "北二丁目", "第八", "旧市民体育館", "—"],
            ["08-012", "水城 結", "1981-04-27", "東三丁目12-4", "第八", "旧市民体育館", "保護者同伴"],
            ["08-013", "［一部非公開］", "—", "臨海一丁目", "第八", "旧市民体育館", "—"],
        ]
        x0 = 16 * mm
        row_h = 13 * mm
        c.setFont("HeiseiKakuGo-W5", 8.5)
        x = x0
        for label, cw in zip(labels, cols):
            c.setFillColor(colors.HexColor("#dedbd2")); c.rect(x, y-row_h, cw*mm, row_h, fill=1, stroke=1)
            c.setFillColor(INK); c.drawString(x+2*mm, y-8*mm, label); x += cw*mm
        y -= row_h
        c.setFont("HeiseiMin-W3", 8.5)
        for ri, row in enumerate(rows):
            x = x0
            if ri == 1:
                c.setFillColor(colors.HexColor("#ece8dd")); c.rect(x0, y-row_h, sum(cols)*mm, row_h, fill=1, stroke=0)
            for val, cw in zip(row, cols):
                c.setFillColor(INK); c.rect(x, y-row_h, cw*mm, row_h, fill=0, stroke=1)
                c.drawString(x+2*mm, y-8*mm, val); x += cw*mm
            y -= row_h
        c.setFont("HeiseiMin-W3", 8)
        c.setFillColor(MUTED)
        c.drawString(18*mm, 15*mm, "抽出行のみ / 管理No.08-012は学校史資料との照合対象")
        c.save()
        scan_from_pdf(pdf, out, rotate=0.12, seed=18)


def make_med019() -> None:
    out = MEDIA / "med-019-graduation-ledger-scan.png"
    with tempfile.TemporaryDirectory() as td:
        pdf = Path(td) / "grad.pdf"
        c = canvas.Canvas(str(pdf), pagesize=A4)
        w, h = A4
        y = header(c, "平成8年度 卒業台帳", "卒業: 1997年3月 / 公開許諾断片")
        fields = [
            ("氏名", "水城 結"),
            ("生年月日", "1981年4月27日"),
            ("卒業時住所", "凪代市東三丁目12-4"),
            ("保護者", "水城 真理子"),
            ("進学先", "市内県立高等学校"),
        ]
        x = 30 * mm
        label_w = 38 * mm
        value_w = 105 * mm
        row_h = 15 * mm
        c.setFont("HeiseiMin-W3", 10)
        for label, value in fields:
            c.setFillColor(colors.HexColor("#e4e0d5")); c.rect(x, y-row_h, label_w, row_h, fill=1, stroke=1)
            c.setFillColor(INK); c.rect(x+label_w, y-row_h, value_w, row_h, fill=0, stroke=1)
            c.drawString(x+3*mm, y-9.5*mm, label)
            c.drawString(x+label_w+4*mm, y-9.5*mm, value)
            y -= row_h
        y -= 15 * mm
        c.setFont("HeiseiMin-W3", 8.5)
        c.setFillColor(MUTED)
        c.drawString(30*mm, y, "個人情報保護のため、作品内公開許諾のある項目のみ複写。写真欄は公開対象外。")
        footer(c, "凪代市学校史資料室 / 公開可能項目複写")
        c.save()
        scan_from_pdf(pdf, out, rotate=-0.15, seed=19)


def make_med020() -> None:
    path = MEDIA / "med-020-school-summer-notice.pdf"
    c = canvas.Canvas(str(path), pagesize=A4)
    c.setTitle("夏季休業中の連絡対応について（追補）")
    c.setAuthor("凪代市教育委員会")
    y = header(c, "夏季休業中の連絡対応について（追補）", "平成10年8月21日")
    y = draw_lines(c, ["市内学校関係者 各位", "凪代市教育委員会"], 20*mm, y, 9.5, 7*mm)
    y -= 4*mm
    y = draw_lines(c, [
        "防災課からの依頼に基づき、該当する生徒・児童への連絡については、",
        "通常の緊急連絡網とは別に指定様式を使用してください。",
        "",
        "第八避難区対象者については、保護者への連絡後、対応結果を教育委員会担当へ報告してください。",
        "",
        "対象者氏名は別紙によります。",
    ], 24*mm, y, 10, 7*mm)
    footer(c, "教育委員会保存資料 / 現実の学校連絡ではありません")
    c.save()

    # Companion record used by PZ-004 identity confirmation.
    out = MEDIA / "med-020b-enrollment-confirmation-scan.png"
    with tempfile.TemporaryDirectory() as td:
        pdf = Path(td) / "enrollment.pdf"
        c = canvas.Canvas(str(pdf), pagesize=A4)
        y = header(c, "平成10年度 在籍確認", "2年B組 / 公開可能項目")
        fields = [
            ("氏名", "水城 結"),
            ("生年月日", "1981年4月27日"),
            ("保護者", "水城 真理子"),
            ("連絡先地区", "東三丁目"),
        ]
        x = 35*mm; lw = 42*mm; vw = 92*mm; rh = 16*mm
        c.setFont("HeiseiMin-W3", 10)
        for label, value in fields:
            c.setFillColor(colors.HexColor("#e8e4da")); c.rect(x, y-rh, lw, rh, fill=1, stroke=1)
            c.setFillColor(INK); c.rect(x+lw, y-rh, vw, rh, fill=0, stroke=1)
            c.drawString(x+3*mm, y-10*mm, label); c.drawString(x+lw+4*mm, y-10*mm, value)
            y -= rh
        footer(c, "平成10年度学校在籍資料 / 公開項目複写")
        c.save()
        scan_from_pdf(pdf, out, rotate=0.18, seed=20)


def make_med021() -> None:
    out = MEDIA / "med-021-telephone-index-scan.png"
    with tempfile.TemporaryDirectory() as td:
        pdf = Path(td) / "phone.pdf"
        c = canvas.Canvas(str(pdf), pagesize=A4)
        y = header(c, "旧電話帳 人物索引（抜粋）", "1998年保管版 / 補助照合")
        c.setFont("HeiseiMin-W3", 10)
        rows = [
            ("水城 真理子", "東三丁目12-4", "000-000-0000"),
            ("水越 正一", "東三丁目10-8", "000-000-0000"),
            ("水野 恵", "東三丁目15-2", "000-000-0000"),
        ]
        c.setFillColor(MUTED); c.setFont("HeiseiMin-W3", 8.5)
        c.drawString(22*mm, y, "電話番号はフィクション境界のため非通話表記へ置換。住所・氏名列のみ照合用。")
        y -= 12*mm
        c.setFillColor(INK); c.setFont("HeiseiMin-W3", 10)
        for name, addr, phone in rows:
            c.line(22*mm, y-3*mm, 185*mm, y-3*mm)
            c.drawString(25*mm, y, name)
            c.drawString(80*mm, y, addr)
            c.drawString(145*mm, y, phone)
            y -= 12*mm
        footer(c, "補助資料 / この資料単独ではAct 2進行に必須ではない")
        c.save()
        scan_from_pdf(pdf, out, rotate=-0.10, seed=21)


def patch_file(rel: str, anchor: str, insertion: str) -> None:
    path = SITE / rel
    text = path.read_text(encoding="utf-8")
    if insertion.strip() in text:
        return
    if anchor not in text:
        raise RuntimeError(f"patch anchor not found: {rel}: {anchor[:80]}")
    path.write_text(text.replace(anchor, anchor + insertion, 1), encoding="utf-8")


def patch_pages() -> None:
    patch_file(
        "documents/215/index.html",
        "</article>",
        '<figure class="media-evidence"><img src="/media/med-016-bousai-215-scan.png" alt="防災第215号の保存スキャン"><figcaption>原資料スキャン（公開可能範囲）</figcaption></figure>',
    )
    for rel in ["meetings/1998-08-17/index.html", "meetings/1998-08-19/index.html"]:
        patch_file(rel, "</article>", '<p class="media-link"><a href="/media/med-017-meeting-minutes.pdf">会議要旨PDF複写を開く</a></p>')
    patch_file(
        "restricted/subjects-fragment/index.html",
        "</table>",
        '<figure class="media-evidence wide"><img src="/media/med-018-subjects-fragment-scan.png" alt="対象者管理表の保存スキャン"><figcaption>別紙B 対象者管理表（抜粋）原資料スキャン</figcaption></figure><p class="media-link"><a href="/media/med-021-telephone-index-scan.png">補助照合：旧電話帳人物索引</a></p>',
    )
    patch_file(
        "school/junior-high/1997/yui-mizuki/index.html",
        "</div>\n\n<div class=\"school-card\">\n<h3>関連資料</h3>",
        '<figure class="media-evidence"><img src="/media/med-019-graduation-ledger-scan.png" alt="水城結の卒業台帳保存スキャン"><figcaption>平成8年度 卒業台帳 — 公開項目スキャン</figcaption></figure>',
    )
    patch_file(
        "school/notices/1998-08-21/index.html",
        "</article>",
        '<p class="media-link"><a href="/media/med-020-school-summer-notice.pdf">教育委員会保存PDFを開く</a></p>',
    )
    patch_file(
        "school/high-school/1998/enrollment/index.html",
        "</div>\n\n<div class=\"school-card\">",
        '<figure class="media-evidence"><img src="/media/med-020b-enrollment-confirmation-scan.png" alt="平成10年度在籍確認の保存スキャン"><figcaption>平成10年度 在籍確認 — 公開項目スキャン</figcaption></figure>',
    )

    css = SITE / "styles.css"
    text = css.read_text(encoding="utf-8")
    marker = "/* Act 2 staging evidence media */"
    if marker not in text:
        text += """

/* Act 2 staging evidence media */
.media-evidence{margin:22px auto;padding:10px;max-width:760px;border:1px solid #b5afa3;background:#eee9dd;box-shadow:3px 4px 0 rgba(60,55,45,.08)}
.media-evidence img{display:block;width:100%;height:auto;filter:saturate(.55) contrast(.98)}
.media-evidence figcaption{margin-top:8px;color:#666;font-size:12px;text-align:center}
.media-evidence.wide{max-width:960px;overflow-x:auto}.media-link{margin:16px 0;padding:9px 12px;border-left:3px solid #60706c;background:#efebe1}
"""
        css.write_text(text, encoding="utf-8")


def write_manifest() -> None:
    manifest = {
        "status": "STAGING_ONLY_HUMAN_GATE_8_OPEN",
        "public_runtime_linked": False,
        "assets": [
            {"id": "MED-016", "file": "med-016-bousai-215-scan.png", "type": "scan"},
            {"id": "MED-017", "file": "med-017-meeting-minutes.pdf", "type": "pdf", "pages": 2},
            {"id": "MED-018", "file": "med-018-subjects-fragment-scan.png", "type": "scan"},
            {"id": "MED-019", "file": "med-019-graduation-ledger-scan.png", "type": "scan"},
            {"id": "MED-020", "file": "med-020-school-summer-notice.pdf", "type": "pdf", "pages": 1},
            {"id": "MED-020B", "file": "med-020b-enrollment-confirmation-scan.png", "type": "scan", "role": "identity corroboration"},
            {"id": "MED-021", "file": "med-021-telephone-index-scan.png", "type": "scan", "optional": True},
        ],
        "spoiler_prohibitions": ["27秒", "33秒", "共同記憶同期", "記述密度", "player causality"],
    }
    (MEDIA / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    make_med016()
    make_med017()
    make_med018()
    make_med019()
    make_med020()
    make_med021()
    patch_pages()
    write_manifest()
    print("Act 2 staging media generated. dist/ untouched by design.")


if __name__ == "__main__":
    main()
