from django.db import models

class Stop:
    pass

class Passenger(models.Model):
    passenger_id:str = models.CharField(max_length=12, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.passenger_id

class Line(models.Model):
    line_number:str = models.CharField(max_length=128, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    stops = models.ManyToManyField(Stop)
    
    def __str__(self) -> str:
        return self.line_number
    
class Stop(models.Model):
    stop_id:str = models.CharField(max_length=128, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    latitude:float = models.FloatField(null=True)
    longitude:float = models.FloatField(null=True)
    lines = models.ManyToManyField(Line)

    def __str__(self) -> str:
        return self.stop_id

class Bus(models.Model):
    bus_id:str = models.CharField(max_length=3, db_index=True, unique=True)
    line = models.ForeignKey(Line, on_delete=models.SET_NULL)
    capacity = models.IntegerField(null=True)
    passengers = models.ManyToManyField(Passenger)

    def __str__(self) -> str:
        return self.bus_id

class Driver(models.Model):
    driver_id:str = models.CharField(max_length=12, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)
    assingned_bus = models.ForeignKey(Bus, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.driver_id