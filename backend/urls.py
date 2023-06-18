# project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, urls


router = routers.DefaultRouter()

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('bibleApp.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-auth/', include(urls)),
    #path('api/', include((router.urls, 'rest_framework'), namespace='rest_framework')),  # Add this line
]


