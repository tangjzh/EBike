from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, status
from .models import ServiceShop, ServiceTip, Appointment
from .serializers import ServiceShopSerializer, ServiceTipSerializer, AppointmentSerializer
from django.http import HttpResponse, JsonResponse

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

class ServiceShopList(generics.ListCreateAPIView):
    queryset = ServiceShop.objects.all()
    serializer_class = ServiceShopSerializer

class ServiceShopDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceShop.objects.all()
    serializer_class = ServiceShopSerializer

class ServiceTipList(generics.ListCreateAPIView):
    queryset = ServiceTip.objects.all()
    serializer_class = ServiceTipSerializer

class ServiceTipDetailList(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTip.objects.all()
    serializer_class = ServiceTipSerializer

class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return Appointment.objects.filter(user=user) 

class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    # def post(self, request, *args, **kwargs):
    #     id = kwargs.get('pk')
    #     service_type = request.data.get('servive_type')
    #     ap_status = request.data.get('status')
    #     ap_time = request.data.get('appointment_time')

    #     if all(value is None for value in [service_type, ap_status, ap_time]):
    #         return JsonResponse({"message": "Nothing changed."}, status=status.HTTP_200_OK)

    #     try:
    #         appointment = Appointment.objects.filter(id=id).first()
    #     except Appointment.DoesNotExist:
    #         return JsonResponse({"error": "No such appointment."}, status=status.HTTP_404_NOT_FOUND)

    #     try:
    #         for key, value in zip(['servive_type', 'status', 'appointment_time'], [service_type, ap_status, ap_time]):
    #             if value is not None:
    #                 setattr(appointment, key, value)

    #         appointment.save()
    #     except Exception as e:
    #         return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    #     return JsonResponse({"status": "Success"}, status=status.HTTP_200_OK)
