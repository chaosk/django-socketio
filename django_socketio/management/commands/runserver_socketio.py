
from re import match
from os import environ
from optparse import make_option

from socketio.server import SocketIOServer

from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler
from django.core.management.base import BaseCommand, CommandError
from django.core.management.commands.runserver import naiveip_re
from django.utils import autoreload
from django_socketio.settings import HOST, PORT

class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--noreload', action='store_false', dest='use_reloader', default=True,
            help='Tells the server to NOT use the auto-reloader.'),
    )
    help = "Starts a lightweight websocket server for development."
    args = '[optional port number, or ipaddr:port]'

    def handle(self, addrport="", *args, **options):

        if not addrport:
            self.addr = HOST
            self.port = PORT
        else:
            m = match(naiveip_re, addrport)
            if m is None:
                raise CommandError('"%s" is not a valid port number '
                                   'or address:port pair.' % addrport)
            self.addr, _, _, _, self.port = m.groups()

        # Make the port available here for the path:
        #   socketio_tags.socketio ->
        #   socketio_scripts.html ->
        #   io.Socket JS constructor
        # allowing the port to be set as the client-side default there.
        environ["DJANGO_SOCKETIO_PORT"] = str(self.port)

        if options.get('use_reloader', True):
            autoreload.main(self.inner_run, args, options)
        else:
            self.inner_run(*args, **options)


    def inner_run(self, *args, **options):
        bind = (self.addr, int(self.port))
        print()
        print("SocketIOServer running on %s:%s" % bind)
        print()
        handler = self.get_handler(*args, **options)
        server = SocketIOServer(bind, handler, resource="socket.io")
        server.serve_forever()

    def get_handler(self, *args, **options):
        """
        Returns the django.contrib.staticfiles handler.
        """
        handler = WSGIHandler()
        try:
            from django.contrib.staticfiles.handlers import StaticFilesHandler
        except ImportError:
            return handler
        use_static_handler = options.get('use_static_handler', True)
        insecure_serving = options.get('insecure_serving', False)
        if (settings.DEBUG and use_static_handler or
                (use_static_handler and insecure_serving)):
            handler = StaticFilesHandler(handler)
        return handler
