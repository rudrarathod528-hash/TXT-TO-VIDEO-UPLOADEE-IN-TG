# TXT-TO-VIDEO-UPLOADEE-IN-TG

Telegram bot that reads a `.txt` file containing `Name: URL` lines, downloads the
videos (including DRM / Appx-encrypted / YouTube / HLS / direct links) and uploads
them to your channel/chat as videos.

The bot code lives in [`upploder11--main/`](upploder11--main).

## How to run

```bash
cd upploder11--main
pip install -r itsgolubots.txt
python3 main.py
```

Required env vars (or defaults in `vars.py`):

| Variable      | Description                          |
|---------------|--------------------------------------|
| `API_ID`      | Telegram API ID                      |
| `API_HASH`    | Telegram API hash                    |
| `BOT_TOKEN`   | Telegram bot token                   |
| `DATABASE_URL`| MongoDB connection string (auth)     |
| `OWNER_ID`    | Owner Telegram ID                    |
| `ADMINS`      | Space-separated admin IDs            |
| `CREDIT`      | Caption credit name                  |
| `PW_TOKEN`    | (optional) PW player token           |

System requirements: `ffmpeg`, `aria2`, `yt-dlp`, `mp4decrypt` (Bento4) — the
`Dockerfile` installs all of them automatically.

## Main commands

- `/drm` — send a `.txt` file with `Name: https://link` lines; the bot downloads
  every link and uploads videos to the configured channel.
- Send a plain link in a private chat — the bot asks for resolution and uploads
  the video back to you.
- `/t2t`, `/t2h`, `/cookies`, `/plan`, `/add`, `/remove`, `/users` — utilities.

## Bug fixes applied

- **Videos not uploading**: `download_video()` returned a fake file name even when
  the download failed, then crashed during upload with "Downloading Failed".
  Now it verifies the real output file exists and returns `None` on failure.
- **Missing functions crashed download paths**: `download_and_decrypt_video()`,
  `decrypt_file()` (Appx XOR decryption) and `get_mps_and_keys2()` (classplus DRM
  keys API) were referenced but never defined — every Appx / DRM fallback link
  failed with `AttributeError`. They are now implemented.
- **`os.exists()` typo** (should be `os.path.exists()`) made every Appx-encrypted
  video fail even after a successful download+decrypt.
- **Undefined `ClientSession`** crashed visionias playlist extraction.
- **Undefined `mpd` / `keys_string`** crashed `drmcdni` / `drm/wv` / `drm/common`
  URLs (`NameError`). Now defaulted per iteration.
- **YouTube downloads failed** whenever `youtube_cookies.txt` was missing —
  `--cookies` is now only passed when the file exists.
- **Channel usage crashed** (`m.from_user` is `None` in channels) — user id is
  now resolved safely for channel commands.
- **Non-numeric / empty user input** crashed the /drm flow (`int("abc")`) — all
  `listen()` steps are now timeout-safe with validated defaults.
- **`text_handler` (plain link) did nothing** after asking for resolution — the
  download + upload flow is now implemented.
- **Thumbnail watermark** used `font.ttf` (repo ships `font.otf`) and fragile
  shell escaping — now uses `font.otf` + a `textfile`, and never breaks the
  upload if watermarking fails.
- **`duration()`/`get_duration()`** crashed on missing/corrupt files — now return
  `0` gracefully so uploads continue.
- **`decrypt_and_merge_video()`** now handles single-file streams, missing keys,
  and verifies the merged output instead of blindly failing.
- **Blocking `time.sleep()`** inside async handlers replaced with `await asyncio.sleep()`.
- **Google Drive links** now download via yt-dlp (old code wrote the Drive HTML
  page as a `.pdf` and failed on big files).
- PDF / image / audio / `.ws` downloads now verify the output file before upload
  and report a proper failure message otherwise.
- Batch-message pinning no longer tries to pin a non-existent message id.
