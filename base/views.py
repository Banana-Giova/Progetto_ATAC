from django.shortcuts import render, redirect
import django.http
from django.views import View

from .models import *
from .forms import *

# Create your views here.



#-----Basic Pages-----#

def home(request):
    bus_lines = Line.objects.all()
    context = {'bus_lines': bus_lines}
    return render(request, "base/home.html", context)

def success(request):
    return render(request, 'base/success.html')

def create(request):
    return render(request, 'base/create.html')



#-----List Pages-----#

def passengers_list(request):
    passengers_list = Passenger.objects.all()
    context = {'passengers_list':passengers_list}
    return render(request, "base/lists/passengers_list.html", context)

def bus_list(request):
    bus_list = Bus.objects.all()
    context = {'bus_list':bus_list}
    return render(request, "base/lists/bus_list.html", context)

def stops_list(request):
    stops_list = Stop.objects.all()
    context = {'stops_list':stops_list}
    return render(request, "base/lists/stops_list.html", context)

def drivers_list(request):
    drivers = Driver.objects.all()
    context = {'drivers':drivers}
    return render(request, "base/lists/drivers_list.html", context)



#-----Detail Pages-----#

def line(request, line_number):
    req_line = Line.objects.get(line_number=line_number)
    context = {'line':req_line}
    return render(request, "base/details/line.html", context)

def bus(request, bus_id):
    req_bus = Bus.objects.get(bus_id=bus_id)
    context = {'bus':req_bus}
    return render(request, "base/details/bus.html", context)

def stop(request, stop_id):
    req_stop = Stop.objects.get(stop_id=stop_id)
    context = {'stop':req_stop}
    return render(request, "base/details/stop.html", context)

def passenger(request, passenger_id):
    req_passenger = Passenger.objects.get(passenger_id=passenger_id)
    context = {'passenger':req_passenger}
    return render(request, "base/details/passenger.html", context)

def driver(request, driver_id):
    req_driver = Driver.objects.get(driver_id=driver_id)
    context = {'driver':req_driver}
    return render(request, "base/details/driver.html", context)



#-----Creation Tool Forms-----#

def create_bus(request):
    form = BusForm()
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/bus_form.html', context)

def create_line(request):
    form = LineForm()
    if request.method == 'POST':
        form = LineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/line_form.html', context)

def create_stop(request):
    form = StopForm()
    if request.method == 'POST':
        form = StopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/stop_form.html', context)

def create_passenger(request):
    form = PassengerForm()
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/passenger_form.html', context)

def create_driver(request):
    form = DriverForm()
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/driver_form.html', context)



#-----Deletion Tool Forms-----#

def delete_line(request, line_number):
    line = Line.objects.get(line_number=line_number)
    if request.method == 'POST':
        line.delete()
        return redirect('success')
    return render(request, 'base/delete.html', {'obj':line})

def delete_stop(request, stop_id):
    stop = Stop.objects.get(stop_id=stop_id)
    if request.method == 'POST':
        stop.delete()
        return redirect('success')
    return render(request, 'base/delete.html', {'obj':stop})

def delete_bus(request, bus_id):
    bus = Bus.objects.get(bus_id=bus_id)
    if request.method == 'POST':
        bus.delete()
        return redirect('success')
    return render(request, 'base/delete.html', {'obj':bus})

def delete_driver(request, driver_id):
    driver = Driver.objects.get(driver_id=driver_id)
    if request.method == 'POST':
        driver.delete()
        return redirect('success')
    return render(request, 'base/delete.html', {'obj':driver})

def delete_passenger(request, passenger_id):
    passenger = Passenger.objects.get(passenger_id=passenger_id)
    if request.method == 'POST':
        passenger.delete()
        return redirect('success')
    return render(request, 'base/delete.html', {'obj':passenger})