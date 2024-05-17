from django.test import TestCase

# Create your tests here.

from bike_info.models import Bike, BikeImage, Channel
from django.test import TestCase
from django.utils import timezone
import datetime
from datetime import date
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.exceptions import ValidationError
from django.db import DataError, IntegrityError

class BikeModelTest(TestCase):
    def setUp(self):
        # 创建一个 Bike 实例，将品牌名称设为 "雅迪"
        self.bike = Bike.objects.create(
            brand="雅迪",
            model="Emonda",
            price="999.99",
            rating=4.5,
            release_date=datetime.date.today(),
            description="Lightweight road bike."
        )

    def test_str_representation(self):
        # 测试 __str__ 方法返回的字符串是否为 "雅迪 - 999.99"
        self.assertEqual(str(self.bike), "雅迪 - 999.99")

    def test_bike_creation(self):
        # 测试创建的 Bike 实例是否正确
        self.assertTrue(isinstance(self.bike, Bike))
        self.assertEqual(self.bike.brand, "雅迪")

class BikeImageModelTest(TestCase):
    def setUp(self):
        # 在 BikeImageModelTest 中也使用品牌名 "雅迪"，如果需要
        self.bike = Bike.objects.create(
            brand="雅迪",
            model="Allez",
            price="1200.00",
            rating=4.7,
            release_date=datetime.date.today(),
            description="Entry-level race bike."
        )
        self.bike_image = BikeImage.objects.create(
            bike=self.bike,
            image='test.jpg'  # Use a simple path for the test; handling actual images is not needed
        )

    def test_str_representation(self):
        # 测试 __str__ 方法返回的字符串是否为 "雅迪 - Image"
        self.assertEqual(str(self.bike_image), "雅迪 - Image")
