from rest_framework import serializers
from .models import Client, MobileUser, Category, SubCategory, Publication, Rating

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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('category', 'name')


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('client', 'mobile_user', 'completed', 'description', 'photo')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('stars', 'comment', 'user')
