import grpc
from concurrent import futures
import time
import webrtcvad
import prayer_tracker_pb2 as pb2
import prayer_tracker_pb2_grpc as pb2_grpc

class PrayerTrackerServicer(pb2_grpc.PrayerTrackerServiceServicer):
    def __init__(self):
        self.prayer_times = {}
        self.voice_detected = False
        self.vad = webrtcvad.Vad()

    def StartPrayer(self, request, context):
        user_id = request.user_id
        self.prayer_times[user_id] = None  # Initialize prayer start time as None
        self.voice_detected = False  # Reset voice detection flag
        response = pb2.PrayerResponse(message="Prayer started.")
        return response

    def ProcessAudioStream(self, request_iterator):
        frames_per_buffer = 320  # Adjust buffer size according to your needs
        voice_detected = False

        for audio_data in request_iterator:
            if audio_data:
                if self.vad.is_speech(audio_data.audio_chunk, sample_rate=16000):  # Adjust sample rate if needed
                    voice_detected = True
                    if not self.voice_detected:
                        self.voice_detected = True
                        self.prayer_start_time = time.time()
                else:
                    voice_detected = False
            else:
                break

        if not voice_detected and self.voice_detected:
            self.voice_detected = False
            prayer_duration = int(time.time() - self.prayer_start_time)
            return prayer_duration

    def EndPrayer(self, request, context):
        user_id = request.user_id
        if user_id in self.prayer_times:
            prayer_start_time = self.prayer_times[user_id]
            if prayer_start_time is None:
                response = pb2.PrayerResponse(message="Prayer not started.")
            else:
                prayer_duration = prayer_start_time if self.voice_detected else self.ProcessAudioStream(request.audio_stream)
                self.prayer_times[user_id] = None  # Reset prayer start time
                response = pb2.PrayerResponse(message=f"Prayer ended. Duration: {prayer_duration} seconds.")
        else:
            response = pb2.PrayerResponse(message="No active prayer session found.")
        return response

    def PrayerStream(self, request_iterator, context):
        user_id = None
        for request in request_iterator:
            if not user_id:
                user_id = request.user_id
                self.prayer_times[user_id] = None  # Initialize prayer start time as None
                self.voice_detected = False  # Reset voice detection flag
                yield pb2.PrayerResponse(message="Prayer started.")
                continue

            if not self.voice_detected:
                self.voice_detected = self.vad.is_speech(request.audio_chunk, sample_rate=16000)

        if user_id in self.prayer_times:
            prayer_start_time = self.prayer_times[user_id]
            if prayer_start_time is None:
                yield pb2.PrayerResponse(message="Prayer not started.")
            else:
                prayer_duration = prayer_start_time if self.voice_detected else self.ProcessAudioStream(request_iterator)
                self.prayer_times[user_id] = None  # Reset prayer start time
                yield pb2.PrayerResponse(message=f"Prayer ended. Duration: {prayer_duration} seconds.")
        else:
            yield pb2.PrayerResponse(message="No active prayer session found.")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_PrayerTrackerServiceServicer_to_server(PrayerTrackerServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

