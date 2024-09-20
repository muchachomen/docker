from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets

from .models import CarBrand, Profile
from .serializers import CarBrandSerializer, UserSerializer


class CarBrandView(generics.ListCreateAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class CarDetailView(generics.RetrieveAPIView):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer

class ProfileView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
