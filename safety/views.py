from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer
from rest_framework import generics
import base64
from django.core.files.base import ContentFile
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from EBike.utils import response

class ReportAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    @swagger_auto_schema(
        operation_description="创建或更新举报报告",
        responses={
            200: openapi.Response(
                description="报告更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "report_id",
                            "user": "user_id",
                            "location": "报告位置",
                            "description": "报告详情",
                            "timestamp": "2024-05-01T00:00:00Z",
                            "status": "pending",
                            "image": None
                        }
                    }
                }
            ),
            201: openapi.Response(
                description="报告创建成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "report_id",
                            "user": "user_id",
                            "location": "报告位置",
                            "description": "报告详情",
                            "timestamp": "2024-05-01T00:00:00Z",
                            "status": "pending",
                            "image": None
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
        data = request.data
        report_id = data.get('id', None)  # 假设报告的唯一标识符是传递的ID
        
        image_data = data.get('image')
        if image_data:
            image_file = self.handle_image(image_data)
            if image_file:
                data['image'] = image_file

        if report_id:
            # 尝试查找现有报告
            report, created = Report.objects.update_or_create(
                id=report_id,
                defaults={
                    'location': data.get('location'),
                    'description': data.get('description'),
                    'status': data.get('status', 'pending'),
                    'image': data.get('image', None)  # 注意处理文件或图片字段可能需要额外的逻辑
                }
            )
        else:
            # 创建新的报告
            serializer = ReportSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return response(True, data=serializer.data, status=status.HTTP_201_CREATED)
            return response(False, error=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return response(True, data=ReportSerializer(report).data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_description="获取所有举报报告",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "id": "report_id",
                                "user": "user_id",
                                "location": "报告位置",
                                "description": "报告详情",
                                "timestamp": "2024-05-01T00:00:00Z",
                                "status": "pending",
                                "image": None
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

    def handle_image(self, image_data):
        # 检查是否是base64编码
        if 'data:image' in image_data and ';base64,' in image_data:
            format, imgstr = image_data.split(';base64,')  # 分割数据格式和实际图片数据
            ext = format.split('/')[-1]  # 获取图片扩展名
            image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # 解码并转换为图片文件
            return image
        return None

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'  # 使用报告的主键作为查找字段

    @swagger_auto_schema(
        operation_description="获取指定举报报告的详细信息",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "report_id",
                            "user": "user_id",
                            "location": "报告位置",
                            "description": "报告详情",
                            "timestamp": "2024-05-01T00:00:00Z",
                            "status": "pending",
                            "image": None
                        }
                    }
                }
            ),
            404: openapi.Response(
                description="报告未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "报告未找到"
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
        operation_description="更新指定举报报告的信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "report_id",
                            "user": "user_id",
                            "location": "更新后的报告位置",
                            "description": "更新后的报告详情",
                            "timestamp": "2024-05-01T00:00:00Z",
                            "status": "pending",
                            "image": None
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
                description="报告未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "报告未找到"
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
        operation_description="部分更新指定举报报告的信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "id": "report_id",
                            "user": "user_id",
                            "location": "部分更新后的报告位置",
                            "description": "部分更新后的报告详情",
                            "timestamp": "2024-05-01T00:00:00Z",
                            "status": "pending",
                            "image": None
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
                description="报告未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "报告未找到"
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
        operation_description="删除指定举报报告",
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
                description="报告未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "报告未找到"
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
            return response(False, error=str(e), status=status.HTTP_404_NOT_FOUND)
