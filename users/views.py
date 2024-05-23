from django.shortcuts import render
from rest_framework import status, views
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, VehiclePermitSerializer, MyTokenObtainPairSerializer
from django.contrib.auth import get_user_model
from .models import VehiclePermit
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from EBike.utils import response

User = get_user_model()

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="创建新用户",
        responses={
            201: openapi.Response(
                description="用户创建成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "new_user",
                            "email": "new_user@example.com",
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"username": ["This field is required."]}
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(True, data=serializer.data, status=status.HTTP_201_CREATED)
        return response(False, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="用户登录获取JWT",
        responses={
            200: openapi.Response(
                description="登录成功",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'results': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                                'access': openapi.Schema(type=openapi.TYPE_STRING),
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "refresh": "string",
                            "access": "string"
                        }
                    }
                }
            ),
            401: openapi.Response(
                description="认证失败",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": "No active account found with the given credentials"
                    }
                }
            ),
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserDeleteAPIView(APIView):

    @swagger_auto_schema(
        operation_description="删除用户",
        responses={
            204: openapi.Response(
                description="用户删除成功",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    }
                ),
                examples={
                    "application/json": {
                        "success": True
                    }
                }
            ),
            404: openapi.Response(
                description="用户未找到",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": "User not found"
                    }
                }
            ),
        }
    )
    def delete(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return response(False, error="User not found", status=status.HTTP_404_NOT_FOUND)

class UserProfileListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="获取所有用户的列表",
        responses={
            200: openapi.Response(
                description="获取成功",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'results': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": True,
                        "results": [
                            {
                                "id": 1,
                                "username": "user1",
                                "email": "user1@example.com",
                            },
                            {
                                "id": 2,
                                "username": "user2",
                                "email": "user2@example.com",
                            },
                        ]
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(
        operation_description="获取指定用户的详细信息",
        responses={
            200: openapi.Response(
                description="获取成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "user1",
                            "email": "user1@example.com",
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="用户未找到",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": "User not found"
                    }
                }
            ),
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.retrieve(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="更新指定用户的详细信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "updated_user",
                            "email": "updated_user@example.com",
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"username": ["This field is required."]}
                    }
                }
            ),
        }
    )
    def put(self, request, *args, **kwargs):
        try:
            return response(True, data=self.update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="部分更新指定用户的详细信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "updated_user",
                            "email": "updated_user@example.com",
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"username": ["This field is required."]}
                    }
                }
            ),
        }
    )
    def patch(self, request, *args, **kwargs):
        try:
            return response(True, data=self.partial_update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="删除指定用户",
        responses={
            204: openapi.Response(
                description="删除成功",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    }
                ),
                examples={
                    "application/json": {
                        "success": True
                    }
                }
            ),
            404: openapi.Response(
                description="用户未找到",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": "User not found"
                    }
                }
            ),
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return response(False, error=str(e))

class UpdateUserProfileView(generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        operation_description="更新当前用户的资料",
        responses={
            200: openapi.Response(
                description="更新成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "updated_user",
                            "email": "updated_user@example.com",
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"username": ["This field is required."]}
                    }
                }
            ),
        }
    )
    def put(self, request, *args, **kwargs):
        try:
            return response(True, data=self.update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="部分更新当前用户的资料",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "updated_user",
                            "email": "updated_user@example.com",
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"username": ["This field is required."]}
                    }
                }
            ),
        }
    )
    def patch(self, request, *args, **kwargs):
        try:
            return response(True, data=self.partial_update(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

class RetrieveUserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        operation_description="获取当前用户的资料",
        responses={
            200: openapi.Response(
                description="获取成功",
                schema=UserSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "username": "user1",
                            "email": "user1@example.com",
                        }
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.retrieve(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

class BindPermitView(generics.CreateAPIView):
    serializer_class = VehiclePermitSerializer

    @swagger_auto_schema(
        operation_description="绑定用户车辆通行证信息",
        responses={
            201: openapi.Response(
                description="绑定成功",
                schema=VehiclePermitSerializer,
                examples={
                    "application/json": {
                        "success": True,
                        "results": {
                            "id": 1,
                            "user": 1,
                            "permit_number": "12345",
                            "valid_from": "2024-01-01",
                            "valid_to": "2024-12-31"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'permit_number': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING))
                            }
                        )
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": {"permit_number": ["This field is required."]}
                    }
                }
            ),
        }
    )
    def post(self, request):
        serializer = VehiclePermitSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return response(True, data=serializer.data, status=status.HTTP_201_CREATED)
        return response(False, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnbindPermitView(views.APIView):
    @swagger_auto_schema(
        operation_description="解绑用户车辆通行证信息",
        responses={
            204: openapi.Response(
                description="解绑成功",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    }
                ),
                examples={
                    "application/json": {
                        "success": True
                    }
                }
            ),
            404: openapi.Response(
                description="通行证未找到",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'success': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                ),
                examples={
                    "application/json": {
                        "success": False,
                        "error": "No permit found to unbind"
                    }
                }
            ),
        }
    )
    def delete(self, request):
        user = request.user
        try:
            permit = VehiclePermit.objects.get(user=user)
            permit.delete()
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except VehiclePermit.DoesNotExist:
            return response(False, error="No permit found to unbind", status=status.HTTP_404_NOT_FOUND)
