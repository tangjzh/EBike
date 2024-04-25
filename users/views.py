from django.shortcuts import render

# Create your views here.
from rest_framework import status, views
from rest_framework import permissions, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from .models import VehiclePermit
from .serializers import VehiclePermitSerializer, MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

User = get_user_model()

class UserCreateAPIView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserLoginAPIView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
class UserDeleteAPIView(APIView):

    def delete(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class UpdateUserProfileView(generics.UpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class RetrieveUserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class BindPermitView(views.APIView):

    def post(self, request):
        serializer = VehiclePermitSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnbindPermitView(views.APIView):    
    def delete(self, request):
        user = request.user
        try:
            permit = VehiclePermit.objects.get(user=user)
            permit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except VehiclePermit.DoesNotExist:
            return Response({'error': 'No permit found to unbind'}, status=status.HTTP_404_NOT_FOUND)