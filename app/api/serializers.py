from rest_framework import serializers
from .models import (
    Room,
    Device,
    Sensor,
    Measurement,
)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "name",
            "type",
            "description",
        ]


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "name",
            "brand",
            "type",
            "current",
            "voltage",
            "power",
            "description",
            "is_active",
        ]


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            "name",
            "brand",
            "type",
            "current",
            "voltage",
            "power",
            "description",
            "is_active",
        ]


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = [
            "sensor_id",
            "value",
            "unit",
            "description",
        ]
