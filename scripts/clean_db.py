from base.models import *
from django.db.utils import IntegrityError

def run():

    Passenger.objects.all().delete()
    Line.objects.all().delete()
    Stop.objects.all().delete()
    OrdinATAC.objects.all().delete()
    Bus.objects.all().delete()
    Driver.objects.all().delete()