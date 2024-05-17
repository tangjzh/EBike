from rest_framework import serializers
from .models import VehiclePermit
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.files.uploadedfile import InMemoryUploadedFile

from django.utils import timezone
from django.core.files.base import ContentFile
import base64
import uuid

User = get_user_model()

class VehiclePermitSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiclePermit
        fields = ['permit_number', 'issued_date', 'expiry_date', 'owner_name']

    def create(self, validated_data):
        user = self.context['request'].user
        permit, created = VehiclePermit.objects.update_or_create(
            user=user,
            defaults=validated_data
        )
        return permit

class UserSerializer(serializers.ModelSerializer):
    vehicle_permit = VehiclePermitSerializer(read_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'telephone', 'nickname', 'signature', 'avatar', 'birthday', 'gender', 'vehicle_permit', 'following', 'follower']
        extra_kwargs = {'password': {'write_only': True}}

    def to_internal_value(self, data):
        # Check if the incoming data for the image is a string (base64)
        image = data.get('avatar', None)
        if isinstance(image, str) and image.startswith('data:image'):
            # Base64 encoded image
            format, imgstr = image.split(';base64,')  # format ~= data:image/X,
            ext = format.split('/')[-1]  # guess file extension
            id = uuid.uuid4()
            data = ContentFile(base64.b64decode(imgstr), name=f"{id}.{ext}")  # create a Django ContentFile
            data_dict = super().to_internal_value(data)
            data_dict['avatar'] = data
            return data_dict
        else:
            # Default file upload
            return super().to_internal_value(data)

    def validate_avatar(self, value):
        if value and not isinstance(value, InMemoryUploadedFile):
            raise serializers.ValidationError("Invalid type of file uploaded.")
        return value
    
    def get_avatar_url(self, obj):
        if obj.avatar:
            return obj.avatar.url
        return None

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['is_staff'] = self.user.is_staff

        self.user.last_login = timezone.now()
        self.user.save(update_fields=['last_login'])
        return data
