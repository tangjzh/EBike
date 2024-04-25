import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import Message, Room

User = get_user_model()

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.user = self.scope['user']
        self.room_group_name = f'chat_{self.room_id}'

        # Check if user is part of the room
        if not self.is_user_in_room(self.user, self.room_id):
            self.close()
        
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        command = data.get('command', None)

        if command == 'fetch_messages':
            self.fetch_messages(data)
        elif command == 'new_message':
            self.new_message(data)

    def fetch_messages(self, data):
        messages = self.get_room_messages(data['room_id'])
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def new_message(self, data):
        author_user = self.user
        message = self.create_message(author_user, data['room_id'], data['message'])
        
        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        self.send_chat_message(content)

    @database_sync_to_async
    def is_user_in_room(self, user, room_id):
        return Room.objects.filter(id=room_id, participants=user).exists()

    @database_sync_to_async
    def get_room_messages(self, room_id):
        return Message.objects.filter(room__id=room_id).order_by('-timestamp')[:20]

    @database_sync_to_async
    def create_message(self, user, room_id, message):
        room = Room.objects.get(id=room_id)
        return Message.objects.create(room=room, sender=user, content=message)

    def messages_to_json(self, messages):
        return [self.message_to_json(message) for message in messages]

    def message_to_json(self, message):
        return {
            'id': message.id,
            'room': message.room.id,
            'sender': message.sender.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Handler for sending message to WebSocket
    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
