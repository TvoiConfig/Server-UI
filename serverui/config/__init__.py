import os

# Load environment-specific settings
ENV = os.getenv("DJANGO_ENV", "dev")  # Default to "dev" if not set

if ENV == "prod":
    from .settings.prod import *
else:
    from .settings.dev import *