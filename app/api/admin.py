from django.contrib import admin
from .models import (
    Device,
    Sensor,
    Measurement
)
# Register your models here.
admin.site.register(Device)
admin.site.register(Sensor)
admin.site.register(Measurement)
