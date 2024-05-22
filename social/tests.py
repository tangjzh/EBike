from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import User, Post, Comment, Interaction
from .serializers import PostSerializer, CommentSerializer

class SocialAppTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
    def test_create_and_retrieve_post(self):
        """
        测试创建帖子和检索帖子的功能
        """
        url = reverse('social:post-create')
        data = {'title': 'New Post', 'content': 'Content of the new post', 'tags': [], 'images': [], 'location': "Anywhere"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(response.data['title'], 'New Post')

        # 测试获取帖子
        response = self.client.get(reverse('social:post-edit', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Post')
    def test_add_and_retrieve_comment(self):
        """
        测试添加评论和获取评论的功能
        """
        url = reverse('social:comment-create')
        data = {'post': self.post.id, 'content': 'Great post!'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 2)
        self.assertEqual(response.data['content'], 'Great post!')

        # 获取评论
        response = self.client.get(reverse('social:comment-edit', kwargs={'pk': self.comment.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['content'], 'Nice post!')


    def setUp(self):
    # 建立API客户端和认证
        self.client = APIClient()
    # 模拟登录以获得token
        response = self.client.post('/users/login/', {'username': 'testuser', 'password': 'test123'}, format='json')
        token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)

    # 创建测试帖子
        self.post = Post.objects.create(user=self.user, title="Test Post", content="Hello world!", tags=[], images=[], location="Somewhere")
        self.comment = Comment.objects.create(user=self.user, post=self.post, content="Nice post!")
