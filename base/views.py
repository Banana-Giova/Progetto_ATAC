from django.shortcuts import render, redirect
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from .models import *
from .forms import *



#-----Basic Pages-----#

def home(request):
    bus_lines = Line.objects.all()
    context = {'bus_lines': bus_lines}
    return render(request, "base/home.html", context)

def success(request):
    return render(request, 'base/success.html')

def create(request):
    return render(request, 'base/create.html')

def scioperi(request):
    return render(request, 'base/extra_stuff/scioperi.html')



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
    drivers_list = Driver.objects.all()
    context = {'drivers_list':drivers_list}
    return render(request, "base/lists/drivers_list.html", context)



#-----Detail Pages-----#

def line(request, line_number):
    req_line = Line.objects.get(line_number=line_number)
    ordinatac = OrdinATAC.objects.all()
    livetratac = LiveTrATAC.objects.all()
    context = {'line':req_line, 'ordinatac':ordinatac, 'livetratac': livetratac}
    return render(request, "base/details/line.html", context)

def bus(request, bus_id):
    req_bus = Bus.objects.get(bus_id=bus_id)
    livetratac = LiveTrATAC.objects.all()
    context = {'bus': req_bus, 'livetratac': livetratac}
    return render(request, "base/details/bus.html", context)

def stop(request, stop_id):
    req_stop = Stop.objects.get(stop_id=stop_id)
    ordinatac = OrdinATAC.objects.all()
    context = {'stop':req_stop, 'ordinatac':ordinatac}
    return render(request, "base/details/stop.html", context)

def passenger(request, passenger_id):
    req_passenger = Passenger.objects.get(passenger_id=passenger_id)
    context = {'passenger':req_passenger}
    return render(request, "base/details/passenger.html", context)

def driver(request, driver_id):
    req_driver = Driver.objects.get(driver_id=driver_id)
    multidriver = MultiDriver.objects.all()
    context = {'driver':req_driver, 'multidriver': multidriver}
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



#-----Assignment Tool Forms-----#

def passenger_on_bus(request, bus_id):
    bus = get_object_or_404(Bus, bus_id=bus_id)
    
    if request.method == 'POST':
        form = PassengerOnBus(request.POST, instance=bus)
        if form.is_valid():
            passengers = form.cleaned_data['passengers']
            bus.passengers.set(passengers)  
            bus.save()
            return redirect('success')
    else:
        form = PassengerOnBus(instance=bus)
    
    context = {'form': form, 'bus': bus}
    return render(request, 'base/forms/passenger_on_bus.html', context)

def ordinatac(request):
    form = OrdinATACForm()
    if request.method == 'POST':
        form = OrdinATACForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/ordinatac_form.html', context)

def livetratac(request):
    form = LiveTrATACForm()
    if request.method == 'POST':
        form = LiveTrATACForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/livetratac_form.html', context)

def multidriver(request):
    form = MultiDriverForm()
    if request.method == 'POST':
        form = MultiDriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    context = {'form': form}
    return render(request, 'base/forms/multidriver_form.html', context)



#-----Search-----#

def search(request):
    search = request.GET.get('search') if request.GET.get('search') != None else ''

    passengers = list(Passenger.objects.filter(Q(passenger_id__icontains=search)|Q(name__icontains=search)|Q(surname__icontains=search)))
    lines = list(Line.objects.filter(Q(line_number__icontains=search)|Q(name__icontains=search)))
    stops = list(Stop.objects.filter(Q(stop_id__icontains=search)|Q(name__icontains=search)))
    buses = list(Bus.objects.filter(Q(bus_id__icontains=search)))
    drivers = list(Driver.objects.filter(Q(driver_id__icontains=search)|Q(name__icontains=search)|Q(surname__icontains=search)))

    context = {
        'passengers': passengers,
        'lines': lines,
        'stops': stops,
        'buses': buses,
        'drivers': drivers
        }
    return render(request, 'base/search.html', context) 

def stats(request):
    passenger_no = Passenger.objects.count()
    line_no = Line.objects.count()
    stop_no = Stop.objects.count()
    bus_no = Bus.objects.count()
    driver_no = Driver.objects.count()

    context = {
        'passenger_no': passenger_no,
        'line_no': line_no,
        'stop_no': stop_no,
        'bus_no': bus_no,
        'driver_no': driver_no
    }
    return render(request, 'base/stats.html', context)


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



#-----Unassignment Tool Forms-----#

def remove_bus_from_driver(request, driver_id):
    driver = get_object_or_404(Driver, pk=driver_id)
    multidriver = MultiDriver.objects.filter(driver=driver)
    multidriver.delete()
    return redirect("success")