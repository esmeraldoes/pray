import grpc
from concurrent import futures
import time
import prayer_tracker_pb2
import prayer_tracker_pb2_grpc
import webrtcvad
import pyaudio

# Constants for audio capture
CHUNK_SIZE = 160  # Number of audio frames per chunk
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio channel
RATE = 16000  # Audio sample rate (16 kHz)

class PrayerTrackerServicer(prayer_tracker_pb2_grpc.PrayerTrackerServiceServicer):
    def __init__(self):
        self.prayer_times = {}  # Dictionary to store user prayer start times

    def StartPrayer(self, request, context):
        user_id = request.user_id
        self.prayer_times[user_id] = {
            'start_time': time.time(),
            'active': False
        }  # Store the start time and active status
        response = prayer_tracker_pb2.PrayerResponse(message="Prayer started.")
        return response

    def EndPrayer(self, request, context):
        user_id = request.user_id
        if user_id in self.prayer_times:
            start_time = self.prayer_times[user_id]['start_time']
            if self.prayer_times[user_id]['active']:
                prayer_duration = int(time.time() - start_time)
                del self.prayer_times[user_id]  # Remove the prayer entry
                response = prayer_tracker_pb2.PrayerResponse(message=f"Prayer ended. Duration: {prayer_duration} seconds.")
            else:
                response = prayer_tracker_pb2.PrayerResponse(message="No active prayer session found.")
        else:
            response = prayer_tracker_pb2.PrayerResponse(message="No active prayer session found.")
        return response

    def PrayerUpdates(self, request, context):
        user_id = request.user_id
        if user_id in self.prayer_times:
            self.prayer_times[user_id]['active'] = True
            vad = webrtcvad.Vad()
            vad.set_mode(1)  # Aggressive mode for voice activity detection

            # Initialize audio capture
            audio = pyaudio.PyAudio()
            stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)

            try:
                for chunk in self.audio_stream_generator(stream):
                    is_speech = vad.is_speech(chunk, RATE)
                    if is_speech:
                        # Speech detected, update the prayer duration
                        self.prayer_times[user_id]['start_time'] = time.time()
                        print("Speech detected")

                    # Send response to client
                    prayer_response = prayer_tracker_pb2.PrayerResponse(message="Prayer in progress.")
                    yield prayer_response
            except Exception as e:
                print(f"Error during prayer updates: {e}")
            finally:
                stream.stop_stream()
                stream.close()
                audio.terminate()
                self.prayer_times[user_id]['active'] = False  # Prayer session ended

    def audio_stream_generator(self, audio_stream):
        while True:
            yield audio_stream.read(CHUNK_SIZE)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prayer_tracker_pb2_grpc.add_PrayerTrackerServiceServicer_to_server(PrayerTrackerServicer(), server)
    # server.add_insecure_port('[::]:80001')
    server.add_insecure_port('0.0.0.0:8001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()