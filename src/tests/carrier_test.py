from unittest import TestCase

from entities.carrier import Carrier
from entities.vehicle import Vehicle


class CarrierTest(TestCase):
    def testAddVehicle(self):
        carrier = Carrier(0, 0, 0.2, 50, 0.5, 20)
        carrier.add_accepted_types([1, 2])
        carrier.add_vehicle_capacities([50, 100])
        carrier.add_fare(1, 2)
        carrier.add_fare(2, 2)

        vehicle = Vehicle.empty()
        carrier.add_vehicle(vehicle)
        assert vehicle.type in [1, 2]
        assert vehicle.capacity in [50, 100]
        self.assertEqual(vehicle.deadFreight, 0.2*vehicle.capacity)
        self.assertEqual(vehicle.costPerKmPerWeight, 2 -
                         (0 if vehicle.capacity == 50 else 0.5))
        self.assertEqual(vehicle.carrierId, carrier.id)
