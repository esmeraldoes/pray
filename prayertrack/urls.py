from django.urls import path
from .views import StartPrayerView, EndPrayerView, PrayerUpdatesView, PrayerDurationView, VoiceDurationView

urlpatterns = [
    path('start_prayer/', StartPrayerView.as_view(), name='start_prayer'),
    path('end_prayer/', EndPrayerView.as_view(), name='end_prayer'),
    path('prayer_updates/', PrayerUpdatesView.as_view(), name='prayer_updates'),
    path('prayer_duration/', PrayerDurationView.as_view(), name='prayer_duration'),
    path('voice_duration/', VoiceDurationView.as_view(), name='voice_duration'),
]


