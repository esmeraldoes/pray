import grpc
from concurrent import futures
import time
import webrtcvad

import prayer_tracker_pb2
import prayer_tracker_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class PrayerTrackerService(prayer_tracker_pb2_grpc.PrayerTrackerServiceServicer):
    def __init__(self):
        self.vad = webrtcvad.Vad()
        self.vad.set_mode(3)  # Set the aggressiveness of VAD (0-3)

    def StartPrayer(self, request, context):
        print("Prayer started for user:", request.user_id)
        return prayer_tracker_pb2.PrayerStartResponse(message="Prayer started.")

    def EndPrayer(self, request, context):
        print("Prayer ended for user:", request.user_id)
        return prayer_tracker_pb2.PrayerEndResponse(message="Prayer ended.")

    def PrayerUpdates(self, request, context):
        audio_stream_generator = context.stream_recv()

        is_voice_active = False
        prayer_duration = 0

        for audio_data in audio_stream_generator:
            is_speech = self.detect_voice_activity(audio_data)

            if is_speech and not is_voice_active:
                is_voice_active = True
                print("Voice detected while praying.")
            elif not is_speech and is_voice_active:
                is_voice_active = False
                print("Voice stopped while praying.")
            elif is_voice_active:
                prayer_duration += 1

        prayer_updates = [
            prayer_tracker_pb2.PrayerUpdateResponse(voice_detected=is_voice_active),
            prayer_tracker_pb2.PrayerUpdateResponse(prayer_ended=True, prayer_duration=prayer_duration),
        ]

        for update in prayer_updates:
            yield update

    def detect_voice_activity(self, audio_data):
        is_speech = self.vad.is_speech(audio_data, 16000)
        return is_speech

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prayer_tracker_pb2_grpc.add_PrayerTrackerServiceServicer_to_server(PrayerTrackerService(), server)
    server.add_insecure_port('[::]:8001')
    server.start()
    print("Prayer Tracker gRPC server started on port 8001...")
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
