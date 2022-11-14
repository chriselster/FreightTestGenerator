import random
from random import randint


class Veichle:
    @staticmethod
    def header():
        return ['index', 'type', 'capacity', 'carrierId']

    def __init__(self, index, type, capacity, carrierId):
        self.index = index
        self.type = type
        self.capacity = capacity
        self.carrierId = carrierId

    def __str__(self):
        return f"{str(self.index)},{str(self.type)},{str(self.capacity)},"

    def asList(self):
        return [self.index, self.type, self.capacity, self.carrierId]


class VeichleFactory:
    def __init__(self):
        self.index = 0
        self.read_params()

    def create(self, carrierId):
        veichle = Veichle(self.index, self.generate_type(),
                          self.generate_capacity(), carrierId)
        self.index += 1
        return veichle

    def generate_type(self):
        return randint(1, self.types)

    def generate_capacity(self):
        return random.choice(self.possible_capacities)

    def read_params(self):
        with open("in/veichle_params.txt", "r") as f:
            params = f.read().splitlines()
            self.types = int(self.parse_value(params[0]))
            self.possible_capacities = self.parse_value(params[1]).split(",")

    def parse_value(self, line):
        return line.split(":")[1].strip()
