# serializers.py

from rest_framework import serializers

class SocialLoginSerializer(serializers.Serializer):
    provider = serializers.CharField()
    access_token = serializers.CharField()

class UserDetailsSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    # Add any other user details you want to save to the database
