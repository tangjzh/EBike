from rest_framework import generics, permissions
from rest_framework import status
from .models import Post, Comment, Interaction, Follow
from .serializers import PostSerializer, CommentSerializer, InteractionSerializer, ToggleFollowSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Room, Message
from .serializers import RoomSerializer, MessageSerializer

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