from django.test import TestCase

# Create your tests here.
from django.contrib.auth import get_user_model
from .models import Goods
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Goods
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class GoodsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # 创建用户和商品数据
        user = User.objects.create_user(username='testuser', password='12345')
        cls.goods = Goods.objects.create(
            owner=user,
            hash='123456abcdef',  # 注意这里的哈希值
            content='测试商品内容',
            money='100',
            origin_money='120',
            send_money='10',
            classify='电子产品'
        )

    def test_content_field(self):
        goods = Goods.objects.get(hash='123456abcdef')  # 使用正确的哈希值
        field_label = goods._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_money_field(self):
        goods = Goods.objects.get(hash='123456abcdef')
        self.assertEqual(goods.money, '100')  # 注意这里的预期值也需要对应正确

    def test_owner(self):
        goods = Goods.objects.get(hash='123456abcdef')
        self.assertEqual(goods.owner.username, 'testuser')



class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.goods = Goods.objects.create(
            owner=self.user,
            hash='123456abcdef',
            content='good job',
            money='100',
            origin_money='150',
            send_money='10',
            classify='Electronics'
        )
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    def test_publish_view(self):
        # 测试发布商品视图
        url = reverse('shop:publish')
        data = {
            'content': 'good job',
            'money': '100',
            'origin_money': '150',
            'send_money': '10',
            'classify': 'Electronics',
        }
        with open('exchange/test.jpg', 'rb') as img:
            data['image'] = img
            response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, 201)
