from django.urls import path
from .views import *

urlpatterns = [
    path('reports/<str:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('reports/', ReportAPIView.as_view(), name='report-create-or-update'),
]