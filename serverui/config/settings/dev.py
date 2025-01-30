from .base import *  # Import common settings

# Enable debug mode in development
DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Use SQLite for local development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
