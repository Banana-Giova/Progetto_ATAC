from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bus/<int:line_number>', views.bus, name='bus'),
    path('passengers', views.passengers, name='passengers'),
]