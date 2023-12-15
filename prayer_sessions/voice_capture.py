import webrtcvad
import numpy as np

class VoiceCapture:
    def __init__(self):
        self.vad = webrtcvad.Vad()
        self.vad.set_mode(1)  # Set the aggressiveness mode (0 to 3)
        self.is_paused = False
        self.automatic_pause = True 

    def toggle_automatic_pause(self):
        self.automatic_pause = not self.automatic_pause

       
    def pause_capture(self):
        self.is_paused = True

    def resume_capture(self):
        self.is_paused = False

    def is_speech(self, audio_data):
        return self.vad.is_speech(audio_data, sample_rate=16000)


    def simulate_voice_stream(self, audio_data):
        # Simulate the gRPC voice stream response
        chunk_size = 1600  # Adjust this based on your requirements
        audio_data = np.frombuffer(audio_data, dtype=np.int16)

        for i in range(0, len(audio_data), chunk_size):
            if self.automatic_pause and not self.is_speech(audio_data[i:i+chunk_size]):
                self.is_paused = True  # Automatically pause if no speech detected
            if not self.is_paused:
                yield audio_data[i:i+chunk_size].tobytes()
        

            if not  VoiceCapture.is_speech(audio_data[i:i+chunk_size]):
                print(f"Pause detected at {i} ms")