from .base import *  # Import common settings

# Disable debug mode in production
DEBUG = False

# Define allowed hosts
ALLOWED_HOSTS = []

# Use PostgreSQL or another production-ready database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db",
        "USER": "your_user",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

# Use WhiteNoise for serving static files in production
INSTALLED_APPS += ["whitenoise.runserver_nostatic"]
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Enable secure cookies and headers
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
