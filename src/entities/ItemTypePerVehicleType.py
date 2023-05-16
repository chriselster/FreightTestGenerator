from entities.ParamReader import ParamReader


class ItemTypePerVehicleType:
    @staticmethod
    def header():
        return ["vehicleType", "itemType"]

    def __init__(self):
        self.allowedItems = {}
        self.readParams()

    def readParams(self):
        with open("in/itens_per_vehicle.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.read().splitlines())
            vehicleType = 1
            while reader.hasNext():
                items = map(int, reader.next())  # type: ignore
                self.allowedItems[vehicleType] = items
                vehicleType += 1

    def asList(self):
        for vehicleType, itemType in self.allowedItems.items():
            yield [vehicleType, itemType]
