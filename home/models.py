from django.db import models

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    registration = models.IntegerField()
    phone = models.CharField(max_length=12)
    car_meter = models.CharField(max_length=500)
    model = models.CharField(max_length=50)
    vin = models.IntegerField()
    address = models.CharField(max_length=300)
    engine_tune = models.CharField(max_length=30)
    engine_filter = models.CharField(max_length=30)
    air_filter = models.CharField(max_length=30)
    spark_plug = models.CharField(max_length=30)
    fuel_filter = models.CharField(max_length=30)
    injector = models.CharField(max_length=30)
    throttle_body = models.CharField(max_length=30)
    balancing = models.IntegerField()
    alignment = models.CharField(max_length=30)
    tyre_rotation = models.CharField(max_length=30)
    gear_oil = models.CharField(max_length=30)
    coolant = models.CharField(max_length=30)
    date = models.DateField()








