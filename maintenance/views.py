from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import ServiceShop, ServiceTip, Appointment
from .serializers import ServiceShopSerializer, ServiceTipSerializer, AppointmentSerializer
from django.http import HttpResponse, JsonResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from EBike.utils import response

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class ServiceShopList(generics.ListCreateAPIView):
    queryset = ServiceShop.objects.all()
    serializer_class = ServiceShopSerializer

    @swagger_auto_schema(
        operation_description="获取所有服务商家",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": "user_id",
                                "name": "商家名称",
                                "location": "商家位置",
                                "service_description": "服务描述",
                                "contact_info": "联系信息"
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
            return response(True, data=self.list(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="创建新的服务商家",
        responses={
            201: openapi.Response(
                description="创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "name": "商家名称",
                            "location": "商家位置",
                            "service_description": "服务描述",
                            "contact_info": "联系信息"
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
            return response(True, data=self.create(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

class ServiceShopDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceShop.objects.all()
    serializer_class = ServiceShopSerializer

    @swagger_auto_schema(
        operation_description="获取指定的服务商家详情",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "name": "商家名称",
                            "location": "商家位置",
                            "service_description": "服务描述",
                            "contact_info": "联系信息"
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="商家未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "商家未找到"
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

    @swagger_auto_schema(
        operation_description="更新指定的服务商家信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "name": "更新后的商家名称",
                            "location": "更新后的商家位置",
                            "service_description": "更新后的服务描述",
                            "contact_info": "更新后的联系信息"
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
                description="商家未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "商家未找到"
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
        operation_description="部分更新指定的服务商家信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "name": "部分更新后的商家名称",
                            "location": "部分更新后的商家位置",
                            "service_description": "部分更新后的服务描述",
                            "contact_info": "部分更新后的联系信息"
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
                description="商家未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "商家未找到"
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
        operation_description="删除指定的服务商家",
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
                description="商家未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "商家未找到"
                    }
                }
            )
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return response(False, error=str(e))

class ServiceTipList(generics.ListCreateAPIView):
    queryset = ServiceTip.objects.all()
    serializer_class = ServiceTipSerializer

    @swagger_auto_schema(
        operation_description="获取所有服务提示",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "title": "提示标题",
                                "content": "提示内容",
                                "category": "提示类别"
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
            return response(True, data=self.list(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="创建新的服务提示",
        responses={
            201: openapi.Response(
                description="创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "title": "提示标题",
                            "content": "提示内容",
                            "category": "提示类别"
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
            return response(True, data=self.create(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

class ServiceTipDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTip.objects.all()
    serializer_class = ServiceTipSerializer

    @swagger_auto_schema(
        operation_description="获取指定的服务提示详情",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "title": "提示标题",
                            "content": "提示内容",
                            "category": "提示类别"
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="提示未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "提示未找到"
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

    @swagger_auto_schema(
        operation_description="更新指定的服务提示信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "title": "更新后的提示标题",
                            "content": "更新后的提示内容",
                            "category": "更新后的提示类别"
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
                description="提示未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "提示未找到"
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
        operation_description="部分更新指定的服务提示信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "title": "部分更新后的提示标题",
                            "content": "部分更新后的提示内容",
                            "category": "部分更新后的提示类别"
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
                description="提示未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "提示未找到"
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
        operation_description="删除指定的服务提示",
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
                description="提示未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "提示未找到"
                    }
                }
            )
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return response(False, error=str(e))

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_description="获取用户的所有预约",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "user": "user_id",
                                "shop": "shop_id",
                                "service_type": "服务类型",
                                "appointment_time": "2024-05-01T10:00:00Z",
                                "status": "pending",
                                "created_at": "2024-05-01T00:00:00Z",
                                "updated_at": "2024-05-01T00:00:00Z"
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
            return response(True, data=self.list(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    @swagger_auto_schema(
        operation_description="创建新的预约",
        responses={
            201: openapi.Response(
                description="创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "shop": "shop_id",
                            "service_type": "服务类型",
                            "appointment_time": "2024-05-01T10:00:00Z",
                            "status": "pending",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z"
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
            return response(True, data=self.create(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(user=user)

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    @swagger_auto_schema(
        operation_description="获取指定的预约详情",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "shop": "shop_id",
                            "service_type": "服务类型",
                            "appointment_time": "2024-05-01T10:00:00Z",
                            "status": "pending",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z"
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="预约未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "预约未找到"
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

    @swagger_auto_schema(
        operation_description="更新指定的预约信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "shop": "shop_id",
                            "service_type": "更新后的服务类型",
                            "appointment_time": "2024-05-01T10:00:00Z",
                            "status": "pending",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z"
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
                description="预约未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "预约未找到"
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
        operation_description="部分更新指定的预约信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "user": "user_id",
                            "shop": "shop_id",
                            "service_type": "部分更新后的服务类型",
                            "appointment_time": "2024-05-01T10:00:00Z",
                            "status": "pending",
                            "created_at": "2024-05-01T00:00:00Z",
                            "updated_at": "2024-05-01T00:00:00Z"
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
                description="预约未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "预约未找到"
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
        operation_description="删除指定的预约",
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
                description="预约未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "预约未找到"
                    }
                }
            )
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            self.destroy(request, *args, **kwargs)
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return response(False, error=str(e))
