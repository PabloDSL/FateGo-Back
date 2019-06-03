from django.conf.urls import url
from rest_framework import routers
from Servants.views import *

urlpatterns = [
    url(r'^servant/$', ServantList.as_view(),name='ServantList'),
    url(r'^servant/(?P<pk>\d+)/?$', ServantList.as_view())
]