from rest_framework import viewsets
from car_detailing.models import Client, Car
from car_detailing.serializers import ClientSerializer, CarSerializer


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
