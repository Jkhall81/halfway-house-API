from .models import House, Resident
from rest_framework import serializers
from django.contrib.auth.models import User

# Model Serializer


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = User
        fields = ['id', 'owner', 'username',
                  'email', 'first_name', 'last_name']


class HouseModelSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = House
        fields = '__all__'


class ResidentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = '__all__'
