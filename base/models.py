from django.db import models

"""class Stop:
    pass"""

class Passenger(models.Model):
    passenger_id:str = models.CharField(max_length=12, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.passenger_id

class Line(models.Model):
    line_number:str = models.CharField(max_length=128, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    stops = models.ManyToManyField('Stop', through='OrdinATAC')
    
    def __str__(self) -> str:
        return self.line_number
    
class Stop(models.Model):
    stop_id:str = models.CharField(max_length=128, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    latitude:float = models.FloatField(max_length=10)
    longitude:float = models.FloatField(max_length=10)
    lines = models.ManyToManyField('Line', through='OrdinATAC')

    def __str__(self) -> str:
        return self.stop_id
    
class OrdinATAC(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

class Bus(models.Model):
    bus_id:str = models.CharField(max_length=4, db_index=True, unique=True)
    line = models.ForeignKey(Line, null=True, on_delete=models.CASCADE)
    capacity = models.IntegerField()
    passengers = models.ManyToManyField(Passenger)

    def __str__(self) -> str:
        return self.bus_id

class Driver(models.Model):
    driver_id:str = models.CharField(max_length=12, db_index=True, unique=True)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)
    assingned_bus = models.ForeignKey(Bus, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.driver_id