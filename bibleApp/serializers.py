

from django.contrib.auth import get_user_model
from rest_framework import serializers

from rest_framework import serializers
from allauth.account.models import EmailAddress 

from rest_framework import serializers
from .models import CustomUser, UserProfile

User = get_user_model()

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

class UserSerializerz(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
#######DINERO
from rest_framework import serializers
# from django.contrib.auth.models import User




from djoser.serializers import UserCreateSerializer
from .models import CustomUser

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser  # Use your custom user model
        fields = ('email', 'username', 'password', 'first_name', 'last_name')

    def perform_create(self, validated_data):
        user = super().perform_create(validated_data)
        user.first_name = validated_data.get('first_name', '')
        user.last_name = validated_data.get('last_name', '')
        user.save()
        return user
    
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
