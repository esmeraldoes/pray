import grpc
from concurrent import futures
import time
import prayer_tracker_pb2
import prayer_tracker_pb2_grpc
import webrtcvad


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
                prayer_duration_str = self.format_duration(prayer_duration)

                del self.prayer_times[user_id]  # Remove the prayer entry
                response = prayer_tracker_pb2.PrayerResponse(message=f"Prayer ended. Duration: {prayer_duration_str} seconds.")
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
            prayer_start_time = self.prayer_times[user_id]['start_time']

            try:
                # Process audio data received from the frontend
                for audio_chunk in request.audio_stream:
                    is_speech = vad.is_speech(audio_chunk.audio_data, audio_chunk.sample_rate)
                    if self.prayer_times[user_id]['active']:
                        if is_speech:
                            current_time = time.time()
                            prayer_duration = int(current_time - prayer_start_time)
                            prayer_duration_str = self.format_duration(prayer_duration)
                            prayer_start_time = current_time
                             # Speech detected, update the prayer duration
                            # self.prayer_times[user_id]['start_time'] = current_time
                            
                            print("Speech detected")

                        # Send response to client
                        prayer_response = prayer_tracker_pb2.PrayerResponse(message=f"Prayer Voice progress. Duration: {prayer_duration_str}")
                        yield prayer_response


            except Exception as e:
                print(f"Error during prayer updates: {e}")
            finally:
                
                self.prayer_times[user_id]['active'] = False  # Prayer session ended

                #self.prayer_times[user_id]['active'] = False  # Prayer session ended
        else:
            response = prayer_tracker_pb2.PrayerResponse(message="No active prayer session found.")
            yield response

    def format_duration(self, duration):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    prayer_tracker_pb2_grpc.add_PrayerTrackerServiceServicer_to_server(PrayerTrackerServicer(), server)
    server.add_insecure_port('0.0.0.0:8001')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()