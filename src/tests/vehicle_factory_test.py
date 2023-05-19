from unittest import TestCase
from carrier import Carrier
from client import Client
from item import Item

from factories.VehicleFactory import VehicleFactory


class VehicleFactoryTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(VehicleFactoryTest, self).__init__(*args, **kwargs)
        self.factory = VehicleFactory()

    def setUp(self) -> None:
        self.factory = VehicleFactory()
        self.factory.set_capacities([1, 2, 3])
        return super().setUp()

    def test_generate_vehicle_that_attends_item(self):
        item = Item(0, 0.5, 1, 0)
        client = Client(0, 50, 50)
        carrier = Carrier(0, 0, 0.9, 1, 1, 1)
        self.factory.carriers = [carrier]
        vehicle = self.factory.generate_vehicle_that_attends_item(item, client)
        self.assertEqual(vehicle.capacity, 1)
        self.assertEqual(vehicle.carrierId, carrier.index)
