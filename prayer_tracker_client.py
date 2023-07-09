import grpc
import prayer_tracker_pb2
import prayer_tracker_pb2_grpc
import time

def prayer_client():
    # Create a gRPC channel to connect to the server
    channel = grpc.insecure_channel('localhost:8000')

    # Create a gRPC stub
    stub = prayer_tracker_pb2_grpc.PrayerTrackerServiceStub(channel)

    # Open a bidirectional stream to send and receive prayer updates
    stream = stub.PrayerUpdates()

    # Send start prayer request
    start_request = prayer_tracker_pb2.PrayerStartRequest(user_id='user123')
    stream.send_message(start_request)

    # Listen for prayer updates
    for response in stream:
        if response.HasField('voice_detected'):
            if response.voice_detected:
                print("Voice detected while praying.")
        elif response.HasField('prayer_ended'):
            print("Prayer ended.")
            break

    # Close the stream
    stream.close()

def main():
    # Start the prayer client in a separate thread
    import threading
    client_thread = threading.Thread(target=prayer_client)
    client_thread.start()

    # Simulate prayer time
    prayer_duration = 10  # Set the duration of prayer time in seconds
    start_time = time.time()
    while time.time() - start_time < prayer_duration:
        time.sleep(1)  # Simulate a 1-second interval
        print("Prayer in progress...")

    # End prayer
    end_request = prayer_tracker_pb2.PrayerEndRequest(user_id='user123')
    # Create a gRPC channel and stub
    channel = grpc.insecure_channel('localhost:8000')
    stub = prayer_tracker_pb2_grpc.PrayerTrackerServiceStub(channel)
    end_response = stub.EndPrayer(end_request)
    print(end_response.message)

    # Wait for the client thread to finish
    client_thread.join()

if __name__ == '__main__':
    main()



























# import grpc
# import prayer_tracker_pb2
# import prayer_tracker_pb2_grpc
# import time

# def simulate_prayer_time():
#     # Create a gRPC channel and stub
#     channel = grpc.insecure_channel('localhost:8000')
#     stub = prayer_tracker_pb2_grpc.PrayerTrackerServiceStub(channel)

#     # Start prayer
#     start_request = prayer_tracker_pb2.PrayerStartRequest(user_id='123')
#     start_response = stub.StartPrayer(start_request)
#     print(start_response.message)

#      # Subscribe to PrayerUpdates
#     prayer_request = prayer_tracker_pb2.PrayerRequest(user_id='123')
#     prayer_updates = stub.PrayerUpdates(prayer_request)
#     for response in prayer_updates:
#         print(response.message)

#     # Simulate prayer time
#     prayer_duration = 10  # Set the duration of prayer time in seconds
#     start_time = time.time()
#     while time.time() - start_time < prayer_duration:
#         time.sleep(1)  # Simulate a 1-second interval
#         print("Prayer in progress...")

#     # End prayer
#     end_request = prayer_tracker_pb2.PrayerEndRequest(user_id='123')
#     end_response = stub.EndPrayer(end_request)
#     print(end_response.message)

# def main():
#     simulate_prayer_time()

# if __name__ == '__main__':
#     main()
































# import grpc
# import prayer_tracker_pb2
# import prayer_tracker_pb2_grpc
# import time

# def prayer_client():
#     # Create a gRPC channel to connect to the server
#     channel = grpc.insecure_channel('localhost:8000')

#     # Create a stub for the PrayerTrackerService
#     stub = prayer_tracker_pb2_grpc.PrayerTrackerServiceStub(channel)

#     # Send a StartPrayer request
#     start_request = prayer_tracker_pb2.PrayerStartRequest(user_id='123')
#     start_response = stub.StartPrayer(start_request)
#     print(start_response.message)

#     # Simulate prayer time
#     time.sleep(5)

#     # Send an EndPrayer request
#     end_request = prayer_tracker_pb2.PrayerEndRequest(user_id='123')
#     end_response = stub.EndPrayer(end_request)
#     print(end_response.message)

#     # Subscribe to PrayerUpdates
#     prayer_request = prayer_tracker_pb2.PrayerRequest(user_id='123')
#     prayer_updates = stub.PrayerUpdates(prayer_request)
#     for response in prayer_updates:
#         print(response.message)

# if __name__ == '__main__':
#     prayer_client()
