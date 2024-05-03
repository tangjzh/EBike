from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Report
from .serializers import ReportSerializer
from rest_framework import generics, mixins
import base64
from io import BytesIO
from PIL import Image
from django.core.files.base import ContentFile

class ReportAPIView(APIView, mixins.ListModelMixin):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    def handle_image(self, image_data):
        # 检查是否是base64编码
        if 'data:image' in image_data and ';base64,' in image_data:
            format, imgstr = image_data.split(';base64,')  # 分割数据格式和实际图片数据
            ext = format.split('/')[-1]  # 获取图片扩展名
            image = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)  # 解码并转换为图片文件
            return image
        return None
    
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
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(ReportSerializer(report).data, status=status.HTTP_200_OK if not created else status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)    

class ReportDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    lookup_field = 'pk'  # 使用报告的主键作为查找字段