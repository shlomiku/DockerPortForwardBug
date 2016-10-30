# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""
from __future__ import absolute_import
from datetime import timedelta

from config.settings.common import *
import environ

env = environ.Env()
SECRET_KEY = env('DJANGO_SECRET_KEY', default='-aswqd5zwc^bnzo6!gga4#k044!s7rcdi9kjhg=54@q)3e4r*^')

DEBUG = True