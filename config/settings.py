"""Sample 4 — Django settings. The platform must find: backend (gunicorn), worker (celery), cache (redis),
release `python manage.py migrate`, DATABASE_URL and REDIS_URL as references, DJANGO_SECRET_KEY required."""
import os

import dj_database_url

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
DEBUG = os.getenv("DJANGO_DEBUG", "0") == "1"
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["django.contrib.contenttypes", "django.contrib.auth", "tickets"]
ROOT_URLCONF = "config.urls"
DATABASES = {"default": dj_database_url.parse(os.environ["DATABASE_URL"])}
CELERY_BROKER_URL = os.environ.get("REDIS_URL", "redis://localhost:6379/0")
CACHES = {"default": {"BACKEND": "django.core.cache.backends.redis.RedisCache", "LOCATION": CELERY_BROKER_URL}}
