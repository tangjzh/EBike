from rest_framework import serializers
from .models import Goods

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = [
            'owner', 'hash', 'content', 'money', 'origin_money',
            'send_money', 'classify', 'edit_date'
        ]
        read_only_fields = ['edit_date']  # 设置只读字段