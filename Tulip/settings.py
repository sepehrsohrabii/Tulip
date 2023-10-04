import os
from pathlib import Path

from Tulip.SECRETS import SECRET_KEY, POSTGRES_DB_PASS, DEBUG

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = SECRET_KEY
DEBUG = DEBUG

ALLOWED_HOSTS = ["tulipstone.ca", "localhost", "127.0.0.1", "147.182.146.162"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "frontend",
    "products",
    "emailMarketing",
    "gallery",
    "blog",
    "ckeditor",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "Tulip.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "Tulip.context_processors.global_parameters",
            ],
        },
    },
]

WSGI_APPLICATION = "Tulip.wsgi.application"
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "tulipstone",
            "USER": "tulipstoneuser",
            "PASSWORD": POSTGRES_DB_PASS,
            "HOST": "localhost",
            "PORT": "",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

if DEBUG:
    STATIC_URL = "static/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/static/media_root/"
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media_root")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if DEBUG:
    SECURE_SSL_REDIRECT = False
else:
    SECURE_SSL_REDIRECT = True

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
