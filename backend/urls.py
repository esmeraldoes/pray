from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from drf_spectacular.generators import SchemaGenerator
from rest_framework.permissions import AllowAny
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/', include('djoser.urls')),
    path('api/', include('djoser.urls.jwt')),
    # path('rest-auth/', include('rest_auth.urls')),
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('usermanagement/', include('bibleApp.urls')),
    path('bible/', include('mygrpcapp.urls')),
    path('prayertracker/', include('prayertrack.urls')),
    path('communityapps/', include('communityapp.urls')),
    path('prayersessions/', include('prayer_sessions.urls')),
    #  path('prayersessions/', include('prayer_sessions.routing')),

]


# Add static files serving for development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
