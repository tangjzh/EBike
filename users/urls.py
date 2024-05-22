from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='create-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('profile/', UserProfileListView.as_view(), name='update-profile'),
    path('profile/<int:pk>/', UserPofileDetailView.as_view(), name='profile-detail'),
    # TODO: 现在用户直接可以删用户，改掉
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete-user'),
    path('bind-permit/', BindPermitView.as_view(), name='bind-permit'),
    path('unbind-permit/', UnbindPermitView.as_view(), name='unbind-permit'),
]
