from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from users.models import BikeUser, VehiclePermit
from users.serializers import UserSerializer, VehiclePermitSerializer
from rest_framework.test import APIClient
from rest_framework import status
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username= 'test',
            password='12345',
            email='test@example.com'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'test')
        self.assertTrue(self.user.check_password('12345'))
        self.assertEqual(self.user.email, 'test@example.com')

class VehiclePermitModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test',
            password='12345'
        )
        self.permit = VehiclePermit.objects.create(
            user=self.user,
            permit_number='ABC123',
            issued_date=timezone.now().date(),
            expiry_date=timezone.now().date()
        )

    def test_permit_creation(self):
        self.assertEqual(self.permit.permit_number, 'ABC123')
        self.assertEqual(self.permit.user, self.user)

class UserAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'username': 'test',
            'password': '12345',
            'email': 'test@example.com'
        }
        self.url = '/users/register/'

    def test_create_user(self):
        response = self.client.post(self.url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, 'test')

class UserInvalidDataTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create-user')

    def test_create_user_with_blank_username(self):
        user_data = {
            'username': ' ',  # 只有一个空格的用户名
            'password': '12345',
            'email': 'test@example.com'
        }
        response = self.client.post(self.url, user_data, format='json')
        self.assertNotEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('username', response.data)  # 检查错误消息中是否包含关于用户名的提示

class BikeUserModelTest(TestCase):
    def create_user(self, **kwargs):
        kwargs.setdefault('password', 'defaultpassword')  # 为所有用户设置默认密码
        return BikeUser.objects.create_user(**kwargs)  # 使用 create_user 而不是 create，以确保密码正确处理


    def test_nickname_length(self):
        nickname = 'x' * 50
        nickname_long = 'x' * 51
        user = self.create_user(username='user1', nickname=nickname)
        user.full_clean()  # 验证正常情况

        user_with_long_nickname = BikeUser(username='user2', nickname=nickname_long)
        with self.assertRaises(ValidationError):
            user_with_long_nickname.full_clean()

    

    def test_signature_length(self):
        signature = 'y' * 1000
        user = self.create_user(username='user3', signature=signature)
        self.assertEqual(user.signature, signature)

    def test_gender_choices(self):
        user = self.create_user(username='user4', gender='M')
        user.full_clean()  # 确认性别为 'M' 是有效的

        user_invalid = BikeUser(username='user5', gender='X')
        with self.assertRaises(ValidationError):
            user_invalid.full_clean()  # 确保性别为 'X' 时抛出错误


    def test_email_field(self):
        user = BikeUser(username='user6', email='valid@example.com', password='testpassword123')
        user.full_clean()  # This will validate the email field among others
        user.save()

    # Testing invalid email
        user_invalid = BikeUser(username='user7', email='invalid-email', password='testpassword123')
        with self.assertRaises(ValidationError):
             user_invalid.full_clean()


    def test_telephone_field(self):
        user = BikeUser(username='user8', telephone='12345678901', password='testpassword123')
        user.full_clean()
        user.save()

    # Manually testing telephone field length for SQLite
        user_with_long_telephone = BikeUser(username='user9', telephone='123456789012', password='testpassword123')
        with self.assertRaises(ValidationError):
             user_with_long_telephone.full_clean()  # Manually validate length if using SQLite


class VehiclePermitModelTest(TestCase):
    def setUp(self):
        self.user = BikeUser.objects.create(username='testuser', password='12345')
        self.permit_number = 'ABC123456'

    def test_owner_name_length(self):
        owner_name = 'x' * 150
        permit = VehiclePermit(user=self.user, permit_number='DIFF123', owner_name=owner_name)
        permit.save()  # 正常保存

        another_user = BikeUser.objects.create(username='anotheruser', password='12345')  # 创建另一个用户
        permit_with_long_name = VehiclePermit(user=another_user, permit_number='DIFF124', owner_name=owner_name)
        permit_with_long_name.save()  # 使用新用户保存



    def test_permit_number_unique(self):
        VehiclePermit.objects.create(user=self.user, permit_number=self.permit_number)
        with self.assertRaises(IntegrityError):
           VehiclePermit.objects.create(user=self.user, permit_number=self.permit_number)


