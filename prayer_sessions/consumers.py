import json
from channels.generic.websocket import AsyncWebsocketConsumer
from prayertrack import prayer_tracker_pb2

class PrayerTrackerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        user_id = self.scope['url_route']['kwargs']['user_id']  # Get the user ID from the URL
        print(user_id)
        await self.accept()

        # Add the user to a group for broadcasting updates
        await self.channel_layer.group_add(f'user_{user_id}', self.channel_name)

    async def disconnect(self, close_code):
        user_id = self.scope['url_route']['kwargs']['user_id']  # Get the user ID from the URL

        # Remove the user from the group
        await self.channel_layer.group_discard(f'user_{user_id}', self.channel_name)

    async def send_prayer_update(self, event):
        response_data = event['response']
        print('Response Data', response_data)

        response = prayer_tracker_pb2.PrayerUpdateResponse()
        print('Real Response', response)
        response.ParseFromString(response_data)

        # Send the prayer update to the WebSocket client
        await self.send(text_data=json.dumps({
            'prayer_duration': response.prayer_duration,
            'voice_duration': response.voice_duration,
            'voice_detected': response.voice_detected,
        }))
