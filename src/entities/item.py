from random import randint, uniform


class Item:
    @staticmethod
    def header():
        return ['index', 'weight', 'type', 'clientId']

    def __init__(self, index,  weight, type, clientId):
        self.index = index
        self.weight = weight  # INTEGER
        self.type = type
        self.clientId = clientId

    def __str__(self):
        return f"{str(self.index)},{str(self.weight)},{str(self.type)}"

    def asList(self):
        return [self.index, self.weight, self.type, self.clientId]


class ItemFactory:
    def __init__(self):
        self.index = 1
        self.read_params()

    def create(self, clientId):
        item = Item(self.index,
                    self.generate_weight(), self.generate_type(), clientId)
        self.index += 1
        return item

    def generate_weight(self):
        return round(uniform(self.min_weight, self.max_weight), 2)

    def generate_type(self):
        return randint(1, self.types)

    def read_params(self):
        with open("in/item_params.txt", "r") as f:
            params = f.read().splitlines()
            self.min_weight = float(self.parse_value(params[0]))
            self.max_weight = float(self.parse_value(params[1]))
            self.types = int(self.parse_value(params[2]))

    def parse_value(self, line):
        return line.split(":")[1].strip()
