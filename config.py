"""
config.py — All environment variables in one place.
Copy sample.env → .env and fill in your values.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# ── Required ──────────────────────────────────────────────────────────────────
API_ID          = int(os.environ["34944026"])
API_HASH        = os.environ["d594eb23fbadca610d271dec57d7833b"]
BOT_TOKEN       = os.environ["8803348450:AAGmrTYUbkTl7fXVAnPz-MLZ1VX16igPoak"]
STRING_SESSION  = os.environ["STRING_SESSION"]
MONGO_DB_URL    = os.environ["mongodb+srv://vapplication6_db_user:OUT%20ONKTK3@cluster0.jibatpd.mongodb.net/?appName=Cluster0"]
OWNER_ID        = int(os.environ["8076712430"])

# ── Optional ──────────────────────────────────────────────────────────────────
BOT_NAME         = os.getenv("BOT_NAME", "yorxmusic")
BOT_LINK         = os.getenv("BOT_LINK", "https://t.me/xnknoxbot")
UPDATES_CHANNEL  = os.getenv("UPDATES_CHANNEL", "https://t.me/VIP_PFP_SP")
SUPPORT_GROUP    = os.getenv("SUPPORT_GROUP", "https://t.me/zpaveldurov")
LOGGER_ID        = int(os.getenv("LOGGER_ID", "https://t.me/Yor_login"))
PING_IMG_URL     = os.getenv("PING_IMG_URL", "https://files.catbox.moe/sfqdhn.jpg",)
SESSION_NAME     = os.getenv("SESSION_NAME", "yorxmusic")
PORT             = int(os.getenv("PORT", 10000))

# ── NSFW Moderation API ─────────────────────────────────────────────────────
#NSFW_API_URL = os.getenv("NSFW_API_URL", "https://ai-moderation-api-khyr.onrender.com")
#NSFW_API_KEY = os.getenv("NSFW_API_KEY", "nsfwBad")

# Custom detection thresholds — sent with every /detect/upload call.
#NSFW_THRESHOLDS = {
#    "porn": float(os.getenv("NSFW_THRESHOLD_PORN", "0.7")),
#    "sexy": float(os.getenv("NSFW_THRESHOLD_SEXY", "0.8")),
#}

#── Start ───────────────────────────────────────────────────────────────────────
START_PHOTOS = [
    "https://files.catbox.moe/jgt2vm.png",
]

# ── Limits ────────────────────────────────────────────────────────────────────
MAX_DURATION_SECONDS = 1800   # 30 minutes
QUEUE_LIMIT          = 20
COOLDOWN             = 10     # seconds between /play per chat


#BLOCKED_EXTENSIONS = [
#    ".zip",
#    ".rar",
#    ".7z",
#    ".apk",
#    ".exe",
#    ".py",
#    ".js",
#    ".go",
#    ".php",
#]
