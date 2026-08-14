import os
from os import environ

# ==============================================
# CONFIGURATION — apni values environment se daalo
# (Render/Heroku/Koyeb: Environment Variables section)
# ==============================================

# Telegram API Configuration (ZAROORI - apna daalo)
API_ID = int(os.environ.get("API_ID", "33088642") or 0)
API_HASH = os.environ.get("API_HASH", "bf6a7d6071350cb64849d46b8b4849e9")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8843772830:AAFMHa1dwGtd2stn2Bdt1B-yvJX2Bbkcr2I")

# Caption credit (optional — khali chhod sakte ho)
CREDIT = os.environ.get("CREDIT", "")

# PW Token for PhysicsWallah (PW) player URLs (optional)
PW_TOKEN = os.environ.get("PW_TOKEN", "")

# Optional API tokens (ye bhi purane wale nahi hain — apne aap daalo agar chahiye)
API_TOKEN = os.environ.get("API_TOKEN", "")   # utkarsh ws API token
CW_TOKEN = os.environ.get("CW_TOKEN", "")     # brightcove bcov_auth token

# No database required — sab kuch in-memory chalta hai
DATABASE_NAME = os.environ.get("DATABASE_NAME", "TXT_VIDEO_BOT")
DATABASE_URL = os.environ.get("DATABASE_URL", "")

# Owner and Admin Configuration (ZAROORI - apna Telegram ID daalo)
OWNER_ID = int(os.environ.get("OWNER_ID", "5808599565") or 0)
ADMINS = [int(x) for x in os.environ.get("ADMINS", "5808599565").split() if x.strip().isdigit()]

# Channel Configuration
PREMIUM_CHANNEL = ""

# Thumbnail Configuration
THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "").split()))

# Web Server Configuration
WEB_SERVER = os.environ.get("WEB_SERVER", "False").lower() == "true"
WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8000))

# Message Formats
AUTH_MESSAGES = {
    "subscription_active": """<b>🎉 Subscription Activated!</b>

<blockquote>Your subscription has been activated and will expire on {expiry_date}.
You can now use the bot!</blockquote>\n\n Type /start to start uploading """,

    "subscription_expired": """<b>⚠️ Your Subscription Has Ended</b>

<blockquote>Your access to the bot has been revoked as your subscription period has expired.
Please contact the admin to renew your subscription.</blockquote>""",

    "user_added": """<b>✅ User Added Successfully!</b>

<blockquote>👤 Name: {name}
🆔 User ID: {user_id}
📅 Expiry: {expiry_date}</blockquote>""",

    "user_removed": """<b>✅ User Removed Successfully!</b>

<blockquote>User ID {user_id} has been removed from authorized users.</blockquote>""",

    "access_denied": """<b>⚠️ Access Denied!</b>

<blockquote>You are not authorized to use this bot.
Please contact the admin to get access.</blockquote>""",

    "not_admin": "⚠️ You are not authorized to use this command!",
    
    "invalid_format": """❌ <b>Invalid Format!</b>

<blockquote>Use format: {format}</blockquote>"""
}
