# Act 4 Staging Contract

Machine-readable contract for **Act 4 — Human Memory / Shared Geography**.

This preproduction staging remains intentionally unlinked from Act 0–3 while Human Blind Playtest Issue #8 is pending.

Files:
- `content.json` — diary chronology, ordering references, independent drawing provenance, partial topology, accessibility and spoiler boundaries
- `validate_act4.py` — narrative/chronology/fairness validation

Run:

```bash
python3 works/001-district-eight/implementation/act4-staging/validate_act4.py
```

Source of Truth:
- `ACT4_IMPLEMENTATION.md`
- `ACT4_CONTENT.md`
- `EVIDENCE_LEDGER.md`
- `PUZZLE_LEDGER.md`
- `CHARACTERS.md`
- `TIMELINE.md`


## CI

`.github/workflows/act4-preproduction-validate.yml` validates chronology, pre-incident knowledge, drawing independence, topology fairness, accessibility, spoiler boundaries, and Human Gate isolation.

Act 4 preproduction is complete only when:
- Act 4 Preproduction Validation passes
- Vertical Slice Validation remains green


## Local staging

```bash
python3 -m http.server 8300 --directory works/001-district-eight/implementation/act4-staging/site
```

Open:

```text
http://localhost:8300/school/
```

Useful direct entries:
- `/school/mizuki-diary/`
- `/school/mizuki-diary/references/`
- `/school/elementary/special-collection/drawings/`
- `/school/elementary/special-collection/topology/`
- `/school/elementary/special-collection/partial-map/`

Final child-drawing image assets are intentionally out of scope for this staging pass. The current schematic + text descriptions validate provenance, information distribution, topology fairness, and accessibility.
