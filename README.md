# Tickets (Django + Celery + Redis)

Sample repository 4 of the Orkosi bring-your-code test matrix. Three components: the Django web process (gunicorn,
health at `/health/`), the Celery worker, and a Redis cache the worker and the web process share; Django migrations in
`tickets/migrations` (history table `django_migrations`), release command `python manage.py migrate --noinput`.
