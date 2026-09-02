# Act 2 Staging

Machine-readable staging contract for **Act 2 — The Missing People**.

This directory is intentionally **not linked** from the Act 0–1 Vertical Slice while Human Blind Playtest Issue #8 is pending.

Files:
- `content.json`: player-facing facts and puzzle contracts
- `validate_act2.py`: timeline / identity / spoiler / isolation validator

Run:

```bash
python3 works/001-district-eight/implementation/act2-staging/validate_act2.py
```

The staging contract is subordinate to:
- `ACT2_IMPLEMENTATION.md`
- `ACT2_CONTENT.md`
- `TIMELINE.md`
- `CHARACTERS.md`

## CI

`.github/workflows/act2-preproduction-validate.yml` verifies timeline ordering, identity keys, spoiler boundaries, and Human Gate isolation.


## Local staging

```bash
python3 -m http.server 8100 --directory works/001-district-eight/implementation/act2-staging/site
```

Open:

```text
http://localhost:8100/
```

The staging site uses root-relative paths and is self-contained under this server root.

Current Act 0–1 Vertical Slice remains a separate runtime and intentionally has no link to this staging site while Human Blind Playtest Issue #8 is pending.


## Staging completion gate

Issue #11 is complete only when both:
- Act 2 Preproduction Validation
- Vertical Slice Validation

pass on the same pull request.
