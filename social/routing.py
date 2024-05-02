from django.urls import path
from .consumers import *
import jwt
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from channels.auth import AuthMiddlewareStack
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from django.conf import settings
from jwt import ExpiredSignatureError, DecodeError
from .constant import ID2NAME

User = get_user_model()

class TokenAuthMiddleware(BaseMiddleware):
    def __init__(self, inner):
        super().__init__(inner)

    async def __call__(self, scope, receive, send):
        # Decode the query string to extract the token
        query_string = parse_qs(scope['query_string'].decode())
        token = query_string.get('token', [None])[0]
        type = query_string.get('type', [list(ID2NAME.keys())[0]])[0]
        if token:
            try:
                # Decode the JWT token
                payload = jwt.decode(token, settings.SIMPLE_JWT['SIGNING_KEY'], algorithms=[settings.SIMPLE_JWT['ALGORITHM']])
                user_id = payload.get(settings.SIMPLE_JWT['USER_ID_CLAIM'])
                user = await self.get_user(user_id)
                scope['user'] = user
            except (ExpiredSignatureError, DecodeError, User.DoesNotExist) as e:
                scope['user'] = AnonymousUser()
        else:
            scope['user'] = AnonymousUser()

        scope['type'] = type

        return await self.inner(scope, receive, send)
    
    @database_sync_to_async
    def get_user(self, user_id):
        """Fetch user from the database."""
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))


websocket_urlpatterns = [
    path('ws/chat/<str:friendname>/', ChatConsumer.as_asgi()),
]