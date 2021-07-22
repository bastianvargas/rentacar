from rest_framework import serializers
from clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    last_name=serializers.CharField()
    class Meta:
        model = Client
        fields = ['id', 'rut', 'name', 'last_name']

class ClientTotalSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField()
    class Meta:
        model = Client
        fields = ['id', 'rut', 'name', 'total']

