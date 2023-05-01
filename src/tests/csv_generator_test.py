from unittest import TestCase

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


class CSVGenerator:
    def generate(self, aClassList):
        return self.generate_header(aClassList) + self.generate_datarows(aClassList)

    def generate_header(self, aClassList):
        # Get class attributes
        aClass = aClassList[0]
        return ",".join(aClass.__dict__) + "\n"

    def generate_datarows(self, aClassList):
        return "".join([self.generate_datarow(aClass) for aClass in aClassList])

    def generate_datarow(self, aClass):
        return ",".join([str(attr) for attr in aClass.__dict__.values()]) + "\n"
