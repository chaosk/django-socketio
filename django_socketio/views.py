import logging
from socketio import socketio_manage

from django.http import HttpResponse
from django_socketio.events import SOCKETIO_NS


def socketio(request):
    try:
        socketio_manage(request.environ, SOCKETIO_NS, request)
    except:
        logging.getLogger("socketio").error("Exception while handling socketio connection", exc_info=True)
    return HttpResponse("")

