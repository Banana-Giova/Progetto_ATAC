from base.models import *
from django.db.utils import IntegrityError
import time


timed = time.time()

def run():

    print("Cleaning your database...")

    Passenger.objects.all().delete()
    Line.objects.all().delete()
    Stop.objects.all().delete()
    Bus.objects.all().delete()
    Driver.objects.all().delete()

    OrdinATAC.objects.all().delete()
    LiveTrATAC.objects.all().delete()
    MultiDriver.objects.all().delete()

    elapsed = time.time() - timed
    print(f"Database cleaned in {elapsed}s!")