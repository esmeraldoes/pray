
from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.response import Response

from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import UserSerializerz

from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated

# from .serializers import CustomLoginSerializer
from rest_framework.authentication import TokenAuthentication






class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializerz
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)






class CustomLogoutSerializer(serializers.Serializer):
    def logout(self):
        request = self.context.get('request')
        if request.auth:
            Token.objects.filter(key=request.auth.key).delete()


class LogoutView(ObtainAuthToken):
    serializer_class = CustomLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.logout()
        return Response(status=status.HTTP_200_OK)
    






# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from allauth.account.models import EmailAddress  # Import EmailAddress model

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_user_info(request):
   
#     user = request.user
  
#     try:
#         email_address = EmailAddress.objects.get(user=user, primary=True)
#         user_info = {
#             'username': user.username,
#             'email': email_address.email,
#             'first_name': user.first_name,
#             'last_name': user.last_name,
           
#         }
#         return Response(user_info, status=status.HTTP_200_OK)
#     except EmailAddress.DoesNotExist:
#         return Response({'error': 'Email address not found.'}, status=status.HTTP_404_NOT_FOUND)





#############hereererere

from rest_framework import generics, permissions
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsOwnerOrReadOnly

class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.contrib.auth import login, logout
from allauth.account.models import EmailConfirmation
from .models import CustomUser
from .serializers import CustomUserSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.models import SocialAccount
from allauth.account.models import EmailAddress

class CustomLogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # Log the user out
        request.auth.delete()
        
        # If using Social Accounts, remove the associated social account
        try:
            social_account = SocialAccount.objects.get(user=request.user)
            social_account.delete()
        except SocialAccount.DoesNotExist:
            pass
        
        # If using Allauth, clear the session and auth token
        request.session.flush()
        
        return Response({'message': 'User logged out successfully.'})
