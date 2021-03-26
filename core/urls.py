from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from car_detailing.views import ClientsViewSet, CarViewSet

router = routers.DefaultRouter()
router.register(r'client', ClientsViewSet)
router.register(r'car', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
