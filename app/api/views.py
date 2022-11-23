from django.shortcuts import render
from rest_framework import (
    viewsets,
    decorators,
    views,
    response,
    status,
)
# from rest_framework.views import APIView
# from rest_framework.response import Response
from .serializers import (
    RoomMiniSerializer,
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
    # serializer_class = RoomSerializer
    queryset = Room.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return RoomSerializer
        if self.action == "list":
            return RoomSerializer
        return RoomMiniSerializer

    # @decorators.action(detail=True, methods=["POST"])
    def create(self, *args, **kwargs):
        return viewsets.ModelViewSet.create(self, *args, **kwargs)

    # @decorators.action(detail=True, methods=["GET"])
    def retrieve(self, *args, **kwargs):
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)

    def list(self, *args, **kwargs):
        return viewsets.ModelViewSet.retrieve(self, *args, **kwargs)


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
