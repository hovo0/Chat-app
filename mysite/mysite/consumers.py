# myapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model

class MyConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = await self.get_user()
        if self.user.is_authenticated:
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        await self.send(text_data=json.dumps({
            'message': message,
            'username': self.user.username
        }))

    async def get_user(self):
        user = await self.scope["session"].get('user')
        if user is None:
            return await self.scope["user"]
        else:
            return get_user_model().objects.get(pk=user)
