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
