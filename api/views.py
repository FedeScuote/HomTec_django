from .models import Client, MobileUser
from .serializers import ClientSerializer, MobileUserSerializer
from rest_framework import generics
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