"""
Django settings for config project.
Works both locally (SQLite) and on Render (PostgreSQL).
"""

import os
import dj_database_url  # pip install dj-database-url
from pathlib import Path

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-prod")

# Debug
DEBUG = os.environ.get("DEBUG", "True") == "True"

# Allowed hosts
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'myislamicsite.com',
    'www.myislamicsite.com',
    'yourproject.vercel.app',
    '.vercel.app',
    '.now.sh'
]

# Installed apps
INSTALLED_APPS = [
    # Django core
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'tailwind',
    'django_extensions',

    # Local apps
    'theme',
    'users',
    'content',
    'core.apps.CoreConfig',
]

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Authentication settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Serve static files in prod
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URLs
ROOT_URLCONF = 'config.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Global templates    
                'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # Required for auth
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI / ASGI
WSGI_APPLICATION = 'config.wsgi.application'
ASGI_APPLICATION = 'config.asgi.application'

# Database — use PostgreSQL on Render, SQLite locally
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static & media
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Dev static files
STATIC_ROOT = BASE_DIR / 'staticfiles'    # Where collectstatic stores files

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Whitenoise static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
