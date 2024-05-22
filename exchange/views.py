from django.shortcuts import render
from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404, JsonResponse, HttpResponse
from EBike.utils import md5hash, response
from haystack.forms import ModelSearchForm
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from haystack.views import SearchView
from .models import *
from .serializers import *
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import datetime
from PIL import Image
from io import BytesIO
import base64
from django.core.files.base import ContentFile
import hashlib
import operator
from functools import reduce
import time
import requests

class PublishView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser]

    @swagger_auto_schema(
        operation_description="发布新的商品",
        responses={
            201: openapi.Response(
                description="发布成功",
                examples={
                    "application/json": {
                        "success": True,
                        "message": "Success"
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Missing required fields."
                    }
                }
            ),
            500: openapi.Response(
                description="服务器内部错误",
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
        content = request.data.get('content')
        money = request.data.get('money')
        origin_money = request.data.get('origin_money')
        send_money = request.data.get('send_money')
        classify = request.data.get('classify')
        base64_images = request.data.get('base64_images', [])  

        if not all([content, money, origin_money, send_money, classify]):
            return response(False, error='Missing required fields.', status=status.HTTP_400_BAD_REQUEST)

        try:
            user = request.user
            hash_key = md5hash(user.username, content)
            
            goods = Goods.objects.create(
                owner=user, 
                hash=hash_key,
                content=content, 
                money=money,
                origin_money=origin_money, 
                send_money=send_money,
                classify=classify
            )

            valid_images = []
            for file in request.FILES.getlist('image'):
                try:
                    img = Image.open(file)
                    img.verify()
                    valid_images.append(file)
                except (IOError, FileNotFoundError):
                    return response(False, error='Invalid image file.', status=status.HTTP_400_BAD_REQUEST)

            for image_data in base64_images:
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
                try:
                    img = Image.open(data)
                    img.verify()
                    valid_images.append(data)
                except (IOError, FileNotFoundError):
                    return response(False, error='Invalid base64 image.', status=status.HTTP_400_BAD_REQUEST)
            
            for file in valid_images:
                GoodsImage.objects.create(goods=goods, image=file)
            
            return response(True, message='Success', status=status.HTTP_201_CREATED)
        except Exception as e:
            return response(False, error=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="编辑商品信息",
        responses={
            200: openapi.Response(
                description="更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "message": "Goods updated successfully"
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Missing required fields."
                    }
                }
            ),
            403: openapi.Response(
                description="未授权",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Unauthorized"
                    }
                }
            ),
            404: openapi.Response(
                description="商品未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Goods not found."
                    }
                }
            )
        }
    )
    def post(self, request, *args, **kwargs):
        goods_hash = request.POST.get('hash')
        content = request.POST.get('content')
        price = request.POST.get('price')

        try:
            goods = Goods.objects.get(hash=goods_hash)
        except Goods.DoesNotExist:
            return response(False, error='Goods not found.', status=status.HTTP_404_NOT_FOUND)

        if request.user == goods.owner:
            new_hash = md5hash(request.user.username, content)
            Goods.objects.filter(hash=goods_hash).update(
                content=content,
                money=price,
                hash=new_hash
            )
            return response(True, message='Goods updated successfully', status=status.HTTP_200_OK)
        else:
            return response(False, error='Unauthorized', status=status.HTTP_403_FORBIDDEN)

    @swagger_auto_schema(
        operation_description="部分更新商品信息",
        responses={
            200: openapi.Response(
                description="部分更新成功",
                examples={
                    "application/json": {
                        "success": True,
                        "message": "Goods updated successfully"
                    }
                }
            ),
            204: openapi.Response(
                description="没有更新操作",
                examples={
                    "application/json": {
                        "success": True,
                        "message": "No updates performed"
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Hash required."
                    }
                }
            ),
            403: openapi.Response(
                description="未授权",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Unauthorized"
                    }
                }
            ),
            404: openapi.Response(
                description="商品未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Goods not found."
                    }
                }
            )
        }
    )
    def patch(self, request, *args, **kwargs):
        goods_hash = request.data.get('hash')
        if not goods_hash:
            return response(False, error='Hash required.', status=status.HTTP_400_BAD_REQUEST)

        try:
            goods = Goods.objects.get(hash=goods_hash)
        except Goods.DoesNotExist:
            return response(False, error='Goods not found.', status=status.HTTP_404_NOT_FOUND)

        if request.user != goods.owner:
            return response(False, error='Unauthorized', status=status.HTTP_403_FORBIDDEN)

        content = request.data.get('content')
        price = request.data.get('price')
        update_fields = {}
        
        if content:
            update_fields['content'] = content
            new_hash = md5hash(request.user.username, content)
            update_fields['hash'] = new_hash

        if price:
            update_fields['money'] = price

        if update_fields:
            for key, value in update_fields.items():
                setattr(goods, key, value)
            goods.save()

            return response(True, message='Goods updated successfully', status=status.HTTP_200_OK)
        else:
            return response(True, message='No updates performed', status=status.HTTP_204_NO_CONTENT)

class GetGoodsView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_description="获取最新的10个商品",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "user_id": 1,
                                "goods_id": "goods_hash",
                                "image": "image_url",
                                "content": "商品内容",
                                "money": "商品价格",
                                "username": "用户名"
                            }
                        ]
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            goods_list = Goods.objects.order_by('-edit_date')[:10]
            ret = []

            for goods in goods_list:
                images = goods.goodsimage_set.all()
                image_url = str(images[0].image) if images else None

                a = {
                    "user_id": goods.owner.id,
                    "goods_id": goods.hash,
                    "image": image_url,
                    "content": goods.content,
                    "money": goods.money,
                    "username": goods.owner.username,
                }
                ret.append(a)
            
            return response(True, data=ret)
        except Exception as e:
            return response(False, error=str(e))

class GoodsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()

    @swagger_auto_schema(
        operation_description="获取指定商品的详细信息",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": {
                            "user_id": 1,
                            "username": "用户名",
                            "money": "商品价格",
                            "content": "商品内容",
                            "origin_money": "原价",
                            "send_money": "运费",
                            "images": [
                                {"image": "image_url"}
                            ],
                            "time": "2024-05-01 00:00:00"
                        }
                    }
                }
            ),
            400: openapi.Response(
                description="请求无效",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "No goods ID provided"
                    }
                }
            ),
            404: openapi.Response(
                description="商品未找到",
                examples={
                    "application/json": {
                        "success": False,
                        "error": "Goods not found"
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        goods_id = kwargs.get('pk')
        if not goods_id:
            return response(False, error='No goods ID provided', status=status.HTTP_400_BAD_REQUEST)

        try:
            goods = Goods.objects.get(hash=goods_id)
        except Goods.DoesNotExist:
            return response(False, error='Goods not found', status=status.HTTP_404_NOT_FOUND)

        images_url = []
        for image in goods.goodsimage_set.all():
            images_url.append({"image": str(image.image)})

        ret = {
            "user_id": goods.owner.id,
            "username": goods.owner.username,
            "money": goods.money,
            "content": goods.content,
            "origin_money": goods.origin_money,
            "send_money": goods.send_money,
            "images": images_url,
            "time": goods.edit_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        return response(True, data=ret)

class MyGoodsView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="获取当前用户发布的所有商品",
        responses={
            200: openapi.Response(
                description="获取成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "goods_id": "goods_hash",
                                "image": "image_url",
                                "content": "商品内容",
                                "money": "商品价格"
                            }
                        ]
                    }
                }
            )
        }
    )
    def get(self, request, *args, **kwargs):
        try:
            user = request.user
            goods_list = Goods.objects.filter(owner=user).order_by('-edit_date')
            ret = []

            for goods in goods_list:
                images = GoodsImage.objects.filter(goods=goods).all()
                image_url = str(images[0].image) if images else None

                a = {
                    "goods_id": goods.hash,
                    "image": image_url,
                    "content": goods.content,
                    "money": goods.money,
                }
                ret.append(a)

            return response(True, data=ret)
        except Exception as e:
            return response(False, error=str(e))

RESULTS_PER_PAGE = getattr(settings, 'HAYSTACK_SEARCH_RESULTS_PER_PAGE', 20)

class MySearchView(SearchView):
    extra_context = {}
    query = ''
    results = EmptySearchQuerySet()
    request = None
    form = None
    results_per_page = RESULTS_PER_PAGE

    @swagger_auto_schema(
        operation_description="搜索商品",
        responses={
            200: openapi.Response(
                description="搜索成功",
                examples={
                    "application/json": {
                        "success": True,
                        "data": [
                            {
                                "goodsID": "goods_hash",
                                "image": "image_url",
                                "content": "商品内容",
                                "money": "商品价格",
                                "username": "用户名",
                                "time": "编辑时间"
                            }
                        ],
                        "max_page": 10
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
    def create_response(self):
        try:
            context = self.get_context()

            ret = []
            for result in context['paginator'].object_list:
                goods = result._object
                image_url = str(goods.goodsimage_set.all()[0].image)

                a = {
                    "goodsID": goods.hash,
                    "image": image_url,
                    "content": goods.content,
                    "money": goods.money,
                    "username": goods.owner.username,
                    "time": goods.edit_date,
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
            return response(False, error=str(e), status=status.HTTP_400_BAD_REQUEST)
