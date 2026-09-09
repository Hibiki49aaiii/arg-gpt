# 第八避難区 — OpenAI Sites Final Deployment Handoff

Status: READY FOR SITES DEPLOYMENT

この文書は、GitHub側で完成・検証済みのSites公開物を、既存OpenAI Sitesプロジェクトへ再公開するための最終引継ぎです。

## 1. 絶対にやり直さないこと

- Sitesプロジェクトを新規作成しない
- slugを変更しない
- ARGのストーリー／状態機械／分岐を再設計しない
- mainへマージすることを公開条件にしない
- `dist/index.html` の既存状態機械を置き換えない
- 既存のproduction URLを変更しない

## 2. Source of Truth

Repository:
`Hibiki49aaiii/arg-gpt`

Branch:
`codex-district-eight-sites`

Reviewed production payload commit:
`cc01d0dfbbed15d9db6680310452552c416769cb`

21-file validation workflow commit:
`60b6b5dae7f3c362b23c76c046736518b57ba490`

Current production HTML blob after Vertical Slice media integration:
`dist/index.html` = `6d3c07e3d2d9b6128230764f354cf02e1db3f281`

Reconstruction-map asset blob:
`dist/assets/reconstruction-map.svg` = `79f278f49c239d348f3506e28138702cf0289f1f`

The branch may contain later documentation-only handoff commits. Before deployment, re-fetch branch HEAD and review later diffs. The publishable `dist/` payload must correspond to the reviewed media payload above or an explicitly reviewed successor.

## 3. Existing Sites Project

Project ID:
`appgprj_6a9836915bf48191bd2d504f8ac6c46e`

Static directory:
`dist`

Production URL:
`https://district-eight.era-0k.chatgpt.site`

`.openai/hosting.json` must still resolve to the project id above and static directory `dist`.

## 4. Expected Official Package

Expected total Sites package file count: **21**

Required files:
1. `.openai/hosting.json`
2. `dist/index.html`
3. `dist/assets/nagishiro-seal.svg`
4. `dist/assets/evacuation-map.svg`
5. `dist/assets/archive-index.svg`
6. `dist/assets/document-scan.svg`
7. `dist/assets/radio-cassette.svg`
8. `dist/assets/diary-fragment.svg`
9. `dist/assets/reconstruction-map.svg`
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

`dist/assets/vs/area_08.png` **must not exist**. Its absence is an intentional clue and is preserved in `backup-index.txt` as `MISSING`.

**Abort deployment if the official package file count is not exactly 21.**

## 5. Visual / Evidence Payload

Production now includes two layers.

### Archival visual layer
- fictional Nagishiro municipal archive seal
- evacuation district map graphic
- municipal archive index graphic
- scanned internal disaster-document graphic
- disaster-radio cassette graphic
- Yui Mizuki diary-fragment graphic
- District Eight reconstruction-map graphic
- archival paper / FAX / scan / cassette / notebook visual treatment

### Vertical Slice evidence media
- common `area_01.png`–`area_07.png` filename/image rule
- intentionally missing `area_08.png`
- backup index retaining the broken 08 reference
- 10-page `平成10年夏季防災計画` PDF
- 3-page `給水地点一覧` PDF containing `旧八号集会所`
- browser-readable PDF metadata page
- ordinary old-site update history from 1998–2004
- production UI links to the above assets at spoiler-appropriate routes

All new assets are original fictional project media. They do not reproduce a real municipal seal, real emergency map, real contact information, or real emergency instructions.

## 6. Reproducible Media Generation

Generator:
`tools/generate_vs_assets.py`

Generation workflow:
`.github/workflows/generate-vs-media.yml`

Generator Run #1:
ID `34344292717`
Result: **SUCCESS**

Generated asset commit:
`cc01d0dfbbed15d9db6680310452552c416769cb`

The generator validates:
- 7 PNG icons exist and are valid PNGs
- `area_08.png` stays absent
- disaster-plan PDF = 10 pages with expected metadata
- water-points PDF = 3 pages with expected metadata
- backup index contains the missing 08 entries
- all new evidence links are injected into `dist/index.html`

## 7. Validation Already Completed

GitHub Actions workflow:
`.github/workflows/sites-visual-validate.yml`

Latest validation:
Run #5 / ID `34344454607`
Result: **SUCCESS**

Passed:
- hosting project id check
- static directory check
- exact **21-file** package footprint
- 7/7 original SVG existence and XML parse
- all original SVG references resolved
- 12/12 Vertical Slice evidence-media files present
- PNG signatures valid for area 01–07
- `area_08.png` confirmed absent
- PDF signatures valid
- backup-index missing-08 markers present
- PDF metadata page and fiction disclaimer present
- update-history ordinary-content range present
- production UI links to VS assets present
- inline JavaScript extraction
- `node --check` JavaScript syntax
- desktop Chromium `1440x1000`
- mobile Chromium `390x844`
- home / areas / archive / diary / reconstruction-map routes
- direct HTTP 200 checks for all new linked evidence assets
- direct HTTP 404 check for intentionally absent `area_08.png`
- no page error
- no console error
- no unexpected page HTTP >=400 response

Latest QA artifact:
- artifact id: `10101096713`
- name: `sites-visual-qa`
- digest: `sha256:85f2672f5f40bff4e44750debccadb54b7e6ba501c8571923a8c8f5497f5eeac`

## 8. Required Sites Lifecycle

Execute using the existing Sites project only:

1. Re-fetch `codex-district-eight-sites` HEAD.
2. Review commits after `60b6b5dae7f3c362b23c76c046736518b57ba490`; documentation-only changes are acceptable, but unknown `dist/` changes require review.
3. Open/reuse Sites project `appgprj_6a9836915bf48191bd2d504f8ac6c46e`.
4. Push/checkpoint the repository source into the existing Sites checkout.
5. Confirm Sites-side source corresponds to the reviewed GitHub source.
6. Generate/inspect the official package.
7. Require official package file count = **21**.
8. Confirm all 7 root SVG assets and all 12 `dist/assets/vs/` files exist.
9. Confirm `dist/assets/vs/area_08.png` is absent.
10. Save a new Sites version.
11. Deploy that version to production.
12. Poll deployment until terminal success.
13. Confirm production URL.
14. Open production and perform final visual/evidence verification.

## 9. Production Verification

At `https://district-eight.era-0k.chatgpt.site`, verify at minimum:

### Home
- Nagishiro archive seal visible
- four graphical archive cards visible
- fiction disclaimer visible
- old-site update-history link works

### Areas
- filename-rule note appears
- `area_01.png` opens
- backup index opens
- backup index records `area_08.png MISSING`

### Archive search `08`
- `平成10年夏季防災計画` opens
- `給水地点一覧` opens
- PDF metadata page opens
- evidence does not expose later-act spoilers beyond Vertical Slice boundaries

### Documents / Radio / Diary / Map
- existing scan/cassette/diary/map visual treatments remain intact
- JavaScript state progression remains functional
- all six reconstruction landmarks remain visible

### Responsive
- desktop coherent around 1440px width
- mobile coherent around 390px width
- horizontal mobile navigation remains usable

## 10. Failure Conditions

Do not mark deployment complete if any of the following occurs:
- official package file count != 21
- any required SVG or VS asset missing
- `area_08.png` unexpectedly exists
- Sites source does not correspond to reviewed GitHub source
- deployment terminal state is not success
- production still renders the old 2-file/9-file version
- any new PDF/TXT/HTML evidence link returns an error
- JavaScript state progression breaks
- fiction disclaimer disappears

## 11. Completion Recording

After successful production verification, update GitHub Issue #34 with:
- Sites source commit SHA
- GitHub source HEAD used
- `dist/index.html` blob SHA
- official package file count = 21
- Sites version number / version id
- deployment result
- production URL
- final visual/evidence QA PASS

Then close Issue #34 as completed.
