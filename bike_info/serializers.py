from rest_framework import serializers
from .models import Bike, Channel, BikeImage

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'bike', 'name', 'url', 'service_info']

class BikeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeImage
        fields = ['id', 'bike', 'image']

class BikeSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, read_only=True)
    bike_images = BikeImageSerializer(many=True, read_only=True)

    class Meta:
        model = Bike
        fields = ['id', 'brand', 'model', 'price', 'rating', 'release_date', 'description', 'channels', 'bike_images']

class BikeIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id']  # 只包含 id 字段

class ChannelIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id']  # 只包含 id 字段