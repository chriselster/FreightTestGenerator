from unittest import TestCase
from entities.CSVGenerator import CSVGenerator
from entities.item import Item


class CSVGeneratorTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(CSVGeneratorTest, self).__init__(*args, **kwargs)
        self.generator = CSVGenerator()
        self.items = [Item(1, 1, 1, 1), Item(2, 2, 2, 2)]

    def test_generate(self):
        result = self.generator.generate(self.items)
        self.assertEqual(
            result, "index,weight,type,clientId\n1,1,1,1\n2,2,2,2\n")
