from rest_framework import generics, viewsets
from clients.models import Client
from .serializers import ClientSerializer, ClientTotalSerializer
from django.db.models.functions import Substr, StrIndex
from django.db.models import F, Value, Sum
from rest_framework.decorators import action
from rest_framework.response import Response

# class ClientListView(generics.ListAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=False, methods=["GET"], url_path='client-by-last-name')
    def getClientSortByLastName(self, request, *args, **kwargs):

        queryset = Client.objects.annotate(space_index=StrIndex(F('name'), Value(' ')))\
         .annotate(last_name=Substr('name', F('space_index')))\
         .order_by('last_name')

        serializer = ClientSerializer(queryset, many=True)

        return Response(serializer.data)


    @action(detail=False, methods=["GET"], url_path="client-by-rent")
    def getClientsSortByRentExpenses(self, request, *args, **kwargs):

        queryset = Client.objects.prefetch_related('client_rents').annotate(total=Sum(F('client_rents__daily_cost')\
         * F('client_rents__days'))).order_by('-total')

        serializer = ClientTotalSerializer(queryset, many=True)

        return Response(serializer.data)