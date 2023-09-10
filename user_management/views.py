# # views.py

# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser
# from django.shortcuts import redirect
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from allauth.socialaccount.providers.oauth2.client import OAuth2Error
# from allauth.socialaccount.providers.oauth2.views import OAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from .serializers import SocialLoginSerializer

# @api_view(['POST'])
# def social_login(request):
#     serializer = SocialLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     provider = serializer.validated_data['provider']
#     access_token = serializer.validated_data['access_token']
#     user = request.user if request.user.is_authenticated else AnonymousUser()

#     # Configure the appropriate social adapter based on the provider
#     if provider == 'facebook':
#         adapter = FacebookOAuth2Adapter
#     elif provider == 'google':
#         adapter = GoogleOAuth2Adapter
#     else:
#         return Response({'error': 'Invalid provider'}, status=400)

#     # Obtain the social login token
#     try:
#         token = OAuth2Adapter.access_token_url(request)
#         token = OAuth2Adapter.refresh_token(token)
#         token = OAuth2Adapter.parse_token(token)
#     except OAuth2Error as e:
#         return Response({'error': str(e)}, status=400)

#     # Authenticate the user using the social token
#     user = adapter().complete_login(request, app=OAuth2Client(request), access_token=token)

#     if user:
#         return Response({'detail': 'Social login successful.'})
#     else:
#         return Response({'error': 'Social login failed.'}, status=400)
    









# # views.py

# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import AnonymousUser
# from django.shortcuts import redirect
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from allauth.socialaccount.providers.oauth2.client import OAuth2Error
# from allauth.socialaccount.providers.oauth2.views import (
#     OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView
# )
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from .serializers import SocialLoginSerializer, UserDetailsSerializer

# @api_view(['POST'])
# @permission_classes([AllowAny])  # Allow non-authenticated users to access this view
# def social_login(request):
#     serializer = SocialLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     provider = serializer.validated_data['provider']
#     access_token = serializer.validated_data['access_token']
#     user = request.user if request.user.is_authenticated else AnonymousUser()

#     # Configure the appropriate social adapter based on the provider
#     if provider == 'facebook':
#         adapter = FacebookOAuth2Adapter
#     elif provider == 'google':
#         adapter = GoogleOAuth2Adapter
#     else:
#         return Response({'error': 'Invalid provider'}, status=400)

#     # Redirect to the social media provider's authorization page for authentication
#     view = OAuth2LoginView.adapter_view(adapter)
#     return view(request)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])  # Allow only authenticated users to access this view
# def save_user_details(request):
#     serializer = UserDetailsSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)

#     # Save user details to the database
#     user = request.user
#     user.first_name = serializer.validated_data['first_name']
#     user.last_name = serializer.validated_data['last_name']
#     user.email = serializer.validated_data['email']
#     # Add any other user details you want to save to the database
#     user.save()

#     return Response({'detail': 'User details saved successfully.'})

    



# # views.py

# from allauth.socialaccount.providers.oauth2.client import OAuth2Error
# from allauth.socialaccount.providers.oauth2.views import (
#     OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView
# )
# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
# from django.shortcuts import redirect
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def initiate_social_login(request, provider):
#     if provider == 'facebook':
#         adapter = FacebookOAuth2Adapter
#     elif provider == 'google':
#         adapter = GoogleOAuth2Adapter
#     else:
#         return Response({'error': 'Invalid provider'}, status=400)

#     # Redirect to the social media provider's authorization page for authentication
#     view = OAuth2LoginView.adapter_view(adapter)
#     return view(request)

# # OAuth2CallbackView is used to handle the callback after social media authentication
# callback_view = OAuth2CallbackView.adapter_view(FacebookOAuth2Adapter)





