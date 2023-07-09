from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

# Create a custom schema generator
class CustomSchemaGenerator(openapi.SchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.validate = False  # Disable schema validation
        return schema

# Create a schema view for Swagger documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Regimen Endpoints",
        default_version='v1',
        description="API documentation for Regimen",
        terms_of_service="",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    generator_class=CustomSchemaGenerator, 
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('', lambda request: redirect('swagger-ui'), name='root'),  # Redirect root URL to Swagger documentation
    path('admin/', admin.site.urls),
    path('', include('bibleApp.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]

# Add static files serving for development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
