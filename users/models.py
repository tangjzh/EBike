from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os

def user_head_path(instance, filename):
    return os.path.join(instance.username, 'avatar', filename)

class BikeUser(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    signature = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=user_head_path, null=True, blank=True)

    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=1, choices=(('M', '男'), ('F', '女'), ('O', '其他')), blank=True, verbose_name="性别")
    location = models.CharField(max_length=50, null=True, blank=True)

    following = models.ManyToManyField('self', related_name='followings', symmetrical=False, blank=True)
    follower = models.ManyToManyField('self', related_name='followers', symmetrical=False, blank=True)

    def __str__(self):
        return self.username

class VehiclePermit(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='vehicle_permit',
        verbose_name="用户"
    )
    permit_number = models.CharField(max_length=100, unique=True, verbose_name="通行证号")
    issued_date = models.DateField(null=True, blank=True, verbose_name="发行日期")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="过期日期")
    owner_name = models.CharField(max_length=150, null=True, blank=True, verbose_name="持有者姓名")

    def __str__(self):
        return f"{self.user.username} - {self.permit_number}"

    class Meta:
        verbose_name = "电动车通行证"
        verbose_name_plural = "电动车通行证"