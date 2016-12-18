# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from modules.routes import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.list,
        name='list'
    ),
    url(
        regex=r'^add/$',
        view=views.add,
        name='add'
    ),
    url(
        regex=r'^edit/$',
        view=views.edit,
        name='edit'
    ),
    url(
        regex=r'^get/(?P<item_id>\d+)$',
        view=views.get,
        name='get'
    ),
    url(
        regex=r'^delete/(?P<item_id>\d+)$',
        view=views.delete,
        name='delete'
    )
]
