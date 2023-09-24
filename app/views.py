from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import House, Resident
from .serializers import HouseModelSerializer, ResidentModelSerializer, UserSerializer

# Create your views here.


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseModelSerializer


class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
