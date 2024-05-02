from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Appointment

@receiver(post_save, sender=Appointment)
def appointment_status_change(sender, instance, created, **kwargs):
    # TODO: 添加短信通知和微信通知等，也可在前端加
    if not created and 'status' in instance.tracker.changed():
        user_email = instance.user.email
        subject = '预约状态更新通知'
        message = f'您的预约状态已更新为：{instance.get_status_display()}'
        send_mail(subject, message, 'from@example.com', [user_email])
