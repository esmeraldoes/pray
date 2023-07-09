from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from drf_yasg import openapi
from drf_spectacular.generators import SchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    # path('', lambda request: redirect('swagger-ui'), name='root'),  # Redirect root URL to Swagger documentation
    path('admin/', admin.site.urls),
    path('', include('bibleApp.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/', include('bibleApp.urls')),

]

# Add static files serving for development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
