

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


from rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)

        return attrs


from rest_framework import serializers
from allauth.account.models import EmailAddress 

class UserInfoSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
   

    def to_representation(self, instance):
        user = self.context['request'].user
        try:
            email_address = EmailAddress.objects.get(user=user, primary=True)
            user_info = {
                'username': user.username,
                'email': email_address.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            return user_info
        except EmailAddress.DoesNotExist:
            return {}

from rest_framework import serializers
from .models import CustomUser, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('gender', 'date_of_birth', 'profile_picture')
##############################################################################################
################################################################################################
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'age', 'profile_data')  

    profile_data = serializers.SerializerMethodField()

    def get_profile_data(self, obj: CustomUser) -> dict:
        try:
            profile = obj.userprofile
            return UserProfileSerializer(profile).data
        except UserProfile.DoesNotExist:
            return None 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


from rest_framework import serializers
from allauth.socialaccount.models import SocialAccount

class SocialAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialAccount
        fields = ('user', 'provider', 'uid', 'extra_data', 'last_login')




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

