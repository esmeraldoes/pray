# authentication/serializers.py

from django.contrib.auth import get_user_model
from rest_framework import serializers


from .models import Church, Community, Team

User = get_user_model()


# serializers.py

from rest_auth.serializers import LoginSerializer

class CustomLoginSerializer(LoginSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)

        # Add custom validation or modifications if needed

        return attrs


class UserSerializer(serializers.ModelSerializer):
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

class CustomLogoutSerializer(serializers.Serializer):
    pass



class ChurchSerializer(serializers.ModelSerializer):
    # Other fields of the serializer

    class Meta:
        model = Church
        fields = ['name', 'email']
        #exclude = []  # Remove 'user' from the exclude option
        extra_kwargs = {
            'user': {'read_only': True}
        }

    def create(self, validated_data):
        if not self.context['request'].user.is_authenticated:
            raise serializers.ValidationError('User must be authenticated.')

        user = self.context['request'].user
        if not isinstance(user, User):
            raise serializers.ValidationError('User must be an instance of CustomUser.')

        validated_data['user'] = user
        church = Church.objects.create(**validated_data)
        return church


class PrayerResponseSerializer(serializers.Serializer):
    message = serializers.CharField()




# class ChurchSerializer(serializers.ModelSerializer):
#     # user = serializers.ReadOnlyField(source='user.username')
#     class Meta:
#         model = Church
#         fields = '__all__'
#         # exclude = ['user']
#         # fields = ['name', 'email']

#     def create(self, validated_data):
#         # Retrieve the authenticated user from the request
#         user = self.context['request'].user

#         # Create the church object without the 'user' field
#         church = Church.objects.create(**validated_data)

#         # Assign the user to the 'user' field of the church object
#         church.user = user
#         church.save()

#         return church

#     # def create(self, validated_data):
#     #     validated_data['user'] = self.context['request'].user
#     #     return super().create(validated_data)


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ['name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name']