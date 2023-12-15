import grpc
from prayertrack import prayer_tracker_pb2, prayer_tracker_pb2_grpc

server_address = 'localhost:50053'

def start_prayer():
    with grpc.insecure_channel(server_address) as channel:
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        try:
            response = stub.StartPrayer(prayer_tracker_pb2.StartPrayerRequest(user_id=123))
            print(response.message)
        except grpc.RpcError as e:
            print(f"Error: {e}")

def end_prayer():
    with grpc.insecure_channel(server_address) as channel:
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        response = stub.EndPrayer(prayer_tracker_pb2.EndPrayerRequest(user_id=123))
        print(response.message)

def get_prayer_duration():
    with grpc.insecure_channel(server_address) as channel:
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        response = stub.PrayerDuration(prayer_tracker_pb2.PrayerDurationRequest(user_id=123))
        print(response.duration)

def get_voice_duration():
    with grpc.insecure_channel(server_address) as channel:
        stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
        response = stub.VoiceDuration(prayer_tracker_pb2.VoiceDurationRequest(user_id=123))
        print(response.duration)


def prayer_updates():
    user_id = 123 
    request = prayer_tracker_pb2.PrayerUpdatesRequest(user_id=user_id)

    try:
        with grpc.insecure_channel(server_address) as channel:
            stub = prayer_tracker_pb2_grpc.PrayerTrackerStub(channel)
            response_iterator = stub.PrayerUpdates(iter([request]))
            for response in response_iterator:
                print(f'Prayer Duration: {response.prayer_duration}')
                print(f'Voice Duration: {response.voice_duration}')
                print(f'Voice Detected: {response.voice_detected}')
    except grpc._channel._InactiveRpcError as e:
        print(f"Error: {e}")



if __name__ == '__main__':
    start_prayer()
    prayer_updates()
   
    input("Press Enter to end the prayer...")
    end_prayer()
    get_prayer_duration()
    get_voice_duration()
