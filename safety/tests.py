from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Report
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone

class ReportModelTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_create_report(self):
        report = Report.objects.create(
            user=self.user,
            location='测试位置',
            description='测试违规详情',
            timestamp=timezone.now(),
            status='pending'
        )
        self.assertEqual(str(report), f"{report.location} - {report.status}")

class ReportViewsTest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.report = Report.objects.create(
            user=self.user,
            location='测试位置',
            description='测试违规详情',
            timestamp=timezone.now(),
            status='pending'
        )

    def test_report_list_view(self):
        response = self.client.get(reverse('report-create-or-update'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # 检查是否返回了一个报告列表

    def test_report_detail_view(self):
        url = reverse('report-detail', args=[self.report.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['location'], '测试位置')

class ReportAPITest(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_report(self):
        url = reverse('report-create-or-update')
        data = {
            'user': self.user.id,
            'location': '新测试位置',
            'description': '新违规详情',
            'timestamp': timezone.now(),
            'status': 'pending'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Report.objects.count(), 1)
        self.assertEqual(Report.objects.first().location, '新测试位置')

