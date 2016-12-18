
from __future__ import absolute_import
from celery import Celery
from django.apps import AppConfig


app = Celery('modules')


class CeleryConfig(AppConfig):
    name = 'modules.dashboard_websocket'
    verbose_name = 'Celery Config'

    def ready(self):
        pass
