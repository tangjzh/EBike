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


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class UserPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(user=user)
    
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        # if self.request.user != serializer.instance.user:
        #     raise permissions.PermissionDenied("You cannot edit comments made by other users.")
        serializer.save()

    def perform_destroy(self, instance):
        # if self.request.user != instance.user:
        #     raise permissions.PermissionDenied("You cannot delete comments made by other users.")
        instance.delete()

class InteractionToggleView(APIView):
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
                return Response({'status': 'interaction removed'}, status=status.HTTP_204_NO_CONTENT)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InteractionCountView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = InteractionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            post_id = serializer.validated_data.get('post')
            likes_count = Interaction.objects.filter(post_id=post_id, type='like').count()
            favorites_count = Interaction.objects.filter(post_id=post_id, type='favorite').count()
            return Response({
                'likes_count': likes_count,
                'favorites_count': favorites_count
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserFavoritesListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        favorited_posts_ids = Interaction.objects.filter(user=user, type='favorite').values_list('post', flat=True)
        return Post.objects.filter(id__in=favorited_posts_ids)
    
class UserLikeListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        favorited_posts_ids = Interaction.objects.filter(user=user, type='like').values_list('post', flat=True)
        return Post.objects.filter(id__in=favorited_posts_ids)
    
class ToggleFollowView(APIView):
    serializer_class = ToggleFollowSerializer

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

    def get_queryset(self):
        return self.request.user.chat_rooms.all()

class RoomDetailView(generics.RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

class CreateMessageView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

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
            return JsonResponse(ret, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)