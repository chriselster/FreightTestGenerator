from unittest import TestCase

from factories.CarrierFactory import CarrierFactory


class CarrierFactoryTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(CarrierFactoryTest, self).__init__(*args, **kwargs)
        self.factory = CarrierFactory()

    def setUp(self):
        self.factory.baseCosts = [1, 2, 3, 4]
        self.factory.quadrants = [[1, 2], [3, 4]]
        self.factory.minimalContractedLoadPercentages = [0.5, 0.6]
        self.factory.costsPerAdditionalCustomer = [1, 2]
        self.factory.maxDistanceBetweenCustomers = [80, 90]
        self.factory.discountsPerCapacityIncrease = [0.5, 0.6]

    def test_generate(self):
        carriers = self.factory.generate(2)
        self.assertEqual(len(carriers), 2)
        self.assertEqual(carriers[0].index, 0)
        self.assertEqual(carriers[1].index, 1)

    def test_set_quadrants(self):
        self.factory.setQuadrants([[1, 2], [3, 4]])
        carriers = self.factory.generate(2)
        self.assertEqual(carriers[0].quadrants, [1, 2])
        self.assertEqual(carriers[1].quadrants, [3, 4])

    def test_set_minimal_contracted_load_percentage(self):
        self.factory.setMinimalContractedLoadPercentages([0.5, 0.6])
        carrier = self.factory.generate(1)[0]
        self.assertIn(carrier.minimalContractedLoadPercentage, [0.5, 0.6])

    def test_set_cost_per_additional_customer(self):
        self.factory.setCostsPerAdditionalCustomer([1, 2])
        carrier = self.factory.generate(1)[0]
        self.assertIn(carrier.costPerAdditionalCustomer, [1, 2])

    def test_set_max_distance_between_customers(self):
        self.factory.setMaxDistanceBetweenCustomers([80, 90])
        carrier = self.factory.generate(1)[0]
        self.assertIn(carrier.maxDistanceBetweenCustomers, [80, 90])

    def test_set_discount_per_capacity_increase(self):
        self.factory.setDiscountPerCapacityIncrease([0.2, 0.3])
        carrier = self.factory.generate(1)[0]
        self.assertIn(carrier.discountPerCapacityIncrease, [0.2, 0.3])

    def test_set_base_costs(self):
        self.factory.setBaseCosts([1, 2, 3, 4])
        carrier = self.factory.generate(1)[0]
        self.assertIn(carrier.baseCost, [1, 2, 3, 4])
