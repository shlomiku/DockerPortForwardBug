# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),

    # Your stuff: custom urls includes go here
    url(r'^first/', include('apps.myapp.urls', namespace='first', app_name="first"), name="first"),


]