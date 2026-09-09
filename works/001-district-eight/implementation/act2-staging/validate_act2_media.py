from __future__ import annotations

import json
from pathlib import Path

from PIL import Image
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[4]
STAGING = ROOT / "works" / "001-district-eight" / "implementation" / "act2-staging"
SITE = STAGING / "site"
MEDIA = SITE / "media"
DIST = ROOT / "dist"

EXPECTED = {
    "med-016-bousai-215-scan.png": "MED-016",
    "med-017-meeting-minutes.pdf": "MED-017",
    "med-018-subjects-fragment-scan.png": "MED-018",
    "med-019-graduation-ledger-scan.png": "MED-019",
    "med-020-school-summer-notice.pdf": "MED-020",
    "med-020b-enrollment-confirmation-scan.png": "MED-020B",
    "med-021-telephone-index-scan.png": "MED-021",
    "manifest.json": "manifest",
}


def check_files() -> None:
    assert MEDIA.is_dir(), "site/media missing"
    for name in EXPECTED:
        assert (MEDIA / name).is_file(), f"missing {name}"

    for name in [n for n in EXPECTED if n.endswith(".png")]:
        with Image.open(MEDIA / name) as im:
            assert im.format == "PNG", (name, im.format)
            assert im.width >= 900 and im.height >= 700, (name, im.size)


def check_manifest() -> None:
    data = json.loads((MEDIA / "manifest.json").read_text(encoding="utf-8"))
    assert data["status"] == "STAGING_ONLY_HUMAN_GATE_8_OPEN"
    assert data["public_runtime_linked"] is False
    ids = {x["id"] for x in data["assets"]}
    for req in ["MED-016", "MED-017", "MED-018", "MED-019", "MED-020", "MED-020B", "MED-021"]:
        assert req in ids, req


def check_pdfs() -> None:
    meetings = PdfReader(MEDIA / "med-017-meeting-minutes.pdf")
    notice = PdfReader(MEDIA / "med-020-school-summer-notice.pdf")
    assert len(meetings.pages) == 2
    assert len(notice.pages) == 1

    meeting_text = "\n".join((p.extract_text() or "") for p in meetings.pages)
    for s in [
        "平成10年8月17日",
        "8月14日以降",
        "平成10年8月19日",
        "管理区分08",
        "旧市民体育館",
        "外部専門家",
    ]:
        assert s in meeting_text, f"meeting PDF missing: {s}"

    notice_text = notice.pages[0].extract_text() or ""
    for s in ["平成10年8月21日", "凪代市教育委員会", "第八避難区対象者", "保護者"]:
        assert s in notice_text, f"school PDF missing: {s}"
    assert "第八避難区在住者" not in notice_text


def check_existing_exact_copy() -> None:
    files = {
        "215": SITE / "documents/215/index.html",
        "subjects": SITE / "restricted/subjects-fragment/index.html",
        "junior": SITE / "school/junior-high/1997/yui-mizuki/index.html",
        "enrollment": SITE / "school/high-school/1998/enrollment/index.html",
        "notice": SITE / "school/notices/1998-08-21/index.html",
    }
    text = {k: p.read_text(encoding="utf-8") for k, p in files.items()}

    for s in ["平成10年8月19日", "管理区分番号を「08」", "第八避難区", "区域変更は行わない", "8月14日以降"]:
        assert s in text["215"], f"215 exact-copy missing: {s}"
    assert "/media/med-016-bousai-215-scan.png" in text["215"]

    for s in ["水城 結", "1981-04-27", "東三丁目12-4", "管理区分", "第八", "旧市民体育館", "保護者同伴"]:
        assert s in text["subjects"], f"subjects missing: {s}"
    assert "/media/med-018-subjects-fragment-scan.png" in text["subjects"]

    for s in ["水城 結", "1981年4月27日", "凪代市東三丁目12-4", "水城 真理子", "1997年3月"]:
        assert s in text["junior"], f"junior ledger missing: {s}"
    assert "/media/med-019-graduation-ledger-scan.png" in text["junior"]

    for s in ["水城 結", "1981年4月27日", "水城 真理子", "東三丁目"]:
        assert s in text["enrollment"], f"enrollment missing: {s}"
    assert "/media/med-020b-enrollment-confirmation-scan.png" in text["enrollment"]

    assert "第八避難区対象者" in text["notice"]
    assert "第八避難区在住者" not in text["notice"]
    assert "/media/med-020-school-summer-notice.pdf" in text["notice"]


def check_spoiler_boundary() -> None:
    player_files = [p for p in SITE.rglob("*") if p.is_file() and p.suffix.lower() in {".html", ".js", ".css", ".json"}]
    corpus = "\n".join(p.read_text(encoding="utf-8", errors="ignore") for p in player_files)
    prohibited = [
        "33秒",
        "送信ログ27秒",
        "共同記憶同期",
        "記述密度",
        "player causality",
        "記録が現実を作る",
    ]
    for term in prohibited:
        assert term not in corpus, f"Act 3+ spoiler leaked into Act 2 staging: {term}"


def check_public_isolation() -> None:
    assert DIST.is_dir(), "dist missing"
    names = [n for n in EXPECTED if n != "manifest.json"]
    for p in DIST.rglob("*"):
        if not p.is_file() or p.suffix.lower() not in {".html", ".js", ".css", ".json", ".txt"}:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        assert "act2-staging" not in text, f"public dist links act2 staging: {p}"
        for name in names:
            assert name not in text, f"public dist links staging media {name}: {p}"


def check_generator_semantics() -> None:
    source = (STAGING / "generate_act2_media.py").read_text(encoding="utf-8")
    required = [
        "8月14日以降に受付した照会・相談案件",
        "管理区分番号を「08」",
        "関係文書上の呼称を「第八避難区」",
        "第1避難区から第7避難区までの区域変更は行わない",
        "水城 結",
        "1981-04-27",
        "東三丁目12-4",
        "保護者同伴",
        "第八避難区対象者",
    ]
    for term in required:
        assert term in source, f"generator source missing semantic: {term}"
    assert "第八避難区在住者" not in source


def main() -> None:
    check_files()
    check_manifest()
    check_pdfs()
    check_existing_exact_copy()
    check_spoiler_boundary()
    check_public_isolation()
    check_generator_semantics()
    print("Act 2 staging media validation: PASS")


if __name__ == "__main__":
    main()
