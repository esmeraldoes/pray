from rest_framework import serializers

class StartPrayerResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

class PrayerUpdateResponseSerializer(serializers.Serializer):
    prayer_duration = serializers.CharField()
    voice_duration = serializers.CharField()
    voice_detected = serializers.BooleanField()

class EndPrayerResponseSerializer(serializers.Serializer):
    message = serializers.CharField()

class PrayerDurationResponseSerializer(serializers.Serializer):
    duration = serializers.CharField()

class VoiceDurationResponseSerializer(serializers.Serializer):
    duration = serializers.CharField()

