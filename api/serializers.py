from rest_framework import serializers
from .models import Client, MobileUser

# Serializers for the Django Rest Framework


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user', 'active', 'rut', 'name', 'address', 'state',
                  'country', 'phone_number', 'logo', 'category', 'description')


class MobileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileUser
        fields = ('user', 'age', 'state', 'country', 'phone_number')
