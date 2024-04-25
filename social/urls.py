from django.urls import path
from .views import *

app_name = "social"

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-edit'),
    path('post/', UserPostsListView.as_view(), name='user-posts'),
    path('comment/create/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-edit'),
    path('post/<int:post_id>/interaction/toggle/', InteractionToggleView.as_view(), name='toggle-interaction'),
    path('post/<int:post_id>/interaction/count/', InteractionCountView.as_view(), name='interactions-count'),
    path('post/favorites/', UserFavoritesListView.as_view(), name='user-favorites'),
    path('post/likes/', UserLikeListView.as_view(), name='user-likes'),
    path('follow/toggle/', ToggleFollowView.as_view(), name='toggle-follow'),
]
