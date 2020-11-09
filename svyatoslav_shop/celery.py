import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'svyatoslav_shop.settings')

app = Celery('svyatoslav_shop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()