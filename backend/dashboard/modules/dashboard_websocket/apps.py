from __future__ import unicode_literals
import logging
from django.apps import AppConfig
logger = logging.getLogger("subscriber")


class DashboardWebsocketConfig(AppConfig):
    name = 'modules.dashboard_websocket'

    def ready(self):
        pass
