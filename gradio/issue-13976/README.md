# gradio#13976: gr.Audio rejects .ogg uploads

Issue: https://github.com/gradio-app/gradio/issues/13976

## What the reporter did

- Linux, gradio 6.30.0
- Ran the app below and uploaded an `.ogg` file to `gr.Audio()`
- Got "Invalid file type", even though the message lists `audio/ogg` as allowed

## Files

| File | Purpose |
|---|---|
| `app.py` | The app from the issue, unchanged |
| `sample.ogg` | A real 2 s Vorbis `.ogg` file to upload |
| `requirements.txt` | `gradio==6.30.0`, the reporter's version |

## Steps

1. Start the app:

   ```sh
   uv venv --python 3.12 && uv pip install -r requirements.txt
   .venv/bin/python app.py
   ```

2. Open http://127.0.0.1:7860.

3. Click the audio upload area, pick `sample.ogg`, and note what happens.

The reporter is on Linux. Browsers on other systems may report `.ogg` as
`audio/ogg`, which would hide the bug, so record the OS and browser with each run.

## Results

| Browser | OS | Result |
|---|---|---|
| Chrome | macOS | Accepted. Player loaded, 0:02 duration, no error (2026-10-19) |

## Suspected cause (from reading the code, not yet confirmed by the steps above)

`is_valid_mimetype` in `js/upload/src/utils.ts` matches only two kinds of entry:
extensions (`.ogg`) and wildcards (`audio/*`). Exact MIME entries like
`audio/ogg` are never compared. So an `.ogg` passes only when the browser
reports a type starting with `audio/`. If a Linux browser reports `.ogg` as
something else (for example `video/ogg`, `application/ogg` or empty), the
upload is rejected.
