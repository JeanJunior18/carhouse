from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from car_detailing.views import ClientsViewSet, CarViewSet

router = routers.DefaultRouter()
router.register(r'client', ClientsViewSet)
router.register(r'car', CarViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path('api/login/', obtain_jwt_token),
    path('api/', include(router.urls)),
]
