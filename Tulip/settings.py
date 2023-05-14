import os
from pathlib import Path

from Tulip.SECRETS import SECRET_KEY, DB_NAME, DB_PASSWORD, DB_USER

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = False

# mimetypes.add_type('text/css', '.css', True)
# mimetypes.add_type('text/html', '.html', True)
# mimetypes.add_type('text/javascript', '.js', True)

if DEBUG:
    SECRET_KEY = 'sepisepisepisepisepisepisepisepisep'
else:
    SECRET_KEY = SECRET_KEY

ALLOWED_HOSTS = ['tulipstone.ca', 'localhost', '127.0.0.1', '138.197.128.128']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frontend',
    'products',
    'emailMarketing',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Tulip.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Tulip.context_processors.global_parameters'
            ],
        },
    },
]

WSGI_APPLICATION = 'Tulip.wsgi.application'
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DB_NAME,
            'USER': DB_USER,
            'PASSWORD': DB_PASSWORD,
            'HOST': 'localhost',
            'PORT': '',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

if DEBUG:
    STATIC_URL = 'static/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media_root/')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# if DEBUG:
#     SECURE_SSL_REDIRECT = False
# else:
#     SECURE_SSL_REDIRECT = False
#
# if not DEBUG:
#     SESSION_COOKIE_SECURE = True
#     CSRF_COOKIE_SECURE = True
