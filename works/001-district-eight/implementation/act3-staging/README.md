# Act 3 Staging Contract

Machine-readable contract for **Act 3 — 33 Seconds**.

This directory contains preproduction timing, evidence, alignment, and accessibility invariants. It is intentionally not connected to the current Act 0–1 or Act 2 runtimes while Human Blind Playtest Issue #8 is pending.

Files:
- `content.json` — canonical Act 3 timing/evidence contract
- `validate_act3.py` — arithmetic, provenance, transcript-leakage, accessibility, and isolation validation

Run:

```bash
python3 works/001-district-eight/implementation/act3-staging/validate_act3.py
```

Source of Truth:
- `ACT3_IMPLEMENTATION.md`
- `ACT3_CONTENT.md`
- `TIMELINE.md`
- `EVIDENCE_LEDGER.md`
- `PUZZLE_LEDGER.md`


## CI

`.github/workflows/act3-preproduction-validate.yml` validates timing arithmetic, receiver independence, transcript leakage, accessibility equivalence, and isolation from earlier runtimes.

Act 3 preproduction is complete only when:
- Act 3 Preproduction Validation passes
- Vertical Slice regression remains green


## Local staging

```bash
python3 -m http.server 8200 --directory works/001-district-eight/implementation/act3-staging/site
```

Open:

```text
http://localhost:8200/radio/
```

Useful direct entries:
- `/archives/inquiry/1998-08-14/`
- `/old-bousai/sender-log/`
- `/radio/1998-08-14/`
- `/radio/compare/1998-08-14/`

Final recorded audio assets are intentionally out of scope for this staging pass. The waveform, duration, transcript-fragment, and alignment UI are sufficient to validate the narrative/puzzle structure.


## Staging completion gate

Issue #15 is complete only when the same pull request passes:
- Act 3 Preproduction Validation
- Vertical Slice Validation

The human discovery gate remains separate in Issue #8.
