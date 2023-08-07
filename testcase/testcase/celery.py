import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testcase.settings")
app = Celery("test_case")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-five-posts-every-day': {
        'task': 'blogs.tasks.send_last_posts',
        'schedule': crontab(minute=0, hour='*/24')
    }
}
