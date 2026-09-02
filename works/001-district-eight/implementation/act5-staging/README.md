# Act 5 Staging Contract

Machine-readable contract for **Act 5 — Records / Reverse Citation / Saegusa**.

Act 5 remains intentionally unlinked from earlier runtimes while Human Blind Playtest Issue #8 is pending.

Files:
- `content.json` — maps, fixed anchors, record differences, Kiritani reverse citations, containment trend, Saegusa chronology
- `validate_act5.py` — chronology, evidence-role, causal-strength and Act 6 spoiler validation

Run:

```bash
python3 works/001-district-eight/implementation/act5-staging/validate_act5.py
```

Source of Truth:
- `ACT5_IMPLEMENTATION.md`
- `ACT5_CONTENT.md`
- `EVIDENCE_LEDGER.md`
- `PUZZLE_LEDGER.md`
- `CHARACTERS.md`
- `TIMELINE.md`


## CI

`.github/workflows/act5-preproduction-validate.yml` validates map chronology, fixed anchors, record-side corroboration, reverse citations, containment correlation wording, Saegusa chronology, Act 6 spoiler boundaries, and Human Gate isolation.

Act 5 preproduction is complete only when:
- Act 5 Preproduction Validation passes
- Vertical Slice Validation remains green


## Local staging

```bash
python3 -m http.server 8400 --directory works/001-district-eight/implementation/act5-staging/site
```

Open:

```text
http://localhost:8400/archives/
```

Useful direct entries:
- `/archives/maps/`
- `/archives/maps/compare/`
- `/archives/phonebook/`
- `/research/kiritani/note-a/`
- `/research/kiritani/reverse-citation/`
- `/research/containment/`
- `/saegusa/timeline/`

Final map scans/PDF assets are intentionally outside this staging pass. Current schematics validate chronology, information distribution, puzzle gating, causal-strength wording, and accessibility.
