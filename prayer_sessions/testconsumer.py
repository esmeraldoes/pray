import asyncio
import websockets
import json

async def test_websocket():
    async with websockets.connect('ws://127.0.0.1/ws/prayer_tracker/') as websocket:
        
        user_id = 1

        
        start_prayer_message = json.dumps({
            "user_id": user_id,
            "type": "StartPrayer",
        })
        await websocket.send(start_prayer_message)

        
        while True:
            response = await websocket.recv()
            data = json.loads(response)
            print(f"Prayer Duration: {data['prayer_duration']}, Voice Duration: {data['voice_duration']}, Voice Detected: {data['voice_detected']}")

            
            await asyncio.sleep(10)
            end_prayer_message = json.dumps({
                "user_id": user_id,
                "type": "EndPrayer",
            })
            await websocket.send(end_prayer_message)
            break

asyncio.get_event_loop().run_until_complete(test_websocket())
