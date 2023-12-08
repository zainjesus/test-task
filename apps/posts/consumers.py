import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging


class PostConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            "post_group",
            self.channel_name
        )
        await self.accept()
        logging.info("WebSocket connected")

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("post_group", self.channel_name)
        logging.info("WebSocket disconnected")

    async def post_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }, ensure_ascii=False))
        logging.info("Sending WebSocket message")


