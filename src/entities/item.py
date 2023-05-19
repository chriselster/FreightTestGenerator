class Item:
    @staticmethod
    def header():
        return ["index", "weight", "type", "clientId"]

    @staticmethod
    def empty():
        return Item(0, 0, 0, 0)

    def __init__(self, index: int, weight: float, _type: int, clientId: int):
        self.index = index
        self.weight = weight
        self.type = _type
        self.clientId = clientId

    def toCSVData(self):
        return ItemCSVData.from_item(self)

    def __str__(self):
        return f"{str(self.index)},{str(self.weight)},{str(self.type)}"

    def asList(self):
        return [self.index, self.weight, self.type, self.clientId]


class ItemCSVData:
    def __init__(self, index: int, weight: float, _type: int, clientId: int):
        self.index = index
        self.weight = weight
        self.type = _type
        self.clientId = clientId

    @staticmethod
    def from_item(item: Item):
        return ItemCSVData(item.index, item.weight, item.type, item.clientId)
