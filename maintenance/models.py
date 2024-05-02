from django.db import models
from django.contrib.auth import get_user_model
from model_utils.fields import MonitorField
from model_utils import FieldTracker

User = get_user_model()

# Create your models here.
class ServiceShop(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="商家用户")
    name = models.CharField(max_length=255, verbose_name="商家名称")
    location = models.CharField(max_length=255, verbose_name="位置", blank=True, null=True)
    service_description = models.TextField(verbose_name="服务描述", blank=True, null=True)
    contact_info = models.CharField(max_length=255, verbose_name="联系信息")

    def __str__(self):
        return self.name
    
class ServiceTip(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    category = models.CharField(max_length=100, verbose_name="类别", blank=True, null=True)

    def __str__(self):
        return f"{self.category} - {self.title}" if self.category else self.title
    
class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', '待确认'),
        ('check_in', '已接单'),
        ('in_progress', '进行中'),
        ('completed', '已完成')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    shop = models.ForeignKey(ServiceShop, related_name='appointments', on_delete=models.CASCADE, verbose_name="服务商家")
    service_type = models.CharField(max_length=255, verbose_name="服务类型")
    appointment_time = models.DateTimeField(verbose_name="预约时间")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending', verbose_name="状态")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    status_changed = MonitorField(monitor='status')
    tracker = FieldTracker()

    def __str__(self):
        return f"{self.user.username} - {self.shop.name} - {self.appointment_time.strftime('%Y-%m-%d %H:%M')}"