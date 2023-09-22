from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.views import APIView
import grpc
from prayertrack import prayer_tracker_pb2
from prayertrack import prayer_tracker_pb2_grpc
from .serializers import (StartPrayerResponseSerializer, PrayerUpdateResponseSerializer, 
    EndPrayerResponseSerializer, PrayerDurationResponseSerializer, VoiceDurationResponseSerializer)


from django.conf import settings
server_address = f'{settings.GRPC_SERVER_ADDRESS}:50053' 



class StartPrayerView(APIView):
    serializer_class = StartPrayerResponseSerializer 
    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        channel = grpc.insecure_channel(server_address)
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        request = prayer_tracker_pb2.StartPrayerRequest(user_id=user_id)
        response = stub.StartPrayer(request)
        channel.close()
        return Response({'message': response.message})
    
class EndPrayerView(APIView):
    serializer_class = EndPrayerResponseSerializer
    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        channel = grpc.insecure_channel(server_address)
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        request = prayer_tracker_pb2.EndPrayerRequest(user_id=user_id)
        response = stub.EndPrayer(request)
        channel.close()
        serializer = EndPrayerResponseSerializer(data={'message': response.message})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class PrayerUpdatesView(APIView):

    serializer_class = PrayerUpdateResponseSerializer
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        channel = grpc.insecure_channel(server_address)
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        request = prayer_tracker_pb2.PrayerUpdatesRequest(user_id=user_id)
        responses = stub.PrayerUpdates([request])
        data = [{'prayer_duration': response.prayer_duration, 
                 'voice_duration': response.voice_duration, 
                 'voice_detected': response.voice_detected} 
                for response in responses]
        channel.close()
        serializer = PrayerUpdateResponseSerializer(data=data, many=True)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class PrayerDurationView(APIView):
# class PrayerDurationView(LoginRequiredMixin, APIView):
    serializer_class = PrayerDurationResponseSerializer
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        channel = grpc.insecure_channel(server_address)
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        request = prayer_tracker_pb2.PrayerDurationRequest(user_id=user_id)
        response = stub.PrayerDuration(request)
        channel.close()
        serializer = PrayerDurationResponseSerializer(data={'duration': response.duration})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class VoiceDurationView(APIView):
# class VoiceDurationView(LoginRequiredMixin, APIView):
    serializer_class = VoiceDurationResponseSerializer
    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        channel = grpc.insecure_channel(server_address)
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        request = prayer_tracker_pb2.VoiceDurationRequest(user_id=user_id)
        response = stub.VoiceDuration(request)
        channel.close()
        serializer = VoiceDurationResponseSerializer(data={'duration': response.duration})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

