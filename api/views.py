from .models import Client, MobileUser, Category, SubCategory, Rating, Publication
from .serializers import (ClientSerializer, MobileUserSerializer, CategorySerializer,
                          SubCategorySerializer, PublicationSerializer, RatingSerializer)
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


# List Create View for Client model
class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    permission_classes = (IsAuthenticated,)
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


# List Create View for MobileUser model
class MobileUserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = MobileUser.objects.all()
    serializer_class = MobileUserSerializer


# List Create View for Category model
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class PublicationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer


class RatingViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
