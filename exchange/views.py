from django.shortcuts import render

# Create your views here.
from django.conf import settings
from django.core.paginator import InvalidPage, Paginator
from django.http import Http404
from django.http import JsonResponse
from EBike.utils import md5hash

from haystack.forms import ModelSearchForm
from haystack.query import EmptySearchQuerySet, SearchQuerySet
from django.http import HttpResponse, JsonResponse
from .models import *
from .serializers import *
from django.contrib.auth.decorators import *
import hashlib
import datetime
import operator
from functools import reduce
import time
import requests
from haystack.views import SearchView

from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, JSONParser
from datetime import datetime
from PIL import Image
from io import BytesIO
import base64
from django.core.files.base import ContentFile

def user_goods_path(instance, filename):
    return f'user_{instance.goods.owner.id}/goods/{filename}'

class PublishView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, JSONParser]  # Now handles JSON too

    def post(self, request, *args, **kwargs):
        # Handle JSON data (assuming JSON payload also contains other form data as JSON)
        content = request.data.get('content')
        money = request.data.get('money')
        origin_money = request.data.get('origin_money')
        send_money = request.data.get('send_money')
        classify = request.data.get('classify')
        base64_images = request.data.get('base64_images', [])  # List of Base64 encoded images

        if not all([content, money, origin_money, send_money, classify]):
            return JsonResponse({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

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

            # Handle file uploads
            valid_images = []
            for file in request.FILES.getlist('image'):
                try:
                    # Open the image file
                    img = Image.open(file)
                    img.verify()  # Verify that it is, in fact, an image
                    valid_images.append(file)
                except (IOError, FileNotFoundError):
                    return JsonResponse({'error': 'Invalid image file.'}, status=status.HTTP_400_BAD_REQUEST)

            # Handle Base64 encoded images
            for image_data in base64_images:
                format, imgstr = image_data.split(';base64,')
                ext = format.split('/')[-1]
                data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
                try:
                    img = Image.open(data)
                    img.verify()
                    valid_images.append(data)
                except (IOError, FileNotFoundError):
                    return JsonResponse({'error': 'Invalid base64 image.'}, status=status.HTTP_400_BAD_REQUEST)
            
            for file in valid_images:
                GoodsImage.objects.create(goods=goods, image=file)
            
            return JsonResponse({'message': 'Success'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class EditView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        goods_hash = request.POST.get('hash')
        content = request.POST.get('content')
        price = request.POST.get('price')

        # if not all([goods_hash, content, price]):
        #     return JsonResponse({'error': 'Missing required fields.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            goods = Goods.objects.get(hash=goods_hash)
        except Goods.DoesNotExist:
            return JsonResponse({'error': 'Goods not found.'}, status=status.HTTP_404_NOT_FOUND)

        if request.user == goods.owner:
            new_hash = md5hash(request.user.username, content)
            Goods.objects.filter(hash=goods_hash).update(
                content=content,
                money=price,
                hash=new_hash
            )
            return JsonResponse({'message': 'Goods updated successfully'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)
        
    def patch(self, request, *args, **kwargs):
        goods_hash = request.data.get('hash')
        if not goods_hash:
            return JsonResponse({'error': 'Hash required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            goods = Goods.objects.get(hash=goods_hash)
        except Goods.DoesNotExist:
            return JsonResponse({'error': 'Goods not found.'}, status=status.HTTP_404_NOT_FOUND)

        if request.user != goods.owner:
            return JsonResponse({'error': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

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

            return JsonResponse({'message': 'Goods updated successfully'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'message': 'No updates performed'}, status=status.HTTP_204_NO_CONTENT)
        
class GetGoodsView(APIView):
    permission_classes = [AllowAny]  # 允许任何用户访问此视图

    def get(self, request, *args, **kwargs):
        goods_list = Goods.objects.order_by('-edit_date')[:10]  # 按编辑日期降序排列
        ret = []

        for goods in goods_list:
            images = goods.goodsimage_set.all()
            image_url = str(images[0].image) if images else None  # 确保至少有一张图片存在

            a = {
                "user_id": goods.owner.id,
                "goods_id": goods.hash,
                "image": image_url,
                "content": goods.content,
                "money": goods.money,
                "username": goods.owner.username,
            }
            ret.append(a)
        
        return JsonResponse(ret, safe=False)
    
class GoodsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        goods_id = kwargs.get('pk')
        if not goods_id:
            return HttpResponse('No goods ID provided', status=400)

        try:
            goods = Goods.objects.get(hash=goods_id)
        except Goods.DoesNotExist:
            return HttpResponse('Goods not found', status=404)

        images_url = []
        for image in goods.goodsimage_set.all():
            images_url.append({"image": str(image.image)})

        ret = {
            "user_id": goods.owner.id,
            "username": goods.owner.username,  # Assuming owner has a username field
            "money": goods.money,
            "content": goods.content,
            "origin_money": goods.origin_money,
            "send_money": goods.send_money,
            "images": images_url,
            "time": goods.edit_date.strftime("%Y-%m-%d %H:%M:%S")
        }
        return JsonResponse(ret)
    
class MyGoodsView(APIView):
    permission_classes = [IsAuthenticated]  # Ensures only authenticated users can access this view

    def get(self, request, *args, **kwargs):
        user = request.user  # Using the authenticated user directly from the request

        goods_list = Goods.objects.filter(owner=user).order_by('-edit_date')  # Fetch goods related to the user, ordered by edit date
        ret = []

        for goods in goods_list:
            images = GoodsImage.objects.filter(goods=goods).all()
            image_url = str(images[0].image) if images else None  # Handling cases with no images

            a = {
                "goods_id": goods.hash,
                "image": image_url,
                "content": goods.content,
                "money": goods.money,
            }
            ret.append(a)

        return JsonResponse(ret, safe=False)  # safe=False allows returning a list instead of a dictionary
    
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
            return JsonResponse(ret, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)