import os
from datetime import datetime, timedelta
from typing import Optional, Dict, List

from vars import OWNER_ID, ADMINS

# ============================================================
# Lightweight in-memory database.
# NO MongoDB required — bot works fully without any database.
# Data is stored in memory only (resets when bot restarts).
# ============================================================


class Database:
    def __init__(self):
        self._users: Dict[tuple, dict] = {}          # (bot_username, user_id) -> user doc
        self._bot_settings: Dict[str, dict] = {}     # bot_username -> {"log_channel": id}

    # ---------- helpers ----------

    def _is_owner(self, user_id: int) -> bool:
        try:
            if user_id == OWNER_ID:
                return True
            return bool(ADMINS) and user_id in ADMINS
        except Exception:
            return False

    # ---------- auth ----------

    def is_admin(self, user_id: int) -> bool:
        """Check if user is admin or owner."""
        try:
            return self._is_owner(user_id)
        except Exception:
            return False

    def is_user_authorized(self, user_id: int, bot_username: str = "TXT_VIDEO_BOT") -> bool:
        """Everyone is allowed — no subscription/database required."""
        return True

    def is_channel_authorized(self, chat_id: int, bot_username: str = "TXT_VIDEO_BOT") -> bool:
        """All channels are allowed."""
        return True

    # ---------- users ----------

    def get_user(self, user_id: int, bot_username: str = "TXT_VIDEO_BOT") -> Optional[dict]:
        try:
            return self._users.get((bot_username, user_id))
        except Exception:
            return None

    def add_user(self, user_id: int, name: str, days: int,
                 bot_username: str = "TXT_VIDEO_BOT") -> tuple:
        """
        Add or update a user in memory.

        Returns:
            Tuple of (success, expiry_date)
        """
        try:
            expiry_date = datetime.now() + timedelta(days=days)
            self._users[(bot_username, user_id)] = {
                "name": name,
                "expiry_date": expiry_date,
                "added_date": datetime.now(),
                "last_updated": datetime.now()
            }
            return True, expiry_date
        except Exception as e:
            print(f"Add user error for {user_id}: {str(e)}")
            return False, None

    def remove_user(self, user_id: int, bot_username: str = "TXT_VIDEO_BOT") -> bool:
        try:
            return self._users.pop((bot_username, user_id), None) is not None
        except Exception as e:
            print(f"Remove user error for {user_id}: {str(e)}")
            return False

    def list_users(self, bot_username: str = "TXT_VIDEO_BOT") -> List[dict]:
        try:
            return [
                {"name": u.get("name"), "user_id": uid, "expiry_date": u.get("expiry_date")}
                for (bun, uid), u in self._users.items()
                if bun == bot_username
            ]
        except Exception as e:
            print(f"List users error: {str(e)}")
            return []

    def get_user_expiry_info(self, user_id: int, bot_username: str = "TXT_VIDEO_BOT") -> Optional[dict]:
        try:
            user = self.get_user(user_id, bot_username)
            if not user:
                return None

            expiry = user.get('expiry_date')
            if not expiry:
                return None

            if isinstance(expiry, str):
                expiry = datetime.strptime(expiry, "%Y-%m-%d %H:%M:%S")

            days_left = (expiry - datetime.now()).days

            return {
                "name": user.get('name', 'Unknown'),
                "user_id": user_id,
                "expiry_date": expiry.strftime("%d-%m-%Y"),
                "days_left": days_left,
                "added_date": user.get('added_date', 'Unknown'),
                "is_active": days_left > 0
            }
        except Exception as e:
            print(f"Get expiry info error for {user_id}: {str(e)}")
            return None

    async def cleanup_expired_users(self, bot) -> int:
        """Remove expired in-memory users."""
        removed_count = 0
        try:
            current_time = datetime.now()
            expired = [
                ((bun, uid), u) for (bun, uid), u in self._users.items()
                if isinstance(u.get("expiry_date"), datetime) and u["expiry_date"] < current_time
            ]
            for key, user in expired:
                self._users.pop(key, None)
                removed_count += 1
        except Exception as e:
            print(f"Cleanup error: {str(e)}")
        return removed_count

    # ---------- settings ----------

    def get_log_channel(self, bot_username: str):
        try:
            settings = self._bot_settings.get(bot_username)
            if settings and 'log_channel' in settings:
                return settings['log_channel']
            return None
        except Exception:
            return None

    def set_log_channel(self, bot_username: str, channel_id: int):
        try:
            self._bot_settings.setdefault(bot_username, {})['log_channel'] = channel_id
            return True
        except Exception:
            return False

    def list_bot_usernames(self) -> List[str]:
        usernames = {bun for (bun, _uid) in self._users.keys()}
        usernames.update(self._bot_settings.keys())
        return list(usernames) or ["TXT_VIDEO_BOT"]

    # ---------- lifecycle ----------

    def close(self):
        self._users.clear()
        self._bot_settings.clear()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


print("🤖 Database: in-memory mode (no MongoDB required)")

# 🔌 Global instance
db = Database()
