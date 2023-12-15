from django.urls import path
from .views import PrayerSessionView, CreateDailyDevotionView, CreatePrayerSessionView, DailyDevotionViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('sessions/', PrayerSessionView.as_view(), name='prayer-session-list'),
    # path('start/', StartPrayerSessionView.as_view(), name='start_prayer_session'),
    # path('end/', EndPrayerSessionView.as_view(), name='end_prayer_session'),
    path('daily_devotions/create/', CreateDailyDevotionView.as_view(), name='create_daily_devotion'),
    path('prayer_sessions/create/', CreatePrayerSessionView.as_view(), name='create_prayer_session'),


]

router = DefaultRouter()
router.register(r'daily_devotions', DailyDevotionViewSet, basename='daily_devotions')
urlpatterns += router.urls
