from django.urls import path
from .views import RegisterView, LogoutView
from .views import UserProfileView, UserProfileDetail
from rest_framework.authtoken.views import obtain_auth_token
from .views import  CustomLogoutView
from djoser.views import TokenCreateView


urlpatterns = [
    path('register1/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='token'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/token/login/', TokenCreateView.as_view(), name='user-login'),

    path('profile/', UserProfileView.as_view(), name='user-profile'),
    
    path('usermanagement/logout/', CustomLogoutView.as_view(), name='custom_logout'),
   
    
]
