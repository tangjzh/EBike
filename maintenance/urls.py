from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.ServiceShopList.as_view(), name='service-shops'),
    path('shops/<int:pk>/', views.ServiceShopDetailList.as_view(), name='service-shops-detail'),
    path('tips/', views.ServiceTipList.as_view(), name='service-tips'),
    path('tips/<int:pk>/', views.ServiceTipDetailList.as_view(), name='service-tips-detail'),
    path('appointments/', views.AppointmentList.as_view(), name='appointments'),
    path('appointments/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail'),
]
