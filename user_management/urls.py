# # urls.py

# from django.urls import path
# from .views import social_login, save_user_details
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.views import OAuth2CallbackView  # Add this import

# urlpatterns = [
#     path('social/login/', social_login, name='social_login'),
#     path('user/details/', save_user_details, name='save_user_details'),
#     path('social/callback/facebook/', OAuth2CallbackView.adapter_view(adapter=FacebookOAuth2Adapter),
#          name='facebook_callback'),
#     path('social/callback/google/', OAuth2CallbackView.adapter_view(adapter=GoogleOAuth2Adapter),
#          name='google_callback'),
# ]
