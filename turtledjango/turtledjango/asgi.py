import django, os

from django.core.asgi import get_asgi_application

from websocket.middleware import websockets


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "turtledjango.settings")
django.setup()
application = get_asgi_application()
application = websockets(application)


