# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urls

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bibleApp.urls')),
    path('accounts/', include('allauth.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include(urls)),
    #path('api/', include((router.urls, 'rest_framework'), namespace='rest_framework')),  # Add this line
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


