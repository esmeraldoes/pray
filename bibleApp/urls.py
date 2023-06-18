
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginView, LogoutView
from .views import RegisterView, FacebookLogin, GoogleLogin
from .views import ChurchCreateView, CommunityCreateView, TeamCreateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

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
    permission_classes=[AllowAny],
)

urlpatterns = [
    # ...
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='loginview'),
    path('api/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('api/google/', GoogleLogin.as_view(), name='google_login'),
    
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', obtain_auth_token, name='token'),

    path('api/churches/', ChurchCreateView.as_view(), name='church-create'),
    path('api/communities/', CommunityCreateView.as_view(), name='community-create'),
    path('api/teams/', TeamCreateView.as_view(), name='team-create'),
    # ...
    
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
    # ...
]

