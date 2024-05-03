from django.urls import path
from .views import *

urlpatterns = [
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
    path('reports/', ReportAPIView.as_view(), name='report-create-or-update'),
]