from django.forms import ModelForm
from .models import *

class BusForm(ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_id', 'line', 'capacity']

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