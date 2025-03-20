import os
import environ
from pathlib import Path

from django.contrib.messages import constants as messages

from core.log_formatter import GCPJsonFormatter

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "django-insecure"),
    ENVIRONMENT=(str, "development"),
)
env_locations = [".env", "/tmp/.env", "/tmp/env", "/tmp/specific-env"]
for e in env_locations:
    if os.path.isfile(e):
        env.read_env(e)

ENVIRONMENT = env("ENVIRONMENT")
DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY")


if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = [
        "stratus.incubeta.com",
    ]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "gcp_json": {
            "()": GCPJsonFormatter,
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "gcp_json",
        },
    },
    "root": {"level": "INFO", "handlers": ["console"]},
}

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "django_htmx",
    "app",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "core.middleware.custom_social_auth_exception_middleware.CustomSocialAuthExceptionMiddleware",
    "social_django.middleware.SocialAuthExceptionMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["app/templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

if ENVIRONMENT in ("production",):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USERNAME"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST"),
            "PORT": os.getenv("DB_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "app/static"]
STATIC_ROOT = os.path.join(BASE_DIR, "core", "static")
MEDIA_ROOT = os.path.join(BASE_DIR, "core", "media")
MEDIA_URL = "media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}
# Overwrite default to use Google Cloud Storage
if os.environ.get("USE_GCS") == "yes":
    STORAGES["default"] = {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": os.environ.get(
                "GCS_BUCKET", "glo-tech-incubeta-technology-foodportal"
            ),
            "project_id": os.environ.get("PROJECT_ID", "glo-tech-incubeta-technology"),
            "default_acl": "publicRead",
        },
    }
    STORAGES["staticfiles"] = {
        "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
        "OPTIONS": {
            "bucket_name": os.environ.get(
                "GCS_BUCKET", os.environ.get("PROJECT_ID", "") + "-assets"
            ),
            "project_id": os.environ.get("PROJECT_ID", ""),
            "default_acl": "publicRead",
        },
    }

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MESSAGE_TAGS = {
    messages.DEBUG: "alert-secondary",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}

# SOCIAL AUTH
AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

###################################
# OAuth2 Configurations
###################################
SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.social_user",
    "social_core.pipeline.user.get_username",
    "social_core.pipeline.social_auth.associate_by_email",
    "social_core.pipeline.user.create_user",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "core.middleware.pipeline.update_user_social_data",
)

SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("GOOGLE_OAUTH2_SECRET")
if os.getenv("GOOGLE_OAUTH2_WHITELISTED_DOMAINS"):
    SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = os.getenv(
        "GOOGLE_OAUTH2_WHITELISTED_DOMAINS", ""
    ).split(",")
# LOGIN_URL = '/auth/login/google-oauth2/'
LOGIN_URL = "/403/"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/"

# FiveTran Settings
# API Key
FIVETRAN_API_KEY_ENCODED = os.getenv("FIVETRAN_API_KEY_ENCODED")
# Webhook Secret
FIVETRAN_WEBHOOK_SIGNATURE_SECRET = os.getenv("FIVETRAN_WEBHOOK_SIGNATURE_SECRET")

# Google Cloud Principal Emails
# IAM Service Account - Workload Identity
LOADED_IDENTITY = os.environ.get("LOADED_IDENTITY")
IMPERSONATE_IDENTITY = os.environ.get("IMPERSONATE_IDENTITY")
BILLING_ACCOUNT_ID = os.environ.get("BILLING_ACCOUNT_ID")
CUSTOMER_ID = "customers/C01hkuh1j"
ORGANIZATION_ID = os.environ.get("ORGANIZATION_ID")

# Monday.com settings
MONDAY_BOARD_ID = os.getenv("MONDAY_BOARD_ID")
MONDAY_TOKEN = os.getenv("MONDAY_TOKEN")

# SELECT setval(pg_get_serial_sequence('"django_admin_log"','id'), coalesce(max("id"), 1), max("id") IS NOT null) FROM "django_admin_log";
# COMMIT;

# Stratus Admins
STRATUS_SUPERADMIN_USERS = os.getenv("STRATUS_SUPERADMIN_USERS", "").split(",")
STRATUS_ADMIN_USERS = os.getenv("STRATUS_ADMIN_USERS", "").split(",")

GIT_TOKEN = os.environ.get("GIT_TOKEN")