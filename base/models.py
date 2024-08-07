from django.db import models



#-----Models-----#

class Passenger(models.Model):
    passenger_id:str = models.CharField(max_length=12, db_index=True, unique=True, primary_key=True)
    name:str = models.CharField(max_length=128)
    surname:str = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.passenger_id

class Line(models.Model):
    line_number:str = models.CharField(max_length=128, db_index=True, unique=True, primary_key=True)
    name:str = models.CharField(max_length=128)
    stops = models.ManyToManyField('Stop', through='OrdinATAC')
    buses = models.ManyToManyField('Bus', through='LiveTrATAC')
    
    def __str__(self) -> str:
        return self.line_number
    
class Stop(models.Model):
    stop_id:str = models.CharField(max_length=128, db_index=True, unique=True, primary_key=True)
    name:str = models.CharField(max_length=128)
    latitude:float = models.FloatField(max_length=10)
    longitude:float = models.FloatField(max_length=10)
    lines = models.ManyToManyField('Line', through='OrdinATAC')

    def __str__(self) -> str:
        return self.stop_id

class Bus(models.Model):
    bus_id = models.CharField(max_length=4, db_index=True, unique=True, primary_key=True)
    drivers = models.ManyToManyField('Driver', through='MultiDriver')
    capacity = models.PositiveIntegerField()
    passengers = models.ManyToManyField(Passenger)

    def __str__(self) -> str:
        return self.bus_id

class Driver(models.Model):
    driver_id = models.CharField(max_length=12, db_index=True, unique=True, primary_key=True)
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    buses = models.ManyToManyField('Bus', through='MultiDriver')

    def __str__(self) -> str:
        return self.driver_id



#-----Throughs-----#

class OrdinATAC(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE)

class LiveTrATAC(models.Model):
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

class MultiDriver(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)