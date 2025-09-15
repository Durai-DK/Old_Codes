import os
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!9ixrg*)tlv074ie18tbdzcuob&hqe%l^es=68zg8)q&sbjbb('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "myapp.User"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

Local_Apps = [
    "myapp",
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
]

INSTALLED_APPS += Local_Apps

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'User_Authentication.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'User_Authentication.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'new_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Email Configuration
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 465
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = True

EMAIL_HOST_USER = config("sender_email")
EMAIL_HOST_PASSWORD = config("sender_pw")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


SIMPLE_JWT = {
                "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
                "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
                "ROTATE_REFRESH_TOKENS": False,
                "BLACKLIST_AFTER_ROTATION": True,
                "AUTH_HEADER_TYPES": ("Bearer",),
            }

PASSWORD_RESET_TIMEOUT = 900  # 900 Sec = 15 Min
CORS_ALLOWED_ORIGINS = [

    "http://localhost:8080",
    "http://127.0.0.1:9000",
]


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {"format": "[{asctime}] {levelname} {name} {message}", "style": "{",},
        "simple": {"format": "{levelname} {message}", "style": "{",},},

    "handlers": {
        "file_users_app": {"level": "INFO",
                           "class": "logging.handlers.RotatingFileHandler",
                           "filename": os.path.join(BASE_DIR, "logs/users_app.log"),
                           "maxBytes": 5 * 1024 * 1024,  # 5 MB
                           "backupCount": 5,
                           "formatter": "verbose",},

        "console": {"class": "logging.StreamHandler", "formatter": "simple",},
    },

    "loggers": {
                "Users": {"handlers": ["file_users_app", "console"], "level": "INFO", "propagate": False,},
            },
        }

