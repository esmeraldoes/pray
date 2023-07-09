# project/urls.py

from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bibleApp.urls')),
    # path('accounts/', include('allauth.urls')),
    
    #path('api/', include((router.urls, 'rest_framework'), namespace='rest_framework')),  # Add this line
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


