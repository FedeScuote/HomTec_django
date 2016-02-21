from .models import Client, MobileUser, Category, SubCategory, Rating, Publication
from .serializers import (ClientSerializer, MobileUserSerializer, CategorySerializer,
                          SubCategorySerializer, PublicationSerializer, RatingSerializer)
from rest_framework import viewsets


# List Create View for Client model
class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# List Create View for MobileUser model
class MobileUserViewSet(viewsets.ModelViewSet):
    queryset = MobileUser.objects.all()
    serializer_class = MobileUserSerializer


# List Create View for Category model
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
