from django.db import models

# Create your models here.


class Devices(models.Model):
    # id field provided by Django
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    current = models.IntegerField()
    voltage = models.IntegerField()
