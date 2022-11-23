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
    serializer_class = RoomSerializer
    queryset = Room.objects.all()

    @decorators.action(detail=True, methods=["POST"])
    def add_room(self, request, pk=None):
        self.serializer_class = RoomMiniSerializer
        return response.Response(data=request, status=status.HTTP_200_OK)

    @decorators.action(detail=True, methods=["GET"])
    def get_rooms(self):
        self.serializer_class = RoomSerializer
        return response.Response(data=self.queryset, status=status.HTTP_200_OK)


class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()


class SensorViewSet(viewsets.ModelViewSet):
    serializer_class = SensorSerializer
    queryset = Sensor.objects.all()


class MeasurementViewSet(viewsets.ModelViewSet):
    serializer_class = MeasurementSerializer
    queryset = Measurement.objects.all()
