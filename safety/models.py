from django.db import models

# Create your models here.
from django.utils import timezone
import os
import uuid
from django.contrib.auth import get_user_model

User = get_user_model()

def report_path(instance, filename):
    return os.path.join('report', instance.id, filename)

class Report(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporter')
    location = models.CharField(max_length=255, verbose_name="位置")
    description = models.TextField(verbose_name="违规详情")
    timestamp = models.DateTimeField(default=timezone.now, verbose_name="提交时间")
    STATUS_CHOICES = (
        ('pending', '未处理'),
        ('in_progress', '处理中'),
        ('resolved', '已处理')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="状态")
    image = models.ImageField(upload_to='reports/', blank=True, null=True, verbose_name="现场图片")

    def __str__(self):
        return f"{self.location} - {self.status}"

    class Meta:
        verbose_name = "举报"
        verbose_name_plural = "举报"