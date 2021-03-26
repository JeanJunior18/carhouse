from rest_framework import serializers

from car_detailing.models import Client, Car


class ClientSerializer(serializers.ModelSerializer):
    cars = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'name', 'cpf', 'category', 'cars']

    @staticmethod
    def get_cars(client):
        return CarSerializer(instance=client.car_set.all(), many=True).data


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'brand_model', 'license_plate', 'color_code', 'category', 'owner']
