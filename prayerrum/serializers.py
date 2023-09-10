# views.py

from django_grpc_framework import generics

from .models import PrayerRoom, Prayer
from .serializers import PrayerRoomSerializer, PrayerSerializer

class PrayerRoomService(generics.ModelService):
    queryset = PrayerRoom.objects.all()
    serializer_class = PrayerRoomSerializer

class PrayerService(generics.ModelService):
    queryset = Prayer.objects.all()
    serializer_class = PrayerSerializer
