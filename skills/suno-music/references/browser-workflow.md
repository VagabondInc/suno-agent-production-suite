# Browser-Assisted Suno Workflow

Use this workflow for every normal song-creation request unless the user explicitly requests text-only output. Use `$computer-use:computer-use` and read its `SKILL.md` completely before operating the browser.

1. Finish and validate title, 1000-character Style Description, Excluded Styles, Weirdness, Style Influence, and tagged Lyrics before opening the browser.
2. Use Computer Use to open `https://suno.com/create` in the user's default browser. Refresh accessibility state after every action; never reuse stale element indexes.
3. If Suno shows a login or verification screen, pause and ask the user to complete it manually, then say: `Once you are logged into Suno, reply continue and I will resume.` Do not request or handle credentials, cookies, passwords, or verification codes.
4. Enable **Custom** mode.
5. Fill Title, Lyrics, Styles, and Excluded Styles with the validated values. Advanced Options may need to be expanded before Excluded Styles and sliders are visible.
6. Set Weirdness to the selected value and Style Influence to the selected value. Re-read the displayed values and enforce Weirdness ≤80 and Style Influence ≥25. If the UI uses different slider names, identify them semantically; do not guess.
7. Re-read every visible field after entry to detect truncation, misplaced text, a mode change, or a slider that failed to move. If Suno exposes a smaller field limit, stop and report it rather than silently truncating.
8. Leave **Create** untouched and tell the user the fields are ready. Click **Create** only after explicit action-time authorization for the visible credit-consuming generation.
9. After submission, verify what the current UI returns. Do not claim generation succeeded until completed results are visible.
10. If the user wants files, use the currently visible download controls; do not promise MP3 availability without checking.

Browser layouts and model limits change. Prefer visible labels and state over fixed coordinates or stale screenshots. One submission is one stopping condition; do not retry, regenerate, extend, or spend more credits without fresh user authorization.
