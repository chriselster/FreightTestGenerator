from unittest import TestCase

from factories.CarrierFactory import CarrierFactory


class CarrierFactoryTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(CarrierFactoryTest, self).__init__(*args, **kwargs)
        self.factory = CarrierFactory()

    def setUp(self):
        self.factory.baseCosts = [1, 2, 3, 4]

    def test_set_base_costs(self):
        self.factory.setBaseCosts([1, 2, 3, 4])
        carrier = self.factory.generate(1)[0]
        self.assertIn(carrier.baseCost, [1, 2, 3, 4])

    def test_generate(self):
        carriers = self.factory.generate(2)
        self.assertEqual(len(carriers), 2)
        self.assertEqual(carriers[0].index, 0)
        self.assertEqual(carriers[1].index, 1)
