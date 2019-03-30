from __future__ import absolute_import

from django.conf import settings  # noqa

from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangolearn.settings.local')
app = Celery('djangolearn')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
