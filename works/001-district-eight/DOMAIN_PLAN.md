# 第八避難区 — DOMAIN_PLAN

Status: Production Specification
This document defines URL responsibility and fiction-boundary policy.
Actual domains are not selected or purchased in this phase.

## 1. Objectives

- 複数サイトが別組織に見えること
- Core Storyはproject-controlled infrastructureで完結すること
- 外部SNS/検索サービス停止で詰まないこと
- プレイヤーが「実在行政の緊急情報」と誤認しない安全境界を持つこと
- Act stateを複数site間で安全に共有できること
- 将来、作品002以降と分離できること

## 2. Recommended Ownership Model

Preferred:
1つのproject-owned root domain + 複数subdomain。

Example only:
```text
work001.example.invalid
old-bousai.work001.example.invalid
archives.work001.example.invalid
school-archive.work001.example.invalid
saegusa-log.work001.example.invalid
radio-archive.work001.example.invalid
memory-study.work001.example.invalid
bousai-now.work001.example.invalid
meta.work001.example.invalid
```

Why:
- DNS / TLS / deployment管理が容易
- 全siteを自分で維持可能
- cross-site stateの設計が容易
- typo squatting riskを低減
- ARG 002以降を別namespaceにできる

Visual immersionはhostnameではなく、
site owner / design / copy / page historyで作る。

## 3. URL Responsibility

### In-world URLs
Purpose:
物語体験。

Must not:
- developer docsへ直接link
- spoiler metadata expose
- visible game progress UI

### meta / safety URL
Purpose:
作品外の現実情報。

Contains:
- fiction statement
- safety/contact
- accessibility information
- privacy
- content warning
- emergency-service non-affiliation notice
- credits after release as appropriate

Player can intentionally exit immersion here.

### author/project URL
arg-gpt全体の作品一覧。
第八避難区のin-world siteと視覚的に分離。

## 4. Fiction Boundary

Public release must have a reliable route to confirm:
- this is a fictional interactive work
- fictional municipality / organizations
- not an official disaster or evacuation service
- no real emergency instructions should be taken from in-world pages

Do not imitate:
- current real municipality logos
- emergency alert branding
- national agency marks
- real phone numbers
- real public-service email addresses

All contact-like data:
use controlled domains / non-dialable placeholders during development.

## 5. Municipality Naming Lock

Production name: **凪代市（なぎしろし）**。

Decision rationale:
- 旧仮称「久代市（くしろし）」は実在の釧路市との音声混同リスクが高い。
- Web完全一致検索で現行自治体名としての使用は確認できなかった。
- Public release前には企業名・学校名・ドメイン・SNSハンドルの最終衝突確認のみ再実施する。

この名称はVertical Slice以降のartifactで固定し、安易に変更しない。

## 6. Domain State Strategy

### Preferred for Vertical Slice
No account.
No server-side user profile.

State candidates:
```text
found_area08
opened_plan_pdf
opened_water_list
identified_eighth_district
```

Use:
first-party state controlled by project.

Do not expose:
quest names or progress percentages.

### Full Game
If cross-subdomain state is needed:
- shared signed state token or backend session
- privacy-minimal anonymous session
- no sensitive personal data
- ending state can be stored separately

Do not depend solely on localStorage if multiple origins need synchronized conditional content.

## 7. Search Strategy

Core progression must work without public search ranking.

Supported discovery modes:
1. in-world search pages
2. direct cross-site textual references
3. project-controlled search index
4. optional real search-engine discovery

Public Google/Bing search is enhancement only.

Reason:
indexing/ranking is unstable and spoiler-prone.

## 8. Robots / Indexing

Development:
- noindex
- robots deny where appropriate
- private preview

Release:
Decide per property.

SITE-001 / SITE-004:
may be indexable for ARG feel.

Late-game pages:
must not become search-result spoilers.

Use:
- route gating
- noindex before unlock
- build-time separation where necessary

Do not rely on robots.txt as access control.

## 9. Cookies / Privacy

Target:
minimal anonymous analytics.

No need for:
- login
- email capture
- ad tracking
- third-party behavioral profiles

Analytics events:
- site_entry
- clue_seen
- puzzle_attempted
- puzzle_solved
- hint_used
- act_reached
- ending_selected

Document privacy policy on meta site.

## 10. Link Safety

All project-controlled external-looking links:
open normally in same browser context unless UX reason exists.

Do not:
- auto-download executable files
- request browser permissions unrelated to play
- request location/camera/mic for Core Story
- simulate malware/system alerts
- impersonate OS security prompts

## 11. Domain Failure Strategy

If one property fails:
- core evidence mirrored or recoverable
- status page can redirect to preserved version
- in-world archive can explain preservation without breaking story where possible

Critical backups:
- SITE-001
- SITE-002
- SITE-003
- SITE-005 audio
- SITE-006 research
- ending state

## 12. Deployment Separation

Recommended conceptual packaging:
```text
/apps
  /old-bousai
  /archives
  /school-archive
  /saegusa
  /radio
  /research
  /bousai-now
  /meta

/packages
  /content-schema
  /narrative-state
  /analytics
  /accessibility
  /test-utils
```

Sites may share code internally while remaining visually unrelated.

## 13. Security Requirements

- HTTPS everywhere
- CSP per site
- no secrets in client bundle
- safe file serving
- MIME type correctness
- no user-upload feature for MVP
- sanitize any future search query rendering
- rate limit any server-side hint/search API
- prevent route enumeration from exposing late spoilers where practical

## 14. Release Gate

No public launch until:
- naming lock rechecked for release
- fiction boundary tested
- all contact/address data checked
- no real emergency instructions accidentally copied
- late spoilers protected
- domain ownership verified
- TLS valid
- fallback archive tested
