from django.urls import path
from .views import RegisterView, LoginView, LogoutView
from .views import ChurchCreateView, CommunityCreateView, TeamCreateView
from .views import StartPrayerView, EndPrayerView, PrayerUpdatesView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='loginview'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('churches/', ChurchCreateView.as_view(), name='church-create'),
    path('communities/', CommunityCreateView.as_view(), name='community-create'),
    path('teams/', TeamCreateView.as_view(), name='team-create'),
    path('start-prayer/', StartPrayerView.as_view(), name='start-prayer'),
    path('end-prayer/', EndPrayerView.as_view(), name='end-prayer'),
    path('prayer-updates/', PrayerUpdatesView.as_view(), name='prayer-updates'),
]
















# from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
# from .views import RegisterView, LoginView, LogoutView
# from .views import RegisterView, FacebookLogin, GoogleLogin
# from .views import ChurchCreateView, CommunityCreateView, TeamCreateView
# from .views import StartPrayerView, EndPrayerView, PrayerUpdatesView
# from rest_framework import routers, urls

# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework.permissions import AllowAny
# # from django_grpc_framework import services
# from bibleApp import prayer_tracker_service
# from prayer_tracker_server import serve


# schema_view = get_schema_view(
#     openapi.Info(
#         title="Regimen Endpoints",
#         default_version='v1',
#         description="API documentation for Regimen",
#         terms_of_service="",
#         contact=openapi.Contact(email="contact@example.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[AllowAny],
# )

# urlpatterns = [
#     path('accounts/', include('allauth.urls')),
#     path('rest-auth/', include('rest_auth.urls')),
#     path('rest-auth/registration/', include('rest_auth.registration.urls')),
#     path('api-auth/', include(urls)),
#     # ...
#     path('api/register/', RegisterView.as_view(), name='register'),
#     path('api/login/', LoginView.as_view(), name='loginview'),
#     path('api/facebook/', FacebookLogin.as_view(), name='facebook_login'),
#     path('api/google/', GoogleLogin.as_view(), name='google_login'),
    
#     path('api/logout/', LogoutView.as_view(), name='logout'),
#     path('api/token/', obtain_auth_token, name='token'),

#     path('api/churches/', ChurchCreateView.as_view(), name='church-create'),
#     path('api/communities/', CommunityCreateView.as_view(), name='community-create'),
#     path('api/teams/', TeamCreateView.as_view(), name='team-create'),
#     # ...
    
#     path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
#     path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
#     # gRPC
    
#     # path('grpc/', services.server.prune_request_stream(prayer_tracker_service.PrayerTrackerService)),

#     # path('grpc', services.server.prune_request_stream(prayer_tracker_service.PrayerTrackerService)),
#     path('start-prayer/', StartPrayerView.as_view(), name='start-prayer'),
#     path('end-prayer/', EndPrayerView.as_view(), name='end-prayer'),
#     path('prayer-updates/', PrayerUpdatesView.as_view(), name='prayer-updates'),

#     path('grpc/prayer_tracker', prayer_tracker_service.serve),

# ]

