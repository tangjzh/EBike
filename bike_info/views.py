from django.shortcuts import render
from rest_framework import generics
from .models import Bike, Channel, BikeImage
from .serializers import BikeSerializer, ChannelSerializer, BikeIDSerializer, ChannelIDSerializer, BikeImageSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .filters import BikeFilter
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from EBike.utils import response

class BikeIDListView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeIDSerializer

    @swagger_auto_schema(
        operation_description="获取所有电动车ID列表",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {"id": 1},
                            {"id": 2}
                        ]
                    }
                }
            ),
            400: openapi.Response(
                description="获取失败",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "错误信息"
                    }
                }
            ),
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            return response(True, data=self.list(request, *args, **kwargs).data)
        except Exception as e:
            return response(False, error=str(e))

class BikeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

    @swagger_auto_schema(
        operation_description="获取指定电动车的详细信息",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "brand": "品牌",
                            "model": "型号",
                            "price": "价格",
                            "rating": "评价",
                            "release_date": "上市日期",
                            "description": "描述"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="获取失败",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Bike not found."
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
        operation_description="更新指定电动车的信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "brand": "更新后的品牌",
                            "model": "更新后的型号",
                            "price": "更新后的价格",
                            "rating": "更新后的评价",
                            "release_date": "更新后的上市日期",
                            "description": "更新后的描述"
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
                description="电动车未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Bike not found."
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
        operation_description="部分更新指定电动车的信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "brand": "部分更新后的品牌",
                            "model": "部分更新后的型号",
                            "price": "部分更新后的价格",
                            "rating": "部分更新后的评价",
                            "release_date": "部分更新后的上市日期",
                            "description": "部分更新后的描述"
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
                description="电动车未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Bike not found."
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
        operation_description="删除指定电动车",
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
                description="电动车未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Bike not found."
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

class BikeListView(generics.ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    parser_classes = [MultiPartParser, JSONParser]
    filterset_class = BikeFilter
    ordering_fields = ['price', 'rating', 'release_date']

    @swagger_auto_schema(
        operation_description="获取所有电动车的列表",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "brand": "品牌",
                                "model": "型号",
                                "price": "价格",
                                "rating": "评价",
                                "release_date": "上市日期",
                                "description": "描述"
                            }
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

    @swagger_auto_schema(
        operation_description="创建新的电动车",
        responses={
            201: openapi.Response(
                description="创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "brand": "品牌",
                            "model": "型号",
                            "price": "价格",
                            "rating": "评价",
                            "release_date": "上市日期",
                            "description": "描述"
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

class ChannelIDListView(generics.ListAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelIDSerializer

    @swagger_auto_schema(
        operation_description="获取所有渠道ID列表",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {"id": 1},
                            {"id": 2}
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

class ChannelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    @swagger_auto_schema(
        operation_description="获取所有渠道的列表",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": 1,
                                "name": "渠道名称",
                                "url": "购买链接",
                                "service_info": "服务信息"
                            }
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

    @swagger_auto_schema(
        operation_description="创建新的渠道",
        responses={
            201: openapi.Response(
                description="创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "name": "渠道名称",
                            "url": "购买链接",
                            "service_info": "服务信息"
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

class ChannelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    @swagger_auto_schema(
        operation_description="获取指定渠道的详细信息",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "name": "渠道名称",
                            "url": "购买链接",
                            "service_info": "服务信息"
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="渠道未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Channel not found."
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
        operation_description="更新指定渠道的信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "name": "更新后的渠道名称",
                            "url": "更新后的购买链接",
                            "service_info": "更新后的服务信息"
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
                description="渠道未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Channel not found."
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
        operation_description="部分更新指定渠道的信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "name": "部分更新后的渠道名称",
                            "url": "部分更新后的购买链接",
                            "service_info": "部分更新后的服务信息"
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
                description="渠道未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Channel not found."
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
        operation_description="删除指定渠道",
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
                description="渠道未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Channel not found."
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

class BikeImageCreateView(generics.CreateAPIView):
    queryset = BikeImage.objects.all()
    serializer_class = BikeImageSerializer
    parser_classes = [MultiPartParser, JSONParser]

    @swagger_auto_schema(
        operation_description="创建电动车图片",
        responses={
            201: openapi.Response(
                description="创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": 1,
                            "bike": 1,
                            "image": "image_url"
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

class BikeImageDeleteView(generics.DestroyAPIView):
    queryset = BikeImage.objects.all()
    serializer_class = BikeImageSerializer
    lookup_field = 'id'

    @swagger_auto_schema(
        operation_description="删除电动车图片",
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
                description="图片未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Bike image not found."
                    }
                }
            )
        }
    )
    def delete(self, request, *args, **kwargs):
        try:
            bike_image = self.get_object()
            bike_image.image.delete()  # 删除文件
            self.perform_destroy(bike_image)
            return response(True, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return response(False, error=str(e))
