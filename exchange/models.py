from django.db import models

# Create your models here.
import os
from django.contrib.auth import get_user_model

User = get_user_model()

def user_goods_path(instance, filename):
    return os.path.join('user', instance.goods.owner.username, 'goods', str(instance.goods.hash), filename)

class Goods(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hash = models.CharField(max_length=32, primary_key=True)  # 设置为主键
    content = models.CharField(max_length=300, db_index=True)
    money = models.CharField(max_length=10)
    origin_money = models.CharField(max_length=10)
    send_money = models.CharField(max_length=10)
    classify = models.CharField(max_length=200)
    edit_date = models.DateTimeField(auto_now=True, db_index=True)  # 编辑日期


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    image = models.ImageField(default='', upload_to=user_goods_path, blank=True, null=True)