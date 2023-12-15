"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# application = get_asgi_application()
#################################################################################################################
#################################################################################################################
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

from prayer_sessions.consumers import PrayerTrackerConsumer  # Replace YOUR_APP with your actual app name

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        [
            # path("ws/prayer_tracker/", PrayerTrackerConsumer.as_asgi()),
            path("ws/prayer_tracker/<int:user_id>/", PrayerTrackerConsumer.as_asgi()),  # Adjust the path as needed
        
        ]
    ),
})



####################################################################################################################
####################################################################################################################



# # your_project/asgi.py

# import os
# from django.core.asgi import get_asgi_application
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')

# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     "websocket": AuthMiddlewareStack(
#         URLRouter(
#             your_project.routing.websocket_urlpatterns
#         )
#     ),
# })
