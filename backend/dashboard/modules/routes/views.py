# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from httplib import OK
from django.http import HttpResponse

def list(request):
    return HttpResponse({'status': 'ok'}, status=OK)


def add(request):
    return HttpResponse({'status': 'ok'}, status=OK)


def edit(request):
    return HttpResponse({'status': 'ok'}, status=OK)


def get(request, item_id):
    return HttpResponse({'status': 'ok'}, status=OK)


def delete(request, item_id):
    return HttpResponse({'status': 'ok'}, status=OK)
