"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_asgi_application()

ws_pattern = [
    path("ws/chat/<str:room_name>/", ChatConsumer.as_asgi()),
]
application = ProtocolTypeRouter(
    {
        # "http": application,
        "websocket": URLRouter(ws_pattern)
    }
)
