import random

from entities.ParamReader import ParamReader


class Vehicle:
    @staticmethod
    def header():
        return ['index', 'type', 'capacity', 'carrierId']

    def __init__(self, index, _type, capacity, carrierId):
        self.index = index
        self.type = _type
        self.capacity = capacity
        self.carrierId = carrierId
        self.deadFreight = 0
        self.costPerKmPerWeight = 0

    @staticmethod
    # empty vehicle constructor
    def empty():
        return Vehicle(0, 0, 0, 0)

    def __str__(self):
        return f"{str(self.index)},{str(self.type)},{str(self.capacity)},"

    def asList(self):
        return [self.index, self.type, self.capacity, self.carrierId]


class VehicleFactory:
    def __init__(self):
        self.index = 1
        self.read_params()

    def create(self, carrierId):
        vehicle = Vehicle(self.index, self.generate_type(),
                          self.generate_capacity(), carrierId)
        self.index += 1
        return vehicle

    def generate_type(self):
        return random.choice(self.types)

    def generate_capacity(self):
        return random.choice(self.possible_capacities)

    def read_params(self):
        with open("in/vehicle_params.txt", "r", encoding="utf-8") as f:
            reader = ParamReader(f.read().splitlines())
            self.types = reader.next()
            self.possible_capacities = reader.next()

    def parse_value(self, line):
        return line.split(":")[1].strip()
