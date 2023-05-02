from unittest import TestCase

from factories.VehicleFactory import VehicleFactory
from entities.vehicle import Vehicle


class VehicleFactoryTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(VehicleFactoryTest, self).__init__(*args, **kwargs)
        self.factory = VehicleFactory()

    def setUp(self) -> None:
        self.factory = VehicleFactory()
        self.factory.set_capacities([1, 2, 3])
        self.factory.set_min_capacity_factors([0.8, 0.9])
        self.factory.set_cost_per_km_per_weight([0.1, 0.2])
        self.factory.set_additional_delivery_costs([0.1, 0.2])
        self.factory.set_max_distance_between_customers([10, 20])
        self.factory.set_carrier_id(1)
        self.factory.set_possible_types([1, 2, 3])
        return super().setUp()

    def test_generate(self):
        vehicles = self.factory.generate(2)
        self.assertEqual(len(vehicles), 2)
        self.assertIsInstance(vehicles[0], Vehicle)
        self.assertEqual(vehicles[0].index, 0)
        self.assertEqual(vehicles[1].index, 1)

    def test_set_possible_types(self):
        self.factory.set_possible_types([1, 2, 3])
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.type, [1, 2, 3])

    def test_set_possible_capacities(self):
        self.factory.set_capacities([1, 2, 3])
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.capacity, [1, 2, 3])

    def test_set_min_capacity(self):
        min_capacity_factors = [0.8, 0.9]
        self.factory.set_min_capacity_factors(min_capacity_factors)
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.min_capacity, map(
            lambda x: x * vehicle.capacity, min_capacity_factors))

    def test_set_cost_per_km_per_weight(self):
        cost_per_km_per_weight = [0.1, 0.2]
        self.factory.set_cost_per_km_per_weight(cost_per_km_per_weight)
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.costPerKmPerWeight, cost_per_km_per_weight)

    def test_set_additional_delivery_cost(self):
        self.factory.set_additional_delivery_costs([0.1, 0.2])
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.additionalDeliveryCost, [0.1, 0.2])

    def test_max_distance_between_customers(self):
        self.factory.set_max_distance_between_customers([10, 20])
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.maxDistanceBetweenCustomers, [10, 20])

    def test_set_carrier_id(self):
        self.factory.set_carrier_id(1)
        vehicle = self.factory.generate(1)[0]
        self.assertEqual(vehicle.carrierId, 1)
