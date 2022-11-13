from django.db import models

# Create your models here.


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ("classroom", "Classroom"),
        ("amenities", "Amenities"),
        ("outdoors", "Outdoors"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=100,
        choices=ROOM_TYPE_CHOICES,
        default="other"
    )
    description = models.TextField(
        default="",
        blank=True,
    )


class Device(models.Model):
    DEVICE_TYPE_CHOICES = [
        ("lightning", "Lightning"),
        ("electronics", "Electronics"),
        ("appliances", "Appliances"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(
        max_length=100,
        choices=DEVICE_TYPE_CHOICES,
        default="other"
    )
    current = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    voltage = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    power = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    description = models.TextField(
        default="",
        blank=True,
    )
    added = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField()


class Sensor(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    current = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    voltage = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    power = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    description = models.TextField(
        default="",
        blank=True,
    )
    added = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField()


class Measurement(models.Model):
    sensor_id = models.IntegerField()
    value = models.DecimalField(
        decimal_places=9,
        max_digits=18,
    )
    unit = models.CharField(max_length=24)
    datetime = models.DateTimeField(
        auto_now_add=True
    )
    date = models.DateField(
        auto_now_add=True
    )
    time = models.TimeField(
        auto_now_add=True
    )
    description = models.TextField(
        default="",
        blank=True,
    )
