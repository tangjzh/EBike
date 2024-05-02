from rest_framework import serializers
from .models import ServiceShop, ServiceTip, Appointment

class ServiceShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceShop
        fields = '__all__'

class ServiceTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTip
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
