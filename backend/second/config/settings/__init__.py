# -*- coding: utf-8 -*-
import os
if os.environ['DJANGO_SETTINGS_MODULE'] == 'config.settings.local':
    from config.settings.local import *
elif os.environ['DJANGO_SETTINGS_MODULE'] == 'config.settings.test':
    from config.settings.test import *
elif os.environ['DJANGO_SETTINGS_MODULE'] == 'config.settings.staging':
    from config.settings.staging import *
elif os.environ['DJANGO_SETTINGS_MODULE'] == 'config.settings.production':
    from config.settings.production import *
