from rest_framework import generics
from clients.models import Client
from .serializers import ClientSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    