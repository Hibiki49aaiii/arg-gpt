# Act 6 Staging Contract

Machine-readable contract for **Act 6 — The Missing Whole / Seven Became Eight / Endings**.

This directory is intentionally unlinked from Act 0–5 while Human Blind Playtest Issue #8 remains open.

Files:
- `content.json` — candidate graph, distance constraints, evidence support, EV-032 provenance, reality fixtures, state machine, ending persistence
- `validate_act6.py` — 6! uniqueness enumeration and state/ending validation

Run:

```bash
python3 works/001-district-eight/implementation/act6-staging/validate_act6.py
```

Source of Truth:
- `ACT6_IMPLEMENTATION.md`
- `ACT6_CONTENT.md`
- `EVIDENCE_LEDGER.md`
- `PUZZLE_LEDGER.md`
- `SITE_MAP.md`


## CI

`.github/workflows/act6-preproduction-validate.yml` verifies:
- 6! constraint uniqueness
- evidence support minimums
- generated-vs-found map semantics
- reality A/B fixture invariants
- no-glitch state change
- PZ-012 gating
- END-A/B/C mechanical distinction
- Human Gate #8 isolation

Act 6 preproduction is complete only when both Act 6 validation and Vertical Slice regression pass on the same pull request.


## Local staging

```bash
python3 -m http.server 8500 --directory works/001-district-eight/implementation/act6-staging/site
```

Open:

```text
http://localhost:8500/
```

Suggested staging flow:
1. `/bousai-now/areas/` — baseline 1〜7
2. `/old-bousai/disaster/areas/08/` — baseline missing
3. `/workspace/` — solve PZ-011
4. revisit both reality anchors
5. return to `/workspace/`
6. `/ending/` — choose persistence policy
7. `/ending/result/` — inspect persistent result

Development reset:
`/meta/`

## Staging completion gate

Issue #28 is complete only when the same pull request passes:
- Act 6 Preproduction Validation
- Vertical Slice Validation

Human Blind Playtest Issue #8 remains the runtime-integration gate.


## Post-implementation validation

The final staging gate additionally checks:
- all local HTML references
- PZ-011 workspace selectors and canonical state transition
- EV-032 generated/provenance copy
- SITE-007 dynamic A/B template
- SITE-001 /08 dynamic A/B template
- PZ-012 both-anchor state
- ending lock and result distinction
- local reset tool
- no hidden state identifiers in in-world HTML
