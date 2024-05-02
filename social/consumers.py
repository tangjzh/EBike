import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.db.models import Count
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone
from urllib.parse import parse_qs

from .models import Message, Room
from .constant import ID2NAME, DEFAULT_NAME

User = get_user_model()

class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.other_user = None
        self.room = None
        self.room_group_name = None
        self.type = None

    def connect(self):
        # TODO: 如果token过期，如何处理
        self.user = self.scope['user']
        other_username = self.scope['url_route']['kwargs']['friendname']
        self.type = self.scope['type']
        self.room = self.get_or_create_room(self.user, other_username)
        self.room_group_name = f'chat_{self.room.id}'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def get_or_create_room(self, user, other_username):
        self.other_user = User.objects.filter(username=other_username).first()
        if not self.other_user:
            return None  # Handle error appropriately if other user doesn't exist

        room = Room.get_or_new(user, self.other_user, f"{user.username}与{other_username}的{ID2NAME.get(self.type, DEFAULT_NAME)}", self.type)
        return room

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        command = data.get('command')

        if command == 'fetch_messages':
            self.fetch_messages()
        elif command == 'new_message':
            self.new_message(data)
        elif command == 'typing_start':
            self.typing_start(data)
        elif command == 'typing_stop':
            self.typing_stop(data)

    def fetch_messages(self):
        messages = self.room.messages.all().order_by('-timestamp')[:50]  # Fetches the latest 50 messages
        content = {
            'command': 'messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_chat_message(content)

    def new_message(self, data):
        sender_username = data.get('from')
        message_text = data.get('message')

        sender = User.objects.filter(username=sender_username).first()
        if not sender or sender != self.user:
            self.send_error("Sender not found.")
            return

        message = Message.objects.create(
            room=self.room,
            sender=sender,
            content=message_text,
            timestamp=timezone.now()
        )

        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': content
            }
        )

    def typing_start(self, data):
        username = data.get('from')
        content = {
            'command': 'typing_start',
            'username': username
        }
        self.send_chat_message(content)

    def typing_stop(self, data):
        username = data.get('from')
        content = {
            'command': 'typing_stop',
            'username': username
        }
        self.send_chat_message(content)

    def send_chat_message(self, message):
        self.send(text_data=json.dumps(message))

    def send_error(self, message):
        error_message = {'error': message}
        self.send(text_data=json.dumps(error_message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))

    def messages_to_json(self, messages):
        return [self.message_to_json(message) for message in messages]

    def message_to_json(self, message):
        return {
            'id': message.id,
            'sender': message.sender.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }
