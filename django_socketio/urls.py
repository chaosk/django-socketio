from django.conf.urls import patterns, url
from django_socketio.events import autodiscover_socketios


autodiscover_socketios()

urlpatterns = patterns("django_socketio.views",
    url("^socket\.io", "socketio", name="socketio"),
)
