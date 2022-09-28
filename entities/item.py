from random import randint, uniform


class Item:
    def __init__(self, index, weigth, type):
        self.index = index
        self.weigth = weigth
        self.type = type

    def __str__(self):
        return f"{str(self.index)},{str(self.weigth)},{str(self.type)}"


class ItemFactory:
    def __init__(self):
        self.index = 0
        self.read_params()

    def create(self):
        item = Item(self.index, self.generate_weigth(), self.generate_type())
        self.index += 1
        return item

    def generate_weigth(self):
        return round(uniform(self.min_weigth, self.max_weigth), 2)

    def generate_type(self):
        return randint(1, self.types)

    def read_params(self):
        with open("in/item_params.txt", "r") as f:
            params = f.read().splitlines()
            self.min_weigth = float(self.parse_value(params[0]))
            self.max_weigth = float(self.parse_value(params[1]))
            self.types = int(self.parse_value(params[2]))

    def parse_value(self, line):
        return line.split(":")[1].strip()
