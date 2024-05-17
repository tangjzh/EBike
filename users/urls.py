from django.urls import path
from .views import UserCreateAPIView, UserDeleteAPIView, UserLoginAPIView
from .views import BindPermitView, UnbindPermitView, UpdateUserProfileView, RetrieveUserProfileView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='create-user'),
    path('login/', UserLoginAPIView.as_view(), name='login-user'),
    path('refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('profile/', UpdateUserProfileView.as_view(), name='update-profile'),
    path('profile/', RetrieveUserProfileView.as_view(), name='retrieve-profile'),
    # TODO: 现在用户直接可以删用户，改掉
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete-user'),
    path('bind-permit/', BindPermitView.as_view(), name='bind-permit'),
    path('unbind-permit/', UnbindPermitView.as_view(), name='unbind-permit'),
]
