
from __future__ import absolute_import

import os
from celery import Celery
from DjangoBooks import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wh1803JSFDjangoBook.settings')

app = Celery('wh1803JSFDjangoBook', backend='redis', broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


