from django.contrib import admin
from car_detailing.models import Client, Car


class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cpf', 'category']


class CarAdmin(admin.ModelAdmin):
    list_display = ['brand_model', 'license_plate', 'category', 'owner', 'color_code']
    list_display_links = ['brand_model', 'license_plate']


admin.site.register(Client, ClientAdmin)
admin.site.register(Car, CarAdmin)
