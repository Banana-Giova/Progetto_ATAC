from django.db import models

class Stop:
    pass

class Passenger(models.Model):
    passenger_id:str = models.CharField(max_length=12)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)

class Line(models.Model):
    line_number:str = models.CharField(max_length=128)
    name:str = models.CharField(max_length=128)
    stops = models.ManyToManyField(Stop)

class Stop(models.Model):
    stop_id:str = models.CharField(max_length=128)
    name:str = models.CharField(max_length=128)
    latitude:float = models.FloatField(max_length=128)
    longitude:float = models.FloatField(max_length=128)
    lines = models.ManyToManyField(Line)

class Bus(models.Model):
    bus_id:str = models.CharField(max_length=3)
    line = models.ForeignKey(Line)
    capacity = models.IntegerField(max_length=2)
    passengers = models.ManyToManyField(Passenger)

class Driver(models.Model):
    bus_id:str = models.CharField(max_length=12)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)
    assingned_bus = models.ForeignKey(Bus)