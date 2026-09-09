# 第八避難区 — OpenAI Sites Final Deployment Handoff

Status: READY FOR SITES DEPLOYMENT

この文書は、GitHub側で完成・検証済みのVertical Slice公開物を、既存OpenAI Sitesプロジェクトへ再公開するための最終引継ぎです。

## 1. 絶対にやり直さないこと

- Sitesプロジェクトを新規作成しない
- slug / production URLを変更しない
- ARGのストーリー／状態機械／分岐を再設計しない
- mainへのマージを公開条件にしない
- `dist/index.html` の既存状態機械を置き換えない
- `area_08.png` や `areas/08/index.html` を生成して欠番を埋めない

## 2. Source of Truth

Repository:
`Hibiki49aaiii/arg-gpt`

Branch:
`codex-district-eight-sites`

Reviewed production payload commit:
`2772b9fe11a07f90f5b4b42988ea262061c5a139`

29-file validation workflow commit:
`7fb0271a5873525d6465e99f37d8d37557e34bb8`

Current production HTML blob:
`dist/index.html` = `c28b10611184524409b59e34793a707ac8581982`

Reconstruction-map asset blob:
`dist/assets/reconstruction-map.svg` = `79f278f49c239d348f3506e28138702cf0289f1f`

Before deployment, re-fetch branch HEAD. Later documentation-only commits are acceptable; any later `dist/**` change must be reviewed before publishing.

## 3. Existing Sites Project

Project ID:
`appgprj_6a9836915bf48191bd2d504f8ac6c46e`

Static directory:
`dist`

Production URL:
`https://district-eight.era-0k.chatgpt.site`

`.openai/hosting.json` must still point to this project id and `dist`.

## 4. Expected Official Package

Expected total Sites package file count: **29**

### Core
1. `.openai/hosting.json`
2. `dist/index.html`

### Root archival graphics
3. `dist/assets/nagishiro-seal.svg`
4. `dist/assets/evacuation-map.svg`
5. `dist/assets/archive-index.svg`
6. `dist/assets/document-scan.svg`
7. `dist/assets/radio-cassette.svg`
8. `dist/assets/diary-fragment.svg`
9. `dist/assets/reconstruction-map.svg`

### Vertical Slice evidence/media
10. `dist/assets/vs/area_01.png`
11. `dist/assets/vs/area_02.png`
12. `dist/assets/vs/area_03.png`
13. `dist/assets/vs/area_04.png`
14. `dist/assets/vs/area_05.png`
15. `dist/assets/vs/area_06.png`
16. `dist/assets/vs/area_07.png`
17. `dist/assets/vs/backup-index.txt`
18. `dist/assets/vs/h10_summer_disaster_plan.pdf`
19. `dist/assets/vs/h10_water_points.pdf`
20. `dist/assets/vs/pdf-metadata.html`
21. `dist/assets/vs/update-history.html`
22. `dist/assets/vs/contact.html`

### Ordinary district pages
23. `dist/assets/vs/areas/01/index.html`
24. `dist/assets/vs/areas/02/index.html`
25. `dist/assets/vs/areas/03/index.html`
26. `dist/assets/vs/areas/04/index.html`
27. `dist/assets/vs/areas/05/index.html`
28. `dist/assets/vs/areas/06/index.html`
29. `dist/assets/vs/areas/07/index.html`

Intentional missing paths:
- `dist/assets/vs/area_08.png` — MUST NOT EXIST
- `dist/assets/vs/areas/08/index.html` — MUST NOT EXIST

**Abort deployment unless the official package contains exactly 29 files.**

## 5. Vertical Slice MEDIA_LEDGER status

Source-side MED-001–015 are now satisfied:

- MED-001 current 1–7 screen — SPA current-site view
- MED-002 old disaster top — SPA archive home
- MED-003 old zone list — SPA area list
- MED-004 common zone icons 01–07 — PNG assets
- MED-005 broken 08 asset reference — backup index + absent PNG
- MED-006 backup index — `backup-index.txt`
- MED-007 summer disaster plan — 10-page PDF
- MED-008 water-points list — 3-page PDF containing `旧八号集会所`
- MED-009 PDF metadata panel — browser HTML panel
- MED-010 old update history — ordinary 1998–2004 history
- MED-011 disaster-department contact page — optional ordinary page with non-real contact data
- MED-012 individual district 01–07 pages — seven common-template static pages
- MED-013 district 08 404 — real absent static path
- MED-014 document search top — SPA archive/search route
- MED-015 `旧八号集会所` / 08 search 0-result behavior — SPA search route

The VS spoiler boundary remains intact. Early assets expose only the intended `08` / `第八避難区` / `旧八号集会所` evidence and do not reveal later memory/audio/research theory.

## 6. Reproducible generation

### Evidence media
Generator: `tools/generate_vs_assets.py`
Workflow: `.github/workflows/generate-vs-media.yml`
Run #1: `34344292717` — **SUCCESS**
Generated payload commit: `cc01d0dfbbed15d9db6680310452552c416769cb`

### Ordinary district pages
Generator: `tools/generate_vs_area_pages.py`
Workflow: `.github/workflows/generate-vs-area-pages.yml`
Run #1: `34344963399` — **SUCCESS**
Generated production commit: `2772b9fe11a07f90f5b4b42988ea262061c5a139`

## 7. Current validation gate

Workflow:
`.github/workflows/sites-visual-validate.yml`

Latest validation:
Run #6 / ID `34345109026`
Result: **SUCCESS**
Head SHA: `7fb0271a5873525d6465e99f37d8d37557e34bb8`

Passed:
- existing Sites project id / `dist` hosting configuration
- exact **29-file** package footprint
- 7/7 root SVGs present and valid XML
- original visual asset references resolved
- area 01–07 PNG signatures valid
- `area_08.png` absent
- both PDFs valid file signatures
- backup index contains missing 08 icon/page references
- PDF metadata panel + fiction disclaimer
- ordinary update history
- contact page uses only `000-000-0000` and `example.invalid` plus emergency disclaimer
- seven ordinary district pages exist and use the common rule
- district 08 static page absent
- production UI links to update history, area icon, backup index, PDFs, metadata, area 01 page, contact page
- inline JS extraction + `node --check`
- desktop Chromium `1440×1000`
- mobile Chromium `390×844`
- home / areas / archive?q=08 / diary / map routes
- direct HTTP 200 for required evidence and all district 01–07 pages
- direct HTTP 404 for `area_08.png`
- direct HTTP 404 for `areas/08/index.html`
- no page errors / console errors

Latest QA artifact:
- artifact id: `10101360972`
- name: `sites-visual-qa`
- digest: `sha256:01f85292f915875e7e07cf9e2571da40eb47d66da2d40afb7e7d0c5b3eb513ad`

## 8. Required Sites lifecycle

Execute against the existing Sites project only:

1. Re-fetch `codex-district-eight-sites` HEAD.
2. Review all later changes after `7fb0271a...`; unknown `dist/**` changes require review.
3. Reuse project `appgprj_6a9836915bf48191bd2d504f8ac6c46e`.
4. Push/checkpoint source to the existing Sites checkout.
5. Verify Sites-side source corresponds to the reviewed GitHub payload.
6. Generate/inspect official package.
7. Require **exactly 29 files**.
8. Confirm all seven root SVGs and twenty VS/static evidence files are present.
9. Confirm both intentional 08 paths remain absent.
10. Save a new Sites version.
11. Deploy to production.
12. Poll until terminal success.
13. Confirm production URL.
14. Perform final live visual/evidence QA.

## 9. Production verification

At `https://district-eight.era-0k.chatgpt.site` verify:

### Home
- Nagishiro archive seal and four graphical cards
- fiction disclaimer
- old-site update-history link

### Areas / filename rule
- `area_01.png` works
- `areas/01/index.html` works
- all 01–07 ordinary district pages work
- backup index works
- backup index records 08 missing
- `area_08.png` is absent
- `areas/08/index.html` is absent
- old disaster-department contact page uses only non-real contact data

### Archive search `08`
- 10-page summer disaster-plan PDF works
- 3-page water-points PDF works
- browser metadata panel works
- evidence remains within VS spoiler boundary

### Existing later routes
- document scan, radio cassette, diary, reconstruction-map visuals remain intact
- state progression remains functional
- all six reconstruction landmarks remain visible

### Responsive
- desktop around 1440px coherent
- mobile around 390px coherent
- mobile horizontal navigation usable

## 10. Failure conditions

Do not mark deployment complete if:
- official package count != 29
- any required file is missing
- either intentional 08 path exists
- Sites source differs from reviewed payload
- deployment terminal state is not success
- production still shows the prior 2/9/21-file version
- any required evidence link fails
- JavaScript progression breaks
- fiction disclaimer disappears

## 11. Completion recording

After successful production verification, update Issue #34 with:
- Sites source commit SHA
- GitHub source HEAD used
- `dist/index.html` blob SHA
- official package count = 29
- Sites version number / version id
- deployment result
- production URL
- final live visual/evidence QA PASS

Only then close Issue #34.
