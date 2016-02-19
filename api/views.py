from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics
from rest_framework import viewsets


# List Create View for Client model
class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Client.objects.all()
