from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (
    RoomSerializer,
    DeviceSerializer,
    SensorSerializer,
    MeasurementSerializer
)
from .models import (
    Room,
    Device,
    Sensor,
    Measurement,
)

# Create your views here.


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
