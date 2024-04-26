from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from social import routing

application = ProtocolTypeRouter({
    'websocket': routing.TokenAuthMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )),
})
