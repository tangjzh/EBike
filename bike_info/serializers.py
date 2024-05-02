from rest_framework import serializers
from .models import Bike, Channel, BikeImage
from django.core.files.base import ContentFile
import base64
import uuid

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'bike', 'name', 'url', 'service_info']

class BikeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeImage
        fields = ['id', 'bike', 'image']

    def to_internal_value(self, data):
        if 'image' in data:
            image = data['image']
            if isinstance(image, str) and image.startswith('data:image'):
                # Base64 encoded image
                format, imgstr = image.split(';base64,')  # Assumes format ~= data:image/X,
                ext = format.split('/')[-1]  # guess file extension
                id = uuid.uuid4()
                data = ContentFile(base64.b64decode(imgstr), name=f"{id}.{ext}")  # create a Django ContentFile
                data = super().to_internal_value({'bike': data['bike'], 'image': data})
                return data
            elif isinstance(image, str):
                # In case of an error in Base64 format, raise a validation error
                raise serializers.ValidationError("Invalid image format")
        return super().to_internal_value(data)

class BikeSerializer(serializers.ModelSerializer):
    channels = ChannelSerializer(many=True, read_only=True)
    bike_images = BikeImageSerializer(many=True)

    class Meta:
        model = Bike
        fields = ['id', 'brand', 'model', 'price', 'rating', 'release_date', 'description', 'channels', 'bike_images']

    def create(self, validated_data):
        bike_images_data = validated_data.pop('bike_images', [])
        bike = Bike.objects.create(**validated_data)
        for image_data in bike_images_data:
            BikeImage.objects.create(bike=bike, **image_data)
        return bike

    def update(self, instance, validated_data):
        bike_images_data = validated_data.pop('bike_images', [])
        # Update the bike instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Handle updating or adding new images
        for image_data in bike_images_data:
            image_id = image_data.get('id')
            if image_id:
                # Update existing image
                img = BikeImage.objects.get(id=image_id, bike=instance)
                img.image = image_data['image']
                img.save()
            else:
                # Create new image
                BikeImage.objects.create(bike=instance, **image_data)

        return instance

class BikeIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id']  # 只包含 id 字段

class ChannelIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id']  # 只包含 id 字段