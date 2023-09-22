from django.urls import path
from .views import RegisterView, LoginView, LogoutView
from .views import FacebookLogin, GoogleLogin, SocialAccountView, get_user_info, UserProfileView, UserRegistrationView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register1/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='token'),
    path('facebook/', FacebookLogin, name='facebook_login'),
    path('google/', GoogleLogin, name='google_login'),
    path('login/', LoginView.as_view(), name='loginview'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('social_login/', SocialAccountView.as_view(),name='social_account'),
    path('user-info/', get_user_info, name='user-info'),
   
    path('register2/', UserRegistrationView.as_view(), name='user-registration'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    
]
