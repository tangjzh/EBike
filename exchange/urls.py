from django.urls import path, re_path
from .views import *
from django.views.static import serve
from django.conf import settings

app_name = 'shop'

urlpatterns = [
    path('publish/', PublishView.as_view(), name='publish'),
    path('index/', GetGoodsView.as_view(), name='get_goods'),
    path('mine/', MyGoodsView.as_view(), name='my_goods'),
    path('detail/', GoodsDetailView.as_view(), name='goods_detail'),
    path('search/', MySearchView(), name='haystack_search'),
    re_path(r'image/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]