from django.forms import ModelForm
from .models import *

#-----Creation Tool Forms-----#

class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_id', 'capacity']

class LineForm(ModelForm):
    class Meta:
        model = Line
        fields = ['line_number', 'name']

class StopForm(ModelForm):
    class Meta:
        model = Stop
        fields = ['stop_id', 'name', 'latitude', 'longitude']

class PassengerForm(ModelForm):
    class Meta:
        model = Passenger
        fields = '__all__'

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['driver_id', 'name', 'surname']

#-----Assignment Tool Forms-----#

class BusToDriver(ModelForm):
    class Meta:
        model = Driver
        fields = ['assigned_bus']

class LineToBus(ModelForm):
    class Meta:
        model = Bus
        fields = ['line']

class OrdinATACForm(ModelForm):
    class Meta:
        model = OrdinATAC
        fields = '__all__'

class PassengerOnBus(ModelForm):
    class Meta:
        model = Bus
        fields = ['passengers']