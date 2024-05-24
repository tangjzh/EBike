from django.urls import path, re_path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('goods/', PublishView.as_view(), name='publish'),
    path('goods/', GetGoodsView.as_view(), name='get_goods'),
    path('goods/mine/', MyGoodsView.as_view(), name='my_goods'),
    path('goods/<str:pk>/', GoodsDetailView.as_view(), name='goods_detail'),
    path('goods/search/', MySearchView(), name='haystack_search'),
]