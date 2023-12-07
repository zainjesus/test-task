from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/post/(?P<post_id>\d+)/$', consumers.PostNotificationConsumer.as_asgi()),
]