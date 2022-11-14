from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register("rooms", views.RoomViewSet)
router.register("devices", views.DeviceViewSet)
router.register("sensors", views.SensorViewSet)
router.register("measurements", views.MeasurementViewSet)

urlpatterns = [
    path('', include(router.urls))
]
