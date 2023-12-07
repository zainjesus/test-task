import json
from channels.generic.websocket import AsyncWebsocketConsumer


class PostNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def notify_post_published(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'message': message}))
