from django.test import TestCase
from .models import *



class ModelsTestCase(TestCase):
    def setUp(self) -> None:
        Passenger.objects.create(
            passenger_id="T35T", 
            name="TESTefano", 
            surname="Bobbers"
        )
        Line.objects.create(
            line_number="053",
            name="TESTaccio"
        )
        Stop.objects.create(
            stop_id="01T35T01",
            name="TESTuggine",
            latitude=53.35,
            longitude=35.53
        )
        Bus.objects.create(
            bus_id="5353",
            capacity=53
        )
        Driver.objects.create(
            driver_id="53T5",
            name="Testio",
            surname="Lucio"
        )

    def test_info_check(self):
        
        testefano = Passenger.objects.get(passenger_id="T35T")
        testaccio = Line.objects.get(line_number="053")
        testuggine = Stop.objects.get(stop_id="01T35T01")
        cinque_tre = Bus.objects.get(bus_id="5353")
        testio = Driver.objects.get(driver_id="53T5")
        
        #Test for Passenger
        self.assertEqual(testefano.name, "TESTefano")
        self.assertEqual(testefano.surname, "Bobbers")

        #Test for Line
        self.assertEqual(testaccio.name, "TESTaccio")

        #Test for Stop
        self.assertEqual(testuggine.name, "TESTuggine")
        self.assertEqual(testuggine.latitude, 53.35)
        self.assertEqual(testuggine.longitude, 35.53)

        #Test for Bus
        self.assertEqual(cinque_tre.capacity, 53)

        #Test for Driver
        self.assertEqual(testio.name, "Testio")
        self.assertEqual(testio.surname, "Lucio")



    def test_ordinatac(self):
        testaccio = Line.objects.get(line_number="053")
        testuggine = Stop.objects.get(stop_id="01T35T01")
        ordinet = OrdinATAC.objects.create(
            line=testaccio,
            stop=testuggine
        )

        #Test for Line in an OrdinATAC
        self.assertEqual(ordinet.line.name, "TESTaccio")

        #Test for Stop in an OrdinATAC
        self.assertEqual(ordinet.stop.name, "TESTuggine")
        self.assertEqual(ordinet.stop.latitude, 53.35)
        self.assertEqual(ordinet.stop.longitude, 35.53)