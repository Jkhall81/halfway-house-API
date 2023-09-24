from .models import House, Resident
from rest_framework import serializers
from django.contrib.auth.models import User

# Model Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class HouseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class ResidentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'
