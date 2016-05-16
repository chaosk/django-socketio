from django.utils.module_loading import autodiscover_modules
from socketio.mixins import BroadcastMixin
from socketio.namespace import BaseNamespace


__all__ = ['autodiscover_socketios', 'BaseNamespace', 'Namespace',
           'BroadcastMixin']
SOCKETIO_NS = {}


LOADING_SOCKETIO = False


def autodiscover_socketios():
    """
    Auto-discover INSTALLED_APPS sockets.py modules and fail silently when
    not present. NOTE: socketio_autodiscover was inspired/copied from
    django.contrib.admin autodiscover
    """
    global LOADING_SOCKETIO
    if LOADING_SOCKETIO:
        return
    LOADING_SOCKETIO = True

    autodiscover_modules('events')
    LOADING_SOCKETIO = False


class Namespace(object):
    def __init__(self, name=''):
        self.name = name

    def __call__(self, handler):
        SOCKETIO_NS[self.name] = handler
        return handler

