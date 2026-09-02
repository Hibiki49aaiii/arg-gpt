# Full Staging Readiness

Cross-act engineering validation for **第八避難区**.

This gate does not replace Human Blind Playtest Issue #8. It proves that the separately implemented Act 0–6 staging layers remain internally consistent and machine-validatable.

Run:

```bash
python3 works/001-district-eight/full-readiness/validate_full_story.py
```

The master GitHub Actions workflow also executes every existing Act validator before this cross-act validator.
