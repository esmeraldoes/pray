import random
import time
import grpc
import prayer_tracker_pb2
import prayer_tracker_pb2_grpc

def simulate_voice_input(user_id):
    # Create a gRPC channel and stub
    channel = grpc.insecure_channel('localhost:80001')
    stub = prayer_tracker_pb2_grpc.PrayerTrackerServiceStub(channel)

    # Start prayer
    start_request = prayer_tracker_pb2.StartPrayerRequest(user_id=user_id)
    start_response = stub.StartPrayer(start_request)
    print(start_response.message)

    # Simulate voice input
    prayer_duration = 10  # Set the duration of prayer time in seconds
    start_time = time.time()
    while time.time() - start_time < prayer_duration:
        # Simulate random audio data
        audio_data = bytes([random.randint(0, 255) for _ in range(160)])  # 160 frames per chunk

        # Send audio data to the server
        voice_request = prayer_tracker_pb2.ProcessVoiceRequest(user_id=user_id, audio_data=audio_data)
        voice_response = stub.ProcessVoiceStream(voice_request)
        print(voice_response)

        # Process the response if needed
        # ...

        time.sleep(1)  # Simulate a 1-second interval

    # End prayer
    end_request = prayer_tracker_pb2.EndPrayerRequest(user_id=user_id)
    end_response = stub.EndPrayer(end_request)
    print(end_response.message)

def main():
    user_id = '1'  # Replace with the desired user ID
    simulate_voice_input(user_id)

if __name__ == '__main__':
    main()
