# TXT-TO-VIDEO-UPLOADEE-IN-TG

Telegram bot that reads a `.txt` file containing `Name: URL` lines, downloads the
videos (including DRM / Appx-encrypted / YouTube / HLS / direct links) and uploads
them to your channel/chat as videos.

The bot code lives in [`upploder11--main/`](upploder11--main).

> ✅ **No database required** — MongoDB is fully removed. The bot works with
> just `BOT_TOKEN`, `API_ID`, `API_HASH` and `OWNER_ID`.

## How to run

```bash
cd upploder11--main
pip install -r itsgolubots.txt
python3 main.py
```

Required env vars (see `.env.example`):

| Variable      | Description                          | Required |
|---------------|--------------------------------------|----------|
| `API_ID`      | Telegram API ID (my.telegram.org)    | ✅       |
| `API_HASH`    | Telegram API hash                    | ✅       |
| `BOT_TOKEN`   | Telegram bot token (@BotFather)      | ✅       |
| `OWNER_ID`    | Owner Telegram ID (@userinfobot)     | ✅       |
| `ADMINS`      | Space-separated admin IDs            | optional |
| `CREDIT`      | Caption credit name (leave empty to remove) | optional |
| `PW_TOKEN`    | PW player token                      | optional |
| `API_TOKEN`   | utkarsh ws API token                 | optional |
| `CW_TOKEN`    | brightcove bcov_auth token           | optional |
| `THUMBNAILS`  | Default thumbnail image URL          | optional |

System requirements: `ffmpeg`, `aria2`, `yt-dlp`, `mp4decrypt` (Bento4) — the
`Dockerfile` installs all of them automatically.

## Main commands

- `/drm` — send a `.txt` file with `Name: https://link` lines; the bot downloads
  every link and uploads videos to the configured channel.
- Send a plain link in a private chat — the bot asks for resolution and uploads
  the video back to you.
- `/t2t`, `/t2h`, `/cookies`, `/plan`, `/add`, `/remove`, `/users` — utilities.

## Security notes

- All pre-existing credentials (old bot token, API keys, MongoDB URL, owner IDs)
  have been **removed** from the code. The bot will not run until you provide
  your own credentials via environment variables.
- All "made by" branding / developer links / logos have been removed.
