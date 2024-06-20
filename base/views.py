from django.shortcuts import render
import django.http
from django.views import View

from .models import Passenger

# Create your views here.

"""class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self,request):
        return render(request, "home.html")"""

bus_lines = [
    {'id': 1, 'line_number': 451, 'name': 'Ponte Mammolo', 'stops': 18},
    {'id': 2, 'line_number': 558, 'name': 'Gardenie', 'stops': 29},
    {'id': 3, 'line_number': 777, 'name': 'Agricoltura', 'stops': 42},
]

def home(request):
    context = {'bus_lines': bus_lines}
    return render(request, "base/home.html", context)

def bus(request, line_number):
    req_bus = None
    for bus in bus_lines:
        if bus['line_number'] == int(line_number):
            req_bus = bus
            break
    context = {'bus':bus}
    return render(request, "base/bus.html", context)

def passengers(request):
    passengers = Passenger.objects.all()
    context = {'passengers':passengers}
    return render(request, "base/passengers.html", context)