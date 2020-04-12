# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
            url(r'^$', views.index),
            url(r'^data$', views.data),
            url(r'^feedback', views.user)
            ]
