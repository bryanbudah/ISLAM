"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

# config/asgi.py (final working version)
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Django standard ASGI application
application = get_asgi_application()

# Vercel-specific requirement - MUST be named 'app'
app = application  # ← This line must be at MODULE LEVEL (no indentation)