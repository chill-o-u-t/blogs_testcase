from __future__ import absolute_import
import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testcase.settings")
app = Celery("testcase")
app.config_from_object("django.conf:settings")
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-five-posts-every-day': {
        'task': 'blogs.tasks.send_last_posts',
        'schedule': crontab(minute=0, hour='*/24')
    }
}
