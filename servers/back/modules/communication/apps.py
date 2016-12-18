from __future__ import unicode_literals

from django.apps import AppConfig
import redis
redis_cache = redis.Redis(host='redis', port=6379, db=0)
import logging
logger = logging.getLogger('.'.join(__file__.split('/')[-2:]).rstrip('.py'))


class WebsocketConfig(AppConfig):
    '''
    application entry point. registering all handlers will be done in the method ready()
    '''
    name = 'modules.communication'
    def ready(self):
        pass

