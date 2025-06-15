"""
ASGI config for ZutrittskontrolleMobil25 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import ZutrittskontrolleMobil25.routing  # Importiere die WebSocket-Routing-Datei

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ZutrittskontrolleMobil25.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            ZutrittskontrolleMobil25.routing.websocket_urlpatterns
        )
    ),
})