from rest_framework import serializers
from .models import (
    Room,
    Device,
    Sensor,
    Measurement,
)


class DeviceMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            "id",
            "name"
        ]


class SensorMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            "id",
            "name"
        ]


class SensorMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            "id",
            "name",
            "room"
        ]


class RoomMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "type"
        ]


class RoomSerializer(serializers.ModelSerializer):
    devices = DeviceMiniSerializer(many=True)
    sensors = SensorMiniSerializer(many=True)

    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "type",
            "description",
            "devices",
            "sensors"
        ]


class DeviceSerializer(serializers.ModelSerializer):
    room = RoomMiniSerializer(many=False)

    class Meta:
        model = Device
        fields = [
            "id",
            "room",
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
    room = RoomMiniSerializer(many=False)

    class Meta:
        model = Sensor
        fields = [
            "id",
            "room",
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
    sensor = SensorMeasurementSerializer(many=False)

    class Meta:
        model = Measurement
        fields = [
            "id",
            "sensor",
            "value",
            "unit",
            "description",
        ]
