from rest_framework.response import Response
from rest_framework.views import APIView
from .models import PrayerRecord
from .serializers import PrayerSessionSerializer
from .voice_capture import VoiceCapture
import grpc
from prayertrack import prayer_tracker_pb2, prayer_tracker_pb2_grpc
from prayertrack.serializers import StartPrayerResponseSerializer
from bibleApp.models import CustomUser

from rest_framework import generics
from .models import DailyDevotion
from .serializers import DailyDevotionSerializer

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DailyDevotion, Supervisor
from .serializers import DailyDevotionSerializer


# class DailyDevotionCreateView(APIView):
#     def post(self, request, format=None):
#         serializer = DailyDevotionSerializer(data=request.data)
#         if serializer.is_valid():
#             # If the devotion is created by an admin, assign it to a user and supervisor
#             if request.user.is_staff:
#                 user_id = request.data.get('assigned_user')
#                 supervisor_id = request.data.get('supervisor')
#                 if user_id and supervisor_id:
#                     assigned_user = CustomUser.objects.get(id=user_id)
#                     supervisor = Supervisor.objects.get(id=supervisor_id)
#                     serializer.save(created_by=request.user, assigned_user=assigned_user, supervisor=supervisor)
#                 else:
#                     return Response({'error': 'Both assigned_user and supervisor are required for admin-created devotions.'}, status=status.HTTP_400_BAD_REQUEST)
#             else:
#                 serializer.save(created_by=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import DailyDevotion
from .serializers import DailyDevotionSerializer

class DailyDevotionViewSet(viewsets.ModelViewSet):
    queryset = DailyDevotion.objects.all()
    serializer_class = DailyDevotionSerializer

    def get_queryset(self):
        # Filter devotions based on the logged-in user
        return DailyDevotion.objects.filter(assigned_user=self.request.user)

    def create(self, request, *args, **kwargs):
        assigned_user_id = kwargs.get('assigned_user')
        supervisor_id = kwargs.get('supervisor')

        if assigned_user_id and supervisor_id:
            # This means a church admin is creating a devotion for a user
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif not assigned_user_id and not supervisor_id:
            # This means a regular user is creating a devotion for themselves
            request.data['assigned_user'] = request.user.id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Invalid request.'}, status=status.HTTP_400_BAD_REQUEST)






class CreateDailyDevotionView(generics.CreateAPIView):
    queryset = DailyDevotion.objects.all()
    serializer_class = DailyDevotionSerializer


from rest_framework import generics
from .models import UserPrayerSession
from .serializers import UserPrayerSessionSerializer

class CreatePrayerSessionView(generics.CreateAPIView):
    queryset = UserPrayerSession.objects.all()
    serializer_class = UserPrayerSessionSerializer






#########################
# views.py

from rest_framework import viewsets
from .models import DailyDevotion
from .serializers import DailyDevotionSerializer

class DevotionViewSet(viewsets.ModelViewSet):
    queryset = DailyDevotion.objects.all()
    serializer_class = DailyDevotionSerializer

    def perform_create(self, serializer):
        # Assuming you have a field called 'assigned_user' in your Devotion model
        assigned_user_id = self.request.data.get('assigned_user_id')  # Get the assigned user ID from the request data

        # Check if the assigned user ID is valid
        if assigned_user_id:
            assigned_user = CustomUser.objects.get(id=assigned_user_id)
            serializer.save(created_by=self.request.user, assigned_user=assigned_user)
        else:
            serializer.save(created_by=self.request.user)


###########################

class PrayerSessionView(APIView):
    serializer_class = PrayerSessionSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        sessions = UserPrayerSession.objects.filter(user=user)
        serializer = self.serializer_class(sessions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StartPrayerView(APIView):
    
    serializer_class = StartPrayerResponseSerializer
    def __init__(self):
        self.voice_capture = VoiceCapture()
      

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        daily_devotion_id = request.data.get('daily_devotion_id')  # Add this line
        channel = grpc.insecure_channel('localhost:50051')
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        request = prayer_tracker_pb2.StartPrayerRequest(user_id=user_id, daily_devotion_id=daily_devotion_id)
        response = stub.StartPrayer(request)
        channel.close()

        audio_data = request.data.get('audio_data')

        # Assuming you have a way to detect pauses in audio

        if request.data.get('pause_capture'):
            self.voice_capture.pause_capture()
        elif request.data.get('resume_capture'):
            self.voice_capture.resume_capture()


        # Toggle automatic pause if requested by user
        if request.data.get('toggle_automatic_pause'):
            VoiceCapture.toggle_automatic_pause()

        for chunk in VoiceCapture.simulate_voice_stream(audio_data):
            response = stub.ProcessVoiceStream(prayer_tracker_pb2.ProcessVoiceRequest(audio_data=chunk))
        
        return Response({'message': response.message})
