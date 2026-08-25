"""EUF Multi-User Profile and Portable Progress Manager.
Keeps personal user study progress (solved status, notes, attempts) isolated from the core read-only question bank.
"""

import os
import json
import sqlite3

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILES_DIR = os.path.join(BASE_DIR, "profiles")
os.makedirs(PROFILES_DIR, exist_ok=True)

ACTIVE_PROFILE_FILE = os.path.join(PROFILES_DIR, ".active_profile")


def get_active_profile_name():
    """Returns the name of the currently active study profile."""
    if os.path.exists(ACTIVE_PROFILE_FILE):
        try:
            with open(ACTIVE_PROFILE_FILE, "r", encoding="utf-8") as f:
                name = f.read().strip()
                if name:
                    return name
        except Exception:
            pass
    return "default"


def set_active_profile_name(profile_name):
    """Sets the active study profile."""
    clean_name = re.sub(r'[^a-zA-Z0-9_-]', '_', profile_name.strip())
    with open(ACTIVE_PROFILE_FILE, "w", encoding="utf-8") as f:
        f.write(clean_name)
    return clean_name


def get_profile_path(profile_name=None):
    """Returns the JSON file path for a profile."""
    if not profile_name:
        profile_name = get_active_profile_name()
    clean_name = "".join(c for c in profile_name if c.isalnum() or c in ('_', '-')).strip() or "default"
    return os.path.join(PROFILES_DIR, f"{clean_name}.json")


def load_user_profile(profile_name=None):
    """Loads user study data. If fresh user, returns a clean empty progress dict."""
    path = get_profile_path(profile_name)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "profile_name": profile_name or get_active_profile_name(),
        "created_at": None,
        "questions": {},  # {qid: {"status": "solved", "notes": "...", "flag": "...", "errata": "..."}}
        "history": []
    }


def save_user_profile(data, profile_name=None):
    """Saves user study progress to their portable JSON file."""
    path = get_profile_path(profile_name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_question_user_state(qid, profile_name=None):
    """Gets status, notes, flag for a single question."""
    profile = load_user_profile(profile_name)
    return profile.get("questions", {}).get(qid, {
        "status": "unsolved",
        "notes": "",
        "flag": None,
        "errata": None
    })


def update_question_user_state(qid, status="unsolved", notes="", flag=None, errata=None, profile_name=None):
    """Updates status and notes for a question in user profile."""
    profile = load_user_profile(profile_name)
    if "questions" not in profile:
        profile["questions"] = {}
        
    profile["questions"][qid] = {
        "status": status,
        "notes": notes or "",
        "flag": flag,
        "errata": errata
    }
    save_user_profile(profile, profile_name)


def list_profiles():
    """Lists all existing local profiles."""
    files = [f[:-5] for f in os.listdir(PROFILES_DIR) if f.endswith(".json")]
    active = get_active_profile_name()
    return files or ["default"], active
