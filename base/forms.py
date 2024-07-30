from django.forms import ModelForm
from .models import *
from django import forms



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

class LineToBus(ModelForm):
    lines = forms.ModelMultipleChoiceField(queryset=Line.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Bus
        fields = ['lines']

class OrdinATACForm(ModelForm):
    class Meta:
        model = OrdinATAC
        fields = '__all__'

class LiveTrATACForm(ModelForm):
    class Meta:
        model = LiveTrATAC
        fields = '__all__'

class MultiDriverForm(ModelForm):
    class Meta:
        model = MultiDriver
        fields = '__all__'

class PassengerOnBus(forms.ModelForm):
    passengers = forms.ModelMultipleChoiceField(
        queryset=Passenger.objects.all(),
        widget=forms.CheckboxSelectMultiple  
    )

    class Meta:
        model = Bus
        fields = ['passengers']