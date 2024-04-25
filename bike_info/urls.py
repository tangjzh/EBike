from django.urls import path
from .views import BikeListView, BikeDetailView, BikeIDListView
from .views import ChannelListCreateAPIView, ChannelDetailAPIView, ChannelIDListView
from .views import BikeImageCreateView, BikeImageDeleteView

urlpatterns = [
    # TODO: 权限管理
    path('', BikeListView.as_view(), name='bike-list'),
    path('<int:pk>/', BikeDetailView.as_view(), name='bike-detail'),
    path('id/', BikeIDListView.as_view(), name='ids'),
    path('channel/', ChannelListCreateAPIView.as_view(), name='channel-list'),
    path('channel/id/', ChannelIDListView.as_view(), name='channel-id'),
    path('channel/<int:pk>/', ChannelDetailAPIView.as_view(), name='channel-detail'),
    path('images/', BikeImageCreateView.as_view(), name='bike-image-create'),
    path('images/<int:id>/', BikeImageDeleteView.as_view(), name='bike-image-delete'),
]
