from __future__ import absolute_import

import os

from celery import Celery
from real_estate.settings import base

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "real_estate.settings.dev")

app = Celery("real_estate")

app.config_from_object("real_estate.settings.dev", namespace="CELERY"),

app.autodiscover_tasks(lambda: base.INSTALLED_APPS)