# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from httplib import OK
from django.http import HttpResponse

def list(request):
    return HttpResponse({'back server': 'ok'}, status=OK)

