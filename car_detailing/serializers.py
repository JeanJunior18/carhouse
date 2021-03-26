from rest_framework import serializers

from car_detailing.models import Client, Car


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf', 'category']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand_model', 'owner_id', 'category']

