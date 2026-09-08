# 第八避難区 — OpenAI Sites Final Deployment Handoff

Status: READY FOR SITES DEPLOYMENT

この文書は、GitHub側で完成・検証済みのSites公開物を、既存OpenAI Sitesプロジェクトへ再公開するための最終引継ぎです。

## 1. 絶対にやり直さないこと

- Sitesプロジェクトを新規作成しない
- slugを変更しない
- ARGのストーリー／状態機械／分岐を再設計しない
- mainへマージすることを公開条件にしない
- `dist/index.html` のJavaScriptを変更しない
- 既存のproduction URLを変更しない

## 2. Source of Truth

Repository:
`Hibiki49aaiii/arg-gpt`

Branch:
`codex-district-eight-sites`

Deployment source HEAD at handoff creation:
`addd2fdd61f4e512a046c783c33a0369f62ae0cf`

Visual payload HTML blob:
`dist/index.html` = `0defa2376386ccd033f4c88f4b97b6aa55a4807b`

Latest reconstruction-map asset blob:
`dist/assets/reconstruction-map.svg` = `79f278f49c239d348f3506e28138702cf0289f1f`

Before deployment, re-fetch branch HEAD. If it differs from the value above, review the later diff before publishing. Do not silently publish an unknown later commit.

## 3. Existing Sites Project

Project ID:
`appgprj_6a9836915bf48191bd2d504f8ac6c46e`

Static directory:
`dist`

Production URL:
`https://district-eight.era-0k.chatgpt.site`

`.openai/hosting.json` must still resolve to the project id above and static directory `dist`.

## 4. Expected Official Package

Expected total Sites package file count: **9**

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

**Abort deployment if the Sites package contains fewer than 9 files.**

## 5. Visual Payload

The production visual pass includes:
- fictional Nagishiro municipal archive seal
- evacuation district map graphic
- municipal archive index graphic
- scanned internal disaster-document graphic
- disaster-radio cassette graphic
- Yui Mizuki diary-fragment graphic
- District Eight reconstruction-map graphic
- archival paper / FAX / scan / cassette / notebook visual treatment
- distinct 2026 current-site presentation

The assets are original fictional project graphics. They do not reproduce a real municipal seal, real emergency map, or real emergency instructions.

## 6. Validation Already Completed

GitHub Actions workflow:
`.github/workflows/sites-visual-validate.yml`

Latest validation run at handoff creation:
Run #4 / ID `34288908516`

Result: **SUCCESS**

Passed:
- hosting project id check
- static directory check
- expected 9-file package footprint
- 7/7 SVG existence
- 7/7 SVG XML parse
- all SVG references resolved from `index.html`
- no unexpected SVG reference
- inline JavaScript extraction
- `node --check` JavaScript syntax
- required fiction-boundary strings
- desktop Chromium `1440x1000`
- mobile Chromium `390x844`
- no page error
- no console error
- no unexpected HTTP >=400 response
- home visual asset application
- diary visual asset application
- reconstruction-map visual asset application

Latest QA artifact:
- artifact id: `10080573294`
- name: `sites-visual-qa`
- digest: `sha256:54e82b2842f2210c640b6fb36f3a8244409322df6bd877a54af5ff551e7b8872`

The QA screenshots were manually reviewed after Run #4. Desktop and mobile layouts are visually coherent and the reconstruction-map preview keeps all six major landmarks inside the visible safe region.

## 7. Required Sites Lifecycle

Execute using the existing Sites project only:

1. Re-fetch `codex-district-eight-sites` HEAD.
2. Confirm the intended source commit/diff.
3. Open/reuse Sites project `appgprj_6a9836915bf48191bd2d504f8ac6c46e`.
4. Push/checkpoint the repository source into the existing Sites checkout.
5. Confirm Sites-side source commit corresponds to the reviewed GitHub source.
6. Generate/inspect the official package.
7. Require official package file count = **9**.
8. Confirm all seven `dist/assets/*.svg` files exist in the Sites package.
9. Save a new Sites version.
10. Deploy that version to production.
11. Poll deployment until terminal success.
12. Obtain/confirm production URL.
13. Open the production URL and perform final visual verification.

## 8. Production Verification

At `https://district-eight.era-0k.chatgpt.site`, verify at minimum:

### Home
- Nagishiro archive seal visible in masthead
- four graphical archive cards visible
- fiction disclaimer visible

### Documents
- scanned-document treatment visible
- no JavaScript/runtime error

### Radio
- cassette/recording visual treatment visible

### Diary
- diary-fragment visual present

### Reconstruction Map
- all six landmarks visible in preview graphic
- generated reconstruction map below remains functional

### Responsive
- desktop layout coherent around 1440px width
- mobile layout coherent around 390px width
- navigation remains usable horizontally on mobile

## 9. Failure Conditions

Do not mark deployment complete if any of the following occurs:
- package file count < 9
- any SVG missing
- Sites source does not correspond to reviewed GitHub source
- deployment terminal state is not success
- production URL still renders the pre-graphics 2-file version
- JavaScript state progression breaks
- fiction disclaimer disappears

## 10. Completion Recording

After successful production verification, update GitHub Issue #34 with:
- Sites source commit SHA
- GitHub source HEAD used
- `dist/index.html` blob SHA
- official package file count
- Sites version number / version id
- deployment result
- production URL
- final visual QA PASS

Then close Issue #34 as completed.
