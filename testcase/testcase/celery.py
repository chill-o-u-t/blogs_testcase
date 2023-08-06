import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_case.settings")
app = Celery("test_case")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

