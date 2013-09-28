from django.utils.importlib import import_module
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

    import imp
    from django.conf import settings

    for app in settings.INSTALLED_APPS:

        try:
            app_path = import_module(app).__path__
        except AttributeError:
            continue

        try:
            imp.find_module('events', app_path)
        except ImportError:
            continue

        import_module("%s.events" % app)

    LOADING_SOCKETIO = False


class Namespace(object):
    def __init__(self, name=''):
        self.name = name

    def __call__(self, handler):
        SOCKETIO_NS[self.name] = handler
        return handler

