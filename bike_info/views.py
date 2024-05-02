from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Bike, Channel
from .serializers import BikeSerializer, ChannelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import BikeFilter
from .serializers import BikeIDSerializer, ChannelIDSerializer
from .models import BikeImage
from .serializers import BikeImageSerializer
from rest_framework.parsers import MultiPartParser, JSONParser

class BikeIDListView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeIDSerializer

class BikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

class BikeListView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    parser_classes = [MultiPartParser, JSONParser]
    filterset_class = BikeFilter
    ordering_fields = ['price', 'rating', 'release_date']

class ChannelIDListView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelIDSerializer

class ChannelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class ChannelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

class BikeImageCreateView(generics.CreateAPIView):
    queryset = BikeImage.objects.all()
    serializer_class = BikeImageSerializer
    parser_classes = [MultiPartParser, JSONParser]

class BikeImageDeleteView(generics.DestroyAPIView):
    queryset = BikeImage.objects.all()
    serializer_class = BikeImageSerializer
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        bike_image = self.get_object()
        bike_image.image.delete()  # 删除文件
        return super().delete(request, *args, **kwargs)