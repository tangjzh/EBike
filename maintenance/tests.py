from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import ServiceShop, ServiceTip, Appointment
from django.utils import timezone
from django.core import mail
from rest_framework import status
User = get_user_model()
from django.db import IntegrityError, DataError
from django.core.exceptions import ValidationError

from rest_framework.test import APIClient

class MaintenanceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='12345', email='test@example.com')
        # 配置JWT令牌认证
        self.auth_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0NjYyMTQ5LCJpYXQiOjE3MTQ2NjAzNDksImp0aSI6IjdiYzY1MzBkMGJiZDQ2YzU5NDg0MWNlZGJmYTI5NjUwIiwidXNlcl9pZCI6MX0.v4OJlPhjKibXzX2lt_WmVXoleFTOlFkZaJE1i2-9CaI'
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.auth_token}')
        
        self.shop = ServiceShop.objects.create(user=self.user, name="Test Shop", location="Test Location", service_description="Test Description", contact_info="Test Contact")
        self.appointment = Appointment.objects.create(
            user=self.user, 
            shop=self.shop, 
            service_type="Test Service", 
            appointment_time=timezone.now(), 
            status='pending'
        )
    def test_model_str(self):
        expected_str = f"{self.user.username} - {self.shop.name} - {self.appointment.appointment_time.strftime('%Y-%m-%d %H:%M')}"
        self.assertEqual(str(self.appointment), expected_str)

class ModelFieldTest(TestCase):
    def test_service_shop_fields(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        shop = ServiceShop(user=user, name='Test Shop', contact_info='1234567890')
        shop.save()
        self.assertEqual(shop.name, 'Test Shop')
        self.assertEqual(shop.user.email, 'test@example.com')

    def test_field_length_exceeded(self):
        shop = ServiceShop(name='x' * 300, contact_info='1234567890')
        with self.assertRaises(ValidationError):
             shop.full_clean()

class ModelRelationsTest(TestCase):
    def test_cascade_delete(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        shop = ServiceShop.objects.create(user=user, name='Test Shop')
        Appointment.objects.create(user=user, shop=shop, service_type='Repair', appointment_time=timezone.now())
        user.delete()
        self.assertEqual(ServiceShop.objects.count(), 0)
        self.assertEqual(Appointment.objects.count(), 0)
