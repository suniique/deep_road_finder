# chat/routing.py
from django.conf.urls import url

from . import views

websocket_urlpatterns = [
    url(r'^websocket/record/(?P<trial_id>[^/]+)/$', views.RecoderSender),
]
