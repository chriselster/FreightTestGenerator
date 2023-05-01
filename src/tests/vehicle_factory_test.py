from unittest import TestCase

from factories.VehicleFactory import VehicleFactory
from entities.Vehicle import Vehicle

class VehicleFactoryTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(VehicleFactoryTest, self).__init__(*args, **kwargs)
        self.factory = VehicleFactory()
        
    def setUp(self) -> None:
        self.factory = VehicleFactory()
        self.factory.set_capacities([1, 2, 3])
        self.factory.set_min_capacity_factors([0.8, 0.9])
        self.factory.set_cost_per_km_per_weight([0.1, 0.2])
        return super().setUp()
        
    def test_generate(self):
        vehicle = self.factory.generate(1)[0]
        self.assertIsInstance(vehicle, Vehicle)
        
    def test_set_possible_capacities(self):
        self.factory.set_capacities([1, 2, 3])
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.capacity, [1, 2, 3])
        
    def test_set_min_capacity(self):
        min_capacity_factors = [0.8, 0.9]
        self.factory.set_min_capacity_factors(min_capacity_factors)
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.min_capacity, map(lambda x: x * vehicle.capacity, min_capacity_factors))
        
    def test_set_cost_per_km_per_weight(self):
        cost_per_km_per_weight = [0.1, 0.2]
        self.factory.set_cost_per_km_per_weight(cost_per_km_per_weight)
        vehicle = self.factory.generate(1)[0]
        self.assertIn(vehicle.costPerKmPerWeight, cost_per_km_per_weight)
        