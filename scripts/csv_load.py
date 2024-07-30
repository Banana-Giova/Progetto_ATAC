import csv

from base.models import *
from django.db.utils import IntegrityError
import os

def run():

    Passenger.objects.all().delete()
    Line.objects.all().delete()
    Stop.objects.all().delete()
    OrdinATAC.objects.all().delete()
    Bus.objects.all().delete()
    Driver.objects.all().delete()

    directory = 'scripts/data/'
    errors:int = 0
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            with open(f'scripts/data/{filename}', 'r') as f:
                reader = csv.reader(f)
                header_checked = False
                header_type = ''

                for row in reader:
                    print(row)
                    if not header_checked:
                        header_checked = True
                        if row[0] == 'passenger_id':
                            header_type = row[0]
                        elif row[0] == 'line_number':
                            header_type = row[0]
                        elif row[0] == 'stop_id':
                            header_type = row[0]
                        elif row[0] == 'bus_id':
                            header_type = row[0]
                        elif row[0] == 'driver_id':
                            header_type = row[0]
                        continue
                    try:
                        if header_type == 'passenger_id':
                            p, created = Passenger.objects.get_or_create(
                                passenger_id=row[0], name=row[1], surname=row[2])
                        if header_type == 'line_number':
                            p, created = Line.objects.get_or_create(
                                line_number=row[0], name=row[1])
                        if header_type == 'stop_id':
                            p, created = Stop.objects.get_or_create(
                                stop_id=row[0], name=row[1], latitude=row[2], longitude=row[3])
                        if header_type == 'bus_id':
                            p, created = Bus.objects.get_or_create(
                                bus_id=row[0], capacity=row[1])
                        if header_type == 'driver_id':
                            p, created = Driver.objects.get_or_create(
                                driver_id=row[0], name=row[1], surname=row[2])
                    except (IntegrityError, ValueError):
                        errors += 1
                        continue

    print(f"{errors} entries invalid!")
