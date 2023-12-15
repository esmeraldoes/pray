def ProcessVoiceStream(self, request_iterator, context):
    user_id = next(request_iterator).user_id
    prayer_paused = False

    for request in request_iterator:
        audio_data = request.audio_data

        # Using WebRTC VAD to detect voice
        if self._is_speech(audio_data):
            self.prayer_sessions[user_id]['voice_detected'] = True

            if not prayer_paused and self.prayer_sessions[user_id]['active']:
                # If prayer is active and voice is detected, resume the prayer time
                if 'prayer_pause_time' in self.prayer_sessions[user_id]:
                    prayer_pause_time = self.prayer_sessions[user_id]['prayer_pause_time']
                    prayer_resume_time = datetime.now()
                    prayer_pause_duration = prayer_resume_time - prayer_pause_time
                    self.prayer_sessions[user_id]['prayer_duration'] += prayer_pause_duration
                    del self.prayer_sessions[user_id]['prayer_pause_time']
            else:
                # If prayer is active and voice is detected for the first time, start counting the prayer duration
                self.prayer_sessions[user_id]['active'] = True
                self.prayer_sessions[user_id]['start_time'] = datetime.now()

        else:
            self.prayer_sessions[user_id]['voice_detected'] = False

            if not prayer_paused and self.prayer_sessions[user_id]['active']:
                # If prayer is active and voice is not detected, pause the prayer time
                prayer_paused = True
                self.prayer_sessions[user_id]['prayer_pause_time'] = datetime.now()

    response = prayer_tracker_pb2.ProcessVoiceResponse(transcript='Transcription goes here')
    yield response
