from rest_framework import generics, permissions
from rest_framework import status
from .models import Post, Comment, Interaction, Follow
from .serializers import PostSerializer, CommentSerializer, InteractionSerializer, ToggleFollowSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer
import operator
from functools import reduce
from haystack.query import EmptySearchQuerySet
from django.conf import settings
from haystack.views import SearchView
from haystack.forms import ModelSearchForm
from django.http import Http404
from django.http import JsonResponse
from django.core.paginator import InvalidPage, Paginator
from drf_yasg.utils import swagger_auto_schema
from EBike.utils import response
from rest_framework.pagination import PageNumberPagination
from drf_yasg import openapi
from rest_framework.decorators import permission_classes as permission_dec

class HomePagePagination(PageNumberPagination):
    page_size = 10  # 每页的项目数
    page_size_query_param = 'page_size'
    max_page_size = 100  # 每页的最大项目数

class PostCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_description="创建车小圈帖子",
        responses={
            201: openapi.Response(
                description="帖子创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": 1,
                            "title": "新帖子标题",
                            "content": "帖子内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z",
                            "tags": [],
                            "location": "",
                            "likes_count": 0,
                            "views_count": 0
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"title": ["This field is required."]}
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        try:
            return response(True, data=self.create(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))
    
    @swagger_auto_schema(
        operation_description="获取所有车小圈帖子",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": 1,
                                "title": "帖子标题",
                                "content": "帖子内容",
                                "created_at": "2024-05-01T00:00:00Z",
                                "updated_at": "2024-05-01T00:00:00Z",
                                "tags": [],
                                "location": "",
                                "likes_count": 0,
                                "views_count": 0
                            }
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    @permission_dec(permissions.AllowAny)
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class HomePageListView(generics.ListAPIView):
    pagination_class = HomePagePagination
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="获取首页的车小圈帖子，支持指定页码",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": 1,
                                "title": "帖子标题",
                                "content": "帖子内容",
                                "created_at": "2024-05-01T00:00:00Z",
                                "updated_at": "2024-05-01T00:00:00Z",
                                "tags": [],
                                "location": "",
                                "likes_count": 0,
                                "views_count": 0
                            }
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    @permission_dec(permissions.AllowAny)
    def get(self, request, *args, **kwargs):
        gtype = request.GET.get('order_by', '-views_count')

        try:
            queryset = Post.objects.order_by(gtype).all()
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = PostSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)  # 使用分页响应

            serializer = PostSerializer(queryset, many=True)
            return response(True, data=serializer.data)
        except Exception as e:
            return response(False, error=str(e))

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_description="获取指定的车小圈帖子",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": 1,
                            "title": "帖子标题",
                            "content": "帖子内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z",
                            "tags": [],
                            "location": "",
                            "likes_count": 0,
                            "views_count": 0
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="帖子未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "帖子未找到"
                    }
                }
            )
        }
    )
    @permission_dec(permissions.AllowAny)
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.retrieve(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="更新指定的车小圈帖子",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": 1,
                            "title": "更新后的帖子标题",
                            "content": "更新后的帖子内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z",
                            "tags": [],
                            "location": "",
                            "likes_count": 0,
                            "views_count": 0
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            ),
            404: openapi.Response(
                description="帖子未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "帖子未找到"
                    }
                }
            )
        }
    )
    def put(self, request, *args, **kwargs):
        try:
            return response(True, data=self.update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="部分更新指定的车小圈帖子",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": 1,
                            "title": "部分更新后的帖子标题",
                            "content": "部分更新后的帖子内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z",
                            "tags": [],
                            "location": "",
                            "likes_count": 0,
                            "views_count": 0
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            ),
            404: openapi.Response(
                description="帖子未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "帖子未找到"
                    }
                }
            )
        }
    )
    def patch(self, request, *args, **kwargs):
        try:
            return response(True, data=self.partial_update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="删除指定的车小圈帖子",
        responses={
            204: openapi.Response(
                description="删除成功",
                examples={
                    "application/json": {
                        "success": True
                    }
                }
            ),
            404: openapi.Response(
                description="帖子未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "帖子未找到"
                    }
                }
            )
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return response(True)
        except Exception as e:
            return response(False, error=str(e))

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class UserPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_description="获取用户发布过的帖子",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": 1,
                                "title": "用户的帖子标题",
                                "content": "用户的帖子内容",
                                "created_at": "2024-05-01T00:00:00Z",
                                "updated_at": "2024-05-01T00:00:00Z",
                                "tags": [],
                                "location": "",
                                "likes_count": 0,
                                "views_count": 0
                            }
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user=user)

class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @swagger_auto_schema(
        operation_description="获取所有评论",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "post": 1,
                                "user": 1,
                                "content": "评论内容",
                                "created_at": "2024-05-01T00:00:00Z",
                                "likes_count": 0
                            }
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    @permission_dec(permissions.AllowAny)
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))
        
    @swagger_auto_schema(
        operation_description="为帖子创建新评论",
        responses={
            201: openapi.Response(
                description="评论创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "post": 1,
                            "user": 1,
                            "content": "新评论内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "likes_count": 0
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        try:
            return response(True, data=self.create(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_description="获取指定的车小圈帖子评论",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "post": 1,
                            "user": 1,
                            "content": "评论内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "likes_count": 0
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="评论未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "评论未找到"
                    }
                }
            )
        }
    )
    @permission_dec(permissions.AllowAny)
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.retrieve(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="更新指定的车小圈帖子评论",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "post": 1,
                            "user": 1,
                            "content": "更新后的评论内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "likes_count": 0
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            ),
            404: openapi.Response(
                description="评论未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "评论未找到"
                    }
                }
            )
        }
    )
    def put(self, request, *args, **kwargs):
        try:
            return response(True, data=self.update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="部分更新指定的车小圈帖子评论",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "post": 1,
                            "user": 1,
                            "content": "部分更新后的评论内容",
                            "created_at": "2024-05-01T00:00:00Z",
                            "likes_count": 0
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            ),
            404: openapi.Response(
                description="评论未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "评论未找到"
                    }
                }
            )
        }
    )
    def patch(self, request, *args, **kwargs):
        try:
            return response(True, data=self.partial_update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="删除指定的车小圈帖子评论",
        responses={
            204: openapi.Response(
                description="删除成功",
                examples={
                    "application/json": {
                        "success": True
                    }
                }
            ),
            404: openapi.Response(
                description="评论未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "评论未找到"
                    }
                }
            )
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return response(True)
        except Exception as e:
            return response(False, error=str(e))

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class InteractionToggleView(APIView):
    @swagger_auto_schema(
        operation_description="修改当前用户对特定帖子点赞/收藏状态",
        responses={
            201: openapi.Response(
                description="操作成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "user": 1,
                            "post": 1,
                            "type": "like"
                        }
                    }
                }
            ),
            204: openapi.Response(
                description="操作取消",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "interaction removed"
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = InteractionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            interaction_type = serializer.validated_data.get('type')
            post = serializer.validated_data.get('post')
            interaction, created = Interaction.objects.get_or_create(
                user=request.user, post=post, type=interaction_type,
                defaults={'type': interaction_type}
            )
            if not created:
                # If the interaction exists, we toggle it by deleting
                interaction.delete()
                return response(False, error='interaction removed', status=status.HTTP_204_NO_CONTENT)
            return response(True, data=serializer.data, status=status.HTTP_201_CREATED)
        return response(False, error=serializer.errors)

class InteractionCountView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(
        operation_description="获取特定帖子的点赞/收藏数量",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "likes_count": 10,
                            "favorites_count": 5
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = InteractionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            post_id = serializer.validated_data.get('post')
            likes_count = Interaction.objects.filter(post_id=post_id, type='like').count()
            favorites_count = Interaction.objects.filter(post_id=post_id, type='favorite').count()
            return response(True, data={
                'likes_count': likes_count,
                'favorites_count': favorites_count
            })
        return response(False, error=serializer.errors)

class UserFavoritesListView(generics.ListAPIView):
    serializer_class = InteractionSerializer

    @swagger_auto_schema(
        operation_description="获取当前用户的所有收藏过的帖子",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": 1,
                                "title": "收藏的帖子标题",
                                "content": "收藏的帖子内容",
                                "created_at": "2024-05-01T00:00:00Z",
                                "updated_at": "2024-05-01T00:00:00Z",
                                "tags": [],
                                "location": "",
                                "likes_count": 0,
                                "views_count": 0
                            }
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))

    def get_queryset(self):
        user = self.request.user
        favorited_posts_ids = Interaction.objects.filter(user=user, type='favorite').values_list('post', flat=True)
        return Post.objects.filter(id__in=favorited_posts_ids)

class UserLikeListView(generics.ListAPIView):
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_description="获取当前用户的所有点赞过的帖子",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": 1,
                                "title": "点赞的帖子标题",
                                "content": "点赞的帖子内容",
                                "created_at": "2024-05-01T00:00:00Z",
                                "updated_at": "2024-05-01T00:00:00Z",
                                "tags": [],
                                "location": "",
                                "likes_count": 0,
                                "views_count": 0
                            }
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs))
        except Exception as e:
            return response(False, error=str(e))

    def get_queryset(self):
        user = self.request.user
        favorited_posts_ids = Interaction.objects.filter(user=user, type='like').values_list('post', flat=True)
        return Post.objects.filter(id__in=favorited_posts_ids)

class ToggleFollowView(generics.CreateAPIView):
    serializer_class = ToggleFollowSerializer

    @swagger_auto_schema(
        operation_description="修改当前用户对另一用户的关注状态",
        responses={
            200: openapi.Response(
                description="操作成功",
                examples={
                    "application/json": {
                        "status": "followed",
                        "user": "other_user"
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = ToggleFollowSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user, action = serializer.save()
            return Response({'status': action, 'user': user.username}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomListView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="获取当前用户所在的聊天室列表",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": "room_id",
                                "name": "聊天室名称",
                                "type": "聊天室类型",
                                "participants": ["user1", "user2"],
                                "created_at": "2024-05-01T00:00:00Z"
                            }
                        ]
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.chat_rooms.all()

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="获取指定聊天室的详细信息",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "room_id",
                            "name": "聊天室名称",
                            "type": "聊天室类型",
                            "participants": ["user1", "user2"],
                            "created_at": "2024-05-01T00:00:00Z"
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="聊天室未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "聊天室未找到"
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    @swagger_auto_schema(
        operation_description="在指定聊天室中发送消息",
        responses={
            201: openapi.Response(
                description="消息发送成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "message_id",
                            "room": "room_id",
                            "sender": "user1",
                            "content": "消息内容",
                            "timestamp": "2024-05-01T00:00:00Z"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

RESULTS_PER_PAGE = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 20)

class MySearchView(SearchView):
    extra_context = {}
    query = ''
    results = EmptySearchQuerySet()
    request = None
    form = None
    results_per_page = RESULTS_PER_PAGE

    def __init__(self, template=None, load_all=True, form_class=None, searchqueryset=None, results_per_page=None):
        self.load_all = load_all
        self.form_class = form_class
        self.searchqueryset = searchqueryset

        if form_class is None:
            self.form_class = ModelSearchForm

        if not results_per_page is None:
            self.results_per_page = results_per_page

    def __call__(self, request):
        """
        Generates the actual response to the search.

        Relies on internal, overridable methods to construct the response.
        """
        self.request = request

        self.form = self.build_form()
        self.query = self.get_query()
        self.results = self.get_results()

        return self.create_response()

    def build_form(self, form_kwargs=None):
        """
        Instantiates the form the class should use to process the search query.
        """
        data = None
        kwargs = {
            'load_all': self.load_all,
        }
        if form_kwargs:
            kwargs.update(form_kwargs)

        if len(self.request.POST):
            data = self.request.POST

        if self.searchqueryset is not None:
            kwargs['searchqueryset'] = self.searchqueryset

        return self.form_class(data, **kwargs)

    def get_query(self):
        """
        Returns the query provided by the user.

        Returns an empty string if the query is invalid.
        """
        if self.form.is_valid():
            return self.form.cleaned_data['q']

        return ''

    def get_results(self):
        """
        Fetches the results via the form.

        Returns an empty list if there's no query to search with.
        """
        return self.form.search()

    def build_page(self):
        """
        Paginates the results appropriately.

        In case someone does not want to use Django's built-in pagination, it
        should be a simple matter to override this method to do what they would
        like.
        """
        try:
            page_no = int(self.request.POST.get('page', 1))
        except (TypeError, ValueError):
            raise Http404("Not a valid number for page.")

        if page_no < 1:
            raise Http404("Pages should be 1 or greater.")

        start_offset = (page_no - 1) * self.results_per_page
        self.results[start_offset:start_offset + self.results_per_page]

        paginator = Paginator(self.results, self.results_per_page)

        try:
            page = paginator.page(page_no)
        except InvalidPage:
            raise Http404("No such page!")

        return (paginator, page)

    def extra_context(self):
        """
        Allows the addition of more context variables as needed.

        Must return a dictionary.
        """
        return {}

    def get_context(self):
        (paginator, page) = self.build_page()

        context = {
            'query': self.query,
            'form': self.form,
            'page': page,
            'paginator': paginator,
            'suggestion': None,
        }

        if hasattr(self.results, 'query') and self.results.query.backend.include_spelling:
            context['suggestion'] = self.form.get_suggestion()

        context.update(self.extra_context())

        return context

    def create_response(self):
        """
        Generates the actual HttpResponse to send back to the user.
        """
        try:

            context = self.get_context()

            ret = []
            for result in context['paginator'].object_list:
                post = result._object
                image_url = str(post.postimage_set.all()[0].image)

                a = {
                    "post_id": post.id,
                    "image": image_url,
                    "title": post.title,
                    "content": post.content,
                    "username": post.user.username,
                    "tags": post.tags,
                    "likes_count": post.likes_count,
                    "views_count": post.views_count,
                    "time": post.updated_at,
                }
                ret.append(a)

            if self.request.POST['method'] == '1':
                run_function = lambda x, y: x if y in x else x + [y]
                ret = reduce(run_function, [[], ] + ret)
                ret.sort(key=operator.itemgetter('time'))
            elif self.request.POST['method'] == '2':
                run_function = lambda x, y: x if y in x else x + [y]
                ret = reduce(run_function, [[], ] + ret)
                ret.sort(key=operator.itemgetter('time'), reverse=True)
            ret = ret[(int(self.request.POST['page']) - 1) * RESULTS_PER_PAGE:
                    int(self.request.POST['page']) * RESULTS_PER_PAGE]
            ret.append({"max_page": context['paginator'].num_pages, })
            return response(True, data=ret)
        except Exception as e:
            return response(False, error=str(e))
