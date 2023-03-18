'''from __future__ import absolute_import, unicode_literals
import os
import celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'resume.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
app = celery.Celery('resume')
app.config_from_object('django.conf:settings' , namespace='CELERY')
app.autodiscover_tasks()'''