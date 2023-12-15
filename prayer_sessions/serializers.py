from rest_framework import serializers
from .models import PrayerRecord, DailyDevotion, UserPrayerSession

class PrayerRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRecord
        fields = '__all__'

class PrayerSessionSerializer(serializers.ModelSerializer):
    records = PrayerRecordSerializer(many=True, read_only=True)

    class Meta:
        model = UserPrayerSession
        fields = '__all__'


class DailyDevotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyDevotion
        fields = ['id', 'start_date', 'end_date', 'description', 'created_by','assigned_user']


class UserPrayerSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPrayerSession
        fields = ['id', 'daily_devotion', 'user', 'start_time', 'end_time', 'voice_detected']


