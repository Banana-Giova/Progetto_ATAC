from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('success', views.success, name='success'),
    path('create', views.create, name='create'),

#Lists
    path('stops_list', views.stops_list, name='stops_list'),
    path('bus_list', views.bus_list, name='bus_list'),
    path('passengers_list', views.passengers_list, name='passengers_list'),
    path('drivers_list', views.drivers_list, name='drivers_list'),

#Detail Pages paths
    path('line/<str:line_number>', views.line, name='line'),
    path('bus/<str:bus_id>', views.bus, name='bus'),
    path('stop/<str:stop_id>', views.stop, name='stop'),
    path('passenger/<str:passenger_id>', views.passenger, name='passenger'),
    path('driver/<str:driver_id>', views.driver, name='driver'),

#Creation Tools paths
    path('create/bus', views.create_bus, name="create-bus"),
    path('create/line', views.create_line, name="create-line"),
    path('create/stop', views.create_stop, name="create-stop"),
    path('create/passenger', views.create_passenger, name="create-passenger"),
    path('create/driver', views.create_driver, name="create-driver"),

#Deletion Tools paths
    path('delete-line/<str:line_number>', views.delete_line, name='delete-line'),
    path('delete-bus/<str:bus_id>', views.delete_bus, name='delete-bus'),
    path('delete-stop/<str:stop_id>', views.delete_stop, name='delete-stop'),
    path('delete-passenger/<str:passenger_id>', views.delete_passenger, name='delete-passenger'),
    path('delete-driver/<str:driver_id>', views.delete_driver, name='delete-driver'),
]