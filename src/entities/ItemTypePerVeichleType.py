

from entities.ParamReader import ParamReader


class ItemTypePerVeichleType:
    @staticmethod
    def header():
        return ["veichleType", "itemType"]

    def __init__(self):
        self.allowedItems = {}
        self.readParams()

    def readParams(self):
        with open("in/itens_per_veichle.txt", "r") as f:
            reader = ParamReader(f.read().splitlines())
            veichleType = 1
            while reader.hasNext():
                items = map(int, reader.next())  # type: ignore
                self.allowedItems[veichleType] = items
                veichleType += 1

    def asList(self):
        for veichleType in self.allowedItems:
            for itemType in self.allowedItems[veichleType]:
                yield [veichleType, itemType]
