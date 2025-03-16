from django.urls import re_path
from core.consumers import CheckinCheckoutConsumer

websocket_urlpatterns = [
    re_path(r'ws/checkin_checkout/$', CheckinCheckoutConsumer.as_asgi()),
]