# 第八避難区 — Blind Playtest Operator Runbook

This is the short operational companion to `PLAYTEST.md`.
The full protocol remains the Source of Truth.

## 1. Start

From repository root:

```bash
python3 works/001-district-eight/implementation/vertical-slice/serve_playtest.py
```

Default:
- Facilitator control: `http://127.0.0.1:8000/meta/playtest.html`
- Tester entry: `http://127.0.0.1:8000/old-bousai/`

The launcher opens the **Facilitator control** page.
Do not show that page to the tester.

## 2. Prepare One Session

Use Session IDs only.

Examples:
- PT-A01
- PT-A02
- PT-B01
- PT-B02
- PT-C01

Do not put a real name, email, account name, or other personal identifier into Session ID.

On the Facilitator control page:

1. Enter Session ID.
2. Click `セッション状態をリセット`.
3. Confirm state/events are empty.
4. Give the tester only the Tester entry URL.

## 3. Tester Prompt

Use the exact script in `PLAYTEST.md`.

Do not explain:
- that it is an ARG
- that 8 is important
- that documents contain clues
- where to click next

## 4. During Session

Use:
`PLAYTEST_OBSERVER_SHEET.md`

Record timestamps and behavior, not coaching.

Primary observation window:
30 minutes.

## 5. End Session

Return to Facilitator control.

1. Click `状態を表示`.
2. Confirm Session ID.
3. Click `JSONをファイル保存`.
4. Save the observer sheet separately with the same Session ID.

The JSON remains browser-local until you explicitly save it.
The page does not upload telemetry.

## 6. Round 1

Required minimum:

| Session | Type |
|---|---|
| PT-A01 | ARG / puzzle experience almost none |
| PT-A02 | ARG / puzzle experience almost none |
| PT-B01 | puzzle experience, little ARG |
| PT-B02 | puzzle experience, little ARG |
| PT-C01 | ARG / Web investigation experience |

After all five:
- fill `PLAYTEST_RESULTS.md`
- calculate M1–M6
- decide PASS / REVISE / FAIL under `PLAYTEST.md`

## 7. Same-machine Privacy

Before a new tester:
- reset state/events
- use a new Session ID
- close previous exported JSON/notes if the tester can see the screen
- do not leave the previous tester's observer sheet open

## 8. Optional Port

If port 8000 is already used:

```bash
python3 works/001-district-eight/implementation/vertical-slice/serve_playtest.py --port 8088
```

Use the URLs printed by the launcher.
