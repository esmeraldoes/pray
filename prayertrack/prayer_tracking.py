import grpc
from concurrent import futures
from datetime import datetime, timedelta
from prayertrack import prayer_tracker_pb2
from prayertrack import prayer_tracker_pb2_grpc

from django.core.asgiref.sync import async_to_sync


from asgiref.sync import sync_to_async

# import prayer_tracker_pb2_grpc

from django.conf import settings


server_address = f'{settings.GRPC_SERVER_ADDRESS}:50053' 


import webrtcvad
from channels.layers import get_channel_layer
from collections import defaultdict

class PrayerTrackerServicer(prayer_tracker_pb2_grpc.PrayerTrackerServicer):
    def __init__(self):
        self.prayer_sessions = defaultdict(dict)
        self.vad = webrtcvad.Vad()

    def _is_speech(self, audio_data):
        return self.vad.is_speech(audio_data, sample_rate=16000)

    def StartPrayer(self, request, context):
        user_id = request.user_id
        if not self.prayer_sessions[user_id]:
            self.prayer_sessions[user_id] = {
                'start_time': datetime.now(),
                'active': True,
                'voice_detected': False,
                'voice_start_time': None,
                'voice_duration': timedelta(seconds=0),
            }
            response = prayer_tracker_pb2.StartPrayerResponse(message='Prayer started successfully.')
        else:
            response = prayer_tracker_pb2.StartPrayerResponse(message='Prayer is already active.')
        return response

    async def PrayerUpdates(self, request_iterator, context):
        user_id = next(request_iterator).user_id
         # Get the channel layer for handling WebSocket communication
        channel_layer = get_channel_layer()

        while True:
            if self.prayer_sessions[user_id]['active']:
                prayer_start_time = self.prayer_sessions[user_id]['start_time']
                current_time = datetime.now()
                prayer_duration = current_time - prayer_start_time

                voice_detected = self.prayer_sessions[user_id]['voice_detected']
                if voice_detected:
                    voice_start_time = self.prayer_sessions[user_id]['voice_start_time'] or current_time
                    voice_duration = current_time - voice_start_time
                else:
                    voice_duration = self.prayer_sessions[user_id]['voice_duration']

                self.prayer_sessions[user_id]['voice_duration'] = voice_duration

                response = prayer_tracker_pb2.PrayerUpdateResponse(
                    prayer_duration=str(prayer_duration),
                    voice_duration=str(voice_duration),
                    voice_detected=voice_detected,
                )
                # Broadcast the response to all connected WebSocket clients
                await async_to_sync(channel_layer.group_send)(
                    f'user_{user_id}',
                    {
                        'type': 'send_prayer_update',
                        'response': response.SerializeToString(),
                    }
                )
                yield response
            else:
                break

    def ProcessVoiceStream(self, request_iterator, context):
        user_id = next(request_iterator).user_id
        voice_detected = False

        for request in request_iterator:
            audio_data = request.audio_data

            if self._is_speech(audio_data):
                if not voice_detected:
                    voice_detected = True
                    self.prayer_sessions[user_id]['voice_start_time'] = datetime.now()
            else:
                if voice_detected:
                    voice_detected = False
                    voice_start_time = self.prayer_sessions[user_id]['voice_start_time']
                    voice_end_time = datetime.now()
                    voice_duration = voice_end_time - voice_start_time
                    self.prayer_sessions[user_id]['voice_duration'] += voice_duration

        response = prayer_tracker_pb2.ProcessVoiceResponse(transcript='Transcription goes here')
        yield response

    def EndPrayer(self, request, context):
        user_id = request.user_id
        user_session = self.prayer_sessions.get(user_id)
        if user_session:
            prayer_start_time = user_session['start_time']
            current_time = datetime.now()
            prayer_duration = current_time - prayer_start_time
            del self.prayer_sessions[user_id]
            response = prayer_tracker_pb2.EndPrayerResponse(message=f'Prayer ended. Duration: {prayer_duration}')
        else:
            response = prayer_tracker_pb2.EndPrayerResponse(message='No active prayer session found.')
        return response
    

    def _format_duration(self, duration):
        hours, remainder = divmod(duration.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f'{hours:02}:{minutes:02}:{seconds:02}'

    def PrayerDuration(self, request, context):
        user_id = request.user_id
        user_session = self.prayer_sessions.get(user_id)
        if user_session:
            prayer_start_time = user_session['start_time']
            current_time = datetime.now()
            prayer_duration = current_time - prayer_start_time
            return prayer_tracker_pb2.PrayerDurationResponse(duration=self._format_duration(prayer_duration))
        else:
            return prayer_tracker_pb2.PrayerDurationResponse(message='No active prayer session found.')

    def VoiceDuration(self, request, context):
        user_id = request.user_id
        user_session = self.prayer_sessions.get(user_id)
        if user_session:
            voice_duration = user_session['voice_duration']
            return prayer_tracker_pb2.VoiceDurationResponse(duration=self._format_duration(voice_duration))
        else:
            return prayer_tracker_pb2.VoiceDurationResponse(message='No active prayer session found.')


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prayer_tracker_pb2_grpc.add_PrayerTrackerServicer_to_server(PrayerTrackerServicer(), server)
    server.add_insecure_port(server_address)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
